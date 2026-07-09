# 2937. Make Three Strings Equal

## Cpp

```cpp
class Solution {
public:
    int findMinimumOperations(string s1, string s2, string s3) {
        int n1 = s1.size(), n2 = s2.size(), n3 = s3.size();
        int limit = min({n1, n2, n3});
        int common = 0;
        while (common < limit && s1[common] == s2[common] && s1[common] == s3[common]) {
            ++common;
        }
        if (common == 0) return -1; // cannot make them equal without emptying
        return (n1 - common) + (n2 - common) + (n3 - common);
    }
};
```

## Java

```java
class Solution {
    public int findMinimumOperations(String s1, String s2, String s3) {
        int minLen = Math.min(s1.length(), Math.min(s2.length(), s3.length()));
        int lcp = 0;
        while (lcp < minLen &&
               s1.charAt(lcp) == s2.charAt(lcp) &&
               s1.charAt(lcp) == s3.charAt(lcp)) {
            lcp++;
        }
        if (lcp == 0) return -1;
        return (s1.length() - lcp) + (s2.length() - lcp) + (s3.length() - lcp);
    }
}
```

## Python

```python
class Solution(object):
    def findMinimumOperations(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: int
        """
        # Find longest common prefix length among the three strings
        min_len = min(len(s1), len(s2), len(s3))
        lcp = 0
        while lcp < min_len and s1[lcp] == s2[lcp] == s3[lcp]:
            lcp += 1

        if lcp == 0:
            return -1

        # Total deletions needed to reduce each string to the common prefix
        return (len(s1) - lcp) + (len(s2) - lcp) + (len(s3) - lcp)
```

## Python3

```python
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        # Find longest common prefix length among the three strings
        max_len = min(len(s1), len(s2), len(s3))
        lcp = 0
        while lcp < max_len and s1[lcp] == s2[lcp] == s3[lcp]:
            lcp += 1
        if lcp == 0:
            return -1
        return (len(s1) - lcp) + (len(s2) - lcp) + (len(s3) - lcp)
```

## C

```c
#include <string.h>

int findMinimumOperations(char* s1, char* s2, char* s3) {
    int len1 = (int)strlen(s1);
    int len2 = (int)strlen(s2);
    int len3 = (int)strlen(s3);
    
    int minLen = len1;
    if (len2 < minLen) minLen = len2;
    if (len3 < minLen) minLen = len3;
    
    int common = 0;
    while (common < minLen && s1[common] == s2[common] && s1[common] == s3[common]) {
        ++common;
    }
    
    if (common == 0) return -1; // cannot make them equal without emptying
    
    int totalOps = (len1 - common) + (len2 - common) + (len3 - common);
    return totalOps;
}
```

## Csharp

```csharp
public class Solution {
    public int FindMinimumOperations(string s1, string s2, string s3) {
        int n1 = s1.Length, n2 = s2.Length, n3 = s3.Length;
        int minLen = Math.Min(n1, Math.Min(n2, n3));
        int common = 0;
        for (int i = 0; i < minLen; i++) {
            char c = s1[i];
            if (c == s2[i] && c == s3[i]) {
                common++;
            } else {
                break;
            }
        }
        if (common == 0) return -1;
        return (n1 - common) + (n2 - common) + (n3 - common);
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} s3
 * @return {number}
 */
var findMinimumOperations = function(s1, s2, s3) {
    const minLen = Math.min(s1.length, s2.length, s3.length);
    let common = 0;
    while (common < minLen &&
           s1[common] === s2[common] &&
           s1[common] === s3[common]) {
        common++;
    }
    if (common === 0) return -1; // cannot make non‑empty equal strings
    return (s1.length - common) + (s2.length - common) + (s3.length - common);
};
```

## Typescript

```typescript
function findMinimumOperations(s1: string, s2: string, s3: string): number {
    const minLen = Math.min(s1.length, s2.length, s3.length);
    let lcp = 0;
    while (lcp < minLen && s1[lcp] === s2[lcp] && s1[lcp] === s3[lcp]) {
        lcp++;
    }
    if (lcp === 0) return -1;
    return (s1.length - lcp) + (s2.length - lcp) + (s3.length - lcp);
}
```

## Php

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @param String $s3
     * @return Integer
     */
    function findMinimumOperations($s1, $s2, $s3) {
        $len1 = strlen($s1);
        $len2 = strlen($s2);
        $len3 = strlen($s3);
        $minLen = min($len1, $len2, $len3);
        $common = 0;
        while ($common < $minLen && $s1[$common] === $s2[$common] && $s1[$common] === $s3[$common]) {
            $common++;
        }
        if ($common == 0) {
            return -1;
        }
        return ($len1 - $common) + ($len2 - $common) + ($len3 - $common);
    }
}
```

## Swift

```swift
class Solution {
    func findMinimumOperations(_ s1: String, _ s2: String, _ s3: String) -> Int {
        let chars1 = Array(s1)
        let chars2 = Array(s2)
        let chars3 = Array(s3)
        let minLen = min(chars1.count, chars2.count, chars3.count)
        var lcp = 0
        while lcp < minLen {
            let c = chars1[lcp]
            if c == chars2[lcp] && c == chars3[lcp] {
                lcp += 1
            } else {
                break
            }
        }
        if lcp == 0 { return -1 }
        return s1.count + s2.count + s3.count - 3 * lcp
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMinimumOperations(s1: String, s2: String, s3: String): Int {
        val minLen = minOf(s1.length, s2.length, s3.length)
        var lcp = 0
        while (lcp < minLen && s1[lcp] == s2[lcp] && s1[lcp] == s3[lcp]) {
            lcp++
        }
        if (lcp == 0) return -1
        return (s1.length - lcp) + (s2.length - lcp) + (s3.length - lcp)
    }
}
```

## Dart

```dart
class Solution {
  int findMinimumOperations(String s1, String s2, String s3) {
    int minLen = [s1.length, s2.length, s3.length].reduce((a, b) => a < b ? a : b);
    int l = 0;
    while (l < minLen &&
        s1.codeUnitAt(l) == s2.codeUnitAt(l) &&
        s1.codeUnitAt(l) == s3.codeUnitAt(l)) {
      l++;
    }
    if (l == 0) return -1;
    return (s1.length - l) + (s2.length - l) + (s3.length - l);
  }
}
```

## Golang

```go
func findMinimumOperations(s1 string, s2 string, s3 string) int {
    n1, n2, n3 := len(s1), len(s2), len(s3)
    minLen := n1
    if n2 < minLen {
        minLen = n2
    }
    if n3 < minLen {
        minLen = n3
    }

    lcp := 0
    for i := 0; i < minLen; i++ {
        if s1[i] == s2[i] && s2[i] == s3[i] {
            lcp++
        } else {
            break
        }
    }

    if lcp == 0 {
        return -1
    }
    return (n1 + n2 + n3) - 3*lcp
}
```

## Ruby

```ruby
def find_minimum_operations(s1, s2, s3)
  min_len = [s1.length, s2.length, s3.length].min
  l = 0
  while l < min_len && s1[l] == s2[l] && s1[l] == s3[l]
    l += 1
  end
  return -1 if l == 0
  (s1.length - l) + (s2.length - l) + (s3.length - l)
end
```

## Scala

```scala
object Solution {
    def findMinimumOperations(s1: String, s2: String, s3: String): Int = {
        val minLen = math.min(s1.length, math.min(s2.length, s3.length))
        var lcp = 0
        while (lcp < minLen && s1(lcp) == s2(lcp) && s1(lcp) == s3(lcp)) {
            lcp += 1
        }
        if (lcp == 0) -1 else (s1.length - lcp) + (s2.length - lcp) + (s3.length - lcp)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_minimum_operations(s1: String, s2: String, s3: String) -> i32 {
        let b1 = s1.as_bytes();
        let b2 = s2.as_bytes();
        let b3 = s3.as_bytes();

        let min_len = *[b1.len(), b2.len(), b3.len()].iter().min().unwrap();
        let mut common = 0;
        while common < min_len
            && b1[common] == b2[common]
            && b1[common] == b3[common]
        {
            common += 1;
        }

        if common == 0 {
            -1
        } else {
            (b1.len() + b2.len() + b3.len() - 3 * common) as i32
        }
    }
}
```

## Racket

```racket
(define/contract (find-minimum-operations s1 s2 s3)
  (-> string? string? string? exact-integer?)
  (let* ((len1 (string-length s1))
         (len2 (string-length s2))
         (len3 (string-length s3))
         (minlen (apply min (list len1 len2 len3)))
         (lcp
          (let loop ((i 0))
            (if (= i minlen)
                i
                (let ((c1 (string-ref s1 i))
                      (c2 (string-ref s2 i))
                      (c3 (string-ref s3 i)))
                  (if (and (char=? c1 c2) (char=? c1 c3))
                      (loop (+ i 1))
                      i))))))
    (if (= lcp 0)
        -1
        (+ (- len1 lcp) (- len2 lcp) (- len3 lcp)))))
```

## Erlang

```erlang
-spec find_minimum_operations(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary(), S3 :: unicode:unicode_binary()) -> integer().
find_minimum_operations(S1, S2, S3) ->
    L1 = binary_to_list(S1),
    L2 = binary_to_list(S2),
    L3 = binary_to_list(S3),
    PrefixLen = common_prefix_len(L1, L2, L3),
    case PrefixLen of
        0 -> -1;
        _ ->
            Len1 = length(L1),
            Len2 = length(L2),
            Len3 = length(L3),
            (Len1 + Len2 + Len3) - 3 * PrefixLen
    end.

common_prefix_len(L1, L2, L3) ->
    cp(L1, L2, L3, 0).

cp([H|T1], [H|T2], [H|T3], Acc) ->
    cp(T1, T2, T3, Acc + 1);
cp(_, _, _, Acc) ->
    Acc.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_minimum_operations(String.t(), String.t(), String.t()) :: integer()
  def find_minimum_operations(s1, s2, s3) do
    l1 = String.length(s1)
    l2 = String.length(s2)
    l3 = String.length(s3)

    min_len = Enum.min([l1, l2, l3])

    common =
      0..(min_len - 1)
      |> Enum.reduce_while(0, fn i, acc ->
        c1 = :binary.at(s1, i)
        c2 = :binary.at(s2, i)
        c3 = :binary.at(s3, i)

        if c1 == c2 and c2 == c3 do
          {:cont, acc + 1}
        else
          {:halt, acc}
        end
      end)

    if common == 0 do
      -1
    else
      (l1 - common) + (l2 - common) + (l3 - common)
    end
  end
end
```
