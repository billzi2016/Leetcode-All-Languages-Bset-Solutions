# 3121. Count the Number of Special Characters II

## Cpp

```cpp
class Solution {
public:
    int numberOfSpecialChars(string word) {
        const int INF = word.size() + 5;
        vector<int> firstUpper(26, INF);
        vector<int> lastLower(26, -1);
        for (int i = 0; i < (int)word.size(); ++i) {
            char ch = word[i];
            if ('a' <= ch && ch <= 'z') {
                lastLower[ch - 'a'] = i;
            } else { // uppercase
                firstUpper[ch - 'A'] = min(firstUpper[ch - 'A'], i);
            }
        }
        int ans = 0;
        for (int i = 0; i < 26; ++i) {
            if (lastLower[i] != -1 && firstUpper[i] != INF && lastLower[i] < firstUpper[i])
                ++ans;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int numberOfSpecialChars(String word) {
        int n = word.length();
        int[] firstUpper = new int[26];
        int[] lastLower = new int[26];
        for (int i = 0; i < 26; i++) {
            firstUpper[i] = Integer.MAX_VALUE;
            lastLower[i] = -1;
        }
        for (int i = 0; i < n; i++) {
            char c = word.charAt(i);
            if (c >= 'a' && c <= 'z') {
                int idx = c - 'a';
                lastLower[idx] = i;
            } else { // uppercase
                int idx = c - 'A';
                if (i < firstUpper[idx]) {
                    firstUpper[idx] = i;
                }
            }
        }
        int count = 0;
        for (int i = 0; i < 26; i++) {
            if (lastLower[i] != -1 && firstUpper[i] != Integer.MAX_VALUE && lastLower[i] < firstUpper[i]) {
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        INF = len(word) + 1
        first_upper = [INF] * 26
        last_lower = [-1] * 26

        for i, ch in enumerate(word):
            if 'a' <= ch <= 'z':
                idx = ord(ch) - ord('a')
                last_lower[idx] = i
            else:  # uppercase
                idx = ord(ch) - ord('A')
                if i < first_upper[idx]:
                    first_upper[idx] = i

        count = 0
        for i in range(26):
            if last_lower[i] != -1 and first_upper[i] != INF and last_lower[i] < first_upper[i]:
                count += 1
        return count
```

## Python3

```python
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        n = len(word)
        lower_last = [-1] * 26
        upper_first = [n] * 26

        for i, ch in enumerate(word):
            if 'a' <= ch <= 'z':
                idx = ord(ch) - ord('a')
                lower_last[idx] = i
            else:
                idx = ord(ch) - ord('A')
                if upper_first[idx] == n:
                    upper_first[idx] = i

        count = 0
        for i in range(26):
            if lower_last[i] != -1 and upper_first[i] != n and lower_last[i] < upper_first[i]:
                count += 1
        return count
```

## C

```c
int numberOfSpecialChars(char* word) {
    const int INF = 0x3f3f3f3f;
    int firstUpper[26];
    int lastLower[26];
    for (int i = 0; i < 26; ++i) {
        firstUpper[i] = INF;
        lastLower[i] = -1;
    }
    for (int i = 0; word[i]; ++i) {
        char c = word[i];
        if (c >= 'a' && c <= 'z') {
            lastLower[c - 'a'] = i;
        } else { // uppercase
            int idx = c - 'A';
            if (firstUpper[idx] == INF) firstUpper[idx] = i;
        }
    }
    int ans = 0;
    for (int i = 0; i < 26; ++i) {
        if (lastLower[i] != -1 && firstUpper[i] != INF && lastLower[i] < firstUpper[i])
            ++ans;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int NumberOfSpecialChars(string word)
    {
        const int INF = int.MaxValue;
        int[] firstUpper = new int[26];
        int[] lastLower = new int[26];
        for (int i = 0; i < 26; i++)
        {
            firstUpper[i] = INF;
            lastLower[i] = -1;
        }

        for (int i = 0; i < word.Length; i++)
        {
            char ch = word[i];
            if (ch >= 'a' && ch <= 'z')
            {
                int idx = ch - 'a';
                lastLower[idx] = i; // latest lowercase position
            }
            else // uppercase
            {
                int idx = ch - 'A';
                if (i < firstUpper[idx])
                    firstUpper[idx] = i; // earliest uppercase position
            }
        }

        int count = 0;
        for (int i = 0; i < 26; i++)
        {
            if (lastLower[i] != -1 && firstUpper[i] != INF && lastLower[i] < firstUpper[i])
                count++;
        }

        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var numberOfSpecialChars = function(word) {
    const n = word.length;
    const INF = n; // sentinel for "not seen"
    const firstUpper = new Array(26).fill(INF);
    const lastLower = new Array(26).fill(-1);
    
    for (let i = 0; i < n; ++i) {
        const code = word.charCodeAt(i);
        if (code >= 97) { // 'a'..'z'
            const idx = code - 97;
            lastLower[idx] = i; // later occurrences overwrite earlier ones
        } else { // 'A'..'Z'
            const idx = code - 65;
            if (firstUpper[idx] === INF) {
                firstUpper[idx] = i; // record only the first uppercase occurrence
            }
        }
    }
    
    let count = 0;
    for (let i = 0; i < 26; ++i) {
        if (lastLower[i] !== -1 && firstUpper[i] !== INF && lastLower[i] < firstUpper[i]) {
            ++count;
        }
    }
    return count;
};
```

## Typescript

```typescript
function numberOfSpecialChars(word: string): number {
    const n = word.length;
    const lastLower = new Array(26).fill(-1);
    const firstUpper = new Array(26).fill(n);
    for (let i = 0; i < n; i++) {
        const code = word.charCodeAt(i);
        if (code >= 97) { // 'a' to 'z'
            const idx = code - 97;
            lastLower[idx] = i; // keep the latest lowercase position
        } else { // 'A' to 'Z'
            const idx = code - 65;
            if (firstUpper[idx] === n) {
                firstUpper[idx] = i; // record the earliest uppercase position
            }
        }
    }
    let count = 0;
    for (let i = 0; i < 26; i++) {
        if (lastLower[i] !== -1 && firstUpper[i] !== n && lastLower[i] < firstUpper[i]) {
            count++;
        }
    }
    return count;
}
```

## Php

```php
<?php
class Solution {
    /**
     * @param String $word
     * @return Integer
     */
    function numberOfSpecialChars($word) {
        $len = strlen($word);
        $lastLower = array_fill(0, 26, -1);
        $firstUpper = array_fill(0, 26, $len + 1);
        for ($i = 0; $i < $len; $i++) {
            $ch = $word[$i];
            $ord = ord($ch);
            if ($ord >= 97 && $ord <= 122) { // 'a' - 'z'
                $idx = $ord - 97;
                $lastLower[$idx] = $i; // keep the latest lowercase position
            } elseif ($ord >= 65 && $ord <= 90) { // 'A' - 'Z'
                $idx = $ord - 65;
                if ($firstUpper[$idx] > $i) {
                    $firstUpper[$idx] = $i; // keep the earliest uppercase position
                }
            }
        }
        $count = 0;
        for ($i = 0; $i < 26; $i++) {
            if ($lastLower[$i] != -1 && $firstUpper[$i] <= $len - 1 && $lastLower[$i] < $firstUpper[$i]) {
                $count++;
            }
        }
        return $count;
    }
}
?>
```

## Swift

```swift
class Solution {
    func numberOfSpecialChars(_ word: String) -> Int {
        var firstUpper = [Int](repeating: Int.max, count: 26)
        var lastLower = [Int](repeating: -1, count: 26)

        var index = 0
        for byte in word.utf8 {
            if byte >= 97 { // 'a'..'z'
                let i = Int(byte - 97)
                lastLower[i] = index
            } else { // 'A'..'Z'
                let i = Int(byte - 65)
                if firstUpper[i] == Int.max {
                    firstUpper[i] = index
                }
            }
            index += 1
        }

        var count = 0
        for i in 0..<26 {
            if lastLower[i] != -1 && firstUpper[i] != Int.max && lastLower[i] < firstUpper[i] {
                count += 1
            }
        }
        return count
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numberOfSpecialChars(word: String): Int {
        val n = word.length
        val inf = n
        val firstUpper = IntArray(26) { inf }
        val lastLower = IntArray(26) { -1 }

        for (i in 0 until n) {
            val ch = word[i]
            if (ch in 'A'..'Z') {
                val idx = ch.lowercaseChar() - 'a'
                if (firstUpper[idx] == inf) firstUpper[idx] = i
            } else { // lowercase
                val idx = ch - 'a'
                lastLower[idx] = i
            }
        }

        var count = 0
        for (i in 0 until 26) {
            if (lastLower[i] != -1 && firstUpper[i] != inf && lastLower[i] < firstUpper[i]) {
                count++
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int numberOfSpecialChars(String word) {
    const int INF = 1 << 30;
    List<int> firstUpper = List.filled(26, INF);
    List<int> lastLower = List.filled(26, -1);
    for (int i = 0; i < word.length; ++i) {
      int code = word.codeUnitAt(i);
      if (code >= 65 && code <= 90) { // 'A' to 'Z'
        int idx = code - 65;
        if (i < firstUpper[idx]) firstUpper[idx] = i;
      } else { // 'a' to 'z'
        int idx = code - 97;
        if (i > lastLower[idx]) lastLower[idx] = i;
      }
    }
    int count = 0;
    for (int i = 0; i < 26; ++i) {
      if (lastLower[i] != -1 && firstUpper[i] != INF && lastLower[i] < firstUpper[i]) {
        count++;
      }
    }
    return count;
  }
}
```

## Golang

```go
func numberOfSpecialChars(word string) int {
	const inf = int(^uint(0) >> 1)
	firstUpper := make([]int, 26)
	lastLower := make([]int, 26)
	for i := 0; i < 26; i++ {
		firstUpper[i] = inf
		lastLower[i] = -1
	}
	for idx, ch := range word {
		if ch >= 'a' && ch <= 'z' {
			lastLower[ch-'a'] = idx
		} else { // uppercase
			cIdx := ch - 'A'
			if idx < firstUpper[cIdx] {
				firstUpper[cIdx] = idx
			}
		}
	}
	count := 0
	for i := 0; i < 26; i++ {
		if lastLower[i] != -1 && firstUpper[i] != inf && lastLower[i] < firstUpper[i] {
			count++
		}
	}
	return count
}
```

## Ruby

```ruby
def number_of_special_chars(word)
  n = word.length
  inf = n + 1
  first_upper = Array.new(26, inf)
  last_lower = Array.new(26, -1)

  word.each_byte.with_index do |b, i|
    if b >= 65 && b <= 90 # 'A'..'Z'
      idx = b - 65
      first_upper[idx] = i if i < first_upper[idx]
    else # 'a'..'z'
      idx = b - 97
      last_lower[idx] = i
    end
  end

  count = 0
  26.times do |i|
    if last_lower[i] != -1 && first_upper[i] != inf && last_lower[i] < first_upper[i]
      count += 1
    end
  end
  count
end
```

## Scala

```scala
object Solution {
    def numberOfSpecialChars(word: String): Int = {
        val n = word.length
        val INF = n
        val firstUpper = Array.fill(26)(INF)
        val lastLower = Array.fill(26)(-1)

        var i = 0
        while (i < n) {
            val ch = word.charAt(i)
            if (ch >= 'a' && ch <= 'z') {
                val idx = ch - 'a'
                if (i > lastLower(idx)) lastLower(idx) = i
            } else {
                val idx = ch - 'A'
                if (i < firstUpper(idx)) firstUpper(idx) = i
            }
            i += 1
        }

        var count = 0
        var j = 0
        while (j < 26) {
            if (lastLower(j) != -1 && firstUpper(j) != INF && lastLower(j) < firstUpper(j)) {
                count += 1
            }
            j += 1
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn number_of_special_chars(word: String) -> i32 {
        let n = word.len();
        let mut first_upper = [usize::MAX; 26];
        let mut last_lower = [0usize; 26];
        let mut has_lower = [false; 26];

        for (i, b) in word.bytes().enumerate() {
            if (b'A'..=b'Z').contains(&b) {
                let idx = (b - b'A') as usize;
                if i < first_upper[idx] {
                    first_upper[idx] = i;
                }
            } else {
                // lowercase
                let idx = (b - b'a') as usize;
                has_lower[idx] = true;
                last_lower[idx] = i; // later occurrences overwrite, keeping the last index
            }
        }

        let mut count = 0;
        for i in 0..26 {
            if first_upper[i] != usize::MAX && has_lower[i] && last_lower[i] < first_upper[i] {
                count += 1;
            }
        }
        count as i32
    }
}
```

## Racket

```racket
(define/contract (number-of-special-chars word)
  (-> string? exact-integer?)
  (let* ([n (string-length word)]
         [inf n]
         [first-upper (make-vector 26 inf)]
         [last-lower (make-vector 26 -1)])
    (for ([i (in-range n)])
      (let ([c (string-ref word i)])
        (cond
          [(and (char>=? c #\a) (char<=? c #\z))
           (define idx (- (char->integer c) (char->integer #\a)))
           (vector-set! last-lower idx i)]
          [(and (char>=? c #\A) (char<=? c #\Z))
           (define idx (- (char->integer c) (char->integer #\A)))
           (when (< i (vector-ref first-upper idx))
             (vector-set! first-upper idx i))])))
    (let loop ([i 0] [cnt 0])
      (if (= i 26)
          cnt
          (let* ([lu (vector-ref last-lower i)]
                 [fu (vector-ref first-upper i)])
            (loop (+ i 1)
                  (if (and (>= lu 0) (< fu n) (< lu fu))
                      (+ cnt 1)
                      cnt)))))))
```

## Erlang

```erlang
-module(solution).
-export([number_of_special_chars/1]).

-spec number_of_special_chars(Word :: unicode:unicode_binary()) -> integer().
number_of_special_chars(Word) ->
    {FirstUpper, LastLower} = loop(Word, 0,
        erlang:make_tuple(26, -1),
        erlang:make_tuple(26, -1)),
    count_special(FirstUpper, LastLower).

loop(<<>>, _Idx, FU, LL) ->
    {FU, LL};
loop(<<Char, Rest/binary>>, Idx, FU, LL) ->
    case Char of
        C when C >= $a, C =< $z ->
            Index = C - $a + 1,
            NewLL = setelement(Index, LL, Idx),
            loop(Rest, Idx + 1, FU, NewLL);
        C when C >= $A, C =< $Z ->
            Index = C - $A + 1,
            case element(Index, FU) of
                -1 ->
                    NewFU = setelement(Index, FU, Idx),
                    loop(Rest, Idx + 1, NewFU, LL);
                _Existing ->
                    loop(Rest, Idx + 1, FU, LL)
            end;
        _Other ->
            loop(Rest, Idx + 1, FU, LL)
    end.

count_special(FU, LL) ->
    count_special(1, 26, FU, LL, 0).

count_special(I, Max, FU, LL, Acc) when I =< Max ->
    Upper = element(I, FU),
    Lower = element(I, LL),
    NewAcc = if Upper =/= -1, Lower =/= -1, Lower < Upper -> Acc + 1; true -> Acc end,
    count_special(I + 1, Max, FU, LL, NewAcc);
count_special(_, _, _, _, Acc) ->
    Acc.
```

## Elixir

```elixir
defmodule Solution do
  @spec number_of_special_chars(word :: String.t) :: integer
  def number_of_special_chars(word) do
    {lower_last, upper_first} =
      word
      |> String.to_charlist()
      |> Enum.with_index()
      |> Enum.reduce({%{}, %{}}, fn {c, i}, {low, up} ->
        cond do
          c >= ?a and c <= ?z ->
            letter = c - ?a
            {Map.put(low, letter, i), up}

          c >= ?A and c <= ?Z ->
            letter = c - ?A
            {low, Map.put_new(up, letter, i)}

          true ->
            {low, up}
        end
      end)

    Enum.count(0..25, fn l ->
      case {Map.get(lower_last, l), Map.get(upper_first, l)} do
        {nil, _} -> false
        {_, nil} -> false
        {low_idx, up_idx} -> low_idx < up_idx
      end
    end)
  end
end
```
