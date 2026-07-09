# 2283. Check if Number Has Equal Digit Count and Digit Value

## Cpp

```cpp
class Solution {
public:
    bool digitCount(string num) {
        int freq[10] = {0};
        for (char c : num) {
            freq[c - '0']++;
        }
        int n = num.size();
        for (int i = 0; i < n; ++i) {
            if (freq[i] != num[i] - '0')
                return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean digitCount(String num) {
        int[] freq = new int[10];
        for (int i = 0; i < num.length(); i++) {
            freq[num.charAt(i) - '0']++;
        }
        for (int i = 0; i < num.length(); i++) {
            int expected = num.charAt(i) - '0';
            if (freq[i] != expected) {
                return false;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        freq = [0] * 10
        for ch in num:
            freq[ord(ch) - ord('0')] += 1
        for i, ch in enumerate(num):
            if int(ch) != freq[i]:
                return False
        return True
```

## Python3

```python
class Solution:
    def digitCount(self, num: str) -> bool:
        freq = [0] * 10
        for ch in num:
            freq[int(ch)] += 1
        for i, ch in enumerate(num):
            if freq[i] != int(ch):
                return False
        return True
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool digitCount(char* num) {
    int freq[10] = {0};
    int n = strlen(num);
    for (int i = 0; i < n; ++i) {
        int d = num[i] - '0';
        if (d >= 0 && d < 10) {
            freq[d]++;
        }
    }
    for (int i = 0; i < n; ++i) {
        int expected = num[i] - '0';
        if (freq[i] != expected) {
            return false;
        }
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool DigitCount(string num) {
        int[] count = new int[10];
        foreach (char c in num) {
            count[c - '0']++;
        }
        for (int i = 0; i < num.Length; i++) {
            int expected = num[i] - '0';
            if (count[i] != expected) return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} num
 * @return {boolean}
 */
var digitCount = function(num) {
    const cnt = new Array(10).fill(0);
    for (let ch of num) {
        cnt[ch.charCodeAt(0) - 48]++; // '0' char code is 48
    }
    for (let i = 0; i < num.length; ++i) {
        const expected = num.charCodeAt(i) - 48;
        if (cnt[i] !== expected) return false;
    }
    return true;
};
```

## Typescript

```typescript
function digitCount(num: string): boolean {
    const count = new Array(10).fill(0);
    for (const ch of num) {
        count[ch.charCodeAt(0) - 48]++;
    }
    for (let i = 0; i < num.length; i++) {
        const expected = num.charCodeAt(i) - 48;
        if (count[i] !== expected) return false;
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param String $num
     * @return Boolean
     */
    function digitCount($num) {
        $freq = array_fill(0, 10, 0);
        $len = strlen($num);
        for ($i = 0; $i < $len; $i++) {
            $digit = intval($num[$i]);
            $freq[$digit]++;
        }
        for ($i = 0; $i < $len; $i++) {
            $expected = intval($num[$i]);
            if ($freq[$i] !== $expected) {
                return false;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func digitCount(_ num: String) -> Bool {
        var freq = Array(repeating: 0, count: 10)
        for ch in num {
            if let v = ch.wholeNumberValue {
                freq[v] += 1
            }
        }
        let chars = Array(num)
        for i in 0..<chars.count {
            let expected = chars[i].wholeNumberValue ?? 0
            if freq[i] != expected {
                return false
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun digitCount(num: String): Boolean {
        val cnt = IntArray(10)
        for (c in num) {
            cnt[c - '0']++
        }
        for (i in num.indices) {
            if (cnt[i] != (num[i] - '0')) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool digitCount(String num) {
    List<int> cnt = List.filled(10, 0);
    for (int i = 0; i < num.length; i++) {
      int d = num.codeUnitAt(i) - 48;
      cnt[d]++;
    }
    for (int i = 0; i < num.length; i++) {
      int expected = num.codeUnitAt(i) - 48;
      if (cnt[i] != expected) return false;
    }
    return true;
  }
}
```

## Golang

```go
func digitCount(num string) bool {
    cnt := [10]int{}
    for _, ch := range num {
        cnt[ch-'0']++
    }
    for i := 0; i < len(num); i++ {
        expected := int(num[i] - '0')
        if cnt[i] != expected {
            return false
        }
    }
    return true
}
```

## Ruby

```ruby
def digit_count(num)
  freq = Array.new(10, 0)
  num.each_char { |c| freq[c.to_i] += 1 }
  num.chars.each_with_index do |ch, i|
    return false if freq[i] != ch.to_i
  end
  true
end
```

## Scala

```scala
object Solution {
    def digitCount(num: String): Boolean = {
        val freq = new Array[Int](10)
        for (c <- num) {
            freq(c - '0') += 1
        }
        for (i <- 0 until num.length) {
            if (freq(i) != (num.charAt(i) - '0')) return false
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn digit_count(num: String) -> bool {
        let bytes = num.as_bytes();
        let mut cnt = [0usize; 10];
        for &b in bytes {
            cnt[(b - b'0') as usize] += 1;
        }
        for i in 0..bytes.len() {
            if cnt[i] != (bytes[i] - b'0') as usize {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (digit-count num)
  (-> string? boolean?)
  (let* ((len (string-length num))
         (counts (make-vector 10 0)))
    ;; Count frequency of each digit in the string
    (for ([c (in-string num)])
      (let ((d (- (char->integer c) (char->integer #\0))))
        (when (and (>= d 0) (< d 10))
          (vector-set! counts d (+ (vector-ref counts d) 1)))))
    ;; Verify the condition for each index
    (let loop ((i 0))
      (if (= i len)
          #t
          (let* ((c (string-ref num i))
                 (expected (- (char->integer c) (char->integer #\0)))
                 (actual (vector-ref counts i))) ; count of digit i
            (if (= expected actual)
                (loop (+ i 1))
                #f))))))
```

## Erlang

```erlang
-spec digit_count(Num :: unicode:unicode_binary()) -> boolean().
digit_count(Num) ->
    Len = byte_size(Num),
    List = binary_to_list(Num),
    CountMap = lists:foldl(
        fun(C, Acc) ->
            case maps:is_key(C, Acc) of
                true -> maps:update(C, fun(V) -> V + 1 end, Acc);
                false -> maps:put(C, 1, Acc)
            end
        end,
        #{},
        List),
    check(0, Len, List, CountMap).

check(Index, Len, _List, _CountMap) when Index >= Len ->
    true;
check(Index, Len, List, CountMap) ->
    ExpectedChar = lists:nth(Index + 1, List),
    ExpectedCount = ExpectedChar - $0,
    DigitChar = $0 + Index,
    ActualCount = maps:get(DigitChar, CountMap, 0),
    if
        ExpectedCount =:= ActualCount -> check(Index + 1, Len, List, CountMap);
        true -> false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec digit_count(num :: String.t()) :: boolean()
  def digit_count(num) do
    freqs = num |> String.graphemes() |> Enum.frequencies()
    len = String.length(num)

    0..(len - 1)
    |> Enum.all?(fn i ->
      expected = String.at(num, i) |> String.to_integer()
      actual = Map.get(freqs, Integer.to_string(i), 0)
      expected == actual
    end)
  end
end
```
