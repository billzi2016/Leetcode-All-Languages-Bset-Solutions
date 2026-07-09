# 1657. Determine if Two Strings Are Close

## Cpp

```cpp
class Solution {
public:
    bool closeStrings(string word1, string word2) {
        if (word1.size() != word2.size()) return false;
        int cnt1[26] = {0}, cnt2[26] = {0};
        for (char c : word1) ++cnt1[c - 'a'];
        for (char c : word2) ++cnt2[c - 'a'];
        vector<int> freq1, freq2;
        for (int i = 0; i < 26; ++i) {
            if ((cnt1[i] == 0) != (cnt2[i] == 0)) return false;
            if (cnt1[i]) freq1.push_back(cnt1[i]);
            if (cnt2[i]) freq2.push_back(cnt2[i]);
        }
        sort(freq1.begin(), freq1.end());
        sort(freq2.begin(), freq2.end());
        return freq1 == freq2;
    }
};
```

## Java

```java
class Solution {
    public boolean closeStrings(String word1, String word2) {
        if (word1.length() != word2.length()) return false;
        int[] cnt1 = new int[26];
        int[] cnt2 = new int[26];
        for (int i = 0; i < word1.length(); i++) {
            cnt1[word1.charAt(i) - 'a']++;
            cnt2[word2.charAt(i) - 'a']++;
        }
        // Check same character set
        for (int i = 0; i < 26; i++) {
            if ((cnt1[i] == 0) != (cnt2[i] == 0)) return false;
        }
        // Collect non-zero frequencies
        int[] freq1 = new int[26];
        int[] freq2 = new int[26];
        int idx1 = 0, idx2 = 0;
        for (int i = 0; i < 26; i++) {
            if (cnt1[i] > 0) freq1[idx1++] = cnt1[i];
            if (cnt2[i] > 0) freq2[idx2++] = cnt2[i];
        }
        java.util.Arrays.sort(freq1, 0, idx1);
        java.util.Arrays.sort(freq2, 0, idx2);
        if (idx1 != idx2) return false;
        for (int i = 0; i < idx1; i++) {
            if (freq1[i] != freq2[i]) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False
        from collections import Counter
        c1 = Counter(word1)
        c2 = Counter(word2)
        if set(c1.keys()) != set(c2.keys()):
            return False
        return sorted(c1.values()) == sorted(c2.values())
```

## Python3

```python
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        from collections import Counter
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        # The set of characters must be identical
        if set(cnt1.keys()) != set(cnt2.keys()):
            return False
        # The multiset of frequencies must be identical (order can differ)
        return sorted(cnt1.values()) == sorted(cnt2.values())
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool closeStrings(char* word1, char* word2) {
    int n1 = strlen(word1);
    int n2 = strlen(word2);
    if (n1 != n2) return false;

    int cnt1[26] = {0};
    int cnt2[26] = {0};

    for (int i = 0; i < n1; ++i) {
        cnt1[word1[i] - 'a']++;
    }
    for (int i = 0; i < n2; ++i) {
        cnt2[word2[i] - 'a']++;
    }

    // Ensure both strings have the same set of characters
    for (int i = 0; i < 26; ++i) {
        if ((cnt1[i] == 0) != (cnt2[i] == 0))
            return false;
    }

    // Sort frequency arrays (only 26 elements, simple insertion sort)
    for (int i = 1; i < 26; ++i) {
        int key = cnt1[i];
        int j = i - 1;
        while (j >= 0 && cnt1[j] > key) {
            cnt1[j + 1] = cnt1[j];
            --j;
        }
        cnt1[j + 1] = key;
    }

    for (int i = 1; i < 26; ++i) {
        int key = cnt2[i];
        int j = i - 1;
        while (j >= 0 && cnt2[j] > key) {
            cnt2[j + 1] = cnt2[j];
            --j;
        }
        cnt2[j + 1] = key;
    }

    // Compare sorted frequency arrays
    for (int i = 0; i < 26; ++i) {
        if (cnt1[i] != cnt2[i])
            return false;
    }

    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool CloseStrings(string word1, string word2) {
        if (word1.Length != word2.Length) return false;

        int[] cnt1 = new int[26];
        int[] cnt2 = new int[26];

        foreach (char c in word1) cnt1[c - 'a']++;
        foreach (char c in word2) cnt2[c - 'a']++;

        for (int i = 0; i < 26; i++) {
            if ((cnt1[i] == 0) != (cnt2[i] == 0))
                return false;
        }

        var freq1 = new List<int>();
        var freq2 = new List<int>();

        for (int i = 0; i < 26; i++) {
            if (cnt1[i] > 0) freq1.Add(cnt1[i]);
            if (cnt2[i] > 0) freq2.Add(cnt2[i]);
        }

        freq1.Sort();
        freq2.Sort();

        if (freq1.Count != freq2.Count) return false;

        for (int i = 0; i < freq1.Count; i++) {
            if (freq1[i] != freq2[i]) return false;
        }

        return true;
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
var closeStrings = function(word1, word2) {
    if (word1.length !== word2.length) return false;
    
    const freq1 = new Array(26).fill(0);
    const freq2 = new Array(26).fill(0);
    const aCode = 'a'.charCodeAt(0);
    
    for (let i = 0; i < word1.length; ++i) {
        freq1[word1.charCodeAt(i) - aCode]++;
        freq2[word2.charCodeAt(i) - aCode]++;
    }
    
    const counts1 = [];
    const counts2 = [];
    
    for (let i = 0; i < 26; ++i) {
        if ((freq1[i] === 0) !== (freq2[i] === 0)) return false;
        if (freq1[i] > 0) counts1.push(freq1[i]);
        if (freq2[i] > 0) counts2.push(freq2[i]);
    }
    
    counts1.sort((a, b) => a - b);
    counts2.sort((a, b) => a - b);
    
    if (counts1.length !== counts2.length) return false;
    for (let i = 0; i < counts1.length; ++i) {
        if (counts1[i] !== counts2[i]) return false;
    }
    return true;
};
```

## Typescript

```typescript
function closeStrings(word1: string, word2: string): boolean {
    if (word1.length !== word2.length) return false;

    const freq1 = new Array(26).fill(0);
    const freq2 = new Array(26).fill(0);

    for (const ch of word1) {
        freq1[ch.charCodeAt(0) - 97]++;
    }
    for (const ch of word2) {
        freq2[ch.charCodeAt(0) - 97]++;
    }

    // Ensure both strings contain the same set of characters
    for (let i = 0; i < 26; i++) {
        if ((freq1[i] === 0) !== (freq2[i] === 0)) return false;
    }

    const counts1: number[] = [];
    const counts2: number[] = [];

    for (let i = 0; i < 26; i++) {
        if (freq1[i] > 0) counts1.push(freq1[i]);
        if (freq2[i] > 0) counts2.push(freq2[i]);
    }

    counts1.sort((a, b) => a - b);
    counts2.sort((a, b) => a - b);

    if (counts1.length !== counts2.length) return false;

    for (let i = 0; i < counts1.length; i++) {
        if (counts1[i] !== counts2[i]) return false;
    }

    return true;
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
    function closeStrings($word1, $word2) {
        if (strlen($word1) !== strlen($word2)) {
            return false;
        }

        $cnt1 = array_fill(0, 26, 0);
        $cnt2 = array_fill(0, 26, 0);

        $len = strlen($word1);
        for ($i = 0; $i < $len; $i++) {
            $cnt1[ord($word1[$i]) - 97]++;
            $cnt2[ord($word2[$i]) - 97]++;
        }

        // Check if both strings have the same set of characters
        for ($i = 0; $i < 26; $i++) {
            if (($cnt1[$i] > 0 && $cnt2[$i] == 0) || ($cnt2[$i] > 0 && $cnt1[$i] == 0)) {
                return false;
            }
        }

        // Collect frequencies (ignore zeros)
        $freq1 = [];
        $freq2 = [];
        for ($i = 0; $i < 26; $i++) {
            if ($cnt1[$i] > 0) {
                $freq1[] = $cnt1[$i];
            }
            if ($cnt2[$i] > 0) {
                $freq2[] = $cnt2[$i];
            }
        }

        sort($freq1);
        sort($freq2);

        return $freq1 === $freq2;
    }
}
```

## Swift

```swift
class Solution {
    func closeStrings(_ word1: String, _ word2: String) -> Bool {
        if word1.count != word2.count { return false }
        
        var cnt1 = [Int](repeating: 0, count: 26)
        var cnt2 = [Int](repeating: 0, count: 26)
        
        for byte in word1.utf8 {
            let idx = Int(byte - 97) // 'a' ASCII is 97
            cnt1[idx] += 1
        }
        for byte in word2.utf8 {
            let idx = Int(byte - 97)
            cnt2[idx] += 1
        }
        
        // Ensure both strings have the same set of characters
        for i in 0..<26 {
            if (cnt1[i] == 0) != (cnt2[i] == 0) {
                return false
            }
        }
        
        var freq1 = [Int]()
        var freq2 = [Int]()
        for i in 0..<26 {
            if cnt1[i] > 0 { freq1.append(cnt1[i]) }
            if cnt2[i] > 0 { freq2.append(cnt2[i]) }
        }
        
        freq1.sort()
        freq2.sort()
        
        return freq1 == freq2
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun closeStrings(word1: String, word2: String): Boolean {
        if (word1.length != word2.length) return false
        val cnt1 = IntArray(26)
        val cnt2 = IntArray(26)
        for (c in word1) cnt1[c - 'a']++
        for (c in word2) cnt2[c - 'a']++
        for (i in 0 until 26) {
            if ((cnt1[i] == 0) != (cnt2[i] == 0)) return false
        }
        cnt1.sort()
        cnt2.sort()
        for (i in 0 until 26) {
            if (cnt1[i] != cnt2[i]) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool closeStrings(String word1, String word2) {
    if (word1.length != word2.length) return false;

    List<int> cnt1 = List.filled(26, 0);
    List<int> cnt2 = List.filled(26, 0);

    for (int i = 0; i < word1.length; ++i) {
      cnt1[word1.codeUnitAt(i) - 97]++;
      cnt2[word2.codeUnitAt(i) - 97]++;
    }

    // Same set of characters
    for (int i = 0; i < 26; ++i) {
      if ((cnt1[i] == 0) != (cnt2[i] == 0)) return false;
    }

    List<int> freq1 = [];
    List<int> freq2 = [];

    for (int i = 0; i < 26; ++i) {
      if (cnt1[i] > 0) freq1.add(cnt1[i]);
      if (cnt2[i] > 0) freq2.add(cnt2[i]);
    }

    freq1.sort();
    freq2.sort();

    if (freq1.length != freq2.length) return false;
    for (int i = 0; i < freq1.length; ++i) {
      if (freq1[i] != freq2[i]) return false;
    }
    return true;
  }
}
```

## Golang

```go
package main

import "sort"

func closeStrings(word1 string, word2 string) bool {
	if len(word1) != len(word2) {
		return false
	}
	var cnt1 [26]int
	var cnt2 [26]int
	for _, ch := range word1 {
		cnt1[ch-'a']++
	}
	for _, ch := range word2 {
		cnt2[ch-'a']++
	}
	for i := 0; i < 26; i++ {
		if (cnt1[i] == 0) != (cnt2[i] == 0) {
			return false
		}
	}
	freq1 := make([]int, 0, 26)
	freq2 := make([]int, 0, 26)
	for i := 0; i < 26; i++ {
		if cnt1[i] > 0 {
			freq1 = append(freq1, cnt1[i])
		}
		if cnt2[i] > 0 {
			freq2 = append(freq2, cnt2[i])
		}
	}
	sort.Ints(freq1)
	sort.Ints(freq2)
	if len(freq1) != len(freq2) {
		return false
	}
	for i := range freq1 {
		if freq1[i] != freq2[i] {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def close_strings(word1, word2)
  return false unless word1.length == word2.length

  cnt1 = Array.new(26, 0)
  cnt2 = Array.new(26, 0)

  word1.each_byte { |b| cnt1[b - 97] += 1 }
  word2.each_byte { |b| cnt2[b - 97] += 1 }

  26.times do |i|
    return false if (cnt1[i] == 0) != (cnt2[i] == 0)
  end

  freq1 = cnt1.select { |c| c > 0 }.sort
  freq2 = cnt2.select { |c| c > 0 }.sort

  freq1 == freq2
end
```

## Scala

```scala
object Solution {
    def closeStrings(word1: String, word2: String): Boolean = {
        if (word1.length != word2.length) return false

        val freq1 = new Array[Int](26)
        val freq2 = new Array[Int](26)

        for (c <- word1) freq1(c - 'a') += 1
        for (c <- word2) freq2(c - 'a') += 1

        for (i <- 0 until 26) {
            if ((freq1(i) > 0) != (freq2(i) > 0)) return false
        }

        val sorted1 = freq1.filter(_ > 0).sorted
        val sorted2 = freq2.filter(_ > 0).sorted

        if (sorted1.length != sorted2.length) return false
        for (i <- sorted1.indices) {
            if (sorted1(i) != sorted2(i)) return false
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn close_strings(word1: String, word2: String) -> bool {
        if word1.len() != word2.len() {
            return false;
        }
        let mut cnt1 = [0i32; 26];
        let mut cnt2 = [0i32; 26];

        for b in word1.bytes() {
            cnt1[(b - b'a') as usize] += 1;
        }
        for b in word2.bytes() {
            cnt2[(b - b'a') as usize] += 1;
        }

        // Same set of characters required
        for i in 0..26 {
            if (cnt1[i] == 0) != (cnt2[i] == 0) {
                return false;
            }
        }

        let mut freq1: Vec<i32> = cnt1.iter().cloned().filter(|&x| x > 0).collect();
        let mut freq2: Vec<i32> = cnt2.iter().cloned().filter(|&x| x > 0).collect();

        freq1.sort_unstable();
        freq2.sort_unstable();

        freq1 == freq2
    }
}
```

## Racket

```racket
(define/contract (close-strings word1 word2)
  (-> string? string? boolean?)
  (let ([len1 (string-length word1)]
        [len2 (string-length word2)])
    (if (not (= len1 len2))
        #f
        (let* ([cnt1 (make-vector 26 0)]
               [cnt2 (make-vector 26 0)])
          (for ([i (in-range len1)])
            (let* ([c (string-ref word1 i)]
                   [idx (- (char->integer c) (char->integer #\a))])
              (vector-set! cnt1 idx (+ 1 (vector-ref cnt1 idx)))))
          (for ([i (in-range len2)])
            (let* ([c (string-ref word2 i)]
                   [idx (- (char->integer c) (char->integer #\a))])
              (vector-set! cnt2 idx (+ 1 (vector-ref cnt2 idx)))))
          ;; ensure both strings contain exactly the same set of characters
          (define same-set?
            (for/and ([i (in-range 26)])
              (or (and (= (vector-ref cnt1 i) 0) (= (vector-ref cnt2 i) 0))
                  (and (> (vector-ref cnt1 i) 0) (> (vector-ref cnt2 i) 0)))))
          (if (not same-set?)
              #f
              (let* ([freq1 (filter positive? (vector->list cnt1))]
                     [freq2 (filter positive? (vector->list cnt2))])
                (equal? (sort freq1 <) (sort freq2 <))))))))
```

## Erlang

```erlang
-module(solution).
-export([close_strings/2]).

-spec close_strings(Word1 :: unicode:unicode_binary(), Word2 :: unicode:unicode_binary()) -> boolean().
close_strings(Word1, Word2) ->
    if byte_size(Word1) =/= byte_size(Word2) ->
            false;
       true ->
            M1 = freq_map(Word1),
            M2 = freq_map(Word2),
            case lists:sort(maps:keys(M1)) =:= lists:sort(maps:keys(M2)) of
                false -> false;
                true ->
                    lists:sort(maps:values(M1)) =:= lists:sort(maps:values(M2))
            end
    end.

freq_map(String) -> freq_map(String, #{}).

freq_map(<<>>, Map) -> Map;
freq_map(<<C, Rest/binary>>, Map) when C >= $a, C =< $z ->
    NewMap = maps:update_with(C,
                               fun(V) -> V + 1 end,
                               1,
                               Map),
    freq_map(Rest, NewMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec close_strings(word1 :: String.t(), word2 :: String.t()) :: boolean()
  def close_strings(word1, word2) do
    if String.length(word1) != String.length(word2) do
      false
    else
      freq1 = count_freq(word1)
      freq2 = count_freq(word2)

      same_set? =
        Enum.zip(freq1, freq2)
        |> Enum.all?(fn {a, b} -> (a == 0 and b == 0) or (a > 0 and b > 0) end)

      if same_set? do
        Enum.sort(freq1) == Enum.sort(freq2)
      else
        false
      end
    end
  end

  defp count_freq(str) do
    String.to_charlist(str)
    |> Enum.reduce(List.duplicate(0, 26), fn c, acc ->
      idx = c - ?a
      List.update_at(acc, idx, &(&1 + 1))
    end)
  end
end
```
