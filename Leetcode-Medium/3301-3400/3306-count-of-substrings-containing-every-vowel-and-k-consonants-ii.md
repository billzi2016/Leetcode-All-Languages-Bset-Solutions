# 3306. Count of Substrings Containing Every Vowel and K Consonants II

## Cpp

```cpp
class Solution {
public:
    long long countAtLeast(const string& s, int k) {
        if (k < 0) return 0;
        int n = s.size();
        long long ans = 0;
        int cnt[5] = {0};
        int distinct = 0;
        int cons = 0;
        auto idx = [&](char c)->int{
            switch(c){
                case 'a': return 0;
                case 'e': return 1;
                case 'i': return 2;
                case 'o': return 3;
                case 'u': return 4;
            }
            return -1;
        };
        int left = 0;
        for (int right = 0; right < n; ++right) {
            int id = idx(s[right]);
            if (id != -1) {
                if (++cnt[id] == 1) ++distinct;
            } else {
                ++cons;
            }
            while (distinct == 5 && cons >= k) {
                ans += (long long)(n - right);
                int lid = idx(s[left]);
                if (lid != -1) {
                    if (--cnt[lid] == 0) --distinct;
                } else {
                    --cons;
                }
                ++left;
            }
        }
        return ans;
    }

    long long countOfSubstrings(string word, int k) {
        return countAtLeast(word, k) - countAtLeast(word, k + 1);
    }
};
```

## Java

```java
class Solution {
    public long countOfSubstrings(String word, int k) {
        return atLeastK(word, k) - atLeastK(word, k + 1);
    }

    private long atLeastK(String s, int K) {
        if (K < 0) return 0;
        int n = s.length();
        int[] vowelCnt = new int[5]; // a,e,i,o,u
        int distinctVowels = 0;
        int consonants = 0;
        long ans = 0;
        int left = 0;

        for (int right = 0; right < n; ++right) {
            char c = s.charAt(right);
            if (isVowel(c)) {
                int idx = vowelIndex(c);
                if (vowelCnt[idx] == 0) distinctVowels++;
                vowelCnt[idx]++;
            } else {
                consonants++;
            }

            while (distinctVowels == 5 && consonants >= K) {
                ans += n - right; // all extensions to the end are valid
                char cl = s.charAt(left);
                if (isVowel(cl)) {
                    int idx = vowelIndex(cl);
                    vowelCnt[idx]--;
                    if (vowelCnt[idx] == 0) distinctVowels--;
                } else {
                    consonants--;
                }
                left++;
            }
        }
        return ans;
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    private int vowelIndex(char c) {
        switch (c) {
            case 'a': return 0;
            case 'e': return 1;
            case 'i': return 2;
            case 'o': return 3;
            default:  return 4; // 'u'
        }
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
        vowel_index = {'a':0,'e':1,'i':2,'o':3,'u':4}
        
        def at_least(k_needed):
            if k_needed < 0:
                return 0
            cnt = [0]*5          # counts for each vowel
            distinct = 0         # number of different vowels present
            cons = 0             # consonant count in current window
            left = 0
            total = 0
            for right, ch in enumerate(word):
                idx = vowel_index.get(ch)
                if idx is not None:
                    if cnt[idx] == 0:
                        distinct += 1
                    cnt[idx] += 1
                else:
                    cons += 1
                # shrink while window satisfies both conditions
                while distinct == 5 and cons >= k_needed:
                    total += n - right   # all extensions to the right are valid
                    # remove leftmost character
                    lch = word[left]
                    lidx = vowel_index.get(lch)
                    if lidx is not None:
                        cnt[lidx] -= 1
                        if cnt[lidx] == 0:
                            distinct -= 1
                    else:
                        cons -= 1
                    left += 1
            return total
        
        return at_least(k) - at_least(k+1)
```

## Python3

```python
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowel_idx = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        vowels = set(vowel_idx.keys())

        def at_least(target_k: int) -> int:
            cnt = [0] * 5          # counts for each vowel
            types = 0              # how many distinct vowels are present
            cons = 0               # consonant count in window
            res = 0
            l = 0
            for r, ch in enumerate(word):
                if ch in vowels:
                    idx = vowel_idx[ch]
                    cnt[idx] += 1
                    if cnt[idx] == 1:
                        types += 1
                else:
                    cons += 1

                while types == 5 and cons >= target_k:
                    # all substrings starting at l and ending anywhere from r to n-1 are valid
                    res += n - r
                    ch_l = word[l]
                    if ch_l in vowels:
                        idx_l = vowel_idx[ch_l]
                        cnt[idx_l] -= 1
                        if cnt[idx_l] == 0:
                            types -= 1
                    else:
                        cons -= 1
                    l += 1
            return res

        return at_least(k) - at_least(k + 1)
```

## C

```c
#include <string.h>

static inline int vowelIndex(char c) {
    switch (c) {
        case 'a': return 0;
        case 'e': return 1;
        case 'i': return 2;
        case 'o': return 3;
        case 'u': return 4;
        default:  return -1;
    }
}

static long long atLeastK(const char *word, int n, int k) {
    if (k > n) return 0;
    int cnt[5] = {0};
    int distinctVowels = 0;
    int consonants = 0;
    int left = 0;
    long long res = 0;

    for (int right = 0; right < n; ++right) {
        int idx = vowelIndex(word[right]);
        if (idx != -1) {
            if (++cnt[idx] == 1) ++distinctVowels;
        } else {
            ++consonants;
        }

        while (distinctVowels == 5 && consonants >= k) {
            res += (long long)(n - right);
            int lIdx = vowelIndex(word[left]);
            if (lIdx != -1) {
                if (--cnt[lIdx] == 0) --distinctVowels;
            } else {
                --consonants;
            }
            ++left;
        }
    }
    return res;
}

long long countOfSubstrings(char* word, int k) {
    int n = (int)strlen(word);
    long long atK   = atLeastK(word, n, k);
    long long atKP1 = atLeastK(word, n, k + 1);
    return atK - atKP1;
}
```

## Csharp

```csharp
public class Solution
{
    public long CountOfSubstrings(string word, int k)
    {
        return AtLeast(word, k) - AtLeast(word, k + 1);
    }

    private long AtLeast(string s, int K)
    {
        int n = s.Length;
        if (K > n) return 0;
        long ans = 0;
        int[] cntVowel = new int[5];
        int mask = 0; // bits for a,e,i,o,u
        int cons = 0;
        int left = 0;

        for (int right = 0; right < n; ++right)
        {
            char c = s[right];
            int idx = VowelIndex(c);
            if (idx >= 0)
            {
                cntVowel[idx]++;
                mask |= (1 << idx);
            }
            else
            {
                cons++;
            }

            while (mask == 31 && cons >= K)
            {
                ans += n - right;

                char cl = s[left];
                int il = VowelIndex(cl);
                if (il >= 0)
                {
                    cntVowel[il]--;
                    if (cntVowel[il] == 0) mask &= ~(1 << il);
                }
                else
                {
                    cons--;
                }
                left++;
            }
        }

        return ans;
    }

    private int VowelIndex(char c)
    {
        switch (c)
        {
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

## Javascript

```javascript
/**
 * @param {string} word
 * @param {number} k
 * @return {number}
 */
var countOfSubstrings = function(word, k) {
    const n = word.length;
    // helper to count substrings with all vowels and at least K consonants
    const atLeast = (K) => {
        if (K < 0) return 0; // not needed but safe
        let ans = 0;
        let left = 0;
        const cnt = new Uint16Array(26); // frequency of each letter
        let distinctVowels = 0;
        let cons = 0;

        for (let right = 0; right < n; ++right) {
            const code = word.charCodeAt(right) - 97; // 'a' -> 0
            if (code === 0 || code === 4 || code === 8 || code === 14 || code === 20) { // a e i o u
                if (cnt[code] === 0) distinctVowels++;
                cnt[code]++;
            } else {
                cons++;
            }

            while (distinctVowels === 5 && cons >= K) {
                ans += n - right; // all extensions to the right are valid
                const leftCode = word.charCodeAt(left) - 97;
                if (leftCode === 0 || leftCode === 4 || leftCode === 8 || leftCode === 14 || leftCode === 20) {
                    cnt[leftCode]--;
                    if (cnt[leftCode] === 0) distinctVowels--;
                } else {
                    cons--;
                }
                left++;
            }
        }
        return ans;
    };

    return atLeast(k) - atLeast(k + 1);
};
```

## Typescript

```typescript
function countOfSubstrings(word: string, k: number): number {
    const n = word.length;

    const vowelIdx = (ch: string): number => {
        if (ch === 'a') return 0;
        if (ch === 'e') return 1;
        if (ch === 'i') return 2;
        if (ch === 'o') return 3;
        if (ch === 'u') return 4;
        return -1;
    };

    const atLeast = (need: number): number => {
        if (need < 0) return 0;
        let ans = 0;
        let start = 0;
        let consonants = 0;
        const cnt = [0, 0, 0, 0, 0];
        let mask = 0; // bits for a,e,i,o,u

        for (let end = 0; end < n; ++end) {
            const ch = word[end];
            const idx = vowelIdx(ch);
            if (idx !== -1) {
                cnt[idx]++;
                if (cnt[idx] === 1) mask |= (1 << idx);
            } else {
                consonants++;
            }

            while (mask === 31 && consonants >= need) {
                ans += n - end;
                const leftCh = word[start];
                const lIdx = vowelIdx(leftCh);
                if (lIdx !== -1) {
                    cnt[lIdx]--;
                    if (cnt[lIdx] === 0) mask &= ~(1 << lIdx);
                } else {
                    consonants--;
                }
                start++;
            }
        }

        return ans;
    };

    return atLeast(k) - atLeast(k + 1);
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
        return $this->atLeastK($word, $k) - $this->atLeastK($word, $k + 1);
    }

    private function atLeastK($word, $k) {
        $n = strlen($word);
        if ($k > $n) return 0;

        $vowelIdx = ['a'=>0,'e'=>1,'i'=>2,'o'=>3,'u'=>4];
        $cntVowels = array_fill(0, 5, 0);
        $distinct = 0;
        $consonants = 0;
        $start = 0;
        $ans = 0;

        for ($end = 0; $end < $n; $end++) {
            $c = $word[$end];
            if (isset($vowelIdx[$c])) {
                $idx = $vowelIdx[$c];
                if ($cntVowels[$idx] == 0) $distinct++;
                $cntVowels[$idx]++;
            } else {
                $consonants++;
            }

            while ($distinct == 5 && $consonants >= $k) {
                $ans += $n - $end;
                $c2 = $word[$start];
                if (isset($vowelIdx[$c2])) {
                    $idx2 = $vowelIdx[$c2];
                    $cntVowels[$idx2]--;
                    if ($cntVowels[$idx2] == 0) $distinct--;
                } else {
                    $consonants--;
                }
                $start++;
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
        
        @inline(__always) func vowelIndex(_ c: Character) -> Int {
            switch c {
            case "a": return 0
            case "e": return 1
            case "i": return 2
            case "o": return 3
            case "u": return 4
            default: return -1
            }
        }
        
        @inline(__always) func isVowel(_ c: Character) -> Bool {
            return vowelIndex(c) != -1
        }
        
        func countAtLeast(_ need: Int) -> Int64 {
            if need < 0 { return 0 }
            var start = 0
            var consonantCnt = 0
            var vowelCounts = [Int](repeating: 0, count: 5)
            var distinctVowels = 0
            var result: Int64 = 0
            
            for end in 0..<n {
                let ch = chars[end]
                if isVowel(ch) {
                    let idx = vowelIndex(ch)
                    if vowelCounts[idx] == 0 { distinctVowels += 1 }
                    vowelCounts[idx] += 1
                } else {
                    consonantCnt += 1
                }
                
                while distinctVowels == 5 && consonantCnt >= need {
                    result += Int64(n - end)
                    
                    let leftChar = chars[start]
                    if isVowel(leftChar) {
                        let idx = vowelIndex(leftChar)
                        vowelCounts[idx] -= 1
                        if vowelCounts[idx] == 0 { distinctVowels -= 1 }
                    } else {
                        consonantCnt -= 1
                    }
                    start += 1
                }
            }
            return result
        }
        
        let exact = countAtLeast(k) - countAtLeast(k + 1)
        return Int(exact)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countOfSubstrings(word: String, k: Int): Long {
        val n = word.length

        fun atLeast(targetK: Int): Long {
            var ans = 0L
            var left = 0
            var consonants = 0
            val vowelCnt = IntArray(5)
            var distinct = 0

            fun vowelIndex(c: Char): Int = when (c) {
                'a' -> 0
                'e' -> 1
                'i' -> 2
                'o' -> 3
                'u' -> 4
                else -> -1
            }

            for (right in 0 until n) {
                val c = word[right]
                val vi = vowelIndex(c)
                if (vi >= 0) {
                    vowelCnt[vi]++
                    if (vowelCnt[vi] == 1) distinct++
                } else {
                    consonants++
                }

                while (distinct == 5 && consonants >= targetK) {
                    ans += (n - right).toLong()
                    val lc = word[left]
                    val vli = vowelIndex(lc)
                    if (vli >= 0) {
                        vowelCnt[vli]--
                        if (vowelCnt[vli] == 0) distinct--
                    } else {
                        consonants--
                    }
                    left++
                }
            }
            return ans
        }

        return atLeast(k) - atLeast(k + 1)
    }
}
```

## Dart

```dart
class Solution {
  int countOfSubstrings(String word, int k) {
    int n = word.length;

    int atLeast(int kk) {
      if (kk < 0) return 0;
      int ans = 0;
      List<int> cnt = List.filled(5, 0);
      int vowelTypes = 0;
      int cons = 0;
      int left = 0;
      for (int right = 0; right < n; ++right) {
        int idx = _vowelIndex(word.codeUnitAt(right));
        if (idx != -1) {
          if (cnt[idx] == 0) vowelTypes++;
          cnt[idx]++;
        } else {
          cons++;
        }
        while (vowelTypes == 5 && cons >= kk) {
          ans += n - right;
          int lIdx = _vowelIndex(word.codeUnitAt(left));
          if (lIdx != -1) {
            cnt[lIdx]--;
            if (cnt[lIdx] == 0) vowelTypes--;
          } else {
            cons--;
          }
          left++;
        }
      }
      return ans;
    }

    return atLeast(k) - atLeast(k + 1);
  }

  int _vowelIndex(int code) {
    switch (code) {
      case 97: // a
        return 0;
      case 101: // e
        return 1;
      case 105: // i
        return 2;
      case 111: // o
        return 3;
      case 117: // u
        return 4;
    }
    return -1;
  }
}
```

## Golang

```go
func countOfSubstrings(word string, k int) int64 {
    n := len(word)

    isVowel := func(c byte) bool {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
    }
    vowelIdx := func(c byte) int {
        switch c {
        case 'a':
            return 0
        case 'e':
            return 1
        case 'i':
            return 2
        case 'o':
            return 3
        case 'u':
            return 4
        }
        return -1
    }

    atLeast := func(target int) int64 {
        var cnt [5]int
        distinct, cons := 0, 0
        ans := int64(0)
        start := 0
        for end := 0; end < n; end++ {
            c := word[end]
            if isVowel(c) {
                idx := vowelIdx(c)
                if cnt[idx] == 0 {
                    distinct++
                }
                cnt[idx]++
            } else {
                cons++
            }
            for distinct == 5 && cons >= target {
                ans += int64(n - end)
                sc := word[start]
                if isVowel(sc) {
                    idx := vowelIdx(sc)
                    cnt[idx]--
                    if cnt[idx] == 0 {
                        distinct--
                    }
                } else {
                    cons--
                }
                start++
            }
        }
        return ans
    }

    return atLeast(k) - atLeast(k+1)
}
```

## Ruby

```ruby
def count_of_substrings(word, k)
  n = word.length
  vowel_idx = { 'a' => 0, 'e' => 1, 'i' => 2, 'o' => 3, 'u' => 4 }

  at_least = lambda do |target|
    cnt = [0, 0, 0, 0, 0]
    distinct = 0
    cons = 0
    left = 0
    res = 0

    n.times do |right|
      ch = word[right]
      if (idx = vowel_idx[ch])
        cnt[idx] += 1
        distinct += 1 if cnt[idx] == 1
      else
        cons += 1
      end

      while distinct == 5 && cons >= target
        res += n - right
        ch_left = word[left]
        if (idx_l = vowel_idx[ch_left])
          cnt[idx_l] -= 1
          distinct -= 1 if cnt[idx_l] == 0
        else
          cons -= 1
        end
        left += 1
      end
    end

    res
  end

  at_least.call(k) - at_least.call(k + 1)
end
```

## Scala

```scala
object Solution {
  def countOfSubstrings(word: String, k: Int): Long = {
    atLeast(word, k) - atLeast(word, k + 1)
  }

  private def atLeast(word: String, needK: Int): Long = {
    val n = word.length
    if (needK < 0) return 0L
    var left = 0
    var ans = 0L
    val vowelCnt = new Array[Int](5)
    var distinctVowel = 0
    var consCount = 0

    def vowelIndex(c: Char): Int = c match {
      case 'a' => 0
      case 'e' => 1
      case 'i' => 2
      case 'o' => 3
      case 'u' => 4
      case _   => -1
    }

    var right = 0
    while (right < n) {
      val c = word.charAt(right)
      val idx = vowelIndex(c)
      if (idx != -1) {
        if (vowelCnt(idx) == 0) distinctVowel += 1
        vowelCnt(idx) += 1
      } else {
        consCount += 1
      }

      while (distinctVowel == 5 && consCount >= needK) {
        ans += n - right
        val cl = word.charAt(left)
        val idxL = vowelIndex(cl)
        if (idxL != -1) {
          vowelCnt(idxL) -= 1
          if (vowelCnt(idxL) == 0) distinctVowel -= 1
        } else {
          consCount -= 1
        }
        left += 1
      }

      right += 1
    }
    ans
  }
}
```

## Rust

```rust
use std::cmp;

impl Solution {
    fn at_least(s: &[u8], k: usize) -> i64 {
        let n = s.len();
        if k > n {
            return 0;
        }
        let mut start = 0usize;
        let mut ans: i64 = 0;
        let mut cnt = [0i32; 5];
        let mut distinct = 0usize;
        let mut cons = 0usize;

        for end in 0..n {
            let c = s[end];
            if matches!(c, b'a' | b'e' | b'i' | b'o' | b'u') {
                let idx = match c {
                    b'a' => 0,
                    b'e' => 1,
                    b'i' => 2,
                    b'o' => 3,
                    b'u' => 4,
                    _ => unreachable!(),
                };
                cnt[idx] += 1;
                if cnt[idx] == 1 {
                    distinct += 1;
                }
            } else {
                cons += 1;
            }

            while distinct == 5 && cons >= k {
                ans += (n - end) as i64;
                let sc = s[start];
                if matches!(sc, b'a' | b'e' | b'i' | b'o' | b'u') {
                    let idx = match sc {
                        b'a' => 0,
                        b'e' => 1,
                        b'i' => 2,
                        b'o' => 3,
                        b'u' => 4,
                        _ => unreachable!(),
                    };
                    cnt[idx] -= 1;
                    if cnt[idx] == 0 {
                        distinct -= 1;
                    }
                } else {
                    cons -= 1;
                }
                start += 1;
            }
        }

        ans
    }

    pub fn count_of_substrings(word: String, k: i32) -> i64 {
        let bytes = word.as_bytes();
        let k_usize = k as usize;
        let total_k = Self::at_least(bytes, k_usize);
        let total_k1 = Self::at_least(bytes, k_usize + 1);
        total_k - total_k1
    }
}
```

## Racket

```racket
(define/contract (count-of-substrings word k)
  (-> string? exact-integer? exact-integer?)
  (let* ([n (string-length word)]
         [vowel-index
          (lambda (ch)
            (cond [(char=? ch #\a) 0]
                  [(char=? ch #\e) 1]
                  [(char=? ch #\i) 2]
                  [(char=? ch #\o) 3]
                  [(char=? ch #\u) 4]
                  [else -1]))]
         [at-least
          (lambda (k)
            (let ([counts (make-vector 5 0)]
                  [distinct 0]
                  [cons 0]
                  [start 0]
                  [total 0])
              (for ([end (in-range n)])
                (let* ([ch (string-ref word end)]
                       [idx (vowel-index ch)])
                  (if (= idx -1)
                      (set! cons (+ cons 1))
                      (begin
                        (when (= (vector-ref counts idx) 0)
                          (set! distinct (+ distinct 1)))
                        (vector-set! counts idx (+ (vector-ref counts idx) 1)))))
                (let loop ()
                  (when (and (= distinct 5) (>= cons k))
                    (set! total (+ total (- n end)))
                    (let* ([chL (string-ref word start)]
                           [idxL (vowel-index chL)])
                      (if (= idxL -1)
                          (set! cons (- cons 1))
                          (begin
                            (vector-set! counts idxL (- (vector-ref counts idxL) 1))
                            (when (= (vector-ref counts idxL) 0)
                              (set! distinct (- distinct 1))))))
                    (set! start (+ start 1))
                    (loop)))))
              total))])
    (- (at-least k) (at-least (+ k 1)))))
```

## Erlang

```erlang
-module(solution).
-export([count_of_substrings/2]).

-spec count_of_substrings(Word :: unicode:unicode_binary(), K :: integer()) -> integer().
count_of_substrings(Word, K) ->
    AtK = at_least_k(Word, K),
    AtK1 = at_least_k(Word, K + 1),
    AtK - AtK1.

at_least_k(Word, K) ->
    N = byte_size(Word),
    loop(0, 0, N, K, 0, {0,0,0,0,0}, 0, 0, Word).

loop(Start, End, N, K, Cons, VCounts, Mask, Res, Word) when End < N ->
    Char = binary:at(Word, End),
    case is_vowel(Char) of
        true ->
            Idx = vowel_idx(Char),
            {VCounts1, SetBit} = add_vowel(Idx, VCounts),
            NewMask = if SetBit -> Mask bor (1 bsl Idx); true -> Mask end,
            {NewStart, NewCons, NewVCounts, NewMask2, NewRes} =
                shrink_while_valid(Start, End, N, K, Cons, VCounts1, NewMask, Res, Word),
            loop(NewStart, End + 1, N, K, NewCons, NewVCounts, NewMask2, NewRes, Word);
        false ->
            {NewStart, NewCons, NewVCounts, NewMask2, NewRes} =
                shrink_while_valid(Start, End, N, K, Cons + 1, VCounts, Mask, Res, Word),
            loop(NewStart, End + 1, N, K, NewCons, NewVCounts, NewMask2, NewRes, Word)
    end;
loop(_, _, _, _, _, _, _, Res, _) ->
    Res.

shrink_while_valid(Start, EndIdx, N, K, Cons, VCounts, Mask, Res, Word) ->
    case (Mask == 31) andalso (Cons >= K) of
        true ->
            NewRes = Res + (N - EndIdx),
            CharL = binary:at(Word, Start),
            case is_vowel(CharL) of
                true ->
                    IdxL = vowel_idx(CharL),
                    {VCounts2, ClearBit} = remove_vowel(IdxL, VCounts),
                    NewMask = if ClearBit -> Mask band bnot (1 bsl IdxL); true -> Mask end,
                    shrink_while_valid(Start + 1, EndIdx, N, K, Cons, VCounts2, NewMask, NewRes, Word);
                false ->
                    shrink_while_valid(Start + 1, EndIdx, N, K, Cons - 1, VCounts, Mask, NewRes, Word)
            end;
        false ->
            {Start, Cons, VCounts, Mask, Res}
    end.

is_vowel(C) when C =:= $a; C =:= $e; C =:= $i; C =:= $o; C =:= $u -> true;
is_vowel(_) -> false.

vowel_idx(C) ->
    case C of
        $a -> 0;
        $e -> 1;
        $i -> 2;
        $o -> 3;
        $u -> 4
    end.

add_vowel(Idx, Counts) ->
    Pos = Idx + 1,
    Old = element(Pos, Counts),
    NewCounts = setelement(Pos, Counts, Old + 1),
    {NewCounts, (Old == 0)}.

remove_vowel(Idx, Counts) ->
    Pos = Idx + 1,
    Old = element(Pos, Counts),
    NewCounts = setelement(Pos, Counts, Old - 1),
    {NewCounts, (Old == 1)}.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_of_substrings(word :: String.t(), k :: integer) :: integer
  def count_of_substrings(word, k) do
    bytes = String.to_charlist(word)
    arr = :array.from_list(bytes)
    n = length(bytes)

    at_least(arr, n, k) - at_least(arr, n, k + 1)
  end

  # Count substrings with all vowels and at least k consonants
  defp at_least(arr, n, k) do
    go(0, 0, {0, 0, 0, 0, 0}, 0, 0, 0, n, k, arr)
  end

  # Main sliding window loop (right pointer moves)
  defp go(_left, right, _cnt, _distinct, _cons, ans, n, _k, _arr) when right == n do
    ans
  end

  defp go(left, right, cnt, distinct, cons, ans, n, k, arr) do
    code = :array.get(right, arr)

    {cnt1, distinct1, cons1} =
      case vowel_index(code) do
        -1 ->
          {cnt, distinct, cons + 1}

        idx ->
          old = elem(cnt, idx)
          cnt_new = put_elem(cnt, idx, old + 1)
          distinct_new = if old == 0, do: distinct + 1, else: distinct
          {cnt_new, distinct_new, cons}
      end

    {left2, cnt2, distinct2, cons2, ans2} =
      shrink(left, right, cnt1, distinct1, cons1, ans, n, k, arr)

    go(left2, right + 1, cnt2, distinct2, cons2, ans2, n, k, arr)
  end

  # Shrink left side while window satisfies conditions
  defp shrink(l, r, cnt, distinct, cons, ans, n, k, arr) do
    if distinct == 5 and cons >= k do
      ans_new = ans + (n - r)

      code_l = :array.get(l, arr)

      {cnt1, distinct1, cons1} =
        case vowel_index(code_l) do
          -1 ->
            {cnt, distinct, cons - 1}

          idx ->
            old = elem(cnt, idx)
            cnt_new = put_elem(cnt, idx, old - 1)
            distinct_new = if old == 1, do: distinct - 1, else: distinct
            {cnt_new, distinct_new, cons}
        end

      shrink(l + 1, r, cnt1, distinct1, cons1, ans_new, n, k, arr)
    else
      {l, cnt, distinct, cons, ans}
    end
  end

  # Returns vowel index (0..4) or -1 if not a vowel
  defp vowel_index(c) do
    case c do
      ?a -> 0
      ?e -> 1
      ?i -> 2
      ?o -> 3
      ?u -> 4
      _ -> -1
    end
  end
end
```
