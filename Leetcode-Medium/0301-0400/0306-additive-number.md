# 0306. Additive Number

## Cpp

```cpp
class Solution {
public:
    bool isAdditiveNumber(string num) {
        int n = num.size();
        for (int i = 1; i <= n - 2; ++i) {
            string first = num.substr(0, i);
            if (first.size() > 1 && first[0] == '0') break; // leading zero invalid
            for (int j = 1; j <= n - i - 1; ++j) {
                string second = num.substr(i, j);
                if (second.size() > 1 && second[0] == '0') continue;
                if (dfs(num, i + j, first, second)) return true;
            }
        }
        return false;
    }

private:
    string add(const string& a, const string& b) {
        int i = (int)a.size() - 1, j = (int)b.size() - 1, carry = 0;
        string res;
        while (i >= 0 || j >= 0 || carry) {
            int sum = carry;
            if (i >= 0) sum += a[i--] - '0';
            if (j >= 0) sum += b[j--] - '0';
            res.push_back(char('0' + (sum % 10)));
            carry = sum / 10;
        }
        reverse(res.begin(), res.end());
        return res;
    }

    bool dfs(const string& num, int start, const string& a, const string& b) {
        string s = add(a, b);
        if (start + (int)s.size() > (int)num.size()) return false;
        if (num.compare(start, s.size(), s) != 0) return false;
        int nextPos = start + s.size();
        if (nextPos == (int)num.size()) return true;
        return dfs(num, nextPos, b, s);
    }
};
```

## Java

```java
class Solution {
    public boolean isAdditiveNumber(String num) {
        int n = num.length();
        for (int i = 1; i <= n - 2; i++) {
            if (num.charAt(0) == '0' && i > 1) break; // leading zero in first number
            String s1 = num.substring(0, i);
            java.math.BigInteger first = new java.math.BigInteger(s1);
            for (int j = i + 1; j <= n - 1; j++) {
                int len2 = j - i;
                if (num.charAt(i) == '0' && len2 > 1) break; // leading zero in second number
                String s2 = num.substring(i, j);
                java.math.BigInteger second = new java.math.BigInteger(s2);
                if (dfs(first, second, j, num, 2)) return true;
            }
        }
        return false;
    }

    private boolean dfs(java.math.BigInteger a, java.math.BigInteger b, int start,
                        String num, int count) {
        if (start == num.length()) {
            return count >= 3;
        }
        java.math.BigInteger c = a.add(b);
        String cs = c.toString();
        if (!num.startsWith(cs, start)) {
            return false;
        }
        return dfs(b, c, start + cs.length(), num, count + 1);
    }
}
```

## Python

```python
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in range(1, n):
            # first number cannot have leading zeros unless it is "0"
            if num[0] == '0' and i > 1:
                break
            a = int(num[:i])
            for j in range(i + 1, n):
                # second number cannot have leading zeros unless it is "0"
                if num[i] == '0' and j - i > 1:
                    break
                b = int(num[i:j])
                if self._valid(a, b, num[j:]):
                    return True
        return False

    def _valid(self, a, b, remaining):
        while remaining:
            c = a + b
            s = str(c)
            if not remaining.startswith(s):
                return False
            remaining = remaining[len(s):]
            a, b = b, c
        # at least one addition performed means we had >=3 numbers
        return True
```

## Python3

```python
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        # first number length i
        for i in range(1, n):
            # leading zero check for first number
            if num[0] == '0' and i > 1:
                break
            first = num[:i]
            # second number length j-i
            for j in range(i + 1, n):
                # leading zero check for second number
                if num[i] == '0' and (j - i) > 1:
                    break
                second = num[i:j]
                start = j
                f, s = first, second
                while start < n:
                    sum_val = str(int(f) + int(s))
                    if not num.startswith(sum_val, start):
                        break
                    start += len(sum_val)
                    f, s = s, sum_val
                if start == n:
                    return True
        return False
```

## C

```c
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

static char *addStrings(const char *a, const char *b) {
    int len1 = strlen(a), len2 = strlen(b);
    int maxlen = (len1 > len2 ? len1 : len2) + 1;
    char *res = (char *)malloc(maxlen + 1); // extra for '\0'
    int i = len1 - 1, j = len2 - 1, k = 0, carry = 0;
    while (i >= 0 || j >= 0 || carry) {
        int sum = carry;
        if (i >= 0) sum += a[i--] - '0';
        if (j >= 0) sum += b[j--] - '0';
        res[k++] = (char)((sum % 10) + '0');
        carry = sum / 10;
    }
    // reverse
    for (int p = 0; p < k / 2; ++p) {
        char tmp = res[p];
        res[p] = res[k - 1 - p];
        res[k - 1 - p] = tmp;
    }
    res[k] = '\0';
    return res;
}

static bool dfs(const char *num, int n, int start,
                const char *a, const char *b, int count) {
    char *sum = addStrings(a, b);
    int sumLen = strlen(sum);
    if (start + sumLen > n) {
        free(sum);
        return false;
    }
    if (strncmp(num + start, sum, sumLen) != 0) {
        free(sum);
        return false;
    }
    if (start + sumLen == n) {
        bool ok = (count + 1) >= 3;
        free(sum);
        return ok;
    }
    bool res = dfs(num, n, start + sumLen, b, sum, count + 1);
    free(sum);
    return res;
}

bool isAdditiveNumber(char* num) {
    int len = strlen(num);
    for (int i = 1; i <= len - 2; ++i) {
        if (num[0] == '0' && i > 1) break; // leading zero in first number
        for (int j = i + 1; j <= len - 1; ++j) {
            int len2 = j - i;
            if (num[i] == '0' && len2 > 1) continue; // leading zero in second number

            char *a = (char *)malloc(i + 1);
            memcpy(a, num, i);
            a[i] = '\0';
            char *b = (char *)malloc(len2 + 1);
            memcpy(b, num + i, len2);
            b[len2] = '\0';

            bool ok = dfs(num, len, j, a, b, 2);
            free(a);
            free(b);
            if (ok) return true;
        }
    }
    return false;
}
```

## Csharp

```csharp
using System.Numerics;

public class Solution {
    public bool IsAdditiveNumber(string num) {
        int n = num.Length;
        for (int i = 1; i <= n - 2; i++) {
            if (num[0] == '0' && i > 1) break; // leading zero in first number
            string s1 = num.Substring(0, i);
            BigInteger first = BigInteger.Parse(s1);
            for (int j = i + 1; j <= n - 1; j++) {
                int len2 = j - i;
                if (num[i] == '0' && len2 > 1) break; // leading zero in second number
                string s2 = num.Substring(i, len2);
                BigInteger second = BigInteger.Parse(s2);
                if (CheckSequence(first, second, j, num)) return true;
            }
        }
        return false;
    }

    private bool CheckSequence(BigInteger first, BigInteger second, int startIdx, string num) {
        int n = num.Length;
        bool added = false;
        while (startIdx < n) {
            BigInteger sum = first + second;
            string sSum = sum.ToString();
            if (!num.StartsWith(sSum, startIdx)) return false;
            startIdx += sSum.Length;
            first = second;
            second = sum;
            added = true;
        }
        return added && startIdx == n;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} num
 * @return {boolean}
 */
var isAdditiveNumber = function(num) {
    const n = num.length;
    
    // helper to add two numeric strings
    const addStrings = (a, b) => {
        let i = a.length - 1, j = b.length - 1, carry = 0;
        let res = '';
        while (i >= 0 || j >= 0 || carry) {
            const x = i >= 0 ? a.charCodeAt(i) - 48 : 0;
            const y = j >= 0 ? b.charCodeAt(j) - 48 : 0;
            const sum = x + y + carry;
            res = String.fromCharCode((sum % 10) + 48) + res;
            carry = Math.floor(sum / 10);
            i--; j--;
        }
        return res;
    };
    
    // check if starting from index 'start' we can build a valid additive sequence
    const isValid = (start, first, second) => {
        let cnt = 0; // number of additions performed
        while (start < n) {
            const sum = addStrings(first, second);
            if (!num.startsWith(sum, start)) return false;
            start += sum.length;
            first = second;
            second = sum;
            cnt++;
        }
        return cnt >= 1; // need at least one addition => at least three numbers total
    };
    
    for (let i = 1; i <= n - 2; i++) {
        if (num[0] === '0' && i > 1) break; // leading zero in first number
        const first = num.slice(0, i);
        for (let j = i + 1; j <= n - 1; j++) {
            if (num[i] === '0' && j - i > 1) break; // leading zero in second number
            const second = num.slice(i, j);
            if (isValid(j, first, second)) return true;
        }
    }
    return false;
};
```

## Typescript

```typescript
function isAdditiveNumber(num: string): boolean {
    const n = num.length;

    const addStrings = (a: string, b: string): string => {
        let i = a.length - 1;
        let j = b.length - 1;
        let carry = 0;
        const res: string[] = [];
        while (i >= 0 || j >= 0 || carry) {
            const x = i >= 0 ? a.charCodeAt(i) - 48 : 0;
            const y = j >= 0 ? b.charCodeAt(j) - 48 : 0;
            const sum = x + y + carry;
            res.push(String.fromCharCode((sum % 10) + 48));
            carry = Math.floor(sum / 10);
            i--;
            j--;
        }
        return res.reverse().join('');
    };

    for (let i = 1; i <= n - 2; i++) {
        // first number cannot have leading zeros
        if (num[0] === '0' && i > 1) break;
        const first = num.slice(0, i);

        for (let j = i + 1; j <= n - 1; j++) {
            const len2 = j - i;
            // second number cannot have leading zeros
            if (num[i] === '0' && len2 > 1) continue;
            const second = num.slice(i, j);

            let a = first;
            let b = second;
            let idx = j;

            while (idx < n) {
                const sum = addStrings(a, b);
                if (!num.startsWith(sum, idx)) break;
                idx += sum.length;
                a = b;
                b = sum;
            }

            if (idx === n) return true; // consumed whole string
        }
    }

    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param String $num
     * @return Boolean
     */
    function isAdditiveNumber($num) {
        $n = strlen($num);
        for ($i = 1; $i <= $n - 2; $i++) {
            $first = substr($num, 0, $i);
            if ($first[0] === '0' && $i > 1) continue;
            for ($j = 1; $j <= $n - $i - 1; $j++) {
                $second = substr($num, $i, $j);
                if ($second[0] === '0' && $j > 1) continue;
                $remaining = substr($num, $i + $j);
                if ($this->checkSequence($first, $second, $remaining)) {
                    return true;
                }
            }
        }
        return false;
    }

    private function checkSequence(string $a, string $b, string $rest): bool {
        while (true) {
            $c = $this->addStrings($a, $b);
            $lenC = strlen($c);
            if (substr($rest, 0, $lenC) !== $c) {
                return false;
            }
            $rest = substr($rest, $lenC);
            if ($rest === '') {
                // at least three numbers have been used
                return true;
            }
            $a = $b;
            $b = $c;
        }
    }

    private function addStrings(string $num1, string $num2): string {
        $i = strlen($num1) - 1;
        $j = strlen($num2) - 1;
        $carry = 0;
        $res = '';
        while ($i >= 0 || $j >= 0 || $carry > 0) {
            $x = $i >= 0 ? intval($num1[$i]) : 0;
            $y = $j >= 0 ? intval($num2[$j]) : 0;
            $sum = $x + $y + $carry;
            $res = ($sum % 10) . $res;
            $carry = intdiv($sum, 10);
            $i--;
            $j--;
        }
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func isAdditiveNumber(_ num: String) -> Bool {
        let n = num.count
        if n < 3 { return false }
        for i in 1..<(n - 1) { // length of first number
            if i > 1 && num.first! == Character("0") { break } // leading zero not allowed
            for j in 1..<(n - i) { // length of second number
                if j > 1 && num[num.index(num.startIndex, offsetBy: i)] == Character("0") {
                    continue
                }
                let first = sub(num, 0, i)
                let second = sub(num, i, j)
                var pos = i + j
                var a = first
                var b = second
                var count = 2
                while pos < n {
                    let sum = addStrings(a, b)
                    let len = sum.count
                    if pos + len > n { break }
                    let nextPart = sub(num, pos, len)
                    if nextPart != sum { break }
                    pos += len
                    a = b
                    b = sum
                    count += 1
                }
                if pos == n && count >= 3 {
                    return true
                }
            }
        }
        return false
    }

    private func addStrings(_ num1: String, _ num2: String) -> String {
        let arr1 = Array(num1)
        let arr2 = Array(num2)
        var i = arr1.count - 1
        var j = arr2.count - 1
        var carry = 0
        var res = [Character]()
        while i >= 0 || j >= 0 || carry > 0 {
            let d1 = i >= 0 ? Int(String(arr1[i]))! : 0
            let d2 = j >= 0 ? Int(String(arr2[j]))! : 0
            let sum = d1 + d2 + carry
            res.append(Character(UnicodeScalar(sum % 10 + 48)!))
            carry = sum / 10
            i -= 1
            j -= 1
        }
        return String(res.reversed())
    }

    private func sub(_ s: String, _ start: Int, _ length: Int) -> String {
        let startIdx = s.index(s.startIndex, offsetBy: start)
        let endIdx = s.index(startIdx, offsetBy: length)
        return String(s[startIdx..<endIdx])
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isAdditiveNumber(num: String): Boolean {
        val n = num.length
        for (i in 1 until n) { // length of first number
            if (i > 1 && num[0] == '0') break  // leading zero not allowed
            for (j in 1 until n - i) { // length of second number
                if (j > 1 && num[i] == '0') break  // leading zero not allowed
                val first = num.substring(0, i)
                val second = num.substring(i, i + j)
                if (check(first, second, i + j, num)) return true
            }
        }
        return false
    }

    private fun check(first: String, second: String, startIdx: Int, s: String): Boolean {
        var idx = startIdx
        var a = first
        var b = second
        while (idx < s.length) {
            val sum = (java.math.BigInteger(a) + java.math.BigInteger(b)).toString()
            if (!s.startsWith(sum, idx)) return false
            idx += sum.length
            a = b
            b = sum
        }
        // must have used at least one addition (i.e., sequence length >= 3)
        return idx == s.length && startIdx != idx
    }
}
```

## Dart

```dart
class Solution {
  bool isAdditiveNumber(String num) {
    int n = num.length;
    for (int i = 1; i <= n - 2; i++) {
      if (i > 1 && num[0] == '0') break; // leading zero in first number
      String first = num.substring(0, i);
      for (int j = 1; j <= n - i - 1; j++) {
        if (j > 1 && num[i] == '0') continue; // leading zero in second number
        String second = num.substring(i, i + j);
        if (_dfs(num, i + j, first, second)) return true;
      }
    }
    return false;
  }

  bool _dfs(String num, int start, String prev1, String prev2) {
    if (start == num.length) return true;
    String sum = _add(prev1, prev2);
    if (!num.startsWith(sum, start)) return false;
    return _dfs(num, start + sum.length, prev2, sum);
  }

  String _add(String a, String b) {
    int i = a.length - 1;
    int j = b.length - 1;
    int carry = 0;
    List<int> digits = [];
    while (i >= 0 || j >= 0 || carry > 0) {
      int s = carry;
      if (i >= 0) s += a.codeUnitAt(i) - 48;
      if (j >= 0) s += b.codeUnitAt(j) - 48;
      digits.add(s % 10);
      carry = s ~/ 10;
      i--;
      j--;
    }
    StringBuffer sb = StringBuffer();
    for (int k = digits.length - 1; k >= 0; k--) {
      sb.writeCharCode(digits[k] + 48);
    }
    return sb.toString();
  }
}
```

## Golang

```go
import (
	"math/big"
	"strings"
)

func isAdditiveNumber(num string) bool {
	n := len(num)
	for i := 1; i <= n-2; i++ {
		if num[0] == '0' && i > 1 {
			break
		}
		for j := 1; j <= n-i-1; j++ {
			if num[i] == '0' && j > 1 {
				break
			}
			a := num[:i]
			b := num[i : i+j]
			if check(a, b, num[i+j:]) {
				return true
			}
		}
	}
	return false
}

func check(a, b, rest string) bool {
	for len(rest) > 0 {
		sum := addStrings(a, b)
		if !strings.HasPrefix(rest, sum) {
			return false
		}
		rest = rest[len(sum):]
		a, b = b, sum
	}
	return true
}

func addStrings(x, y string) string {
	var a, b big.Int
	a.SetString(x, 10)
	b.SetString(y, 10)
	var s big.Int
	s.Add(&a, &b)
	return s.String()
}
```

## Ruby

```ruby
def is_additive_number(num)
  n = num.length
  (1..n - 2).each do |i|
    next if i > 1 && num[0] == '0'
    a = num[0, i].to_i
    (i + 1..n - 1).each do |j|
      len2 = j - i
      next if len2 > 1 && num[i] == '0'
      b = num[i, len2].to_i
      pos = j
      count = 2
      while pos < n
        sum = a + b
        s = sum.to_s
        break unless pos + s.length <= n && num[pos, s.length] == s
        pos += s.length
        a, b = b, sum
        count += 1
      end
      return true if pos == n && count >= 3
    end
  end
  false
end
```

## Scala

```scala
object Solution {
  import java.math.BigInteger

  def isAdditiveNumber(num: String): Boolean = {
    val n = num.length
    for {
      i <- 1 until n
      if !(num.charAt(0) == '0' && i > 1)
      j <- i + 1 until n
      if !(num.charAt(i) == '0' && (j - i) > 1)
    } {
      val first = new BigInteger(num.substring(0, i))
      val second = new BigInteger(num.substring(i, j))
      if (check(j, first, second, num, n)) return true
    }
    false
  }

  private def check(start: Int, a: BigInteger, b: BigInteger,
                    s: String, len: Int): Boolean = {
    var idx = start
    var prev1 = a
    var prev2 = b
    while (idx < len) {
      val sum = prev1.add(prev2)
      val sumStr = sum.toString
      if (!s.startsWith(sumStr, idx)) return false
      idx += sumStr.length
      prev1 = prev2
      prev2 = sum
    }
    true
  }
}
```

## Rust

```rust
impl Solution {
    pub fn is_additive_number(num: String) -> bool {
        let n = num.len();
        let bytes = num.as_bytes();
        for i in 1..=n - 2 {
            if bytes[0] == b'0' && i > 1 {
                break;
            }
            for j in i + 1..=n - 1 {
                if bytes[i] == b'0' && (j - i) > 1 {
                    continue;
                }
                let first = &num[0..i];
                let second = &num[i..j];
                if Self::dfs(&num, j, first, second) {
                    return true;
                }
            }
        }
        false
    }

    fn dfs(num: &str, start: usize, a: &str, b: &str) -> bool {
        let sum = Self::add_str(a, b);
        if !num[start..].starts_with(&sum) {
            return false;
        }
        let next = start + sum.len();
        if next == num.len() {
            true
        } else {
            Self::dfs(num, next, b, &sum)
        }
    }

    fn add_str(a: &str, b: &str) -> String {
        let mut carry = 0u32;
        let mut res: Vec<u8> = Vec::new();
        let bytes_a = a.as_bytes();
        let bytes_b = b.as_bytes();
        let mut i: i32 = a.len() as i32 - 1;
        let mut j: i32 = b.len() as i32 - 1;
        while i >= 0 || j >= 0 || carry > 0 {
            let mut sum = carry;
            if i >= 0 {
                sum += (bytes_a[i as usize] - b'0') as u32;
                i -= 1;
            }
            if j >= 0 {
                sum += (bytes_b[j as usize] - b'0') as u32;
                j -= 1;
            }
            res.push((sum % 10) as u8 + b'0');
            carry = sum / 10;
        }
        res.reverse();
        unsafe { String::from_utf8_unchecked(res) }
    }
}
```

## Racket

```racket
(define/contract (is-additive-number num)
  (-> string? boolean?)
  (let ((n (string-length num)))
    (let recur-i ((i 1))
      (if (> i (- n 2))
          #f
          (let ((first (substring num 0 i)))
            (if (and (> (string-length first) 1)
                     (char=? (string-ref first 0) #\0))
                (recur-i (+ i 1))
                (let recur-j ((j (+ i 1)))
                  (cond
                    [(> j (- n 1)) (recur-i (+ i 1))]
                    [else
                     (let ((second (substring num i j)))
                       (if (and (> (string-length second) 1)
                                (char=? (string-ref second 0) #\0))
                           (recur-j (+ j 1))
                           (let* ((a (string->number first))
                                  (b (string->number second)))
                             (define (check a b idx)
                               (if (= idx n)
                                   #t
                                   (let* ((sum (+ a b))
                                          (sum-str (number->string sum))
                                          (len (string-length sum-str)))
                                     (if (> (+ idx len) n)
                                         #f
                                         (if (string=? (substring num idx (+ idx len)) sum-str)
                                             (check b sum (+ idx len))
                                             #f)))))
                             (if (check a b j)
                                 #t
                                 (recur-j (+ j 1))))))])))))))))
```

## Erlang

```erlang
-module(solution).
-export([is_additive_number/1]).
-spec is_additive_number(Num :: unicode:unicode_binary()) -> boolean().
is_additive_number(Num) ->
    Len = byte_size(Num),
    try_first_split(Num, Len, 1).

try_first_split(_Num, _Len, I) when I > _Len - 2 ->
    false;
try_first_split(Num, Len, I) ->
    FirstBin = binary:part(Num, {0, I}),
    case valid_number_bin(FirstBin) of
        false -> try_first_split(Num, Len, I + 1);
        true ->
            FirstInt = binary_to_integer(FirstBin),
            case try_second_split(Num, Len, I, FirstInt, I + 1) of
                true -> true;
                false -> try_first_split(Num, Len, I + 1)
            end
    end.

try_second_split(_Num, _Len, _I, _FirstInt, J) when J > _Len - 1 ->
    false;
try_second_split(Num, Len, I, FirstInt, J) ->
    SecondBin = binary:part(Num, {I, J - I}),
    case valid_number_bin(SecondBin) of
        false -> try_second_split(Num, Len, I, FirstInt, J + 1);
        true ->
            SecondInt = binary_to_integer(SecondBin),
            case check_rest(Num, Len, J, FirstInt, SecondInt) of
                true -> true;
                false -> try_second_split(Num, Len, I, FirstInt, J + 1)
            end
    end.

check_rest(_Num, _Len, Pos, _Prev1, _Prev2) when Pos >= _Len ->
    false;
check_rest(Num, Len, Pos, Prev1, Prev2) ->
    Sum = Prev1 + Prev2,
    SumBin = integer_to_binary(Sum),
    SumLen = byte_size(SumBin),
    case Pos + SumLen =< Len of
        false -> false;
        true ->
            case binary:part(Num, {Pos, SumLen}) of
                SumBin ->
                    NewPos = Pos + SumLen,
                    if
                        NewPos == Len -> true;
                        true -> check_rest(Num, Len, NewPos, Prev2, Sum)
                    end;
                _Other -> false
            end
    end.

valid_number_bin(Bin) ->
    case Bin of
        <<$0, _/binary>> when byte_size(Bin) > 1 -> false;
        _ -> true
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_additive_number(num :: String.t()) :: boolean()
  def is_additive_number(num) do
    n = String.length(num)

    1..(n - 2)
    |> Enum.any?(fn i ->
      if i > 1 && String.at(num, 0) == "0" do
        false
      else
        a_int = String.slice(num, 0, i) |> String.to_integer()

        (i + 1)..(n - 1)
        |> Enum.any?(fn j ->
          len_b = j - i

          if len_b > 1 && String.at(num, i) == "0" do
            false
          else
            b_int = String.slice(num, i, len_b) |> String.to_integer()
            j < n && valid?(num, a_int, b_int, j)
          end
        end)
      end
    end)
  end

  defp valid?(num, a, b, idx) do
    len = String.length(num)

    if idx == len do
      true
    else
      sum = a + b
      sum_str = Integer.to_string(sum)
      sum_len = byte_size(sum_str)

      if idx + sum_len <= len && String.slice(num, idx, sum_len) == sum_str do
        valid?(num, b, sum, idx + sum_len)
      else
        false
      end
    end
  end
end
```
