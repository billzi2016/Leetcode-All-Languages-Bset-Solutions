# 0744. Find Smallest Letter Greater Than Target

## Cpp

```cpp
class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int n = letters.size();
        int low = 0, high = n;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (letters[mid] <= target)
                low = mid + 1;
            else
                high = mid;
        }
        return letters[low % n];
    }
};
```

## Java

```java
class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int n = letters.length;
        int lo = 0, hi = n - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (letters[mid] <= target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return letters[lo % n];
    }
}
```

## Python

```python
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        n = len(letters)
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if letters[mid] <= target:
                lo = mid + 1
            else:
                hi = mid - 1
        return letters[lo % n]
```

## Python3

```python
from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return letters[left % len(letters)]
```

## C

```c
char nextGreatestLetter(char* letters, int lettersSize, char target) {
    int low = 0, high = lettersSize;
    while (low < high) {
        int mid = low + (high - low) / 2;
        if (letters[mid] <= target)
            low = mid + 1;
        else
            high = mid;
    }
    return letters[low % lettersSize];
}
```

## Csharp

```csharp
public class Solution
{
    public char NextGreatestLetter(char[] letters, char target)
    {
        int left = 0;
        int right = letters.Length - 1;

        while (left <= right)
        {
            int mid = left + ((right - left) >> 1);
            if (letters[mid] <= target)
                left = mid + 1;
            else
                right = mid - 1;
        }

        return letters[left % letters.Length];
    }
}
```

## Javascript

```javascript
/**
 * @param {character[]} letters
 * @param {character} target
 * @return {character}
 */
var nextGreatestLetter = function(letters, target) {
    let left = 0, right = letters.length;
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (letters[mid] <= target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return letters[left % letters.length];
};
```

## Typescript

```typescript
function nextGreatestLetter(letters: string[], target: string): string {
    let left = 0;
    let right = letters.length;
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (letters[mid] <= target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left === letters.length ? letters[0] : letters[left];
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $letters
     * @param String $target
     * @return String
     */
    function nextGreatestLetter($letters, $target) {
        $n = count($letters);
        $low = 0;
        $high = $n - 1;
        while ($low <= $high) {
            $mid = intdiv($low + $high, 2);
            if ($letters[$mid] <= $target) {
                $low = $mid + 1;
            } else {
                $high = $mid - 1;
            }
        }
        return $letters[$low % $n];
    }
}
```

## Swift

```swift
class Solution {
    func nextGreatestLetter(_ letters: [Character], _ target: Character) -> Character {
        var left = 0
        var right = letters.count
        while left < right {
            let mid = (left + right) / 2
            if letters[mid] <= target {
                left = mid + 1
            } else {
                right = mid
            }
        }
        return left == letters.count ? letters[0] : letters[left]
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun nextGreatestLetter(letters: CharArray, target: Char): Char {
        var left = 0
        var right = letters.size - 1
        while (left <= right) {
            val mid = left + (right - left) / 2
            if (letters[mid] <= target) {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
        return if (left < letters.size) letters[left] else letters[0]
    }
}
```

## Dart

```dart
class Solution {
  String nextGreatestLetter(List<String> letters, String target) {
    int n = letters.length;
    int left = 0, right = n - 1;
    while (left < right) {
      int mid = left + ((right - left) >> 1);
      if (letters[mid].compareTo(target) <= 0) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    return letters[left].compareTo(target) > 0 ? letters[left] : letters[0];
  }
}
```

## Golang

```go
func nextGreatestLetter(letters []byte, target byte) byte {
    left, right := 0, len(letters)
    for left < right {
        mid := (left + right) / 2
        if letters[mid] <= target {
            left = mid + 1
        } else {
            right = mid
        }
    }
    if left == len(letters) {
        return letters[0]
    }
    return letters[left]
}
```

## Ruby

```ruby
def next_greatest_letter(letters, target)
  left = 0
  right = letters.length - 1
  while left <= right
    mid = (left + right) / 2
    if letters[mid] <= target
      left = mid + 1
    else
      right = mid - 1
    end
  end
  letters[left % letters.length]
end
```

## Scala

```scala
object Solution {
    def nextGreatestLetter(letters: Array[Char], target: Char): Char = {
        var lo = 0
        var hi = letters.length - 1
        while (lo <= hi) {
            val mid = lo + (hi - lo) / 2
            if (letters(mid) <= target) lo = mid + 1
            else hi = mid - 1
        }
        if (lo < letters.length) letters(lo) else letters(0)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn next_greatest_letter(letters: Vec<char>, target: char) -> char {
        let n = letters.len();
        let mut left = 0usize;
        let mut right = n;
        while left < right {
            let mid = (left + right) / 2;
            if letters[mid] <= target {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        if left == n { letters[0] } else { letters[left] }
    }
}
```

## Racket

```racket
(define/contract (next-greatest-letter letters target)
  (-> (listof char?) char? char?)
  (let* ((vec (list->vector letters))
         (n (vector-length vec)))
    (let loop ((low 0) (high (sub1 n)) (ans #\null))
      (if (> low high)
          (if (char=? ans #\null)
              (vector-ref vec 0)
              ans)
          (let* ((mid (quotient (+ low high) 2))
                 (mid-char (vector-ref vec mid)))
            (if (char<? target mid-char) ; mid-char > target
                (loop low (sub1 mid) mid-char)
                (loop (add1 mid) high ans)))))))
```

## Erlang

```erlang
-spec next_greatest_letter(Letters :: [char()], Target :: char()) -> char().
next_greatest_letter(Letters, Target) ->
    Len = length(Letters),
    Tuple = list_to_tuple(Letters),
    binary_search(Tuple, Len, Target).

binary_search(Tuple, Len, Target) ->
    search(0, Len - 1, Tuple, Len, Target).

search(Low, High, Tuple, Len, Target) when Low =< High ->
    Mid = (Low + High) div 2,
    Char = element(Mid + 1, Tuple),
    if
        Char =< Target ->
            search(Mid + 1, High, Tuple, Len, Target);
        true ->
            search(Low, Mid - 1, Tuple, Len, Target)
    end;
search(Low, _High, Tuple, Len, _Target) ->
    if
        Low >= Len -> element(1, Tuple);
        true       -> element(Low + 1, Tuple)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec next_greatest_letter(letters :: [char], target :: char) :: char
  def next_greatest_letter(letters, target) do
    len = length(letters)
    idx = bs(letters, target, 0, len - 1, len)
    Enum.at(letters, idx)
  end

  defp bs(_list, _target, low, high, len) when low > high,
    do: rem(low, len)

  defp bs(list, target, low, high, len) do
    mid = div(low + high, 2)
    val = Enum.at(list, mid)

    if val <= target do
      bs(list, target, mid + 1, high, len)
    else
      bs(list, target, low, mid - 1, len)
    end
  end
end
```
