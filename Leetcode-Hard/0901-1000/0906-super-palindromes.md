# 0906. Super Palindromes

## Cpp

```cpp
class Solution {
public:
    bool isPalindrome(unsigned long long x) {
        unsigned long long orig = x, rev = 0;
        while (x > 0) {
            rev = rev * 10 + x % 10;
            x /= 10;
        }
        return rev == orig;
    }

    int superpalindromesInRange(string left, string right) {
        unsigned long long L = stoull(left);
        unsigned long long R = stoull(right);
        const unsigned long long MAX_ROOT = 1000000000ULL; // sqrt(1e18)
        int ans = 0;

        auto check = [&](unsigned long long root) {
            unsigned long long sq = root * root;
            if (sq < L || sq > R) return;
            if (isPalindrome(sq)) ++ans;
        };

        for (int i = 1; ; ++i) {
            string s = to_string(i);
            string rev(s.rbegin(), s.rend());

            // odd length palindrome
            string oddStr = s + rev.substr(1);
            unsigned long long rootOdd = stoull(oddStr);
            if (rootOdd > MAX_ROOT) break;
            check(rootOdd);

            // even length palindrome
            string evenStr = s + rev;
            unsigned long long rootEven = stoull(evenStr);
            if (rootEven <= MAX_ROOT) {
                check(rootEven);
            }
        }

        return ans;
    }
};
```

## Java

```java
class Solution {
    public int superpalindromesInRange(String left, String right) {
        long L = Long.parseLong(left);
        long R = Long.parseLong(right);
        int count = 0;
        long limit = (long) Math.sqrt(R) + 1;

        for (int i = 1; ; i++) {
            String s = Integer.toString(i);
            String rev = new StringBuilder(s).reverse().toString();

            // odd length palindrome
            String oddStr = s + rev.substring(1);
            long rootOdd = Long.parseLong(oddStr);
            if (rootOdd > limit) break;
            long sq = rootOdd * rootOdd;
            if (sq >= L && sq <= R && isPalindrome(sq)) {
                count++;
            }

            // even length palindrome
            String evenStr = s + rev;
            long rootEven = Long.parseLong(evenStr);
            if (rootEven > limit) continue;
            long sq2 = rootEven * rootEven;
            if (sq2 >= L && sq2 <= R && isPalindrome(sq2)) {
                count++;
            }
        }

        return count;
    }

    private boolean isPalindrome(long x) {
        String s = Long.toString(x);
        int i = 0, j = s.length() - 1;
        while (i < j) {
            if (s.charAt(i++) != s.charAt(j--)) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def superpalindromesInRange(self, left, right):
        """
        :type left: str
        :type right: str
        :rtype: int
        """
        L = int(left)
        R = int(right)

        def is_pal(num):
            s = str(num)
            return s == s[::-1]

        count = 0
        LIMIT = 100000  # enough because sqrt(10^18) < 10^9 and half length <=5

        for i in range(1, LIMIT):
            s = str(i)

            # odd length palindrome root
            odd_root = int(s + s[-2::-1])
            sq = odd_root * odd_root
            if L <= sq <= R and is_pal(sq):
                count += 1

            # even length palindrome root
            even_root = int(s + s[::-1])
            sq = even_root * even_root
            if L <= sq <= R and is_pal(sq):
                count += 1

        return count
```

## Python3

```python
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        L = int(left)
        R = int(right)
        MAX_ROOT = 10 ** 9

        def is_pal(num: int) -> bool:
            s = str(num)
            return s == s[::-1]

        count = 0
        for i in range(1, 100000):
            s = str(i)

            # odd length palindrome root
            r = int(s + s[-2::-1])
            if r > MAX_ROOT:
                break
            sq = r * r
            if L <= sq <= R and is_pal(sq):
                count += 1

            # even length palindrome root
            r2 = int(s + s[::-1])
            if r2 > MAX_ROOT:
                continue
            sq2 = r2 * r2
            if L <= sq2 <= R and is_pal(sq2):
                count += 1

        return count
```

## C

```c
#include <stdlib.h>
#include <stdint.h>

static unsigned long long make_palindrome(unsigned int x, int odd) {
    unsigned long long res = x;
    unsigned int y = odd ? x / 10 : x;
    while (y > 0) {
        res = res * 10 + (y % 10);
        y /= 10;
    }
    return res;
}

static int is_palindrome_ull(unsigned long long n) {
    unsigned long long orig = n, rev = 0;
    while (n > 0) {
        rev = rev * 10 + (n % 10);
        n /= 10;
    }
    return orig == rev;
}

int superpalindromesInRange(char* left, char* right) {
    unsigned long long L = strtoull(left, NULL, 10);
    unsigned long long R = strtoull(right, NULL, 10);
    int count = 0;

    const unsigned long long LIMIT_ROOT = 1000000000ULL; // sqrt(1e18)

    for (unsigned int i = 1; i < 100000; ++i) {
        // odd length palindrome root
        unsigned long long root = make_palindrome(i, 1);
        if (root > LIMIT_ROOT) break;
        unsigned long long sq = root * root;
        if (sq >= L && sq <= R && is_palindrome_ull(sq)) {
            ++count;
        }

        // even length palindrome root
        root = make_palindrome(i, 0);
        if (root > LIMIT_ROOT) continue; // may still be within limit for larger i, but skip this one
        sq = root * root;
        if (sq >= L && sq <= R && is_palindrome_ull(sq)) {
            ++count;
        }
    }

    return count;
}
```

## Csharp

```csharp
using System;
using System.Text;

public class Solution {
    public int SuperpalindromesInRange(string left, string right) {
        long lower = long.Parse(left);
        long upper = long.Parse(right);
        int count = 0;
        long maxRoot = (long)Math.Sqrt(upper) + 1;

        for (int i = 1; i < 100000; i++) {
            string s = i.ToString();

            // odd length palindrome
            var sbOdd = new StringBuilder(s);
            for (int j = s.Length - 2; j >= 0; j--) sbOdd.Append(s[j]);
            long rootOdd = long.Parse(sbOdd.ToString());
            if (rootOdd <= maxRoot) {
                long sq = rootOdd * rootOdd;
                if (sq >= lower && sq <= upper && IsPalindrome(sq)) count++;
            }

            // even length palindrome
            var sbEven = new StringBuilder(s);
            for (int j = s.Length - 1; j >= 0; j--) sbEven.Append(s[j]);
            long rootEven = long.Parse(sbEven.ToString());
            if (rootEven <= maxRoot) {
                long sq = rootEven * rootEven;
                if (sq >= lower && sq <= upper && IsPalindrome(sq)) count++;
            }
        }

        return count;
    }

    private bool IsPalindrome(long x) {
        string s = x.ToString();
        int i = 0, j = s.Length - 1;
        while (i < j) {
            if (s[i++] != s[j--]) return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} left
 * @param {string} right
 * @return {number}
 */
var superpalindromesInRange = function(left, right) {
    const leftBig = BigInt(left);
    const rightBig = BigInt(right);
    
    const isPalindrome = (s) => {
        let i = 0, j = s.length - 1;
        while (i < j) {
            if (s[i] !== s[j]) return false;
            i++; j--;
        }
        return true;
    };
    
    let count = 0;
    for (let i = 1; ; i++) {
        const s = i.toString();
        const rev = s.split('').reverse().join('');
        
        // odd length palindrome root
        const oddRootStr = s + rev.slice(1);
        const oddRoot = BigInt(oddRootStr);
        const oddSq = oddRoot * oddRoot;
        if (oddSq > rightBig) break; // further roots will only be larger
        if (oddSq >= leftBig && isPalindrome(oddSq.toString())) {
            count++;
        }
        
        // even length palindrome root
        const evenRootStr = s + rev;
        const evenRoot = BigInt(evenRootStr);
        const evenSq = evenRoot * evenRoot;
        if (evenSq <= rightBig && evenSq >= leftBig && isPalindrome(evenSq.toString())) {
            count++;
        }
    }
    
    return count;
};
```

## Typescript

```typescript
function superpalindromesInRange(left: string, right: string): number {
    const leftBig = BigInt(left);
    const rightBig = BigInt(right);
    const MAGIC = 100000; // enough for sqrt(1e18)
    let count = 0;

    const isPal = (n: bigint): boolean => {
        const s = n.toString();
        let i = 0, j = s.length - 1;
        while (i < j) {
            if (s[i] !== s[j]) return false;
            i++;
            j--;
        }
        return true;
    };

    for (let i = 1; i < MAGIC; i++) {
        const s = i.toString();
        const rev = s.split('').reverse().join('');

        // odd length palindrome root
        const oddStr = s + rev.slice(1);
        const rootOdd = BigInt(oddStr);
        const sqOdd = rootOdd * rootOdd;
        if (sqOdd >= leftBig && sqOdd <= rightBig && isPal(sqOdd)) {
            count++;
        }

        // even length palindrome root
        const evenStr = s + rev;
        const rootEven = BigInt(evenStr);
        const sqEven = rootEven * rootEven;
        if (sqEven >= leftBig && sqEven <= rightBig && isPal(sqEven)) {
            count++;
        }
    }

    return count;
}
```

## Php

```php
class Solution {
    /**
     * @param String $left
     * @param String $right
     * @return Integer
     */
    function superpalindromesInRange($left, $right) {
        $L = intval($left);
        $R = intval($right);
        $count = 0;
        for ($k = 1; $k < 100000; $k++) {
            $s = strval($k);
            // odd length palindrome root
            $oddPalStr = $s . strrev(substr($s, 0, -1));
            $root = intval($oddPalStr);
            $square = $root * $root;
            if ($square > $R) {
                break; // further roots will only be larger
            }
            if ($square >= $L && $this->isPalindrome($square)) {
                $count++;
            }
            // even length palindrome root
            $evenPalStr = $s . strrev($s);
            $root2 = intval($evenPalStr);
            $square2 = $root2 * $root2;
            if ($square2 > $R) {
                continue;
            }
            if ($square2 >= $L && $this->isPalindrome($square2)) {
                $count++;
            }
        }
        return $count;
    }

    private function isPalindrome($num) {
        $s = strval($num);
        return $s === strrev($s);
    }
}
```

## Swift

```swift
class Solution {
    func superpalindromesInRange(_ left: String, _ right: String) -> Int {
        let L = UInt64(left)!
        let R = UInt64(right)!
        var ans = 0
        
        for i in 1..<100000 {
            let s = String(i)
            
            // odd length palindrome root
            var rev = String(s.dropLast().reversed())
            var palStr = s + rev
            if let root = UInt64(palStr) {
                let sq = root * root
                if sq >= L && sq <= R && isPalindrome(sq) {
                    ans += 1
                }
            }
            
            // even length palindrome root
            rev = String(s.reversed())
            palStr = s + rev
            if let root2 = UInt64(palStr) {
                let sq2 = root2 * root2
                if sq2 >= L && sq2 <= R && isPalindrome(sq2) {
                    ans += 1
                }
            }
        }
        
        return ans
    }
    
    private func isPalindrome(_ num: UInt64) -> Bool {
        let s = String(num)
        return s == String(s.reversed())
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun superpalindromesInRange(left: String, right: String): Int {
        val leftVal = left.toLong()
        val rightVal = right.toLong()
        var count = 0
        for (i in 1 until 100000) {
            val s = i.toString()
            val rs = s.reversed()
            // odd length palindrome root
            var palStr = s + rs.substring(1)
            var root = palStr.toLong()
            var sq = root * root
            if (sq in leftVal..rightVal && isPalindrome(sq)) {
                count++
            }
            // even length palindrome root
            palStr = s + rs
            root = palStr.toLong()
            sq = root * root
            if (sq in leftVal..rightVal && isPalindrome(sq)) {
                count++
            }
        }
        return count
    }

    private fun isPalindrome(num: Long): Boolean {
        val str = num.toString()
        var i = 0
        var j = str.length - 1
        while (i < j) {
            if (str[i] != str[j]) return false
            i++
            j--
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool _isPalindrome(BigInt n) {
    String s = n.toString();
    int i = 0, j = s.length - 1;
    while (i < j) {
      if (s.codeUnitAt(i) != s.codeUnitAt(j)) return false;
      i++;
      j--;
    }
    return true;
  }

  int superpalindromesInRange(String left, String right) {
    final BigInt L = BigInt.parse(left);
    final BigInt R = BigInt.parse(right);
    int count = 0;

    for (int i = 1; i < 100000; ++i) {
      final String s = i.toString();

      // odd length palindrome root
      final String revOdd =
          s.substring(0, s.length - 1).split('').reversed.join('');
      final BigInt rootOdd = BigInt.parse(s + revOdd);
      final BigInt sqOdd = rootOdd * rootOdd;
      if (sqOdd >= L && sqOdd <= R && _isPalindrome(sqOdd)) {
        count++;
      }

      // even length palindrome root
      final String revEven = s.split('').reversed.join('');
      final BigInt rootEven = BigInt.parse(s + revEven);
      final BigInt sqEven = rootEven * rootEven;
      if (sqEven >= L && sqEven <= R && _isPalindrome(sqEven)) {
        count++;
      }

      // early termination: further roots will only be larger
      if (sqOdd > R && sqEven > R) break;
    }

    return count;
  }
}
```

## Golang

```go
package main

import "strconv"

func superpalindromesInRange(left string, right string) int {
	l, _ := strconv.ParseUint(left, 10, 64)
	r, _ := strconv.ParseUint(right, 10, 64)
	count := 0
	const limit = 100000 // half part upper bound

	rev := func(s string) string {
		b := []byte(s)
		i, j := 0, len(b)-1
		for i < j {
			b[i], b[j] = b[j], b[i]
			i++
			j--
		}
		return string(b)
	}

	isPal := func(x uint64) bool {
		var revNum uint64
		orig := x
		for x > 0 {
			revNum = revNum*10 + x%10
			x /= 10
		}
		return revNum == orig
	}

	for i := 1; i < limit; i++ {
		s := strconv.Itoa(i)

		// odd length palindrome root
		oddRootStr := s + rev(s[:len(s)-1])
		oddRoot, _ := strconv.ParseUint(oddRootStr, 10, 64)
		sq := oddRoot * oddRoot
		if sq > r {
			break
		}
		if sq >= l && isPal(sq) {
			count++
		}

		// even length palindrome root
		evenRootStr := s + rev(s)
		evenRoot, _ := strconv.ParseUint(evenRootStr, 10, 64)
		sq2 := evenRoot * evenRoot
		if sq2 > r {
			continue
		}
		if sq2 >= l && isPal(sq2) {
			count++
		}
	}

	return count
}
```

## Ruby

```ruby
def palindrome?(num)
  s = num.to_s
  s == s.reverse
end

def superpalindromes_in_range(left, right)
  l = left.to_i
  r = right.to_i
  max_root = Integer.sqrt(r)
  count = 0

  i = 1
  while true
    s = i.to_s
    rev = s[0...-1].reverse
    root = (s + rev).to_i
    break if root > max_root
    sq = root * root
    count += 1 if sq >= l && sq <= r && palindrome?(sq)
    i += 1
  end

  i = 1
  while true
    s = i.to_s
    rev = s.reverse
    root = (s + rev).to_i
    break if root > max_root
    sq = root * root
    count += 1 if sq >= l && sq <= r && palindrome?(sq)
    i += 1
  end

  count
end
```

## Scala

```scala
object Solution {
    def superpalindromesInRange(left: String, right: String): Int = {
        val L = left.toLong
        val R = right.toLong
        var count = 0

        def isPal(num: Long): Boolean = {
            var x = num
            var rev = 0L
            while (x > 0) {
                rev = rev * 10 + (x % 10)
                x /= 10
            }
            rev == num
        }

        val limit = 100000 // sufficient for generating palindromic roots up to sqrt(1e18)

        var k = 1
        while (k < limit) {
            val s = k.toString

            // odd length palindrome root
            val oddRootStr = s + s.reverse.drop(1)
            val oddRoot = oddRootStr.toLong
            val oddSq = oddRoot * oddRoot
            if (oddSq >= L && oddSq <= R && isPal(oddSq)) {
                count += 1
            }

            // even length palindrome root
            val evenRootStr = s + s.reverse
            val evenRoot = evenRootStr.toLong
            val evenSq = evenRoot * evenRoot
            if (evenSq >= L && evenSq <= R && isPal(evenSq)) {
                count += 1
            }

            k += 1
        }

        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn superpalindromes_in_range(left: String, right: String) -> i32 {
        fn is_palindrome(num: u128) -> bool {
            let s = num.to_string();
            s.as_bytes().iter().rev().eq(s.as_bytes().iter())
        }

        let left_u: u128 = left.parse().unwrap();
        let right_u: u128 = right.parse().unwrap();

        let mut count = 0i32;

        // k up to 10^5 is enough because sqrt(10^18) < 10^9 (9 digits)
        for k in 1..=100_000 {
            let s = k.to_string();

            // odd length palindrome
            let rev_odd: String = s.chars().rev().skip(1).collect();
            let pal_odd_str = format!("{}{}", s, rev_odd);
            if let Ok(root) = pal_odd_str.parse::<u128>() {
                let square = root * root;
                if square > right_u {
                    // further odd palindromes will only get larger
                    // but we continue to generate even ones for this k
                } else if square >= left_u && is_palindrome(square) {
                    count += 1;
                }
            }

            // even length palindrome
            let rev_even: String = s.chars().rev().collect();
            let pal_even_str = format!("{}{}", s, rev_even);
            if let Ok(root) = pal_even_str.parse::<u128>() {
                let square = root * root;
                if square >= left_u && square <= right_u && is_palindrome(square) {
                    count += 1;
                }
            }
        }

        count
    }
}
```

## Racket

```racket
(define/contract (superpalindromes-in-range left right)
  (-> string? string? exact-integer?)
  (let* ((L (string->number left))
         (R (string->number right))
         (max-k 100000) ; iterate k = 1 .. 99999
         (count 0))
    (define (pal? n)
      (let* ((s (number->string n))
             (rev (list->string (reverse (string->list s)))))
        (string=? s rev)))
    (define (make-palindrome k odd?)
      (let* ((s (number->string k))
             (rev (list->string (reverse (string->list s)))))
        (if odd?
            (string-append s (substring rev 1))
            (string-append s rev))))
    (for ([k (in-range 1 max-k)])
      (let* ((oddRoot (string->number (make-palindrome k #t)))
             (sq (* oddRoot oddRoot)))
        (when (and (>= sq L) (<= sq R) (pal? sq))
          (set! count (+ count 1))))
      (let* ((evenRoot (string->number (make-palindrome k #f)))
             (sq (* evenRoot evenRoot)))
        (when (and (>= sq L) (<= sq R) (pal? sq))
          (set! count (+ count 1)))))
    count))
```

## Erlang

```erlang
-spec superpalindromes_in_range(Left :: unicode:unicode_binary(), Right :: unicode:unicode_binary()) -> integer().
superpalindromes_in_range(Left, Right) ->
    L = list_to_integer(binary_to_list(Left)),
    R = list_to_integer(binary_to_list(Right)),
    MaxK = 100000,
    count_super(1, MaxK, L, R, 0).

count_super(K, MaxK, _L, _R, Acc) when K > MaxK ->
    Acc;
count_super(K, MaxK, L, R, Acc) ->
    S = integer_to_list(K),
    RevS = lists:reverse(S),

    %% even length palindrome root
    RootEvenStr = S ++ RevS,
    RootEven = list_to_integer(RootEvenStr),
    Acc1 = maybe_add(RootEven, L, R, Acc),

    %% odd length palindrome root
    Len = length(S),
    PrefixWithoutLast = if Len > 0 -> lists:sublist(S, Len - 1); true -> [] end,
    RevOdd = lists:reverse(PrefixWithoutLast),
    RootOddStr = S ++ RevOdd,
    RootOdd = list_to_integer(RootOddStr),
    Acc2 = maybe_add(RootOdd, L, R, Acc1),

    count_super(K + 1, MaxK, L, R, Acc2).

maybe_add(Root, L, R, Acc) ->
    Square = Root * Root,
    if
        Square < L; Square > R -> Acc;
        true ->
            case is_palindrome(Square) of
                true -> Acc + 1;
                false -> Acc
            end
    end.

is_palindrome(N) ->
    Str = integer_to_list(N),
    Str == lists:reverse(Str).
```

## Elixir

```elixir
defmodule Solution do
  @spec superpalindromes_in_range(left :: String.t(), right :: String.t()) :: integer()
  def superpalindromes_in_range(left, right) do
    l = String.to_integer(left)
    r = String.to_integer(right)

    Enum.reduce(1..100_000, 0, fn k, acc ->
      s = Integer.to_string(k)
      rev = String.reverse(s)

      # odd length palindrome root
      odd_root =
        (s <> String.slice(rev, 1, byte_size(rev) - 1))
        |> String.to_integer()

      acc =
        if in_range_and_pal?(odd_root * odd_root, l, r) do
          acc + 1
        else
          acc
        end

      # even length palindrome root
      even_root =
        (s <> rev)
        |> String.to_integer()

      if in_range_and_pal?(even_root * even_root, l, r) do
        acc + 1
      else
        acc
      end
    end)
  end

  defp in_range_and_pal?(num, l, r) do
    num >= l and num <= r and palindrome?(num)
  end

  defp palindrome?(n) do
    s = Integer.to_string(n)
    s == String.reverse(s)
  end
end
```
