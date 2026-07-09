# 1400. Construct K Palindrome Strings

## Cpp

```cpp
class Solution {
public:
    bool canConstruct(string s, int k) {
        if (s.size() < k) return false;
        int freq[26] = {0};
        for (char c : s) ++freq[c - 'a'];
        int odd = 0;
        for (int i = 0; i < 26; ++i)
            if (freq[i] & 1) ++odd;
        return odd <= k;
    }
};
```

## Java

```java
class Solution {
    public boolean canConstruct(String s, int k) {
        if (s.length() < k) return false;
        int[] freq = new int[26];
        for (int i = 0; i < s.length(); i++) {
            freq[s.charAt(i) - 'a']++;
        }
        int oddCount = 0;
        for (int cnt : freq) {
            if ((cnt & 1) == 1) oddCount++;
        }
        return oddCount <= k;
    }
}
```

## Python

```python
class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        n = len(s)
        if n < k:
            return False
        # count characters with odd frequency
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] ^= 1  # toggle parity
        odd_count = sum(freq)
        return odd_count <= k
```

## Python3

```python
import collections

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        odd = sum(v & 1 for v in collections.Counter(s).values())
        return odd <= k
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool canConstruct(char* s, int k) {
    int n = strlen(s);
    if (n < k) return false;
    
    int freq[26] = {0};
    for (int i = 0; s[i]; ++i) {
        freq[s[i] - 'a']++;
    }
    
    int odd = 0;
    for (int i = 0; i < 26; ++i) {
        if (freq[i] & 1) odd++;
    }
    
    return odd <= k;
}
```

## Csharp

```csharp
public class Solution
{
    public bool CanConstruct(string s, int k)
    {
        if (s.Length < k) return false;

        int[] freq = new int[26];
        foreach (char c in s)
        {
            freq[c - 'a']++;
        }

        int oddCount = 0;
        foreach (int cnt in freq)
        {
            if ((cnt & 1) == 1) oddCount++;
        }

        return oddCount <= k;
    }
}
```

## Javascript

```javascript
var canConstruct = function(s, k) {
    if (s.length < k) return false;
    const freq = new Array(26).fill(0);
    for (let i = 0; i < s.length; i++) {
        freq[s.charCodeAt(i) - 97]++;
    }
    let oddCount = 0;
    for (const cnt of freq) {
        if (cnt % 2 === 1) oddCount++;
    }
    return oddCount <= k;
};
```

## Typescript

```typescript
function canConstruct(s: string, k: number): boolean {
    const n = s.length;
    if (k > n) return false;

    const freq = new Array(26).fill(0);
    for (let i = 0; i < n; i++) {
        freq[s.charCodeAt(i) - 97]++;
    }

    let oddCount = 0;
    for (const cnt of freq) {
        if (cnt % 2 === 1) oddCount++;
    }

    return oddCount <= k;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Boolean
     */
    function canConstruct($s, $k) {
        $n = strlen($s);
        if ($n < $k) {
            return false;
        }
        $freq = array_fill(0, 26, 0);
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - 97; // 'a' ASCII is 97
            $freq[$idx]++;
        }
        $oddCount = 0;
        foreach ($freq as $cnt) {
            if ($cnt & 1) {
                $oddCount++;
            }
        }
        return $oddCount <= $k;
    }
}
```

## Swift

```swift
class Solution {
    func canConstruct(_ s: String, _ k: Int) -> Bool {
        let n = s.count
        if n < k { return false }
        var freq = [Int](repeating: 0, count: 26)
        for byte in s.utf8 {
            let idx = Int(byte - 97) // 'a' ascii is 97
            if idx >= 0 && idx < 26 {
                freq[idx] += 1
            }
        }
        var oddCount = 0
        for count in freq where count % 2 == 1 {
            oddCount += 1
        }
        return oddCount <= k
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canConstruct(s: String, k: Int): Boolean {
        if (s.length < k) return false
        val freq = IntArray(26)
        for (ch in s) {
            freq[ch - 'a']++
        }
        var oddCount = 0
        for (cnt in freq) {
            if ((cnt and 1) == 1) oddCount++
        }
        return oddCount <= k
    }
}
```

## Dart

```dart
class Solution {
  bool canConstruct(String s, int k) {
    if (s.length < k) return false;
    List<int> freq = List.filled(26, 0);
    for (int i = 0; i < s.length; i++) {
      freq[s.codeUnitAt(i) - 97]++;
    }
    int oddCount = 0;
    for (int cnt in freq) {
      if ((cnt & 1) == 1) oddCount++;
    }
    return oddCount <= k;
  }
}
```

## Golang

```go
func canConstruct(s string, k int) bool {
	if len(s) < k {
		return false
	}
	var freq [26]int
	for i := 0; i < len(s); i++ {
		freq[s[i]-'a']++
	}
	oddCount := 0
	for _, v := range freq[:] {
		if v%2 == 1 {
			oddCount++
		}
	}
	return oddCount <= k
}
```

## Ruby

```ruby
def can_construct(s, k)
  return false if s.length < k
  freq = Array.new(26, 0)
  s.each_byte { |b| freq[b - 97] += 1 }
  odd = freq.count { |c| c.odd? }
  odd <= k
end
```

## Scala

```scala
object Solution {
    def canConstruct(s: String, k: Int): Boolean = {
        if (s.length < k) return false
        val freq = new Array[Int](26)
        for (ch <- s) {
            freq(ch - 'a') += 1
        }
        var oddCount = 0
        for (cnt <- freq) {
            if ((cnt & 1) == 1) oddCount += 1
        }
        oddCount <= k
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_construct(s: String, k: i32) -> bool {
        let n = s.len();
        if n < k as usize {
            return false;
        }
        let mut freq = [0i32; 26];
        for b in s.bytes() {
            freq[(b - b'a') as usize] += 1;
        }
        let odd_cnt = freq.iter().filter(|&&c| c % 2 == 1).count();
        odd_cnt <= k as usize
    }
}
```

## Racket

```racket
(define/contract (can-construct s k)
  (-> string? exact-integer? boolean?)
  (let ((n (string-length s)))
    (if (< n k)
        #f
        (let ((freq (make-vector 26 0)))
          (for ([ch (in-string s)])
            (define idx (- (char->integer ch) (char->integer #\a)))
            (vector-set! freq idx (+ 1 (vector-ref freq idx))))
          (define odd-count
            (let loop ((i 0) (cnt 0))
              (if (= i 26)
                  cnt
                  (loop (+ i 1)
                        (if (odd? (vector-ref freq i)) (+ cnt 1) cnt)))))
          (<= odd-count k)))) )
```

## Erlang

```erlang
-spec can_construct(S :: unicode:unicode_binary(), K :: integer()) -> boolean().
can_construct(S, K) ->
    Len = byte_size(S),
    if
        Len < K -> false;
        true ->
            Mask = toggle_bits(S, 0),
            OddCount = count_ones(Mask),
            OddCount =< K
    end.

toggle_bits(<<>>, Mask) -> Mask;
toggle_bits(<<C, Rest/binary>>, Mask) ->
    Index = C - $a,
    NewMask = Mask bxor (1 bsl Index),
    toggle_bits(Rest, NewMask).

count_ones(N) -> count_ones(N, 0).
count_ones(0, Acc) -> Acc;
count_ones(N, Acc) ->
    count_ones(N band (N - 1), Acc + 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec can_construct(s :: String.t(), k :: integer) :: boolean
  def can_construct(s, k) do
    n = String.length(s)

    if n < k do
      false
    else
      mask =
        Enum.reduce(String.to_charlist(s), 0, fn ch, acc ->
          Bitwise.bxor(acc, 1 <<< (ch - ?a))
        end)

      odd_count =
        Enum.reduce(0..25, 0, fn i, cnt ->
          if Bitwise.band(mask, 1 <<< i) != 0 do
            cnt + 1
          else
            cnt
          end
        end)

      odd_count <= k
    end
  end
end
```
