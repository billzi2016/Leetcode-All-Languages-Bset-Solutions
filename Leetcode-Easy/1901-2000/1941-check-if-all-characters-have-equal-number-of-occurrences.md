# 1941. Check if All Characters Have Equal Number of Occurrences

## Cpp

```cpp
class Solution {
public:
    bool areOccurrencesEqual(string s) {
        int cnt[26] = {0};
        for (char c : s) ++cnt[c - 'a'];
        int target = 0;
        for (int i = 0; i < 26; ++i) {
            if (cnt[i] > 0) {
                if (target == 0) target = cnt[i];
                else if (cnt[i] != target) return false;
            }
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean areOccurrencesEqual(String s) {
        int[] freq = new int[26];
        for (int i = 0; i < s.length(); i++) {
            freq[s.charAt(i) - 'a']++;
        }
        int target = -1;
        for (int f : freq) {
            if (f == 0) continue;
            if (target == -1) {
                target = f;
            } else if (f != target) {
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
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        # All frequencies must be the same
        return len(set(freq.values())) == 1
```

## Python3

```python
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import Counter
        freq = Counter(s)
        return len(set(freq.values())) == 1
```

## C

```c
#include <stdbool.h>

bool areOccurrencesEqual(char* s) {
    int freq[26] = {0};
    for (int i = 0; s[i]; ++i) {
        freq[s[i] - 'a']++;
    }
    int target = -1;
    for (int i = 0; i < 26; ++i) {
        if (freq[i] > 0) {
            if (target == -1) {
                target = freq[i];
            } else if (freq[i] != target) {
                return false;
            }
        }
    }
    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool AreOccurrencesEqual(string s)
    {
        int[] freq = new int[26];
        foreach (char c in s)
        {
            freq[c - 'a']++;
        }

        int target = 0;
        foreach (int count in freq)
        {
            if (count > 0)
            {
                target = count;
                break;
            }
        }

        foreach (int count in freq)
        {
            if (count > 0 && count != target)
                return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var areOccurrencesEqual = function(s) {
    const freq = new Array(26).fill(0);
    for (let i = 0; i < s.length; ++i) {
        freq[s.charCodeAt(i) - 97]++;
    }
    let target = -1;
    for (let count of freq) {
        if (count === 0) continue;
        if (target === -1) {
            target = count;
        } else if (count !== target) {
            return false;
        }
    }
    return true;
};
```

## Typescript

```typescript
function areOccurrencesEqual(s: string): boolean {
    const freq = new Array(26).fill(0);
    for (const ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }
    let target = -1;
    for (const count of freq) {
        if (count === 0) continue;
        if (target === -1) {
            target = count;
        } else if (count !== target) {
            return false;
        }
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function areOccurrencesEqual($s) {
        $freq = [];
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $ch = $s[$i];
            if (isset($freq[$ch])) {
                $freq[$ch]++;
            } else {
                $freq[$ch] = 1;
            }
        }

        $counts = array_values($freq);
        $first = $counts[0];
        foreach ($counts as $c) {
            if ($c !== $first) {
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
    func areOccurrencesEqual(_ s: String) -> Bool {
        var freq = [Character: Int]()
        for ch in s {
            freq[ch, default: 0] += 1
        }
        guard let firstCount = freq.values.first else { return true }
        for count in freq.values {
            if count != firstCount {
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
    fun areOccurrencesEqual(s: String): Boolean {
        val freq = IntArray(26)
        for (ch in s) {
            freq[ch - 'a']++
        }
        var target = 0
        for (cnt in freq) {
            if (cnt > 0) {
                target = cnt
                break
            }
        }
        for (cnt in freq) {
            if (cnt > 0 && cnt != target) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool areOccurrencesEqual(String s) {
    List<int> cnt = List.filled(26, 0);
    for (int i = 0; i < s.length; ++i) {
      cnt[s.codeUnitAt(i) - 97]++;
    }
    int? target;
    for (int c in cnt) {
      if (c > 0) {
        if (target == null) {
          target = c;
        } else if (c != target) {
          return false;
        }
      }
    }
    return true;
  }
}
```

## Golang

```go
func areOccurrencesEqual(s string) bool {
    var cnt [26]int
    for _, ch := range s {
        cnt[ch-'a']++
    }
    target := -1
    for _, c := range cnt {
        if c == 0 {
            continue
        }
        if target == -1 {
            target = c
        } else if c != target {
            return false
        }
    }
    return true
}
```

## Ruby

```ruby
def are_occurrences_equal(s)
  freq = Hash.new(0)
  s.each_char { |c| freq[c] += 1 }
  freq.values.uniq.length == 1
end
```

## Scala

```scala
object Solution {
    def areOccurrencesEqual(s: String): Boolean = {
        val freq = new Array[Int](26)
        for (c <- s) {
            freq(c - 'a') += 1
        }
        var target = -1
        for (f <- freq if f > 0) {
            if (target == -1) target = f
            else if (f != target) return false
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn are_occurrences_equal(s: String) -> bool {
        let mut cnt = [0usize; 26];
        for b in s.bytes() {
            cnt[(b - b'a') as usize] += 1;
        }
        let mut expected = None;
        for &c in cnt.iter() {
            if c == 0 {
                continue;
            }
            match expected {
                None => expected = Some(c),
                Some(v) => {
                    if v != c {
                        return false;
                    }
                }
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (are-occurrences-equal s)
  (-> string? boolean?)
  (let* ((len (string-length s))
         (freq (make-vector 26 0)))
    (for ([i (in-range len)])
      (let* ((ch (string-ref s i))
             (idx (- (char->integer ch) (char->integer #\a))))
        (vector-set! freq idx (+ 1 (vector-ref freq idx)))))
    (let loop ((i 0) (target #f))
      (cond
        [(= i 26) #t]
        [else
         (define cnt (vector-ref freq i))
         (if (= cnt 0)
             (loop (+ i 1) target)
             (if (not target)
                 (loop (+ i 1) cnt)
                 (and (= cnt target) (loop (+ i 1) target))))]))))
```

## Erlang

```erlang
-spec are_occurrences_equal(S :: unicode:unicode_binary()) -> boolean().
are_occurrences_equal(S) ->
    CountMap = count_chars(S, #{}),
    Values = maps:values(CountMap),
    case Values of
        [] -> true;
        [First|Rest] ->
            lists:all(fun(V) -> V =:= First end, Rest)
    end.

count_chars(<<>>, Acc) -> Acc;
count_chars(<<Char, Rest/binary>>, Acc) ->
    NewAcc = maps:update_with(Char,
                              fun(Cnt) -> Cnt + 1 end,
                              1,
                              Acc),
    count_chars(Rest, NewAcc).
```

## Elixir

```elixir
defmodule Solution do
  @spec are_occurrences_equal(s :: String.t) :: boolean
  def are_occurrences_equal(s) do
    freqs =
      s
      |> String.graphemes()
      |> Enum.reduce(%{}, fn ch, acc ->
        Map.update(acc, ch, 1, &(&1 + 1))
      end)

    case Map.values(freqs) do
      [] -> true
      [first | rest] -> Enum.all?(rest, fn v -> v == first end)
    end
  end
end
```
