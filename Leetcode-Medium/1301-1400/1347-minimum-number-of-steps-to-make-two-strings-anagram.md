# 1347. Minimum Number of Steps to Make Two Strings Anagram

## Cpp

```cpp
class Solution {
public:
    int minSteps(string s, string t) {
        int cnt[26] = {0};
        for (size_t i = 0; i < s.size(); ++i) {
            ++cnt[t[i] - 'a'];
            --cnt[s[i] - 'a'];
        }
        int ans = 0;
        for (int x : cnt) if (x > 0) ans += x;
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minSteps(String s, String t) {
        int[] diff = new int[26];
        int n = s.length();
        for (int i = 0; i < n; i++) {
            diff[t.charAt(i) - 'a']++;
            diff[s.charAt(i) - 'a']--;
        }
        int ans = 0;
        for (int d : diff) {
            if (d > 0) ans += d;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        cnt = [0] * 26
        for cs, ct in zip(s, t):
            cnt[ord(ct) - 97] += 1
            cnt[ord(cs) - 97] -= 1
        return sum(x for x in cnt if x > 0)
```

## Python3

```python
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt = [0] * 26
        for cs, ct in zip(s, t):
            cnt[ord(ct) - 97] += 1
            cnt[ord(cs) - 97] -= 1
        return sum(x for x in cnt if x > 0)
```

## C

```c
#include <string.h>

int minSteps(char* s, char* t) {
    int cnt[26] = {0};
    for (int i = 0; s[i] && t[i]; ++i) {
        cnt[t[i] - 'a']++;
        cnt[s[i] - 'a']--;
    }
    int ans = 0;
    for (int i = 0; i < 26; ++i) {
        if (cnt[i] > 0) ans += cnt[i];
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinSteps(string s, string t)
    {
        int[] diff = new int[26];
        for (int i = 0; i < s.Length; i++)
        {
            diff[t[i] - 'a']++;
            diff[s[i] - 'a']--;
        }

        int steps = 0;
        foreach (int val in diff)
        {
            if (val > 0) steps += val;
        }
        return steps;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var minSteps = function(s, t) {
    const diff = new Array(26).fill(0);
    const aCode = 'a'.charCodeAt(0);
    for (let i = 0; i < s.length; ++i) {
        diff[t.charCodeAt(i) - aCode]++;   // count in t
        diff[s.charCodeAt(i) - aCode]--;   // subtract count in s
    }
    let ans = 0;
    for (let i = 0; i < 26; ++i) {
        if (diff[i] > 0) ans += diff[i];
    }
    return ans;
};
```

## Typescript

```typescript
function minSteps(s: string, t: string): number {
    const diff = new Array(26).fill(0);
    for (let i = 0; i < s.length; ++i) {
        diff[t.charCodeAt(i) - 97]++;
        diff[s.charCodeAt(i) - 97]--;
    }
    let ans = 0;
    for (const d of diff) {
        if (d > 0) ans += d;
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Integer
     */
    function minSteps($s, $t) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $cnt[ord($t[$i]) - 97]++;
            $cnt[ord($s[$i]) - 97]--;
        }
        $ans = 0;
        foreach ($cnt as $v) {
            if ($v > 0) {
                $ans += $v;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minSteps(_ s: String, _ t: String) -> Int {
        let aValue = Character("a").unicodeScalars.first!.value
        var count = [Int](repeating: 0, count: 26)
        
        for (sc, tc) in zip(s.unicodeScalars, t.unicodeScalars) {
            let ti = Int(tc.value - aValue)
            let si = Int(sc.value - aValue)
            count[ti] += 1
            count[si] -= 1
        }
        
        var ans = 0
        for v in count where v > 0 {
            ans += v
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minSteps(s: String, t: String): Int {
        val diff = IntArray(26)
        for (i in s.indices) {
            diff[t[i] - 'a']++
            diff[s[i] - 'a']--
        }
        var ans = 0
        for (v in diff) {
            if (v > 0) ans += v
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minSteps(String s, String t) {
    const int aCode = 97; // 'a'.codeUnitAt(0)
    List<int> diff = List.filled(26, 0);
    for (int i = 0; i < s.length; i++) {
      diff[t.codeUnitAt(i) - aCode]++;
      diff[s.codeUnitAt(i) - aCode]--;
    }
    int ans = 0;
    for (int d in diff) {
      if (d > 0) ans += d;
    }
    return ans;
  }
}
```

## Golang

```go
func minSteps(s string, t string) int {
    var count [26]int
    for i := 0; i < len(s); i++ {
        count[t[i]-'a']++
        count[s[i]-'a']--
    }
    ans := 0
    for _, v := range count {
        if v > 0 {
            ans += v
        }
    }
    return ans
}
```

## Ruby

```ruby
def min_steps(s, t)
  count = Array.new(26, 0)
  s.each_byte.with_index do |b, i|
    count[t.getbyte(i) - 97] += 1
    count[b - 97] -= 1
  end
  ans = 0
  count.each { |c| ans += c if c > 0 }
  ans
end
```

## Scala

```scala
object Solution {
    def minSteps(s: String, t: String): Int = {
        val diff = new Array[Int](26)
        for (i <- s.indices) {
            diff(t.charAt(i) - 'a') += 1
            diff(s.charAt(i) - 'a') -= 1
        }
        var ans = 0
        for (v <- diff) if (v > 0) ans += v
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_steps(s: String, t: String) -> i32 {
        let mut count = [0i32; 26];
        for (cs, ct) in s.bytes().zip(t.bytes()) {
            count[(ct - b'a') as usize] += 1;
            count[(cs - b'a') as usize] -= 1;
        }
        count.iter().filter(|&&x| x > 0).sum()
    }
}
```

## Racket

```racket
(define/contract (min-steps s t)
  (-> string? string? exact-integer?)
  (let* ((n (string-length s))
         (cnt (make-vector 26 0)))
    (for ([i (in-range n)])
      (let* ((idx-t (- (char->integer (string-ref t i))
                       (char->integer #\a))))
        (vector-set! cnt idx-t (+ 1 (vector-ref cnt idx-t))))
      (let* ((idx-s (- (char->integer (string-ref s i))
                       (char->integer #\a))))
        (vector-set! cnt idx-s (- (vector-ref cnt idx-s) 1))))
    (let loop ((i 0) (ans 0))
      (if (= i 26)
          ans
          (let ((val (vector-ref cnt i)))
            (loop (+ i 1) (+ ans (if (> val 0) val 0))))))))
```

## Erlang

```erlang
-spec min_steps(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> integer().
min_steps(S, T) ->
    Freq0 = array:new(26, {default,0}),
    Freq = build_freq(binary_to_list(S), Freq0),
    process_t(binary_to_list(T), Freq, 0).

build_freq([], Arr) -> Arr;
build_freq([C|Rest], Arr) ->
    Idx = C - $a,
    Val = array:get(Idx+1, Arr),
    build_freq(Rest, array:set(Idx+1, Val+1, Arr)).

process_t([], _Arr, Ans) -> Ans;
process_t([C|Rest], Arr, Ans) ->
    Idx = C - $a,
    Val = array:get(Idx+1, Arr),
    if
        Val > 0 ->
            process_t(Rest, array:set(Idx+1, Val-1, Arr), Ans);
        true ->
            process_t(Rest, Arr, Ans + 1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_steps(s :: String.t(), t :: String.t()) :: integer()
  def min_steps(s, t) do
    freq =
      Enum.reduce(String.to_charlist(s), :array.new(26, default: 0), fn c, acc ->
        idx = c - ?a
        val = :array.get(idx, acc)
        :array.set(idx, val + 1, acc)
      end)

    {ans, _} =
      Enum.reduce(String.to_charlist(t), {0, freq}, fn c, {cnt, arr} ->
        idx = c - ?a
        val = :array.get(idx, arr)

        if val > 0 do
          {cnt, :array.set(idx, val - 1, arr)}
        else
          {cnt + 1, arr}
        end
      end)

    ans
  end
end
```
