# 2947. Count Beautiful Substrings I

## Cpp

```cpp
class Solution {
public:
    bool isVowel(char ch) {
        return ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u';
    }
    
    int beautifulSubstrings(string s, int k) {
        int n = s.size();
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            int v = 0, c = 0;
            for (int j = i; j < n; ++j) {
                if (isVowel(s[j])) ++v;
                else ++c;
                if (v == c && ((long long)v * c) % k == 0) {
                    ++ans;
                }
            }
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int beautifulSubstrings(String s, int k) {
        int n = s.length();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int vowels = 0, consonants = 0;
            for (int j = i; j < n; j++) {
                char c = s.charAt(j);
                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                    vowels++;
                } else {
                    consonants++;
                }
                if (vowels == consonants && ((vowels * consonants) % k == 0)) {
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
    def beautifulSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = set('aeiou')
        n = len(s)
        ans = 0
        for i in range(n):
            v = c = 0
            for j in range(i, n):
                if s[j] in vowels:
                    v += 1
                else:
                    c += 1
                if v == c and (v * c) % k == 0:
                    ans += 1
        return ans
```

## Python3

```python
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        n = len(s)
        ans = 0
        for i in range(n):
            v = c = 0
            for j in range(i, n):
                if s[j] in vowels:
                    v += 1
                else:
                    c += 1
                if v == c and (v * c) % k == 0:
                    ans += 1
        return ans
```

## C

```c
#include <string.h>

static inline int isVowel(char ch) {
    return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
}

int beautifulSubstrings(char* s, int k) {
    int n = (int)strlen(s);
    int result = 0;
    for (int i = 0; i < n; ++i) {
        int v = 0, c = 0;
        for (int j = i; j < n; ++j) {
            if (isVowel(s[j]))
                ++v;
            else
                ++c;
            if (v == c && ((v * c) % k == 0))
                ++result;
        }
    }
    return result;
}
```

## Csharp

```csharp
public class Solution {
    public int BeautifulSubstrings(string s, int k) {
        int n = s.Length;
        int result = 0;
        for (int i = 0; i < n; i++) {
            int vowels = 0, consonants = 0;
            for (int j = i; j < n; j++) {
                char c = s[j];
                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
                    vowels++;
                else
                    consonants++;
                
                if (vowels == consonants && ((long)vowels * consonants) % k == 0)
                    result++;
            }
        }
        return result;
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
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);
    const n = s.length;
    let ans = 0;
    for (let i = 0; i < n; ++i) {
        let v = 0, c = 0;
        for (let j = i; j < n; ++j) {
            if (vowels.has(s[j])) v++;
            else c++;
            if (v === c && (v * c) % k === 0) ans++;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function beautifulSubstrings(s: string, k: number): number {
    const n = s.length;
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);
    const prefVowel = new Array(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        prefVowel[i + 1] = prefVowel[i] + (vowels.has(s[i]) ? 1 : 0);
    }
    let ans = 0;
    for (let i = 0; i < n; ++i) {
        for (let j = i; j < n; ++j) {
            const v = prefVowel[j + 1] - prefVowel[i];
            const len = j - i + 1;
            const c = len - v;
            if (v === c && (v * c) % k === 0) {
                ++ans;
            }
        }
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
        $n = strlen($s);
        $ans = 0;
        $vowelSet = ['a'=>1,'e'=>1,'i'=>1,'o'=>1,'u'=>1];
        for ($i = 0; $i < $n; $i++) {
            $v = 0;
            $c = 0;
            for ($j = $i; $j < $n; $j++) {
                $ch = $s[$j];
                if (isset($vowelSet[$ch])) {
                    $v++;
                } else {
                    $c++;
                }
                if ($v === $c && ($v * $c) % $k === 0) {
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
    func beautifulSubstrings(_ s: String, _ k: Int) -> Int {
        let vowels: Set<Character> = ["a", "e", "i", "o", "u"]
        let chars = Array(s)
        let n = chars.count
        var result = 0
        
        for i in 0..<n {
            var vCount = 0
            var cCount = 0
            for j in i..<n {
                if vowels.contains(chars[j]) {
                    vCount += 1
                } else {
                    cCount += 1
                }
                if vCount == cCount && (vCount * cCount) % k == 0 {
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
    fun beautifulSubstrings(s: String, k: Int): Int {
        val vowels = setOf('a', 'e', 'i', 'o', 'u')
        var count = 0
        val n = s.length
        for (i in 0 until n) {
            var v = 0
            var c = 0
            for (j in i until n) {
                if (s[j] in vowels) v++ else c++
                if (v == c && (v * c) % k == 0) {
                    count++
                }
            }
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int beautifulSubstrings(String s, int k) {
    bool isVowel(int code) {
      return code == 97 || // a
          code == 101 || // e
          code == 105 || // i
          code == 111 || // o
          code == 117;   // u
    }

    int n = s.length;
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      int v = 0, c = 0;
      for (int j = i; j < n; ++j) {
        if (isVowel(s.codeUnitAt(j))) {
          ++v;
        } else {
          ++c;
        }
        if (v == c && ((v * c) % k) == 0) {
          ++ans;
        }
      }
    }
    return ans;
  }
}
```

## Golang

```go
func beautifulSubstrings(s string, k int) int {
	isVowel := func(ch byte) bool {
		switch ch {
		case 'a', 'e', 'i', 'o', 'u':
			return true
		}
		return false
	}

	n := len(s)
	prefV := make([]int, n+1)
	for i := 0; i < n; i++ {
		prefV[i+1] = prefV[i]
		if isVowel(s[i]) {
			prefV[i+1]++
		}
	}

	ans := 0
	for i := 0; i < n; i++ {
		for j := i; j < n; j++ {
			v := prefV[j+1] - prefV[i]
			length := j - i + 1
			c := length - v
			if v == c && (v*c)%k == 0 {
				ans++
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def beautiful_substrings(s, k)
  n = s.length
  vowels = "aeiou"
  total = 0

  (0...n).each do |i|
    v = 0
    c = 0
    (i...n).each do |j|
      if vowels.include?(s[j])
        v += 1
      else
        c += 1
      end
      total += 1 if v == c && (v * c) % k == 0
    end
  end

  total
end
```

## Scala

```scala
object Solution {
    def beautifulSubstrings(s: String, k: Int): Int = {
        val vowelSet = Set('a', 'e', 'i', 'o', 'u')
        var count = 0
        val n = s.length
        for (i <- 0 until n) {
            var v = 0
            var c = 0
            var j = i
            while (j < n) {
                if (vowelSet.contains(s.charAt(j))) v += 1 else c += 1
                if (v == c && ((v * c) % k == 0)) count += 1
                j += 1
            }
        }
        count
    }
}
```

## Rust

```rust
impl Solution {
    pub fn beautiful_substrings(s: String, k: i32) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut is_vowel = vec![false; n];
        for (i, &b) in bytes.iter().enumerate() {
            is_vowel[i] = matches!(b as char, 'a' | 'e' | 'i' | 'o' | 'u');
        }
        let mut ans: i32 = 0;
        for i in 0..n {
            let (mut v, mut c) = (0, 0);
            for j in i..n {
                if is_vowel[j] {
                    v += 1;
                } else {
                    c += 1;
                }
                if v == c && ((v * c) as i32 % k == 0) {
                    ans += 1;
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (beautiful-substrings s k)
  (-> string? exact-integer? exact-integer?)
  (let* ((n (string-length s))
         (total 0))
    (for ([i (in-range n)])
      (let ((v 0) (c 0))
        (for ([j (in-range i n)])
          (define ch (string-ref s j))
          (if (or (char=? ch #\a)
                  (char=? ch #\e)
                  (char=? ch #\i)
                  (char=? ch #\o)
                  (char=? ch #\u))
              (set! v (+ v 1))
              (set! c (+ c 1)))
          (when (and (= v c) (= (modulo (* v c) k) 0))
            (set! total (+ total 1))))))
    total))
```

## Erlang

```erlang
-spec beautiful_substrings(S :: unicode:unicode_binary(), K :: integer()) -> integer().
beautiful_substrings(S, K) ->
    Chars = binary_to_list(S),
    process_all(Chars, K).

process_all([], _) -> 0;
process_all([_|Tail]=Rest, K) ->
    CountStart = count_substrings(Rest, K, 0, 0, 0),
    CountStart + process_all(Tail, K).

count_substrings([], _, _, _, Acc) -> Acc;
count_substrings([C|Rest], K, V, Cn, Acc) ->
    {V1, Cn1} = case is_vowel(C) of
        true -> {V + 1, Cn};
        false -> {V, Cn + 1}
    end,
    NewAcc = if V1 == Cn1, (V1 * Cn1) rem K =:= 0 ->
                 Acc + 1;
             true -> Acc
            end,
    count_substrings(Rest, K, V1, Cn1, NewAcc).

is_vowel(C) when C == $a; C == $e; C == $i; C == $o; C == $u -> true;
is_vowel(_) -> false.
```

## Elixir

```elixir
defmodule Solution do
  @spec beautiful_substrings(s :: String.t(), k :: integer) :: integer
  def beautiful_substrings(s, k) do
    chars = String.graphemes(s)
    n = length(chars)

    is_vowel =
      Enum.map(chars, fn
        "a" -> true
        "e" -> true
        "i" -> true
        "o" -> true
        "u" -> true
        _ -> false
      end)

    0..(n - 1)
    |> Enum.reduce(0, fn i, total ->
      {cnt, _} =
        (i..(n - 1))
        |> Enum.reduce({0, {0, 0}}, fn j, {acc, {v, c}} ->
          if Enum.at(is_vowel, j) do
            v = v + 1
            {if(v == c and rem(v * c, k) == 0, do: acc + 1, else: acc), {v, c}}
          else
            c = c + 1
            {if(v == c and rem(v * c, k) == 0, do: acc + 1, else: acc), {v, c}}
          end
        end)

      total + cnt
    end)
  end
end
```
