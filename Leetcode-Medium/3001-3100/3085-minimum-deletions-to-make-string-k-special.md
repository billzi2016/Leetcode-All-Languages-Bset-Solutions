# 3085. Minimum Deletions to Make String K-Special

## Cpp

```cpp
class Solution {
public:
    int minimumDeletions(string word, int k) {
        vector<int> cnt(26, 0);
        for (char c : word) cnt[c - 'a']++;
        int n = word.size();
        int ans = n; // worst case: delete all characters
        for (int i = 0; i < 26; ++i) {
            if (cnt[i] == 0) continue; // cannot be the smallest retained character
            int x = cnt[i];
            long long del = 0;
            for (int j = 0; j < 26; ++j) {
                int y = cnt[j];
                if (y < x) {
                    del += y; // delete all occurrences of this character
                } else if (y > x + k) {
                    del += y - (x + k); // reduce to the allowed maximum
                }
            }
            ans = min(ans, (int)del);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minimumDeletions(String word, int k) {
        int[] cnt = new int[26];
        for (int i = 0; i < word.length(); i++) {
            cnt[word.charAt(i) - 'a']++;
        }
        int totalLen = word.length();
        int answer = totalLen; // worst case: delete all characters
        for (int i = 0; i < 26; i++) {
            if (cnt[i] == 0) continue; // cannot be the smallest frequency if absent
            int base = cnt[i];
            int deletions = 0;
            for (int j = 0; j < 26; j++) {
                if (cnt[j] == 0) continue;
                if (cnt[j] < base) {
                    deletions += cnt[j]; // delete all occurrences
                } else if (cnt[j] > base + k) {
                    deletions += cnt[j] - (base + k); // reduce to allowed max
                }
            }
            answer = Math.min(answer, deletions);
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - ord('a')] += 1

        ans = len(word)  # worst case delete all
        for i in range(26):
            if freq[i] == 0:
                continue
            x = freq[i]
            limit = x + k
            deletions = 0
            for j in range(26):
                cnt = freq[j]
                if cnt < x:
                    deletions += cnt
                elif cnt > limit:
                    deletions += cnt - limit
            if deletions < ans:
                ans = deletions
        return ans
```

## Python3

```python
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - 97] += 1

        n = len(word)
        best = n  # worst case: delete all characters

        for x in freq:
            if x == 0:
                continue
            low = x
            high = x + k
            deletions = 0
            for y in freq:
                if y < low:
                    deletions += y
                elif y > high:
                    deletions += y - high
            if deletions < best:
                best = deletions

        return best
```

## C

```c
#include <string.h>

int minimumDeletions(char* word, int k) {
    int freq[26] = {0};
    int n = 0;
    for (char *p = word; *p; ++p) {
        freq[*p - 'a']++;
        n++;
    }

    int best = n; // worst case: delete all characters

    for (int i = 0; i < 26; ++i) {
        if (freq[i] == 0) continue; // cannot be the smallest kept character
        int x = freq[i];
        int deletions = 0;
        for (int j = 0; j < 26; ++j) {
            if (j == i || freq[j] == 0) continue;
            if (freq[j] < x) {
                deletions += freq[j]; // delete all of this character
            } else if (freq[j] > x + k) {
                deletions += freq[j] - (x + k); // reduce to x+k
            }
        }
        if (deletions < best) best = deletions;
    }

    return best;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumDeletions(string word, int k) {
        int[] cnt = new int[26];
        foreach (char ch in word) {
            cnt[ch - 'a']++;
        }
        int n = word.Length;
        int best = n; // worst case: delete all characters
        for (int i = 0; i < 26; i++) {
            if (cnt[i] == 0) continue; // cannot be the smallest frequency among kept chars
            int x = cnt[i];
            int deletions = 0;
            for (int j = 0; j < 26; j++) {
                if (j == i) continue;
                int y = cnt[j];
                if (y < x) {
                    deletions += y; // delete all occurrences
                } else if (y > x + k) {
                    deletions += y - (x + k); // reduce to x+k
                }
            }
            if (deletions < best) best = deletions;
        }
        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @param {number} k
 * @return {number}
 */
var minimumDeletions = function(word, k) {
    const freq = new Array(26).fill(0);
    for (const ch of word) {
        freq[ch.charCodeAt(0) - 97]++;
    }
    const n = word.length;
    let ans = n; // worst case: delete all characters
    for (let i = 0; i < 26; i++) {
        if (freq[i] === 0) continue; // cannot be the smallest retained character
        const x = freq[i];
        let del = 0;
        for (let j = 0; j < 26; j++) {
            if (i === j) continue;
            const y = freq[j];
            if (y < x) {
                del += y; // delete all occurrences
            } else if (y > x + k) {
                del += y - (x + k); // reduce to allowed maximum
            }
        }
        if (del < ans) ans = del;
    }
    return ans;
};
```

## Typescript

```typescript
function minimumDeletions(word: string, k: number): number {
    const cnt = new Array(26).fill(0);
    for (const ch of word) {
        cnt[ch.charCodeAt(0) - 97]++;
    }

    let ans = Number.MAX_SAFE_INTEGER;
    const n = word.length;

    for (let i = 0; i < 26; i++) {
        const minFreq = cnt[i];
        if (minFreq === 0) continue;
        let del = 0;
        for (let j = 0; j < 26; j++) {
            const cur = cnt[j];
            if (cur === 0) continue;
            if (cur < minFreq) {
                del += cur;
            } else if (cur > minFreq + k) {
                del += cur - (minFreq + k);
            }
        }
        ans = Math.min(ans, del);
    }

    // In case all characters are removed (worst case)
    ans = Math.min(ans, n);
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $word
     * @param Integer $k
     * @return Integer
     */
    function minimumDeletions($word, $k) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($word);
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($word[$i]) - 97;
            $cnt[$idx]++;
        }

        $ans = $n; // worst case: delete all characters
        for ($c = 0; $c < 26; $c++) {
            if ($cnt[$c] == 0) continue; // cannot be the smallest if absent
            $x = $cnt[$c];
            $del = 0;
            for ($d = 0; $d < 26; $d++) {
                $y = $cnt[$d];
                if ($y == 0) continue;
                if ($y < $x) {
                    $del += $y; // delete all of this character
                } elseif ($y > $x + $k) {
                    $del += $y - ($x + $k); // reduce to x+k
                }
            }
            if ($del < $ans) $ans = $del;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minimumDeletions(_ word: String, _ k: Int) -> Int {
        var cnt = [Int](repeating: 0, count: 26)
        for byte in word.utf8 {
            let idx = Int(byte - 97) // 'a' ascii is 97
            cnt[idx] += 1
        }
        let n = word.count
        var answer = n
        
        for i in 0..<26 {
            let x = cnt[i]
            if x == 0 { continue }   // cannot be the smallest kept character
            var deletions = 0
            for j in 0..<26 {
                let y = cnt[j]
                if y == 0 { continue }
                if y < x {
                    deletions += y               // delete all of this character
                } else if y > x + k {
                    deletions += y - (x + k)     // trim down to x + k
                }
            }
            answer = min(answer, deletions)
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumDeletions(word: String, k: Int): Int {
        val cnt = IntArray(26)
        for (ch in word) {
            cnt[ch - 'a']++
        }
        var answer = Int.MAX_VALUE
        for (i in 0 until 26) {
            val x = cnt[i]
            if (x == 0) continue
            var deletions = 0
            for (j in 0 until 26) {
                val y = cnt[j]
                when {
                    y < x -> deletions += y               // delete all of this character
                    y > x + k -> deletions += y - (x + k) // reduce to max allowed
                }
            }
            if (deletions < answer) answer = deletions
        }
        return answer
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  int minimumDeletions(String word, int k) {
    List<int> freq = List.filled(26, 0);
    for (int i = 0; i < word.length; ++i) {
      freq[word.codeUnitAt(i) - 97]++;
    }

    int n = word.length;
    int answer = n; // worst case: delete all characters

    for (int i = 0; i < 26; ++i) {
      if (freq[i] == 0) continue; // cannot be the smallest kept character
      int x = freq[i];
      int deletions = 0;
      for (int j = 0; j < 26; ++j) {
        int y = freq[j];
        if (y == 0) continue;
        if (y < x) {
          deletions += y;
        } else if (y > x + k) {
          deletions += y - (x + k);
        }
      }
      answer = min(answer, deletions);
    }

    return answer;
  }
}
```

## Golang

```go
func minimumDeletions(word string, k int) int {
    var cnt [26]int
    for _, ch := range word {
        cnt[ch-'a']++
    }
    maxFreq := 0
    for _, v := range cnt {
        if v > maxFreq {
            maxFreq = v
        }
    }
    ans := len(word)
    for x := 0; x <= maxFreq; x++ {
        del := 0
        limit := x + k
        for _, y := range cnt {
            if y < x {
                del += y
            } else if y > limit {
                del += y - limit
            }
        }
        if del < ans {
            ans = del
        }
    }
    return ans
}
```

## Ruby

```ruby
def minimum_deletions(word, k)
  cnt = Array.new(26, 0)
  word.each_byte { |b| cnt[b - 97] += 1 }

  total_len = word.length
  ans = total_len

  (0...26).each do |i|
    x = cnt[i]
    next if x == 0

    del = 0
    (0...26).each do |j|
      y = cnt[j]
      next if y == 0
      if y < x
        del += y
      elsif y > x + k
        del += y - (x + k)
      end
    end
    ans = del if del < ans
  end

  ans
end
```

## Scala

```scala
object Solution {
    def minimumDeletions(word: String, k: Int): Int = {
        val freq = Array.fill(26)(0)
        for (ch <- word) {
            freq(ch - 'a') += 1
        }
        var best = Int.MaxValue
        for (i <- 0 until 26 if freq(i) > 0) {
            val x = freq(i)
            var del = 0
            for (j <- 0 until 26) {
                val y = freq(j)
                if (y < x) del += y
                else if (y > x + k) del += y - (x + k)
            }
            if (del < best) best = del
        }
        if (best == Int.MaxValue) word.length else best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_deletions(word: String, k: i32) -> i32 {
        let mut freq = [0i32; 26];
        for b in word.bytes() {
            freq[(b - b'a') as usize] += 1;
        }
        let k = k;
        let mut ans = word.len() as i32;
        for &x in freq.iter() {
            if x == 0 {
                continue;
            }
            let mut del = 0i32;
            for &y in freq.iter() {
                if y == 0 {
                    continue;
                }
                if y < x {
                    del += y;
                } else if y > x + k {
                    del += y - (x + k);
                }
            }
            if del < ans {
                ans = del;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (minimum-deletions word k)
  (-> string? exact-integer? exact-integer?)
  (let* ((n (string-length word))
         (cnt (make-vector 26 0)))
    ;; count frequencies
    (for ([i n])
      (let* ((ch (string-ref word i))
             (idx (- (char->integer ch) (char->integer #\a))))
        (vector-set! cnt idx (+ (vector-ref cnt idx) 1))))
    (define (deletions-for x)
      (let ((total 0))
        (for ([j 26])
          (let ((y (vector-ref cnt j)))
            (cond
              [(< y x) (set! total (+ total y))]
              [(> y (+ x k)) (set! total (+ total (- y (+ x k))))])))
        total))
    (define ans n)
    ;; consider smallest frequency = 0
    (let ((d0 (deletions-for 0)))
      (when (< d0 ans) (set! ans d0)))
    ;; enumerate each character's original count as possible minimum
    (for ([i 26])
      (let ((x (vector-ref cnt i)))
        (when (> x 0)
          (let ((d (deletions-for x)))
            (when (< d ans) (set! ans d))))))
    ans)))
```

## Erlang

```erlang
-module(solution).
-export([minimum_deletions/2]).

-spec minimum_deletions(Word :: unicode:unicode_binary(), K :: integer()) -> integer().
minimum_deletions(Word, K) ->
    CountsTuple = count_chars(Word),
    CountsList = tuple_to_list(CountsTuple),
    NonZero = [C || C <- CountsList, C > 0],
    Candidates = lists:usort([0 | NonZero]),
    TotalLen = byte_size(Word),
    lists:foldl(
        fun(X, Best) ->
            Del = deletions_for_x(X, K, CountsList),
            if Del < Best -> Del; true -> Best end
        end,
        TotalLen,
        Candidates).

count_chars(Word) ->
    EmptyTuple = erlang:list_to_tuple(lists:duplicate(26, 0)),
    go_count(Word, EmptyTuple).

go_count(<<>>, Tuple) -> Tuple;
go_count(<<Byte, Rest/binary>>, Tuple) ->
    Index = Byte - $a + 1,
    Old = element(Index, Tuple),
    NewTuple = setelement(Index, Tuple, Old + 1),
    go_count(Rest, NewTuple).

deletions_for_x(_X, _K, []) -> 0;
deletions_for_x(X, K, [Y|Rest]) ->
    DelHere =
        if Y == 0 -> 0;
           Y < X -> Y;
           Y > X + K -> Y - (X + K);
           true -> 0
        end,
    DelHere + deletions_for_x(X, K, Rest).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_deletions(word :: String.t(), k :: integer) :: integer
  def minimum_deletions(word, k) do
    freq =
      :binary.bin_to_list(word)
      |> Enum.reduce(List.duplicate(0, 26), fn byte, acc ->
        idx = byte - ?a
        List.update_at(acc, idx, &(&1 + 1))
      end)

    total_len = String.length(word)

    Enum.reduce(freq, total_len, fn x, best ->
      if x == 0 do
        best
      else
        del =
          Enum.reduce(freq, 0, fn y, acc ->
            cond do
              y == 0 -> acc
              y < x -> acc + y
              y > x + k -> acc + (y - (x + k))
              true -> acc
            end
          end)

        if del < best, do: del, else: best
      end
    end)
  end
end
```
