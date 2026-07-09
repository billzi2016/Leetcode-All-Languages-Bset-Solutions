# 1781. Sum of Beauty of All Substrings

## Cpp

```cpp
class Solution {
public:
    int beautySum(string s) {
        int n = s.size();
        long long total = 0;
        for (int i = 0; i < n; ++i) {
            int freq[26] = {0};
            for (int j = i; j < n; ++j) {
                ++freq[s[j] - 'a'];
                int mx = 0, mn = INT_MAX;
                for (int k = 0; k < 26; ++k) {
                    if (freq[k] > 0) {
                        mx = max(mx, freq[k]);
                        mn = min(mn, freq[k]);
                    }
                }
                total += (mx - mn);
            }
        }
        return (int)total;
    }
};
```

## Java

```java
class Solution {
    public int beautySum(String s) {
        int n = s.length();
        char[] chars = s.toCharArray();
        int totalBeauty = 0;
        for (int i = 0; i < n; i++) {
            int[] freq = new int[26];
            for (int j = i; j < n; j++) {
                freq[chars[j] - 'a']++;
                int max = 0;
                int min = Integer.MAX_VALUE;
                for (int k = 0; k < 26; k++) {
                    if (freq[k] > 0) {
                        if (freq[k] > max) max = freq[k];
                        if (freq[k] < min) min = freq[k];
                    }
                }
                totalBeauty += max - min;
            }
        }
        return totalBeauty;
    }
}
```

## Python

```python
class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        total = 0
        for i in range(n):
            cnt = [0] * 26
            for j in range(i, n):
                idx = ord(s[j]) - 97
                cnt[idx] += 1
                mx = 0
                mn = float('inf')
                for c in cnt:
                    if c:
                        if c > mx:
                            mx = c
                        if c < mn:
                            mn = c
                total += mx - mn
        return total
```

## Python3

```python
class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        total = 0
        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                idx = ord(s[j]) - 97
                freq[idx] += 1
                max_cnt = 0
                min_cnt = n + 1
                for cnt in freq:
                    if cnt > 0:
                        if cnt > max_cnt:
                            max_cnt = cnt
                        if cnt < min_cnt:
                            min_cnt = cnt
                total += max_cnt - min_cnt
        return total
```

## C

```c
int beautySum(char* s) {
    int n = 0;
    while (s[n] != '\0') n++;
    int total = 0;
    for (int i = 0; i < n; ++i) {
        int freq[26] = {0};
        for (int j = i; j < n; ++j) {
            freq[s[j] - 'a']++;
            int mx = 0, mn = n + 1;
            for (int k = 0; k < 26; ++k) {
                if (freq[k] > 0) {
                    if (freq[k] > mx) mx = freq[k];
                    if (freq[k] < mn) mn = freq[k];
                }
            }
            total += (mx - mn);
        }
    }
    return total;
}
```

## Csharp

```csharp
public class Solution {
    public int BeautySum(string s) {
        int n = s.Length;
        int total = 0;
        for (int i = 0; i < n; i++) {
            int[] cnt = new int[26];
            for (int j = i; j < n; j++) {
                cnt[s[j] - 'a']++;
                int max = 0, min = int.MaxValue;
                for (int k = 0; k < 26; k++) {
                    if (cnt[k] > 0) {
                        if (cnt[k] > max) max = cnt[k];
                        if (cnt[k] < min) min = cnt[k];
                    }
                }
                total += max - min;
            }
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
var beautySum = function(s) {
    const n = s.length;
    let total = 0;
    for (let i = 0; i < n; ++i) {
        const freq = new Array(26).fill(0);
        for (let j = i; j < n; ++j) {
            const idx = s.charCodeAt(j) - 97;
            freq[idx]++;
            let max = 0;
            let min = Infinity;
            for (let k = 0; k < 26; ++k) {
                if (freq[k] > 0) {
                    if (freq[k] > max) max = freq[k];
                    if (freq[k] < min) min = freq[k];
                }
            }
            total += max - min;
        }
    }
    return total;
};
```

## Typescript

```typescript
function beautySum(s: string): number {
    const n = s.length;
    let total = 0;
    for (let i = 0; i < n; i++) {
        const freq = new Array(26).fill(0);
        for (let j = i; j < n; j++) {
            const idx = s.charCodeAt(j) - 97;
            freq[idx]++;
            let maxF = 0;
            let minF = Number.MAX_SAFE_INTEGER;
            for (let k = 0; k < 26; k++) {
                if (freq[k] > 0) {
                    if (freq[k] > maxF) maxF = freq[k];
                    if (freq[k] < minF) minF = freq[k];
                }
            }
            total += maxF - minF;
        }
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
    function beautySum($s) {
        $n = strlen($s);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $cnt = array_fill(0, 26, 0);
            for ($j = $i; $j < $n; $j++) {
                $idx = ord($s[$j]) - 97;
                $cnt[$idx]++;

                $maxFreq = 0;
                $minFreq = PHP_INT_MAX;
                for ($k = 0; $k < 26; $k++) {
                    if ($cnt[$k] > 0) {
                        if ($cnt[$k] > $maxFreq) $maxFreq = $cnt[$k];
                        if ($cnt[$k] < $minFreq) $minFreq = $cnt[$k];
                    }
                }
                $ans += $maxFreq - $minFreq;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func beautySum(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var total = 0
        for i in 0..<n {
            var freq = [Int](repeating: 0, count: 26)
            for j in i..<n {
                let idx = Int(chars[j].unicodeScalars.first!.value - UnicodeScalar("a").value)
                freq[idx] += 1
                var maxFreq = 0
                var minFreq = Int.max
                for f in freq {
                    if f > 0 {
                        if f > maxFreq { maxFreq = f }
                        if f < minFreq { minFreq = f }
                    }
                }
                total += maxFreq - minFreq
            }
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun beautySum(s: String): Int {
        val n = s.length
        var total = 0
        for (i in 0 until n) {
            val freq = IntArray(26)
            for (j in i until n) {
                val idx = s[j] - 'a'
                freq[idx]++
                var maxF = 0
                var minF = Int.MAX_VALUE
                for (k in 0 until 26) {
                    if (freq[k] > 0) {
                        if (freq[k] > maxF) maxF = freq[k]
                        if (freq[k] < minF) minF = freq[k]
                    }
                }
                total += maxF - minF
            }
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int beautySum(String s) {
    int n = s.length;
    int total = 0;
    List<int> cnt = List.filled(26, 0);
    for (int i = 0; i < n; ++i) {
      // reset counts for new start index
      for (int k = 0; k < 26; ++k) cnt[k] = 0;
      int maxFreq = 0;
      for (int j = i; j < n; ++j) {
        int idx = s.codeUnitAt(j) - 97;
        cnt[idx]++;
        if (cnt[idx] > maxFreq) maxFreq = cnt[idx];
        int minFreq = n + 1;
        for (int k = 0; k < 26; ++k) {
          int c = cnt[k];
          if (c > 0 && c < minFreq) minFreq = c;
        }
        total += maxFreq - minFreq;
      }
    }
    return total;
  }
}
```

## Golang

```go
func beautySum(s string) int {
	n := len(s)
	total := 0
	for i := 0; i < n; i++ {
		var freq [26]int
		for j := i; j < n; j++ {
			idx := s[j] - 'a'
			freq[idx]++
			maxFreq, minFreq := 0, n+1
			for k := 0; k < 26; k++ {
				if freq[k] > 0 {
					if freq[k] > maxFreq {
						maxFreq = freq[k]
					}
					if freq[k] < minFreq {
						minFreq = freq[k]
					}
				}
			}
			total += maxFreq - minFreq
		}
	}
	return total
}
```

## Ruby

```ruby
def beauty_sum(s)
  n = s.length
  bytes = s.bytes
  total = 0

  (0...n).each do |i|
    freq = Array.new(26, 0)
    (i...n).each do |j|
      idx = bytes[j] - 97
      freq[idx] += 1

      max_f = 0
      min_f = nil
      26.times do |k|
        f = freq[k]
        next if f == 0
        max_f = f if f > max_f
        min_f = f if min_f.nil? || f < min_f
      end

      total += (max_f - min_f) if max_f && min_f && max_f > min_f
    end
  end

  total
end
```

## Scala

```scala
object Solution {
    def beautySum(s: String): Int = {
        val n = s.length
        var total = 0
        for (i <- 0 until n) {
            val freq = new Array[Int](26)
            for (j <- i until n) {
                val idx = s.charAt(j) - 'a'
                freq(idx) += 1
                var maxF = 0
                var minF = Int.MaxValue
                var k = 0
                while (k < 26) {
                    if (freq(k) > 0) {
                        if (freq(k) > maxF) maxF = freq(k)
                        if (freq(k) < minF) minF = freq(k)
                    }
                    k += 1
                }
                total += (maxF - minF)
            }
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn beauty_sum(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut total: i32 = 0;
        for i in 0..n {
            let mut freq = [0i32; 26];
            for j in i..n {
                let idx = (bytes[j] - b'a') as usize;
                freq[idx] += 1;

                let mut max_cnt = 0i32;
                let mut min_cnt = i32::MAX;
                for &cnt in freq.iter() {
                    if cnt > 0 {
                        if cnt > max_cnt {
                            max_cnt = cnt;
                        }
                        if cnt < min_cnt {
                            min_cnt = cnt;
                        }
                    }
                }
                if max_cnt > min_cnt {
                    total += max_cnt - min_cnt;
                }
            }
        }
        total
    }
}
```

## Racket

```racket
(define/contract (beauty-sum s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (base (char->integer #\a)))
    (let ((total 0))
      (for ([i (in-range n)])
        (define freq (make-vector 26 0))
        (for ([j (in-range i n)])
          (define idx (- (char->integer (string-ref s j)) base))
          (vector-set! freq idx (+ 1 (vector-ref freq idx)))
          ;; compute max and min (non‑zero) frequencies
          (let loop ((k 0) (maxc 0) (minc #f))
            (if (= k 26)
                (let ((beauty (- maxc (or minc 0))))
                  (set! total (+ total beauty)))
                (let ((cnt (vector-ref freq k)))
                  (if (> cnt 0)
                      (loop (+ k 1) (max maxc cnt) (if minc (min minc cnt) cnt))
                      (loop (+ k 1) maxc minc)))))))
      total)))
```

## Erlang

```erlang
-module(solution).
-export([beauty_sum/1]).

-spec beauty_sum(unicode:unicode_binary()) -> integer().
beauty_sum(S) ->
    Chars = unicode:characters_to_list(S),
    N = length(Chars),
    beauty_sum_start(0, Chars, N, 0).

beauty_sum_start(I, _Chars, N, Acc) when I >= N ->
    Acc;
beauty_sum_start(I, Chars, N, Acc) ->
    Suffix = lists:nthtail(I, Chars),
    NewAcc = beauty_sum_from_suffix(Suffix, erlang:make_tuple(26, 0), Acc),
    beauty_sum_start(I + 1, Chars, N, NewAcc).

beauty_sum_from_suffix([], _Freq, Acc) ->
    Acc;
beauty_sum_from_suffix([C | Rest], Freq, Acc) ->
    Index = C - $a + 1,
    OldVal = element(Index, Freq),
    UpdatedFreq = setelement(Index, Freq, OldVal + 1),
    {Max, Min} = max_min(UpdatedFreq),
    NewAcc = Acc + (Max - Min),
    beauty_sum_from_suffix(Rest, UpdatedFreq, NewAcc).

max_min(Freq) ->
    max_min_iter(1, Freq, 0, 1000000).

max_min_iter(I, _Freq, Max, Min) when I > 26 ->
    {Max, Min};
max_min_iter(I, Freq, Max, Min) ->
    Val = element(I, Freq),
    if
        Val > 0 ->
            NewMax = case Val > Max of true -> Val; false -> Max end,
            NewMin = case Val < Min of true -> Val; false -> Min end,
            max_min_iter(I + 1, Freq, NewMax, NewMin);
        true ->
            max_min_iter(I + 1, Freq, Max, Min)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec beauty_sum(s :: String.t()) :: integer()
  def beauty_sum(s) do
    chars = String.to_charlist(s)
    n = length(chars)

    Enum.reduce(0..(n - 1), 0, fn i, total_acc ->
      freq_start = :erlang.make_tuple(26, 0)

      {_, sum_i} =
        Enum.reduce(i..(n - 1), {freq_start, 0}, fn j, {freq_acc, sum_acc} ->
          idx = Enum.at(chars, j) - ?a
          cur = elem(freq_acc, idx + 1)
          freq_new = put_elem(freq_acc, idx + 1, cur + 1)

          min_init = n + 1

          {max_f, min_f} =
            Enum.reduce(0..25, {0, min_init}, fn k, {mx, mn} ->
              c = elem(freq_new, k + 1)

              if c > 0 do
                mx2 = if c > mx, do: c, else: mx
                mn2 = if c < mn, do: c, else: mn
                {mx2, mn2}
              else
                {mx, mn}
              end
            end)

          diff = max_f - min_f
          {freq_new, sum_acc + diff}
        end)

      total_acc + sum_i
    end)
  end
end
```
