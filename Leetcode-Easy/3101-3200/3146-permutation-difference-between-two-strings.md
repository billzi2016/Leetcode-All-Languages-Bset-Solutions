# 3146. Permutation Difference between Two Strings

## Cpp

```cpp
class Solution {
public:
    int findPermutationDifference(string s, string t) {
        int pos[26];
        for (int i = 0; i < 26; ++i) pos[i] = -1;
        for (int i = 0; i < (int)s.size(); ++i) {
            pos[s[i] - 'a'] = i;
        }
        int ans = 0;
        for (int i = 0; i < (int)t.size(); ++i) {
            int idx = pos[t[i] - 'a'];
            ans += abs(i - idx);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int findPermutationDifference(String s, String t) {
        int[] indexInS = new int[26];
        for (int i = 0; i < s.length(); i++) {
            indexInS[s.charAt(i) - 'a'] = i;
        }
        int diffSum = 0;
        for (int i = 0; i < t.length(); i++) {
            diffSum += Math.abs(i - indexInS[t.charAt(i) - 'a']);
        }
        return diffSum;
    }
}
```

## Python

```python
class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        pos = {ch: i for i, ch in enumerate(s)}
        diff = 0
        for i, ch in enumerate(t):
            diff += abs(pos[ch] - i)
        return diff
```

## Python3

```python
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        pos = {ch: i for i, ch in enumerate(s)}
        ans = 0
        for i, ch in enumerate(t):
            ans += abs(i - pos[ch])
        return ans
```

## C

```c
#include <string.h>
#include <stdlib.h>

int findPermutationDifference(char* s, char* t) {
    int n = strlen(s);
    int pos[26];
    for (int i = 0; i < 26; ++i) pos[i] = -1;
    for (int i = 0; i < n; ++i) {
        pos[s[i] - 'a'] = i;
    }
    int diff = 0;
    for (int i = 0; i < n; ++i) {
        int idx = pos[t[i] - 'a'];
        diff += abs(i - idx);
    }
    return diff;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindPermutationDifference(string s, string t)
    {
        int[] indexInS = new int[26];
        for (int i = 0; i < s.Length; i++)
        {
            indexInS[s[i] - 'a'] = i;
        }

        int total = 0;
        for (int i = 0; i < t.Length; i++)
        {
            int idx = t[i] - 'a';
            total += Math.Abs(i - indexInS[idx]);
        }

        return total;
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
var findPermutationDifference = function(s, t) {
    const indexMap = new Map();
    for (let i = 0; i < s.length; i++) {
        indexMap.set(s[i], i);
    }
    let diffSum = 0;
    for (let i = 0; i < t.length; i++) {
        diffSum += Math.abs(i - indexMap.get(t[i]));
    }
    return diffSum;
};
```

## Typescript

```typescript
function findPermutationDifference(s: string, t: string): number {
    const pos = new Map<string, number>();
    for (let i = 0; i < s.length; i++) {
        pos.set(s[i], i);
    }
    let diff = 0;
    for (let i = 0; i < t.length; i++) {
        const j = pos.get(t[i])!;
        diff += Math.abs(i - j);
    }
    return diff;
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
    function findPermutationDifference($s, $t) {
        $pos = [];
        $lenS = strlen($s);
        for ($i = 0; $i < $lenS; $i++) {
            $pos[$s[$i]] = $i;
        }

        $diff = 0;
        $lenT = strlen($t);
        for ($j = 0; $j < $lenT; $j++) {
            $c = $t[$j];
            $diff += abs($pos[$c] - $j);
        }

        return $diff;
    }
}
```

## Swift

```swift
class Solution {
    func findPermutationDifference(_ s: String, _ t: String) -> Int {
        var indexMap = [Character: Int]()
        for (i, ch) in s.enumerated() {
            indexMap[ch] = i
        }
        var total = 0
        for (i, ch) in t.enumerated() {
            if let j = indexMap[ch] {
                total += abs(i - j)
            }
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findPermutationDifference(s: String, t: String): Int {
        val pos = IntArray(26) { -1 }
        for (i in s.indices) {
            pos[s[i] - 'a'] = i
        }
        var diff = 0
        for (j in t.indices) {
            diff += kotlin.math.abs(pos[t[j] - 'a'] - j)
        }
        return diff
    }
}
```

## Dart

```dart
class Solution {
  int findPermutationDifference(String s, String t) {
    final List<int> indexInS = List.filled(26, -1);
    for (int i = 0; i < s.length; i++) {
      indexInS[s.codeUnitAt(i) - 97] = i;
    }
    int diffSum = 0;
    for (int i = 0; i < t.length; i++) {
      int idx = indexInS[t.codeUnitAt(i) - 97];
      diffSum += (idx - i).abs();
    }
    return diffSum;
  }
}
```

## Golang

```go
func findPermutationDifference(s string, t string) int {
	pos := make([]int, 26)
	for i, ch := range s {
		pos[ch-'a'] = i
	}
	sum := 0
	for i, ch := range t {
		diff := i - pos[ch-'a']
		if diff < 0 {
			diff = -diff
		}
		sum += diff
	}
	return sum
}
```

## Ruby

```ruby
def find_permutation_difference(s, t)
  pos = {}
  s.each_char.with_index { |ch, i| pos[ch] = i }
  diff = 0
  t.each_char.with_index { |ch, i| diff += (pos[ch] - i).abs }
  diff
end
```

## Scala

```scala
object Solution {
    def findPermutationDifference(s: String, t: String): Int = {
        val pos = new Array[Int](26)
        for (i <- s.indices) {
            pos(s.charAt(i) - 'a') = i
        }
        var diff = 0
        for (i <- t.indices) {
            diff += math.abs(pos(t.charAt(i) - 'a') - i)
        }
        diff
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_permutation_difference(s: String, t: String) -> i32 {
        let mut pos = [0usize; 26];
        for (i, ch) in s.bytes().enumerate() {
            pos[(ch - b'a') as usize] = i;
        }
        let mut ans: i32 = 0;
        for (j, ch) in t.bytes().enumerate() {
            let i = pos[(ch - b'a') as usize];
            ans += ((i as i32) - (j as i32)).abs();
        }
        ans
    }
}
```

## Racket

```racket
#lang racket

(define/contract (find-permutation-difference s t)
  (-> string? string? exact-integer?)
  (let* ((len (string-length s))
         (pos (make-hash)))
    ;; map each character in s to its index
    (for ([i (in-range len)])
      (hash-set! pos (string-ref s i) i))
    (let loop ((i 0) (sum 0))
      (if (= i len)
          sum
          (let* ((ch (string-ref t i))
                 (orig (hash-ref pos ch)))
            (loop (+ i 1) (+ sum (abs (- i orig)))))))))
```

## Erlang

```erlang
-spec find_permutation_difference(unicode:unicode_binary(), unicode:unicode_binary()) -> integer().
find_permutation_difference(S, T) ->
    SList = binary_to_list(S),
    TList = binary_to_list(T),
    SMap = build_map(SList, 0, #{}),
    TMap = build_map(TList, 0, #{}),
    lists:foldl(fun(Char, Acc) ->
        IndexS = maps:get(Char, SMap),
        IndexT = maps:get(Char, TMap),
        Acc + erlang:abs(IndexS - IndexT)
    end, 0, SList).

build_map([], _Idx, Map) -> Map;
build_map([Char|Rest], Idx, Map) ->
    build_map(Rest, Idx + 1, maps:put(Char, Idx, Map)).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_permutation_difference(s :: String.t(), t :: String.t()) :: integer()
  def find_permutation_difference(s, t) do
    s_indices = for {c, i} <- Enum.with_index(String.graphemes(s)), into: %{}, do: {c, i}
    t_indices = for {c, i} <- Enum.with_index(String.graphemes(t)), into: %{}, do: {c, i}

    Enum.reduce(s_indices, 0, fn {c, idx_s}, acc ->
      idx_t = Map.fetch!(t_indices, c)
      acc + abs(idx_s - idx_t)
    end)
  end
end
```
