# 2405. Optimal Partition of String

## Cpp

```cpp
class Solution {
public:
    int partitionString(string s) {
        int partitions = 0;
        bool seen[26] = {false};
        for (char c : s) {
            int idx = c - 'a';
            if (seen[idx]) {
                ++partitions;
                memset(seen, 0, sizeof(seen));
            }
            seen[idx] = true;
        }
        return partitions + 1; // account for the last substring
    }
};
```

## Java

```java
class Solution {
    public int partitionString(String s) {
        int partitions = 1;
        boolean[] seen = new boolean[26];
        for (int i = 0; i < s.length(); i++) {
            int idx = s.charAt(i) - 'a';
            if (seen[idx]) {
                partitions++;
                java.util.Arrays.fill(seen, false);
            }
            seen[idx] = true;
        }
        return partitions;
    }
}
```

## Python

```python
class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        seen = set()
        for ch in s:
            if ch in seen:
                count += 1
                seen.clear()
            seen.add(ch)
        # add the last substring if any characters were processed
        return count + (1 if seen else 0)
```

## Python3

```python
class Solution:
    def partitionString(self, s: str) -> int:
        substrings = 1
        seen = set()
        for ch in s:
            if ch in seen:
                substrings += 1
                seen.clear()
            seen.add(ch)
        return substrings
```

## C

```c
int partitionString(char* s) {
    if (!s || !*s) return 0;
    int cnt = 1;
    int mask = 0;
    for (int i = 0; s[i]; ++i) {
        int bit = 1 << (s[i] - 'a');
        if (mask & bit) {
            ++cnt;
            mask = 0;
        }
        mask |= bit;
    }
    return cnt;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int PartitionString(string s) {
        var seen = new HashSet<char>();
        int partitions = 1;
        foreach (char c in s) {
            if (!seen.Add(c)) {
                partitions++;
                seen.Clear();
                seen.Add(c);
            }
        }
        return partitions;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var partitionString = function(s) {
    let partitions = 1;
    const seen = new Set();
    for (const ch of s) {
        if (seen.has(ch)) {
            partitions++;
            seen.clear();
        }
        seen.add(ch);
    }
    return partitions;
};
```

## Typescript

```typescript
function partitionString(s: string): number {
    const seen = new Set<string>();
    let count = 1;
    for (const ch of s) {
        if (seen.has(ch)) {
            count++;
            seen.clear();
        }
        seen.add(ch);
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function partitionString($s) {
        $len = strlen($s);
        $count = 1; // at least one substring
        $set = [];

        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if (isset($set[$c])) {
                $count++;
                $set = [];
            }
            $set[$c] = true;
        }

        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func partitionString(_ s: String) -> Int {
        var seen = Set<Character>()
        var partitions = 1
        for ch in s {
            if seen.contains(ch) {
                partitions += 1
                seen.removeAll()
            }
            seen.insert(ch)
        }
        return partitions
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun partitionString(s: String): Int {
        var partitions = 1
        val seen = HashSet<Char>()
        for (ch in s) {
            if (!seen.add(ch)) {
                partitions++
                seen.clear()
                seen.add(ch)
            }
        }
        return partitions
    }
}
```

## Dart

```dart
class Solution {
  int partitionString(String s) {
    Set<int> seen = {};
    int partitions = 1;
    for (int i = 0; i < s.length; i++) {
      int ch = s.codeUnitAt(i);
      if (seen.contains(ch)) {
        partitions++;
        seen.clear();
      }
      seen.add(ch);
    }
    return partitions;
  }
}
```

## Golang

```go
func partitionString(s string) int {
    count := 1
    mask := 0
    for i := 0; i < len(s); i++ {
        b := s[i] - 'a'
        bit := 1 << b
        if mask&bit != 0 {
            count++
            mask = 0
        }
        mask |= bit
    }
    return count
}
```

## Ruby

```ruby
def partition_string(s)
  count = 1
  mask = 0
  s.each_byte do |b|
    bit = 1 << (b - 97)
    if (mask & bit) != 0
      count += 1
      mask = 0
    end
    mask |= bit
  end
  count
end
```

## Scala

```scala
object Solution {
    def partitionString(s: String): Int = {
        var partitions = 1
        val seen = scala.collection.mutable.HashSet[Char]()
        for (c <- s) {
            if (seen.contains(c)) {
                partitions += 1
                seen.clear()
            }
            seen.add(c)
        }
        partitions
    }
}
```

## Rust

```rust
impl Solution {
    pub fn partition_string(s: String) -> i32 {
        use std::collections::HashSet;
        let mut seen = HashSet::new();
        let mut parts = 1;
        for ch in s.chars() {
            if seen.contains(&ch) {
                parts += 1;
                seen.clear();
            }
            seen.insert(ch);
        }
        parts
    }
}
```

## Racket

```racket
(define/contract (partition-string s)
  (-> string? exact-integer?)
  (let* ((n (string-length s)))
    (let loop ((i 0) (count 1) (vec (make-vector 26 #f)))
      (if (= i n)
          count
          (let* ((ch (string-ref s i))
                 (idx (- (char->integer ch) (char->integer #\a))))
            (if (vector-ref vec idx)
                (let ((new-vec (make-vector 26 #f)))
                  (vector-set! new-vec idx #t)
                  (loop (+ i 1) (+ count 1) new-vec))
                (begin
                  (vector-set! vec idx #t)
                  (loop (+ i 1) count vec))))))))
```

## Erlang

```erlang
-spec partition_string(unicode:unicode_binary()) -> integer().
partition_string(S) ->
    partition_string_binary(S, 0, 0).

partition_string_binary(<<>>, Count, _Mask) ->
    Count + 1;
partition_string_binary(<<Char:8, Rest/binary>>, Count, Mask) ->
    Index = Char - $a,
    Bit = 1 bsl Index,
    case (Mask band Bit) of
        0 -> partition_string_binary(Rest, Count, Mask bor Bit);
        _ -> partition_string_binary(Rest, Count + 1, Bit)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec partition_string(s :: String.t()) :: integer()
  def partition_string(s) do
    {count, _set} =
      Enum.reduce(String.to_charlist(s), {1, MapSet.new()}, fn char, {cnt, set} ->
        if MapSet.member?(set, char) do
          {cnt + 1, MapSet.put(MapSet.new(), char)}
        else
          {cnt, MapSet.put(set, char)}
        end
      end)

    count
  end
end
```
