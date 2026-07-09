# 2949. Count Beautiful Substrings II

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long beautifulSubstrings(string s, int k) {
        // compute minimal m such that k divides m^2
        int kk = k;
        long long m = 1;
        for (int p = 2; p * p <= kk; ++p) {
            if (kk % p == 0) {
                int e = 0;
                while (kk % p == 0) {
                    kk /= p;
                    ++e;
                }
                int need = (e + 1) / 2; // ceil(e/2)
                for (int i = 0; i < need; ++i) m *= p;
            }
        }
        if (kk > 1) { // remaining prime factor with exponent 1
            m *= kk;
        }
        int period = static_cast<int>(2 * m); // length must be multiple of this
        
        struct PairHash {
            size_t operator()(const pair<int,int>&p) const noexcept {
                return (static_cast<uint64_t>(static_cast<unsigned int>(p.first)) << 32)
                       ^ static_cast<unsigned int>(p.second);
            }
        };
        
        unordered_map<pair<int,int>, long long, PairHash> cnt;
        cnt.reserve(s.size() * 2);
        int diff = 0;
        cnt[{0, 0}] = 1; // position 0
        
        long long ans = 0;
        for (int i = 1; i <= (int)s.size(); ++i) {
            char ch = s[i-1];
            bool isVowel = (ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u');
            diff += isVowel ? 1 : -1;
            int rem = i % period;
            auto key = make_pair(diff, rem);
            auto it = cnt.find(key);
            if (it != cnt.end()) {
                ans += it->second;
                it->second++;
            } else {
                cnt[key] = 1;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long beautifulSubstrings(String s, int k) {
        int m = minimalMultiple(k);
        java.util.HashMap<Long, Integer> map = new java.util.HashMap<>();
        int diff = 0;
        int vowelCount = 0;
        int mod = (m == 1) ? 0 : 0; // initial mod is 0
        long key = ((long) diff << 32) ^ (mod & 0xffffffffL);
        map.put(key, 1);
        long ans = 0;
        for (int i = 0; i < s.length(); ++i) {
            char ch = s.charAt(i);
            if (isVowel(ch)) {
                vowelCount++;
                diff++; // vowel adds +1 to (vowels - consonants)
            } else {
                diff--; // consonant subtracts 1
            }
            mod = (m == 1) ? 0 : (vowelCount % m);
            key = ((long) diff << 32) ^ (mod & 0xffffffffL);
            ans += map.getOrDefault(key, 0);
            map.put(key, map.getOrDefault(key, 0) + 1);
        }
        return ans;
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    // Compute the smallest positive integer m such that x^2 % k == 0 iff x is a multiple of m
    private int minimalMultiple(int k) {
        if (k == 1) return 1;
        int result = 1;
        int temp = k;
        for (int p = 2; p * p <= temp; ++p) {
            if (temp % p == 0) {
                int exp = 0;
                while (temp % p == 0) {
                    temp /= p;
                    exp++;
                }
                int need = (exp + 1) / 2; // ceil(exp/2)
                for (int i = 0; i < need; ++i) {
                    result *= p;
                }
            }
        }
        if (temp > 1) { // remaining prime factor with exponent 1
            result *= temp; // need one copy of this prime
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def beautifulSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # compute minimal multiplier m such that x^2 % k == 0 iff m divides x
        def min_multiplier(k):
            m = 1
            temp = k
            p = 2
            while p * p <= temp:
                if temp % p == 0:
                    e = 0
                    while temp % p == 0:
                        temp //= p
                        e += 1
                    exp = (e + 1) // 2  # ceil(e/2)
                    m *= p ** exp
                p += 1 if p == 2 else 2
            if temp > 1:  # remaining prime factor with exponent 1
                m *= temp
            return m

        m = min_multiplier(k)

        vowel_set = set('aeiou')
        diff = 0
        ans = 0
        from collections import defaultdict

        # map (diff, parity) -> dict of residue counts modulo m
        cnt_map = {}

        n = len(s)
        for i in range(n + 1):
            parity = i & 1
            t = i >> 1
            key = (diff, parity)
            r = t % m

            inner = cnt_map.get(key)
            if inner is None:
                inner = defaultdict(int)
                cnt_map[key] = inner
            ans += inner[r]
            inner[r] += 1

            if i < n:
                diff += 1 if s[i] in vowel_set else -1

        return ans
```

## Python3

```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        # compute minimal d such that k divides d^2
        d = 1
        temp = k
        p = 2
        while p * p <= temp:
            if temp % p == 0:
                e = 0
                while temp % p == 0:
                    temp //= p
                    e += 1
                need = (e + 1) // 2  # ceil(e/2)
                d *= p ** need
            p += 1 if p == 2 else 2
        if temp > 1:  # remaining prime factor with exponent 1
            d *= temp  # need = 1
        M = 2 * d

        from collections import defaultdict

        diff_map = defaultdict(lambda: defaultdict(int))
        ans = 0
        pref_vowel = 0
        n = len(s)
        for i in range(n + 1):
            if i:
                if s[i - 1] in vowels:
                    pref_vowel += 1
            diff = 2 * pref_vowel - i
            residue = i % M
            inner = diff_map[diff]
            ans += inner.get(residue, 0)
            inner[residue] = inner.get(residue, 0) + 1

        return ans
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

static bool isVowel(char c){
    return c=='a'||c=='e'||c=='i'||c=='o'||c=='u';
}

long long beautifulSubstrings(char* s, int k) {
    // compute minimal m such that k divides m^2
    int kk = k;
    long long m = 1;
    for (int p = 2; p * p <= kk; ++p) {
        if (kk % p == 0) {
            int e = 0;
            while (kk % p == 0) { kk /= p; ++e; }
            int need = (e + 1) / 2; // ceil(e/2)
            for (int i = 0; i < need; ++i) m *= p;
        }
    }
    if (kk > 1) {
        // remaining prime factor with exponent 1
        m *= kk; // need power 1
    }

    unordered_map<long long, unordered_map<int,int>> mp;
    long long ans = 0;
    long long prefV = 0;

    // initial prefix at position 0
    long long key0 = 0;               // 2*prefV - pos (pos=0)
    int rem0 = static_cast<int>(prefV % m);
    mp[key0][rem0] = 1;

    for (int i = 0; s[i]; ++i) {
        if (isVowel(s[i])) ++prefV;
        long long pos = i + 1;
        long long key = 2 * prefV - pos;
        int rem = static_cast<int>(prefV % m);
        auto &inner = mp[key];
        auto it = inner.find(rem);
        if (it != inner.end()) {
            ans += it->second;
            ++(it->second);
        } else {
            inner[rem] = 1;
        }
    }
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long BeautifulSubstrings(string s, int k) {
        // Compute minimal D such that D^2 % k == 0
        int D = 1;
        int tempK = k;
        for (int p = 2; p * p <= tempK; ++p) {
            if (tempK % p != 0) continue;
            int exp = 0;
            while (tempK % p == 0) {
                tempK /= p;
                exp++;
            }
            int need = (exp + 1) / 2; // ceil(exp/2)
            for (int i = 0; i < need; ++i) D *= p;
        }
        if (tempK > 1) { // remaining prime factor with exponent 1
            // need ceil(1/2)=1
            D *= tempK;
        }

        long ans = 0;
        int diff = 0;      // vowels - consonants
        int prefV = 0;     // total vowels so far

        var dict = new Dictionary<(int, int), long>();
        // initial prefix at position 0
        dict[(0, 0)] = 1;

        foreach (char ch in s) {
            bool isVowel = ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
            if (isVowel) {
                diff += 1;
                prefV += 1;
            } else {
                diff -= 1;
            }
            int mod = prefV % D; // D >= 1
            var key = (diff, mod);
            if (dict.TryGetValue(key, out long cnt)) {
                ans += cnt;
                dict[key] = cnt + 1;
            } else {
                dict[key] = 1;
            }
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var beautifulSubstrings = function(s, k) {
    // compute minimal m such that m^2 is divisible by k
    let temp = k;
    let m = 1;
    for (let p = 2; p * p <= temp; ++p) {
        if (temp % p === 0) {
            let cnt = 0;
            while (temp % p === 0) {
                temp /= p;
                cnt++;
            }
            const need = Math.ceil(cnt / 2);
            for (let i = 0; i < need; ++i) m *= p;
        }
    }
    if (temp > 1) { // remaining prime factor with exponent 1
        m *= temp;   // ceil(1/2)=1
    }
    const L = 2 * m; // required distance multiple

    const isVowel = ch => {
        return ch === 'a' || ch === 'e' || ch === 'i' || ch === 'o' || ch === 'u';
    };

    let diff = 0;
    const map = new Map(); // key: "diff#rem" -> count
    let ans = 0;

    // initial prefix at index 0
    const initKey = `${diff}#${0 % L}`;
    map.set(initKey, (map.get(initKey) || 0) + 1);

    for (let i = 0; i < s.length; ++i) {
        diff += isVowel(s[i]) ? 1 : -1;
        const idx = i + 1;
        const rem = idx % L;
        const key = `${diff}#${rem}`;
        const cnt = map.get(key) || 0;
        ans += cnt;
        map.set(key, cnt + 1);
    }

    return ans;
};
```

## Typescript

```typescript
function beautifulSubstrings(s: string, k: number): number {
    // compute minimal g such that x^2 % k == 0 iff g divides x
    let kk = k;
    let g = 1;
    for (let p = 2; p * p <= kk; ++p) {
        if (kk % p === 0) {
            let cnt = 0;
            while (kk % p === 0) {
                kk /= p;
                cnt++;
            }
            const need = Math.ceil(cnt / 2);
            for (let i = 0; i < need; ++i) g *= p;
        }
    }
    if (kk > 1) {
        // remaining prime factor with exponent 1
        g *= kk;
    }

    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);
    let V = 0; // total vowels seen so far
    let ans = 0;

    interface Group {
        resCnt: Map<number, number>;
        exact: Map<number, number>;
    }

    const groups = new Map<number, Group>();

    // initial prefix (empty string)
    const initDiff = 0; // 2*V - i where i=0
    const initResidue = 0 % g;
    let initGroup = groups.get(initDiff);
    if (!initGroup) {
        initGroup = { resCnt: new Map(), exact: new Map() };
        groups.set(initDiff, initGroup);
    }
    initGroup.resCnt.set(initResidue, (initGroup.resCnt.get(initResidue) ?? 0) + 1);
    initGroup.exact.set(V, (initGroup.exact.get(V) ?? 0) + 1);

    const n = s.length;
    for (let i = 1; i <= n; ++i) {
        const ch = s.charAt(i - 1);
        if (vowels.has(ch)) V++;
        const diff = 2 * V - i; // D = V - C
        const residue = ((V % g) + g) % g;

        const grp = groups.get(diff);
        if (grp) {
            const cntResidue = grp.resCnt.get(residue) ?? 0;
            const exactFreq = grp.exact.get(V) ?? 0;
            ans += cntResidue - exactFreq;
        }

        let curGrp = grp;
        if (!curGrp) {
            curGrp = { resCnt: new Map(), exact: new Map() };
            groups.set(diff, curGrp);
        }
        curGrp.resCnt.set(residue, (curGrp.resCnt.get(residue) ?? 0) + 1);
        curGrp.exact.set(V, (curGrp.exact.get(V) ?? 0) + 1);
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function beautifulSubstrings($s, $k) {
        // compute minimal M such that k divides x^2 iff M divides x
        $M = 1;
        $temp = $k;
        for ($p = 2; $p * $p <= $temp; $p++) {
            if ($temp % $p == 0) {
                $e = 0;
                while ($temp % $p == 0) {
                    $temp /= $p;
                    $e++;
                }
                $need = intdiv($e + 1, 2); // ceil(e/2)
                for ($i = 0; $i < $need; $i++) {
                    $M *= $p;
                }
            }
        }
        if ($temp > 1) { // remaining prime factor with exponent 1
            $M *= $temp; // need one copy of this prime
        }

        $n = strlen($s);
        $vowelCount = 0;
        $answer = 0;

        // map: diff => [residue => count]
        $map = [];

        // initial prefix (empty string)
        $diff0 = 0;               // 2*0 - 0
        $res0 = 0 % $M;
        $map[$diff0] = [$res0 => 1];

        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if (strpos('aeiou', $ch) !== false) {
                $vowelCount++;
            }
            $pos = $i + 1;                     // length of prefix
            $diff = 2 * $vowelCount - $pos;    // V - C
            $residue = $vowelCount % $M;

            if (isset($map[$diff]) && isset($map[$diff][$residue])) {
                $answer += $map[$diff][$residue];
            }

            if (!isset($map[$diff])) {
                $map[$diff] = [];
            }
            $map[$diff][$residue] = ($map[$diff][$residue] ?? 0) + 1;
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func beautifulSubstrings(_ s: String, _ k: Int) -> Int {
        // Compute minimal m such that x^2 % k == 0 iff x is multiple of m
        var kk = k
        var m = 1
        var p = 2
        while p * p <= kk {
            if kk % p == 0 {
                var cnt = 0
                while kk % p == 0 {
                    kk /= p
                    cnt += 1
                }
                let expM = (cnt + 1) / 2   // ceil(cnt/2)
                for _ in 0..<expM { m *= p }
            }
            p += 1
        }
        if kk > 1 {
            // remaining prime factor with exponent 1
            m *= kk
        }

        var diffMap = [Int: [Int:Int]]()   // diff -> (rem -> count)
        var vowelCount = 0
        var answer = 0

        // initial prefix at position 0
        let initDiff = 0               // 2*0 - 0
        let initRem = 0 % m
        diffMap[initDiff] = [initRem: 1]

        var index = 0   // number of processed characters
        for ch in s {
            if "aeiou".contains(ch) { vowelCount += 1 }
            index += 1
            let diff = 2 * vowelCount - index
            let rem = vowelCount % m

            if var inner = diffMap[diff] {
                if let cnt = inner[rem] {
                    answer += cnt
                    inner[rem] = cnt + 1
                } else {
                    inner[rem] = 1
                }
                diffMap[diff] = inner
            } else {
                diffMap[diff] = [rem: 1]
            }
        }

        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun beautifulSubstrings(s: String, k: Int): Long {
        // compute minimal L such that v^2 % k == 0 iff L divides v
        var kk = k
        var L = 1
        var p = 2
        while (p * p <= kk) {
            if (kk % p == 0) {
                var cnt = 0
                while (kk % p == 0) {
                    kk /= p
                    cnt++
                }
                val need = (cnt + 1) / 2 // ceil(cnt/2)
                repeat(need) { L *= p }
            }
            p++
        }
        if (kk > 1) {
            // remaining prime factor with exponent 1
            val need = 1 // ceil(1/2)=1
            repeat(need) { L *= kk }
        }

        fun isVowel(c: Char): Boolean =
            c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'

        val outer = HashMap<Int, MutableMap<Int, Long>>()
        var diff = 0          // vowels - consonants prefix
        var prefV = 0         // vowel count prefix

        // initial empty prefix
        outer.computeIfAbsent(0) { HashMap() }
            .merge(0, 1L, Long::plus)

        var ans = 0L
        for (ch in s) {
            if (isVowel(ch)) {
                prefV++
                diff++
            } else {
                diff--
            }
            val rem = prefV % L
            val inner = outer.computeIfAbsent(diff) { HashMap() }
            ans += inner.getOrDefault(rem, 0L)
            inner[rem] = inner.getOrDefault(rem, 0L) + 1L
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  bool _isVowel(int codeUnit) {
    // a, e, i, o, u
    return codeUnit == 97 || codeUnit == 101 || codeUnit == 105 ||
        codeUnit == 111 || codeUnit == 117;
  }

  int _minimalM(int k) {
    int m = 1;
    int temp = k;
    for (int p = 2; p * p <= temp; ++p) {
      if (temp % p == 0) {
        int cnt = 0;
        while (temp % p == 0) {
          temp ~/= p;
          cnt++;
        }
        int need = (cnt + 1) >> 1; // ceil(cnt/2)
        for (int i = 0; i < need; ++i) m *= p;
      }
    }
    if (temp > 1) {
      // remaining prime factor with exponent 1
      m *= temp;
    }
    return m;
  }

  int beautifulSubstrings(String s, int k) {
    int n = s.length;
    int m = _minimalM(k);
    // outer map: diff -> (residue -> count)
    final Map<int, Map<int, int>> outer = {};
    // initial prefix at position 0
    outer[0] = {0: 1};

    int vowelCnt = 0;
    int consonantCnt = 0;
    int answer = 0;

    for (int i = 0; i < n; ++i) {
      if (_isVowel(s.codeUnitAt(i))) {
        vowelCnt++;
      } else {
        consonantCnt++;
      }
      int diff = vowelCnt - consonantCnt;
      int residue = vowelCnt % m;

      var inner = outer[diff];
      if (inner == null) {
        inner = {};
        outer[diff] = inner;
      }

      answer += inner[residue] ?? 0;
      inner[residue] = (inner[residue] ?? 0) + 1;
    }
    return answer;
  }
}
```

## Golang

```go
func beautifulSubstrings(s string, k int) int64 {
	// Compute minimal multiplier L such that any x divisible by L satisfies x^2 % k == 0
	L := 1
	tmp := k
	for p := 2; p*p <= tmp; p++ {
		if tmp%p == 0 {
			exp := 0
			for tmp%p == 0 {
				tmp /= p
				exp++
			}
			need := (exp + 1) / 2 // ceil(exp/2)
			for i := 0; i < need; i++ {
				L *= p
			}
		}
	}
	if tmp > 1 { // remaining prime factor with exponent 1
		L *= tmp
	}

	type innerMap map[int]int64
	diffMap := make(map[int]innerMap)

	prefV, prefC := 0, 0
	ans := int64(0)

	// initial prefix (empty string)
	initialDiff := 0
	initialRem := 0 % L
	if _, ok := diffMap[initialDiff]; !ok {
		diffMap[initialDiff] = make(innerMap)
	}
	diffMap[initialDiff][initialRem] = 1

	for i := 0; i < len(s); i++ {
		ch := s[i]
		if ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' {
			prefV++
		} else {
			prefC++
		}
		curDiff := prefV - prefC
		curRem := prefV % L

		if inner, ok := diffMap[curDiff]; ok {
			ans += inner[curRem]
		}

		if _, ok := diffMap[curDiff]; !ok {
			diffMap[curDiff] = make(innerMap)
		}
		diffMap[curDiff][curRem]++
	}

	return ans
}
```

## Ruby

```ruby
def beautiful_substrings(s, k)
  # Compute minimal L such that L^2 % k == 0
  l = 1
  temp = k
  i = 2
  while i * i <= temp
    if temp % i == 0
      cnt = 0
      while temp % i == 0
        temp /= i
        cnt += 1
      end
      exp = (cnt + 1) / 2  # ceil(cnt/2)
      l *= i ** exp
    end
    i += 1
  end
  if temp > 1
    # remaining prime factor with exponent 1
    l *= temp
  end

  d = 2 * l
  counts = Hash.new { |h, _| h[_] = Hash.new(0) }

  diff = 0
  ans = 0

  rem = 0 % d
  ans += counts[diff][rem]
  counts[diff][rem] += 1

  vowels = {'a'=>true,'e'=>true,'i'=>true,'o'=>true,'u'=>true}
  s.each_char.with_index do |ch, idx|
    diff += vowels.key?(ch) ? 1 : -1
    i = idx + 1
    rem = i % d
    ans += counts[diff][rem]
    counts[diff][rem] += 1
  end

  ans
end
```

## Scala

```scala
object Solution {
    def beautifulSubstrings(s: String, k: Int): Long = {
        // compute minimal g such that k divides g^2
        val g: Int = {
            var kk = k
            var res = 1
            var p = 2
            while (p * p <= kk) {
                if (kk % p == 0) {
                    var cnt = 0
                    while (kk % p == 0) { cnt += 1; kk /= p }
                    val need = (cnt + 1) / 2 // ceil(cnt/2)
                    for (_ <- 0 until need) res *= p
                }
                p += 1
            }
            if (kk > 1) {
                // remaining prime factor with exponent 1
                res *= kk
            }
            res
        }

        import scala.collection.mutable

        val outer = mutable.HashMap[Int, mutable.HashMap[Int, Long]]()
        var diff = 0          // vowels - consonants prefix
        var prefV = 0         // vowel count prefix

        // initial empty prefix
        val initInner = mutable.HashMap[Int, Long]()
        initInner.update(0 % g, 1L)
        outer.update(0, initInner)

        var ans: Long = 0L

        def isVowel(ch: Char): Boolean =
            ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u'

        for (ch <- s) {
            if (isVowel(ch)) {
                prefV += 1
                diff += 1
            } else {
                diff -= 1
            }
            val rem = ((prefV % g) + g) % g
            val inner = outer.getOrElseUpdate(diff, mutable.HashMap[Int, Long]())
            ans += inner.getOrElse(rem, 0L)
            inner.update(rem, inner.getOrElse(rem, 0L) + 1L)
        }

        ans
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn beautiful_substrings(s: String, k: i32) -> i64 {
        // Compute minimal m such that m^2 is divisible by k
        let mut kk = k;
        let mut m: i64 = 1;
        let mut p = 2;
        while (p * p) as i32 <= kk {
            if kk % p == 0 {
                let mut cnt = 0;
                while kk % p == 0 {
                    kk /= p;
                    cnt += 1;
                }
                // need exponent ceil(cnt/2)
                let need = (cnt + 1) / 2;
                for _ in 0..need {
                    m *= p as i64;
                }
            }
            p += 1;
        }
        if kk > 1 {
            // remaining prime factor with exponent 1
            m *= kk as i64; // need exponent ceil(1/2)=1
        }

        let l0: i64 = 2 * m; // required distance multiple

        let mut map: HashMap<(i32, i64), i64> = HashMap::new();
        let mut diff: i32 = 0;
        let mut ans: i64 = 0;

        // prefix position 0
        map.insert((diff, 0), 1);

        for (i, ch) in s.chars().enumerate() {
            if matches!(ch, 'a' | 'e' | 'i' | 'o' | 'u') {
                diff += 1;
            } else {
                diff -= 1;
            }
            let pos = (i + 1) as i64; // current prefix index
            let rem = pos % l0;
            let key = (diff, rem);
            if let Some(cnt) = map.get(&key) {
                ans += *cnt;
            }
            *map.entry(key).or_insert(0) += 1;
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (beautiful-substrings s k)
  (-> string? exact-integer? exact-integer?)
  (letrec
      ((vowel?
        (lambda (ch)
          (or (char=? ch #\a) (char=? ch #\e) (char=? ch #\i)
              (char=? ch #\o) (char=? ch #\u))))
       (minimal-m
        (lambda (k)
          (let loop ((m 1))
            (if (= (modulo (* m m) k) 0)
                m
                (loop (+ m 1)))))))
    (let* ((m (minimal-m k))
           (n (string-length s))
           (hash (make-hash))
           (ans 0)
           (D 0)          ; V - C
           (V 0))         ; vowel count
      ;; initial prefix (empty substring)
      (hash-set! hash (vector D (modulo V m)) 1)
      (for ([i (in-range n)])
        (let ((ch (string-ref s i)))
          (if (vowel? ch)
              (begin
                (set! V (+ V 1))
                (set! D (+ D 1)))   ; vowel adds +1 to difference
              (set! D (- D 1))))    ; consonant adds -1
        (let* ((key (vector D (modulo V m)))
               (cnt (hash-ref hash key 0)))
          (set! ans (+ ans cnt))
          (hash-set! hash key (+ cnt 1))))
      ans)))
```

## Erlang

```erlang
-spec beautiful_substrings(S :: unicode:unicode_binary(), K :: integer()) -> integer().
beautiful_substrings(S, K) ->
    L = l_factor(K),
    InitialInner = #{0 => 1},
    OuterMap0 = #{0 => InitialInner},
    process(S, 0, 0, L, OuterMap0, 0).

process(<<>>, _D, _V, _L, _OuterMap, Ans) ->
    Ans;
process(<<C, Rest/binary>>, D, V, L, OuterMap, Ans) ->
    {D1, V1} = if is_vowel(C) -> {D + 1, V + 1};
                true       -> {D - 1, V}
               end,
    Rem = V1 rem L,
    Inner = maps:get(D1, OuterMap, #{}),
    CountPrev = maps:get(Rem, Inner, 0),
    Ans1 = Ans + CountPrev,
    Inner2 = case maps:is_key(Rem, Inner) of
                 true -> maps:update(Rem, fun(Old) -> Old + 1 end, Inner);
                 false -> maps:put(Rem, 1, Inner)
             end,
    OuterMap2 = maps:put(D1, Inner2, OuterMap),
    process(Rest, D1, V1, L, OuterMap2, Ans1).

is_vowel(C) ->
    C == $a orelse C == $e orelse C == $i orelse C == $o orelse C == $u.

l_factor(K) -> l_factor(K, 2, 1).

l_factor(1, _P, Acc) -> Acc;
l_factor(N, P, Acc) when P * P =< N ->
    case count_power(N, P, 0) of
        {N1, 0} ->
            l_factor(N, P + 1, Acc);
        {N1, Exp} ->
            Needed = (Exp + 1) div 2,
            NewAcc = Acc * pow(P, Needed),
            l_factor(N1, P + 1, NewAcc)
    end;
l_factor(N, _P, Acc) -> % N is prime > sqrt(original K)
    Acc * N.

count_power(N, P, C) when N rem P == 0 ->
    count_power(N div P, P, C + 1);
count_power(N, _P, C) ->
    {N, C}.

pow(Base, Exp) -> pow(Base, Exp, 1).

pow(_B, 0, Acc) -> Acc;
pow(B, E, Acc) when E rem 2 == 1 ->
    pow(B * B, E div 2, Acc * B);
pow(B, E, Acc) ->
    pow(B * B, E div 2, Acc).
```

## Elixir

```elixir
defmodule Solution do
  @spec beautiful_substrings(String.t(), integer()) :: integer()
  def beautiful_substrings(s, k) do
    l = minimal_l(k)

    # map of {diff, prefV mod l} => count, start with empty prefix
    init_map = %{{0, 0} => 1}
    {ans, _diff, _pref_v, _map} =
      String.graphemes(s)
      |> Enum.reduce({0, 0, 0, init_map}, fn ch, {cnt, diff, pref_v, m} ->
        is_vowel = vowel?(ch)

        diff = if is_vowel, do: diff + 1, else: diff - 1
        pref_v = if is_vowel, do: pref_v + 1, else: pref_v

        mod = rem(pref_v, l)
        key = {diff, mod}
        add = Map.get(m, key, 0)

        cnt = cnt + add
        m = Map.update(m, key, 1, &(&1 + 1))

        {cnt, diff, pref_v, m}
      end)

    ans
  end

  defp vowel?(c) do
    case c do
      "a" -> true
      "e" -> true
      "i" -> true
      "o" -> true
      "u" -> true
      _ -> false
    end
  end

  # minimal L such that L^2 is divisible by k
  defp minimal_l(k) do
    factorize(k, 2, %{})
    |> Enum.reduce(1, fn {p, e}, acc ->
      need = div(e + 1, 2)
      acc * ipow(p, need)
    end)
  end

  # integer power
  defp ipow(_, 0), do: 1
  defp ipow(base, exp) when rem(exp, 2) == 0 do
    half = ipow(base, div(exp, 2))
    half * half
  end
  defp ipow(base, exp), do: base * ipow(base, exp - 1)

  # factorize n into map prime => exponent
  defp factorize(0, _p, acc), do: acc
  defp factorize(n, p, acc) when p * p > n do
    if n > 1 do
      Map.update(acc, n, 1, &(&1 + 1))
    else
      acc
    end
  end

  defp factorize(n, p, acc) do
    if rem(n, p) == 0 do
      {cnt, rest} = count_factor(n, p, 0)
      acc = Map.update(acc, p, cnt, &(&1 + cnt))
      factorize(rest, p + 1, acc)
    else
      factorize(n, p + 1, acc)
    end
  end

  defp count_factor(n, p, c) do
    if rem(n, p) == 0 do
      count_factor(div(n, p), p, c + 1)
    else
      {c, n}
    end
  end
end
```
