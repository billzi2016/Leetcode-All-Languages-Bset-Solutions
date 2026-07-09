# 0467. Unique Substrings in Wraparound String

## Cpp

```cpp
class Solution {
public:
    int findSubstringInWraproundString(string s) {
        if (s.empty()) return 0;
        vector<int> maxLen(26, 0);
        int cur = 0;
        for (int i = 0; i < (int)s.size(); ++i) {
            if (i > 0 && ((s[i] - s[i-1] == 1) || (s[i-1] == 'z' && s[i] == 'a')))
                ++cur;
            else
                cur = 1;
            int idx = s[i] - 'a';
            maxLen[idx] = max(maxLen[idx], cur);
        }
        int ans = 0;
        for (int len : maxLen) ans += len;
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int findSubstringInWraproundString(String s) {
        if (s == null || s.isEmpty()) return 0;
        int[] maxLen = new int[26];
        int curLen = 0;
        for (int i = 0; i < s.length(); i++) {
            if (i > 0 && ( (s.charAt(i) - s.charAt(i - 1) + 26) % 26 == 1 )) {
                curLen++;
            } else {
                curLen = 1;
            }
            int idx = s.charAt(i) - 'a';
            if (curLen > maxLen[idx]) {
                maxLen[idx] = curLen;
            }
        }
        int total = 0;
        for (int len : maxLen) total += len;
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def findSubstringInWraproundString(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [0] * 26  # max length of valid substring ending with each character
        cur_len = 0
        for i, ch in enumerate(s):
            if i > 0 and (ord(ch) - ord(s[i - 1]) == 1 or (s[i - 1] == 'z' and ch == 'a')):
                cur_len += 1
            else:
                cur_len = 1
            idx = ord(ch) - ord('a')
            if cur_len > dp[idx]:
                dp[idx] = cur_len
        return sum(dp)
```

## Python3

```python
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        dp = [0] * 26  # max length of valid substring ending with each letter
        cur_len = 0
        for i, ch in enumerate(s):
            if i > 0 and (ord(ch) - ord(s[i - 1]) == 1 or (s[i - 1] == 'z' and ch == 'a')):
                cur_len += 1
            else:
                cur_len = 1
            idx = ord(ch) - ord('a')
            if cur_len > dp[idx]:
                dp[idx] = cur_len
        return sum(dp)
```

## C

```c
int findSubstringInWraproundString(char* s) {
    int dp[26] = {0};
    int cur = 0;
    for (int i = 0; s[i]; ++i) {
        if (i > 0 && ((s[i] - s[i-1] == 1) || (s[i-1] == 'z' && s[i] == 'a'))) {
            ++cur;
        } else {
            cur = 1;
        }
        int idx = s[i] - 'a';
        if (cur > dp[idx]) dp[idx] = cur;
    }
    int ans = 0;
    for (int i = 0; i < 26; ++i) ans += dp[i];
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindSubstringInWraproundString(string s)
    {
        if (string.IsNullOrEmpty(s)) return 0;

        int[] maxLenEndingWith = new int[26];
        int curLen = 0;

        for (int i = 0; i < s.Length; i++)
        {
            if (i > 0 && ((s[i] - s[i - 1] + 26) % 26) == 1)
                curLen++;
            else
                curLen = 1;

            int idx = s[i] - 'a';
            if (curLen > maxLenEndingWith[idx])
                maxLenEndingWith[idx] = curLen;
        }

        int result = 0;
        foreach (int len in maxLenEndingWith)
            result += len;

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var findSubstringInWraproundString = function(s) {
    const dp = new Array(26).fill(0);
    let cur = 0;
    for (let i = 0; i < s.length; i++) {
        if (i > 0 && ((s.charCodeAt(i) - s.charCodeAt(i - 1) + 26) % 26 === 1)) {
            cur += 1;
        } else {
            cur = 1;
        }
        const idx = s.charCodeAt(i) - 97;
        dp[idx] = Math.max(dp[idx], cur);
    }
    return dp.reduce((sum, val) => sum + val, 0);
};
```

## Typescript

```typescript
function findSubstringInWraproundString(s: string): number {
    const maxLen = new Array(26).fill(0);
    let cur = 0;
    for (let i = 0; i < s.length; ++i) {
        if (i > 0 && ((s.charCodeAt(i) - s.charCodeAt(i - 1) + 26) % 26 === 1)) {
            cur += 1;
        } else {
            cur = 1;
        }
        const idx = s.charCodeAt(i) - 97;
        if (cur > maxLen[idx]) {
            maxLen[idx] = cur;
        }
    }
    return maxLen.reduce((sum, v) => sum + v, 0);
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function findSubstringInWraproundString($s) {
        $n = strlen($s);
        if ($n == 0) return 0;

        $maxLen = array_fill(0, 26, 0);
        $cur = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($i > 0 && ( (ord($s[$i]) - ord($s[$i-1]) + 26) % 26 == 1 )) {
                $cur += 1;
            } else {
                $cur = 1;
            }
            $idx = ord($s[$i]) - ord('a');
            if ($cur > $maxLen[$idx]) {
                $maxLen[$idx] = $cur;
            }
        }

        return array_sum($maxLen);
    }
}
```

## Swift

```swift
class Solution {
    func findSubstringInWraproundString(_ s: String) -> Int {
        let bytes = Array(s.utf8)
        var maxLen = [Int](repeating: 0, count: 26)
        var cur = 0
        
        for i in 0..<bytes.count {
            if i > 0 && (bytes[i] == bytes[i - 1] + 1 || (bytes[i - 1] == 122 && bytes[i] == 97)) {
                cur += 1
            } else {
                cur = 1
            }
            let idx = Int(bytes[i] - 97)
            if cur > maxLen[idx] {
                maxLen[idx] = cur
            }
        }
        
        return maxLen.reduce(0, +)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findSubstringInWraproundString(s: String): Int {
        if (s.isEmpty()) return 0
        val maxLenEnding = IntArray(26)
        var curLen = 0
        for (i in s.indices) {
            if (i > 0 && ((s[i] - s[i - 1] + 26) % 26 == 1)) {
                curLen += 1
            } else {
                curLen = 1
            }
            val idx = s[i] - 'a'
            if (curLen > maxLenEnding[idx]) {
                maxLenEnding[idx] = curLen
            }
        }
        var result = 0
        for (len in maxLenEnding) {
            result += len
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  int findSubstringInWraproundString(String s) {
    if (s.isEmpty) return 0;
    List<int> dp = List.filled(26, 0);
    int cur = 0;
    for (int i = 0; i < s.length; i++) {
      if (i > 0 &&
          ((s.codeUnitAt(i) - s.codeUnitAt(i - 1) + 26) % 26) == 1) {
        cur += 1;
      } else {
        cur = 1;
      }
      int idx = s.codeUnitAt(i) - 97; // 'a' ASCII code
      if (cur > dp[idx]) dp[idx] = cur;
    }
    int ans = 0;
    for (int v in dp) ans += v;
    return ans;
  }
}
```

## Golang

```go
func findSubstringInWraproundString(s string) int {
	if len(s) == 0 {
		return 0
	}
	maxLen := make([]int, 26)
	cur := 0
	for i := 0; i < len(s); i++ {
		if i > 0 && (s[i]-s[i-1]+26)%26 == 1 {
			cur++
		} else {
			cur = 1
		}
		idx := s[i] - 'a'
		if cur > maxLen[idx] {
			maxLen[idx] = cur
		}
	}
	sum := 0
	for _, v := range maxLen {
		sum += v
	}
	return sum
}
```

## Ruby

```ruby
def find_substring_in_wrapround_string(s)
  dp = Array.new(26, 0)
  cur_len = 0
  (0...s.length).each do |i|
    if i > 0 && ((s[i].ord - s[i - 1].ord) % 26 == 1)
      cur_len += 1
    else
      cur_len = 1
    end
    idx = s[i].ord - 97
    dp[idx] = cur_len if cur_len > dp[idx]
  end
  dp.sum
end
```

## Scala

```scala
object Solution {
    def findSubstringInWraproundString(s: String): Int = {
        val maxLen = Array.fill(26)(0)
        var cur = 0
        for (i <- s.indices) {
            if (i > 0 && ((s(i) - s(i - 1) + 26) % 26 == 1)) {
                cur += 1
            } else {
                cur = 1
            }
            val idx = s(i) - 'a'
            maxLen(idx) = math.max(maxLen(idx), cur)
        }
        maxLen.sum
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_substring_in_wrapround_string(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut dp = [0i32; 26];
        let mut cur_len = 0i32;
        for i in 0..bytes.len() {
            if i > 0 && ((bytes[i] == b'a' && bytes[i - 1] == b'z') || (bytes[i] == bytes[i - 1] + 1)) {
                cur_len += 1;
            } else {
                cur_len = 1;
            }
            let idx = (bytes[i] - b'a') as usize;
            if dp[idx] < cur_len {
                dp[idx] = cur_len;
            }
        }
        dp.iter().sum()
    }
}
```

## Racket

```racket
(define/contract (find-substring-in-wrapround-string s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (dp (make-vector 26 0))
         (cur-len 0))
    (for ([i (in-range n)])
      (let* ((c (string-ref s i))
             (idx (- (char->integer c) (char->integer #\a))))
        (if (and (> i 0)
                 (let ((prev (string-ref s (- i 1))))
                   (or (= (- (char->integer c) (char->integer prev)) 1)
                       (and (eq? prev #\z) (eq? c #\a)))))
            (set! cur-len (+ cur-len 1))
            (set! cur-len 1))
        (vector-set! dp idx (max (vector-ref dp idx) cur-len))))
    (let loop ((i 0) (sum 0))
      (if (= i 26)
          sum
          (loop (+ i 1) (+ sum (vector-ref dp i)))))))
```

## Erlang

```erlang
-module(solution).
-export([find_substring_in_wrapround_string/1]).

-spec find_substring_in_wrapround_string(S :: unicode:unicode_binary()) -> integer().
find_substring_in_wrapround_string(S) ->
    Bytes = binary_to_list(S),
    MaxTuple0 = erlang:make_tuple(26, 0),
    FinalTuple = loop(Bytes, undefined, 0, MaxTuple0),
    lists:sum(tuple_to_list(FinalTuple)).

loop([], _Prev, _CurrLen, MaxTuple) ->
    MaxTuple;
loop([C|Rest], Prev, CurrLen, MaxTuple) ->
    NewCurrLen =
        case Prev of
            undefined -> 1;
            _ when ((Prev + 1) rem 26) =:= C -> CurrLen + 1;
            _ -> 1
        end,
    Index = C - $a + 1,
    Existing = element(Index, MaxTuple),
    UpdatedMax = if NewCurrLen > Existing -> NewCurrLen; true -> Existing end,
    NewTuple = setelement(Index, MaxTuple, UpdatedMax),
    loop(Rest, C, NewCurrLen, NewTuple).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_substring_in_wrapround_string(String.t()) :: integer()
  def find_substring_in_wrapround_string(s) do
    bytes = :binary.bin_to_list(s)

    dp_initial = :erlang.make_tuple(26, 0)

    {_prev, _len, dp_final} =
      Enum.reduce(bytes, {nil, 0, dp_initial}, fn byte, {prev, cur_len, acc_dp} ->
        new_len =
          if prev != nil and
               ((byte - prev == 1) or (prev == ?z and byte == ?a)) do
            cur_len + 1
          else
            1
          end

        idx = byte - ?a
        existing = elem(acc_dp, idx + 1)

        updated_dp =
          if new_len > existing do
            put_elem(acc_dp, idx + 1, new_len)
          else
            acc_dp
          end

        {byte, new_len, updated_dp}
      end)

    Enum.reduce(1..26, 0, fn i, sum -> sum + elem(dp_final, i) end)
  end
end
```
