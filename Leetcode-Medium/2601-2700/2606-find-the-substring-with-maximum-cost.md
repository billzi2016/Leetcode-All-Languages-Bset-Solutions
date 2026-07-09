# 2606. Find the Substring With Maximum Cost

## Cpp

```cpp
class Solution {
public:
    int maximumCostSubstring(string s, string chars, vector<int>& vals) {
        // Initialize all character values to 1
        vector<int> value(26, 1);
        for (size_t i = 0; i < chars.size(); ++i) {
            value[chars[i] - 'a'] = vals[i];
        }
        
        long long cur = 0;
        long long best = 0;
        for (char c : s) {
            cur += value[c - 'a'];
            if (cur < 0) cur = 0;
            if (cur > best) best = cur;
        }
        return static_cast<int>(best);
    }
};
```

## Java

```java
class Solution {
    public int maximumCostSubstring(String s, String chars, int[] vals) {
        int[] value = new int[26];
        // default value is 1 for all letters
        for (int i = 0; i < 26; i++) {
            value[i] = 1;
        }
        // set custom values
        for (int i = 0; i < chars.length(); i++) {
            value[chars.charAt(i) - 'a'] = vals[i];
        }

        int maxSoFar = 0;
        int cur = 0;
        for (int i = 0; i < s.length(); i++) {
            int v = value[s.charAt(i) - 'a'];
            cur = Math.max(v, cur + v);
            if (cur > maxSoFar) {
                maxSoFar = cur;
            }
        }
        return maxSoFar;
    }
}
```

## Python

```python
class Solution(object):
    def maximumCostSubstring(self, s, chars, vals):
        """
        :type s: str
        :type chars: str
        :type vals: List[int]
        :rtype: int
        """
        value_map = {c: v for c, v in zip(chars, vals)}
        max_sum = 0
        cur = 0
        for ch in s:
            v = value_map.get(ch, 1)
            cur = max(v, cur + v)
            if cur > max_sum:
                max_sum = cur
        return max_sum
```

## Python3

```python
from typing import List

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        value_map = {c: v for c, v in zip(chars, vals)}
        max_ending = 0
        max_total = 0
        for ch in s:
            cur = value_map.get(ch, 1)
            max_ending = max(0, max_ending + cur)
            if max_ending > max_total:
                max_total = max_ending
        return max_total
```

## C

```c
int maximumCostSubstring(char* s, char* chars, int* vals, int valsSize) {
    int value[26];
    for (int i = 0; i < 26; ++i) value[i] = 1;
    for (int i = 0; i < valsSize; ++i) {
        char c = chars[i];
        value[c - 'a'] = vals[i];
    }
    long long cur = 0, best = 0;
    for (int i = 0; s[i]; ++i) {
        cur += value[s[i] - 'a'];
        if (cur < 0) cur = 0;
        if (cur > best) best = cur;
    }
    return (int)best;
}
```

## Csharp

```csharp
public class Solution {
    public int MaximumCostSubstring(string s, string chars, int[] vals) {
        int[] value = new int[26];
        for (int i = 0; i < 26; i++) value[i] = 1;
        for (int i = 0; i < chars.Length; i++) {
            value[chars[i] - 'a'] = vals[i];
        }
        int maxSoFar = 0;
        int cur = 0;
        foreach (char c in s) {
            int v = value[c - 'a'];
            cur = System.Math.Max(v, cur + v);
            if (cur > maxSoFar) maxSoFar = cur;
        }
        return maxSoFar;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} chars
 * @param {number[]} vals
 * @return {number}
 */
var maximumCostSubstring = function(s, chars, vals) {
    const base = new Array(26).fill(1);
    for (let i = 0; i < chars.length; ++i) {
        const idx = chars.charCodeAt(i) - 97;
        base[idx] = vals[i];
    }
    let cur = 0, best = 0;
    for (let i = 0; i < s.length; ++i) {
        const v = base[s.charCodeAt(i) - 97];
        cur = Math.max(0, cur + v);
        if (cur > best) best = cur;
    }
    return best;
};
```

## Typescript

```typescript
function maximumCostSubstring(s: string, chars: string, vals: number[]): number {
    const valueMap = new Map<string, number>();
    for (let i = 0; i < chars.length; i++) {
        valueMap.set(chars[i], vals[i]);
    }

    let maxSum = 0;
    let cur = 0;
    for (const ch of s) {
        const v = valueMap.has(ch) ? valueMap.get(ch)! : 1;
        cur = Math.max(0, cur + v);
        if (cur > maxSum) maxSum = cur;
    }
    return maxSum;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $chars
     * @param Integer[] $vals
     * @return Integer
     */
    function maximumCostSubstring($s, $chars, $vals) {
        $map = [];
        $lenChars = strlen($chars);
        for ($i = 0; $i < $lenChars; $i++) {
            $map[$chars[$i]] = $vals[$i];
        }

        $maxEndingHere = 0;
        $maxSoFar = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            $value = $map[$c] ?? 1;
            $maxEndingHere = max(0, $maxEndingHere + $value);
            if ($maxEndingHere > $maxSoFar) {
                $maxSoFar = $maxEndingHere;
            }
        }

        return $maxSoFar;
    }
}
```

## Swift

```swift
class Solution {
    func maximumCostSubstring(_ s: String, _ chars: String, _ vals: [Int]) -> Int {
        var valueMap = [Character: Int]()
        for (c, v) in zip(chars, vals) {
            valueMap[c] = v
        }
        var current = 0
        var best = 0
        for ch in s {
            let val = valueMap[ch] ?? 1
            current = max(0, current + val)
            if current > best { best = current }
        }
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maximumCostSubstring(s: String, chars: String, vals: IntArray): Int {
        val value = IntArray(26) { 1 }
        for (i in chars.indices) {
            value[chars[i] - 'a'] = vals[i]
        }
        var maxEndingHere = 0
        var maxSoFar = 0
        for (ch in s) {
            val v = value[ch - 'a']
            maxEndingHere = kotlin.math.max(0, maxEndingHere + v)
            if (maxEndingHere > maxSoFar) {
                maxSoFar = maxEndingHere
            }
        }
        return maxSoFar
    }
}
```

## Dart

```dart
class Solution {
  int maximumCostSubstring(String s, String chars, List<int> vals) {
    // Initialize all character values to 1
    List<int> charValues = List.filled(26, 1);
    for (int i = 0; i < chars.length; i++) {
      int idx = chars.codeUnitAt(i) - 97;
      charValues[idx] = vals[i];
    }

    int maxCost = 0;
    int current = 0;

    for (int i = 0; i < s.length; i++) {
      int v = charValues[s.codeUnitAt(i) - 97];
      current += v;
      if (current < 0) current = 0;
      if (current > maxCost) maxCost = current;
    }

    return maxCost;
  }
}
```

## Golang

```go
func maximumCostSubstring(s string, chars string, vals []int) int {
    // Initialize values for all lowercase letters to default value 1
    charVals := make([]int, 26)
    for i := 0; i < 26; i++ {
        charVals[i] = 1
    }
    // Override with given values for characters in 'chars'
    for i, ch := range chars {
        idx := ch - 'a'
        charVals[idx] = vals[i]
    }

    maxSum, cur := 0, 0
    for _, c := range s {
        v := charVals[c-'a']
        cur += v
        if cur < 0 {
            cur = 0
        }
        if cur > maxSum {
            maxSum = cur
        }
    }
    return maxSum
}
```

## Ruby

```ruby
def maximum_cost_substring(s, chars, vals)
  value_map = {}
  chars.each_char.with_index { |ch, i| value_map[ch] = vals[i] }

  max_sum = 0
  current = 0

  s.each_char do |c|
    v = value_map.fetch(c, 1)
    current += v
    current = 0 if current < 0
    max_sum = current if current > max_sum
  end

  max_sum
end
```

## Scala

```scala
object Solution {
    def maximumCostSubstring(s: String, chars: String, vals: Array[Int]): Int = {
        val valueMap = scala.collection.mutable.HashMap[Char, Int]()
        for (i <- chars.indices) {
            valueMap(chars(i)) = vals(i)
        }
        var maxEndingHere = 0
        var maxSoFar = 0
        for (c <- s) {
            val v = valueMap.getOrElse(c, 1)
            maxEndingHere = math.max(v, maxEndingHere + v)
            maxSoFar = math.max(maxSoFar, maxEndingHere)
        }
        maxSoFar
    }
}
```

## Rust

```rust
impl Solution {
    pub fn maximum_cost_substring(s: String, chars: String, vals: Vec<i32>) -> i32 {
        let mut value = [1i32; 26];
        for (c, v) in chars.chars().zip(vals.iter()) {
            let idx = (c as u8 - b'a') as usize;
            value[idx] = *v;
        }
        let mut max_ending_here: i32 = 0;
        let mut max_sofar: i32 = 0;
        for ch in s.chars() {
            let idx = (ch as u8 - b'a') as usize;
            let val = value[idx];
            max_ending_here = (max_ending_here + val).max(0);
            if max_ending_here > max_sofar {
                max_sofar = max_ending_here;
            }
        }
        max_sofar
    }
}
```

## Racket

```racket
(define/contract (maximum-cost-substring s chars vals)
  (-> string? string? (listof exact-integer?) exact-integer?)
  (let* ((len-s (string-length s))
         (len-c (string-length chars))
         (h (make-hash)))
    ;; map each character in `chars` to its corresponding value
    (for ([i (in-range len-c)])
      (hash-set! h (string-ref chars i) (list-ref vals i)))
    (let loop ((i 0) (cur 0) (best 0))
      (if (= i len-s)
          best
          (let* ((ch (string-ref s i))
                 (val (if (hash-has-key? h ch) (hash-ref h ch) 1))
                 (new-cur (+ cur val))
                 (next-cur (max new-cur 0))
                 (next-best (max best next-cur)))
            (loop (+ i 1) next-cur next-best))))))
```

## Erlang

```erlang
-module(solution).
-export([maximum_cost_substring/3]).

-spec maximum_cost_substring(S :: unicode:unicode_binary(), Chars :: unicode:unicode_binary(), Vals :: [integer()]) -> integer().
maximum_cost_substring(S, Chars, Vals) ->
    CharList = unicode:characters_to_list(Chars),
    CharMap = maps:from_list(lists:zip(CharList, Vals)),
    {_, Max} =
        lists:foldl(
            fun(C, {Curr, MaxAcc}) ->
                Val = maps:get(C, CharMap, 1),
                NewCurr = erlang:max(Val, Curr + Val),
                NewMax = erlang:max(MaxAcc, NewCurr),
                {NewCurr, NewMax}
            end,
            {0, 0},
            unicode:characters_to_list(S)
        ),
    Max.
```

## Elixir

```elixir
defmodule Solution do
  @spec maximum_cost_substring(s :: String.t(), chars :: String.t(), vals :: [integer()]) :: integer()
  def maximum_cost_substring(s, chars, vals) do
    char_vals =
      chars
      |> String.graphemes()
      |> Enum.zip(vals)
      |> Map.new()

    {max_sum, _} =
      s
      |> String.graphemes()
      |> Enum.reduce({0, 0}, fn ch, {max_sofar, cur} ->
        v = Map.get(char_vals, ch, 1)
        new_cur = max(v, cur + v)
        new_max = max(max_sofar, new_cur)
        {new_max, new_cur}
      end)

    max_sum
  end
end
```
