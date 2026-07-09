# 2081. Sum of k-Mirror Numbers

## Cpp

```cpp
class Solution {
public:
    bool isKPalindrome(long long x, int k) {
        vector<int> digits;
        while (x > 0) {
            digits.push_back(x % k);
            x /= k;
        }
        int i = 0, j = (int)digits.size() - 1;
        while (i < j) {
            if (digits[i] != digits[j]) return false;
            ++i; --j;
        }
        return true;
    }

    long long makePal(long long prefix, bool odd) {
        string s = to_string(prefix);
        string rev = s;
        reverse(rev.begin(), rev.end());
        if (odd) rev.erase(0, 1); // remove the middle digit duplicate
        return stoll(s + rev);
    }

    long long kMirror(int k, int n) {
        long long sum = 0;
        int cnt = 0;
        for (int len = 1; ; ++len) {
            bool odd = (len % 2 == 1);
            int halfLen = (len + 1) / 2;
            long long start = 1;
            for (int i = 1; i < halfLen; ++i) start *= 10; // 10^{halfLen-1}
            long long end = start * 10 - 1;               // 10^{halfLen}-1
            for (long long prefix = start; prefix <= end; ++prefix) {
                long long pal = makePal(prefix, odd);
                if (isKPalindrome(pal, k)) {
                    sum += pal;
                    ++cnt;
                    if (cnt == n) return sum;
                }
            }
        }
        return sum; // unreachable
    }
};
```

## Java

```java
class Solution {
    public long kMirror(int k, int n) {
        long sum = 0;
        int count = 0;
        for (int len = 1; ; len++) {
            int start = (len == 1) ? 1 : (int)Math.pow(10, len - 1);
            int end = (int)Math.pow(10, len) - 1;

            // odd length palindromes
            for (int half = start; half <= end; half++) {
                long pal = makeOdd(half);
                if (isKPalindrome(pal, k)) {
                    sum += pal;
                    count++;
                    if (count == n) return sum;
                }
            }

            // even length palindromes
            for (int half = start; half <= end; half++) {
                long pal = makeEven(half);
                if (isKPalindrome(pal, k)) {
                    sum += pal;
                    count++;
                    if (count == n) return sum;
                }
            }
        }
    }

    private long makeOdd(int half) {
        String s = Integer.toString(half);
        String rev = new StringBuilder(s.substring(0, s.length() - 1)).reverse().toString();
        return Long.parseLong(s + rev);
    }

    private long makeEven(int half) {
        String s = Integer.toString(half);
        String rev = new StringBuilder(s).reverse().toString();
        return Long.parseLong(s + rev);
    }

    private boolean isKPalindrome(long num, int k) {
        if (num == 0) return true;
        long x = num;
        char[] buf = new char[64];
        int idx = 0;
        while (x > 0) {
            int digit = (int)(x % k);
            buf[idx++] = (char)('0' + digit);
            x /= k;
        }
        for (int i = 0; i < idx / 2; i++) {
            if (buf[i] != buf[idx - 1 - i]) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def kMirror(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        def is_pal_base(x):
            digs = []
            while x:
                digs.append(x % k)
                x //= k
            return digs == digs[::-1]

        total = 0
        count = 0
        half_len = 1
        while True:
            start = 10 ** (half_len - 1)
            end = 10 ** half_len
            for i in range(start, end):
                s = str(i)
                # odd length palindrome
                p_odd = int(s + s[-2::-1])
                if is_pal_base(p_odd):
                    total += p_odd
                    count += 1
                    if count == n:
                        return total
                # even length palindrome
                p_even = int(s + s[::-1])
                if is_pal_base(p_even):
                    total += p_even
                    count += 1
                    if count == n:
                        return total
            half_len += 1
```

## Python3

```python
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_pal_base(num: int) -> bool:
            digits = []
            while num:
                digits.append(num % k)
                num //= k
            return digits == digits[::-1]

        total = 0
        count = 0
        i = 1
        while count < n:
            s = str(i)

            # odd length palindrome
            odd = int(s + s[-2::-1])
            if is_pal_base(odd):
                total += odd
                count += 1
                if count == n:
                    break

            # even length palindrome
            even = int(s + s[::-1])
            if count < n and is_pal_base(even):
                total += even
                count += 1
                if count == n:
                    break

            i += 1

        return total
```

## C

```c
#include <stdio.h>

static long long makePalindrome(long long prefix, int odd) {
    long long res = prefix;
    long long x = odd ? prefix / 10 : prefix;
    while (x > 0) {
        res = res * 10 + (x % 10);
        x /= 10;
    }
    return res;
}

static int isKMirrorNum(long long num, int base) {
    int digits[64];
    int len = 0;
    while (num > 0) {
        digits[len++] = num % base;
        num /= base;
    }
    for (int i = 0; i < len / 2; ++i)
        if (digits[i] != digits[len - 1 - i])
            return 0;
    return 1;
}

static long long pow10_int(int exp) {
    static long long pows[20] = {0};
    if (pows[0] == 0) {
        pows[0] = 1;
        for (int i = 1; i < 20; ++i)
            pows[i] = pows[i - 1] * 10LL;
    }
    return pows[exp];
}

long long kMirror(int k, int n) {
    long long sum = 0;
    int cnt = 0;
    int len = 1;
    while (cnt < n) {
        if (len % 2 == 1) { // odd length
            int half = (len + 1) / 2;
            long long start = pow10_int(half - 1);
            long long end   = pow10_int(half);
            for (long long prefix = start; prefix < end && cnt < n; ++prefix) {
                long long pal = makePalindrome(prefix, 1);
                if (isKMirrorNum(pal, k)) {
                    sum += pal;
                    ++cnt;
                }
            }
        } else { // even length
            int half = len / 2;
            long long start = pow10_int(half - 1);
            long long end   = pow10_int(half);
            for (long long prefix = start; prefix < end && cnt < n; ++prefix) {
                long long pal = makePalindrome(prefix, 0);
                if (isKMirrorNum(pal, k)) {
                    sum += pal;
                    ++cnt;
                }
            }
        }
        ++len;
    }
    return sum;
}
```

## Csharp

```csharp
public class Solution
{
    public long KMirror(int k, int n)
    {
        long sum = 0;
        int found = 0;

        for (int len = 1; ; len++)
        {
            bool odd = (len % 2 == 1);
            int halfLen = (len + 1) / 2;

            long start = 1;
            for (int i = 1; i < halfLen; i++) start *= 10;
            long end = start * 10 - 1;

            for (long prefix = start; prefix <= end; prefix++)
            {
                long pal = BuildPalindrome(prefix, odd);
                if (IsKPalindrome(pal, k))
                {
                    sum += pal;
                    found++;
                    if (found == n) return sum;
                }
            }
        }
    }

    private long BuildPalindrome(long prefix, bool odd)
    {
        long result = prefix;
        long x = odd ? prefix / 10 : prefix;
        while (x > 0)
        {
            result = result * 10 + (x % 10);
            x /= 10;
        }
        return result;
    }

    private bool IsKPalindrome(long num, int k)
    {
        var digits = new System.Collections.Generic.List<int>();
        long x = num;
        while (x > 0)
        {
            digits.Add((int)(x % k));
            x /= k;
        }
        int i = 0, j = digits.Count - 1;
        while (i < j)
        {
            if (digits[i] != digits[j]) return false;
            i++;
            j--;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} k
 * @param {number} n
 * @return {number}
 */
var kMirror = function(k, n) {
    let count = 0;
    let sum = 0;
    for (let len = 1; ; ++len) {
        const odd = len % 2 === 1;
        const halfLen = Math.floor((len + 1) / 2);
        let start = Math.pow(10, halfLen - 1);
        if (halfLen === 1) start = 1;
        const end = Math.pow(10, halfLen) - 1;
        for (let prefix = start; prefix <= end && count < n; ++prefix) {
            const pal = buildPalindrome(prefix, odd);
            if (isKPalindrome(pal, k)) {
                sum += pal;
                ++count;
                if (count === n) return sum;
            }
        }
    }
};

function buildPalindrome(prefix, odd) {
    const s = prefix.toString();
    let rev = s.split('').reverse().join('');
    if (odd) rev = rev.slice(1);
    return Number(s + rev);
}

function isKPalindrome(num, k) {
    const digits = [];
    while (num > 0) {
        digits.push(num % k);
        num = Math.floor(num / k);
    }
    for (let i = 0, j = digits.length - 1; i < j; ++i, --j) {
        if (digits[i] !== digits[j]) return false;
    }
    return true;
}
```

## Typescript

```typescript
function kMirror(k: number, n: number): number {
    const isPalindromeBase = (num: number, base: number): boolean => {
        const s = num.toString(base);
        let i = 0, j = s.length - 1;
        while (i < j) {
            if (s[i] !== s[j]) return false;
            i++;
            j--;
        }
        return true;
    };

    const makePalindrome = (prefix: number, odd: boolean): number => {
        const s = prefix.toString();
        const rev = s.split('').reverse().join('');
        const palStr = odd ? s + rev.slice(1) : s + rev;
        return Number(palStr);
    };

    let count = 0;
    let sum = 0;

    for (let len = 1; ; len++) {
        const odd = len % 2 === 1;
        const half = odd ? Math.floor((len + 1) / 2) : len / 2;
        let start = Math.pow(10, half - 1);
        if (half === 1) start = 1;
        const end = Math.pow(10, half) - 1;

        for (let prefix = start; prefix <= end; prefix++) {
            const pal = makePalindrome(prefix, odd);
            if (isPalindromeBase(pal, k)) {
                sum += pal;
                count++;
                if (count === n) return sum;
            }
        }
    }
}
```

## Php

```php
class Solution {
    /**
     * @param Integer $k
     * @param Integer $n
     * @return Integer
     */
    function kMirror($k, $n) {
        $found = 0;
        $sum = 0;
        for ($len = 1; ; $len++) {
            $halfLen = intdiv($len + 1, 2); // ceil(len/2)
            $start = ($halfLen == 1) ? 1 : (int)pow(10, $halfLen - 1);
            $end   = (int)pow(10, $halfLen) - 1;
            for ($prefix = $start; $prefix <= $end; $prefix++) {
                if ($len % 2 == 1) {
                    $pal = $this->buildPalindrome($prefix, true);
                } else {
                    $pal = $this->buildPalindrome($prefix, false);
                }
                if ($this->isKPalindrome($pal, $k)) {
                    $sum += $pal;
                    $found++;
                    if ($found == $n) {
                        return $sum;
                    }
                }
            }
        }
    }

    private function buildPalindrome(int $prefix, bool $odd): int {
        $s = strval($prefix);
        if ($odd) {
            $rev = strrev(substr($s, 0, -1));
        } else {
            $rev = strrev($s);
        }
        return intval($s . $rev);
    }

    private function isKPalindrome(int $num, int $base): bool {
        $digits = [];
        while ($num > 0) {
            $digits[] = $num % $base;
            $num = intdiv($num, $base);
        }
        $i = 0;
        $j = count($digits) - 1;
        while ($i < $j) {
            if ($digits[$i] !== $digits[$j]) {
                return false;
            }
            $i++;
            $j--;
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func kMirror(_ k: Int, _ n: Int) -> Int {
        var count = 0
        var sum: Int64 = 0
        var cur = 1
        while count < n {
            let oddPal = makePalindrome(cur, true)
            if isKMirror(oddPal, k) {
                sum += oddPal
                count += 1
                if count == n { break }
            }
            let evenPal = makePalindrome(cur, false)
            if isKMirror(evenPal, k) {
                sum += evenPal
                count += 1
                if count == n { break }
            }
            cur += 1
        }
        return Int(sum)
    }

    private func makePalindrome(_ x: Int, _ odd: Bool) -> Int64 {
        var res: Int64 = Int64(x)
        var y = odd ? x / 10 : x
        while y > 0 {
            res = res * 10 + Int64(y % 10)
            y /= 10
        }
        return res
    }

    private func isKMirror(_ num: Int64, _ base: Int) -> Bool {
        var digits: [Int] = []
        var x = num
        while x > 0 {
            digits.append(Int(x % Int64(base)))
            x /= Int64(base)
        }
        var i = 0
        var j = digits.count - 1
        while i < j {
            if digits[i] != digits[j] { return false }
            i += 1
            j -= 1
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun kMirror(k: Int, n: Int): Long {
        val candidates = mutableListOf<Long>()
        var prefix = 1
        // Upper bound sufficient for the constraints (n <= 30)
        val LIMIT = 1_000_000
        while (prefix <= LIMIT) {
            val odd = makeOdd(prefix)
            if (isKPalindrome(odd, k)) candidates.add(odd)
            val even = makeEven(prefix)
            if (isKPalindrome(even, k)) candidates.add(even)
            prefix++
        }
        candidates.sort()
        var sum = 0L
        for (i in 0 until n) {
            sum += candidates[i]
        }
        return sum
    }

    private fun makeOdd(x: Int): Long {
        var res = x.toLong()
        var y = x / 10
        while (y > 0) {
            res = res * 10 + (y % 10)
            y /= 10
        }
        return res
    }

    private fun makeEven(x: Int): Long {
        var res = x.toLong()
        var y = x
        while (y > 0) {
            res = res * 10 + (y % 10)
            y /= 10
        }
        return res
    }

    private fun isKPalindrome(num: Long, k: Int): Boolean {
        var x = num
        val digits = IntArray(64)
        var len = 0
        while (x > 0) {
            digits[len++] = (x % k).toInt()
            x /= k
        }
        for (i in 0 until len / 2) {
            if (digits[i] != digits[len - 1 - i]) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  int kMirror(int k, int n) {
    int count = 0;
    int sum = 0;
    for (int i = 1;; i++) {
      int oddPal = _makePalindrome(i, true);
      if (_isKMirror(oddPal, k)) {
        sum += oddPal;
        if (++count == n) return sum;
      }
      int evenPal = _makePalindrome(i, false);
      if (_isKMirror(evenPal, k)) {
        sum += evenPal;
        if (++count == n) return sum;
      }
    }
  }

  int _makePalindrome(int x, bool odd) {
    String s = x.toString();
    String rev = s.split('').reversed.join('');
    if (odd) rev = rev.substring(1);
    return int.parse(s + rev);
  }

  bool _isKMirror(int num, int k) {
    List<int> digits = [];
    int t = num;
    while (t > 0) {
      digits.add(t % k);
      t ~/= k;
    }
    for (int i = 0, j = digits.length - 1; i < j; ++i, --j) {
      if (digits[i] != digits[j]) return false;
    }
    return true;
  }
}
```

## Golang

```go
import (
	"strconv"
)

func kMirror(k int, n int) int64 {
	var sum int64
	count := 0

	pow10 := func(exp int) int64 {
		var res int64 = 1
		for i := 0; i < exp; i++ {
			res *= 10
		}
		return res
	}

	reverseStr := func(s string) string {
		b := []byte(s)
		i, j := 0, len(b)-1
		for i < j {
			b[i], b[j] = b[j], b[i]
			i++
			j--
		}
		return string(b)
	}

	makePal := func(prefix int64, odd bool) int64 {
		s := strconv.FormatInt(prefix, 10)
		rev := reverseStr(s)
		var palStr string
		if odd {
			palStr = s + rev[1:]
		} else {
			palStr = s + rev
		}
		val, _ := strconv.ParseInt(palStr, 10, 64)
		return val
	}

	isKPal := func(num int64) bool {
		if num == 0 {
			return true
		}
		var digits []int
		for num > 0 {
			digits = append(digits, int(num%int64(k)))
			num /= int64(k)
		}
		i, j := 0, len(digits)-1
		for i < j {
			if digits[i] != digits[j] {
				return false
			}
			i++
			j--
		}
		return true
	}

outer:
	for length := 1; ; length++ {
		odd := length%2 == 1
		var half int
		if odd {
			half = (length + 1) / 2
		} else {
			half = length / 2
		}
		start := pow10(half - 1)
		end := pow10(half) - 1
		for prefix := start; prefix <= end; prefix++ {
			pal := makePal(prefix, odd)
			if isKPal(pal) {
				sum += pal
				count++
				if count == n {
					break outer
				}
			}
		}
	}

	return sum
}
```

## Ruby

```ruby
def k_mirror(k, n)
  is_k_pal = lambda do |num|
    digits = []
    x = num
    while x > 0
      digits << (x % k)
      x /= k
    end
    i = 0
    j = digits.length - 1
    while i < j
      return false if digits[i] != digits[j]
      i += 1
      j -= 1
    end
    true
  end

  make_pal = lambda do |prefix, odd|
    s = prefix.to_s
    if odd
      tail = s[0...-1].reverse
      (s + tail).to_i
    else
      (s + s.reverse).to_i
    end
  end

  count = 0
  sum = 0
  len = 1
  while count < n
    start = (len == 1) ? 1 : 10**(len - 1)
    finish = 10**len - 1
    prefix = start
    while prefix <= finish && count < n
      pal = make_pal.call(prefix, true)
      if is_k_pal.call(pal)
        sum += pal
        count += 1
        break if count == n
      end

      pal = make_pal.call(prefix, false)
      if is_k_pal.call(pal)
        sum += pal
        count += 1
        break if count == n
      end

      prefix += 1
    end
    len += 1
  end
  sum
end
```

## Scala

```scala
object Solution {
  def kMirror(k: Int, n: Int): Long = {
    var count = 0
    var sum: Long = 0L
    var len = 1

    def intPow10(exp: Int): Int = {
      var res = 1
      var i = 0
      while (i < exp) {
        res *= 10
        i += 1
      }
      res
    }

    def buildOdd(prefix: Int): Long = {
      var left: Long = prefix.toLong
      var right = prefix / 10
      while (right > 0) {
        left = left * 10 + (right % 10)
        right /= 10
      }
      left
    }

    def buildEven(prefix: Int): Long = {
      var left: Long = prefix.toLong
      var right = prefix
      while (right > 0) {
        left = left * 10 + (right % 10)
        right /= 10
      }
      left
    }

    def isKPalindrome(num: Long, base: Int): Boolean = {
      var x = num
      val sb = new StringBuilder
      while (x > 0) {
        sb.append((x % base).toInt)
        x /= base
      }
      val l = sb.length()
      var i = 0
      while (i < l / 2) {
        if (sb.charAt(i) != sb.charAt(l - 1 - i)) return false
        i += 1
      }
      true
    }

    while (count < n) {
      if ((len & 1) == 0) { // even length
        val half = len / 2
        val start = intPow10(half - 1)
        val end = intPow10(half) - 1
        var prefix = start
        while (prefix <= end && count < n) {
          val pal = buildEven(prefix)
          if (isKPalindrome(pal, k)) {
            sum += pal
            count += 1
          }
          prefix += 1
        }
      } else { // odd length
        val half = (len + 1) / 2
        val start = intPow10(half - 1)
        val end = intPow10(half) - 1
        var prefix = start
        while (prefix <= end && count < n) {
          val pal = buildOdd(prefix)
          if (isKPalindrome(pal, k)) {
            sum += pal
            count += 1
          }
          prefix += 1
        }
      }
      len += 1
    }

    sum
  }
}
```

## Rust

```rust
impl Solution {
    pub fn k_mirror(k: i32, n: i32) -> i64 {
        fn make_pal(prefix: i64, odd: bool) -> i64 {
            let s = prefix.to_string();
            let rev_part: String = if odd && s.len() > 1 {
                s[..s.len() - 1].chars().rev().collect()
            } else if odd && s.len() == 1 {
                String::new()
            } else {
                s.chars().rev().collect()
            };
            let pal_str = format!("{}{}", s, rev_part);
            pal_str.parse::<i64>().unwrap()
        }

        fn is_pal_in_base(mut x: i64, k: i32) -> bool {
            let base = k as i64;
            let mut digits = Vec::new();
            while x > 0 {
                digits.push((x % base) as i32);
                x /= base;
            }
            let len = digits.len();
            for i in 0..len / 2 {
                if digits[i] != digits[len - 1 - i] {
                    return false;
                }
            }
            true
        }

        let mut count = 0i32;
        let mut sum: i64 = 0;
        let mut len = 1usize; // length of palindrome in decimal

        while count < n {
            let odd = len % 2 == 1;
            let half_len = (len + 1) / 2;
            let start: i64 = if half_len == 1 { 1 } else { 10i64.pow((half_len - 1) as u32) };
            let end: i64 = 10i64.pow(half_len as u32) - 1;

            for prefix in start..=end {
                let pal = make_pal(prefix, odd);
                if is_pal_in_base(pal, k) {
                    sum += pal;
                    count += 1;
                    if count == n {
                        break;
                    }
                }
            }

            len += 1;
        }

        sum
    }
}
```

## Racket

```racket
(require racket/string)

(define (make-odd prefix)
  (let* ([s (number->string prefix)]
         [len (string-length s)]
         [prefix-part (if (> len 1) (substring s 0 (- len 1)) "")]
         [rev (string-reverse prefix-part)])
    (string->number (string-append s rev))))

(define (make-even prefix)
  (let* ([s (number->string prefix)]
         [rev (string-reverse s)])
    (string->number (string-append s rev))))

(define (pal? num base)
  (let loop ([n num] [digits '()])
    (if (= n 0)
        (equal? digits (reverse digits))
        (loop (quotient n base) (cons (remainder n base) digits)))))

(define/contract (k-mirror k n)
  (-> exact-integer? exact-integer? exact-integer?)
  (let loop-length ((len 1) (cnt 0) (sum 0))
    (if (= cnt n)
        sum
        (let* ([odd? (odd? len)]
               [m (if odd? (quotient (+ len 1) 2) (/ len 2))]
               [start (if (= m 1) 1 (expt 10 (- m 1)))]
               [end (sub1 (expt 10 m))])
          (let inner ((prefix start) (cnt cnt) (sum sum))
            (cond
              [(= cnt n) (loop-length (add1 len) cnt sum)]
              [(> prefix end) (loop-length (add1 len) cnt sum)]
              [else
               (define pal (if odd? (make-odd prefix) (make-even prefix)))
               (if (pal? pal k)
                   (inner (add1 prefix) (+ cnt 1) (+ sum pal))
                   (inner (add1 prefix) cnt sum))]))))))
```

## Erlang

```erlang
-spec k_mirror(K :: integer(), N :: integer()) -> integer().
k_mirror(K, N) ->
    loop(N, K, 0, 0, 1, 1).

loop(N, _K, Sum, Count, _Iodd, _Ieven) when Count =:= N ->
    Sum;
loop(N, K, Sum, Count, Iodd, Ieven) ->
    Po = make_pal(Iodd, true),
    Pe = make_pal(Ieven, false),
    if
        Po < Pe ->
            Cand = Po,
            NewIodd = Iodd + 1,
            NewIeven = Ieven;
        true ->
            Cand = Pe,
            NewIodd = Iodd,
            NewIeven = Ieven + 1
    end,
    case is_pal_base(Cand, K) of
        true -> loop(N, K, Sum + Cand, Count + 1, NewIodd, NewIeven);
        false -> loop(N, K, Sum, Count, NewIodd, NewIeven)
    end.

make_pal(Num, Odd) ->
    Digits = int_to_digits(Num),
    RevPart =
        case Odd of
            true ->
                Len = length(Digits),
                case Len of
                    1 -> [];
                    _ -> lists:reverse(lists:sublist(Digits, Len - 1))
                end;
            false ->
                lists:reverse(Digits)
        end,
    PalDigits = Digits ++ RevPart,
    digits_to_int(PalDigits).

is_pal_base(N, Base) ->
    Digs = digits_in_base(N, Base),
    Digs =:= lists:reverse(Digs).

int_to_digits(0) -> [0];
int_to_digits(N) when N > 0 ->
    int_to_digits(N, []).

int_to_digits(0, Acc) -> Acc;
int_to_digits(N, Acc) ->
    D = N rem 10,
    int_to_digits(N div 10, [D | Acc]).

digits_in_base(0, _Base) -> [0];
digits_in_base(N, Base) when N > 0 ->
    digits_in_base(N, Base, []).

digits_in_base(0, _Base, Acc) -> Acc;
digits_in_base(N, Base, Acc) ->
    D = N rem Base,
    digits_in_base(N div Base, Base, [D | Acc]).

digits_to_int(Digits) ->
    lists:foldl(fun(D, Acc) -> Acc * 10 + D end, 0, Digits).
```

## Elixir

```elixir
defmodule Solution do
  @spec k_mirror(k :: integer, n :: integer) :: integer
  def k_mirror(k, n) do
    generate(1, 0, 0, k, n)
  end

  # Recursive generation by length of the prefix
  defp generate(_len, sum, cnt, _k, n) when cnt >= n, do: sum

  defp generate(len, sum, cnt, k, n) do
    start = if len == 1, do: 1, else: trunc(:math.pow(10, len - 1))
    finish = trunc(:math.pow(10, len)) - 1

    {new_sum, new_cnt} =
      Enum.reduce_while(start..finish, {sum, cnt}, fn prefix, {s_acc, c_acc} ->
        s = Integer.to_string(prefix)

        # odd length palindrome
        odd_str = s <> String.reverse(String.slice(s, 0, String.length(s) - 1))
        odd_num = String.to_integer(odd_str)

        if palindrome_in_base?(odd_num, k) do
          c_new = c_acc + 1
          s_new = s_acc + odd_num

          if c_new == n do
            {:halt, {s_new, c_new}}
          else
            # even length palindrome for same prefix
            even_str = s <> String.reverse(s)
            even_num = String.to_integer(even_str)

            if palindrome_in_base?(even_num, k) do
              c_new2 = c_new + 1
              s_new2 = s_new + even_num

              if c_new2 == n do
                {:halt, {s_new2, c_new2}}
              else
                {:cont, {s_new2, c_new2}}
              end
            else
              {:cont, {s_new, c_new}}
            end
          end
        else
          # odd not valid, check even only
          even_str = s <> String.reverse(s)
          even_num = String.to_integer(even_str)

          if palindrome_in_base?(even_num, k) do
            c_new = c_acc + 1
            s_new = s_acc + even_num

            if c_new == n do
              {:halt, {s_new, c_new}}
            else
              {:cont, {s_new, c_new}}
            end
          else
            {:cont, {s_acc, c_acc}}
          end
        end
      end)

    if new_cnt >= n do
      new_sum
    else
      generate(len + 1, new_sum, new_cnt, k, n)
    end
  end

  defp palindrome_in_base?(num, base) do
    digits = get_digits(num, base, [])
    digits == Enum.reverse(digits)
  end

  defp get_digits(0, _base, []), do: [0]
  defp get_digits(0, _base, acc), do: acc
  defp get_digits(num, base, acc) do
    get_digits(div(num, base), base, [rem(num, base) | acc])
  end
end
```
