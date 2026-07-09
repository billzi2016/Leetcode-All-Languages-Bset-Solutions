# 2514. Count Anagrams

## Cpp

```cpp
class Solution {
public:
    static const int MOD = 1'000'000'007;
    
    long long modPow(long long a, long long e) {
        long long res = 1;
        while (e) {
            if (e & 1) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return res;
    }
    
    int countAnagrams(string s) {
        // find maximum word length to size factorial arrays
        int maxLen = 0, cur = 0;
        for (char c : s) {
            if (c == ' ') {
                maxLen = max(maxLen, cur);
                cur = 0;
            } else {
                ++cur;
            }
        }
        maxLen = max(maxLen, cur); // last word
        
        vector<long long> fact(maxLen + 1), invFact(maxLen + 1);
        fact[0] = 1;
        for (int i = 1; i <= maxLen; ++i) fact[i] = fact[i-1] * i % MOD;
        invFact[maxLen] = modPow(fact[maxLen], MOD - 2);
        for (int i = maxLen; i > 0; --i) invFact[i-1] = invFact[i] * i % MOD;
        
        long long ans = 1;
        int n = s.size();
        vector<int> freq(26, 0);
        int len = 0;
        for (int i = 0; i <= n; ++i) {
            if (i == n || s[i] == ' ') {
                // process current word
                ans = ans * fact[len] % MOD;
                for (int f : freq) {
                    if (f > 1) ans = ans * invFact[f] % MOD;
                }
                // reset for next word
                fill(freq.begin(), freq.end(), 0);
                len = 0;
            } else {
                ++len;
                ++freq[s[i] - 'a'];
            }
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    private static final long MOD = 1000000007L;
    
    public int countAnagrams(String s) {
        String[] words = s.split(" ");
        int maxLen = 0;
        for (String w : words) {
            if (w.length() > maxLen) maxLen = w.length();
        }
        long[] fact = new long[maxLen + 1];
        long[] invFact = new long[maxLen + 1];
        fact[0] = 1;
        for (int i = 1; i <= maxLen; i++) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        invFact[maxLen] = modPow(fact[maxLen], MOD - 2);
        for (int i = maxLen; i > 0; i--) {
            invFact[i - 1] = invFact[i] * i % MOD;
        }
        
        long ans = 1;
        int[] cnt = new int[26];
        for (String w : words) {
            int n = w.length();
            long ways = fact[n];
            java.util.Arrays.fill(cnt, 0);
            for (int i = 0; i < n; i++) {
                cnt[w.charAt(i) - 'a']++;
            }
            for (int c : cnt) {
                if (c > 1) {
                    ways = ways * invFact[c] % MOD;
                }
            }
            ans = ans * ways % MOD;
        }
        return (int) ans;
    }
    
    private long modPow(long a, long e) {
        long res = 1;
        long base = a % MOD;
        while (e > 0) {
            if ((e & 1) == 1) {
                res = res * base % MOD;
            }
            base = base * base % MOD;
            e >>= 1;
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def countAnagrams(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        words = s.split(' ')
        max_len = 0
        for w in words:
            if len(w) > max_len:
                max_len = len(w)
        # precompute factorials and inverse factorials up to max_len
        fact = [1] * (max_len + 1)
        for i in range(2, max_len + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (max_len + 1)
        inv_fact[max_len] = pow(fact[max_len], MOD - 2, MOD)
        for i in range(max_len, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        result = 1
        for w in words:
            n = len(w)
            ways = fact[n]
            # count character frequencies
            cnt = {}
            for ch in w:
                cnt[ch] = cnt.get(ch, 0) + 1
            for c in cnt.values():
                ways = ways * inv_fact[c] % MOD
            result = result * ways % MOD
        return result
```

## Python3

```python
class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = 10**9 + 7
        words = s.split(' ')
        max_len = max(len(w) for w in words)
        fact = [1] * (max_len + 1)
        for i in range(2, max_len + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (max_len + 1)
        inv_fact[max_len] = pow(fact[max_len], MOD - 2, MOD)
        for i in range(max_len, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        ans = 1
        for w in words:
            n = len(w)
            cnt = {}
            for ch in w:
                cnt[ch] = cnt.get(ch, 0) + 1
            ways = fact[n]
            for c in cnt.values():
                ways = ways * inv_fact[c] % MOD
            ans = ans * ways % MOD
        return ans
```

## C

```c
int countAnagrams(char* s) {
    const int MOD = 1000000007;
    int n = 0;
    while (s[n] != '\0') ++n;

    static long long fact[100005];
    static long long invFact[100005];
    fact[0] = 1;
    for (int i = 1; i <= n; ++i) fact[i] = fact[i - 1] * i % MOD;

    // fast power to compute modular inverse of fact[n]
    long long base = fact[n], exp = MOD - 2, res = 1;
    while (exp) {
        if (exp & 1) res = res * base % MOD;
        base = base * base % MOD;
        exp >>= 1;
    }
    invFact[n] = res;
    for (int i = n; i > 0; --i) invFact[i - 1] = invFact[i] * i % MOD;

    long long ans = 1;
    int freq[26] = {0};
    int len = 0;

    for (int i = 0; i <= n; ++i) {
        if (s[i] == ' ' || s[i] == '\0') {
            long long ways = fact[len];
            for (int j = 0; j < 26; ++j) {
                if (freq[j] > 1) ways = ways * invFact[freq[j]] % MOD;
            }
            ans = ans * ways % MOD;

            len = 0;
            for (int j = 0; j < 26; ++j) freq[j] = 0;
        } else {
            int idx = s[i] - 'a';
            ++freq[idx];
            ++len;
        }
    }

    return (int)ans;
}
```

## Csharp

```csharp
using System;
public class Solution {
    private const int MOD = 1000000007;
    public int CountAnagrams(string s) {
        string[] words = s.Split(' ');
        int maxLen = s.Length; // total length is enough for factorials
        long[] fact = new long[maxLen + 1];
        long[] invFact = new long[maxLen + 1];
        fact[0] = 1;
        for (int i = 1; i <= maxLen; i++) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        invFact[maxLen] = ModPow(fact[maxLen], MOD - 2);
        for (int i = maxLen - 1; i >= 0; i--) {
            invFact[i] = invFact[i + 1] * (i + 1) % MOD;
        }

        long result = 1;
        foreach (var word in words) {
            int len = word.Length;
            long ways = fact[len];
            int[] cnt = new int[26];
            foreach (char c in word) {
                cnt[c - 'a']++;
            }
            for (int i = 0; i < 26; i++) {
                if (cnt[i] > 1) {
                    ways = ways * invFact[cnt[i]] % MOD;
                }
            }
            result = result * ways % MOD;
        }
        return (int)result;
    }

    private long ModPow(long baseVal, long exp) {
        long res = 1;
        baseVal %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                res = res * baseVal % MOD;
            }
            baseVal = baseVal * baseVal % MOD;
            exp >>= 1;
        }
        return res;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var countAnagrams = function(s) {
    const MOD = 1000000007n;

    // fast exponentiation (base^exp % MOD)
    const modPow = (base, exp) => {
        let result = 1n;
        base %= MOD;
        while (exp > 0n) {
            if (exp & 1n) result = (result * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1n;
        }
        return result;
    };

    const words = s.split(' ');
    let maxLen = 0;
    for (const w of words) {
        if (w.length > maxLen) maxLen = w.length;
    }

    // precompute factorials and inverse factorials up to maxLen
    const fact = new Array(maxLen + 1);
    const invFact = new Array(maxLen + 1);
    fact[0] = 1n;
    for (let i = 1; i <= maxLen; ++i) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }
    invFact[maxLen] = modPow(fact[maxLen], MOD - 2n);
    for (let i = maxLen; i >= 1; --i) {
        invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;
    }

    let answer = 1n;

    for (const w of words) {
        const len = w.length;
        let ways = fact[len];
        const cnt = new Array(26).fill(0);
        for (let i = 0; i < len; ++i) {
            cnt[w.charCodeAt(i) - 97]++;
        }
        for (const c of cnt) {
            if (c > 1) {
                ways = (ways * invFact[c]) % MOD;
            }
        }
        answer = (answer * ways) % MOD;
    }

    return Number(answer);
};
```

## Typescript

```typescript
function countAnagrams(s: string): number {
    const MOD = 1000000007n;
    const words = s.split(' ');
    let maxLen = 0;
    for (const w of words) if (w.length > maxLen) maxLen = w.length;

    const fact: bigint[] = new Array(maxLen + 1);
    const invFact: bigint[] = new Array(maxLen + 1);
    fact[0] = 1n;
    for (let i = 1; i <= maxLen; ++i) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }

    const modPow = (base: bigint, exp: bigint): bigint => {
        let result = 1n;
        let b = base % MOD;
        let e = exp;
        while (e > 0) {
            if (e & 1n) result = (result * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return result;
    };

    invFact[maxLen] = modPow(fact[maxLen], MOD - 2n);
    for (let i = maxLen; i > 0; --i) {
        invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;
    }

    let ans = 1n;
    const freq = new Array(26).fill(0);
    for (const w of words) {
        const len = w.length;
        freq.fill(0);
        for (let i = 0; i < len; ++i) {
            const idx = w.charCodeAt(i) - 97;
            ++freq[idx];
        }
        let ways = fact[len];
        for (let i = 0; i < 26; ++i) {
            const c = freq[i];
            if (c > 0) {
                ways = (ways * invFact[c]) % MOD;
            }
        }
        ans = (ans * ways) % MOD;
    }

    return Number(ans);
}
```

## Php

```php
class Solution {

    const MOD = 1000000007;

    private function modPow($base, $exp) {
        $mod = self::MOD;
        $result = 1;
        $base %= $mod;
        while ($exp > 0) {
            if ($exp & 1) {
                $result = ($result * $base) % $mod;
            }
            $base = ($base * $base) % $mod;
            $exp >>= 1;
        }
        return $result;
    }

    /**
     * @param String $s
     * @return Integer
     */
    function countAnagrams($s) {
        $words = explode(' ', trim($s));
        $maxLen = 0;
        foreach ($words as $w) {
            $len = strlen($w);
            if ($len > $maxLen) $maxLen = $len;
        }

        // precompute factorials and inverse factorials up to maxLen
        $fact = array_fill(0, $maxLen + 1, 1);
        for ($i = 1; $i <= $maxLen; $i++) {
            $fact[$i] = ($fact[$i - 1] * $i) % self::MOD;
        }
        $invFact = array_fill(0, $maxLen + 1, 1);
        $invFact[$maxLen] = $this->modPow($fact[$maxLen], self::MOD - 2);
        for ($i = $maxLen; $i > 0; $i--) {
            $invFact[$i - 1] = ($invFact[$i] * $i) % self::MOD;
        }

        $ans = 1;
        foreach ($words as $w) {
            $len = strlen($w);
            if ($len <= 1) continue; // only one permutation
            $cnt = array_fill(0, 26, 0);
            for ($j = 0; $j < $len; $j++) {
                $idx = ord($w[$j]) - 97;
                $cnt[$idx]++;
            }
            $ways = $fact[$len];
            foreach ($cnt as $c) {
                if ($c > 1) {
                    $ways = ($ways * $invFact[$c]) % self::MOD;
                }
            }
            $ans = ($ans * $ways) % self::MOD;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    let MOD: Int64 = 1_000_000_007

    private func modPow(_ base: Int64, _ exp: Int64) -> Int64 {
        var result: Int64 = 1
        var b = base % MOD
        var e = exp
        while e > 0 {
            if e & 1 == 1 {
                result = (result * b) % MOD
            }
            b = (b * b) % MOD
            e >>= 1
        }
        return result
    }

    func countAnagrams(_ s: String) -> Int {
        let words = s.split(separator: " ")
        var maxLen = 0
        for w in words {
            if w.count > maxLen { maxLen = w.count }
        }

        // factorials and inverse factorials up to maxLen
        var fact = [Int64](repeating: 0, count: maxLen + 1)
        var invFact = [Int64](repeating: 0, count: maxLen + 1)
        fact[0] = 1
        if maxLen > 0 {
            for i in 1...maxLen {
                fact[i] = (fact[i - 1] * Int64(i)) % MOD
            }
            invFact[maxLen] = modPow(fact[maxLen], MOD - 2)
            var i = maxLen
            while i > 0 {
                invFact[i - 1] = (invFact[i] * Int64(i)) % MOD
                i -= 1
            }
        } else {
            invFact[0] = 1
        }

        var answer: Int64 = 1
        for sub in words {
            let word = String(sub)
            let len = word.count
            var freq = [Int](repeating: 0, count: 26)
            for ch in word.utf8 {
                let idx = Int(ch - 97) // 'a' ascii is 97
                freq[idx] += 1
            }
            var ways = fact[len]
            for cnt in freq where cnt > 0 {
                ways = (ways * invFact[cnt]) % MOD
            }
            answer = (answer * ways) % MOD
        }

        return Int(answer)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countAnagrams(s: String): Int {
        val words = s.split(' ')
        var maxLen = 0
        for (w in words) if (w.length > maxLen) maxLen = w.length

        val MOD = 1_000_000_007L
        val fact = LongArray(maxLen + 1)
        val invFact = LongArray(maxLen + 1)
        fact[0] = 1L
        for (i in 1..maxLen) {
            fact[i] = fact[i - 1] * i % MOD
        }

        fun modPow(base: Long, exp: Long): Long {
            var b = base % MOD
            var e = exp
            var res = 1L
            while (e > 0) {
                if ((e and 1L) == 1L) res = res * b % MOD
                b = b * b % MOD
                e = e shr 1
            }
            return res
        }

        invFact[maxLen] = modPow(fact[maxLen], MOD - 2)
        for (i in maxLen downTo 1) {
            invFact[i - 1] = invFact[i] * i % MOD
        }

        var ans = 1L
        val freq = IntArray(26)
        for (word in words) {
            java.util.Arrays.fill(freq, 0)
            for (ch in word) {
                freq[ch - 'a']++
            }
            var ways = fact[word.length]
            for (cnt in freq) {
                if (cnt > 1) {
                    ways = ways * invFact[cnt] % MOD
                }
            }
            ans = ans * ways % MOD
        }
        return ans.toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  int countAnagrams(String s) {
    int n = s.length;
    // Precompute factorials up to n
    List<int> fact = List.filled(n + 1, 0);
    fact[0] = 1;
    for (int i = 1; i <= n; ++i) {
      fact[i] = (fact[i - 1] * i) % _mod;
    }
    // Precompute inverse factorials
    List<int> invFact = List.filled(n + 1, 0);
    invFact[n] = _powMod(fact[n], _mod - 2);
    for (int i = n; i >= 1; --i) {
      invFact[i - 1] = (invFact[i] * i) % _mod;
    }

    int result = 1;
    List<String> words = s.split(' ');
    for (String word in words) {
      int len = word.length;
      int ways = fact[len];
      // count frequencies
      List<int> cnt = List.filled(26, 0);
      for (int i = 0; i < len; ++i) {
        int idx = word.codeUnitAt(i) - 97; // 'a' ascii is 97
        cnt[idx]++;
      }
      for (int c in cnt) {
        if (c > 1) {
          ways = (ways * invFact[c]) % _mod;
        }
      }
      result = (result * ways) % _mod;
    }

    return result;
  }

  int _powMod(int base, int exp) {
    int res = 1;
    int b = base % _mod;
    while (exp > 0) {
      if ((exp & 1) == 1) {
        res = (res * b) % _mod;
      }
      b = (b * b) % _mod;
      exp >>= 1;
    }
    return res;
  }
}
```

## Golang

```go
package main

import (
	"strings"
)

const MOD int64 = 1000000007

func modPow(a, e int64) int64 {
	res := int64(1)
	for e > 0 {
		if e&1 == 1 {
			res = res * a % MOD
		}
		a = a * a % MOD
		e >>= 1
	}
	return res
}

func countAnagrams(s string) int {
	n := len(s)
	fact := make([]int64, n+1)
	invFact := make([]int64, n+1)

	fact[0] = 1
	for i := 1; i <= n; i++ {
		fact[i] = fact[i-1] * int64(i) % MOD
	}
	invFact[n] = modPow(fact[n], MOD-2)
	for i := n; i >= 1; i-- {
		invFact[i-1] = invFact[i] * int64(i) % MOD
	}

	words := strings.Split(s, " ")
	ans := int64(1)

	for _, w := range words {
		l := len(w)
		ways := fact[l]

		var cnt [26]int
		for i := 0; i < l; i++ {
			cnt[w[i]-'a']++
		}
		for _, c := range cnt {
			if c > 1 {
				ways = ways * invFact[c] % MOD
			}
		}
		ans = ans * ways % MOD
	}

	return int(ans)
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def mod_pow(base, exp, mod)
  result = 1
  b = base % mod
  e = exp
  while e > 0
    result = result * b % mod if (e & 1) == 1
    b = b * b % mod
    e >>= 1
  end
  result
end

def count_anagrams(s)
  words = s.split(' ')
  max_len = words.map(&:length).max || 0

  fact = Array.new(max_len + 1, 1)
  (1..max_len).each { |i| fact[i] = fact[i - 1] * i % MOD }

  inv_fact = Array.new(max_len + 1, 1)
  if max_len > 0
    inv_fact[max_len] = mod_pow(fact[max_len], MOD - 2, MOD)
    max_len.downto(1) { |i| inv_fact[i - 1] = inv_fact[i] * i % MOD }
  end

  ans = 1
  words.each do |word|
    ways = fact[word.length]
    freq = Hash.new(0)
    word.each_char { |c| freq[c] += 1 }
    freq.each_value { |cnt| ways = ways * inv_fact[cnt] % MOD }
    ans = ans * ways % MOD
  end

  ans
end
```

## Scala

```scala
object Solution {
    private val MOD: Long = 1000000007L

    private def modPow(base: Long, exp: Long): Long = {
        var b = base % MOD
        var e = exp
        var res = 1L
        while (e > 0) {
            if ((e & 1L) == 1L) res = (res * b) % MOD
            b = (b * b) % MOD
            e >>= 1
        }
        res
    }

    def countAnagrams(s: String): Int = {
        val maxLen = s.length
        val fact = new Array[Long](maxLen + 1)
        fact(0) = 1L
        var i = 1
        while (i <= maxLen) {
            fact(i) = (fact(i - 1) * i) % MOD
            i += 1
        }
        val invFact = new Array[Long](maxLen + 1)
        invFact(maxLen) = modPow(fact(maxLen), MOD - 2)
        i = maxLen
        while (i >= 1) {
            invFact(i - 1) = (invFact(i) * i) % MOD
            i -= 1
        }

        var result: Long = 1L
        val words = s.split(" ")
        for (w <- words) {
            val len = w.length
            var ways = fact(len)
            val cnt = new Array[Int](26)
            var idx = 0
            while (idx < len) {
                cnt(w.charAt(idx) - 'a') += 1
                idx += 1
            }
            var cIdx = 0
            while (cIdx < 26) {
                val c = cnt(cIdx)
                if (c > 0) ways = (ways * invFact(c)) % MOD
                cIdx += 1
            }
            result = (result * ways) % MOD
        }

        result.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_anagrams(s: String) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let words: Vec<&str> = s.split(' ').collect();
        let mut max_len = 0usize;
        for w in &words {
            if w.len() > max_len {
                max_len = w.len();
            }
        }
        // factorials
        let mut fact: Vec<i64> = vec![1; max_len + 1];
        for i in 1..=max_len {
            fact[i] = fact[i - 1] * (i as i64) % MOD;
        }
        // inverse factorials using Fermat's little theorem
        let mut inv_fact: Vec<i64> = vec![1; max_len + 1];
        inv_fact[max_len] = mod_pow(fact[max_len], MOD - 2, MOD);
        for i in (1..=max_len).rev() {
            inv_fact[i - 1] = inv_fact[i] * (i as i64) % MOD;
        }

        let mut ans: i64 = 1;
        for w in words {
            let len = w.len();
            let mut cnt = [0usize; 26];
            for b in w.bytes() {
                cnt[(b - b'a') as usize] += 1;
            }
            let mut ways = fact[len];
            for &c in &cnt {
                if c > 0 {
                    ways = ways * inv_fact[c] % MOD;
                }
            }
            ans = ans * ways % MOD;
        }
        ans as i32
    }
}

fn mod_pow(mut base: i64, mut exp: i64, modu: i64) -> i64 {
    let mut res: i64 = 1;
    base %= modu;
    while exp > 0 {
        if (exp & 1) == 1 {
            res = res * base % modu;
        }
        base = base * base % modu;
        exp >>= 1;
    }
    res
}
```

## Racket

```racket
(define/contract (count-anagrams s)
  (-> string? exact-integer?)
  (let* ((MOD 1000000007)
         (words (string-split s))
         (max-n (apply max (map string-length words)))
         (fact (make-vector (+ max-n 1) 0)))
    ;; factorials modulo MOD
    (vector-set! fact 0 1)
    (for ([i (in-range 1 (+ max-n 1))])
      (vector-set! fact i (modulo (* (vector-ref fact (- i 1)) i) MOD)))
    ;; fast exponentiation
    (define (pow-mod a e)
      (let loop ((base (modulo a MOD)) (exp e) (res 1))
        (if (= exp 0)
            res
            (let ((new-res (if (odd? exp) (modulo (* res base) MOD) res))
                  (new-base (modulo (* base base) MOD)))
              (loop new-base (quotient exp 2) new-res)))))
    ;; ways for a single word
    (define (word-ways w)
      (let* ((len (string-length w))
             (freq (make-vector 26 0)))
        (for ([i (in-range len)])
          (let* ((ch (char->integer (string-ref w i)))
                 (idx (- ch (char->integer #\a))))
            (vector-set! freq idx (+ 1 (vector-ref freq idx)))))
        (define numerator (vector-ref fact len))
        (define denominator
          (for/fold ([prod 1]) ([cnt (in-vector freq)])
            (if (> cnt 1)
                (modulo (* prod (vector-ref fact cnt)) MOD)
                prod)))
        (let ((invDen (pow-mod denominator (- MOD 2))))
          (modulo (* numerator invDen) MOD))))
    ;; combine all words
    (for/fold ([ans 1]) ([w words])
      (modulo (* ans (word-ways w)) MOD))))
```

## Erlang

```erlang
-define(MOD, 1000000007).

-spec count_anagrams(S :: unicode:unicode_binary()) -> integer().
count_anagrams(S) ->
    Words = binary:split(S, <<" ">>, [global]),
    MaxLen = max_word_len(Words, 0),
    FactMap = precompute_fact(MaxLen, #{0 => 1}),
    lists:foldl(fun(Word, Acc) ->
        Len = byte_size(Word),
        FactLen = maps:get(Len, FactMap),
        FreqMap = char_counts(Word, #{}),
        Perms = maps:fold(
            fun(_Char, Cnt, Prod) ->
                if
                    Cnt > 1 ->
                        InvFact = pow_mod(maps:get(Cnt, FactMap), ?MOD - 2),
                        (Prod * InvFact) rem ?MOD;
                    true -> Prod
                end
            end,
            FactLen,
            FreqMap),
        (Acc * Perms) rem ?MOD
    end, 1, Words).

max_word_len([], Max) -> Max;
max_word_len([W|Rest], Max) ->
    L = byte_size(W),
    NewMax = if L > Max -> L; true -> Max end,
    max_word_len(Rest, NewMax).

precompute_fact(Max, InitMap) ->
    precompute_fact_loop(1, Max, InitMap).

precompute_fact_loop(I, Max, Map) when I =< Max ->
    Prev = maps:get(I - 1, Map),
    FactI = (Prev * I) rem ?MOD,
    NewMap = maps:put(I, FactI, Map),
    precompute_fact_loop(I + 1, Max, NewMap);
precompute_fact_loop(_, _, Map) -> Map.

char_counts(<<>>, Acc) -> Acc;
char_counts(<<Char, Rest/binary>>, Acc) ->
    Count = maps:get(Char, Acc, 0) + 1,
    char_counts(Rest, maps:put(Char, Count, Acc)).

pow_mod(_Base, 0) -> 1;
pow_mod(Base, Exp) when (Exp band 1) == 1 ->
    ((Base rem ?MOD) * pow_mod((Base * Base) rem ?MOD, Exp bsr 1)) rem ?MOD;
pow_mod(Base, Exp) ->
    pow_mod((Base * Base) rem ?MOD, Exp bsr 1).
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec count_anagrams(String.t()) :: integer()
  def count_anagrams(s) do
    words = String.split(s, " ", trim: true)
    max_len = words |> Enum.map(&String.length/1) |> Enum.max()

    fact_tuple = build_fact_tuple(max_len)

    Enum.reduce(words, 1, fn word, acc ->
      n = String.length(word)
      numerator = elem(fact_tuple, n)

      freq = Enum.frequencies(String.graphemes(word))

      denom =
        Enum.reduce(freq, 1, fn {_ch, cnt}, dacc ->
          cur = elem(fact_tuple, cnt)
          rem(dacc * cur, @mod)
        end)

      inv_denom = mod_pow(denom, @mod - 2, @mod)
      word_perm = rem(numerator * inv_denom, @mod)
      rem(acc * word_perm, @mod)
    end)
  end

  defp build_fact_tuple(max_len) do
    list =
      Enum.reduce(1..max_len, [1], fn i, acc ->
        prev = hd(acc)
        cur = rem(prev * i, @mod)
        [cur | acc]
      end)
      |> Enum.reverse()

    List.to_tuple(list)
  end

  defp mod_pow(_base, 0, _mod), do: 1

  defp mod_pow(base, exp, mod) when exp > 0 do
    if rem(exp, 2) == 0 do
      half = mod_pow(base, div(exp, 2), mod)
      rem(half * half, mod)
    else
      rem(base * mod_pow(base, exp - 1, mod), mod)
    end
  end
end
```
