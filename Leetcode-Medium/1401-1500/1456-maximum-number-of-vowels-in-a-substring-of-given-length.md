# 1456. Maximum Number of Vowels in a Substring of Given Length

## Cpp

```cpp
class Solution {
public:
    int maxVowels(string s, int k) {
        auto isVowel = [](char c) {
            return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        };
        int cnt = 0;
        for (int i = 0; i < k; ++i) {
            if (isVowel(s[i])) ++cnt;
        }
        int ans = cnt;
        for (int i = k; i < (int)s.size(); ++i) {
            if (isVowel(s[i])) ++cnt;
            if (isVowel(s[i - k])) --cnt;
            ans = max(ans, cnt);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxVowels(String s, int k) {
        int n = s.length();
        int count = 0, max = 0;
        for (int i = 0; i < n; i++) {
            if (isVowel(s.charAt(i))) {
                count++;
            }
            if (i >= k && isVowel(s.charAt(i - k))) {
                count--;
            }
            if (i >= k - 1) {
                max = Math.max(max, count);
            }
        }
        return max;
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}
```

## Python

```python
class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = set('aeiou')
        count = sum(1 for ch in s[:k] if ch in vowels)
        max_count = count
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            if count > max_count:
                max_count = count
        return max_count
```

## Python3

```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        cnt = sum(1 for c in s[:k] if c in vowels)
        ans = cnt
        for i in range(k, len(s)):
            if s[i] in vowels:
                cnt += 1
            if s[i - k] in vowels:
                cnt -= 1
            if cnt > ans:
                ans = cnt
        return ans
```

## C

```c
#include <string.h>

static inline int isVowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int maxVowels(char* s, int k) {
    int n = strlen(s);
    int cnt = 0, best = 0;
    for (int i = 0; i < n; ++i) {
        if (isVowel(s[i])) cnt++;
        if (i >= k && isVowel(s[i - k])) cnt--;
        if (i >= k - 1 && cnt > best) best = cnt;
    }
    return best;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxVowels(string s, int k)
    {
        if (string.IsNullOrEmpty(s) || k == 0) return 0;

        bool IsVowel(char c) => c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';

        int current = 0;
        for (int i = 0; i < k; i++)
            if (IsVowel(s[i])) current++;

        int max = current;

        for (int i = k; i < s.Length; i++)
        {
            if (IsVowel(s[i - k])) current--;
            if (IsVowel(s[i])) current++;
            if (current > max) max = current;
        }

        return max;
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
var maxVowels = function(s, k) {
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);
    let count = 0;
    for (let i = 0; i < k; ++i) {
        if (vowels.has(s[i])) count++;
    }
    let max = count;
    for (let i = k; i < s.length; ++i) {
        if (vowels.has(s[i])) count++;
        if (vowels.has(s[i - k])) count--;
        if (count > max) max = count;
    }
    return max;
};
```

## Typescript

```typescript
function maxVowels(s: string, k: number): number {
    const isVowel = (ch: string): boolean => {
        return ch === 'a' || ch === 'e' || ch === 'i' || ch === 'o' || ch === 'u';
    };
    
    let count = 0;
    for (let i = 0; i < k; ++i) {
        if (isVowel(s[i])) count++;
    }
    let max = count;
    
    for (let i = k; i < s.length; ++i) {
        if (isVowel(s[i])) count++;
        if (isVowel(s[i - k])) count--;
        if (count > max) max = count;
    }
    
    return max;
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
    function maxVowels($s, $k) {
        $vowels = ['a'=>true,'e'=>true,'i'=>true,'o'=>true,'u'=>true];
        $n = strlen($s);
        $count = 0;
        for ($i = 0; $i < $k; $i++) {
            if (isset($vowels[$s[$i]])) {
                $count++;
            }
        }
        $max = $count;
        for ($i = $k; $i < $n; $i++) {
            if (isset($vowels[$s[$i]])) {
                $count++;
            }
            if (isset($vowels[$s[$i - $k]])) {
                $count--;
            }
            if ($count > $max) {
                $max = $count;
            }
        }
        return $max;
    }
}
```

## Swift

```swift
class Solution {
    func maxVowels(_ s: String, _ k: Int) -> Int {
        let vowels: Set<Character> = ["a", "e", "i", "o", "u"]
        let chars = Array(s)
        var current = 0
        for i in 0..<k {
            if vowels.contains(chars[i]) { current += 1 }
        }
        var maxCount = current
        if k < chars.count {
            for i in k..<chars.count {
                if vowels.contains(chars[i]) { current += 1 }
                if vowels.contains(chars[i - k]) { current -= 1 }
                if current > maxCount { maxCount = current }
            }
        }
        return maxCount
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxVowels(s: String, k: Int): Int {
        val n = s.length
        var count = 0
        var best = 0
        val vowel = BooleanArray(26)
        vowel['a' - 'a'] = true
        vowel['e' - 'a'] = true
        vowel['i' - 'a'] = true
        vowel['o' - 'a'] = true
        vowel['u' - 'a'] = true

        for (i in 0 until n) {
            if (vowel[s[i] - 'a']) count++
            if (i >= k && vowel[s[i - k] - 'a']) count--
            if (i >= k - 1 && count > best) best = count
        }
        return best
    }
}
```

## Dart

```dart
class Solution {
  int maxVowels(String s, int k) {
    const vowelSet = {'a', 'e', 'i', 'o', 'u'};
    int count = 0;
    for (int i = 0; i < k; ++i) {
      if (vowelSet.contains(s[i])) count++;
    }
    int maxCount = count;
    for (int i = k; i < s.length; ++i) {
      if (vowelSet.contains(s[i])) count++;
      if (vowelSet.contains(s[i - k])) count--;
      if (count > maxCount) maxCount = count;
    }
    return maxCount;
  }
}
```

## Golang

```go
func maxVowels(s string, k int) int {
	isVowel := func(c byte) bool {
		return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
	}
	n := len(s)
	if n == 0 || k == 0 {
		return 0
	}
	cnt := 0
	for i := 0; i < k; i++ {
		if isVowel(s[i]) {
			cnt++
		}
	}
	maxCnt := cnt
	for i := k; i < n; i++ {
		if isVowel(s[i]) {
			cnt++
		}
		if isVowel(s[i-k]) {
			cnt--
		}
		if cnt > maxCnt {
			maxCnt = cnt
		}
	}
	return maxCnt
}
```

## Ruby

```ruby
def max_vowels(s, k)
  n = s.length
  is_vowel = Array.new(256, false)
  [97, 101, 105, 111, 117].each { |c| is_vowel[c] = true } # a e i o u

  count = 0
  (0...k).each do |i|
    count += 1 if is_vowel[s.getbyte(i)]
  end
  max = count

  (k...n).each do |i|
    count += 1 if is_vowel[s.getbyte(i)]
    count -= 1 if is_vowel[s.getbyte(i - k)]
    max = count if count > max
  end

  max
end
```

## Scala

```scala
object Solution {
    def maxVowels(s: String, k: Int): Int = {
        val vowels = Set('a', 'e', 'i', 'o', 'u')
        var count = 0
        for (i <- 0 until k) {
            if (vowels.contains(s(i))) count += 1
        }
        var maxCount = count
        for (i <- k until s.length) {
            if (vowels.contains(s(i))) count += 1
            if (vowels.contains(s(i - k))) count -= 1
            if (count > maxCount) maxCount = count
        }
        maxCount
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_vowels(s: String, k: i32) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let k = k as usize;
        let mut cnt = 0usize;
        for i in 0..k {
            if is_vowel(bytes[i]) {
                cnt += 1;
            }
        }
        let mut max_cnt = cnt;
        for i in k..n {
            if is_vowel(bytes[i]) {
                cnt += 1;
            }
            if is_vowel(bytes[i - k]) {
                cnt -= 1;
            }
            if cnt > max_cnt {
                max_cnt = cnt;
            }
        }
        max_cnt as i32
    }
}

fn is_vowel(c: u8) -> bool {
    matches!(c, b'a' | b'e' | b'i' | b'o' | b'u')
}
```

## Racket

```racket
(define/contract (max-vowels s k)
  (-> string? exact-integer? exact-integer?)
  (let* ([n (string-length s)]
         [is-vowel (lambda (ch)
                     (or (char=? ch #\a) (char=? ch #\e) (char=? ch #\i)
                         (char=? ch #\o) (char=? ch #\u)))])
    ;; count vowels in the first window
    (let loop-first ((i 0) (cnt 0))
      (if (= i k)
          (let recur-slide ((idx k) (curr cnt) (best cnt))
            (if (= idx n)
                best
                (let* ([out-ch (string-ref s (- idx k))]
                       [in-ch  (string-ref s idx)]
                       [new-curr (+ curr
                                    (if (is-vowel in-ch) 1 0)
                                    (if (is-vowel out-ch) -1 0))])
                  (recur-slide (+ idx 1) new-curr (max best new-curr)))))
          (loop-first (+ i 1)
                      (+ cnt (if (is-vowel (string-ref s i)) 1 0)))))))
```

## Erlang

```erlang
-spec max_vowels(S :: unicode:unicode_binary(), K :: integer()) -> integer().
max_vowels(S, K) ->
    List = binary:bin_to_list(S),
    Cum = build_cum(List),
    Tail = lists:nthtail(K, Cum),
    max_diff(Tail, Cum, 0).

build_cum(List) ->
    build_cum(List, 0, []).

build_cum([], Sum, Acc) ->
    lists:reverse([Sum | Acc]);
build_cum([H|T], Sum, Acc) ->
    NewSum = Sum + (if is_vowel(H) -> 1; true -> 0 end),
    build_cum(T, NewSum, [Sum | Acc]).

max_diff([], _, Max) ->
    Max;
max_diff([C1|RestTail], [C2|RestHead], Max) ->
    Diff = C1 - C2,
    NewMax = if Diff > Max -> Diff; true -> Max end,
    max_diff(RestTail, RestHead, NewMax).

is_vowel(C) when C == $a; C == $e; C == $i; C == $o; C == $u ->
    true;
is_vowel(_) ->
    false.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_vowels(s :: String.t(), k :: integer) :: integer
  def max_vowels(s, k) do
    vowels = MapSet.new('aeiou')
    chars = :binary.bin_to_list(s)

    {max_cnt, _cur_cnt, _queue_state} =
      Enum.reduce(chars, {0, 0, {:queue.new(), 0}}, fn c,
                                                    {max_sofar, cur_cnt,
                                                     {q, qsize}} ->
        flag = if MapSet.member?(vowels, c), do: 1, else: 0
        new_q = :queue.in(flag, q)
        new_size = qsize + 1
        new_cur = cur_cnt + flag

        {final_q, final_size, final_cur} =
          if new_size > k do
            {{:value, old_flag}, q2} = :queue.out(new_q)
            {q2, new_size - 1, new_cur - old_flag}
          else
            {new_q, new_size, new_cur}
          end

        new_max = if final_cur > max_sofar, do: final_cur, else: max_sofar
        {new_max, final_cur, {final_q, final_size}}
      end)

    max_cnt
  end
end
```
