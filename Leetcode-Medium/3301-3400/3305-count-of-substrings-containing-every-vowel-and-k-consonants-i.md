# 3305. Count of Substrings Containing Every Vowel and K Consonants I

## Cpp

```cpp
class Solution {
public:
    int countOfSubstrings(string word, int k) {
        int n = word.size();
        int ans = 0;
        auto vowelIdx = [&](char c) -> int {
            if (c == 'a') return 0;
            if (c == 'e') return 1;
            if (c == 'i') return 2;
            if (c == 'o') return 3;
            if (c == 'u') return 4;
            return -1;
        };
        const int ALL = (1 << 5) - 1; // 31
        for (int i = 0; i < n; ++i) {
            int cons = 0, mask = 0;
            for (int j = i; j < n; ++j) {
                int idx = vowelIdx(word[j]);
                if (idx == -1) {
                    ++cons;
                    if (cons > k) break;
                } else {
                    mask |= (1 << idx);
                }
                if (mask == ALL && cons == k) ++ans;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countOfSubstrings(String word, int k) {
        int n = word.length();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            boolean[] seen = new boolean[5];
            int vowelCnt = 0;
            int cons = 0;
            for (int j = i; j < n; j++) {
                char ch = word.charAt(j);
                switch (ch) {
                    case 'a':
                        if (!seen[0]) { seen[0] = true; vowelCnt++; }
                        break;
                    case 'e':
                        if (!seen[1]) { seen[1] = true; vowelCnt++; }
                        break;
                    case 'i':
                        if (!seen[2]) { seen[2] = true; vowelCnt++; }
                        break;
                    case 'o':
                        if (!seen[3]) { seen[3] = true; vowelCnt++; }
                        break;
                    case 'u':
                        if (!seen[4]) { seen[4] = true; vowelCnt++; }
                        break;
                    default:
                        cons++;
                }
                if (cons > k) {
                    break;
                }
                if (vowelCnt == 5 && cons == k) {
                    ans++;
                }
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        n = len(word)
        vowels = {'a':1, 'e':2, 'i':4, 'o':8, 'u':16}
        full_mask = 31  # 0b11111
        ans = 0

        for i in range(n):
            mask = 0
            cons = 0
            for j in range(i, n):
                ch = word[j]
                if ch in vowels:
                    mask |= vowels[ch]
                else:
                    cons += 1
                    if cons > k:
                        break
                if mask == full_mask and cons == k:
                    ans += 1
        return ans
```

## Python3

```python
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowel_to_bit = {'a':1, 'e':2, 'i':4, 'o':8, 'u':16}
        full_mask = 31
        n = len(word)
        ans = 0
        for i in range(n):
            mask = 0
            cons = 0
            for j in range(i, n):
                ch = word[j]
                if ch in vowel_to_bit:
                    mask |= vowel_to_bit[ch]
                else:
                    cons += 1
                    if cons > k:
                        break
                if mask == full_mask and cons == k:
                    ans += 1
        return ans
```

## C

```c
#include <string.h>

int countOfSubstrings(char* word, int k) {
    int n = (int)strlen(word);
    int total = 0;
    const int FULL_MASK = 31; // 0b11111 for a,e,i,o,u

    for (int i = 0; i < n; ++i) {
        int mask = 0;
        int cons = 0;
        for (int j = i; j < n; ++j) {
            char c = word[j];
            if (c == 'a') mask |= 1 << 0;
            else if (c == 'e') mask |= 1 << 1;
            else if (c == 'i') mask |= 1 << 2;
            else if (c == 'o') mask |= 1 << 3;
            else if (c == 'u') mask |= 1 << 4;
            else cons++;

            if (cons > k) break;
            if (mask == FULL_MASK && cons == k) ++total;
        }
    }

    return total;
}
```

## Csharp

```csharp
public class Solution {
    public int CountOfSubstrings(string word, int k) {
        int n = word.Length;
        // vowel order: a e i o u
        int[,] prefVowel = new int[5, n + 1];
        int[] prefCons = new int[n + 1];

        for (int i = 0; i < n; i++) {
            // copy previous counts
            for (int v = 0; v < 5; v++) {
                prefVowel[v, i + 1] = prefVowel[v, i];
            }
            prefCons[i + 1] = prefCons[i];

            char c = word[i];
            switch (c) {
                case 'a':
                    prefVowel[0, i + 1]++;
                    break;
                case 'e':
                    prefVowel[1, i + 1]++;
                    break;
                case 'i':
                    prefVowel[2, i + 1]++;
                    break;
                case 'o':
                    prefVowel[3, i + 1]++;
                    break;
                case 'u':
                    prefVowel[4, i + 1]++;
                    break;
                default:
                    prefCons[i + 1]++;
                    break;
            }
        }

        int count = 0;
        for (int start = 0; start < n; start++) {
            // early stop: remaining length must be at least 5
            if (n - start < 5) break;
            for (int end = start + 4; end < n; end++) { // minimum length 5 to have all vowels
                int cons = prefCons[end + 1] - prefCons[start];
                if (cons != k) continue;

                bool allVowels = true;
                for (int v = 0; v < 5; v++) {
                    if (prefVowel[v, end + 1] - prefVowel[v, start] == 0) {
                        allVowels = false;
                        break;
                    }
                }
                if (allVowels) count++;
            }
        }

        return count;
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
var countOfSubstrings = function(word, k) {
    const n = word.length;
    const vowelBit = {
        'a': 1 << 0,
        'e': 1 << 1,
        'i': 1 << 2,
        'o': 1 << 3,
        'u': 1 << 4
    };
    const fullMask = (1 << 5) - 1; // 31
    
    let ans = 0;
    
    for (let i = 0; i < n; ++i) {
        let mask = 0;
        let cons = 0;
        for (let j = i; j < n; ++j) {
            const ch = word[j];
            if (vowelBit.hasOwnProperty(ch)) {
                mask |= vowelBit[ch];
            } else {
                cons++;
                if (cons > k) break; // cannot satisfy exactly k anymore
            }
            if (mask === fullMask && cons === k) {
                ans++;
            }
        }
    }
    
    return ans;
};
```

## Typescript

```typescript
function countOfSubstrings(word: string, k: number): number {
    const vowelBit: { [ch: string]: number } = { a: 1, e: 2, i: 4, o: 8, u: 16 };
    const fullMask = 1 | 2 | 4 | 8 | 16; // 31
    const n = word.length;
    let ans = 0;

    for (let i = 0; i < n; ++i) {
        let mask = 0;
        let cons = 0;
        for (let j = i; j < n; ++j) {
            const ch = word[j];
            if (vowelBit[ch] !== undefined) {
                mask |= vowelBit[ch];
            } else {
                ++cons;
            }
            if (cons > k) break;
            if (cons === k && mask === fullMask) ++ans;
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
     * @param Integer $k
     * @return Integer
     */
    function countOfSubstrings($word, $k) {
        $n = strlen($word);
        $ans = 0;
        $vowelBit = ['a'=>1,'e'=>2,'i'=>4,'o'=>8,'u'=>16];
        for ($i = 0; $i < $n; $i++) {
            $mask = 0;
            $cons = 0;
            for ($j = $i; $j < $n; $j++) {
                $ch = $word[$j];
                if (isset($vowelBit[$ch])) {
                    $mask |= $vowelBit[$ch];
                } else {
                    $cons++;
                    if ($cons > $k) {
                        break;
                    }
                }
                if ($mask == 31 && $cons == $k) {
                    $ans++;
                }
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countOfSubstrings(_ word: String, _ k: Int) -> Int {
        let chars = Array(word)
        let n = chars.count
        var result = 0
        
        for i in 0..<n {
            var vowelSeen = [false, false, false, false, false] // a e i o u
            var consonants = 0
            
            for j in i..<n {
                let c = chars[j]
                switch c {
                case "a":
                    vowelSeen[0] = true
                case "e":
                    vowelSeen[1] = true
                case "i":
                    vowelSeen[2] = true
                case "o":
                    vowelSeen[3] = true
                case "u":
                    vowelSeen[4] = true
                default:
                    consonants += 1
                }
                
                if consonants > k {
                    break
                }
                
                // check all vowels present
                var allVowels = true
                for seen in vowelSeen {
                    if !seen {
                        allVowels = false
                        break
                    }
                }
                
                if allVowels && consonants == k {
                    result += 1
                }
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countOfSubstrings(word: String, k: Int): Int {
        val n = word.length
        var ans = 0
        for (i in 0 until n) {
            var a = false
            var e = false
            var iV = false
            var o = false
            var u = false
            var cons = 0
            for (j in i until n) {
                when (word[j]) {
                    'a' -> a = true
                    'e' -> e = true
                    'i' -> iV = true
                    'o' -> o = true
                    'u' -> u = true
                    else -> cons++
                }
                if (cons > k) break
                if (a && e && iV && o && u && cons == k) ans++
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int countOfSubstrings(String word, int k) {
    const vowelSet = {'a', 'e', 'i', 'o', 'u'};
    int n = word.length;
    int ans = 0;

    for (int i = 0; i < n; i++) {
      int consonants = 0;
      var seen = {'a': false, 'e': false, 'i': false, 'o': false, 'u': false};

      for (int j = i; j < n; j++) {
        String ch = word[j];
        if (vowelSet.contains(ch)) {
          seen[ch] = true;
        } else {
          consonants++;
          if (consonants > k) break;
        }

        if (consonants == k && seen.values.every((v) => v)) {
          ans++;
        }
      }
    }

    return ans;
  }
}
```

## Golang

```go
func countOfSubstrings(word string, k int) int {
	n := len(word)
	const fullMask = 1<<5 - 1 // 0b11111
	ans := 0

	for i := 0; i < n; i++ {
		mask := 0
		consonants := 0
		for j := i; j < n; j++ {
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
			default:
				consonants++
			}
			if consonants > k {
				break
			}
			if mask == fullMask && consonants == k {
				ans++
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def count_of_substrings(word, k)
  n = word.length
  vowels = %w[a e i o u]
  ans = 0

  (0...n).each do |i|
    vowel_counts = Hash.new(0)
    cons = 0
    (i...n).each do |j|
      ch = word[j]
      if ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u'
        vowel_counts[ch] += 1
      else
        cons += 1
      end
      break if cons > k
      if cons == k && vowels.all? { |v| vowel_counts[v] > 0 }
        ans += 1
      end
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def countOfSubstrings(word: String, k: Int): Int = {
        val n = word.length
        val vowels = Set('a', 'e', 'i', 'o', 'u')
        var result = 0

        for (i <- 0 until n) {
            var cntA = 0
            var cntE = 0
            var cntI = 0
            var cntO = 0
            var cntU = 0
            var consonants = 0
            var j = i

            while (j < n && consonants <= k) {
                val ch = word.charAt(j)
                if (vowels.contains(ch)) {
                    ch match {
                        case 'a' => cntA += 1
                        case 'e' => cntE += 1
                        case 'i' => cntI += 1
                        case 'o' => cntO += 1
                        case 'u' => cntU += 1
                    }
                } else {
                    consonants += 1
                }

                if (cntA > 0 && cntE > 0 && cntI > 0 && cntO > 0 && cntU > 0 && consonants == k) {
                    result += 1
                }
                j += 1
            }
        }

        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_of_substrings(word: String, k: i32) -> i32 {
        let bytes = word.as_bytes();
        let n = bytes.len();
        let k_usize = k as usize;

        // prefix counts for consonants and each vowel
        let mut pref_cons = vec![0usize; n + 1];
        let mut pref_vowel = vec![[0usize; 5]; n + 1];

        for i in 0..n {
            let c = bytes[i] as char;
            // copy previous counts
            pref_cons[i + 1] = pref_cons[i];
            pref_vowel[i + 1] = pref_vowel[i];

            match c {
                'a' => {
                    pref_vowel[i + 1][0] += 1;
                }
                'e' => {
                    pref_vowel[i + 1][1] += 1;
                }
                'i' => {
                    pref_vowel[i + 1][2] += 1;
                }
                'o' => {
                    pref_vowel[i + 1][3] += 1;
                }
                'u' => {
                    pref_vowel[i + 1][4] += 1;
                }
                _ => {
                    // consonant
                    pref_cons[i + 1] += 1;
                }
            }
        }

        let mut ans: usize = 0;

        for i in 0..n {
            // minimum length to contain all five vowels is 5
            for j in (i + 4)..n {
                let cons = pref_cons[j + 1] - pref_cons[i];
                if cons != k_usize {
                    continue;
                }
                let mut ok = true;
                for v in 0..5 {
                    if pref_vowel[j + 1][v] - pref_vowel[i][v] == 0 {
                        ok = false;
                        break;
                    }
                }
                if ok {
                    ans += 1;
                }
            }
        }

        ans as i32
    }
}
```

## Racket

```racket
#lang racket

(define/contract (count-of-substrings word k)
  (-> string? exact-integer? exact-integer?)
  (let* ([n (string-length word)]
         [pref-cons (make-vector (+ n 1) 0)]
         [pref-a    (make-vector (+ n 1) 0)]
         [pref-e    (make-vector (+ n 1) 0)]
         [pref-i    (make-vector (+ n 1) 0)]
         [pref-o    (make-vector (+ n 1) 0)]
         [pref-u    (make-vector (+ n 1) 0)])
    ;; build prefix sums
    (for ([idx (in-range n)])
      (define ch (string-ref word idx))
      (vector-set! pref-cons (+ idx 1)
                   (+ (vector-ref pref-cons idx)
                      (if (member ch '(#\a #\e #\i #\o #\u)) 0 1)))
      (vector-set! pref-a (+ idx 1)
                   (+ (vector-ref pref-a idx) (if (char=? ch #\a) 1 0)))
      (vector-set! pref-e (+ idx 1)
                   (+ (vector-ref pref-e idx) (if (char=? ch #\e) 1 0)))
      (vector-set! pref-i (+ idx 1)
                   (+ (vector-ref pref-i idx) (if (char=? ch #\i) 1 0)))
      (vector-set! pref-o (+ idx 1)
                   (+ (vector-ref pref-o idx) (if (char=? ch #\o) 1 0)))
      (vector-set! pref-u (+ idx 1)
                   (+ (vector-ref pref-u idx) (if (char=? ch #\u) 1 0))))
    (let ([ans 0])
      (for ([l (in-range n)])
        (for ([r (in-range l n)])
          (define cons
            (- (vector-ref pref-cons (+ r 1))
               (vector-ref pref-cons l)))
          (when (= cons k)
            (define has-a (> (- (vector-ref pref-a (+ r 1))
                                (vector-ref pref-a l)) 0))
            (define has-e (> (- (vector-ref pref-e (+ r 1))
                                (vector-ref pref-e l)) 0))
            (define has-i (> (- (vector-ref pref-i (+ r 1))
                                (vector-ref pref-i l)) 0))
            (define has-o (> (- (vector-ref pref-o (+ r 1))
                                (vector-ref pref-o l)) 0))
            (define has-u (> (- (vector-ref pref-u (+ r 1))
                                (vector-ref pref-u l)) 0))
            (when (and has-a has-e has-i has-o has-u)
              (set! ans (+ ans 1))))))
      ans)))
```

## Erlang

```erlang
-module(solution).
-export([count_of_substrings/2]).

-spec count_of_substrings(Word :: unicode:unicode_binary(), K :: integer()) -> integer().
count_of_substrings(Word, K) ->
    List = unicode:characters_to_list(Word),
    N = length(List),
    count_start(List, N, K, 0, 0).

%% iterate over start positions
count_start(_List, _N, _K, Index, Acc) when Index >= _N ->
    Acc;
count_start(List, N, K, Index, Acc) ->
    CountStart = count_end(List, N, K, Index, Index, 0, 0),
    count_start(List, N, K, Index + 1, Acc + CountStart).

%% iterate over end positions for a fixed start
count_end(_List, _N, _K, _StartIdx, EndIdx, _VMask, _CntCons) when EndIdx >= _N ->
    0;
count_end(List, N, K, StartIdx, EndIdx, VMask, CntCons) ->
    Char = lists:nth(EndIdx + 1, List),
    case vowel_bit(Char) of
        0 -> % consonant
            NewCons = CntCons + 1,
            if NewCons > K ->
                    0;
               true ->
                    Add = if VMask == 31 andalso NewCons == K -> 1 else 0 end,
                    Add + count_end(List, N, K, StartIdx, EndIdx + 1, VMask, NewCons)
            end;
        Bit -> % vowel
            NewMask = VMask bor Bit,
            Add = if NewMask == 31 andalso CntCons == K -> 1 else 0 end,
            Add + count_end(List, N, K, StartIdx, EndIdx + 1, NewMask, CntCons)
    end.

%% map vowel character to bit mask
vowel_bit($a) -> 1;
vowel_bit($e) -> 2;
vowel_bit($i) -> 4;
vowel_bit($o) -> 8;
vowel_bit($u) -> 16;
vowel_bit(_)   -> 0.
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec count_of_substrings(word :: String.t(), k :: integer) :: integer
  def count_of_substrings(word, k) do
    chars = String.graphemes(word)
    n = length(chars)
    all_mask = 31

    Enum.reduce(0..(n - 1), 0, fn i, acc ->
      cnt = expand(i, chars, n, k, all_mask)
      acc + cnt
    end)
  end

  defp expand(start, chars, n, k, all_mask) do
    Enum.reduce_while(start..(n - 1), {0, 0, 0}, fn idx, {cnt, mask, cons} ->
      c = Enum.at(chars, idx)

      {new_mask, new_cons} =
        case c do
          "a" -> {mask ||| 1, cons}
          "e" -> {mask ||| 2, cons}
          "i" -> {mask ||| 4, cons}
          "o" -> {mask ||| 8, cons}
          "u" -> {mask ||| 16, cons}
          _   -> {mask, cons + 1}
        end

      if new_cons > k do
        {:halt, {cnt, new_mask, new_cons}}
      else
        new_cnt = if new_mask == all_mask and new_cons == k, do: cnt + 1, else: cnt
        {:cont, {new_cnt, new_mask, new_cons}}
      end
    end)
    |> elem(0)
  end
end
```
