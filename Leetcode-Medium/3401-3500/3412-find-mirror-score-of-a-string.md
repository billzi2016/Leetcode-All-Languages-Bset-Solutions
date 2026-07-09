# 3412. Find Mirror Score of a String

## Cpp

```cpp
class Solution {
public:
    long long calculateScore(string s) {
        vector<vector<int>> stk(26);
        long long ans = 0;
        for (int i = 0; i < (int)s.size(); ++i) {
            int c = s[i] - 'a';
            int mir = 25 - c; // mirror character index
            if (!stk[mir].empty()) {
                int j = stk[mir].back();
                stk[mir].pop_back();
                ans += i - j;
            } else {
                stk[c].push_back(i);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long calculateScore(String s) {
        int n = s.length();
        @SuppressWarnings("unchecked")
        java.util.ArrayDeque<Integer>[] stacks = new java.util.ArrayDeque[26];
        for (int i = 0; i < 26; i++) {
            stacks[i] = new java.util.ArrayDeque<>();
        }
        long score = 0L;
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            int idx = c - 'a';
            int mirrorIdx = 'z' - c; // gives ASCII code of mirror character
            mirrorIdx = mirrorIdx - 'a'; // convert to 0-25 index
            if (!stacks[mirrorIdx].isEmpty()) {
                int prevPos = stacks[mirrorIdx].pop();
                score += (long) (i - prevPos);
            } else {
                stacks[idx].push(i);
            }
        }
        return score;
    }
}
```

## Python

```python
class Solution(object):
    def calculateScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        # stacks for each character storing indices of unpaired occurrences
        stacks = [[] for _ in range(26)]
        total = 0
        base = ord('a')
        for i, ch in enumerate(s):
            idx = ord(ch) - base
            mirror_idx = 25 - idx  # index of mirror character
            if stacks[mirror_idx]:
                j = stacks[mirror_idx].pop()
                total += i - j
            else:
                stacks[idx].append(i)
        return total
```

## Python3

```python
class Solution:
    def calculateScore(self, s: str) -> int:
        stacks = [[] for _ in range(26)]
        total = 0
        base = ord('a')
        for i, ch in enumerate(s):
            idx = ord(ch) - base
            mirror_idx = 25 - idx  # since a<->z, b<->y, etc.
            if stacks[mirror_idx]:
                j = stacks[mirror_idx].pop()
                total += i - j
            else:
                stacks[idx].append(i)
        return total
```

## C

```c
#include <string.h>

#define MAXN 100005

long long calculateScore(char* s) {
    int top[26] = {0};
    static int st[26][MAXN];
    long long score = 0;
    int n = strlen(s);
    for (int i = 0; i < n; ++i) {
        int idx = s[i] - 'a';
        int mirIdx = 'z' - s[i] + 'a';
        if (top[mirIdx] > 0) {
            int j = st[mirIdx][--top[mirIdx]];
            score += i - j;
        } else {
            st[idx][top[idx]++] = i;
        }
    }
    return score;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public long CalculateScore(string s) {
        var stacks = new Stack<int>[26];
        for (int i = 0; i < 26; i++) {
            stacks[i] = new Stack<int>();
        }

        long score = 0;
        for (int i = 0; i < s.Length; i++) {
            int idx = s[i] - 'a';
            int mirrorIdx = 25 - idx;

            if (stacks[mirrorIdx].Count > 0) {
                int j = stacks[mirrorIdx].Pop();
                score += i - j;
            } else {
                stacks[idx].Push(i);
            }
        }

        return score;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var calculateScore = function(s) {
    const stacks = Array.from({ length: 26 }, () => []);
    let score = 0;
    for (let i = 0; i < s.length; i++) {
        const chIdx = s.charCodeAt(i) - 97;          // index of current character
        const mirIdx = 25 - chIdx;                   // mirror character index
        if (stacks[mirIdx].length > 0) {
            const j = stacks[mirIdx].pop();         // match with latest unmarked mirror
            score += i - j;
        } else {
            stacks[chIdx].push(i);                  // store position for future matches
        }
    }
    return score;
};
```

## Typescript

```typescript
function calculateScore(s: string): number {
    const stacks: number[][] = Array.from({ length: 26 }, () => []);
    let score = 0;
    for (let i = 0; i < s.length; i++) {
        const chIdx = s.charCodeAt(i) - 97;          // 0..25
        const mirrorIdx = 25 - chIdx;                // mirrored letter index
        if (stacks[mirrorIdx].length > 0) {
            const j = stacks[mirrorIdx].pop()!;
            score += i - j;
        } else {
            stacks[chIdx].push(i);
        }
    }
    return score;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function calculateScore($s) {
        $n = strlen($s);
        $stacks = array_fill(0, 26, []);
        $score = 0;
        for ($i = 0; $i < $n; $i++) {
            $chIdx = ord($s[$i]) - 97;          // index of current character
            $mirrorIdx = 25 - $chIdx;           // index of its mirror character
            if (!empty($stacks[$mirrorIdx])) {
                $prevIdx = array_pop($stacks[$mirrorIdx]);
                $score += $i - $prevIdx;
            } else {
                $stacks[$chIdx][] = $i;         // push current index onto its own stack
            }
        }
        return $score;
    }
}
```

## Swift

```swift
class Solution {
    func calculateScore(_ s: String) -> Int {
        var stacks = Array(repeating: [Int](), count: 26)
        var score = 0
        let aValue = Character("a").unicodeScalars.first!.value
        for (i, ch) in s.enumerated() {
            guard let scalar = ch.unicodeScalars.first else { continue }
            let idx = Int(scalar.value - aValue) // 0...25
            let mirrorIdx = 25 - idx
            if var arr = stacks[mirrorIdx], !arr.isEmpty {
                // pop last element
                let j = stacks[mirrorIdx].removeLast()
                score += i - j
            } else {
                stacks[idx].append(i)
            }
        }
        return score
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun calculateScore(s: String): Long {
        val stacks = Array(26) { mutableListOf<Int>() }
        var score = 0L
        for (i in s.indices) {
            val ch = s[i]
            val mirChar = ('z'.code - (ch.code - 'a'.code)).toChar()
            val mirIdx = mirChar - 'a'
            if (stacks[mirIdx].isNotEmpty()) {
                val j = stacks[mirIdx].removeAt(stacks[mirIdx].size - 1)
                score += (i - j).toLong()
            } else {
                val idx = ch - 'a'
                stacks[idx].add(i)
            }
        }
        return score
    }
}
```

## Dart

```dart
class Solution {
  int calculateScore(String s) {
    List<List<int>> stacks = List.generate(26, (_) => []);
    int score = 0;
    for (int i = 0; i < s.length; ++i) {
      int chIdx = s.codeUnitAt(i) - 97;
      int mirIdx = 25 - chIdx;
      if (stacks[mirIdx].isNotEmpty) {
        int j = stacks[mirIdx].removeLast();
        score += i - j;
      } else {
        stacks[chIdx].add(i);
      }
    }
    return score;
  }
}
```

## Golang

```go
func calculateScore(s string) int64 {
    // stacks for each character 'a' to 'z'
    stacks := make([][]int, 26)
    var score int64 = 0
    for i, chRune := range s {
        c := int(chRune - 'a')
        // mirror character index
        m := 25 - c // because 'a'->0, 'z'->25
        if len(stacks[m]) > 0 {
            // pop the last index from mirror's stack
            jIdx := stacks[m][len(stacks[m])-1]
            stacks[m] = stacks[m][:len(stacks[m])-1]
            score += int64(i - jIdx)
        } else {
            // push current index onto its own character stack
            stacks[c] = append(stacks[c], i)
        }
    }
    return score
}
```

## Ruby

```ruby
def calculate_score(s)
  stacks = Array.new(26) { [] }
  score = 0
  s.each_char.with_index do |ch, i|
    idx = ch.ord - 97
    mirror_idx = 25 - idx
    if !stacks[mirror_idx].empty?
      j = stacks[mirror_idx].pop
      score += i - j
    else
      stacks[idx] << i
    end
  end
  score
end
```

## Scala

```scala
object Solution {
  def calculateScore(s: String): Long = {
    val stacks = Array.fill(26)(new java.util.ArrayDeque[Int]())
    var score: Long = 0L
    var i = 0
    while (i < s.length) {
      val chIdx = s.charAt(i) - 'a'
      val mirrorIdx = 25 - chIdx
      if (!stacks(mirrorIdx).isEmpty) {
        val j = stacks(mirrorIdx).removeLast()
        score += (i - j)
      } else {
        stacks(chIdx).addLast(i)
      }
      i += 1
    }
    score
  }
}
```

## Rust

```rust
impl Solution {
    pub fn calculate_score(s: String) -> i64 {
        let bytes = s.as_bytes();
        let mut stacks: Vec<Vec<usize>> = vec![Vec::new(); 26];
        let mut score: i64 = 0;
        for (i, &b) in bytes.iter().enumerate() {
            let idx = (b - b'a') as usize;
            let mirror = 25 - idx;
            if let Some(prev) = stacks[mirror].pop() {
                score += (i - prev) as i64;
            } else {
                stacks[idx].push(i);
            }
        }
        score
    }
}
```

## Racket

```racket
(define/contract (calculate-score s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (stacks (make-vector 26 '()))
         (score 0))
    (for ([i (in-range n)])
      (let* ((ch (string-ref s i))
             (code (- (char->integer ch) (char->integer #\a)))
             (mirror-code (- 25 code))
             (mirror-stack (vector-ref stacks mirror-code)))
        (if (null? mirror-stack)
            (let ((curr-stack (vector-ref stacks code)))
              (vector-set! stacks code (cons i curr-stack)))
            (begin
              (set! score (+ score (- i (car mirror-stack))))
              (vector-set! stacks mirror-code (cdr mirror-stack))))))
    score)))
```

## Erlang

```erlang
-module(solution).
-export([calculate_score/1]).

-spec calculate_score(S :: unicode:unicode_binary()) -> integer().
calculate_score(S) ->
    Stacks = erlang:make_tuple(26, []),
    loop(S, 0, Stacks, 0).

loop(<<>>, _Pos, _Stacks, Score) ->
    Score;
loop(<<C, Rest/binary>>, Pos, Stacks, Score) ->
    Idx = C - $a,
    MirrorIdx = 25 - Idx,
    MirrorStack = element(MirrorIdx + 1, Stacks),
    case MirrorStack of
        [] ->
            CurStack = element(Idx + 1, Stacks),
            NewCurStack = [Pos | CurStack],
            NewStacks = setelement(Idx + 1, Stacks, NewCurStack),
            loop(Rest, Pos + 1, NewStacks, Score);
        [J | RestMirror] ->
            NewScore = Score + (Pos - J),
            NewStacks = setelement(MirrorIdx + 1, Stacks, RestMirror),
            loop(Rest, Pos + 1, NewStacks, NewScore)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec calculate_score(s :: String.t()) :: integer()
  def calculate_score(s) do
    chars = String.to_charlist(s)

    # Initialize stacks for each letter (0..25) as empty lists
    init_stacks =
      Enum.reduce(0..25, %{}, fn i, acc ->
        Map.put(acc, i, [])
      end)

    {score, _stacks} =
      Enum.with_index(chars)
      |> Enum.reduce({0, init_stacks}, fn {ch, idx}, {sc, stacks} ->
        c = ch - ?a
        mirror = 25 - c

        case Map.get(stacks, mirror) do
          [] ->
            # No available mirror, push current index onto its own stack
            cur_stack = Map.get(stacks, c)
            new_stacks = Map.put(stacks, c, [idx | cur_stack])
            {sc, new_stacks}

          [j | rest] ->
            # Found a matching mirror, add distance to score and pop it
            new_sc = sc + (idx - j)
            new_stacks = Map.put(stacks, mirror, rest)
            {new_sc, new_stacks}
        end
      end)

    score
  end
end
```
