# 3090. Maximum Length Substring With Two Occurrences

## Cpp

```cpp
class Solution {
public:
    int maximumLengthSubstring(string s) {
        int n = s.size();
        for (int len = n / 2; len >= 1; --len) {
            for (int i = 0; i + len <= n; ++i) {
                for (int j = i + len; j + len <= n; ++j) { // ensure non‑overlapping
                    if (s.compare(i, len, s, j, len) == 0) {
                        return len;
                    }
                }
            }
        }
        return 0;
    }
};
```

## Java

```java
class Solution {
    public int maximumLengthSubstring(String s) {
        int n = s.length();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                String sub = s.substring(i, j + 1);
                int len = sub.length();
                if (s.indexOf(sub, i + len) != -1) {
                    ans = Math.max(ans, len);
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
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        max_len = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                sub = s[i:j]
                # Look for another occurrence starting after position i
                if s.find(sub, i + 1) != -1:
                    max_len = max(max_len, j - i)
        return max_len
```

## Python3

```python
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                sub = s[i:j]
                if s.count(sub) >= 2:
                    ans = max(ans, j - i)
        return ans
```

## C

```c
#include <string.h>

int maximumLengthSubstring(char* s) {
    int n = (int)strlen(s);
    int maxLen = 0;
    for (int i = 0; i < n; ++i) {
        int freq[26] = {0};
        for (int j = i; j < n; ++j) {
            int idx = s[j] - 'a';
            if (++freq[idx] > 2) break;
            int curLen = j - i + 1;
            if (curLen > maxLen) maxLen = curLen;
        }
    }
    return maxLen;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumLengthSubstring(string s) {
        int n = s.Length;
        int maxLen = 0;
        for (int i = 0; i < n; i++) {
            int[] cnt = new int[26];
            for (int j = i; j < n; j++) {
                int idx = s[j] - 'a';
                cnt[idx]++;
                if (cnt[idx] > 2) break;
                maxLen = Math.Max(maxLen, j - i + 1);
            }
        }
        return maxLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maximumLengthSubstring = function(s) {
    const n = s.length;
    for (let len = n - 1; len >= 1; len--) {
        for (let i = 0; i + len <= n; i++) {
            const sub = s.substring(i, i + len);
            if (s.indexOf(sub, i + len) !== -1) {
                return len;
            }
        }
    }
    return 0;
};
```

## Typescript

```typescript
function maximumLengthSubstring(s: string): number {
    const freq = new Array(26).fill(0);
    let left = 0;
    let maxLen = 0;
    for (let right = 0; right < s.length; ++right) {
        const rIdx = s.charCodeAt(right) - 97;
        freq[rIdx]++;
        while (freq[rIdx] > 2) {
            const lIdx = s.charCodeAt(left) - 97;
            freq[lIdx]--;
            left++;
        }
        maxLen = Math.max(maxLen, right - left + 1);
    }
    return maxLen;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function maximumLengthSubstring($s) {
        $n = strlen($s);
        $maxLen = 0;
        for ($len = 1; $len <= $n - 1; $len++) {
            for ($i = 0; $i + $len <= $n; $i++) {
                $sub = substr($s, $i, $len);
                // Look for a second occurrence that does not overlap with the first one
                $pos = strpos($s, $sub, $i + $len);
                if ($pos !== false) {
                    if ($len > $maxLen) {
                        $maxLen = $len;
                    }
                    break; // No need to check other start positions for this length
                }
            }
        }
        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func maximumLengthSubstring(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var maxLen = 0
        
        for i in 0..<n {
            for j in (i + 1)...n {
                let len = j - i
                if len <= maxLen { continue }
                
                var found = false
                // try all other start positions k
                for k in 0..<(n - len + 1) where k != i {
                    // ensure non‑overlapping occurrences
                    if !(k + len <= i || i + len <= k) { continue }
                    
                    var match = true
                    for t in 0..<len {
                        if chars[i + t] != chars[k + t] {
                            match = false
                            break
                        }
                    }
                    if match {
                        found = true
                        break
                    }
                }
                
                if found {
                    maxLen = len
                }
            }
        }
        
        return maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumLengthSubstring(s: String): Int {
        val n = s.length
        var ans = 0
        for (i in 0 until n) {
            for (j in i + 1..n) {
                val len = j - i
                if (len <= ans) continue
                val sub = s.substring(i, j)
                var cnt = 0
                var k = 0
                while (k + len <= n) {
                    if (s.regionMatches(k, sub, 0, len)) {
                        cnt++
                        if (cnt >= 2) break
                    }
                    k++
                }
                if (cnt >= 2) ans = len
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maximumLengthSubstring(String s) {
    int n = s.length;
    for (int len = n - 1; len >= 1; len--) {
      Map<String, int> firstPos = {};
      for (int i = 0; i + len <= n; i++) {
        String sub = s.substring(i, i + len);
        if (firstPos.containsKey(sub)) {
          int prev = firstPos[sub]!;
          if (i - prev >= len) return len;
        } else {
          firstPos[sub] = i;
        }
      }
    }
    return -1;
  }
}
```

## Golang

```go
func maximumLengthSubstring(s string) int {
    n := len(s)
    maxLen := 0
    for l := 1; l <= n-1; l++ {
        seen := make(map[string]int)
        for i := 0; i+l <= n; i++ {
            sub := s[i : i+l]
            if first, ok := seen[sub]; ok {
                if i-first >= l && l > maxLen {
                    maxLen = l
                }
            } else {
                seen[sub] = i
            }
        }
    }
    return maxLen
}
```

## Ruby

```ruby
def maximum_length_substring(s)
  n = s.length
  max_len = 0
  (1...n).each do |len|
    (0..(n - len)).each do |i|
      sub = s[i, len]
      j_start = i + len
      while j_start <= n - len
        if s[j_start, len] == sub
          max_len = len if len > max_len
          break
        end
        j_start += 1
      end
    end
  end
  max_len
end
```

## Scala

```scala
object Solution {
    def maximumLengthSubstring(s: String): Int = {
        val n = s.length
        var ans = 0
        for (len <- 1 to n) {
            val firstPos = scala.collection.mutable.Map[String, Int]()
            var i = 0
            while (i + len <= n) {
                val sub = s.substring(i, i + len)
                firstPos.get(sub) match {
                    case Some(prev) =>
                        if (i - prev >= len) {
                            ans = math.max(ans, len)
                        }
                    case None =>
                        firstPos.put(sub, i)
                }
                i += 1
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_length_substring(s: String) -> i32 {
        let n = s.len();
        // iterate lengths from largest to smallest
        for len in (1..=n).rev() {
            use std::collections::HashMap;
            let mut cnt: HashMap<String, i32> = HashMap::new();
            for i in 0..=n - len {
                // safe because s contains only lowercase ASCII letters
                let sub = s[i..i + len].to_string();
                *cnt.entry(sub).or_insert(0) += 1;
            }
            if cnt.values().any(|&c| c >= 2) {
                return len as i32;
            }
        }
        0
    }
}
```

## Racket

```racket
(define/contract (maximum-length-substring s)
  (-> string? exact-integer?)
  (let ((n (string-length s)))
    (let loop ((len (- n 1))) ; maximum possible length with two occurrences
      (if (= len 0)
          0
          (let ((seen (make-hash))
                (found #f))
            (let inner ((i 0) (found found))
              (cond
                [found len]
                [(> i (- n len)) (loop (- len 1))]
                [else
                 (let ((sub (substring s i (+ i len))))
                   (if (hash-has-key? seen sub)
                       (inner (+ i 1) #t)
                       (begin
                         (hash-set! seen sub #t)
                         (inner (+ i 1) #f))))])))))))
```

## Erlang

```erlang
-spec maximum_length_substring(S :: unicode:unicode_binary()) -> integer().
maximum_length_substring(S) ->
    N = byte_size(S),
    find_max(N, S).

find_max(0, _S) -> 0;
find_max(Len, S) when Len > 0 ->
    case has_two_occurrences(Len, S) of
        true -> Len;
        false -> find_max(Len - 1, S)
    end.

has_two_occurrences(Len, S) ->
    N = byte_size(S),
    MaxStart = N - Len,
    check_positions(0, MaxStart, Len, S, #{}).

check_positions(I, MaxI, _Len, _S, _Map) when I > MaxI -> false;
check_positions(I, MaxI, Len, S, Map) ->
    Sub = binary:part(S, I, Len),
    case maps:get(Sub, Map, undefined) of
        undefined ->
            NewMap = maps:put(Sub, I, Map),
            check_positions(I + 1, MaxI, Len, S, NewMap);
        PrevIdx ->
            if
                I - PrevIdx >= Len -> true;
                true ->
                    Earliest = min(PrevIdx, I),
                    NewMap = maps:put(Sub, Earliest, Map),
                    check_positions(I + 1, MaxI, Len, S, NewMap)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_length_substring(s :: String.t()) :: integer()
  def maximum_length_substring(s) do
    len = String.length(s)

    Enum.reduce_while((len - 1)..1, 0, fn l, _acc ->
      found =
        0..(len - l)
        |> Enum.reduce_while(MapSet.new(), fn i, set ->
          sub = String.slice(s, i, l)

          if MapSet.member?(set, sub) do
            {:halt, true}
          else
            {:cont, MapSet.put(set, sub)}
          end
        end)

      case found do
        true -> {:halt, l}
        false -> {:cont, 0}
      end
    end)
  end
end
```
