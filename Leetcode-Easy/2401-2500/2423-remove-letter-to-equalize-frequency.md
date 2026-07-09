# 2423. Remove Letter To Equalize Frequency

## Cpp

```cpp
class Solution {
public:
    bool equalFrequency(string word) {
        int freq[26] = {0};
        for (char c : word) freq[c - 'a']++;
        
        for (int i = 0; i < 26; ++i) {
            if (freq[i] == 0) continue;
            freq[i]--; // remove one occurrence of this letter
            
            int target = -1;
            bool ok = true;
            for (int j = 0; j < 26; ++j) {
                if (freq[j] == 0) continue;
                if (target == -1) target = freq[j];
                else if (freq[j] != target) { ok = false; break; }
            }
            
            freq[i]++; // restore
            if (ok) return true;
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean equalFrequency(String word) {
        int[] freq = new int[26];
        for (int i = 0; i < word.length(); i++) {
            freq[word.charAt(i) - 'a']++;
        }
        for (int i = 0; i < word.length(); i++) {
            int idx = word.charAt(i) - 'a';
            freq[idx]--;
            Integer target = null;
            boolean ok = true;
            for (int f : freq) {
                if (f == 0) continue;
                if (target == null) {
                    target = f;
                } else if (f != target) {
                    ok = false;
                    break;
                }
            }
            if (ok) return true;
            freq[idx]++; // restore for next iteration
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        from collections import Counter
        n = len(word)
        for i in range(n):
            cnt = Counter(word)
            cnt[word[i]] -= 1
            if cnt[word[i]] == 0:
                del cnt[word[i]]
            freqs = list(cnt.values())
            if len(set(freqs)) == 1:
                return True
        return False
```

## Python3

```python
class Solution:
    def equalFrequency(self, word: str) -> bool:
        from collections import Counter
        freq = Counter(word)
        counts = list(freq.values())
        cnt = Counter(counts)

        if len(cnt) == 1:
            # all frequencies are the same
            f = next(iter(cnt))
            # can remove one character only if that frequency is 1
            return f == 1

        if len(cnt) == 2:
            (f1, c1), (f2, c2) = cnt.items()
            # case: one character occurs once and can be removed entirely
            if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
                return True
            # case: one frequency is higher by exactly 1 and occurs only once
            if abs(f1 - f2) == 1:
                if (f1 > f2 and c1 == 1) or (f2 > f1 and c2 == 1):
                    return True

        return False
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool equalFrequency(char* word) {
    int freq[26] = {0};
    for (char *p = word; *p; ++p) {
        freq[*p - 'a']++;
    }
    int n = strlen(word);
    for (int i = 0; i < n; ++i) {
        int idx = word[i] - 'a';
        freq[idx]--;
        int target = 0;
        bool ok = true;
        for (int j = 0; j < 26; ++j) {
            if (freq[j] == 0) continue;
            if (target == 0) target = freq[j];
            else if (freq[j] != target) { ok = false; break; }
        }
        freq[idx]++; // restore
        if (ok) return true;
    }
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool EqualFrequency(string word) {
        int[] cnt = new int[26];
        foreach (char c in word) cnt[c - 'a']++;

        char[] arr = word.ToCharArray();
        for (int i = 0; i < arr.Length; i++) {
            cnt[arr[i] - 'a']--;
            if (AllEqual(cnt)) return true;
            cnt[arr[i] - 'a']++;
        }
        return false;

        bool AllEqual(int[] frequencies) {
            int target = -1;
            foreach (int f in frequencies) {
                if (f == 0) continue;
                if (target == -1) target = f;
                else if (f != target) return false;
            }
            return true;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word
 * @return {boolean}
 */
var equalFrequency = function(word) {
    const n = word.length;
    const cnt = new Array(26).fill(0);
    for (let ch of word) cnt[ch.charCodeAt(0) - 97]++;

    const isValid = () => {
        let target = -1;
        for (let f of cnt) {
            if (f === 0) continue;
            if (target === -1) target = f;
            else if (f !== target) return false;
        }
        return true;
    };

    for (let i = 0; i < n; ++i) {
        const idx = word.charCodeAt(i) - 97;
        cnt[idx]--;
        if (isValid()) return true;
        cnt[idx]++;
    }
    return false;
};
```

## Typescript

```typescript
function equalFrequency(word: string): boolean {
    const freq = new Array(26).fill(0);
    for (let i = 0; i < word.length; i++) {
        freq[word.charCodeAt(i) - 97]++;
    }

    for (let i = 0; i < word.length; i++) {
        const idx = word.charCodeAt(i) - 97;
        freq[idx]--;

        let target = -1;
        let ok = true;
        for (const f of freq) {
            if (f === 0) continue;
            if (target === -1) {
                target = f;
            } else if (f !== target) {
                ok = false;
                break;
            }
        }

        if (ok) return true;

        freq[idx]++; // restore
    }

    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param String $word
     * @return Boolean
     */
    function equalFrequency($word) {
        $cnt = array_fill(0, 26, 0);
        $len = strlen($word);
        for ($i = 0; $i < $len; $i++) {
            $idx = ord($word[$i]) - ord('a');
            $cnt[$idx]++;
        }

        for ($i = 0; $i < 26; $i++) {
            if ($cnt[$i] == 0) continue;
            $cnt[$i]--; // remove one occurrence of this letter

            $freqs = [];
            foreach ($cnt as $v) {
                if ($v > 0) $freqs[] = $v;
            }

            $ok = true;
            if (count($freqs) > 0) {
                $first = $freqs[0];
                foreach ($freqs as $f) {
                    if ($f != $first) {
                        $ok = false;
                        break;
                    }
                }
            } else {
                $ok = false; // shouldn't happen with given constraints
            }

            if ($ok) return true;

            $cnt[$i]++; // restore count
        }

        return false;
    }
}
```

## Swift

```swift
class Solution {
    func equalFrequency(_ word: String) -> Bool {
        var freq = [Int](repeating: 0, count: 26)
        let aValue = Character("a").unicodeScalars.first!.value
        for ch in word {
            let idx = Int(ch.unicodeScalars.first!.value - aValue)
            freq[idx] += 1
        }
        let chars = Array(word)
        for i in 0..<chars.count {
            var temp = freq
            let idx = Int(chars[i].unicodeScalars.first!.value - aValue)
            temp[idx] -= 1
            var target: Int? = nil
            var ok = true
            for f in temp where f > 0 {
                if let t = target {
                    if f != t {
                        ok = false
                        break
                    }
                } else {
                    target = f
                }
            }
            if ok { return true }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun equalFrequency(word: String): Boolean {
        val cnt = IntArray(26)
        for (ch in word) {
            cnt[ch - 'a']++
        }
        for (i in 0 until 26) {
            if (cnt[i] == 0) continue
            cnt[i]--
            var target = 0
            var ok = true
            for (c in cnt) {
                if (c == 0) continue
                if (target == 0) {
                    target = c
                } else if (c != target) {
                    ok = false
                    break
                }
            }
            if (ok) return true
            cnt[i]++
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool equalFrequency(String word) {
    List<int> baseFreq = List.filled(26, 0);
    for (int i = 0; i < word.length; i++) {
      baseFreq[word.codeUnitAt(i) - 97]++;
    }

    for (int i = 0; i < word.length; i++) {
      List<int> freq = List.from(baseFreq);
      int idx = word.codeUnitAt(i) - 97;
      freq[idx]--;

      int? target;
      bool ok = true;
      for (int j = 0; j < 26; j++) {
        if (freq[j] > 0) {
          if (target == null) {
            target = freq[j];
          } else if (freq[j] != target) {
            ok = false;
            break;
          }
        }
      }
      if (ok) return true;
    }

    return false;
  }
}
```

## Golang

```go
func equalFrequency(word string) bool {
    var freq [26]int
    for _, ch := range word {
        freq[ch-'a']++
    }
    for i := 0; i < 26; i++ {
        if freq[i] == 0 {
            continue
        }
        freq[i]--
        val := -1
        ok := true
        for j := 0; j < 26; j++ {
            if freq[j] == 0 {
                continue
            }
            if val == -1 {
                val = freq[j]
            } else if freq[j] != val {
                ok = false
                break
            }
        }
        freq[i]++
        if ok {
            return true
        }
    }
    return false
}
```

## Ruby

```ruby
def equal_frequency(word)
  freq = Array.new(26, 0)
  word.each_char { |c| freq[c.ord - 97] += 1 }

  26.times do |i|
    next if freq[i] == 0
    freq[i] -= 1
    vals = freq.select { |v| v > 0 }
    return true if vals.uniq.length == 1
    freq[i] += 1
  end

  false
end
```

## Scala

```scala
object Solution {
    def equalFrequency(word: String): Boolean = {
        val cnt = new Array[Int](26)
        for (ch <- word) {
            cnt(ch - 'a') += 1
        }
        for (i <- 0 until 26 if cnt(i) > 0) {
            cnt(i) -= 1
            var freq = -1
            var ok = true
            for (j <- 0 until 26 if cnt(j) > 0 && ok) {
                if (freq == -1) freq = cnt(j)
                else if (cnt(j) != freq) ok = false
            }
            if (ok && freq != -1) return true
            cnt(i) += 1
        }
        false
    }
}
```

## Rust

```rust
impl Solution {
    pub fn equal_frequency(word: String) -> bool {
        let bytes = word.as_bytes();
        let n = bytes.len();

        for i in 0..n {
            // count frequencies
            let mut cnt = [0i32; 26];
            for &b in bytes.iter() {
                cnt[(b - b'a') as usize] += 1;
            }
            // remove character at position i
            cnt[(bytes[i] - b'a') as usize] -= 1;

            // check if remaining non‑zero frequencies are all equal
            let mut target: Option<i32> = None;
            let mut ok = true;
            for &c in cnt.iter() {
                if c > 0 {
                    match target {
                        Some(t) => {
                            if t != c {
                                ok = false;
                                break;
                            }
                        }
                        None => target = Some(c),
                    }
                }
            }
            if ok {
                return true;
            }
        }
        false
    }
}
```

## Racket

```racket
(define/contract (equal-frequency word)
  (-> string? boolean?)
  (let* ([chars (string->list word)]
         [n (length chars)])
    (let loop ((i 0))
      (if (>= i n)
          #f
          (let ([freq (make-vector 26 0)])
            (for ([idx (in-range n)])
              (when (not (= idx i))
                (define ch (list-ref chars idx))
                (define pos (- (char->integer ch) (char->integer #\a)))
                (vector-set! freq pos (+ 1 (vector-ref freq pos)))))
            (let* ([vals (filter positive? (vector->list freq))])
              (if (apply = vals)
                  #t
                  (loop (+ i 1)))))))))
```

## Erlang

```erlang
-spec equal_frequency(Word :: unicode:unicode_binary()) -> boolean().
equal_frequency(Word) ->
    FreqMap = build_freq_map(unicode:characters_to_list(Word), #{}),
    lists:any(fun({K, C}) ->
        SimMap = if
            C == 1 -> maps:remove(K, FreqMap);
            true   -> maps:put(K, C - 1, FreqMap)
        end,
        frequencies_equal(SimMap)
    end, maps:to_list(FreqMap)).

build_freq_map([], Acc) ->
    Acc;
build_freq_map([Char | Rest], Acc) ->
    Key = Char - $a,
    NewAcc = maps:update_with(Key, fun(V) -> V + 1 end, 1, Acc),
    build_freq_map(Rest, NewAcc).

frequencies_equal(Map) ->
    Counts = [V || {_K, V} <- maps:to_list(Map)],
    case Counts of
        [] -> true;
        _  -> length(lists:usort(Counts)) == 1
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec equal_frequency(String.t()) :: boolean()
  def equal_frequency(word) do
    freq =
      word
      |> :binary.bin_to_list()
      |> Enum.reduce(List.duplicate(0, 26), fn char, acc ->
        idx = char - ?a
        List.update_at(acc, idx, &(&1 + 1))
      end)

    Enum.any?(0..25, fn i ->
      cnt = Enum.at(freq, i)

      if cnt == 0 do
        false
      else
        new_freq = List.update_at(freq, i, &(&1 - 1))

        counts =
          new_freq
          |> Enum.filter(fn x -> x > 0 end)

        case counts do
          [] -> false
          _ ->
            uniq = Enum.uniq(counts)
            length(uniq) == 1
        end
      end
    end)
  end
end
```
