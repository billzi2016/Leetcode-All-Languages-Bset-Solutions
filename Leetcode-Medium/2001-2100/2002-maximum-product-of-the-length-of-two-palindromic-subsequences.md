# 2002. Maximum Product of the Length of Two Palindromic Subsequences

## Cpp

```cpp
class Solution {
public:
    int maxProduct(string s) {
        int n = s.size();
        int total = 1 << n;
        vector<int> palLen(total, 0);
        for (int mask = 1; mask < total; ++mask) {
            string sub;
            sub.reserve(__builtin_popcount(mask));
            for (int i = 0; i < n; ++i)
                if (mask >> i & 1) sub.push_back(s[i]);
            bool ok = true;
            int l = 0, r = (int)sub.size() - 1;
            while (l < r) {
                if (sub[l] != sub[r]) { ok = false; break; }
                ++l; --r;
            }
            if (ok) palLen[mask] = sub.size();
        }
        int ans = 0;
        for (int mask1 = 1; mask1 < total; ++mask1) {
            if (!palLen[mask1]) continue;
            int complement = (total - 1) ^ mask1;
            for (int mask2 = complement; mask2; mask2 = (mask2 - 1) & complement) {
                if (!palLen[mask2]) continue;
                ans = max(ans, palLen[mask1] * palLen[mask2]);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxProduct(String s) {
        int n = s.length();
        int total = 1 << n;
        int[] palLen = new int[total];
        char[] chars = s.toCharArray();

        for (int mask = 0; mask < total; ++mask) {
            // build subsequence characters in order
            int len = Integer.bitCount(mask);
            if (len == 0) continue;
            char[] seq = new char[len];
            int idx = 0;
            for (int i = 0; i < n; ++i) {
                if ((mask & (1 << i)) != 0) {
                    seq[idx++] = chars[i];
                }
            }
            boolean ok = true;
            for (int l = 0, r = len - 1; l < r; ++l, --r) {
                if (seq[l] != seq[r]) {
                    ok = false;
                    break;
                }
            }
            if (ok) palLen[mask] = len;
        }

        int ans = 0;
        for (int mask1 = 0; mask1 < total; ++mask1) {
            if (palLen[mask1] == 0) continue;
            for (int mask2 = mask1 + 1; mask2 < total; ++mask2) {
                if ((mask1 & mask2) != 0) continue;
                if (palLen[mask2] == 0) continue;
                int prod = palLen[mask1] * palLen[mask2];
                if (prod > ans) ans = prod;
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxProduct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        total = 1 << n
        dp = [0] * total  # length of palindrome for each mask, 0 if not palindrome

        # precompute palindrome lengths
        for mask in range(1, total):
            chars = []
            m = mask
            idx = 0
            while m:
                if m & 1:
                    chars.append(s[idx])
                idx += 1
                m >>= 1
            if chars == chars[::-1]:
                dp[mask] = len(chars)

        # SOS DP to get best palindrome length for any submask
        best = dp[:]
        for i in range(n):
            bit = 1 << i
            for mask in range(total):
                if mask & bit:
                    if best[mask ^ bit] > best[mask]:
                        best[mask] = best[mask ^ bit]

        full_mask = total - 1
        ans = 0
        for mask in range(1, total):
            if dp[mask]:
                complement = full_mask ^ mask
                prod = dp[mask] * best[complement]
                if prod > ans:
                    ans = prod
        return ans
```

## Python3

```python
class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        total = 1 << n
        dp = [0] * total

        for mask in range(total):
            seq = []
            idx = 0
            m = mask
            while m:
                if m & 1:
                    seq.append(s[idx])
                idx += 1
                m >>= 1
            if seq == seq[::-1]:
                dp[mask] = len(seq)

        best = dp[:]
        for i in range(n):
            bit = 1 << i
            for mask in range(total):
                if mask & bit:
                    sub = mask ^ bit
                    if best[sub] > best[mask]:
                        best[mask] = best[sub]

        full = total - 1
        ans = 0
        for mask in range(total):
            l1 = dp[mask]
            if l1 == 0:
                continue
            remaining = full ^ mask
            l2 = best[remaining]
            prod = l1 * l2
            if prod > ans:
                ans = prod
        return ans
```

## C

```c
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

int maxProduct(char* s) {
    int n = strlen(s);
    int total = 1 << n;
    int *palLen = (int *)calloc(total, sizeof(int));
    
    char seq[13];
    for (int mask = 1; mask < total; ++mask) {
        int len = 0;
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                seq[len++] = s[i];
            }
        }
        bool ok = true;
        for (int l = 0, r = len - 1; l < r; ++l, --r) {
            if (seq[l] != seq[r]) { ok = false; break; }
        }
        if (ok) palLen[mask] = len;
    }
    
    int ans = 0;
    for (int mask1 = 1; mask1 < total; ++mask1) {
        if (!palLen[mask1]) continue;
        for (int mask2 = mask1 + 1; mask2 < total; ++mask2) {
            if ((mask1 & mask2) != 0) continue;
            if (!palLen[mask2]) continue;
            int prod = palLen[mask1] * palLen[mask2];
            if (prod > ans) ans = prod;
        }
    }
    
    free(palLen);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxProduct(string s)
    {
        int n = s.Length;
        int totalMasks = 1 << n;
        int[] palLen = new int[totalMasks];

        for (int mask = 1; mask < totalMasks; mask++)
        {
            var sb = new System.Text.StringBuilder();
            for (int i = 0; i < n; i++)
                if (((mask >> i) & 1) == 1)
                    sb.Append(s[i]);

            string sub = sb.ToString();
            int len = sub.Length;
            bool isPal = true;
            for (int l = 0, r = len - 1; l < r; l++, r--)
                if (sub[l] != sub[r]) { isPal = false; break; }

            if (isPal) palLen[mask] = len;
        }

        int maxProd = 0;
        for (int mask1 = 1; mask1 < totalMasks; mask1++)
        {
            if (palLen[mask1] == 0) continue;
            for (int mask2 = mask1 + 1; mask2 < totalMasks; mask2++)
            {
                if ((mask1 & mask2) != 0) continue;
                if (palLen[mask2] == 0) continue;

                int prod = palLen[mask1] * palLen[mask2];
                if (prod > maxProd) maxProd = prod;
            }
        }

        return maxProd;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maxProduct = function(s) {
    const n = s.length;
    const total = 1 << n;
    const palLen = new Uint8Array(total); // length up to 12 fits in Uint8

    // Precompute palindrome lengths for all masks
    for (let mask = 1; mask < total; ++mask) {
        const chars = [];
        for (let i = 0; i < n; ++i) {
            if ((mask >> i) & 1) chars.push(s[i]);
        }
        let l = 0, r = chars.length - 1;
        let ok = true;
        while (l < r) {
            if (chars[l] !== chars[r]) { ok = false; break; }
            ++l; --r;
        }
        if (ok) palLen[mask] = chars.length;
    }

    let ans = 0;
    for (let m1 = 1; m1 < total; ++m1) {
        const len1 = palLen[m1];
        if (!len1) continue;
        for (let m2 = m1 + 1; m2 < total; ++m2) {
            if ((m1 & m2) !== 0) continue; // not disjoint
            const len2 = palLen[m2];
            if (!len2) continue;
            const prod = len1 * len2;
            if (prod > ans) ans = prod;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function maxProduct(s: string): number {
    const n = s.length;
    const total = 1 << n;
    const palLen = new Array<number>(total).fill(0);

    // helper to count bits
    const bitCount = (x: number): number => {
        let cnt = 0;
        while (x) {
            x &= x - 1;
            cnt++;
        }
        return cnt;
    };

    // check each subset if it forms a palindrome
    for (let mask = 1; mask < total; ++mask) {
        const chars: string[] = [];
        for (let i = 0; i < n; ++i) {
            if ((mask >> i) & 1) chars.push(s[i]);
        }
        let l = 0, r = chars.length - 1;
        let ok = true;
        while (l < r) {
            if (chars[l] !== chars[r]) { ok = false; break; }
            ++l; --r;
        }
        if (ok) palLen[mask] = chars.length; // same as bitCount(mask)
    }

    const pals: number[] = [];
    for (let mask = 1; mask < total; ++mask) {
        if (palLen[mask] > 0) pals.push(mask);
    }

    let ans = 0;
    for (let i = 0; i < pals.length; ++i) {
        const m1 = pals[i];
        const len1 = palLen[m1];
        for (let j = i + 1; j < pals.length; ++j) {
            const m2 = pals[j];
            if ((m1 & m2) === 0) {
                const prod = len1 * palLen[m2];
                if (prod > ans) ans = prod;
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
     * @return Integer
     */
    function maxProduct($s) {
        $n = strlen($s);
        $total = 1 << $n;
        $palLen = array_fill(0, $total, 0);

        for ($mask = 1; $mask < $total; $mask++) {
            $sub = '';
            for ($i = 0; $i < $n; $i++) {
                if (($mask >> $i) & 1) {
                    $sub .= $s[$i];
                }
            }
            $len = strlen($sub);
            $isPal = true;
            for ($l = 0, $r = $len - 1; $l < $r; $l++, $r--) {
                if ($sub[$l] !== $sub[$r]) {
                    $isPal = false;
                    break;
                }
            }
            if ($isPal) {
                $palLen[$mask] = $len;
            }
        }

        $maxProd = 0;
        for ($mask1 = 1; $mask1 < $total; $mask1++) {
            if ($palLen[$mask1] == 0) continue;
            for ($mask2 = $mask1 + 1; $mask2 < $total; $mask2++) {
                if (($mask1 & $mask2) != 0) continue;
                if ($palLen[$mask2] == 0) continue;
                $prod = $palLen[$mask1] * $palLen[$mask2];
                if ($prod > $maxProd) {
                    $maxProd = $prod;
                }
            }
        }

        return $maxProd;
    }
}
```

## Swift

```swift
class Solution {
    func maxProduct(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        let total = 1 << n
        var palLen = [Int](repeating: 0, count: total)

        for mask in 1..<total {
            var subseq = [Character]()
            for i in 0..<n {
                if (mask & (1 << i)) != 0 {
                    subseq.append(chars[i])
                }
            }
            let len = subseq.count
            var isPal = true
            var l = 0, r = len - 1
            while l < r {
                if subseq[l] != subseq[r] {
                    isPal = false
                    break
                }
                l += 1
                r -= 1
            }
            if isPal {
                palLen[mask] = len
            }
        }

        var ans = 0
        let fullMask = total - 1
        for mask1 in 1..<total {
            let len1 = palLen[mask1]
            if len1 == 0 { continue }
            let remaining = fullMask ^ mask1
            var mask2 = remaining
            while mask2 > 0 {
                let len2 = palLen[mask2]
                if len2 > 0 {
                    let product = len1 * len2
                    if product > ans { ans = product }
                }
                mask2 = (mask2 - 1) & remaining
            }
        }

        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxProduct(s: String): Int {
        val n = s.length
        val total = 1 shl n
        val palLen = IntArray(total)

        // Precompute palindrome lengths for all subsets
        for (mask in 1 until total) {
            val len = Integer.bitCount(mask)
            val chars = CharArray(len)
            var idx = 0
            for (i in 0 until n) {
                if ((mask and (1 shl i)) != 0) {
                    chars[idx++] = s[i]
                }
            }
            var ok = true
            var l = 0
            var r = len - 1
            while (l < r) {
                if (chars[l] != chars[r]) {
                    ok = false
                    break
                }
                l++
                r--
            }
            if (ok) palLen[mask] = len
        }

        var ans = 0
        for (mask1 in 1 until total) {
            val len1 = palLen[mask1]
            if (len1 == 0) continue
            val complement = (total - 1) xor mask1
            var sub = complement
            while (sub > 0) {
                val len2 = palLen[sub]
                if (len2 != 0) {
                    ans = maxOf(ans, len1 * len2)
                }
                sub = (sub - 1) and complement
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int maxProduct(String s) {
    int n = s.length;
    int total = 1 << n;
    List<int> palLen = List.filled(total, 0);
    for (int mask = 1; mask < total; ++mask) {
      List<int> seq = [];
      for (int i = 0; i < n; ++i) {
        if ((mask >> i & 1) == 1) {
          seq.add(s.codeUnitAt(i));
        }
      }
      bool ok = true;
      int l = 0, r = seq.length - 1;
      while (l < r) {
        if (seq[l] != seq[r]) {
          ok = false;
          break;
        }
        ++l;
        --r;
      }
      if (ok) palLen[mask] = seq.length;
    }

    int ans = 0;
    for (int mask1 = 1; mask1 < total; ++mask1) {
      int len1 = palLen[mask1];
      if (len1 == 0) continue;
      for (int mask2 = mask1 + 1; mask2 < total; ++mask2) {
        if ((mask1 & mask2) != 0) continue;
        int len2 = palLen[mask2];
        if (len2 == 0) continue;
        int prod = len1 * len2;
        if (prod > ans) ans = prod;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func maxProduct(s string) int {
	n := len(s)
	total := 1 << n
	palLen := make([]int, total)

	// Precompute palindrome lengths for all subsets
	for mask := 1; mask < total; mask++ {
		var chars []byte
		for i := 0; i < n; i++ {
			if mask&(1<<i) != 0 {
				chars = append(chars, s[i])
			}
		}
		ok := true
		l, r := 0, len(chars)-1
		for l < r {
			if chars[l] != chars[r] {
				ok = false
				break
			}
			l++
			r--
		}
		if ok {
			palLen[mask] = len(chars)
		}
	}

	maxProd := 0
	for m1 := 1; m1 < total; m1++ {
		if palLen[m1] == 0 {
			continue
		}
		for m2 := m1 + 1; m2 < total; m2++ {
			if palLen[m2] == 0 {
				continue
			}
			if (m1 & m2) == 0 {
				prod := palLen[m1] * palLen[m2]
				if prod > maxProd {
					maxProd = prod
				}
			}
		}
	}
	return maxProd
}
```

## Ruby

```ruby
def max_product(s)
  n = s.length
  total = 1 << n
  pal_len = Array.new(total, 0)

  (1...total).each do |mask|
    chars = []
    i = 0
    while i < n
      if (mask & (1 << i)) != 0
        chars << s[i]
      end
      i += 1
    end
    pal_len[mask] = chars.length if chars == chars.reverse
  end

  ans = 0
  (0...total).each do |m1|
    len1 = pal_len[m1]
    next if len1 == 0
    ((m1 + 1)...total).each do |m2|
      next if (m1 & m2) != 0
      len2 = pal_len[m2]
      next if len2 == 0
      prod = len1 * len2
      ans = prod if prod > ans
    end
  end

  ans
end
```

## Scala

```scala
object Solution {
    def maxProduct(s: String): Int = {
        val n = s.length
        val total = 1 << n
        val palLen = new Array[Int](total)

        for (mask <- 1 until total) {
            if (isPal(mask, s, n)) {
                palLen(mask) = Integer.bitCount(mask)
            }
        }

        var maxProd = 0
        for (m1 <- 1 until total) {
            val len1 = palLen(m1)
            if (len1 > 0) {
                var m2 = m1 + 1
                while (m2 < total) {
                    if ((m1 & m2) == 0) {
                        val len2 = palLen(m2)
                        if (len2 > 0) {
                            val prod = len1 * len2
                            if (prod > maxProd) maxProd = prod
                        }
                    }
                    m2 += 1
                }
            }
        }

        maxProd
    }

    private def isPal(mask: Int, s: String, n: Int): Boolean = {
        var i = 0
        var j = n - 1
        while (i < j) {
            while (i < j && ((mask >> i) & 1) == 0) i += 1
            while (i < j && ((mask >> j) & 1) == 0) j -= 1
            if (i >= j) return true
            if (s.charAt(i) != s.charAt(j)) return false
            i += 1
            j -= 1
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_product(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let total = 1usize << n;
        let mut pal_len = vec![-1i32; total];

        for mask in 0..total {
            // collect indices of selected characters
            let mut idxs = Vec::with_capacity(n);
            for i in 0..n {
                if (mask >> i) & 1 == 1 {
                    idxs.push(i);
                }
            }
            let len = idxs.len();
            if len == 0 {
                pal_len[mask] = 0;
                continue;
            }
            // check palindrome
            let mut ok = true;
            let mut i = 0usize;
            let mut j = len - 1;
            while i < j {
                if bytes[idxs[i]] != bytes[idxs[j]] {
                    ok = false;
                    break;
                }
                i += 1;
                j -= 1;
            }
            if ok {
                pal_len[mask] = len as i32;
            }
        }

        let mut max_prod = 0i32;
        for m1 in 0..total {
            let len1 = pal_len[m1];
            if len1 <= 0 {
                continue;
            }
            // masks disjoint with m1 are subsets of its complement
            let complement = (!m1) & (total - 1);
            let mut sub = complement;
            while sub > 0 {
                let len2 = pal_len[sub];
                if len2 > 0 {
                    let prod = len1 * len2;
                    if prod > max_prod {
                        max_prod = prod;
                    }
                }
                sub = (sub - 1) & complement; // iterate over subsets
            }
        }

        max_prod
    }
}
```

## Racket

```racket
(define/contract (max-product s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (total (arithmetic-shift 1 n))
         (pal-lens (make-vector total 0)))
    ;; compute palindrome lengths for each mask
    (for ([mask (in-range total)])
      (let loop ((i 0) (chars '()))
        (if (= i n)
            (when (and (> (length chars) 0)
                       (equal? chars (reverse chars)))
              (vector-set! pal-lens mask (length chars)))
            (if (zero? (bitwise-and mask (arithmetic-shift 1 i)))
                (loop (+ i 1) chars)
                (loop (+ i 1) (cons (string-ref s i) chars))))))
    ;; find maximum product of two disjoint palindromic subsequences
    (let ((ans 0))
      (for ([mask1 (in-range total)])
        (let ((len1 (vector-ref pal-lens mask1)))
          (when (> len1 0)
            (for ([mask2 (in-range total)])
              (let ((len2 (vector-ref pal-lens mask2)))
                (when (and (> len2 0) (= (bitwise-and mask1 mask2) 0))
                  (let ((prod (* len1 len2)))
                    (when (> prod ans)
                      (set! ans prod)))))))))
      ans)))
```

## Erlang

```erlang
-spec max_product(S :: unicode:unicode_binary()) -> integer().
max_product(S) ->
    L = binary:bin_to_list(S),
    N = length(L),
    MaxMask = (1 bsl N) - 1,
    PalList = [ {Mask, Len} ||
                Mask <- lists:seq(0, MaxMask),
                Sub = mask_to_subseq(Mask, L),
                is_palindrome(Sub),
                Len = length(Sub), Len > 0 ],
    max_product_pairs(PalList).

mask_to_subseq(Mask, List) ->
    mask_to_subseq(Mask, List, 0).

mask_to_subseq(_, [], _) -> [];
mask_to_subseq(Mask, [H|T], Index) ->
    Bit = (Mask bsr Index) band 1,
    Rest = mask_to_subseq(Mask, T, Index + 1),
    case Bit of
        1 -> [H | Rest];
        _ -> Rest
    end.

is_palindrome(Lst) ->
    Lst == lists:reverse(Lst).

max_product_pairs(PalList) ->
    max_product_pairs(PalList, 0).

max_product_pairs([], Max) -> Max;
max_product_pairs([{Mask1, Len1}|Rest], Max) ->
    NewMax = max_with_mask(Mask1, Len1, Rest, Max),
    max_product_pairs(Rest, NewMax).

max_with_mask(_, _, [], Max) -> Max;
max_with_mask(Mask1, Len1, [{Mask2, Len2}|Tail], Max) ->
    case (Mask1 band Mask2) of
        0 ->
            Prod = Len1 * Len2,
            Updated = if Prod > Max -> Prod; true -> Max end,
            max_with_mask(Mask1, Len1, Tail, Updated);
        _ ->
            max_with_mask(Mask1, Len1, Tail, Max)
    end.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec max_product(s :: String.t()) :: integer()
  def max_product(s) do
    chars = String.graphemes(s)
    n = length(chars)
    total = 1 <<< n

    pal_map =
      Enum.reduce(1..(total - 1), %{}, fn mask, acc ->
        seq =
          for i <- 0..(n - 1),
              (mask &&& (1 <<< i)) != 0,
              do: Enum.at(chars, i)

        if seq == Enum.reverse(seq) do
          Map.put(acc, mask, length(seq))
        else
          acc
        end
      end)

    masks = Map.keys(pal_map)

    Enum.reduce(masks, 0, fn m1, cur_max ->
      len1 = pal_map[m1]

      new_max =
        Enum.reduce(masks, cur_max, fn m2, acc2 ->
          if (m1 &&& m2) == 0 do
            prod = len1 * pal_map[m2]
            if prod > acc2, do: prod, else: acc2
          else
            acc2
          end
        end)

      new_max
    end)
  end
end
```
