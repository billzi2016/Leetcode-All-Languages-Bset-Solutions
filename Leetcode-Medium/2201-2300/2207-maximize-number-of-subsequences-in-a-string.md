# 2207. Maximize Number of Subsequences in a String

## Cpp

```cpp
class Solution {
public:
    long long maximumSubsequenceCount(string text, string pattern) {
        char a = pattern[0], b = pattern[1];
        if (a == b) {
            long long cnt = 0;
            for (char c : text) if (c == a) ++cnt;
            return (cnt + 1) * cnt / 2;
        }
        long long totalA = 0, totalB = 0;
        for (char c : text) {
            if (c == a) ++totalA;
            else if (c == b) ++totalB;
        }
        long long base = 0, curA = 0;
        for (char c : text) {
            if (c == a) ++curA;
            else if (c == b) base += curA;
        }
        return base + max(totalA, totalB);
    }
};
```

## Java

```java
class Solution {
    public long maximumSubsequenceCount(String text, String pattern) {
        char a = pattern.charAt(0);
        char b = pattern.charAt(1);
        if (a == b) {
            long cnt = 0;
            for (int i = 0; i < text.length(); ++i) {
                if (text.charAt(i) == a) cnt++;
            }
            long base = cnt * (cnt - 1) / 2;
            return base + cnt;
        } else {
            long totalA = 0, totalB = 0, base = 0;
            for (int i = 0; i < text.length(); ++i) {
                char c = text.charAt(i);
                if (c == a) totalA++;
                else if (c == b) totalB++;
            }
            long suffixB = 0;
            for (int i = text.length() - 1; i >= 0; --i) {
                char c = text.charAt(i);
                if (c == b) {
                    suffixB++;
                } else if (c == a) {
                    base += suffixB;
                }
            }
            long added = Math.max(totalA, totalB);
            return base + added;
        }
    }
}
```

## Python

```python
class Solution(object):
    def maximumSubsequenceCount(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: int
        """
        a, b = pattern[0], pattern[1]
        if a == b:
            cnt = text.count(a)
            # after adding one more 'a', total pairs become C(cnt+1, 2)
            return cnt * (cnt + 1) // 2

        cnt_a = 0
        base = 0
        for ch in text:
            if ch == a:
                cnt_a += 1
            elif ch == b:
                base += cnt_a

        total_a = text.count(a)
        total_b = text.count(b)

        # Adding 'a' yields extra subsequences equal to total number of 'b's
        # Adding 'b' yields extra subsequences equal to total number of 'a's
        return base + max(total_b, total_a)
```

## Python3

```python
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        p0, p1 = pattern[0], pattern[1]
        if p0 == p1:
            cnt = text.count(p0)
            base = cnt * (cnt - 1) // 2
            return base + cnt
        # count occurrences of each character
        cnt_p0 = cnt_p1 = 0
        for ch in text:
            if ch == p0:
                cnt_p0 += 1
            elif ch == p1:
                cnt_p1 += 1
        # compute existing subsequences where pattern[0] appears before pattern[1]
        base = 0
        seen_p0 = 0
        for ch in text:
            if ch == p0:
                seen_p0 += 1
            elif ch == p1:
                base += seen_p0
        # best extra by inserting p0 at the beginning (all p1 after) or p1 at the end (all p0 before)
        extra = max(cnt_p1, cnt_p0)
        return base + extra
```

## C

```c
long long maximumSubsequenceCount(char* text, char* pattern) {
    char a = pattern[0];
    char b = pattern[1];
    if (a == b) {
        long long cnt = 0;
        for (int i = 0; text[i]; ++i)
            if (text[i] == a) ++cnt;
        long long base = cnt * (cnt - 1) / 2;
        return base + cnt;
    } else {
        long long cntA = 0, cntB = 0;
        long long base = 0;
        for (int i = 0; text[i]; ++i) {
            char c = text[i];
            if (c == a) {
                ++cntA;
            } else if (c == b) {
                base += cntA;
                ++cntB;
            }
        }
        long long incAddA = cntB; // adding pattern[0]
        long long incAddB = cntA; // adding pattern[1]
        return base + (incAddA > incAddB ? incAddA : incAddB);
    }
}
```

## Csharp

```csharp
public class Solution
{
    public long MaximumSubsequenceCount(string text, string pattern)
    {
        char a = pattern[0];
        char b = pattern[1];

        // Case when both characters are the same
        if (a == b)
        {
            long cnt = 0;
            foreach (char ch in text)
                if (ch == a) cnt++;

            long baseCount = cnt * (cnt - 1) / 2; // existing subsequences
            return baseCount + cnt;               // adding one more character adds 'cnt' new subsequences
        }

        // Count existing subsequences of pattern in the original text
        long baseCount = 0;
        long countASeen = 0;
        foreach (char ch in text)
        {
            if (ch == a)
                countASeen++;
            else if (ch == b)
                baseCount += countASeen;
        }

        // Maximum increase by inserting 'a' (pattern[0])
        long totalB = 0;
        foreach (char ch in text)
            if (ch == b) totalB++;

        long remainingB = totalB;
        long maxAddA = 0; // best suffix count of 'b'
        for (int i = 0; i <= text.Length; i++)
        {
            if (remainingB > maxAddA) maxAddA = remainingB;
            if (i < text.Length && text[i] == b) remainingB--;
        }

        // Maximum increase by inserting 'b' (pattern[1])
        long seenA = 0;
        long maxAddB = 0; // best prefix count of 'a'
        for (int i = 0; i <= text.Length; i++)
        {
            if (seenA > maxAddB) maxAddB = seenA;
            if (i < text.Length && text[i] == a) seenA++;
        }

        long bestIncrease = maxAddA > maxAddB ? maxAddA : maxAddB;
        return baseCount + bestIncrease;
    }
}
```

## Javascript

```javascript
var maximumSubsequenceCount = function(text, pattern) {
    const a = pattern[0];
    const b = pattern[1];
    let totalA = 0;
    let totalB = 0;
    let base = 0;
    for (let i = 0; i < text.length; ++i) {
        const ch = text[i];
        if (ch === b) {
            base += totalA;
            totalB++;
        }
        if (ch === a) {
            totalA++;
        }
    }
    return base + Math.max(totalA, totalB);
};
```

## Typescript

```typescript
function maximumSubsequenceCount(text: string, pattern: string): number {
    const first = pattern[0];
    const second = pattern[1];
    let seenFirst = 0;
    let base = 0;
    let cntFirst = 0;
    let cntSecond = 0;

    for (const ch of text) {
        if (ch === first) cntFirst++;
        if (ch === second) cntSecond++;

        if (ch === second) {
            base += seenFirst;
        }
        if (ch === first) {
            seenFirst++;
        }
    }

    const add = Math.max(cntFirst, cntSecond);
    return base + add;
}
```

## Php

```php
class Solution {
    /**
     * @param String $text
     * @param String $pattern
     * @return Integer
     */
    function maximumSubsequenceCount($text, $pattern) {
        $a = $pattern[0];
        $b = $pattern[1];
        $len = strlen($text);
        $totalA = 0;
        $totalB = 0;
        for ($i = 0; $i < $len; $i++) {
            $ch = $text[$i];
            if ($ch === $a) $totalA++;
            if ($ch === $b) $totalB++;
        }
        if ($a === $b) {
            // number of pairs in original string
            $base = intdiv($totalA * ($totalA - 1), 2);
            // adding one more same character creates 'totalA' new subsequences
            return $base + $totalA;
        } else {
            $base = 0;
            $cntASeen = 0;
            for ($i = 0; $i < $len; $i++) {
                $ch = $text[$i];
                if ($ch === $a) {
                    $cntASeen++;
                } elseif ($ch === $b) {
                    $base += $cntASeen;
                }
            }
            // Insert pattern[0] to get all existing pattern[1] after it
            $addA = $base + $totalB;
            // Insert pattern[1] to get all existing pattern[0] before it
            $addB = $base + $totalA;
            return max($addA, $addB);
        }
    }
}
```

## Swift

```swift
class Solution {
    func maximumSubsequenceCount(_ text: String, _ pattern: String) -> Int {
        let p = Array(pattern)
        let first = p[0]
        let second = p[1]
        let chars = Array(text)
        
        if first == second {
            var cnt = 0
            for ch in chars {
                if ch == first { cnt += 1 }
            }
            // existing subsequences: C(cnt,2)
            let base = cnt * (cnt - 1) / 2
            // adding one more same character creates 'cnt' new pairs
            return base + cnt
        } else {
            var countFirstSoFar = 0          // number of first seen so far while scanning
            var totalSubseq = 0              // existing pattern subsequences
            var totalFirst = 0               // total occurrences of first in whole text
            var totalSecond = 0              // total occurrences of second in whole text
            
            for ch in chars {
                if ch == first {
                    countFirstSoFar += 1
                    totalFirst += 1
                } else if ch == second {
                    totalSubseq += countFirstSoFar
                    totalSecond += 1
                }
            }
            
            // If we insert 'first', it can pair with every existing 'second'
            let addIfInsertFirst = totalSecond
            // If we insert 'second', it can pair with every existing 'first'
            let addIfInsertSecond = totalFirst
            
            return totalSubseq + max(addIfInsertFirst, addIfInsertSecond)
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumSubsequenceCount(text: String, pattern: String): Long {
        val a = pattern[0]
        val b = pattern[1]
        return if (a == b) {
            var cnt = 0L
            for (ch in text) {
                if (ch == a) cnt++
            }
            val base = cnt * (cnt - 1) / 2
            base + cnt
        } else {
            var totalA = 0L
            var totalB = 0L
            var countFirst = 0L
            var base = 0L
            for (ch in text) {
                if (ch == a) {
                    totalA++
                    countFirst++
                } else if (ch == b) {
                    totalB++
                    base += countFirst
                }
            }
            val extraAddA = totalB   // add pattern[0] before all pattern[1]
            val extraAddB = totalA   // add pattern[1] after all pattern[0]
            base + maxOf(extraAddA, extraAddB)
        }
    }
}
```

## Dart

```dart
class Solution {
  int maximumSubsequenceCount(String text, String pattern) {
    var p0 = pattern[0];
    var p1 = pattern[1];

    int cnt0 = 0;
    int cnt1 = 0;
    for (int i = 0; i < text.length; ++i) {
      var ch = text[i];
      if (ch == p0) cnt0++;
      if (ch == p1) cnt1++;
    }

    if (p0 == p1) {
      int base = cnt0 * (cnt0 - 1) ~/ 2;
      return base + cnt0;
    } else {
      int seen0 = 0;
      int base = 0;
      for (int i = 0; i < text.length; ++i) {
        var ch = text[i];
        if (ch == p0) {
          seen0++;
        } else if (ch == p1) {
          base += seen0;
        }
      }
      int add = cnt0 > cnt1 ? cnt0 : cnt1;
      return base + add;
    }
  }
}
```

## Golang

```go
func maximumSubsequenceCount(text string, pattern string) int64 {
    a := pattern[0]
    b := pattern[1]

    var cntA, cntB int64
    for i := 0; i < len(text); i++ {
        c := text[i]
        if c == a {
            cntA++
        }
        if c == b {
            cntB++
        }
    }

    var original, prefA int64
    for i := 0; i < len(text); i++ {
        c := text[i]
        if c == a {
            prefA++
        } else if c == b {
            original += prefA
        }
    }

    if a == b {
        return original + cntA
    }
    addedIfAddA := cntB // insert pattern[0]
    addedIfAddB := cntA // insert pattern[1]

    if addedIfAddA > addedIfAddB {
        return original + addedIfAddA
    }
    return original + addedIfAddB
}
```

## Ruby

```ruby
def maximum_subsequence_count(text, pattern)
  a = pattern[0]
  b = pattern[1]

  if a == b
    cnt = text.count(a)
    return cnt * (cnt - 1) / 2 + cnt
  end

  count_a = 0
  base = 0
  total_b = 0

  text.each_char do |ch|
    total_b += 1 if ch == b
  end

  text.each_char do |ch|
    if ch == a
      count_a += 1
    elsif ch == b
      base += count_a
    end
  end

  added_by_a = total_b   # insert 'a' before all characters
  added_by_b = count_a   # insert 'b' after all characters

  base + [added_by_a, added_by_b].max
end
```

## Scala

```scala
object Solution {
    def maximumSubsequenceCount(text: String, pattern: String): Long = {
        val a = pattern.charAt(0)
        val b = pattern.charAt(1)
        if (a == b) {
            var cnt: Long = 0
            for (ch <- text) {
                if (ch == a) cnt += 1
            }
            val base = cnt * (cnt - 1) / 2
            base + cnt
        } else {
            var totalA: Long = 0
            var totalB: Long = 0
            var prefixA: Long = 0
            var base: Long = 0
            for (ch <- text) {
                if (ch == a) {
                    totalA += 1
                    prefixA += 1
                } else if (ch == b) {
                    totalB += 1
                    base += prefixA
                }
            }
            base + math.max(totalA, totalB)
        }
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn maximum_subsequence_count(text: String, pattern: String) -> i64 {
        let bytes = text.as_bytes();
        let p = pattern.as_bytes();
        let p0 = p[0];
        let p1 = p[1];

        if p0 == p1 {
            // count occurrences of the single character
            let mut cnt: i64 = 0;
            for &b in bytes {
                if b == p0 {
                    cnt += 1;
                }
            }
            // existing subsequences + new ones formed with the added character
            cnt * (cnt - 1) / 2 + cnt
        } else {
            let mut count_p0: i64 = 0; // number of pattern[0] seen so far
            let mut total_p0: i64 = 0; // total occurrences of pattern[0]
            let mut total_p1: i64 = 0; // total occurrences of pattern[1]
            let mut base: i64 = 0;     // existing subsequence count

            for &b in bytes {
                if b == p0 {
                    count_p0 += 1;
                    total_p0 += 1;
                } else if b == p1 {
                    base += count_p0;
                    total_p1 += 1;
                }
            }

            let add = if total_p0 > total_p1 { total_p0 } else { total_p1 };
            base + add
        }
    }
}
```

## Racket

```racket
(define/contract (maximum-subsequence-count text pattern)
  (-> string? string? exact-integer?)
  (let* ((c0 (string-ref pattern 0))
         (c1 (string-ref pattern 1)))
    (if (char=? c0 c1)
        ;; pattern like "aa"
        (let ((cnt 0))
          (for ([i (in-range (string-length text))])
            (when (char=? (string-ref text i) c0)
              (set! cnt (+ cnt 1))))
          (+ (/ (* cnt (- cnt 1)) 2) cnt))
        ;; pattern like "ab"
        (let ((cnt0 0)
              (cnt1 0)
              (base 0))
          (for ([i (in-range (string-length text))])
            (let ((ch (string-ref text i)))
              (cond
                [(char=? ch c0) (set! cnt0 (+ cnt0 1))]
                [(char=? ch c1)
                 (set! base (+ base cnt0))
                 (set! cnt1 (+ cnt1 1))])))
          (+ base (max cnt0 cnt1))))))
```

## Erlang

```erlang
-spec maximum_subsequence_count(Text :: unicode:unicode_binary(), Pattern :: unicode:unicode_binary()) -> integer().
maximum_subsequence_count(Text, Pattern) ->
    <<P0, P1>> = Pattern,
    TextList = binary_to_list(Text),
    case P0 == P1 of
        true ->
            Count = count_char(TextList, P0, 0),
            Original = (Count * (Count - 1)) div 2,
            Original + Count;
        false ->
            {Original, TotalA, TotalB} = scan(TextList, P0, P1, 0, 0, 0, 0),
            Original + erlang:max(TotalA, TotalB)
    end.

count_char([], _Char, Acc) -> Acc;
count_char([H|T], Char, Acc) ->
    if H == Char ->
            count_char(T, Char, Acc + 1);
       true ->
            count_char(T, Char, Acc)
    end.

scan([], _P0, _P1, _CntFirst, Orig, TotA, TotB) ->
    {Orig, TotA, TotB};
scan([H|T], P0, P1, CntFirst, Orig, TotA, TotB) ->
    if H == P0 ->
            scan(T, P0, P1, CntFirst + 1, Orig, TotA + 1, TotB);
       H == P1 ->
            scan(T, P0, P1, CntFirst, Orig + CntFirst, TotA, TotB + 1);
       true ->
            scan(T, P0, P1, CntFirst, Orig, TotA, TotB)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_subsequence_count(text :: String.t(), pattern :: String.t()) :: integer()
  def maximum_subsequence_count(text, pattern) do
    a = String.at(pattern, 0)
    b = String.at(pattern, 1)

    if a == b do
      cnt =
        text
        |> String.graphemes()
        |> Enum.count(fn ch -> ch == a end)

      existing = div(cnt * (cnt - 1), 2)
      existing + cnt
    else
      chars = String.graphemes(text)

      {cnt_a, cnt_b, existing} =
        Enum.reduce(chars, {0, 0, 0}, fn ch, {ca, cb, ex} ->
          cond do
            ch == a -> {ca + 1, cb, ex}
            ch == b -> {ca, cb + 1, ex + ca}
            true -> {ca, cb, ex}
          end
        end)

      existing + max(cnt_a, cnt_b)
    end
  end
end
```
