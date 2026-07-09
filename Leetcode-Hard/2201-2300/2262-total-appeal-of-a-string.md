# 2262. Total Appeal of A String

## Cpp

```cpp
class Solution {
public:
    long long appealSum(string s) {
        vector<int> last(26, -1);
        long long cur = 0, ans = 0;
        for (int i = 0; i < (int)s.size(); ++i) {
            int idx = s[i] - 'a';
            cur += i - last[idx];
            last[idx] = i;
            ans += cur;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long appealSum(String s) {
        int n = s.length();
        int[] last = new int[26];
        for (int i = 0; i < 26; i++) {
            last[i] = -1;
        }
        long cur = 0;
        long ans = 0;
        for (int i = 0; i < n; i++) {
            int c = s.charAt(i) - 'a';
            cur += i - last[c];
            last[c] = i;
            ans += cur;
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = [-1] * 26
        cur = 0
        total = 0
        for i, ch in enumerate(s):
            idx = ord(ch) - 97
            cur += i - last[idx]
            last[idx] = i
            total += cur
        return total
```

## Python3

```python
class Solution:
    def appealSum(self, s: str) -> int:
        last = [-1] * 26
        total = 0
        cur = 0
        for i, ch in enumerate(s):
            idx = ord(ch) - 97
            cur += i - last[idx]
            last[idx] = i
            total += cur
        return total
```

## C

```c
long long appealSum(char* s) {
    long long last[26];
    for (int i = 0; i < 26; ++i) last[i] = -1;
    long long cur = 0, ans = 0;
    for (long long i = 0; s[i]; ++i) {
        int idx = s[i] - 'a';
        cur += i - last[idx];
        ans += cur;
        last[idx] = i;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public long AppealSum(string s) {
        int n = s.Length;
        long cur = 0;
        long total = 0;
        int[] last = new int[26];
        for (int i = 0; i < 26; i++) last[i] = -1;
        for (int i = 0; i < n; i++) {
            int idx = s[i] - 'a';
            int prev = last[idx];
            cur += i - prev;
            total += cur;
            last[idx] = i;
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var appealSum = function(s) {
    const last = new Array(26).fill(-1);
    let dp = 0;
    let total = 0;
    for (let i = 0; i < s.length; ++i) {
        const idx = s.charCodeAt(i) - 97;
        const add = i - last[idx];
        dp += add;
        total += dp;
        last[idx] = i;
    }
    return total;
};
```

## Typescript

```typescript
function appealSum(s: string): number {
    const last = new Array(26).fill(-1);
    let cur = 0;
    let total = 0;
    for (let i = 0; i < s.length; i++) {
        const idx = s.charCodeAt(i) - 97;
        cur += i - last[idx];
        total += cur;
        last[idx] = i;
    }
    return total;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function appealSum($s) {
        $n = strlen($s);
        $last = array_fill(0, 26, -1);
        $cur = 0;
        $total = 0;
        for ($i = 0; $i < $n; ++$i) {
            $idx = ord($s[$i]) - 97;
            $cur += $i - $last[$idx];
            $total += $cur;
            $last[$idx] = $i;
        }
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func appealSum(_ s: String) -> Int {
        var last = [Int](repeating: -1, count: 26)
        var cur = 0
        var ans = 0
        for (i, ch) in s.utf8.enumerated() {
            let idx = Int(ch - 97) // 'a' ascii is 97
            cur += i - last[idx]
            last[idx] = i
            ans += cur
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun appealSum(s: String): Long {
        val last = IntArray(26) { -1 }
        var cur = 0L
        var ans = 0L
        for (i in s.indices) {
            val idx = s[i].code - 'a'.code
            cur += (i - last[idx]).toLong()
            last[idx] = i
            ans += cur
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int appealSum(String s) {
    List<int> last = List.filled(26, -1);
    int cur = 0;
    int ans = 0;
    for (int i = 0; i < s.length; ++i) {
      int idx = s.codeUnitAt(i) - 97;
      cur += i - last[idx];
      last[idx] = i;
      ans += cur;
    }
    return ans;
  }
}
```

## Golang

```go
func appealSum(s string) int64 {
    last := make([]int, 26)
    for i := 0; i < 26; i++ {
        last[i] = -1
    }
    var total int64
    n := len(s)
    for i := 0; i < n; i++ {
        var cur int64
        for j := 0; j < 26; j++ {
            cur += int64(i - last[j])
        }
        total += cur
        idx := s[i] - 'a'
        last[idx] = i
    }
    return total
}
```

## Ruby

```ruby
def appeal_sum(s)
  last = Array.new(26, -1)
  cur = 0
  total = 0
  s.each_char.with_index do |ch, i|
    idx = ch.ord - 97
    cur += i - last[idx]
    last[idx] = i
    total += cur
  end
  total
end
```

## Scala

```scala
object Solution {
    def appealSum(s: String): Long = {
        val last = Array.fill(26)(-1)
        var sumPrev: Long = 0L
        var ans: Long = 0L
        var i = 0
        while (i < s.length) {
            val idx = s.charAt(i) - 'a'
            var total = sumPrev + (i + 1).toLong
            if (last(idx) != -1) {
                total -= (last(idx) + 1)
            }
            ans += total
            if (last(idx) != -1) {
                sumPrev = sumPrev - (last(idx) + 1) + (i + 1)
            } else {
                sumPrev = sumPrev + (i + 1)
            }
            last(idx) = i
            i += 1
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn appeal_sum(s: String) -> i64 {
        let bytes = s.as_bytes();
        let mut last = [-1i64; 26];
        let mut cur: i64 = 0;
        let mut ans: i64 = 0;
        for (i, &b) in bytes.iter().enumerate() {
            let idx = (b - b'a') as usize;
            let inc = i as i64 - last[idx];
            cur += inc;
            ans += cur;
            last[idx] = i as i64;
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (appeal-sum s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (last (make-vector 26 -1)))
    (let loop ((i 0) (cur 0) (ans 0))
      (if (= i n)
          ans
          (let* ((ch (string-ref s i))
                 (idx (- (char->integer ch) (char->integer #\a)))
                 (prev (vector-ref last idx))
                 (delta (- i prev))
                 (new-cur (+ cur delta))
                 (new-ans (+ ans new-cur)))
            (vector-set! last idx i)
            (loop (+ i 1) new-cur new-ans))))))
```

## Erlang

```erlang
-spec appeal_sum(S :: unicode:unicode_binary()) -> integer().
appeal_sum(S) ->
    Last = list_to_tuple(lists:duplicate(26, -1)),
    process(S, 0, 0, 0, Last).

process(<<>>, _I, _Cur, Ans, _Last) ->
    Ans;
process(<<Char, Rest/binary>>, I, Cur, Ans, Last) ->
    Idx = Char - $a,
    Prev = element(Idx + 1, Last),
    Delta = I - Prev,
    NewCur = Cur + Delta,
    NewAns = Ans + NewCur,
    NewLast = setelement(Idx + 1, Last, I),
    process(Rest, I + 1, NewCur, NewAns, NewLast).
```

## Elixir

```elixir
defmodule Solution do
  @spec appeal_sum(s :: String.t) :: integer
  def appeal_sum(s) do
    chars = String.to_charlist(s)

    {_, _, ans} =
      Enum.with_index(chars)
      |> Enum.reduce({:array.new(26, default: -1), 0, 0}, fn {cp, i},
            {last_arr, cur, acc} ->
        idx = cp - ?a
        prev = :array.get(idx, last_arr)
        new_cur = cur + i - prev
        new_last = :array.set(idx, i, last_arr)
        {new_last, new_cur, acc + new_cur}
      end)

    ans
  end
end
```
