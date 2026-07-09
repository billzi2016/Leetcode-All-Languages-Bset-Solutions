# 2531. Make Number of Distinct Characters Equal

## Cpp

```cpp
class Solution {
public:
    bool isItPossible(string word1, string word2) {
        vector<int> cnt1(26, 0), cnt2(26, 0);
        for (char c : word1) cnt1[c - 'a']++;
        for (char c : word2) cnt2[c - 'a']++;
        
        int d1 = 0, d2 = 0;
        for (int i = 0; i < 26; ++i) {
            if (cnt1[i] > 0) ++d1;
            if (cnt2[i] > 0) ++d2;
        }
        
        for (int c1 = 0; c1 < 26; ++c1) {
            if (cnt1[c1] == 0) continue;
            for (int c2 = 0; c2 < 26; ++c2) {
                if (cnt2[c2] == 0) continue;
                
                int nd1 = d1, nd2 = d2;
                if (c1 != c2) {
                    // effect on word1
                    if (cnt1[c1] == 1) --nd1;          // removing last occurrence of c1
                    if (cnt1[c2] == 0) ++nd1;          // adding new character c2
                    
                    // effect on word2
                    if (cnt2[c2] == 1) --nd2;          // removing last occurrence of c2
                    if (cnt2[c1] == 0) ++nd2;          // adding new character c1
                }
                // when c1 == c2, nd1 and nd2 stay the same
                
                if (nd1 == nd2) return true;
            }
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean isItPossible(String word1, String word2) {
        int[] cnt1 = new int[26];
        int[] cnt2 = new int[26];
        for (char ch : word1.toCharArray()) cnt1[ch - 'a']++;
        for (char ch : word2.toCharArray()) cnt2[ch - 'a']++;

        int distinct1 = 0, distinct2 = 0;
        for (int i = 0; i < 26; i++) {
            if (cnt1[i] > 0) distinct1++;
            if (cnt2[i] > 0) distinct2++;
        }

        if (distinct1 == distinct2) return true;

        for (int c = 0; c < 26; c++) {
            if (cnt1[c] == 0) continue;
            for (int d = 0; d < 26; d++) {
                if (cnt2[d] == 0) continue;
                if (c == d) continue; // swapping same character changes nothing

                int newDistinct1 = distinct1;
                int newDistinct2 = distinct2;

                // effect on word1
                if (cnt1[c] == 1) newDistinct1--;          // lose character c
                if (cnt1[d] == 0) newDistinct1++;          // gain character d

                // effect on word2
                if (cnt2[d] == 1) newDistinct2--;          // lose character d
                if (cnt2[c] == 0) newDistinct2++;          // gain character c

                if (newDistinct1 == newDistinct2) return true;
            }
        }

        return false;
    }
}
```

## Python

```python
class Solution(object):
    def isItPossible(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        freq1 = [0] * 26
        freq2 = [0] * 26
        for ch in word1:
            freq1[ord(ch) - 97] += 1
        for ch in word2:
            freq2[ord(ch) - 97] += 1

        d1 = sum(1 for x in freq1 if x > 0)
        d2 = sum(1 for x in freq2 if x > 0)

        # iterate over possible characters to swap
        for a in range(26):
            if freq1[a] == 0:
                continue
            for b in range(26):
                if freq2[b] == 0:
                    continue

                if a == b:
                    # swapping same character leaves counts unchanged
                    if d1 == d2:
                        return True
                    continue

                nd1 = d1
                nd2 = d2

                # effect on word1 distinct count
                if freq1[a] == 1:      # removing last occurrence of a
                    nd1 -= 1
                if freq1[b] == 0:      # adding new character b
                    nd1 += 1

                # effect on word2 distinct count
                if freq2[b] == 1:      # removing last occurrence of b
                    nd2 -= 1
                if freq2[a] == 0:      # adding new character a
                    nd2 += 1

                if nd1 == nd2:
                    return True

        return False
```

## Python3

```python
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26
        for ch in word1:
            freq1[ord(ch) - 97] += 1
        for ch in word2:
            freq2[ord(ch) - 97] += 1

        d1 = sum(1 for x in freq1 if x > 0)
        d2 = sum(1 for x in freq2 if x > 0)

        for a in range(26):
            if freq1[a] == 0:
                continue
            for b in range(26):
                if freq2[b] == 0:
                    continue

                new_d1, new_d2 = d1, d2

                if a != b:
                    # word1 changes
                    if freq1[a] == 1:
                        new_d1 -= 1
                    if freq1[b] == 0:
                        new_d1 += 1
                    # word2 changes
                    if freq2[b] == 1:
                        new_d2 -= 1
                    if freq2[a] == 0:
                        new_d2 += 1

                # if a == b, counts stay the same (new_d1 == d1, new_d2 == d2)

                if new_d1 == new_d2:
                    return True
        return False
```

## C

```c
#include <stdbool.h>

bool isItPossible(char* word1, char* word2) {
    int freq1[26] = {0}, freq2[26] = {0};
    for (char *p = word1; *p; ++p) freq1[*p - 'a']++;
    for (char *p = word2; *p; ++p) freq2[*p - 'a']++;

    int d1 = 0, d2 = 0;
    for (int i = 0; i < 26; ++i) {
        if (freq1[i]) ++d1;
        if (freq2[i]) ++d2;
    }

    if (d1 == d2) return true;

    for (int i = 0; i < 26; ++i) {
        if (!freq1[i]) continue;
        for (int j = 0; j < 26; ++j) {
            if (!freq2[j]) continue;
            if (i == j) continue; // swapping same character won't change distinct counts
            int nd1 = d1;
            if (freq1[i] == 1) nd1--;
            if (freq1[j] == 0) nd1++;
            int nd2 = d2;
            if (freq2[j] == 1) nd2--;
            if (freq2[i] == 0) nd2++;
            if (nd1 == nd2) return true;
        }
    }
    return false;
}
```

## Csharp

```csharp
public class Solution
{
    public bool IsItPossible(string word1, string word2)
    {
        int[] cnt1 = new int[26];
        int[] cnt2 = new int[26];

        foreach (char ch in word1) cnt1[ch - 'a']++;
        foreach (char ch in word2) cnt2[ch - 'a']++;

        int d1 = 0, d2 = 0;
        for (int i = 0; i < 26; i++)
        {
            if (cnt1[i] > 0) d1++;
            if (cnt2[i] > 0) d2++;
        }

        for (int a = 0; a < 26; a++)
        {
            if (cnt1[a] == 0) continue;
            for (int b = 0; b < 26; b++)
            {
                if (cnt2[b] == 0) continue;

                // swapping same character
                if (a == b)
                {
                    if (d1 == d2) return true;
                    continue;
                }

                int nd1 = d1;
                int nd2 = d2;

                // word1 loses a, gains b
                if (cnt1[a] == 1) nd1--;          // a disappears from word1
                if (cnt1[b] == 0) nd1++;          // b appears in word1

                // word2 loses b, gains a
                if (cnt2[b] == 1) nd2--;          // b disappears from word2
                if (cnt2[a] == 0) nd2++;          // a appears in word2

                if (nd1 == nd2) return true;
            }
        }

        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word1
 * @param {string} word2
 * @return {boolean}
 */
var isItPossible = function(word1, word2) {
    const cnt1 = new Array(26).fill(0);
    const cnt2 = new Array(26).fill(0);
    for (let ch of word1) cnt1[ch.charCodeAt(0) - 97]++;
    for (let ch of word2) cnt2[ch.charCodeAt(0) - 97]++;

    let d1 = 0, d2 = 0;
    for (let i = 0; i < 26; i++) {
        if (cnt1[i] > 0) d1++;
        if (cnt2[i] > 0) d2++;
    }

    for (let a = 0; a < 26; a++) {
        if (cnt1[a] === 0) continue;
        for (let b = 0; b < 26; b++) {
            if (cnt2[b] === 0) continue;

            let newD1 = d1, newD2 = d2;

            if (a === b) {
                // swapping same character leaves distinct counts unchanged
                if (newD1 === newD2) return true;
                continue;
            }

            // Effects on word1
            if (cnt1[a] === 1) newD1--;          // lose a completely
            if (cnt1[b] === 0) newD1++;          // gain b as new distinct

            // Effects on word2
            if (cnt2[b] === 1) newD2--;          // lose b completely
            if (cnt2[a] === 0) newD2++;          // gain a as new distinct

            if (newD1 === newD2) return true;
        }
    }

    return false;
};
```

## Typescript

```typescript
function isItPossible(word1: string, word2: string): boolean {
    const freq1 = new Array(26).fill(0);
    const freq2 = new Array(26).fill(0);
    for (const ch of word1) freq1[ch.charCodeAt(0) - 97]++;
    for (const ch of word2) freq2[ch.charCodeAt(0) - 97]++;

    let d1 = 0, d2 = 0;
    for (let i = 0; i < 26; i++) {
        if (freq1[i] > 0) d1++;
        if (freq2[i] > 0) d2++;
    }

    for (let c1 = 0; c1 < 26; c1++) {
        if (freq1[c1] === 0) continue;
        for (let c2 = 0; c2 < 26; c2++) {
            if (freq2[c2] === 0) continue;

            let nd1 = d1, nd2 = d2;
            if (c1 !== c2) {
                // word1 changes
                if (freq1[c1] === 1) nd1--;
                if (freq1[c2] === 0) nd1++;
                // word2 changes
                if (freq2[c2] === 1) nd2--;
                if (freq2[c1] === 0) nd2++;
            }
            if (nd1 === nd2) return true;
        }
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param String $word1
     * @param String $word2
     * @return Boolean
     */
    function isItPossible($word1, $word2) {
        $freq1 = array_fill(0, 26, 0);
        $freq2 = array_fill(0, 26, 0);

        $len1 = strlen($word1);
        for ($i = 0; $i < $len1; $i++) {
            $idx = ord($word1[$i]) - 97;
            $freq1[$idx]++;
        }

        $len2 = strlen($word2);
        for ($i = 0; $i < $len2; $i++) {
            $idx = ord($word2[$i]) - 97;
            $freq2[$idx]++;
        }

        $d1 = 0;
        $d2 = 0;
        for ($i = 0; $i < 26; $i++) {
            if ($freq1[$i] > 0) $d1++;
            if ($freq2[$i] > 0) $d2++;
        }

        for ($c1 = 0; $c1 < 26; $c1++) {
            if ($freq1[$c1] == 0) continue;
            for ($c2 = 0; $c2 < 26; $c2++) {
                if ($freq2[$c2] == 0) continue;

                if ($c1 == $c2) {
                    // swapping same character leaves counts unchanged
                    if ($d1 == $d2) return true;
                    continue;
                }

                $newD1 = $d1;
                if ($freq1[$c1] == 1) $newD1--;          // removing last occurrence of c1 from word1
                if ($freq1[$c2] == 0) $newD1++;          // adding new character c2 to word1

                $newD2 = $d2;
                if ($freq2[$c2] == 1) $newD2--;          // removing last occurrence of c2 from word2
                if ($freq2[$c1] == 0) $newD2++;          // adding new character c1 to word2

                if ($newD1 == $newD2) return true;
            }
        }

        return false;
    }
}
```

## Swift

```swift
class Solution {
    func isItPossible(_ word1: String, _ word2: String) -> Bool {
        var f1 = [Int](repeating: 0, count: 26)
        var f2 = [Int](repeating: 0, count: 26)
        
        for scalar in word1.unicodeScalars {
            let idx = Int(scalar.value - 97)
            f1[idx] += 1
        }
        for scalar in word2.unicodeScalars {
            let idx = Int(scalar.value - 97)
            f2[idx] += 1
        }
        
        var d1 = 0, d2 = 0
        for i in 0..<26 {
            if f1[i] > 0 { d1 += 1 }
            if f2[i] > 0 { d2 += 1 }
        }
        
        for i in 0..<26 where f1[i] > 0 {
            for j in 0..<26 where f2[j] > 0 {
                var nd1 = d1
                var nd2 = d2
                
                if i != j {
                    // word1 loses character i
                    if f1[i] == 1 { nd1 -= 1 }
                    // word1 gains character j
                    if f1[j] == 0 { nd1 += 1 }
                    
                    // word2 loses character j
                    if f2[j] == 1 { nd2 -= 1 }
                    // word2 gains character i
                    if f2[i] == 0 { nd2 += 1 }
                }
                
                if nd1 == nd2 {
                    return true
                }
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isItPossible(word1: String, word2: String): Boolean {
        val f1 = IntArray(26)
        val f2 = IntArray(26)
        for (ch in word1) f1[ch - 'a']++
        for (ch in word2) f2[ch - 'a']++

        var d1 = 0
        var d2 = 0
        for (i in 0 until 26) {
            if (f1[i] > 0) d1++
            if (f2[i] > 0) d2++
        }

        for (c1 in 0 until 26) {
            if (f1[c1] == 0) continue
            for (c2 in 0 until 26) {
                if (f2[c2] == 0) continue

                var nd1 = d1
                var nd2 = d2

                if (c1 == c2) {
                    if (nd1 == nd2) return true
                    continue
                }

                // word1 adjustments
                if (f1[c1] == 1) nd1--
                if (f1[c2] == 0) nd1++

                // word2 adjustments
                if (f2[c2] == 1) nd2--
                if (f2[c1] == 0) nd2++

                if (nd1 == nd2) return true
            }
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool isItPossible(String word1, String word2) {
    List<int> cnt1 = List.filled(26, 0);
    List<int> cnt2 = List.filled(26, 0);

    for (int c in word1.codeUnits) {
      cnt1[c - 97]++;
    }
    for (int c in word2.codeUnits) {
      cnt2[c - 97]++;
    }

    int d1 = 0;
    int d2 = 0;
    for (int i = 0; i < 26; i++) {
      if (cnt1[i] > 0) d1++;
      if (cnt2[i] > 0) d2++;
    }

    for (int a = 0; a < 26; a++) {
      if (cnt1[a] == 0) continue;
      for (int b = 0; b < 26; b++) {
        if (cnt2[b] == 0) continue;

        if (a == b) {
          // swapping identical characters leaves distinct counts unchanged
          if (d1 == d2) return true;
        } else {
          int delta1 = 0;
          if (cnt1[a] == 1) delta1--;      // a disappears from word1
          if (cnt1[b] == 0) delta1++;      // b appears in word1

          int delta2 = 0;
          if (cnt2[b] == 1) delta2--;      // b disappears from word2
          if (cnt2[a] == 0) delta2++;      // a appears in word2

          if (d1 + delta1 == d2 + delta2) return true;
        }
      }
    }

    return false;
  }
}
```

## Golang

```go
func isItPossible(word1 string, word2 string) bool {
    var f1, f2 [26]int
    for _, ch := range word1 {
        f1[ch-'a']++
    }
    for _, ch := range word2 {
        f2[ch-'a']++
    }

    d1, d2 := 0, 0
    for i := 0; i < 26; i++ {
        if f1[i] > 0 {
            d1++
        }
        if f2[i] > 0 {
            d2++
        }
    }

    // If distinct counts already equal, a swap of the same character works.
    if d1 == d2 {
        for i := 0; i < 26; i++ {
            if f1[i] > 0 && f2[i] > 0 {
                return true
            }
        }
    }

    // Try swapping different characters.
    for i := 0; i < 26; i++ {
        if f1[i] == 0 {
            continue
        }
        for j := 0; j < 26; j++ {
            if i == j || f2[j] == 0 {
                continue
            }

            nd1 := d1
            if f1[i] == 1 {
                nd1--
            }
            if f1[j] == 0 {
                nd1++
            }

            nd2 := d2
            if f2[j] == 1 {
                nd2--
            }
            if f2[i] == 0 {
                nd2++
            }

            if nd1 == nd2 {
                return true
            }
        }
    }
    return false
}
```

## Ruby

```ruby
def is_it_possible(word1, word2)
  cnt1 = Array.new(26, 0)
  cnt2 = Array.new(26, 0)

  word1.each_byte { |c| cnt1[c - 97] += 1 }
  word2.each_byte { |c| cnt2[c - 97] += 1 }

  d1 = cnt1.count { |v| v > 0 }
  d2 = cnt2.count { |v| v > 0 }

  # Swapping identical characters (no change)
  if d1 == d2
    26.times do |i|
      return true if cnt1[i] > 0 && cnt2[i] > 0
    end
  end

  26.times do |a|
    next if cnt1[a] == 0
    26.times do |b|
      next if cnt2[b] == 0
      next if a == b

      delta1 = (cnt1[a] == 1 ? -1 : 0) + (cnt1[b] == 0 ? 1 : 0)
      delta2 = (cnt2[b] == 1 ? -1 : 0) + (cnt2[a] == 0 ? 1 : 0)

      return true if d1 + delta1 == d2 + delta2
    end
  end

  false
end
```

## Scala

```scala
object Solution {
    def isItPossible(word1: String, word2: String): Boolean = {
        val freq1 = Array.fill(26)(0)
        val freq2 = Array.fill(26)(0)

        for (ch <- word1) freq1(ch - 'a') += 1
        for (ch <- word2) freq2(ch - 'a') += 1

        var d1 = 0
        var d2 = 0
        for (i <- 0 until 26) {
            if (freq1(i) > 0) d1 += 1
            if (freq2(i) > 0) d2 += 1
        }

        // Swapping identical characters keeps distinct counts unchanged.
        if (d1 == d2) {
            for (i <- 0 until 26) {
                if (freq1(i) > 0 && freq2(i) > 0) return true
            }
        }

        // Try swapping different characters.
        for (c <- 0 until 26 if freq1(c) > 0) {
            for (d <- 0 until 26 if freq2(d) > 0 && c != d) {
                var delta1 = 0
                if (freq1(c) == 1) delta1 -= 1          // c disappears from word1
                if (freq1(d) == 0) delta1 += 1          // d appears in word1

                var delta2 = 0
                if (freq2(d) == 1) delta2 -= 1          // d disappears from word2
                if (freq2(c) == 0) delta2 += 1          // c appears in word2

                if (d1 + delta1 == d2 + delta2) return true
            }
        }

        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_it_possible(word1: String, word2: String) -> bool {
        let mut freq1 = [0i32; 26];
        let mut freq2 = [0i32; 26];

        for &ch in word1.as_bytes() {
            let idx = (ch - b'a') as usize;
            freq1[idx] += 1;
        }
        for &ch in word2.as_bytes() {
            let idx = (ch - b'a') as usize;
            freq2[idx] += 1;
        }

        let distinct1 = freq1.iter().filter(|&&c| c > 0).count();
        let distinct2 = freq2.iter().filter(|&&c| c > 0).count();

        for a in 0..26 {
            if freq1[a] == 0 { continue; }
            for b in 0..26 {
                if freq2[b] == 0 { continue; }

                let mut nd1 = distinct1 as i32;
                let mut nd2 = distinct2 as i32;

                if a != b {
                    if freq1[a] == 1 { nd1 -= 1; }
                    if freq1[b] == 0 { nd1 += 1; }

                    if freq2[b] == 1 { nd2 -= 1; }
                    if freq2[a] == 0 { nd2 += 1; }
                }

                if nd1 == nd2 {
                    return true;
                }
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (is-it-possible word1 word2)
  (-> string? string? boolean?)
  (let* ([freq1 (make-vector 26 0)]
         [freq2 (make-vector 26 0)]
         [base (char->integer #\a)])
    ;; count frequencies in word1
    (for ([i (in-range (string-length word1))])
      (let* ([c (string-ref word1 i)]
             [idx (- (char->integer c) base)])
        (vector-set! freq1 idx (+ 1 (vector-ref freq1 idx)))))
    ;; count frequencies in word2
    (for ([i (in-range (string-length word2))])
      (let* ([c (string-ref word2 i)]
             [idx (- (char->integer c) base)])
        (vector-set! freq2 idx (+ 1 (vector-ref freq2 idx)))))
    ;; distinct character counts
    (define (distinct-count vec)
      (for/sum ([i (in-range 26)]) (if (> (vector-ref vec i) 0) 1 0)))
    (define d1 (distinct-count freq1))
    (define d2 (distinct-count freq2))
    ;; try all possible swaps
    (for/or ([a (in-range 26)] #:when (> (vector-ref freq1 a) 0))
      (for/or ([b (in-range 26)] #:when (> (vector-ref freq2 b) 0))
        (if (= a b)
            (= d1 d2)
            (let* ([dr1 (if (= (vector-ref freq1 a) 1) -1 0)]
                   [da1 (if (= (vector-ref freq1 b) 0) 1 0)]
                   [newd1 (+ d1 dr1 da1)]
                   [dr2 (if (= (vector-ref freq2 b) 1) -1 0)]
                   [da2 (if (= (vector-ref freq2 a) 0) 1 0)]
                   [newd2 (+ d2 dr2 da2)])
              (= newd1 newd2))))))))
```

## Erlang

```erlang
-module(solution).
-export([is_it_possible/2]).
-spec is_it_possible(Word1 :: unicode:unicode_binary(), Word2 :: unicode:unicode_binary()) -> boolean().
is_it_possible(Word1, Word2) ->
    F1 = build_freq(Word1),
    F2 = build_freq(Word2),
    D1 = distinct(F1),
    D2 = distinct(F2),
    possible(F1, F2, D1, D2).

build_freq(Bin) -> build_freq(Bin, erlang:make_tuple(26, 0)).
build_freq(<<>>, Tuple) -> Tuple;
build_freq(<<Char, Rest/binary>>, Tuple) ->
    Index = Char - $a + 1,
    Count = element(Index, Tuple),
    NewTuple = setelement(Index, Tuple, Count + 1),
    build_freq(Rest, NewTuple).

distinct(Tuple) -> distinct(1, Tuple, 0).
distinct(I, Tuple, Acc) when I =< 26 ->
    case element(I, Tuple) of
        0 -> distinct(I + 1, Tuple, Acc);
        _ -> distinct(I + 1, Tuple, Acc + 1)
    end;
distinct(_, _, Acc) -> Acc.

possible(F1, F2, D1, D2) -> possible_a(1, F1, F2, D1, D2).

possible_a(AIdx, F1, F2, D1, D2) when AIdx =< 26 ->
    case element(AIdx, F1) of
        0 -> possible_a(AIdx + 1, F1, F2, D1, D2);
        _ ->
            case possible_b(AIdx, 1, F1, F2, D1, D2) of
                true -> true;
                false -> possible_a(AIdx + 1, F1, F2, D1, D2)
            end
    end;
possible_a(_, _, _, _, _) -> false.

possible_b(_AIdx, BIdx, _F1, _F2, _D1, _D2) when BIdx > 26 -> false;
possible_b(AIdx, BIdx, F1, F2, D1, D2) ->
    case element(BIdx, F2) of
        0 -> possible_b(AIdx, BIdx + 1, F1, F2, D1, D2);
        _CountB ->
            if AIdx =:= BIdx ->
                    case D1 == D2 of
                        true -> true;
                        false -> possible_b(AIdx, BIdx + 1, F1, F2, D1, D2)
                    end;
               true ->
                    F1a = element(AIdx, F1),
                    F1b = element(BIdx, F1),
                    F2b = element(BIdx, F2),
                    F2a = element(AIdx, F2),

                    Nd1 = D1 - (if F1a == 1 -> 1; true -> 0 end) + (if F1b == 0 -> 1; true -> 0 end),
                    Nd2 = D2 - (if F2b == 1 -> 1; true -> 0 end) + (if F2a == 0 -> 1; true -> 0 end),

                    case Nd1 == Nd2 of
                        true -> true;
                        false -> possible_b(AIdx, BIdx + 1, F1, F2, D1, D2)
                    end
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_it_possible(word1 :: String.t(), word2 :: String.t()) :: boolean()
  def is_it_possible(word1, word2) do
    cnt1 = build_counts(word1)
    cnt2 = build_counts(word2)

    d1 = distinct_count(cnt1)
    d2 = distinct_count(cnt2)

    # Check swaps of different characters
    possible =
      Enum.reduce_while(0..25, false, fn a, _acc ->
        ca = elem(cnt1, a)

        if ca == 0 do
          {:cont, false}
        else
          inner_result =
            Enum.reduce_while(0..25, false, fn b, _inner_acc ->
              cb = elem(cnt2, b)

              cond do
                cb == 0 or a == b ->
                  {:cont, false}

                true ->
                  nd1 =
                    d1 -
                      (if ca == 1, do: 1, else: 0) +
                      (if elem(cnt1, b) == 0, do: 1, else: 0)

                  nd2 =
                    d2 -
                      (if cb == 1, do: 1, else: 0) +
                      (if elem(cnt2, a) == 0, do: 1, else: 0)

                  if nd1 == nd2 do
                    {:halt, true}
                  else
                    {:cont, false}
                  end
              end
            end)

          if inner_result do
            {:halt, true}
          else
            {:cont, false}
          end
        end
      end)

    if possible do
      true
    else
      # Swapping same character (no change) is allowed if distinct counts already equal
      common_exists? =
        Enum.any?(0..25, fn i -> elem(cnt1, i) > 0 and elem(cnt2, i) > 0 end)

      d1 == d2 and common_exists?
    end
  end

  defp build_counts(str) do
    Enum.reduce(:binary.bin_to_list(str), Tuple.duplicate(0, 26), fn byte, acc ->
      idx = byte - ?a
      cur = elem(acc, idx)
      put_elem(acc, idx, cur + 1)
    end)
  end

  defp distinct_count(cnt) do
    cnt
    |> Tuple.to_list()
    |> Enum.count(&(&1 > 0))
  end
end
```
