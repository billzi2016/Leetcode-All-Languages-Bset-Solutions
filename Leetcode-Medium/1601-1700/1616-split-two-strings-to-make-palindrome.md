# 1616. Split Two Strings to Make Palindrome

## Cpp

```cpp
class Solution {
public:
    bool isPal(const string& s, int l, int r) {
        while (l < r && s[l] == s[r]) {
            ++l;
            --r;
        }
        return l >= r;
    }
    
    bool check(const string& a, const string& b) {
        int i = 0, j = (int)a.size() - 1;
        while (i < j && a[i] == b[j]) {
            ++i;
            --j;
        }
        if (i >= j) return true;
        // either take remaining part from a or from b
        return isPal(a, i, j) || isPal(b, i, j);
    }
    
    bool checkPalindromeFormation(string a, string b) {
        return check(a, b) || check(b, a);
    }
};
```

## Java

```java
class Solution {
    public boolean checkPalindromeFormation(String a, String b) {
        return canForm(a, b) || canForm(b, a);
    }
    
    private boolean canForm(String a, String b) {
        int i = 0, j = a.length() - 1;
        while (i < j && a.charAt(i) == b.charAt(j)) {
            i++;
            j--;
        }
        return isPalindrome(a, i, j) || isPalindrome(b, i, j);
    }
    
    private boolean isPalindrome(String s, int l, int r) {
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) return false;
            l++;
            r--;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def checkPalindromeFormation(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        def can_make(s1, s2):
            l, r = 0, len(s1) - 1
            while l < r and s1[l] == s2[r]:
                l += 1
                r -= 1
            if l >= r:
                return True
            # check remaining part in either string is palindrome
            sub = s1[l:r+1]
            if sub == sub[::-1]:
                return True
            sub = s2[l:r+1]
            if sub == sub[::-1]:
                return True
            return False

        return can_make(a, b) or can_make(b, a)
```

## Python3

```python
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def is_pal(s: str, l: int, r: int) -> bool:
            while l < r and s[l] == s[r]:
                l += 1
                r -= 1
            return l >= r

        def check(s1: str, s2: str) -> bool:
            i, j = 0, len(s1) - 1
            while i < j and s1[i] == s2[j]:
                i += 1
                j -= 1
            if i >= j:
                return True
            return is_pal(s1, i, j) or is_pal(s2, i, j)

        return check(a, b) or check(b, a)
```

## C

```c
#include <stdbool.h>
#include <string.h>

static bool isPal(const char *s, int l, int r) {
    while (l < r) {
        if (s[l] != s[r]) return false;
        ++l;
        --r;
    }
    return true;
}

static bool canForm(const char *a, const char *b) {
    int n = strlen(a);
    int i = 0, j = n - 1;
    while (i < j && a[i] == b[j]) {
        ++i;
        --j;
    }
    if (i >= j) return true;
    return isPal(a, i, j) || isPal(b, i, j);
}

bool checkPalindromeFormation(char* a, char* b) {
    return canForm(a, b) || canForm(b, a);
}
```

## Csharp

```csharp
public class Solution {
    public bool CheckPalindromeFormation(string a, string b) {
        return Check(a, b) || Check(b, a);
    }

    private bool Check(string s1, string s2) {
        int i = 0;
        int j = s1.Length - 1;
        while (i < j && s1[i] == s2[j]) {
            i++;
            j--;
        }
        if (i >= j) return true;
        return IsPalindrome(s1, i, j) || IsPalindrome(s2, i, j);
    }

    private bool IsPalindrome(string s, int l, int r) {
        while (l < r) {
            if (s[l] != s[r]) return false;
            l++;
            r--;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} a
 * @param {string} b
 * @return {boolean}
 */
var checkPalindromeFormation = function(a, b) {
    const isPal = (s, l, r) => {
        while (l < r) {
            if (s[l] !== s[r]) return false;
            ++l; --r;
        }
        return true;
    };
    
    const canForm = (s1, s2) => {
        let i = 0, j = s1.length - 1;
        while (i < j && s1[i] === s2[j]) {
            ++i; --j;
        }
        if (i >= j) return true;
        return isPal(s1, i, j) || isPal(s2, i, j);
    };
    
    return canForm(a, b) || canForm(b, a);
};
```

## Typescript

```typescript
function checkPalindromeFormation(a: string, b: string): boolean {
    const n = a.length;
    
    const isPal = (s: string, l: number, r: number): boolean => {
        while (l < r) {
            if (s[l] !== s[r]) return false;
            l++;
            r--;
        }
        return true;
    };
    
    const check = (s1: string, s2: string): boolean => {
        let i = 0, j = n - 1;
        while (i < j && s1[i] === s2[j]) {
            i++;
            j--;
        }
        if (i >= j) return true;
        return isPal(s1, i, j) || isPal(s2, i, j);
    };
    
    return check(a, b) || check(b, a);
}
```

## Php

```php
class Solution {

    /**
     * @param String $a
     * @param String $b
     * @return Boolean
     */
    function checkPalindromeFormation($a, $b) {
        return $this->canForm($a, $b) || $this->canForm($b, $a);
    }

    private function canForm(string $s1, string $s2): bool {
        $n = strlen($s1);
        $l = 0;
        $r = $n - 1;
        while ($l < $r && $s1[$l] === $s2[$r]) {
            $l++;
            $r--;
        }
        if ($l >= $r) {
            return true;
        }
        return $this->isPalindrome($s1, $l, $r) || $this->isPalindrome($s2, $l, $r);
    }

    private function isPalindrome(string $s, int $l, int $r): bool {
        while ($l < $r) {
            if ($s[$l] !== $s[$r]) {
                return false;
            }
            $l++;
            $r--;
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func checkPalindromeFormation(_ a: String, _ b: String) -> Bool {
        let arrA = Array(a)
        let arrB = Array(b)
        return canForm(arrA, arrB) || canForm(arrB, arrA)
    }
    
    private func canForm(_ s1: [Character], _ s2: [Character]) -> Bool {
        var i = 0
        var j = s1.count - 1
        while i < j && s1[i] == s2[j] {
            i += 1
            j -= 1
        }
        if i >= j { return true }
        return isPalindrome(s1, i, j) || isPalindrome(s2, i, j)
    }
    
    private func isPalindrome(_ arr: [Character], _ left: Int, _ right: Int) -> Bool {
        var l = left
        var r = right
        while l < r {
            if arr[l] != arr[r] { return false }
            l += 1
            r -= 1
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkPalindromeFormation(a: String, b: String): Boolean {
        return canForm(a, b) || canForm(b, a)
    }

    private fun canForm(s1: String, s2: String): Boolean {
        var i = 0
        var j = s1.length - 1
        while (i < j && s1[i] == s2[j]) {
            i++
            j--
        }
        if (i >= j) return true
        return isPalindrome(s1, i, j) || isPalindrome(s2, i, j)
    }

    private fun isPalindrome(s: String, left: Int, right: Int): Boolean {
        var l = left
        var r = right
        while (l < r) {
            if (s[l] != s[r]) return false
            l++
            r--
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool checkPalindromeFormation(String a, String b) {
    return _check(a, b) || _check(b, a);
  }

  bool _check(String s1, String s2) {
    int l = 0;
    int r = s1.length - 1;
    while (l < r && s1.codeUnitAt(l) == s2.codeUnitAt(r)) {
      l++;
      r--;
    }
    if (l >= r) return true;
    return _isPal(s1, l, r) || _isPal(s2, l, r);
  }

  bool _isPal(String s, int l, int r) {
    while (l < r && s.codeUnitAt(l) == s.codeUnitAt(r)) {
      l++;
      r--;
    }
    return l >= r;
  }
}
```

## Golang

```go
func checkPalindromeFormation(a string, b string) bool {
    return canForm(a, b) || canForm(b, a)
}

func canForm(s1, s2 string) bool {
    i, j := 0, len(s1)-1
    for i < j && s1[i] == s2[j] {
        i++
        j--
    }
    if i >= j {
        return true
    }
    return isPal(s1, i, j) || isPal(s2, i, j)
}

func isPal(s string, l, r int) bool {
    for l < r && s[l] == s[r] {
        l++
        r--
    }
    return l >= r
}
```

## Ruby

```ruby
def palindrome_range?(s, left, right)
  while left < right
    return false if s.getbyte(left) != s.getbyte(right)
    left += 1
    right -= 1
  end
  true
end

def check_combination(a, b)
  n = a.length
  l = 0
  r = n - 1
  while l < r && a.getbyte(l) == b.getbyte(r)
    l += 1
    r -= 1
  end
  return true if l >= r
  palindrome_range?(a, l, r) || palindrome_range?(b, l, r)
end

# @param {String} a
# @param {String} b
# @return {Boolean}
def check_palindrome_formation(a, b)
  check_combination(a, b) || check_combination(b, a)
end
```

## Scala

```scala
object Solution {
    def checkPalindromeFormation(a: String, b: String): Boolean = {
        def isPal(s: String, l: Int, r: Int): Boolean = {
            var i = l
            var j = r
            while (i < j && s.charAt(i) == s.charAt(j)) {
                i += 1
                j -= 1
            }
            i >= j
        }

        def check(s1: String, s2: String): Boolean = {
            var i = 0
            var j = s1.length - 1
            while (i < j && s1.charAt(i) == s2.charAt(j)) {
                i += 1
                j -= 1
            }
            if (i >= j) return true
            isPal(s1, i, j) || isPal(s2, i, j)
        }

        check(a, b) || check(b, a)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_palindrome_formation(a: String, b: String) -> bool {
        let a_bytes = a.as_bytes();
        let b_bytes = b.as_bytes();

        fn is_pal(s: &[u8], mut l: usize, mut r: usize) -> bool {
            while l < r {
                if s[l] != s[r] {
                    return false;
                }
                l += 1;
                r -= 1;
            }
            true
        }

        fn check(s1: &[u8], s2: &[u8]) -> bool {
            let n = s1.len();
            let mut i = 0usize;
            let mut j = n - 1;
            while i < j && s1[i] == s2[j] {
                i += 1;
                j -= 1;
            }
            if i >= j {
                return true;
            }
            is_pal(s1, i, j) || is_pal(s2, i, j)
        }

        check(a_bytes, b_bytes) || check(b_bytes, a_bytes)
    }
}
```

## Racket

```racket
(define (is-pal? s l r)
  (let loop ((i l) (j r))
    (if (>= i j)
        #t
        (if (char=? (string-ref s i) (string-ref s j))
            (loop (+ i 1) (- j 1))
            #f))))

(define (check-helper s1 s2)
  (let* ((n (string-length s1)))
    (let loop ((i 0) (j (- n 1)))
      (cond
        [(>= i j) #t]
        [(char=? (string-ref s1 i) (string-ref s2 j))
         (loop (+ i 1) (- j 1))]
        [else (or (is-pal? s1 i j) (is-pal? s2 i j))]))))

(define/contract (check-palindrome-formation a b)
  (-> string? string? boolean?)
  (or (check-helper a b) (check-helper b a)))
```

## Erlang

```erlang
-spec check_palindrome_formation(A :: unicode:unicode_binary(), B :: unicode:unicode_binary()) -> boolean().
check_palindrome_formation(A, B) ->
    check(A, B) orelse check(B, A).

%% Check if prefix of S1 + suffix of S2 can form a palindrome
-spec check(binary(), binary()) -> boolean().
check(S1, S2) ->
    N = byte_size(S1),
    match_until_mismatch(S1, S2, 0, N - 1).

-spec match_until_mismatch(binary(), binary(), non_neg_integer(), integer()) -> boolean().
match_until_mismatch(_S1, _S2, L, R) when L >= R ->
    true;
match_until_mismatch(S1, S2, L, R) ->
    C1 = binary:at(S1, L),
    C2 = binary:at(S2, R),
    if
        C1 == C2 ->
            match_until_mismatch(S1, S2, L + 1, R - 1);
        true ->
            is_palindrome(S1, L, R) orelse is_palindrome(S2, L, R)
    end.

-spec is_palindrome(binary(), non_neg_integer(), integer()) -> boolean().
is_palindrome(_Bin, L, R) when L >= R ->
    true;
is_palindrome(Bin, L, R) ->
    if
        binary:at(Bin, L) == binary:at(Bin, R) ->
            is_palindrome(Bin, L + 1, R - 1);
        true ->
            false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_palindrome_formation(a :: String.t(), b :: String.t()) :: boolean()
  def check_palindrome_formation(a, b) do
    possible?(a, b) or possible?(b, a)
  end

  defp possible?(s1, s2) do
    n = byte_size(s1)
    {l, r} = advance(s1, s2, 0, n - 1)

    if l >= r do
      true
    else
      is_pal?(s1, l, r) or is_pal?(s2, l, r)
    end
  end

  defp advance(_s1, _s2, l, r) when l >= r, do: {l, r}

  defp advance(s1, s2, l, r) do
    if :binary.at(s1, l) == :binary.at(s2, r) do
      advance(s1, s2, l + 1, r - 1)
    else
      {l, r}
    end
  end

  defp is_pal?(_s, l, r) when l >= r, do: true

  defp is_pal?(s, l, r) do
    if :binary.at(s, l) == :binary.at(s, r) do
      is_pal?(s, l + 1, r - 1)
    else
      false
    end
  end
end
```
