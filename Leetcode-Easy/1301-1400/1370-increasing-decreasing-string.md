# 1370. Increasing Decreasing String

## Cpp

```cpp
class Solution {
public:
    string sortString(string s) {
        int cnt[26] = {0};
        for (char c : s) cnt[c - 'a']++;
        string res;
        res.reserve(s.size());
        while ((int)res.size() < (int)s.size()) {
            // increasing
            for (int i = 0; i < 26; ++i) {
                if (cnt[i] > 0) {
                    res.push_back('a' + i);
                    --cnt[i];
                }
            }
            // decreasing
            for (int i = 25; i >= 0; --i) {
                if (cnt[i] > 0) {
                    res.push_back('a' + i);
                    --cnt[i];
                }
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String sortString(String s) {
        int[] cnt = new int[26];
        for (char c : s.toCharArray()) {
            cnt[c - 'a']++;
        }
        StringBuilder sb = new StringBuilder(s.length());
        int total = s.length();
        while (sb.length() < total) {
            // ascending
            for (int i = 0; i < 26; i++) {
                if (cnt[i] > 0) {
                    sb.append((char) ('a' + i));
                    cnt[i]--;
                }
            }
            // descending
            for (int i = 25; i >= 0; i--) {
                if (cnt[i] > 0) {
                    sb.append((char) ('a' + i));
                    cnt[i]--;
                }
            }
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        res = []
        n = len(s)
        while len(res) < n:
            for i in range(26):
                if cnt[i]:
                    res.append(chr(i + ord('a')))
                    cnt[i] -= 1
            for i in range(25, -1, -1):
                if cnt[i]:
                    res.append(chr(i + ord('a')))
                    cnt[i] -= 1
        return ''.join(res)
```

## Python3

```python
class Solution:
    def sortString(self, s: str) -> str:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        res = []
        total = len(s)
        while len(res) < total:
            # increasing order
            for i in range(26):
                if cnt[i]:
                    res.append(chr(i + ord('a')))
                    cnt[i] -= 1
            # decreasing order
            for i in range(25, -1, -1):
                if cnt[i]:
                    res.append(chr(i + ord('a')))
                    cnt[i] -= 1
        return ''.join(res)
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* sortString(char* s) {
    int freq[26] = {0};
    int n = strlen(s);
    for (int i = 0; i < n; ++i) {
        freq[s[i] - 'a']++;
    }
    
    char *res = (char *)malloc(n + 1);
    int pos = 0;
    while (pos < n) {
        for (int i = 0; i < 26; ++i) {
            if (freq[i] > 0) {
                res[pos++] = 'a' + i;
                freq[i]--;
            }
        }
        for (int i = 25; i >= 0; --i) {
            if (freq[i] > 0) {
                res[pos++] = 'a' + i;
                freq[i]--;
            }
        }
    }
    res[n] = '\0';
    return res;
}
```

## Csharp

```csharp
using System.Text;

public class Solution {
    public string SortString(string s) {
        int[] cnt = new int[26];
        foreach (char ch in s) {
            cnt[ch - 'a']++;
        }
        StringBuilder sb = new StringBuilder(s.Length);
        int total = s.Length;
        while (sb.Length < total) {
            for (int i = 0; i < 26; i++) {
                if (cnt[i] > 0) {
                    sb.Append((char)('a' + i));
                    cnt[i]--;
                }
            }
            for (int i = 25; i >= 0; i--) {
                if (cnt[i] > 0) {
                    sb.append((char)('a' + i));
                    cnt[i]--;
                }
            }
        }
        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var sortString = function(s) {
    const cnt = new Array(26).fill(0);
    for (let i = 0; i < s.length; ++i) {
        cnt[s.charCodeAt(i) - 97]++;
    }
    const res = [];
    const n = s.length;
    while (res.length < n) {
        // ascend
        for (let i = 0; i < 26; ++i) {
            if (cnt[i] > 0) {
                res.push(String.fromCharCode(i + 97));
                cnt[i]--;
            }
        }
        // descend
        for (let i = 25; i >= 0; --i) {
            if (cnt[i] > 0) {
                res.push(String.fromCharCode(i + 97));
                cnt[i]--;
            }
        }
    }
    return res.join('');
};
```

## Typescript

```typescript
function sortString(s: string): string {
    const freq = new Array(26).fill(0);
    for (const ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }

    let result = "";
    const n = s.length;

    while (result.length < n) {
        // increasing order
        for (let i = 0; i < 26; i++) {
            if (freq[i] > 0) {
                result += String.fromCharCode(i + 97);
                freq[i]--;
            }
        }
        // decreasing order
        for (let i = 25; i >= 0; i--) {
            if (freq[i] > 0) {
                result += String.fromCharCode(i + 97);
                freq[i]--;
            }
        }
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function sortString($s) {
        $freq = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($s[$i]) - ord('a');
            $freq[$idx]++;
        }

        $result = '';
        while (strlen($result) < $n) {
            // Ascending order
            for ($i = 0; $i < 26; $i++) {
                if ($freq[$i] > 0) {
                    $result .= chr(ord('a') + $i);
                    $freq[$i]--;
                }
            }
            // Descending order
            for ($i = 25; $i >= 0; $i--) {
                if ($freq[$i] > 0) {
                    $result .= chr(ord('a') + $i);
                    $freq[$i]--;
                }
            }
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func sortString(_ s: String) -> String {
        var freq = [Int](repeating: 0, count: 26)
        let aValue = UnicodeScalar("a").value
        for scalar in s.unicodeScalars {
            let idx = Int(scalar.value - aValue)
            freq[idx] += 1
        }
        var result = ""
        let total = s.count
        while result.count < total {
            // Ascending order
            for i in 0..<26 {
                if freq[i] > 0 {
                    let ch = Character(UnicodeScalar(i + Int(aValue))!)
                    result.append(ch)
                    freq[i] -= 1
                }
            }
            // Descending order
            for i in stride(from: 25, through: 0, by: -1) {
                if freq[i] > 0 {
                    let ch = Character(UnicodeScalar(i + Int(aValue))!)
                    result.append(ch)
                    freq[i] -= 1
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
    fun sortString(s: String): String {
        val cnt = IntArray(26)
        for (ch in s) {
            cnt[ch.code - 'a'.code]++
        }
        val sb = StringBuilder()
        val n = s.length
        while (sb.length < n) {
            for (i in 0..25) {
                if (cnt[i] > 0) {
                    sb.append(('a'.code + i).toChar())
                    cnt[i]--
                }
            }
            for (i in 25 downTo 0) {
                if (cnt[i] > 0) {
                    sb.append(('a'.code + i).toChar())
                    cnt[i]--
                }
            }
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String sortString(String s) {
    List<int> cnt = List.filled(26, 0);
    for (int i = 0; i < s.length; i++) {
      cnt[s.codeUnitAt(i) - 97]++;
    }
    StringBuffer sb = StringBuffer();
    int total = s.length;
    while (sb.length < total) {
      for (int i = 0; i < 26; i++) {
        if (cnt[i] > 0) {
          sb.writeCharCode(97 + i);
          cnt[i]--;
        }
      }
      for (int i = 25; i >= 0; i--) {
        if (cnt[i] > 0) {
          sb.writeCharCode(97 + i);
          cnt[i]--;
        }
      }
    }
    return sb.toString();
  }
}
```

## Golang

```go
import "strings"

func sortString(s string) string {
    var cnt [26]int
    for _, ch := range s {
        cnt[ch-'a']++
    }
    total := len(s)
    var sb strings.Builder
    for sb.Len() < total {
        for i := 0; i < 26; i++ {
            if cnt[i] > 0 {
                sb.WriteByte(byte('a' + i))
                cnt[i]--
            }
        }
        for i := 25; i >= 0; i-- {
            if cnt[i] > 0 {
                sb.WriteByte(byte('a' + i))
                cnt[i]--
            }
        }
    }
    return sb.String()
}
```

## Ruby

```ruby
def sort_string(s)
  freq = Array.new(26, 0)
  s.each_char { |c| freq[c.ord - 97] += 1 }
  res = +""
  total = s.length
  while res.length < total
    (0...26).each do |i|
      if freq[i] > 0
        res << (i + 97).chr
        freq[i] -= 1
      end
    end
    25.downto(0) do |i|
      if freq[i] > 0
        res << (i + 97).chr
        freq[i] -= 1
      end
    end
  end
  res
end
```

## Scala

```scala
object Solution {
    def sortString(s: String): String = {
        val cnt = new Array[Int](26)
        for (ch <- s) cnt(ch - 'a') += 1
        val sb = new StringBuilder(s.length)
        var total = s.length
        while (total > 0) {
            // increasing order
            for (i <- 0 until 26 if cnt(i) > 0) {
                sb.append(('a' + i).toChar)
                cnt(i) -= 1
                total -= 1
            }
            // decreasing order
            for (i <- 25 to 0 by -1 if cnt(i) > 0) {
                sb.append(('a' + i).toChar)
                cnt(i) -= 1
                total -= 1
            }
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn sort_string(s: String) -> String {
        let mut cnt = [0usize; 26];
        for &b in s.as_bytes() {
            cnt[(b - b'a') as usize] += 1;
        }
        let mut result = Vec::with_capacity(s.len());
        while result.len() < s.len() {
            for i in 0..26 {
                if cnt[i] > 0 {
                    result.push((b'a' + i as u8) as char);
                    cnt[i] -= 1;
                }
            }
            for i in (0..26).rev() {
                if cnt[i] > 0 {
                    result.push((b'a' + i as u8) as char);
                    cnt[i] -= 1;
                }
            }
        }
        result.iter().collect()
    }
}
```

## Racket

```racket
(define/contract (sort-string s)
  (-> string? string?)
  (let* ((len (string-length s))
         (cnt (make-vector 26 0)))
    (for ([i (in-range len)])
      (let* ((ch (string-ref s i))
             (idx (- (char->integer ch) (char->integer #\a))))
        (vector-set! cnt idx (+ (vector-ref cnt idx) 1))))
    (let loop ((remaining len) (acc '()))
      (if (= remaining 0)
          (list->string (reverse acc))
          (let-values ([(rem1 acc1)
                        (let inner ((i 0) (rem remaining) (a acc))
                          (if (> i 25)
                              (values rem a)
                              (let ((c (vector-ref cnt i)))
                                (if (> c 0)
                                    (begin
                                      (vector-set! cnt i (- c 1))
                                      (inner (+ i 1) (- rem 1)
                                             (cons (integer->char (+ i (char->integer #\a))) a)))
                                    (inner (+ i 1) rem a)))))]
                       [(rem2 acc2)
                        (let inner ((i 25) (rem rem1) (a acc1))
                          (if (< i 0)
                              (values rem a)
                              (let ((c (vector-ref cnt i)))
                                (if (> c 0)
                                    (begin
                                      (vector-set! cnt i (- c 1))
                                      (inner (- i 1) (- rem 1)
                                             (cons (integer->char (+ i (char->integer #\a))) a)))
                                    (inner (- i 1) rem a))))]))
            (loop rem2 acc2))))))
```

## Erlang

```erlang
-spec sort_string(unicode:unicode_binary()) -> unicode:unicode_binary().
sort_string(S) ->
    Codes = binary_to_list(S),
    Counts0 = init_counts(Codes, erlang:make_tuple(26, 0)),
    ResultList = loop(Counts0, []),
    list_to_binary(ResultList).

init_counts([], Tuple) -> Tuple;
init_counts([C|Rest], Tuple) ->
    Index = C - $a + 1,
    Old = element(Index, Tuple),
    NewTuple = setelement(Index, Tuple, Old + 1),
    init_counts(Rest, NewTuple).

any_positive(Tuple) -> any_positive(1, Tuple).
any_positive(I, Tuple) when I =< 26 ->
    case element(I, Tuple) of
        C when C > 0 -> true;
        _ -> any_positive(I+1, Tuple)
    end;
any_positive(_, _) -> false.

process_up(Idx, Tuple, Acc) when Idx =< 26 ->
    Count = element(Idx, Tuple),
    if Count > 0 ->
            Char = $a + Idx - 1,
            NewTuple = setelement(Idx, Tuple, Count-1),
            process_up(Idx+1, NewTuple, [Char|Acc]);
       true ->
            process_up(Idx+1, Tuple, Acc)
    end;
process_up(_, Tuple, Acc) -> {Tuple, Acc}.

process_down(Idx, Tuple, Acc) when Idx >= 1 ->
    Count = element(Idx, Tuple),
    if Count > 0 ->
            Char = $a + Idx - 1,
            NewTuple = setelement(Idx, Tuple, Count-1),
            process_down(Idx-1, NewTuple, [Char|Acc]);
       true ->
            process_down(Idx-1, Tuple, Acc)
    end;
process_down(_, Tuple, Acc) -> {Tuple, Acc}.

loop(Tuple, Acc) ->
    case any_positive(Tuple) of
        false -> lists:reverse(Acc);
        true ->
            {T1, A1} = process_up(1, Tuple, Acc),
            {T2, A2} = process_down(26, T1, A1),
            loop(T2, A2)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec sort_string(s :: String.t) :: String.t
  def sort_string(s) do
    freq =
      s
      |> String.to_charlist()
      |> Enum.reduce(%{}, fn c, acc -> Map.update(acc, c, 1, &(&1 + 1)) end)

    total = String.length(s)
    build(freq, total, [])
  end

  defp build(_freq, 0, acc), do: acc |> Enum.reverse() |> List.to_string()

  defp build(freq, remaining, acc) do
    {freq_up, rem_up, acc_up} =
      Enum.reduce(?a..?z, {freq, remaining, acc}, fn code, {f, r, a} ->
        cnt = Map.get(f, code, 0)

        if cnt > 0 do
          f2 = Map.put(f, code, cnt - 1)
          {f2, r - 1, [code | a]}
        else
          {f, r, a}
        end
      end)

    {freq_down, rem_down, acc_down} =
      Enum.reduce(Enum.reverse(?a..?z), {freq_up, rem_up, acc_up}, fn code, {f, r, a} ->
        cnt = Map.get(f, code, 0)

        if cnt > 0 do
          f2 = Map.put(f, code, cnt - 1)
          {f2, r - 1, [code | a]}
        else
          {f, r, a}
        end
      end)

    build(freq_down, rem_down, acc_down)
  end
end
```
