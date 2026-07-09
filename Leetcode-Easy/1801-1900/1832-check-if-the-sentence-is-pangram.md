# 1832. Check if the Sentence Is Pangram

## Cpp

```cpp
class Solution {
public:
    bool checkIfPangram(string sentence) {
        int mask = 0;
        for (char c : sentence) {
            mask |= 1 << (c - 'a');
        }
        return mask == ((1 << 26) - 1);
    }
};
```

## Java

```java
class Solution {
    public boolean checkIfPangram(String sentence) {
        int mask = 0;
        int fullMask = (1 << 26) - 1; // all 26 bits set
        for (int i = 0; i < sentence.length(); i++) {
            mask |= 1 << (sentence.charAt(i) - 'a');
            if (mask == fullMask) return true;
        }
        return mask == fullMask;
    }
}
```

## Python

```python
class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        return len(set(sentence)) == 26
```

## Python3

```python
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
```

## C

```c
#include <stdbool.h>

bool checkIfPangram(char* sentence) {
    unsigned int mask = 0;
    for (; *sentence; ++sentence) {
        mask |= 1u << (*sentence - 'a');
    }
    return mask == ((1u << 26) - 1);
}
```

## Csharp

```csharp
public class Solution {
    public bool CheckIfPangram(string sentence) {
        int mask = 0;
        const int fullMask = (1 << 26) - 1;
        foreach (char c in sentence) {
            mask |= 1 << (c - 'a');
            if (mask == fullMask) return true;
        }
        return mask == fullMask;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} sentence
 * @return {boolean}
 */
var checkIfPangram = function(sentence) {
    const seen = new Set();
    for (let i = 0; i < sentence.length; i++) {
        seen.add(sentence.charCodeAt(i) - 97);
        if (seen.size === 26) return true;
    }
    return false;
};
```

## Typescript

```typescript
function checkIfPangram(sentence: string): boolean {
    const seen = new Set<string>();
    for (const ch of sentence) {
        seen.add(ch);
        if (seen.size === 26) return true;
    }
    return false;
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param String $sentence
     * @return Boolean
     */
    function checkIfPangram($sentence) {
        $mask = 0;
        $len = strlen($sentence);
        for ($i = 0; $i < $len; $i++) {
            $idx = ord($sentence[$i]) - 97;
            if ($idx >= 0 && $idx < 26) {
                $mask |= (1 << $idx);
                if ($mask == 67108863) { // all 26 bits set
                    return true;
                }
            }
        }
        return $mask == 67108863;
    }
}
?>
```

## Swift

```swift
class Solution {
    func checkIfPangram(_ sentence: String) -> Bool {
        var seen = [Bool](repeating: false, count: 26)
        for ch in sentence.utf8 {
            let idx = Int(ch - 97) // 'a' ascii is 97
            if idx >= 0 && idx < 26 {
                seen[idx] = true
            }
        }
        return !seen.contains(false)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkIfPangram(sentence: String): Boolean {
        val seen = BooleanArray(26)
        var count = 0
        for (ch in sentence) {
            val idx = ch - 'a'
            if (!seen[idx]) {
                seen[idx] = true
                count++
                if (count == 26) return true
            }
        }
        return count == 26
    }
}
```

## Dart

```dart
class Solution {
  bool checkIfPangram(String sentence) {
    final seen = List<bool>.filled(26, false);
    int count = 0;
    for (int i = 0; i < sentence.length; i++) {
      int idx = sentence.codeUnitAt(i) - 97;
      if (!seen[idx]) {
        seen[idx] = true;
        count++;
        if (count == 26) return true;
      }
    }
    return false;
  }
}
```

## Golang

```go
func checkIfPangram(sentence string) bool {
	const fullMask uint32 = 1<<26 - 1
	var mask uint32
	for i := 0; i < len(sentence); i++ {
		mask |= 1 << (sentence[i] - 'a')
		if mask == fullMask {
			return true
		}
	}
	return mask == fullMask
}
```

## Ruby

```ruby
def check_if_pangram(sentence)
  seen = Array.new(26, false)
  count = 0
  sentence.each_byte do |b|
    idx = b - 97
    unless seen[idx]
      seen[idx] = true
      count += 1
      return true if count == 26
    end
  end
  false
end
```

## Scala

```scala
object Solution {
    def checkIfPangram(sentence: String): Boolean = {
        val seen = new Array[Boolean](26)
        var count = 0
        for (ch <- sentence) {
            val idx = ch - 'a'
            if (!seen(idx)) {
                seen(idx) = true
                count += 1
                if (count == 26) return true
            }
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_if_pangram(sentence: String) -> bool {
        let mut mask: u32 = 0;
        for b in sentence.bytes() {
            let idx = (b - b'a') as u32;
            mask |= 1 << idx;
        }
        mask == (1u32 << 26) - 1
    }
}
```

## Racket

```racket
(define/contract (check-if-pangram sentence)
  (-> string? boolean?)
  (let* ((target (sub1 (arithmetic-shift 1 26))))
    (let loop ((i 0) (mask 0))
      (if (= i (string-length sentence))
          (= mask target)
          (let* ((c (string-ref sentence i))
                 (pos (- (char->integer c) (char->integer #\a))))
            (loop (+ i 1) (bitwise-ior mask (arithmetic-shift 1 pos))))))))
```

## Erlang

```erlang
-module(solution).
-export([check_if_pangram/1]).

-spec check_if_pangram(Sentence :: unicode:unicode_binary()) -> boolean().
check_if_pangram(Sentence) ->
    Mask = fold_mask(binary_to_list(Sentence), 0),
    Mask == ((1 bsl 26) - 1).

fold_mask([], Acc) -> Acc;
fold_mask([C|Rest], Acc) ->
    Bit = C - $a,
    NewAcc = Acc bor (1 bsl Bit),
    fold_mask(Rest, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec check_if_pangram(sentence :: String.t()) :: boolean()
  def check_if_pangram(sentence) do
    import Bitwise

    mask =
      sentence
      |> String.to_charlist()
      |> Enum.reduce(0, fn char, acc ->
        if char >= ?a and char <= ?z do
          acc ||| (1 <<< (char - ?a))
        else
          acc
        end
      end)

    mask == ((1 <<< 26) - 1)
  end
end
```
