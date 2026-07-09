# 1239. Maximum Length of a Concatenated String with Unique Characters

## Cpp

```cpp
class Solution {
public:
    int maxLength(vector<string>& arr) {
        vector<int> masks;
        for (const string& s : arr) {
            int mask = 0;
            bool ok = true;
            for (char ch : s) {
                int bit = 1 << (ch - 'a');
                if (mask & bit) { // duplicate character in the same string
                    ok = false;
                    break;
                }
                mask |= bit;
            }
            if (ok) masks.push_back(mask);
        }
        int ans = 0;
        function<void(int,int)> dfs = [&](int idx, int curMask) {
            ans = max(ans, __builtin_popcount(curMask));
            for (int i = idx; i < (int)masks.size(); ++i) {
                if ((curMask & masks[i]) == 0) {
                    dfs(i + 1, curMask | masks[i]);
                }
            }
        };
        dfs(0, 0);
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private int max = 0;

    public int maxLength(List<String> arr) {
        List<Integer> masks = new ArrayList<>();
        for (String s : arr) {
            int mask = 0;
            boolean duplicate = false;
            for (char c : s.toCharArray()) {
                int bit = 1 << (c - 'a');
                if ((mask & bit) != 0) {
                    duplicate = true;
                    break;
                }
                mask |= bit;
            }
            if (!duplicate) {
                masks.add(mask);
            }
        }
        dfs(0, 0, masks);
        return max;
    }

    private void dfs(int index, int curMask, List<Integer> masks) {
        max = Math.max(max, Integer.bitCount(curMask));
        for (int i = index; i < masks.size(); i++) {
            int m = masks.get(i);
            if ((curMask & m) == 0) {
                dfs(i + 1, curMask | m, masks);
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        # Convert each string to a bitmask; discard strings with duplicate chars.
        masks = []
        for s in arr:
            mask = 0
            dup = False
            for ch in s:
                bit = 1 << (ord(ch) - ord('a'))
                if mask & bit:
                    dup = True
                    break
                mask |= bit
            if not dup:
                masks.append(mask)

        self.best = 0

        def dfs(idx, cur_mask):
            # Update best length using popcount of current mask.
            cur_len = cur_mask.bit_count() if hasattr(int, "bit_count") else bin(cur_mask).count("1")
            if cur_len > self.best:
                self.best = cur_len
            for i in range(idx, len(masks)):
                m = masks[i]
                if cur_mask & m == 0:   # no overlapping characters
                    dfs(i + 1, cur_mask | m)

        dfs(0, 0)
        return self.best
```

## Python3

```python
from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = []
        for s in arr:
            mask = 0
            duplicate = False
            for ch in s:
                bit = 1 << (ord(ch) - ord('a'))
                if mask & bit:
                    duplicate = True
                    break
                mask |= bit
            if not duplicate:
                masks.append(mask)

        self.best = 0

        def dfs(idx: int, cur_mask: int):
            self.best = max(self.best, cur_mask.bit_count())
            for i in range(idx, len(masks)):
                if cur_mask & masks[i] == 0:
                    dfs(i + 1, cur_mask | masks[i])

        dfs(0, 0)
        return self.best
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

int maxLength(char** arr, int arrSize) {
    int strMasks[16];
    int n = 0;
    for (int i = 0; i < arrSize; ++i) {
        char *s = arr[i];
        int mask = 0;
        bool ok = true;
        for (int j = 0; s[j]; ++j) {
            int bit = 1 << (s[j] - 'a');
            if (mask & bit) { ok = false; break; }
            mask |= bit;
        }
        if (ok) strMasks[n++] = mask;
    }

    int maxCombos = 1 << 16;               // maximum possible combinations
    int *combos = (int *)malloc(sizeof(int) * maxCombos);
    int comboCount = 0;
    combos[comboCount++] = 0;              // start with empty string

    int ans = 0;

    for (int i = 0; i < n; ++i) {
        int curMask = strMasks[i];
        int oldCount = comboCount;
        for (int j = 0; j < oldCount; ++j) {
            if ((combos[j] & curMask) == 0) {
                int newMask = combos[j] | curMask;
                combos[comboCount++] = newMask;
                int len = __builtin_popcount(newMask);
                if (len > ans) ans = len;
            }
        }
    }

    free(combos);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Numerics;

public class Solution {
    public int MaxLength(IList<string> arr) {
        var masks = new List<int>();
        foreach (var s in arr) {
            int mask = 0;
            bool duplicate = false;
            foreach (char ch in s) {
                int bit = 1 << (ch - 'a');
                if ((mask & bit) != 0) {
                    duplicate = true;
                    break;
                }
                mask |= bit;
            }
            if (!duplicate) masks.Add(mask);
        }

        int maxLen = 0;

        void Dfs(int index, int curMask) {
            int len = BitOperations.PopCount((uint)curMask);
            if (len > maxLen) maxLen = len;

            for (int i = index; i < masks.Count; i++) {
                int m = masks[i];
                if ((curMask & m) == 0) {
                    Dfs(i + 1, curMask | m);
                }
            }
        }

        Dfs(0, 0);
        return maxLen;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} arr
 * @return {number}
 */
var maxLength = function(arr) {
    const masks = [];
    for (const s of arr) {
        let mask = 0;
        let dup = false;
        for (let i = 0; i < s.length; i++) {
            const bit = 1 << (s.charCodeAt(i) - 97);
            if ((mask & bit) !== 0) { // duplicate char in the same string
                dup = true;
                break;
            }
            mask |= bit;
        }
        if (!dup) masks.push(mask);
    }

    const popcnt = (x) => {
        let cnt = 0;
        while (x) {
            x &= x - 1;
            cnt++;
        }
        return cnt;
    };

    let dp = [0];
    let maxLen = 0;

    for (const m of masks) {
        const newCombos = [];
        for (const cur of dp) {
            if ((cur & m) === 0) { // no overlapping characters
                const combined = cur | m;
                newCombos.push(combined);
                const len = popcnt(combined);
                if (len > maxLen) maxLen = len;
            }
        }
        dp = dp.concat(newCombos);
    }

    return maxLen;
};
```

## Typescript

```typescript
function maxLength(arr: string[]): number {
    const masks: number[] = [];
    for (const s of arr) {
        let mask = 0;
        let dup = false;
        for (const ch of s) {
            const bit = 1 << (ch.charCodeAt(0) - 97);
            if ((mask & bit) !== 0) {
                dup = true;
                break;
            }
            mask |= bit;
        }
        if (!dup) masks.push(mask);
    }

    const dp: number[] = [0];
    let maxLen = 0;

    const bitCount = (x: number): number => {
        let cnt = 0;
        while (x) {
            x &= x - 1;
            cnt++;
        }
        return cnt;
    };

    for (const m of masks) {
        const curSize = dp.length;
        for (let i = 0; i < curSize; i++) {
            const existing = dp[i];
            if ((existing & m) === 0) {
                const newMask = existing | m;
                dp.push(newMask);
                const len = bitCount(newMask);
                if (len > maxLen) maxLen = len;
            }
        }
    }

    return maxLen;
}
```

## Php

```php
class Solution {
    /**
     * @param String[] $arr
     * @return Integer
     */
    function maxLength($arr) {
        $masks = [];
        foreach ($arr as $s) {
            $mask = 0;
            $valid = true;
            $len = strlen($s);
            for ($i = 0; $i < $len; $i++) {
                $c = ord($s[$i]) - 97; // 'a' = 97
                if (($mask >> $c) & 1) {
                    $valid = false;
                    break;
                }
                $mask |= (1 << $c);
            }
            if ($valid) {
                $masks[] = $mask;
            }
        }

        $this->maxLen = 0;
        $n = count($masks);
        $this->dfs(0, 0, $masks, $n);
        return $this->maxLen;
    }

    private function dfs($idx, $curMask, &$masks, $n) {
        $len = $this->bitCount($curMask);
        if ($len > $this->maxLen) {
            $this->maxLen = $len;
        }
        for ($i = $idx; $i < $n; $i++) {
            if (($curMask & $masks[$i]) === 0) {
                $this->dfs($i + 1, $curMask | $masks[$i], $masks, $n);
            }
        }
    }

    private function bitCount($x) {
        $cnt = 0;
        while ($x) {
            $cnt += $x & 1;
            $x >>= 1;
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func maxLength(_ arr: [String]) -> Int {
        var masks = [Int]()
        for s in arr {
            var mask = 0
            var hasDuplicate = false
            for byte in s.utf8 {
                let bit = 1 << (Int(byte) - 97)
                if (mask & bit) != 0 {
                    hasDuplicate = true
                    break
                }
                mask |= bit
            }
            if !hasDuplicate {
                masks.append(mask)
            }
        }
        
        var maxLen = 0
        
        func dfs(_ index: Int, _ curMask: Int) {
            let curLen = curMask.nonzeroBitCount
            if curLen > maxLen { maxLen = curLen }
            for i in index..<masks.count {
                let m = masks[i]
                if (curMask & m) == 0 {
                    dfs(i + 1, curMask | m)
                }
            }
        }
        
        dfs(0, 0)
        return maxLen
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxLength(arr: List<String>): Int {
        val masks = mutableListOf<Int>()
        for (s in arr) {
            var mask = 0
            var duplicate = false
            for (ch in s) {
                val bit = 1 shl (ch - 'a')
                if ((mask and bit) != 0) {
                    duplicate = true
                    break
                }
                mask = mask or bit
            }
            if (!duplicate) masks.add(mask)
        }

        var maxLen = 0

        fun dfs(index: Int, curMask: Int, curLen: Int) {
            if (curLen > maxLen) maxLen = curLen
            for (i in index until masks.size) {
                val m = masks[i]
                if ((curMask and m) == 0) {
                    dfs(i + 1, curMask or m, curLen + Integer.bitCount(m))
                }
            }
        }

        dfs(0, 0, 0)
        return maxLen
    }
}
```

## Dart

```dart
class Solution {
  int maxLength(List<String> arr) {
    List<int> masks = [];
    for (var s in arr) {
      int mask = 0;
      bool dup = false;
      for (int i = 0; i < s.length; i++) {
        int bit = 1 << (s.codeUnitAt(i) - 97);
        if ((mask & bit) != 0) {
          dup = true;
          break;
        }
        mask |= bit;
      }
      if (!dup) masks.add(mask);
    }

    int n = masks.length;

    int dfs(int idx, int curMask) {
      int best = _popCount(curMask);
      for (int i = idx; i < n; i++) {
        if ((curMask & masks[i]) == 0) {
          int cand = dfs(i + 1, curMask | masks[i]);
          if (cand > best) best = cand;
        }
      }
      return best;
    }

    return dfs(0, 0);
  }

  int _popCount(int x) {
    int cnt = 0;
    while (x != 0) {
      x &= x - 1;
      cnt++;
    }
    return cnt;
  }
}
```

## Golang

```go
import "math/bits"

func maxLength(arr []string) int {
	masks := make([]int, 0, len(arr))
	for _, s := range arr {
		m := 0
		dup := false
		for i := 0; i < len(s); i++ {
			bit := 1 << (s[i] - 'a')
			if m&bit != 0 {
				dup = true
				break
			}
			m |= bit
		}
		if !dup {
			masks = append(masks, m)
		}
	}

	maxAns := 0
	var dfs func(int, int)
	dfs = func(idx, curMask int) {
		if l := bits.OnesCount(uint(curMask)); l > maxAns {
			maxAns = l
		}
		for i := idx; i < len(masks); i++ {
			if curMask&masks[i] == 0 {
				dfs(i+1, curMask|masks[i])
			}
		}
	}

	dfs(0, 0)
	return maxAns
}
```

## Ruby

```ruby
def max_length(arr)
  masks = []
  arr.each do |s|
    mask = 0
    dup = false
    s.each_char do |ch|
      bit = 1 << (ch.ord - 97)
      if (mask & bit) != 0
        dup = true
        break
      end
      mask |= bit
    end
    masks << mask unless dup
  end

  max_len = 0
  dfs = nil
  dfs = lambda do |idx, cur_mask|
    len = cur_mask.to_s(2).count('1')
    max_len = len if len > max_len
    (idx...masks.size).each do |i|
      next if (cur_mask & masks[i]) != 0
      dfs.call(i + 1, cur_mask | masks[i])
    end
  end

  dfs.call(0, 0)
  max_len
end
```

## Scala

```scala
object Solution {
    def maxLength(arr: List[String]): Int = {
        val masks: Array[Int] = arr.flatMap { s =>
            var mask = 0
            var dup = false
            for (c <- s) {
                val bit = 1 << (c - 'a')
                if ((mask & bit) != 0) {
                    dup = true
                } else {
                    mask |= bit
                }
            }
            if (!dup) Some(mask) else None
        }.toArray

        var maxLen = 0

        def dfs(idx: Int, curMask: Int, curLen: Int): Unit = {
            if (curLen > maxLen) maxLen = curLen
            var i = idx
            while (i < masks.length) {
                val m = masks(i)
                if ((curMask & m) == 0) {
                    dfs(i + 1, curMask | m, curLen + Integer.bitCount(m))
                }
                i += 1
            }
        }

        dfs(0, 0, 0)
        maxLen
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_length(arr: Vec<String>) -> i32 {
        fn mask_of(s: &str) -> Option<u32> {
            let mut mask = 0u32;
            for b in s.bytes() {
                let bit = 1 << (b - b'a');
                if mask & bit != 0 {
                    return None;
                }
                mask |= bit;
            }
            Some(mask)
        }

        let mut valid: Vec<(u32, usize)> = Vec::new();
        for s in arr.iter() {
            if let Some(m) = mask_of(s) {
                valid.push((m, s.len()));
            }
        }

        let mut combos: Vec<(u32, usize)> = vec![(0, 0)];
        let mut max_len = 0usize;

        for (mask_i, len_i) in valid {
            let cur = combos.len();
            for i in 0..cur {
                let (mask_j, len_j) = combos[i];
                if mask_j & mask_i == 0 {
                    let new_mask = mask_j | mask_i;
                    let new_len = len_j + len_i;
                    combos.push((new_mask, new_len));
                    if new_len > max_len {
                        max_len = new_len;
                    }
                }
            }
        }

        max_len as i32
    }
}
```

## Racket

```racket
(define/contract (max-length arr)
  (-> (listof string?) exact-integer?)
  (let* ((string-mask
          (lambda (s)
            (let loop ((i 0) (mask 0))
              (if (= i (string-length s))
                  mask
                  (let* ((c (string-ref s i))
                         (bit (arithmetic-shift 1 (- (char->integer c) (char->integer #\a)))))
                    (if (zero? (bitwise-and mask bit))
                        (loop (+ i 1) (bitwise-ior mask bit))
                        -1))))))
         (pairs
          (for/list ([s arr])
            (let ((m ((string-mask) s)))
              (if (= m -1)
                  #f
                  (list m (string-length s))))))
         (filtered (filter identity pairs))
         (masks (list->vector (map car filtered)))
         (lens  (list->vector (map cadr filtered)))
         (n (vector-length masks)))
    (let rec ((idx 0) (cur-mask 0))
      (if (= idx n)
          0
          (let ((m (vector-ref masks idx))
                (len (vector-ref lens idx)))
            (if (zero? (bitwise-and cur-mask m))
                (max (rec (+ idx 1) cur-mask)
                     (+ len (rec (+ idx 1) (bitwise-ior cur-mask m))))
                (rec (+ idx 1) cur-mask)))))))
```

## Erlang

```erlang
-module(solution).
-export([max_length/1]).

-spec max_length(Arr :: [unicode:unicode_binary()]) -> integer().
max_length(Arr) ->
    Masks = [Mask || S <- Arr,
                     {ok, Mask} <- [mask_of_binary(S, 0)]],
    {_, MaxLen} = lists:foldl(
        fun(M, {CurrMasks, CurMax}) ->
            NewMasks = [Cur bor M || Cur <- CurrMasks, (Cur band M) == 0],
            UpdatedMasks = CurrMasks ++ NewMasks,
            NewMax = max(CurMax, max_new_len(NewMasks)),
            {UpdatedMasks, NewMax}
        end,
        {[0], 0},
        Masks),
    MaxLen.

mask_of_binary(<<>>, Mask) -> {ok, Mask};
mask_of_binary(<<C, Rest/binary>>, Mask) ->
    Bit = 1 bsl (C - $a),
    case (Mask band Bit) of
        0 -> mask_of_binary(Rest, Mask bor Bit);
        _ -> error
    end.

popcount(N) -> popcount(N, 0).
popcount(0, Acc) -> Acc;
popcount(N, Acc) ->
    popcount(N band (N-1), Acc + 1).

max_new_len([]) -> 0;
max_new_len(List) ->
    lists:max([popcount(M) || M <- List] ++ [0]).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec max_length(arr :: [String.t()]) :: integer()
  def max_length(arr) do
    masks =
      arr
      |> Enum.map(&string_to_mask/1)
      |> Enum.filter(& &1 != nil)

    {max_len, _} =
      Enum.reduce(masks, {0, [0]}, fn mask, {cur_max, dp_masks} ->
        new_combinations =
          for existing <- dp_masks,
              (existing &&& mask) == 0 do
            existing ||| mask
          end

        new_max =
          Enum.reduce(new_combinations, cur_max, fn m, acc ->
            len = bit_count(m)
            if len > acc, do: len, else: acc
          end)

        {new_max, dp_masks ++ new_combinations}
      end)

    max_len
  end

  defp string_to_mask(str) do
    chars = String.to_charlist(str)

    Enum.reduce_while(chars, 0, fn c, acc ->
      bit = 1 <<< (c - ?a)

      if (acc &&& bit) != 0 do
        {:halt, nil}
      else
        {:cont, acc ||| bit}
      end
    end)
  end

  defp bit_count(0), do: 0

  defp bit_count(n) do
    count_bits(n, 0)
  end

  defp count_bits(0, cnt), do: cnt

  defp count_bits(n, cnt) do
    count_bits(n &&& (n - 1), cnt + 1)
  end
end
```
