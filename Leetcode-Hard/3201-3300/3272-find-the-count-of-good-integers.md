# 3272. Find the Count of Good Integers

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long countGoodIntegers(int n, int k) {
        vector<long long> fact(n + 1, 1);
        for (int i = 1; i <= n; ++i) fact[i] = fact[i - 1] * i;
        
        unordered_set<string> seen;
        long long ans = 0;
        
        auto ipow = [&](int base, int exp) {
            int res = 1;
            while (exp--) res *= base;
            return res;
        };
        
        if (n == 1) {
            for (int d = 1; d <= 9; ++d) {
                if (d % k == 0) ans += 1; // only one permutation
            }
            return ans;
        }
        
        int halfLen = n / 2;
        int start = (halfLen == 0) ? 0 : ipow(10, halfLen - 1);
        int end   = ipow(10, halfLen);
        
        for (int leftNum = start; leftNum < end; ++leftNum) {
            string left = to_string(leftNum);
            while ((int)left.size() < halfLen) left = "0" + left;
            string revLeft = left;
            reverse(revLeft.begin(), revLeft.end());
            
            if (n % 2 == 0) { // even length
                string pal = left + revLeft;
                long long mod = 0;
                for (char ch : pal) mod = (mod * 10 + (ch - '0')) % k;
                if (mod != 0) continue;
                
                string sortedPal = pal;
                sort(sortedPal.begin(), sortedPal.end());
                if (seen.count(sortedPal)) continue;
                seen.insert(sortedPal);
                
                int cnt[10] = {0};
                for (char ch : pal) ++cnt[ch - '0'];
                int c0 = cnt[0];
                long long numerator = 1LL * (n - c0) * fact[n - 1];
                long long denominator = 1;
                for (int i = 0; i < 10; ++i) denominator *= fact[cnt[i]];
                ans += numerator / denominator;
            } else { // odd length
                for (int mid = 0; mid <= 9; ++mid) {
                    string pal = left + char('0' + mid) + revLeft;
                    long long mod = 0;
                    for (char ch : pal) mod = (mod * 10 + (ch - '0')) % k;
                    if (mod != 0) continue;
                    
                    string sortedPal = pal;
                    sort(sortedPal.begin(), sortedPal.end());
                    if (seen.count(sortedPal)) continue;
                    seen.insert(sortedPal);
                    
                    int cnt[10] = {0};
                    for (char ch : pal) ++cnt[ch - '0'];
                    int c0 = cnt[0];
                    long long numerator = 1LL * (n - c0) * fact[n - 1];
                    long long denominator = 1;
                    for (int i = 0; i < 10; ++i) denominator *= fact[cnt[i]];
                    ans += numerator / denominator;
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public long countGoodIntegers(int n, int k) {
        long[] fact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; ++i) fact[i] = fact[i - 1] * i;

        Set<String> seen = new HashSet<>();
        long ans = 0;

        int m = (n + 1) / 2;
        int start = (int) Math.pow(10, m - 1);
        int end = (int) Math.pow(10, m) - 1;

        for (int i = start; i <= end; ++i) {
            String left = String.format("%0" + m + "d", i);
            StringBuilder sb = new StringBuilder();
            sb.append(left);
            int idxStart = (n % 2 == 0) ? m - 1 : m - 2;
            for (int j = idxStart; j >= 0; --j) {
                sb.append(left.charAt(j));
            }
            String pal = sb.toString();

            long val = Long.parseLong(pal);
            if (val % k != 0) continue;

            char[] sorted = pal.toCharArray();
            Arrays.sort(sorted);
            String key = new String(sorted);
            if (!seen.add(key)) continue; // already processed

            int[] cnt = new int[10];
            for (int p = 0; p < n; ++p) cnt[pal.charAt(p) - '0']++;

            long numerator = (long) (n - cnt[0]) * fact[n - 1];
            long denom = 1;
            for (int d = 0; d <= 9; ++d) {
                denom *= fact[cnt[d]];
            }
            ans += numerator / denom;
        }

        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def countGoodIntegers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # factorials up to n
        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i

        seen = set()
        ans = 0

        half = n // 2
        if n % 2 == 0:
            # even length: generate left half of length half
            start = 10 ** (half - 1) if half > 0 else 0
            end = 10 ** half
            for left in range(start, end):
                s = str(left)
                pal = s + s[::-1]
                if int(pal) % k != 0:
                    continue
                # count digits
                cnt = [0] * 10
                for ch in pal:
                    cnt[ord(ch) - 48] += 1
                key = tuple(cnt)
                if key in seen:
                    continue
                seen.add(key)

                c0 = cnt[0]
                ways = (n - c0) * fact[n - 1]
                for c in cnt:
                    ways //= fact[c]
                ans += ways
        else:
            # odd length: generate prefix of length half+1 (includes middle)
            pref_len = half + 1
            start = 10 ** (pref_len - 1)
            end = 10 ** pref_len
            for left in range(start, end):
                s = str(left)
                pal = s + s[-2::-1]  # mirror without the last character
                if int(pal) % k != 0:
                    continue
                cnt = [0] * 10
                for ch in pal:
                    cnt[ord(ch) - 48] += 1
                key = tuple(cnt)
                if key in seen:
                    continue
                seen.add(key)

                c0 = cnt[0]
                ways = (n - c0) * fact[n - 1]
                for c in cnt:
                    ways //= fact[c]
                ans += ways

        return ans
```

## Python3

```python
class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # factorials up to n
        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i

        m = (n + 1) // 2  # length of left part including middle if odd
        start = 10 ** (m - 1)  # first digit cannot be zero
        end = 10 ** m

        seen = set()
        ans = 0

        for i in range(start, end):
            s_left = str(i)
            if n % 2 == 0:
                s_pal = s_left + s_left[::-1]
            else:
                s_pal = s_left + s_left[-2::-1]  # skip middle char
            # check divisibility by k
            if int(s_pal) % k != 0:
                continue

            cnt = [0] * 10
            for ch in s_pal:
                cnt[ord(ch) - 48] += 1
            key = tuple(cnt)
            if key in seen:
                continue
            seen.add(key)

            c0 = cnt[0]
            total_perm = (n - c0) * fact[n - 1]
            denom = 1
            for c in cnt:
                denom *= fact[c]
            ans += total_perm // denom

        return ans
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

long long countGoodIntegers(int n, int k) {
    // factorials up to 10
    long long fact[11];
    fact[0] = 1;
    for (int i = 1; i <= 10; ++i) fact[i] = fact[i - 1] * i;

    // powers of 10
    int pow10[11];
    pow10[0] = 1;
    for (int i = 1; i <= 10; ++i) pow10[i] = pow10[i - 1] * 10;

    int half = (n + 1) / 2;                 // ceil(n/2)
    int start = pow10[half - 1];            // first digit non‑zero
    int end   = pow10[half];

    unordered_set<string> seen;
    long long ans = 0;

    string left(half, '0');
    for (int num = start; num < end; ++num) {
        // build left part with leading zeros to length half
        int tmp = num;
        for (int i = half - 1; i >= 0; --i) {
            left[i] = char('0' + (tmp % 10));
            tmp /= 10;
        }

        // construct palindrome string of length n
        string pal = left;
        if (n % 2 == 0) {
            for (int i = half - 1; i >= 0; --i) pal.push_back(left[i]);
        } else {
            for (int i = half - 2; i >= 0; --i) pal.push_back(left[i]);
        }

        // check divisibility by k
        long long val = 0;
        for (char c : pal) {
            val = val * 10 + (c - '0');
        }
        if (val % k != 0) continue;

        // sort digits to obtain canonical key
        string key = pal;
        sort(key.begin(), key.end());
        if (seen.find(key) != seen.end()) continue;
        seen.insert(key);

        // count digit frequencies
        int cnt[10] = {0};
        for (char c : pal) ++cnt[c - '0'];
        int cnt0 = cnt[0];

        long long numerator = 1LL * (n - cnt0) * fact[n - 1];
        long long denominator = 1;
        for (int d = 0; d <= 9; ++d) denominator *= fact[cnt[d]];
        ans += numerator / denominator;
    }
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Text;

public class Solution {
    public long CountGoodIntegers(int n, int k) {
        // factorials up to 10
        long[] fact = new long[11];
        fact[0] = 1;
        for (int i = 1; i <= 10; i++) fact[i] = fact[i - 1] * i;

        int leftLen = (n + 1) / 2;
        int start = (int)Math.Pow(10, leftLen - 1);
        int end = (int)Math.Pow(10, leftLen) - 1;

        HashSet<string> seen = new HashSet<string>();
        long ans = 0;

        for (int left = start; left <= end; left++) {
            int[] digits = new int[n];
            // fill left part
            int temp = left;
            for (int i = leftLen - 1; i >= 0; i--) {
                digits[i] = temp % 10;
                temp /= 10;
            }
            // mirror to right side
            for (int i = 0; i < n / 2; i++) {
                digits[n - 1 - i] = digits[i];
            }

            long value = 0;
            foreach (int d in digits) {
                value = value * 10 + d;
            }
            if (value % k != 0) continue;

            int[] cnt = new int[10];
            foreach (int d in digits) cnt[d]++;

            // create a unique key for the multiset of digits
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 10; i++) {
                sb.Append(cnt[i]);
                sb.Append('#');
            }
            string key = sb.ToString();
            if (seen.Contains(key)) continue;
            seen.Add(key);

            long denom = 1;
            for (int i = 0; i < 10; i++) {
                denom *= fact[cnt[i]];
            }

            long ways = ((long)(n - cnt[0]) * fact[n - 1]) / denom;
            ans += ways;
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var countGoodIntegers = function(n, k) {
    // factorials up to 10
    const fact = [1];
    for (let i = 1; i <= 10; ++i) fact[i] = fact[i - 1] * i;

    const halfLen = Math.floor((n + 1) / 2);
    const start = Math.pow(10, halfLen - 1); // first digit cannot be zero
    const end = Math.pow(10, halfLen) - 1;

    const seen = new Set();
    let ans = 0;

    for (let left = start; left <= end; ++left) {
        const leftStr = left.toString();

        // build palindrome of length n
        let revPart;
        if (n % 2 === 0) {
            revPart = leftStr.split('').reverse().join('');
        } else {
            revPart = leftStr.slice(0, -1).split('').reverse().join('');
        }
        const fullStr = leftStr + revPart;

        // check k-divisibility
        if (Number(fullStr) % k !== 0) continue;

        // canonical key: sorted digits
        const key = fullStr.split('').sort().join('');
        if (seen.has(key)) continue;
        seen.add(key);

        // count digit frequencies
        const cnt = new Array(10).fill(0);
        for (let ch of fullStr) {
            cnt[ch.charCodeAt(0) - 48]++; // '0' char code is 48
        }
        const c0 = cnt[0];
        const total = n;

        let numerator = (total - c0) * fact[total - 1];
        let denominator = 1;
        for (let i = 0; i <= 9; ++i) {
            denominator *= fact[cnt[i]];
        }
        ans += Math.floor(numerator / denominator);
    }

    return ans;
};
```

## Typescript

```typescript
function countGoodIntegers(n: number, k: number): number {
    const fact = new Array<number>(n + 1);
    fact[0] = 1;
    for (let i = 1; i <= n; ++i) fact[i] = fact[i - 1] * i;

    const halfLen = Math.floor((n + 1) / 2);
    const start = Math.pow(10, halfLen - 1);
    const end = Math.pow(10, halfLen);

    const seen = new Set<string>();

    for (let i = start; i < end; ++i) {
        const left = i.toString().padStart(halfLen, '0');
        const rev = left.split('').reverse().join('');
        let pal: string;
        if (n % 2 === 0) {
            pal = left + rev;
        } else {
            pal = left + rev.slice(1);
        }
        const num = Number(pal);
        if (num % k !== 0) continue;
        const sorted = pal.split('').sort().join('');
        seen.add(sorted);
    }

    let ans = 0;
    for (const s of seen) {
        const cnt = new Array<number>(10).fill(0);
        for (const ch of s) cnt[ch.charCodeAt(0) - 48]++;
        const c0 = cnt[0];
        const numerator = (n - c0) * fact[n - 1];
        let denom = 1;
        for (let d = 0; d <= 9; ++d) denom *= fact[cnt[d]];
        ans += numerator / denom;
    }
    return ans;
}
```

## Php

```php
<?php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function countGoodIntegers($n, $k) {
        // factorials up to 10
        $fact = array_fill(0, $n + 1, 1);
        for ($i = 1; $i <= $n; $i++) {
            $fact[$i] = $fact[$i - 1] * $i;
        }

        // length of left half (including middle digit when n is odd)
        $m = intdiv($n + 1, 2);   // ceil(n/2)

        $start = (int)pow(10, $m - 1);          // smallest left part without leading zero
        $end   = (int)pow(10, $m) - 1;          // largest left part

        $seen = [];
        $ans = 0;

        for ($left = $start; $left <= $end; $left++) {
            $sLeft = strval($left);
            $rev   = strrev($sLeft);
            if ($n % 2 == 0) {
                $palStr = $sLeft . $rev;
            } else {
                $palStr = $sLeft . substr($rev, 1); // drop duplicated middle digit
            }

            // check divisibility by k
            if ((int)$palStr % $k !== 0) continue;

            // count digits
            $cnt = array_fill(0, 10, 0);
            for ($i = 0; $i < $n; $i++) {
                $digit = intval($palStr[$i]);
                $cnt[$digit]++;
            }

            // unique key for this multiset of digits
            $key = implode('#', $cnt);
            if (isset($seen[$key])) continue;
            $seen[$key] = true;

            // number of permutations without leading zero
            $nonZeroFirst = $n - $cnt[0];
            $numerator = $nonZeroFirst * $fact[$n - 1];
            $denominator = 1;
            for ($d = 0; $d <= 9; $d++) {
                $denominator *= $fact[$cnt[$d]];
            }
            $add = intdiv($numerator, $denominator);
            $ans += $add;
        }

        return $ans;
    }
}
?>
```

## Swift

```swift
import Foundation

class Solution {
    func countGoodIntegers(_ n: Int, _ k: Int) -> Int {
        var uniqueSortedDigits = Set<String>()
        let halfLen = (n + 1) / 2   // ceil(n/2)
        
        func intPow10(_ exp: Int) -> Int {
            var res = 1
            for _ in 0..<exp { res *= 10 }
            return res
        }
        
        let start = intPow10(halfLen - 1)          // first digit non‑zero
        let end   = intPow10(halfLen) - 1
        
        for left in start...end {
            let leftStr = String(left)
            var revPart: String
            if n % 2 == 0 {
                revPart = String(leftStr.reversed())
            } else {
                var tmp = leftStr
                tmp.removeLast()
                revPart = String(tmp.reversed())
            }
            let palindromeStr = leftStr + revPart
            // check divisibility by k
            if Int64(palindromeStr)! % Int64(k) != 0 { continue }
            // store sorted digit multiset
            let key = String(palindromeStr.sorted())
            uniqueSortedDigits.insert(key)
        }
        
        // factorials up to n
        var fact = [Int64](repeating: 1, count: n + 1)
        for i in 1...n {
            fact[i] = fact[i - 1] * Int64(i)
        }
        
        var answer: Int64 = 0
        
        for key in uniqueSortedDigits {
            var cnt = [Int](repeating: 0, count: 10)
            for ch in key {
                let d = Int(ch.unicodeScalars.first!.value - 48)
                cnt[d] += 1
            }
            let c0 = cnt[0]
            let nonZeroFirstChoices = n - c0
            var denom: Int64 = 1
            for i in 0..<10 {
                denom *= fact[cnt[i]]
            }
            // (n - c0) * (n-1)! / product cnt[i]!
            let ways = Int64(nonZeroFirstChoices) * fact[n - 1] / denom
            answer += ways
        }
        
        return Int(answer)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countGoodIntegers(n: Int, k: Int): Long {
        // factorials up to n
        val fact = LongArray(n + 1)
        fact[0] = 1L
        for (i in 1..n) fact[i] = fact[i - 1] * i

        val visited = HashSet<String>()
        var answer = 0L

        val leftLen = (n + 1) / 2  // ceil(n/2)

        fun intPow10(exp: Int): Int {
            var res = 1
            repeat(exp) { res *= 10 }
            return res
        }

        val start = intPow10(leftLen - 1)
        val end = intPow10(leftLen) - 1

        for (i in start..end) {
            val leftStr = i.toString()
            // build palindrome of length n
            val pal = if (n % 2 == 0) {
                leftStr + leftStr.reversed()
            } else {
                leftStr + leftStr.substring(0, leftLen - 1).reversed()
            }

            // check divisibility by k
            var rem = 0
            for (ch in pal) {
                rem = (rem * 10 + (ch - '0')) % k
            }
            if (rem != 0) continue

            // digit counts
            val cnt = IntArray(10)
            for (ch in pal) cnt[ch - '0']++

            // unique key for this multiset
            val keyBuilder = StringBuilder()
            for (d in 0..9) {
                keyBuilder.append(cnt[d]).append('#')
            }
            val key = keyBuilder.toString()
            if (!visited.add(key)) continue

            var denom = 1L
            for (d in 0..9) {
                denom *= fact[cnt[d]]
            }
            val numerator = (n - cnt[0]).toLong() * fact[n - 1]
            val add = numerator / denom
            answer += add
        }

        return answer
    }
}
```

## Dart

```dart
class Solution {
  int countGoodIntegers(int n, int k) {
    // factorials up to n
    List<int> fact = List.filled(n + 1, 1);
    for (int i = 1; i <= n; ++i) {
      fact[i] = fact[i - 1] * i;
    }

    int m = (n + 1) ~/ 2; // ceil half length
    int start = _ipow(10, m - 1);
    int end = _ipow(10, m) - 1;

    Set<String> seen = {};
    int ans = 0;

    for (int left = start; left <= end; ++left) {
      String leftStr = left.toString().padLeft(m, '0');

      String right;
      if (n % 2 == 0) {
        right = leftStr.split('').reversed.join();
      } else {
        right = leftStr.substring(0, m - 1).split('').reversed.join();
      }

      String palStr = leftStr + right;
      int val = int.parse(palStr);
      if (val % k != 0) continue;

      List<String> chars = palStr.split('');
      chars.sort();
      String key = chars.join();

      if (seen.contains(key)) continue;
      seen.add(key);

      // count digit frequencies
      List<int> cnt = List.filled(10, 0);
      for (var ch in chars) {
        cnt[int.parse(ch)]++;
      }

      int zeroCnt = cnt[0];
      int total = (n - zeroCnt) * fact[n - 1];
      for (int i = 0; i < 10; ++i) {
        total ~/= fact[cnt[i]];
      }
      ans += total;
    }

    return ans;
  }

  int _ipow(int base, int exp) {
    int result = 1;
    while (exp > 0) {
      if ((exp & 1) == 1) result *= base;
      base *= base;
      exp >>= 1;
    }
    return result;
  }
}
```

## Golang

```go
func countGoodIntegers(n int, k int) int64 {
    // factorials up to n
    fact := make([]int64, n+1)
    fact[0] = 1
    for i := 1; i <= n; i++ {
        fact[i] = fact[i-1] * int64(i)
    }

    leftLen := (n + 1) / 2 // ceil(n/2)

    ans := int64(0)
    visited := make(map[uint64]struct{})

    var dfs func(pos int, cur []int)
    dfs = func(pos int, cur []int) {
        if pos == leftLen {
            // build full palindrome
            pal := make([]int, n)
            for i := 0; i < leftLen; i++ {
                pal[i] = cur[i]
                pal[n-1-i] = cur[i]
            }
            // compute numeric value
            var val int64 = 0
            for _, d := range pal {
                val = val*10 + int64(d)
            }
            if int(val%int64(k)) != 0 {
                return
            }

            // count digit frequencies
            cnt := [10]int{}
            for _, d := range pal {
                cnt[d]++
            }

            // encode multiset as key
            var key uint64 = 0
            for i := 0; i < 10; i++ {
                key |= uint64(cnt[i]) << (uint(i) * 4)
            }
            if _, ok := visited[key]; ok {
                return
            }
            visited[key] = struct{}{}

            cnt0 := cnt[0]
            perm := int64(n-cnt0) * fact[n-1]
            for i := 0; i < 10; i++ {
                perm /= fact[cnt[i]]
            }
            ans += perm
            return
        }

        start := 0
        if pos == 0 {
            start = 1 // leading digit cannot be zero
        }
        for d := start; d <= 9; d++ {
            cur[pos] = d
            dfs(pos+1, cur)
        }
    }

    digits := make([]int, leftLen)
    dfs(0, digits)

    return ans
}
```

## Ruby

```ruby
def count_good_integers(n, k)
  half = (n + 1) / 2
  start = 10**(half - 1)
  finish = 10**half - 1

  # factorials up to n
  fact = Array.new(n + 1, 1)
  (1..n).each { |i| fact[i] = fact[i - 1] * i }

  seen = {}

  (start..finish).each do |left|
    s_left = left.to_s
    pal =
      if n.even?
        s_left + s_left.reverse
      else
        s_left + s_left[0...-1].reverse
      end

    next unless pal.length == n
    val = pal.to_i
    next unless (val % k).zero?

    key = pal.chars.sort.join
    seen[key] = true
  end

  ans = 0
  seen.each_key do |key|
    cnt = Array.new(10, 0)
    key.each_char { |ch| cnt[ch.ord - 48] += 1 }

    non_zero = n - cnt[0]
    next if non_zero.zero?

    ways = non_zero * fact[n - 1]
    (0..9).each { |d| ways /= fact[cnt[d]] }
    ans += ways
  end

  ans
end
```

## Scala

```scala
object Solution {
    def countGoodIntegers(n: Int, k: Int): Long = {
        // factorials up to 10 as BigInt
        val fact = new Array[scala.math.BigInt](11)
        fact(0) = scala.math.BigInt(1)
        for (i <- 1 to 10) fact(i) = fact(i - 1) * i

        val m = (n + 1) / 2 // number of digits that define the palindrome

        var start = 1
        for (_ <- 1 until m) start *= 10          // 10^(m-1)
        var end = 1
        for (_ <- 0 until m) end *= 10            // 10^m
        end -= 1

        val seen = scala.collection.mutable.HashSet[String]()
        var ans: Long = 0L

        for (num <- start to end) {
            val leftStr = num.toString                     // exactly m digits, no leading zero
            val palStr =
                if (n % 2 == 0)
                    leftStr + leftStr.reverse
                else
                    leftStr + leftStr.substring(0, m - 1).reverse

            // check k‑palindromic condition
            if ((palStr.toLong % k) == 0) {
                val key = palStr.sorted
                if (!seen.contains(key)) {
                    seen.add(key)

                    // digit counts
                    val cnt = new Array[Int](10)
                    for (ch <- palStr) cnt(ch - '0') += 1

                    val c0 = cnt(0)
                    var denom: scala.math.BigInt = scala.math.BigInt(1)
                    for (i <- 0 to 9) denom *= fact(cnt(i))

                    val contrib = (scala.math.BigInt(n - c0) * fact(n - 1)) / denom
                    ans += contrib.longValue
                }
            }
        }

        ans
    }
}
```

## Rust

```rust
use std::collections::HashSet;

impl Solution {
    pub fn count_good_integers(n: i32, k: i32) -> i64 {
        let n_usize = n as usize;
        let len_left = (n_usize + 1) / 2; // ceiling of n/2
        // factorials up to 10
        let mut fact = vec![1i64; 11];
        for i in 1..=10 {
            fact[i] = fact[i - 1] * i as i64;
        }

        let start = 10usize.pow((len_left - 1) as u32);
        let end = 10usize.pow(len_left as u32); // exclusive

        let mut seen: HashSet<[u8; 10]> = HashSet::new();
        let mut ans: i64 = 0;

        for num in start..end {
            // extract left part digits
            let mut left_digits = vec![0u8; len_left];
            let mut tmp = num;
            for i in (0..len_left).rev() {
                left_digits[i] = (tmp % 10) as u8;
                tmp /= 10;
            }

            // build full palindrome digits
            let mut digits: Vec<u8> = left_digits.clone();
            if n % 2 == 0 {
                for i in (0..len_left).rev() {
                    digits.push(left_digits[i]);
                }
            } else {
                for i in (0..len_left - 1).rev() {
                    digits.push(left_digits[i]);
                }
            }

            // compute numeric value
            let mut val: u64 = 0;
            for &d in &digits {
                val = val * 10 + d as u64;
            }
            if val % k as u64 != 0 {
                continue;
            }

            // count digit frequencies
            let mut cnt = [0u8; 10];
            for &d in &digits {
                cnt[d as usize] += 1;
            }

            if seen.contains(&cnt) {
                continue;
            }
            seen.insert(cnt);

            // number of permutations without leading zero
            let total = n as i64;
            let c0 = cnt[0] as i64;
            let mut denom: i64 = 1;
            for &c in cnt.iter() {
                denom *= fact[c as usize];
            }
            let ways = (total - c0) * fact[(total - 1) as usize] / denom;
            ans += ways;
        }

        ans
    }
}
```

## Racket

```racket
(define (count-good-integers n k)
  (define (pow10 e) (expt 10 e))
  ;; factorials up to n
  (define fact
    (let loop ((i 0) (acc 1) (lst (list 1)))
      (if (> i n)
          (reverse lst)
          (loop (+ i 1) (* acc i) (cons (* acc i) lst)))))
  (define (fact-at idx) (list-ref fact idx))
  ;; product of factorials of counts
  (define (prod-fact cnts)
    (let loop ((i 0) (p 1))
      (if (= i 10)
          p
          (loop (+ i 1) (* p (fact-at (vector-ref cnts i)))))))
  ;; compute number of good permutations for a digit multiset
  (define (good-perms cnts)
    (let* ((cnt0 (vector-ref cnts 0))
           (numerator (* (- n cnt0) (fact-at (- n 1))))
           (denominator (prod-fact cnts)))
      (/ numerator denominator)))
  ;; generate palindrome string from left part integer
  (define (palindrome-from-left left half even?)
    (let* ((s (number->string left))
           (len (string-length s))
           (left-list (string->list s)))
      (if even?
          (list->string (append left-list (reverse left-list)))
          (let* ((prefix (substring s 0 (- len 1)))
                 (rev (reverse (string->list prefix))))
            (list->string (append left-list rev))))))
  ;; main enumeration
  (let* ((half (quotient (+ n 1) 2))
         (even? (= (modulo n 2) 0))
         (start (pow10 (- half 1)))
         (end (sub1 (pow10 half)))
         (seen (make-hash))
         (ans
          (let loop ((left start) (total 0))
            (if (> left end)
                total
                (let* ((pal-str (palindrome-from-left left half even?))
                       (pal-num (string->number pal-str)))
                  (if (= (remainder pal-num k) 0)
                      (let* ((cnts (make-vector 10 0)))
                        (for ([ch (in-string pal-str)])
                          (vector-set! cnts
                                       (- (char->integer ch) (char->integer #\0))
                                       (+ 1 (vector-ref cnts
                                                        (- (char->integer ch)
                                                           (char->integer #\0))))))
                        (let ((key (list->string (sort (string->list pal-str) char<?))))
                          (if (hash-has-key? seen key)
                              (loop (+ left 1) total)
                              (begin
                                (hash-set! seen key #t)
                                (loop (+ left 1)
                                      (+ total (good-perms cnts)))))))
                      (loop (+ left 1) total))))))
    ans))
```

## Erlang

```erlang
-spec count_good_integers(N :: integer(), K :: integer()) -> integer().
count_good_integers(N, K) ->
    Half = (N + 1) div 2,
    Start = pow10(Half - 1),
    End = pow10(Half) - 1,
    PalMap = enumerate_palindromes(Start, End, N, K, #{}),
    FactList = [fact(I) || I <- lists:seq(0, N)],
    maps:fold(fun(_Key, _Val, Acc) ->
                      Digits = tuple_to_list(_Key),
                      Counts = count_digits(Digits, 10, lists:duplicate(10, 0)),
                      C0 = lists:nth(1, Counts), % count of digit 0
                      ProdFact = prod_factorials(Counts, FactList, 1),
                      Add = ((N - C0) * lists:nth(N, FactList)) div ProdFact,
                      Acc + Add
              end, 0, PalMap).

%% Enumerate all palindromes in the given range and collect unique sorted digit tuples.
enumerate_palindromes(I, End, N, K, Map) when I =< End ->
    DigLeft = int_to_digits(I),
    FullDigits = build_full(DigLeft, N),
    Value = digits_to_int(FullDigits),
    NewMap = if
        Value rem K == 0 ->
            Sorted = lists:sort(FullDigits),
            Key = list_to_tuple(Sorted),
            case maps:is_key(Key, Map) of
                true -> Map;
                false -> maps:put(Key, true, Map)
            end;
        true -> Map
    end,
    enumerate_palindromes(I + 1, End, N, K, NewMap);
enumerate_palindromes(_, _, _, _, Map) ->
    Map.

%% Build full palindrome digits from left part.
build_full(Left, N) when N rem 2 == 0 ->
    Left ++ lists:reverse(Left);
build_full(Left, N) ->
    Len = length(Left),
    MidRemoved = lists:sublist(Left, Len - 1),
    Left ++ lists:reverse(MidRemoved).

%% Convert integer to list of its decimal digits.
int_to_digits(I) ->
    lists:map(fun(C) -> C - $0 end, integer_to_list(I)).

%% Convert list of digits to integer value.
digits_to_int(Ds) ->
    lists:foldl(fun(D, Acc) -> Acc * 10 + D end, 0, Ds).

%% Count occurrences of each digit (0..9).
count_digits([], _Base, Counts) -> Counts;
count_digits([D | Rest], Base, Counts) ->
    Index = D + 1,
    Old = lists:nth(Index, Counts),
    NewCounts = set_nth(Index, Old + 1, Counts),
    count_digits(Rest, Base, NewCounts).

set_nth(1, Val, [_|Tail]) -> [Val | Tail];
set_nth(N, Val, [H|Tail]) when N > 1 ->
    [H | set_nth(N-1, Val, Tail)].

%% Product of factorials for each digit count.
prod_factorials([], _FactList, Acc) -> Acc;
prod_factorials([C | Rest], FactList, Acc) ->
    Prod = Acc * lists:nth(C + 1, FactList),
    prod_factorials(Rest, FactList, Prod).

%% Integer power of 10.
pow10(Exp) when Exp >= 0 -> int_pow(10, Exp).

int_pow(_, 0) -> 1;
int_pow(Base, Exp) -> Base * int_pow(Base, Exp - 1).

%% Factorial (small n).
fact(0) -> 1;
fact(N) -> N * fact(N - 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_good_integers(n :: integer, k :: integer) :: integer
  def count_good_integers(n, k) do
    fac = factorials(n)
    {ans, _} = enumerate(n, k, fac, MapSet.new(), 0)
    ans
  end

  # factorial map: i => i!
  defp factorials(n) do
    Enum.reduce(0..n, %{}, fn i, acc ->
      val = if i == 0, do: 1, else: Map.get(acc, i - 1) * i
      Map.put(acc, i, val)
    end)
  end

  defp enumerate(n, k, fac, set, ans) when n == 1 do
    ans =
      Enum.reduce(1..9, ans, fn d, a ->
        if rem(d, k) == 0 do
          cnt = List.duplicate(0, 10) |> List.update_at(d, &(&1 + 1))
          a + good_count(cnt, n, fac)
        else
          a
        end
      end)

    {ans, set}
  end

  defp enumerate(n, k, fac, set, ans) do
    half = div(n, 2)
    start = trunc(:math.pow(10, half - 1))
    finish = trunc(:math.pow(10, half)) - 1

    Enum.reduce(start..finish, {ans, set}, fn left, {a, s} ->
      left_str = Integer.to_string(left)
      rev = String.reverse(left_str)

      if rem(n, 2) == 0 do
        pal = left_str <> rev
        process_pal(pal, k, n, fac, a, s)
      else
        Enum.reduce(0..9, {a, s}, fn mid, {aa, ss} ->
          pal = left_str <> Integer.to_string(mid) <> rev
          process_pal(pal, k, n, fac, aa, ss)
        end)
      end
    end)
  end

  defp process_pal(pal, k, n, fac, ans, set) do
    num = String.to_integer(pal)

    if rem(num, k) != 0 do
      {ans, set}
    else
      sorted = pal |> String.graphemes() |> Enum.sort() |> Enum.join()

      if MapSet.member?(set, sorted) do
        {ans, set}
      else
        cnt = digit_counts(pal)
        add = good_count(cnt, n, fac)
        {ans + add, MapSet.put(set, sorted)}
      end
    end
  end

  defp digit_counts(str) do
    Enum.reduce(String.graphemes(str), List.duplicate(0, 10), fn ch, acc ->
      d = String.to_integer(ch)
      List.update_at(acc, d, &(&1 + 1))
    end)
  end

  defp good_count(cnt, n, fac) do
    cnt0 = Enum.at(cnt, 0)
    non_zero = n - cnt0

    if non_zero == 0 do
      0
    else
      num = non_zero * Map.get(fac, n - 1)
      den = Enum.reduce(cnt, 1, fn c, acc -> acc * Map.get(fac, c) end)
      div(num, den)
    end
  end
end
```
