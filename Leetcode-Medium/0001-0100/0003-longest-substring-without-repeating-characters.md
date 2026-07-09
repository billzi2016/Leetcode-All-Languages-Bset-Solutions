# 0003. Longest Substring Without Repeating Characters

## Cpp

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> last(256, -1);
        int start = 0, maxLen = 0;
        for (int i = 0; i < (int)s.size(); ++i) {
            unsigned char c = s[i];
            if (last[c] >= start) {
                start = last[c] + 1;
            }
            last[c] = i;
            maxLen = max(maxLen, i - start + 1);
        }
        return maxLen;
    }
};
```

## Java

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        if (n == 0) return 0;
        int[] lastIdx = new int[256];
        java.util.Arrays.fill(lastIdx, -1);
        int maxLen = 0;
        int left = 0;
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (lastIdx[c] >= left) {
                left = lastIdx[c] + 1;
            }
            lastIdx[c] = i;
            maxLen = Math.max(maxLen, i - left + 1);
        }
        return maxLen;
    }
}
```

## Python

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}
        left = 0
        max_len = 0
        for right, ch in enumerate(s):
            if ch in char_index and char_index[ch] >= left:
                left = char_index[ch] + 1
            char_index[ch] = right
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
        return max_len
```

## Python3

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_idx = {}
        left = 0
        max_len = 0
        for right, ch in enumerate(s):
            if ch in last_idx and last_idx[ch] >= left:
                left = last_idx[ch] + 1
            last_idx[ch] = right
            cur_len = right - left + 1
            if cur_len > max_len:
                max_len = cur_len
        return max_len
```

## C

```c
int lengthOfLongestSubstring(char* s) {
    if (!s) return 0;
    int last[256];
    for (int i = 0; i < 256; ++i) last[i] = -1;
    int maxlen = 0, start = 0;
    for (int i = 0; s[i]; ++i) {
        unsigned char c = (unsigned char)s[i];
        if (last[c] >= start) start = last[c] + 1;
        last[c] = i;
        int cur = i - start + 1;
        if (cur > maxlen) maxlen = cur;
    }
    return maxlen;
}
```

## Csharp

```csharp
public class Solution {
    public int LengthOfLongestSubstring(string s) {
        var lastIndex = new Dictionary<char, int>();
        int maxLen = 0, start = 0;
        for (int i = 0; i < s.Length; i++) {
            char c = s[i];
            if (lastIndex.TryGetValue(c, out int prev) && prev >= start) {
                start = prev + 1;
            }
            lastIndex[c] = i;
            int curLen = i - start + 1;
            if (curLen > maxLen) maxLen = curLen;
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
var lengthOfLongestSubstring = function(s) {
    const n = s.length;
    let left = 0, maxLen = 0;
    const lastPos = new Map(); // character -> latest index
    
    for (let right = 0; right < n; ++right) {
        const ch = s[right];
        if (lastPos.has(ch) && lastPos.get(ch) >= left) {
            left = lastPos.get(ch) + 1;
        }
        lastPos.set(ch, right);
        maxLen = Math.max(maxLen, right - left + 1);
    }
    
    return maxLen;
};
```

## Typescript

```typescript
function lengthOfLongestSubstring(s: string): number {
    const n = s.length;
    let maxLen = 0;
    const lastPos = new Map<string, number>();
    let left = 0;
    for (let right = 0; right < n; right++) {
        const ch = s[right];
        if (lastPos.has(ch) && lastPos.get(ch)! >= left) {
            left = lastPos.get(ch)! + 1;
        }
        lastPos.set(ch, right);
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
    function lengthOfLongestSubstring($s) {
        $n = strlen($s);
        $charPos = [];
        $left = 0;
        $maxLen = 0;

        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if (isset($charPos[$c]) && $charPos[$c] >= $left) {
                $left = $charPos[$c] + 1;
            }
            $charPos[$c] = $i;
            $currentLen = $i - $left + 1;
            if ($currentLen > $maxLen) {
                $maxLen = $currentLen;
            }
        }

        return $maxLen;
    }
}
```

## Swift

```swift
class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        let chars = Array(s)
        var lastSeen = [Character: Int]()
        var left = 0
        var maxLen = 0
        
        for (right, ch) in chars.enumerated() {
            if let prev = lastSeen[ch], prev >= left {
                left = prev + 1
            }
            lastSeen[ch] = right
            maxLen = max(maxLen, right - left + 1)
        }
        
        return maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun lengthOfLongestSubstring(s: String): Int {
        val lastPos = IntArray(128) { -1 }
        var left = 0
        var maxLen = 0
        for (right in s.indices) {
            val idx = s[right].code
            if (lastPos[idx] >= left) {
                left = lastPos[idx] + 1
            }
            lastPos[idx] = right
            val curLen = right - left + 1
            if (curLen > maxLen) maxLen = curLen
        }
        return maxLen
    }
}
```

## Dart

```dart
class Solution {
  int lengthOfLongestSubstring(String s) {
    Map<String, int> lastSeen = {};
    int maxLen = 0;
    int start = 0;

    for (int i = 0; i < s.length; i++) {
      String ch = s[i];
      if (lastSeen.containsKey(ch) && lastSeen[ch]! >= start) {
        start = lastSeen[ch]! + 1;
      }
      lastSeen[ch] = i;
      int curLen = i - start + 1;
      if (curLen > maxLen) {
        maxLen = curLen;
      }
    }

    return maxLen;
  }
}
```

## Golang

```go
func lengthOfLongestSubstring(s string) int {
	n := len(s)
	if n == 0 {
		return 0
	}
	last := make([]int, 256)
	for i := range last {
		last[i] = -1
	}
	maxLen, start := 0, 0
	for i := 0; i < n; i++ {
		c := s[i]
		if last[c] >= start {
			start = last[c] + 1
		}
		last[c] = i
		if cur := i - start + 1; cur > maxLen {
			maxLen = cur
		}
	}
	return maxLen
}
```

## Ruby

```ruby
# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
  last_index = {}
  max_len = 0
  start = 0

  s.each_char.with_index do |ch, i|
    if last_index.key?(ch) && last_index[ch] >= start
      start = last_index[ch] + 1
    end
    last_index[ch] = i
    cur_len = i - start + 1
    max_len = cur_len if cur_len > max_len
  end

  max_len
end
```

## Scala

```scala
object Solution {
    def lengthOfLongestSubstring(s: String): Int = {
        val lastPos = scala.collection.mutable.Map[Char, Int]()
        var maxLen = 0
        var left = 0
        for (right <- s.indices) {
            val c = s(right)
            if (lastPos.contains(c) && lastPos(c) >= left) {
                left = lastPos(c) + 1
            }
            lastPos(c) = right
            maxLen = math.max(maxLen, right - left + 1)
        }
        maxLen
    }
}
```

## Rust

```rust
impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        use std::collections::HashMap;
        let mut last_pos: HashMap<char, usize> = HashMap::new();
        let mut left = 0usize;
        let mut max_len = 0usize;

        for (right, ch) in s.chars().enumerate() {
            if let Some(&prev) = last_pos.get(&ch) {
                if prev > left {
                    left = prev;
                }
            }
            let cur_len = right - left + 1;
            if cur_len > max_len {
                max_len = cur_len;
            }
            // store the index after current character to simplify next comparison
            last_pos.insert(ch, right + 1);
        }

        max_len as i32
    }
}
```

## Racket

```racket
(define/contract (length-of-longest-substring s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (ht (make-hash))
         (left 0)
         (maxlen 0))
    (for ([right (in-range n)])
      (define c (string-ref s right))
      (define prev (hash-ref ht c #f))
      (when (and prev (> prev left))
        (set! left prev))
      (hash-set! ht c (+ right 1))
      (define cur (- (+ right 1) left))
      (when (> cur maxlen)
        (set! maxlen cur)))
    maxlen))
```

## Erlang

```erlang
-module(solution).
-export([length_of_longest_substring/1]).

-spec length_of_longest_substring(S :: unicode:unicode_binary()) -> integer().
length_of_longest_substring(S) ->
    Chars = unicode:characters_to_list(S),
    longest(Chars, 0, #{}, 0, 0).

longest([], _Idx, _Map, _Start, Max) ->
    Max;
longest([C|Rest], Idx, Map, Start, Max) ->
    case maps:find(C, Map) of
        {ok, Pos} when Pos >= Start ->
            NewStart = Pos + 1,
            UpdatedMap = maps:put(C, Idx, Map),
            NewMax = max(Max, Idx - NewStart + 1),
            longest(Rest, Idx + 1, UpdatedMap, NewStart, NewMax);
        _ ->
            UpdatedMap = maps:put(C, Idx, Map),
            NewMax = max(Max, Idx - Start + 1),
            longest(Rest, Idx + 1, UpdatedMap, Start, NewMax)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec length_of_longest_substring(s :: String.t()) :: integer()
  def length_of_longest_substring(s) do
    chars = String.graphemes(s)

    {max_len, _start, _map} =
      Enum.reduce(Enum.with_index(chars), {0, 0, %{}}, fn {c, i},
                                                      {max_len, start, last_pos} ->
        last_index = Map.get(last_pos, c, -1)
        new_start = if last_index >= start, do: last_index + 1, else: start
        len = i - new_start + 1
        new_max = max(max_len, len)
        new_map = Map.put(last_pos, c, i)
        {new_max, new_start, new_map}
      end)

    max_len
  end
end
```
