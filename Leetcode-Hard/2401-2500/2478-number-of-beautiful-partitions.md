# 2478. Number of Beautiful Partitions

## Cpp

```cpp
class Solution {
public:
    int beautifulPartitions(string s, int k, int minLength) {
        const int MOD = 1'000'000'007;
        int n = s.size();
        auto isPrime = [&](char c)->bool{
            return c=='2'||c=='3'||c=='5'||c=='7';
        };
        if (!isPrime(s[0]) || isPrime(s[n-1])) return 0;
        vector<int> dpPrev(n,0), dpCurr(n,0);
        // cnt = 1
        for (int end=0; end<n; ++end) {
            if (!isPrime(s[end]) && end+1 >= minLength) dpCurr[end] = 1;
        }
        if (k==1) return dpCurr[n-1];
        for (int cnt=2; cnt<=k; ++cnt) {
            dpPrev.swap(dpCurr);
            fill(dpCurr.begin(), dpCurr.end(), 0);
            vector<int> pref(n,0);
            // pref[i] = sum_{p=0..i} (s[p+1] is prime ? dpPrev[p] : 0)
            if (n>=2) {
                pref[0] = isPrime(s[1]) ? dpPrev[0] : 0;
                for (int i=1; i<n; ++i) {
                    long long val = pref[i-1];
                    if (i+1 < n && isPrime(s[i+1])) {
                        val += dpPrev[i];
                    }
                    pref[i] = val % MOD;
                }
            }
            for (int end=0; end<n; ++end) {
                if (!isPrime(s[end]) && end - minLength >= 0) {
                    dpCurr[end] = pref[end - minLength];
                }
            }
        }
        return dpCurr[n-1];
    }
};
```

## Java

```java
class Solution {
    public int beautifulPartitions(String s, int k, int minLength) {
        final int MOD = 1_000_000_007;
        int n = s.length();
        if ((long)k * minLength > n) return 0;

        boolean[] startPrime = new boolean[n];
        boolean[] endNonPrime = new boolean[n];
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            boolean prime = c == '2' || c == '3' || c == '5' || c == '7';
            startPrime[i] = prime;
            endNonPrime[i] = !prime;
        }
        if (!startPrime[0] || !endNonPrime[n - 1]) return 0;

        long[] dpPrev = new long[n];
        // cnt = 1
        for (int end = minLength - 1; end < n; end++) {
            if (endNonPrime[end]) dpPrev[end] = 1;
        }

        for (int cnt = 2; cnt <= k; cnt++) {
            long[] pref = new long[n];
            long sum = 0;
            for (int i = 0; i < n; i++) {
                if (startPrime[i]) {
                    long add = (i == 0) ? 0 : dpPrev[i - 1];
                    sum += add;
                    if (sum >= MOD) sum -= MOD;
                }
                pref[i] = sum;
            }

            long[] dpCurr = new long[n];
            for (int end = 0; end < n; end++) {
                if (!endNonPrime[end]) continue;
                int maxStartIdx = end - minLength + 1;
                if (maxStartIdx < 0) continue;
                dpCurr[end] = pref[maxStartIdx];
            }
            dpPrev = dpCurr;
        }

        return (int)(dpPrev[n - 1] % MOD);
    }
}
```

## Python

```python
class Solution(object):
    def beautifulPartitions(self, s, k, minLength):
        """
        :type s: str
        :type k: int
        :type minLength: int
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(s)
        prime = set('2357')
        # first part must start with prime, last part must end with non‑prime
        if s[0] not in prime or s[-1] in prime:
            return 0

        # dp[i][c]: ways to partition prefix ending at i (inclusive) into c parts,
        # where the c-th part ends exactly at i.
        dp = [[0] * (k + 1) for _ in range(n)]

        # initialise first part (c = 1)
        if s[0] in prime:
            for i in range(minLength - 1, n):
                if s[i] not in prime:
                    dp[i][1] = 1

        # transitions for c >= 2
        for cnt in range(2, k + 1):
            # prefix sums of dp[j][cnt-1] where the next part would start at j+1 (prime)
            pref = [0] * n
            cur = 0
            for j in range(n):
                if j + 1 < n and s[j + 1] in prime:
                    cur = (cur + dp[j][cnt - 1]) % MOD
                pref[j] = cur

            for i in range(n):
                if s[i] not in prime:
                    limit = i - minLength
                    if limit >= 0:
                        dp[i][cnt] = pref[limit]

        return dp[n - 1][k] % MOD
```

## Python3

```python
class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = 10**9 + 7
        n = len(s)
        prime = {'2', '3', '5', '7'}
        good_start = [c in prime for c in s]
        good_end = [c not in prime for c in s]

        dp_start = [0] * (n + 1)
        dp_start[0] = 1

        for _ in range(k):
            # prefix sums of dp_start where start position is valid
            pref = [0] * n
            cur = 0
            for i in range(n):
                if good_start[i]:
                    cur = (cur + dp_start[i]) % MOD
                pref[i] = cur

            dp_next = [0] * (n + 1)
            for e in range(n):
                if not good_end[e]:
                    continue
                start_max = e - minLength + 1
                if start_max < 0:
                    continue
                ways = pref[start_max]
                dp_next[e + 1] = (dp_next[e + 1] + ways) % MOD

            dp_start = dp_next

        return dp_start[n] % MOD
```

## C

```c
#include <stddef.h>
#include <string.h>

#define MOD 1000000007

static inline int isPrimeDigit(char c) {
    return c == '2' || c == '3' || c == '5' || c == '7';
}
static inline int isNonPrimeDigit(char c) {
    return !isPrimeDigit(c);
}

int beautifulPartitions(char* s, int k, int minLength) {
    int n = (int)strlen(s);
    if (n < k * minLength) return 0;
    static int dp[1005][1005];
    memset(dp, 0, sizeof(dp));

    /* first part */
    if (isPrimeDigit(s[0])) {
        for (int i = minLength - 1; i < n; ++i) {
            if (isNonPrimeDigit(s[i]))
                dp[1][i] = 1;
        }
    }

    static int pref[1005];
    for (int part = 2; part <= k; ++part) {
        /* build prefix sums of positions where next char is prime */
        for (int i = 0; i < n; ++i) {
            long long add = dp[part - 1][i];
            if (i + 1 < n && isPrimeDigit(s[i + 1])) {
                pref[i] = ((i > 0 ? pref[i - 1] : 0) + add) % MOD;
            } else {
                pref[i] = (i > 0 ? pref[i - 1] : 0);
            }
        }

        for (int i = 0; i < n; ++i) {
            if (!isNonPrimeDigit(s[i])) {
                dp[part][i] = 0;
                continue;
            }
            int limit = i - minLength;
            if (limit >= 0) {
                dp[part][i] = pref[limit];
            } else {
                dp[part][i] = 0;
            }
        }
    }

    return dp[k][n - 1];
}
```

## Csharp

```csharp
public class Solution {
    private const int MOD = 1_000_000_007;
    private bool IsPrime(char c) => c == '2' || c == '3' || c == '5' || c == '7';
    private bool IsNonPrime(char c) => !(c == '2' || c == '3' || c == '5' || c == '7');

    public int BeautifulPartitions(string s, int k, int minLength) {
        int n = s.Length;
        if (!IsPrime(s[0]) || !IsNonPrime(s[n - 1])) return 0;

        int[,] dp = new int[n, k + 1];

        // Initialize for the first part
        for (int i = 0; i < n; i++) {
            if (IsNonPrime(s[i]) && i + 1 >= minLength) {
                dp[i, 1] = 1;
            }
        }

        for (int cnt = 2; cnt <= k; cnt++) {
            long[] prefix = new long[n];
            long sum = 0;
            for (int prev = 0; prev < n; prev++) {
                if (prev + 1 < n && IsPrime(s[prev + 1])) {
                    sum += dp[prev, cnt - 1];
                    if (sum >= MOD) sum -= MOD;
                }
                prefix[prev] = sum;
            }

            for (int i = 0; i < n; i++) {
                if (!IsNonPrime(s[i])) continue;
                int idx = i - minLength;
                if (idx >= 0) {
                    dp[i, cnt] = (int)prefix[idx];
                }
            }
        }

        return dp[n - 1, k];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @param {number} minLength
 * @return {number}
 */
var beautifulPartitions = function(s, k, minLength) {
    const MOD = 1000000007;
    const n = s.length;
    if (minLength * k > n) return 0;

    const primeSet = new Set(['2', '3', '5', '7']);
    const isPrimeStart = Array.from({length: n}, (_, i) => primeSet.has(s[i]));
    const isNonPrimeEnd = Array.from({length: n}, (_, i) => !primeSet.has(s[i]));

    // first and last character constraints
    if (!isPrimeStart[0] || !isNonPrimeEnd[n - 1]) return 0;

    // dp for the first part
    let dpPrev = new Array(n).fill(0);
    for (let i = minLength - 1; i < n; i++) {
        if (isNonPrimeEnd[i]) dpPrev[i] = 1;
    }

    for (let part = 2; part <= k; part++) {
        // prefix sums of dpPrev where the next character starts a prime
        const prefix = new Array(n).fill(0);
        let acc = 0;
        for (let j = 0; j < n; j++) {
            if (j + 1 < n && isPrimeStart[j + 1]) {
                acc += dpPrev[j];
                if (acc >= MOD) acc -= MOD;
            }
            prefix[j] = acc;
        }

        const dpCurr = new Array(n).fill(0);
        for (let i = 0; i < n; i++) {
            if (!isNonPrimeEnd[i]) continue;
            const limitIdx = i - minLength;
            if (limitIdx >= 0) {
                dpCurr[i] = prefix[limitIdx];
            }
        }
        dpPrev = dpCurr;
    }

    return dpPrev[n - 1] % MOD;
};
```

## Typescript

```typescript
function beautifulPartitions(s: string, k: number, minLength: number): number {
    const MOD = 1_000_000_007;
    const n = s.length;

    const isPrimeDigit = (c: string) => c === '2' || c === '3' || c === '5' || c === '7';
    const primeStart = new Array(n).fill(0);
    const nonPrimeEnd = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        if (isPrimeDigit(s[i])) primeStart[i] = 1;
        else nonPrimeEnd[i] = 1; // non‑prime includes '1','4','6','8','9'
    }

    let dpPrev = new Array(n + 1).fill(0);
    dpPrev[0] = 1;

    for (let part = 1; part <= k; part++) {
        const pref = new Array(n).fill(0);
        for (let i = 0; i < n; i++) {
            const add = primeStart[i] ? dpPrev[i] : 0;
            pref[i] = ((i > 0 ? pref[i - 1] : 0) + add) % MOD;
        }

        const dpCurr = new Array(n + 1).fill(0);
        for (let i = 1; i <= n; i++) {
            if (i - minLength >= 0 && nonPrimeEnd[i - 1]) {
                dpCurr[i] = pref[i - minLength];
            }
        }
        dpPrev = dpCurr;
    }

    return dpPrev[n] % MOD;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @param Integer $minLength
     * @return Integer
     */
    function beautifulPartitions($s, $k, $minLength) {
        $mod = 1000000007;
        $n = strlen($s);
        if ($n == 0) return 0;

        // prime digit check for each position
        $prime = array_fill(0, $n, false);
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            $prime[$i] = ($ch === '2' || $ch === '3' || $ch === '5' || $ch === '7');
        }

        // dp[i][j]: ways to partition prefix ending at i into j parts
        $dp = array_fill(0, $n, array_fill(0, $k + 1, 0));

        // First part (j = 1)
        if ($prime[0]) {
            for ($i = $minLength - 1; $i < $n; $i++) {
                if (!$prime[$i]) { // end must be non‑prime
                    $dp[$i][1] = 1;
                }
            }
        }

        // Subsequent parts
        for ($j = 2; $j <= $k; $j++) {
            // prefix sums of dp[*][j-1] where the next character is prime
            $prefix = array_fill(0, $n, 0);
            $cum = 0;
            for ($p = 0; $p < $n; $p++) {
                if ($p + 1 < $n && $prime[$p + 1]) {
                    $cum += $dp[$p][$j - 1];
                    if ($cum >= $mod) $cum -= $mod;
                }
                $prefix[$p] = $cum;
            }

            for ($i = $minLength; $i < $n; $i++) {
                if (!$prime[$i]) { // current part must end with non‑prime
                    $idx = $i - $minLength;
                    $dp[$i][$j] = $prefix[$idx];
                }
            }
        }

        // The whole string must end with a non‑prime digit
        if ($prime[$n - 1]) return 0;
        return $dp[$n - 1][$k] % $mod;
    }
}
```

## Swift

```swift
class Solution {
    func beautifulPartitions(_ s: String, _ k: Int, _ minLength: Int) -> Int {
        let MOD = 1_000_000_007
        let chars = Array(s)
        let n = chars.count
        if n == 0 { return 0 }
        
        var isPrime = [Bool](repeating: false, count: n)
        for i in 0..<n {
            let c = chars[i]
            if c == "2" || c == "3" || c == "5" || c == "7" {
                isPrime[i] = true
            }
        }
        
        // The first character must be prime to start the first partition.
        if !isPrime[0] { return 0 }
        
        var dpPrev = [Int](repeating: 0, count: n)
        // Initialize for one partition.
        if minLength <= n {
            for i in (minLength - 1)..<n {
                if !isPrime[i] {   // end must be non‑prime
                    dpPrev[i] = 1
                }
            }
        }
        
        if k == 1 {
            return dpPrev[n - 1]
        }
        
        var part = 2
        while part <= k {
            var pref = [Int](repeating: 0, count: n)
            var running = 0
            for p in 0..<n {
                if p + 1 < n && isPrime[p + 1] {
                    running += dpPrev[p]
                    if running >= MOD { running -= MOD }
                }
                pref[p] = running
            }
            
            var dpCurr = [Int](repeating: 0, count: n)
            for i in 0..<n {
                if isPrime[i] { continue } // end must be non‑prime
                let maxP = i - minLength
                if maxP >= 0 {
                    dpCurr[i] = pref[maxP]
                }
            }
            
            dpPrev = dpCurr
            part += 1
        }
        
        return dpPrev[n - 1]
    }
}
```

## Kotlin

```kotlin
import java.util.*

class Solution {
    private val MOD = 1_000_000_007L
    private fun isPrime(c: Char): Boolean = c == '2' || c == '3' || c == '5' || c == '7'

    fun beautifulPartitions(s: String, k: Int, minLength: Int): Int {
        val n = s.length
        if (k * minLength > n) return 0
        // dpPrev holds DP for j-1 parts, dpCurr for current j parts
        var dpPrev = LongArray(n) { 0L }

        // Initialize for j = 1 (first part)
        val firstPrime = isPrime(s[0])
        if (firstPrime) {
            for (i in minLength - 1 until n) {
                if (!isPrime(s[i])) {
                    dpPrev[i] = 1L
                }
            }
        }

        if (k == 1) {
            return (dpPrev[n - 1] % MOD).toInt()
        }

        // Iterate for parts 2..k
        for (part in 2..k) {
            val dpCurr = LongArray(n) { 0L }
            // Build prefix sums of contributions where a part could start
            val prefix = LongArray(n)
            var running = 0L
            for (i in 0 until n) {
                if (isPrime(s[i])) {
                    val add = if (i == 0) 0L else dpPrev[i - 1]
                    running += add
                    if (running >= MOD) running -= MOD
                }
                prefix[i] = running
            }

            for (end in 0 until n) {
                if (!isPrime(s[end])) { // end must be non‑prime
                    val limit = end - minLength + 1
                    if (limit >= 0) {
                        dpCurr[end] = prefix[limit]
                    }
                }
            }

            dpPrev = dpCurr
        }

        return (dpPrev[n - 1] % MOD).toInt()
    }
}
```

## Dart

```dart
class Solution {
  static const int _mod = 1000000007;

  bool _isPrimeDigit(String ch) {
    return ch == '2' || ch == '3' || ch == '5' || ch == '7';
  }

  int beautifulPartitions(String s, int k, int minLength) {
    int n = s.length;
    List<int> dpPrev = List.filled(n, 0);

    for (int part = 1; part <= k; ++part) {
      List<int> dpCurr = List.filled(n, 0);
      int cum = 0;

      // base contribution for the first part when it starts at index 0
      if (part == 1 && _isPrimeDigit(s[0])) {
        cum = 1;
      }

      for (int i = minLength - 1; i < n; ++i) {
        int p = i - minLength;
        if (p >= 0 && _isPrimeDigit(s[p + 1])) {
          cum += dpPrev[p];
          if (cum >= _mod) cum -= _mod;
        }
        if (!_isPrimeDigit(s[i])) {
          dpCurr[i] = cum;
        }
      }

      dpPrev = dpCurr;
    }

    return dpPrev[n - 1] % _mod;
  }
}
```

## Golang

```go
func beautifulPartitions(s string, k int, minLength int) int {
	const MOD int64 = 1000000007
	n := len(s)
	if n == 0 {
		return 0
	}
	isPrime := func(c byte) bool { return c == '2' || c == '3' || c == '5' || c == '7' }

	goodStart := make([]bool, n) // prime digit
	goodEnd := make([]bool, n)   // non‑prime digit
	for i := 0; i < n; i++ {
		if isPrime(s[i]) {
			goodStart[i] = true
		} else {
			goodEnd[i] = true
		}
	}

	// first segment must start with prime, last must end with non‑prime
	if !goodStart[0] || !goodEnd[n-1] {
		return 0
	}

	// dpPrev[i]: ways to partition prefix ending at i into current number of segments
	dpPrev := make([]int64, n)
	for i := 0; i < n; i++ {
		if goodEnd[i] && i+1 >= minLength {
			dpPrev[i] = 1
		}
	}

	for cnt := 2; cnt <= k; cnt++ {
		pref := make([]int64, n)
		var sum int64 = 0
		for p := 0; p < n; p++ {
			if p+1 < n && goodStart[p+1] {
				sum += dpPrev[p]
				if sum >= MOD {
					sum -= MOD
				}
			}
			pref[p] = sum
		}

		dpCurr := make([]int64, n)
		for i := 0; i < n; i++ {
			if !goodEnd[i] {
				continue
			}
			limit := i - minLength
			if limit >= 0 {
				dpCurr[i] = pref[limit]
			}
		}
		dpPrev = dpCurr
	}

	return int(dpPrev[n-1] % MOD)
}
```

## Ruby

```ruby
def beautiful_partitions(s, k, min_length)
  mod = 1_000_000_007
  n = s.length
  prime = {'2'=>true,'3'=>true,'5'=>true,'7'=>true}
  return 0 unless prime[s[0]]
  return 0 if prime[s[-1]] # last char must be non‑prime

  dp = Array.new(k + 1) { Array.new(n, 0) }

  # j = 1 (first segment starts at index 0)
  ((min_length - 1)...n).each do |i|
    dp[1][i] = 1 unless prime[s[i]]
  end

  (2..k).each do |j|
    pref = Array.new(n, 0)
    sum = 0
    (0...n).each do |idx|
      if prime[s[idx]]
        val = idx - 1 >= 0 ? dp[j - 1][idx - 1] : 0
        sum += val
        sum -= mod if sum >= mod
      end
      pref[idx] = sum
    end

    (0...n).each do |i|
      next if prime[s[i]] # end must be non‑prime
      limit = i - min_length + 1
      dp[j][i] = pref[limit] if limit >= 0
    end
  end

  dp[k][n - 1] % mod
end
```

## Scala

```scala
object Solution {
    def beautifulPartitions(s: String, k: Int, minLength: Int): Int = {
        val MOD = 1000000007L
        val n = s.length
        if (k * minLength > n) return 0

        def isPrime(c: Char): Boolean = c == '2' || c == '3' || c == '5' || c == '7'

        val prime = Array.ofDim[Boolean](n)
        val nonPrime = Array.ofDim[Boolean](n)
        var i = 0
        while (i < n) {
            prime(i) = isPrime(s.charAt(i))
            nonPrime(i) = !prime(i)
            i += 1
        }

        if (!prime(0)) return 0

        val dp = Array.ofDim[Long](n, k + 1)

        // base case for first part
        var idx = minLength - 1
        while (idx < n) {
            if (nonPrime(idx)) dp(idx)(1) = 1L
            idx += 1
        }

        var cnt = 2
        while (cnt <= k) {
            val pref = new Array[Long](n)
            var sum = 0L
            var p = 0
            while (p < n) {
                if (p + 1 < n && prime(p + 1)) {
                    sum += dp(p)(cnt - 1)
                    if (sum >= MOD) sum -= MOD
                }
                pref(p) = sum
                p += 1
            }

            var j = 0
            while (j < n) {
                if (nonPrime(j)) {
                    val limit = j - minLength
                    if (limit >= 0) dp(j)(cnt) = pref(limit)
                }
                j += 1
            }
            cnt += 1
        }

        (dp(n - 1)(k) % MOD).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn beautiful_partitions(s: String, k: i32, min_length: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = s.len();
        let chars: Vec<char> = s.chars().collect();
        let mut is_prime = vec![false; n];
        for i in 0..n {
            is_prime[i] = matches!(chars[i], '2' | '3' | '5' | '7');
        }
        if !is_prime[0] {
            return 0;
        }
        let k_usize = k as usize;
        let min_len = min_length as usize;

        // dp[pos][cnt]: ways to partition prefix ending at pos into cnt parts
        let mut dp = vec![vec![0i64; k_usize + 1]; n];

        // Base case: first part only
        for pos in (min_len - 1)..n {
            if !is_prime[pos] {
                dp[pos][1] = 1;
            }
        }

        for cnt in 2..=k_usize {
            let mut pref = vec![0i64; n];
            for i in 0..n {
                let add = if i + 1 < n && is_prime[i + 1] { dp[i][cnt - 1] } else { 0 };
                pref[i] = (if i > 0 { pref[i - 1] } else { 0 } + add) % MOD;
            }
            for pos in min_len..n {
                if !is_prime[pos] {
                    let idx = pos - min_len;
                    dp[pos][cnt] = pref[idx];
                }
            }
        }

        (dp[n - 1][k_usize] % MOD) as i32
    }
}
```

## Racket

```racket
(define (beautiful-partitions s k minLength)
  (let* ((MOD 1000000007)
         (n (string-length s))
         (prime?
          (lambda (ch)
            (or (char=? ch #\2) (char=? ch #\3) (char=? ch #\5) (char=? ch #\7))))
         (first-prime (prime? (string-ref s 0))))
    (if (not first-prime)
        0
        (let loop ((t 1) (dpPrev (make-vector n 0)))
          (if (> t k)
              (vector-ref dpPrev (- n 1))
              (begin
                ;; prefix sums of contributions from possible start positions
                (define pref (make-vector n 0))
                (define sum 0)
                (for ([pos (in-range n)])
                  (when (prime? (string-ref s pos))
                    (let ((add (if (= pos 0)
                                   (if (= t 1) 1 0)
                                   (vector-ref dpPrev (- pos 1)))))
                      (set! sum (modulo (+ sum add) MOD))))
                  (vector-set! pref pos sum))
                ;; compute dp for current part endings
                (define dpCurr (make-vector n 0))
                (for ([i (in-range n)])
                  (when (not (prime? (string-ref s i)))
                    (let ((limit (- i (- minLength 1)))) ; i - minLength + 1
                      (when (>= limit 0)
                        (vector-set! dpCurr i (vector-ref pref limit))))))
                (loop (+ t 1) dpCurr)))))))
```

## Erlang

```erlang
-define(MOD, 1000000007).

-spec beautiful_partitions(S :: unicode:unicode_binary(), K :: integer(), MinLength :: integer()) -> integer().
beautiful_partitions(S, K, MinLength) ->
    Digits = [C - $0 || C <- binary_to_list(S)],
    N = length(Digits),
    if
        K * MinLength > N -> 0;
        true ->
            DigitsTuple = list_to_tuple(Digits),
            DP0 = lists:duplicate(N, 0),
            FinalDP = iterate_parts(1, DP0, Digits, DigitsTuple, K, MinLength, N),
            element(N, list_to_tuple(FinalDP))
    end.

iterate_parts(Part, _DPPrev, _DigitsList, _DigitsTuple, K, _MinLen, N) when Part > K ->
    _DPPrev;
iterate_parts(Part, DPPrev, DigitsList, DigitsTuple, K, MinLen, N) ->
    Base = case Part of
               1 ->
                   case hd(DigitsList) of
                       D0 when is_prime(D0) -> 1;
                       _ -> 0
                   end;
               _ -> 0
           end,
    PrefList = build_pref(DigitsList, DPPrev, Base),
    PrefTuple = list_to_tuple(PrefList),
    DPcurr = build_dp_curr(0, N, MinLen, DigitsTuple, PrefTuple, []),
    iterate_parts(Part + 1, DPcurr, DigitsList, DigitsTuple, K, MinLen, N).

build_pref(Digits, DPPrev, Base) ->
    build_pref(Digits, DPPrev, Base, 0, undefined).

build_pref([], [], _Base, _Acc, _PrevDP) -> [];
build_pref([D|Ds], [Dp|Dps], Base, Acc, PrevDP) ->
    Contrib = if
                  is_prime(D) ->
                      case PrevDP of
                          undefined -> Base;
                          _ -> PrevDP
                      end;
                  true -> 0
              end,
    NewAcc = (Acc + Contrib) rem ?MOD,
    Rest = build_pref(Ds, Dps, Base, NewAcc, Dp),
    [NewAcc | Rest].

build_dp_curr(I, N, _MinLen, _DigitsT, _PrefT, Acc) when I == N ->
    lists:reverse(Acc);
build_dp_curr(I, N, MinLen, DigitsT, PrefT, Acc) ->
    Digit = element(I + 1, DigitsT),
    Val = if
              not is_prime(Digit), I - MinLen >= 0 ->
                  element(I - MinLen + 1, PrefT);
              true -> 0
          end,
    build_dp_curr(I + 1, N, MinLen, DigitsT, PrefT, [Val | Acc]).

is_prime(2) -> true;
is_prime(3) -> true;
is_prime(5) -> true;
is_prime(7) -> true;
is_prime(_) -> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec beautiful_partitions(s :: String.t(), k :: integer(), min_length :: integer()) :: integer()
  def beautiful_partitions(s, k, min_length) do
    mod = 1_000_000_007
    chars = String.graphemes(s)
    n = length(chars)

    prime_digit = fn ch -> ch in ["2", "3", "5", "7"] end

    dp_rows = for _ <- 0..k, do: :array.new(n, default: 0)
    total_rows = for _ <- 0..k, do: :array.new(n, default: 0)
    pref_rows = for _ <- 0..k, do: :array.new(n, default: 0)

    {final_dp, _, _} =
      Enum.reduce(0..(n - 1), {dp_rows, total_rows, pref_rows}, fn i,
                                                                   {dp_acc, tot_acc, pre_acc} ->
        is_end_non_prime = not prime_digit.(Enum.at(chars, i))
        max_start = i - min_length + 1

        dp_updated =
          if is_end_non_prime and max_start >= 0 do
            Enum.reduce(1..k, dp_acc, fn c, dp_cur ->
              val =
                if c == 1 do
                  if prime_digit.(Enum.at(chars, 0)), do: 1, else: 0
                else
                  :array.get(max_start, pre_acc[c - 1])
                end

              List.update_at(dp_cur, c, fn arr -> :array.set(i, val, arr) end)
            end)
          else
            dp_acc
          end

        {tot_updated, pre_updated} =
          Enum.reduce(0..k, {tot_acc, pre_acc}, fn c,
                                                  {t_cur, p_cur} ->
            prev_total = if i == 0, do: 0, else: :array.get(i - 1, t_cur)
            dp_val = :array.get(i, List.at(dp_updated, c))
            new_total = rem(prev_total + dp_val, mod)

            t_new = List.update_at(t_cur, c, fn arr -> :array.set(i, new_total, arr) end)

            prev_pref = if i == 0, do: 0, else: :array.get(i - 1, p_cur)

            add =
              if prime_digit.(Enum.at(chars, i)) do
                prev_total
              else
                0
              end

            new_pref = rem(prev_pref + add, mod)
            p_new = List.update_at(p_cur, c, fn arr -> :array.set(i, new_pref, arr) end)

            {t_new, p_new}
          end)

        {dp_updated, tot_updated, pre_updated}
      end)

    if n == 0 do
      0
    else
      :array.get(n - 1, List.at(final_dp, k))
    end
  end
end
```
