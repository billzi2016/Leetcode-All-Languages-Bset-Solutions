# 0318. Maximum Product of Word Lengths

## Cpp

```cpp
class Solution {
public:
    int maxProduct(vector<string>& words) {
        int n = words.size();
        vector<int> masks(n);
        vector<int> lens(n);
        for (int i = 0; i < n; ++i) {
            int mask = 0;
            for (char c : words[i]) {
                mask |= 1 << (c - 'a');
            }
            masks[i] = mask;
            lens[i] = words[i].size();
        }
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if ((masks[i] & masks[j]) == 0) {
                    ans = max(ans, lens[i] * lens[j]);
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxProduct(String[] words) {
        int n = words.length;
        int[] masks = new int[n];
        int[] lens = new int[n];
        for (int i = 0; i < n; i++) {
            String w = words[i];
            int mask = 0;
            for (int j = 0; j < w.length(); j++) {
                mask |= 1 << (w.charAt(j) - 'a');
            }
            masks[i] = mask;
            lens[i] = w.length();
        }
        int max = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if ((masks[i] & masks[j]) == 0) {
                    int prod = lens[i] * lens[j];
                    if (prod > max) {
                        max = prod;
                    }
                }
            }
        }
        return max;
    }
}
```

## Python

```python
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        masks = [0] * n
        lengths = [0] * n

        for i, w in enumerate(words):
            mask = 0
            for ch in set(w):  # using set to avoid duplicate work
                mask |= 1 << (ord(ch) - ord('a'))
            masks[i] = mask
            lengths[i] = len(w)

        max_prod = 0
        # optional: sort indices by length descending to allow early break
        idxs = sorted(range(n), key=lambda i: lengths[i], reverse=True)
        for a in range(n):
            i = idxs[a]
            if lengths[i] * lengths[i] <= max_prod:
                break  # further pairs can't beat current max
            for b in range(a + 1, n):
                j = idxs[b]
                potential = lengths[i] * lengths[j]
                if potential <= max_prod:
                    break
                if masks[i] & masks[j] == 0:
                    max_prod = potential
                    break  # since further j will have smaller length

        return max_prod
```

## Python3

```python
from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n
        lens = [0] * n
        for i, w in enumerate(words):
            mask = 0
            for ch in set(w):  # using set to avoid duplicate work
                mask |= 1 << (ord(ch) - ord('a'))
            masks[i] = mask
            lens[i] = len(w)

        max_prod = 0
        for i in range(n):
            mi = masks[i]
            li = lens[i]
            # early skip if potential max can't exceed current max
            for j in range(i + 1, n):
                if mi & masks[j] == 0:
                    prod = li * lens[j]
                    if prod > max_prod:
                        max_prod = prod
        return max_prod
```

## C

```c
#include <stdlib.h>

int maxProduct(char** words, int wordsSize) {
    int *mask = (int *)malloc(sizeof(int) * wordsSize);
    int *len  = (int *)malloc(sizeof(int) * wordsSize);
    for (int i = 0; i < wordsSize; ++i) {
        char *w = words[i];
        int m = 0, l = 0;
        while (*w) {
            m |= 1 << (*w - 'a');
            ++l;
            ++w;
        }
        mask[i] = m;
        len[i] = l;
    }

    int maxProd = 0;
    for (int i = 0; i < wordsSize; ++i) {
        for (int j = i + 1; j < wordsSize; ++j) {
            if ((mask[i] & mask[j]) == 0) {
                int prod = len[i] * len[j];
                if (prod > maxProd) maxProd = prod;
            }
        }
    }

    free(mask);
    free(len);
    return maxProd;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxProduct(string[] words) {
        int n = words.Length;
        int[] masks = new int[n];
        int[] lens = new int[n];
        for (int i = 0; i < n; i++) {
            int mask = 0;
            foreach (char c in words[i]) {
                mask |= 1 << (c - 'a');
            }
            masks[i] = mask;
            lens[i] = words[i].Length;
        }

        int maxProd = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if ((masks[i] & masks[j]) == 0) {
                    int prod = lens[i] * lens[j];
                    if (prod > maxProd) maxProd = prod;
                }
            }
        }
        return maxProd;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @return {number}
 */
var maxProduct = function(words) {
    const n = words.length;
    const masks = new Array(n);
    const lens = new Array(n);
    
    for (let i = 0; i < n; i++) {
        const w = words[i];
        let mask = 0;
        for (const ch of w) {
            mask |= 1 << (ch.charCodeAt(0) - 97);
        }
        masks[i] = mask;
        lens[i] = w.length;
    }
    
    let max = 0;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if ((masks[i] & masks[j]) === 0) {
                const prod = lens[i] * lens[j];
                if (prod > max) max = prod;
            }
        }
    }
    
    return max;
};
```

## Typescript

```typescript
function maxProduct(words: string[]): number {
    const n = words.length;
    const masks: number[] = new Array(n);
    const lens: number[] = new Array(n);
    
    for (let i = 0; i < n; i++) {
        let mask = 0;
        for (const ch of words[i]) {
            mask |= 1 << (ch.charCodeAt(0) - 97);
        }
        masks[i] = mask;
        lens[i] = words[i].length;
    }
    
    let maxProd = 0;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if ((masks[i] & masks[j]) === 0) {
                const prod = lens[i] * lens[j];
                if (prod > maxProd) maxProd = prod;
            }
        }
    }
    
    return maxProd;
}
```

## Php

```php
class Solution {
    /**
     * @param String[] $words
     * @return Integer
     */
    function maxProduct($words) {
        $n = count($words);
        $masks = [];
        $lens = [];

        foreach ($words as $idx => $word) {
            $mask = 0;
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) {
                $c = ord($word[$i]) - 97;
                $mask |= (1 << $c);
            }
            $masks[$idx] = $mask;
            $lens[$idx] = $len;
        }

        $maxProd = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                if (($masks[$i] & $masks[$j]) === 0) {
                    $prod = $lens[$i] * $lens[$j];
                    if ($prod > $maxProd) {
                        $maxProd = $prod;
                    }
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
    func maxProduct(_ words: [String]) -> Int {
        let n = words.count
        var masks = [Int](repeating: 0, count: n)
        var lengths = [Int](repeating: 0, count: n)

        for i in 0..<n {
            var mask = 0
            for scalar in words[i].unicodeScalars {
                let bit = Int(scalar.value - 97) // 'a' ascii is 97
                mask |= (1 << bit)
            }
            masks[i] = mask
            lengths[i] = words[i].count
        }

        var maxProd = 0
        for i in 0..<n {
            for j in i+1..<n {
                if (masks[i] & masks[j]) == 0 {
                    let prod = lengths[i] * lengths[j]
                    if prod > maxProd { maxProd = prod }
                }
            }
        }
        return maxProd
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxProduct(words: Array<String>): Int {
        val n = words.size
        val masks = IntArray(n)
        val lens = IntArray(n)
        for (i in 0 until n) {
            var mask = 0
            for (c in words[i]) {
                mask = mask or (1 shl (c - 'a'))
            }
            masks[i] = mask
            lens[i] = words[i].length
        }
        var maxProd = 0
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                if ((masks[i] and masks[j]) == 0) {
                    val prod = lens[i] * lens[j]
                    if (prod > maxProd) maxProd = prod
                }
            }
        }
        return maxProd
    }
}
```

## Dart

```dart
class Solution {
  int maxProduct(List<String> words) {
    int n = words.length;
    List<int> masks = List.filled(n, 0);
    List<int> lens = List.filled(n, 0);

    for (int i = 0; i < n; i++) {
      String w = words[i];
      int mask = 0;
      for (int j = 0; j < w.length; j++) {
        int bit = w.codeUnitAt(j) - 97; // 'a' ascii code
        mask |= (1 << bit);
      }
      masks[i] = mask;
      lens[i] = w.length;
    }

    int maxProd = 0;
    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        if ((masks[i] & masks[j]) == 0) {
          int prod = lens[i] * lens[j];
          if (prod > maxProd) maxProd = prod;
        }
      }
    }

    return maxProd;
  }
}
```

## Golang

```go
func maxProduct(words []string) int {
	n := len(words)
	masks := make([]int, n)
	lengths := make([]int, n)

	for i, w := range words {
		mask := 0
		for _, ch := range w {
			mask |= 1 << (ch - 'a')
		}
		masks[i] = mask
		lengths[i] = len(w)
	}

	maxProd := 0
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if masks[i]&masks[j] == 0 {
				prod := lengths[i] * lengths[j]
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
def max_product(words)
  n = words.length
  masks = Array.new(n, 0)
  lengths = Array.new(n, 0)

  words.each_with_index do |w, i|
    mask = 0
    w.each_byte { |c| mask |= 1 << (c - 97) }
    masks[i] = mask
    lengths[i] = w.length
  end

  max_prod = 0
  (0...n).each do |i|
    ((i + 1)...n).each do |j|
      if (masks[i] & masks[j]).zero?
        prod = lengths[i] * lengths[j]
        max_prod = prod if prod > max_prod
      end
    end
  end

  max_prod
end
```

## Scala

```scala
object Solution {
  def maxProduct(words: Array[String]): Int = {
    val n = words.length
    val masks = new Array[Int](n)
    val lens = new Array[Int](n)

    var i = 0
    while (i < n) {
      var mask = 0
      val w = words(i)
      var k = 0
      while (k < w.length) {
        mask |= 1 << (w.charAt(k) - 'a')
        k += 1
      }
      masks(i) = mask
      lens(i) = w.length
      i += 1
    }

    var maxProd = 0
    i = 0
    while (i < n) {
      var j = i + 1
      while (j < n) {
        if ((masks(i) & masks(j)) == 0) {
          val prod = lens(i) * lens(j)
          if (prod > maxProd) maxProd = prod
        }
        j += 1
      }
      i += 1
    }

    maxProd
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_product(words: Vec<String>) -> i32 {
        let n = words.len();
        let mut masks: Vec<(u32, i32)> = Vec::with_capacity(n);
        for w in &words {
            let mut mask: u32 = 0;
            for b in w.bytes() {
                mask |= 1 << ((b - b'a') as u32);
            }
            masks.push((mask, w.len() as i32));
        }

        let mut max_prod = 0;
        for i in 0..n {
            for j in (i + 1)..n {
                if masks[i].0 & masks[j].0 == 0 {
                    let prod = masks[i].1 * masks[j].1;
                    if prod > max_prod {
                        max_prod = prod;
                    }
                }
            }
        }
        max_prod
    }
}
```

## Racket

```racket
(require racket/contract)

(define/contract (max-product words)
  (-> (listof string?) exact-integer?)
  (let* ((n (length words))
         (len-vec (make-vector n))
         (mask-vec (make-vector n)))
    (for ([w words] [i (in-range n)])
      (vector-set! len-vec i (string-length w))
      (vector-set! mask-vec i
                   (let loop ((idx 0) (m 0))
                     (if (= idx (string-length w))
                         m
                         (let* ((c (string-ref w idx))
                                (bit (- (char->integer c)
                                        (char->integer #\a))))
                           (loop (+ idx 1)
                                 (bitwise-ior m (arithmetic-shift 1 bit))))))))
    (let loop ((i 0) (best 0))
      (if (>= i (- n 1))
          best
          (let* ((len-i (vector-ref len-vec i))
                 (mask-i (vector-ref mask-vec i)))
            (let inner ((j (+ i 1)) (cur best))
              (if (>= j n)
                  (loop (+ i 1) cur)
                  (let* ((len-j (vector-ref len-vec j))
                         (mask-j (vector-ref mask-vec j))
                         (prod (* len-i len-j)))
                    (if (= (bitwise-and mask-i mask-j) 0)
                        (inner (+ j 1) (max cur prod))
                        (inner (+ j 1) cur))))))))))
```

## Erlang

```erlang
-module(solution).
-export([max_product/1]).
-spec max_product(Words :: [unicode:unicode_binary()]) -> integer().
max_product(Words) ->
    WordInfos = [{mask_word(W), byte_size(W)} || W <- Words],
    max_pair_loop(WordInfos, 0).

mask_word(Bin) ->
    lists:foldl(fun(C, Acc) -> Acc bor (1 bsl (C - $a)) end,
                0,
                binary_to_list(Bin)).

max_pair_loop([], Max) ->
    Max;
max_pair_loop([H|T], Max) ->
    NewMax = max_with_rest(H, T, Max),
    max_pair_loop(T, NewMax).

max_with_rest(_, [], Max) ->
    Max;
max_with_rest({Mask1, Len1}, [{Mask2, Len2}|Rest], Max) ->
    case (Mask1 band Mask2) of
        0 ->
            Prod = Len1 * Len2,
            Updated = if Prod > Max -> Prod; true -> Max end,
            max_with_rest({Mask1, Len1}, Rest, Updated);
        _ ->
            max_with_rest({Mask1, Len1}, Rest, Max)
    end.
```

## Elixir

```elixir
defmodule Solution do
  import Bitwise

  @spec max_product(words :: [String.t]) :: integer
  def max_product(words) do
    masks =
      Enum.map(words, fn w ->
        mask =
          w
          |> String.to_charlist()
          |> Enum.reduce(0, fn c, acc -> acc ||| (1 <<< (c - ?a)) end)

        {mask, String.length(w)}
      end)

    n = length(masks)
    max_product_recursive(masks, n, 0, 0)
  end

  defp max_product_recursive(_masks, n, i, current_max) when i >= n - 1,
    do: current_max

  defp max_product_recursive(masks, n, i, current_max) do
    {mask_i, len_i} = Enum.at(masks, i)

    new_max =
      Enum.reduce((i + 1)..(n - 1), current_max, fn j, acc ->
        {mask_j, len_j} = Enum.at(masks, j)

        if (mask_i &&& mask_j) == 0 do
          prod = len_i * len_j
          if prod > acc, do: prod, else: acc
        else
          acc
        end
      end)

    max_product_recursive(masks, n, i + 1, new_max)
  end
end
```
