# 2062. Count Vowel Substrings of a String

## Cpp

```cpp
class Solution {
public:
    int countVowelSubstrings(string word) {
        auto isVowel = [](char c)->bool{
            return c=='a' || c=='e' || c=='i' || c=='o' || c=='u';
        };
        auto bit = [](char c)->int{
            switch(c){
                case 'a': return 1<<0;
                case 'e': return 1<<1;
                case 'i': return 1<<2;
                case 'o': return 1<<3;
                case 'u': return 1<<4;
            }
            return 0;
        };
        const int FULL = (1<<5)-1; // 31
        int n = word.size();
        int ans = 0;
        for(int i=0;i<n;++i){
            if(!isVowel(word[i])) continue;
            int mask = 0;
            for(int j=i;j<n && isVowel(word[j]);++j){
                mask |= bit(word[j]);
                if(mask==FULL) ++ans;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countVowelSubstrings(String word) {
        int n = word.length();
        int result = 0;
        for (int i = 0; i < n; i++) {
            int[] cnt = new int[5];
            int distinct = 0;
            for (int j = i; j < n; j++) {
                int idx = vowelIndex(word.charAt(j));
                if (idx == -1) break; // consonant stops the substring
                if (cnt[idx] == 0) distinct++;
                cnt[idx]++;
                if (distinct == 5) result++;
            }
        }
        return result;
    }

    private int vowelIndex(char c) {
        switch (c) {
            case 'a': return 0;
            case 'e': return 1;
            case 'i': return 2;
            case 'o': return 3;
            case 'u': return 4;
            default: return -1;
        }
    }
}
```

## Python

```python
class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels = set('aeiou')
        n = len(word)
        ans = 0
        for i in range(n):
            if word[i] not in vowels:
                continue
            seen = set()
            for j in range(i, n):
                ch = word[j]
                if ch not in vowels:
                    break
                seen.add(ch)
                if len(seen) == 5:
                    ans += 1
        return ans
```

## Python3

```python
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set('aeiou')
        n = len(word)
        ans = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if word[j] not in vowels:
                    break
                seen.add(word[j])
                if len(seen) == 5:
                    ans += 1
        return ans
```

## C

```c
static int isVowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int countVowelSubstrings(char* word) {
    int total = 0;
    for (int i = 0; word[i] != '\0'; ++i) {
        if (!isVowel(word[i])) continue;
        int mask = 0;
        for (int j = i; word[j] != '\0'; ++j) {
            char c = word[j];
            if (!isVowel(c)) break;
            switch (c) {
                case 'a': mask |= 1 << 0; break;
                case 'e': mask |= 1 << 1; break;
                case 'i': mask |= 1 << 2; break;
                case 'o': mask |= 1 << 3; break;
                case 'u': mask |= 1 << 4; break;
            }
            if (mask == 31) ++total;
        }
    }
    return total;
}
```

## Csharp

```csharp
public class Solution
{
    public int CountVowelSubstrings(string word)
    {
        int n = word.Length;
        int result = 0;

        for (int i = 0; i < n; i++)
        {
            int mask = 0;
            for (int j = i; j < n; j++)
            {
                char c = word[j];
                if (!IsVowel(c))
                    break;

                mask |= VowelBit(c);
                if (mask == 31) // all five vowels present
                    result++;
            }
        }

        return result;

        bool IsVowel(char ch)
        {
            return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
        }

        int VowelBit(char ch)
        {
            switch (ch)
            {
                case 'a': return 1;   // 00001
                case 'e': return 2;   // 00010
                case 'i': return 4;   // 00100
                case 'o': return 8;   // 01000
                case 'u': return 16;  // 10000
                default: return 0;
            }
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var countVowelSubstrings = function(word) {
    const vowelSet = new Set(['a', 'e', 'i', 'o', 'u']);
    const n = word.length;
    let ans = 0;
    for (let i = 0; i < n; ++i) {
        if (!vowelSet.has(word[i])) continue;
        const seen = new Set();
        for (let j = i; j < n; ++j) {
            const ch = word[j];
            if (!vowelSet.has(ch)) break;
            seen.add(ch);
            if (seen.size === 5) ans++;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function countVowelSubstrings(word: string): number {
    const vowelMask = (c: string): number => {
        switch (c) {
            case 'a': return 1;   // 00001
            case 'e': return 2;   // 00010
            case 'i': return 4;   // 00100
            case 'o': return 8;   // 01000
            case 'u': return 16;  // 10000
            default: return 0;
        }
    };
    const n = word.length;
    let ans = 0;
    for (let i = 0; i < n; ++i) {
        if (vowelMask(word[i]) === 0) continue;
        let mask = 0;
        for (let j = i; j < n; ++j) {
            const v = vowelMask(word[j]);
            if (v === 0) break;
            mask |= v;
            if (mask === 31) ans++;
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $word
     * @return Integer
     */
    function countVowelSubstrings($word) {
        $n = strlen($word);
        $vowelsSet = ['a'=>true,'e'=>true,'i'=>true,'o'=>true,'u'=>true];
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            if (!isset($vowelsSet[$word[$i]])) continue;
            $cnt = ['a'=>0,'e'=>0,'i'=>0,'o'=>0,'u'=>0];
            $distinct = 0;
            for ($j = $i; $j < $n; $j++) {
                $ch = $word[$j];
                if (!isset($vowelsSet[$ch])) break;
                if ($cnt[$ch] == 0) $distinct++;
                $cnt[$ch]++;
                if ($distinct == 5) $ans++;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countVowelSubstrings(_ word: String) -> Int {
        let chars = Array(word)
        let n = chars.count
        var result = 0
        let vowelSet: Set<Character> = ["a", "e", "i", "o", "u"]
        
        for i in 0..<n {
            if !vowelSet.contains(chars[i]) { continue }
            var seen = [Bool](repeating: false, count: 5)
            var distinct = 0
            var j = i
            while j < n {
                let c = chars[j]
                if !vowelSet.contains(c) { break }
                switch c {
                case "a":
                    if !seen[0] { seen[0] = true; distinct += 1 }
                case "e":
                    if !seen[1] { seen[1] = true; distinct += 1 }
                case "i":
                    if !seen[2] { seen[2] = true; distinct += 1 }
                case "o":
                    if !seen[3] { seen[3] = true; distinct += 1 }
                case "u":
                    if !seen[4] { seen[4] = true; distinct += 1 }
                default:
                    break
                }
                if distinct == 5 {
                    result += 1
                }
                j += 1
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countVowelSubstrings(word: String): Int {
        val n = word.length
        var ans = 0
        for (i in 0 until n) {
            if (!isVowel(word[i])) continue
            val cnt = IntArray(5)
            var distinct = 0
            for (j in i until n) {
                val c = word[j]
                if (!isVowel(c)) break
                when (c) {
                    'a' -> { if (cnt[0] == 0) distinct++; cnt[0]++ }
                    'e' -> { if (cnt[1] == 0) distinct++; cnt[1]++ }
                    'i' -> { if (cnt[2] == 0) distinct++; cnt[2]++ }
                    'o' -> { if (cnt[3] == 0) distinct++; cnt[3]++ }
                    'u' -> { if (cnt[4] == 0) distinct++; cnt[4]++ }
                }
                if (distinct == 5) ans++
            }
        }
        return ans
    }

    private fun isVowel(ch: Char): Boolean {
        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u'
    }
}
```

## Dart

```dart
class Solution {
  int countVowelSubstrings(String word) {
    const Map<String, int> bit = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16};
    int n = word.length;
    int ans = 0;
    for (int i = 0; i < n; i++) {
      int mask = 0;
      for (int j = i; j < n; j++) {
        String ch = word[j];
        if (!bit.containsKey(ch)) break;
        mask |= bit[ch]!;
        if (mask == 31) ans++;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func countVowelSubstrings(word string) int {
	n := len(word)
	isVowel := func(c byte) bool {
		return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
	}
	total := 0
	for i := 0; i < n; i++ {
		if !isVowel(word[i]) {
			continue
		}
		mask := 0
		for j := i; j < n && isVowel(word[j]); j++ {
			switch word[j] {
			case 'a':
				mask |= 1 << 0
			case 'e':
				mask |= 1 << 1
			case 'i':
				mask |= 1 << 2
			case 'o':
				mask |= 1 << 3
			case 'u':
				mask |= 1 << 4
			}
			if mask == 31 {
				total++
			}
		}
	}
	return total
}
```

## Ruby

```ruby
def count_vowel_substrings(word)
  vowels = { 'a' => true, 'e' => true, 'i' => true, 'o' => true, 'u' => true }
  n = word.length
  ans = 0
  (0...n).each do |i|
    next unless vowels[word[i]]
    freq = Hash.new(0)
    distinct = 0
    j = i
    while j < n && vowels[word[j]]
      ch = word[j]
      distinct += 1 if freq[ch] == 0
      freq[ch] += 1
      ans += 1 if distinct == 5
      j += 1
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def countVowelSubstrings(word: String): Int = {
        val vowelSet = Set('a', 'e', 'i', 'o', 'u')
        var result = 0
        val n = word.length

        for (i <- 0 until n) {
            if (!vowelSet.contains(word(i))) {
                // start at consonant, skip
            } else {
                val seen = new Array[Boolean](5)
                var cnt = 0
                var j = i
                while (j < n && vowelSet.contains(word(j))) {
                    val idx = word(j) match {
                        case 'a' => 0
                        case 'e' => 1
                        case 'i' => 2
                        case 'o' => 3
                        case 'u' => 4
                    }
                    if (!seen(idx)) {
                        seen(idx) = true
                        cnt += 1
                    }
                    if (cnt == 5) result += 1
                    j += 1
                }
            }
        }

        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_vowel_substrings(word: String) -> i32 {
        let bytes = word.as_bytes();
        let n = bytes.len();
        let mut ans = 0i32;
        for i in 0..n {
            if !Self::is_vowel(bytes[i]) {
                continue;
            }
            let mut mask: u8 = 0;
            for j in i..n {
                let b = bytes[j];
                if !Self::is_vowel(b) {
                    break;
                }
                mask |= Self::vowel_bit(b);
                if mask == 31 {
                    ans += 1;
                }
            }
        }
        ans
    }

    #[inline]
    fn is_vowel(b: u8) -> bool {
        matches!(b, b'a' | b'e' | b'i' | b'o' | b'u')
    }

    #[inline]
    fn vowel_bit(b: u8) -> u8 {
        match b {
            b'a' => 1,
            b'e' => 2,
            b'i' => 4,
            b'o' => 8,
            b'u' => 16,
            _ => 0,
        }
    }
}
```

## Racket

```racket
(define/contract (count-vowel-substrings word)
  (-> string? exact-integer?)
  (let* ((n (string-length word))
         (full-mask 31)
         (vowel-bit
          (lambda (ch)
            (cond [(char=? ch #\a) 1]
                  [(char=? ch #\e) 2]
                  [(char=? ch #\i) 4]
                  [(char=? ch #\o) 8]
                  [(char=? ch #\u) 16]
                  [else 0]))))
    (let loop-i ((i 0) (total 0))
      (if (= i n)
          total
          (let ((start-bit (vowel-bit (string-ref word i))))
            (if (= start-bit 0)
                (loop-i (+ i 1) total)
                (let inner-loop ((j i) (mask 0) (cnt total))
                  (if (= j n)
                      (loop-i (+ i 1) cnt)
                      (let ((bit (vowel-bit (string-ref word j))))
                        (if (= bit 0)
                            (loop-i (+ i 1) cnt)
                            (let ((new-mask (bitwise-ior mask bit))
                                  (new-cnt (if (= new-mask full-mask) (+ cnt 1) cnt)))
                              (inner-loop (+ j 1) new-mask new-cnt)))))))))))
```

## Erlang

```erlang
-export([count_vowel_substrings/1]).

-spec count_vowel_substrings(Word :: unicode:unicode_binary()) -> integer().
count_vowel_substrings(Word) ->
    Chars = unicode:characters_to_list(Word),
    count_from(Chars).

count_from([]) -> 0;
count_from([_|T]=Rest) ->
    CountStart = inner_count(Rest, 0, 0),
    CountStart + count_from(T).

inner_count([], _Mask, Acc) -> Acc;
inner_count([C|Cs], Mask, Acc) ->
    Bit = vowel_bit(C),
    case Bit of
        0 -> Acc; % stop when a consonant is met
        _ ->
            NewMask = Mask bor Bit,
            NewAcc = if NewMask == 31 -> Acc + 1 else Acc end,
            inner_count(Cs, NewMask, NewAcc)
    end.

vowel_bit($a) -> 1;
vowel_bit($e) -> 2;
vowel_bit($i) -> 4;
vowel_bit($o) -> 8;
vowel_bit($u) -> 16;
vowel_bit(_) -> 0.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_vowel_substrings(String.t()) :: integer()
  def count_vowel_substrings(word) do
    chars = String.to_charlist(word)
    len = length(chars)
    count_from(0, chars, len, 0)
  end

  defp count_from(i, _chars, len, acc) when i >= len, do: acc

  defp count_from(i, chars, len, acc) do
    acc = inner(i, i, 0, chars, len, acc)
    count_from(i + 1, chars, len, acc)
  end

  defp inner(_start, j, _mask, _chars, len, acc) when j >= len, do: acc

  defp inner(start, j, mask, chars, len, acc) do
    c = Enum.at(chars, j)

    case vowel_mask(c) do
      nil ->
        acc

      m ->
        new_mask = mask ||| m
        new_acc = if new_mask == 31, do: acc + 1, else: acc
        inner(start, j + 1, new_mask, chars, len, new_acc)
    end
  end

  defp vowel_mask(?a), do: 1
  defp vowel_mask(?e), do: 2
  defp vowel_mask(?i), do: 4
  defp vowel_mask(?o), do: 8
  defp vowel_mask(?u), do: 16
  defp vowel_mask(_), do: nil
end
```
