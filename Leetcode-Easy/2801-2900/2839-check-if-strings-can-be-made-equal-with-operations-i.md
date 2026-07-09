# 2839. Check if Strings Can be Made Equal With Operations I

## Cpp

```cpp
class Solution {
public:
    bool canBeEqual(string s1, string s2) {
        string even1 = {s1[0], s1[2]};
        string odd1  = {s1[1], s1[3]};
        string even2 = {s2[0], s2[2]};
        string odd2  = {s2[1], s2[3]};
        sort(even1.begin(), even1.end());
        sort(even2.begin(), even2.end());
        sort(odd1.begin(), odd1.end());
        sort(odd2.begin(), odd2.end());
        return even1 == even2 && odd1 == odd2;
    }
};
```

## Java

```java
class Solution {
    public boolean canBeEqual(String s1, String s2) {
        char[] even1 = {s1.charAt(0), s1.charAt(2)};
        char[] odd1 = {s1.charAt(1), s1.charAt(3)};
        char[] even2 = {s2.charAt(0), s2.charAt(2)};
        char[] odd2 = {s2.charAt(1), s2.charAt(3)};
        java.util.Arrays.sort(even1);
        java.util.Arrays.sort(odd1);
        java.util.Arrays.sort(even2);
        java.util.Arrays.sort(odd2);
        return java.util.Arrays.equals(even1, even2) && java.util.Arrays.equals(odd1, odd2);
    }
}
```

## Python

```python
class Solution(object):
    def canBeEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Compare characters at even indices and odd indices separately
        return (sorted(s1[0::2]) == sorted(s2[0::2])) and (sorted(s1[1::2]) == sorted(s2[1::2]))
```

## Python3

```python
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return (sorted(s1[0::2]) == sorted(s2[0::2]) and
                sorted(s1[1::2]) == sorted(s2[1::2]))
```

## C

```c
#include <stdbool.h>

bool canBeEqual(char* s1, char* s2) {
    int even[26] = {0}, odd[26] = {0};
    for (int i = 0; i < 4; ++i) {
        if (i % 2 == 0) {
            even[s1[i] - 'a']++;
            even[s2[i] - 'a']--;
        } else {
            odd[s1[i] - 'a']++;
            odd[s2[i] - 'a']--;
        }
    }
    for (int i = 0; i < 26; ++i) {
        if (even[i] != 0 || odd[i] != 0)
            return false;
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool CanBeEqual(string s1, string s2) {
        char[] e1 = new char[] { s1[0], s1[2] };
        char[] o1 = new char[] { s1[1], s1[3] };
        char[] e2 = new char[] { s2[0], s2[2] };
        char[] o2 = new char[] { s2[1], s2[3] };
        Array.Sort(e1);
        Array.Sort(o1);
        Array.Sort(e2);
        Array.Sort(o2);
        return e1[0] == e2[0] && e1[1] == e2[1] &&
               o1[0] == o2[0] && o1[1] == o2[1];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var canBeEqual = function(s1, s2) {
    const even1 = [s1[0], s1[2]].sort().join('');
    const even2 = [s2[0], s2[2]].sort().join('');
    if (even1 !== even2) return false;
    
    const odd1 = [s1[1], s1[3]].sort().join('');
    const odd2 = [s2[1], s2[3]].sort().join('');
    return odd1 === odd2;
};
```

## Typescript

```typescript
function canBeEqual(s1: string, s2: string): boolean {
    const even1 = [s1[0], s1[2]].sort().join('');
    const even2 = [s2[0], s2[2]].sort().join('');
    const odd1 = [s1[1], s1[3]].sort().join('');
    const odd2 = [s2[1], s2[3]].sort().join('');
    return even1 === even2 && odd1 === odd2;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @return Boolean
     */
    function canBeEqual($s1, $s2) {
        // Collect characters at even indices (0 and 2)
        $even1 = [$s1[0], $s1[2]];
        $even2 = [$s2[0], $s2[2]];
        // Collect characters at odd indices (1 and 3)
        $odd1 = [$s1[1], $s1[3]];
        $odd2 = [$s2[1], $s2[3]];

        sort($even1);
        sort($even2);
        sort($odd1);
        sort($odd2);

        return $even1 === $even2 && $odd1 === $odd2;
    }
}
```

## Swift

```swift
class Solution {
    func canBeEqual(_ s1: String, _ s2: String) -> Bool {
        let a1 = Array(s1)
        let a2 = Array(s2)
        var even1: [Character] = []
        var odd1:  [Character] = []
        var even2: [Character] = []
        var odd2:  [Character] = []
        
        for i in 0..<4 {
            if i % 2 == 0 {
                even1.append(a1[i])
                even2.append(a2[i])
            } else {
                odd1.append(a1[i])
                odd2.append(a2[i])
            }
        }
        
        even1.sort()
        even2.sort()
        odd1.sort()
        odd2.sort()
        
        return even1 == even2 && odd1 == odd2
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canBeEqual(s1: String, s2: String): Boolean {
        val ev1 = CharArray(2)
        val od1 = CharArray(2)
        val ev2 = CharArray(2)
        val od2 = CharArray(2)
        var eIdx = 0
        var oIdx = 0
        for (i in 0 until 4) {
            if (i % 2 == 0) {
                ev1[eIdx++] = s1[i]
            } else {
                od1[oIdx++] = s1[i]
            }
        }
        eIdx = 0
        oIdx = 0
        for (i in 0 until 4) {
            if (i % 2 == 0) {
                ev2[eIdx++] = s2[i]
            } else {
                od2[oIdx++] = s2[i]
            }
        }
        ev1.sort()
        ev2.sort()
        od1.sort()
        od2.sort()
        return ev1.contentEquals(ev2) && od1.contentEquals(od2)
    }
}
```

## Dart

```dart
class Solution {
  bool canBeEqual(String s1, String s2) {
    List<String> even1 = [], odd1 = [];
    List<String> even2 = [], odd2 = [];

    for (int i = 0; i < 4; i++) {
      if (i % 2 == 0) {
        even1.add(s1[i]);
        even2.add(s2[i]);
      } else {
        odd1.add(s1[i]);
        odd2.add(s2[i]);
      }
    }

    even1.sort();
    even2.sort();
    odd1.sort();
    odd2.sort();

    for (int i = 0; i < 2; i++) {
      if (even1[i] != even2[i] || odd1[i] != odd2[i]) return false;
    }
    return true;
  }
}
```

## Golang

```go
import "sort"

func canBeEqual(s1 string, s2 string) bool {
	ev1 := []byte{s1[0], s1[2]}
	ev2 := []byte{s2[0], s2[2]}
	od1 := []byte{s1[1], s1[3]}
	od2 := []byte{s2[1], s2[3]}

	sort.Slice(ev1, func(i, j int) bool { return ev1[i] < ev1[j] })
	sort.Slice(ev2, func(i, j int) bool { return ev2[i] < ev2[j] })
	sort.Slice(od1, func(i, j int) bool { return od1[i] < od1[j] })
	sort.Slice(od2, func(i, j int) bool { return od2[i] < od2[j] })

	return string(ev1) == string(ev2) && string(od1) == string(od2)
}
```

## Ruby

```ruby
def can_be_equal(s1, s2)
  ev1 = []
  od1 = []
  ev2 = []
  od2 = []

  s1.chars.each_with_index do |c, i|
    (i.even? ? ev1 : od1) << c
  end

  s2.chars.each_with_index do |c, i|
    (i.even? ? ev2 : od2) << c
  end

  ev1.sort == ev2.sort && od1.sort == od2.sort
end
```

## Scala

```scala
object Solution {
    def canBeEqual(s1: String, s2: String): Boolean = {
        val even1 = new scala.collection.mutable.ArrayBuffer[Char]()
        val odd1  = new scala.collection.mutable.ArrayBuffer[Char]()
        val even2 = new scala.collection.mutable.ArrayBuffer[Char]()
        val odd2  = new scala.collection.mutable.ArrayBuffer[Char]()

        for (i <- s1.indices) {
            if ((i & 1) == 0) {
                even1 += s1(i)
                even2 += s2(i)
            } else {
                odd1 += s1(i)
                odd2 += s2(i)
            }
        }

        even1.sorted == even2.sorted && odd1.sorted == odd2.sorted
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_be_equal(s1: String, s2: String) -> bool {
        let b1 = s1.as_bytes();
        let b2 = s2.as_bytes();

        // even indices (0 and 2)
        let mut ev1 = [b1[0], b1[2]];
        let mut ev2 = [b2[0], b2[2]];
        ev1.sort_unstable();
        ev2.sort_unstable();
        if ev1 != ev2 {
            return false;
        }

        // odd indices (1 and 3)
        let mut od1 = [b1[1], b1[3]];
        let mut od2 = [b2[1], b2[3]];
        od1.sort_unstable();
        od2.sort_unstable();

        od1 == od2
    }
}
```

## Racket

```racket
(define/contract (can-be-equal s1 s2)
  (-> string? string? boolean?)
  (let* ([sorted1 (list->string (sort (string->list s1) char<?))]
         [sorted2 (list->string (sort (string->list s2) char<?))])
    (string=? sorted1 sorted2)))
```

## Erlang

```erlang
-spec can_be_equal(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> boolean().
can_be_equal(S1, S2) ->
    Even1 = [binary:at(S1, 0), binary:at(S1, 2)],
    Odd1  = [binary:at(S1, 1), binary:at(S1, 3)],
    Even2 = [binary:at(S2, 0), binary:at(S2, 2)],
    Odd2  = [binary:at(S2, 1), binary:at(S2, 3)],
    lists:sort(Even1) == lists:sort(Even2) andalso
    lists:sort(Odd1)  == lists:sort(Odd2).
```

## Elixir

```elixir
defmodule Solution do
  @spec can_be_equal(s1 :: String.t(), s2 :: String.t()) :: boolean()
  def can_be_equal(s1, s2) do
    {e1, o1} = split_parity(s1)
    {e2, o2} = split_parity(s2)

    Enum.sort(e1) == Enum.sort(e2) and Enum.sort(o1) == Enum.sort(o2)
  end

  defp split_parity(str) do
    chars = String.graphemes(str)

    Enum.reduce(Enum.with_index(chars), {[], []}, fn {ch, idx}, {evens, odds} ->
      if rem(idx, 2) == 0 do
        {[ch | evens], odds}
      else
        {evens, [ch | odds]}
      end
    end)
  end
end
```
