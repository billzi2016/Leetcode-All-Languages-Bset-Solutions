# 2068. Check Whether Two Strings are Almost Equivalent

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool checkAlmostEquivalent(string word1, string word2) {
        int diff[26] = {0};
        for (size_t i = 0; i < word1.size(); ++i) {
            ++diff[word1[i] - 'a'];
            --diff[word2[i] - 'a'];
        }
        for (int d : diff) {
            if (abs(d) > 3) return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean checkAlmostEquivalent(String word1, String word2) {
        int[] diff = new int[26];
        int n = word1.length();
        for (int i = 0; i < n; i++) {
            diff[word1.charAt(i) - 'a']++;
            diff[word2.charAt(i) - 'a']--;
        }
        for (int d : diff) {
            if (Math.abs(d) > 3) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        cnt = [0] * 26
        for c1, c2 in zip(word1, word2):
            cnt[ord(c1) - 97] += 1
            cnt[ord(c2) - 97] -= 1
        for v in cnt:
            if abs(v) > 3:
                return False
        return True
```

## Python3

```python
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        cnt = [0] * 26
        for c1, c2 in zip(word1, word2):
            cnt[ord(c1) - 97] += 1
            cnt[ord(c2) - 97] -= 1
        return all(abs(x) <= 3 for x in cnt)
```

## C

```c
#include <stdbool.h>
#include <stdlib.h>

bool checkAlmostEquivalent(char* word1, char* word2) {
    int cnt[26] = {0};
    while (*word1 && *word2) {
        cnt[*word1 - 'a']++;
        cnt[*word2 - 'a']--;
        word1++;
        word2++;
    }
    for (int i = 0; i < 26; ++i) {
        if (abs(cnt[i]) > 3) return false;
    }
    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool CheckAlmostEquivalent(string word1, string word2)
    {
        int[] diff = new int[26];
        for (int i = 0; i < word1.Length; i++)
        {
            diff[word1[i] - 'a']++;
            diff[word2[i] - 'a']--;
        }
        foreach (int d in diff)
        {
            if (d > 3 || d < -3) return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} word1
 * @param {string} word2
 * @return {boolean}
 */
var checkAlmostEquivalent = function(word1, word2) {
    const diff = new Array(26).fill(0);
    for (let i = 0; i < word1.length; ++i) {
        diff[word1.charCodeAt(i) - 97] += 1;
        diff[word2.charCodeAt(i) - 97] -= 1;
    }
    for (let d of diff) {
        if (Math.abs(d) > 3) return false;
    }
    return true;
};
```

## Typescript

```typescript
function checkAlmostEquivalent(word1: string, word2: string): boolean {
    const diff = new Array(26).fill(0);
    for (let i = 0; i < word1.length; i++) {
        diff[word1.charCodeAt(i) - 97]++;
        diff[word2.charCodeAt(i) - 97]--;
    }
    for (const d of diff) {
        if (Math.abs(d) > 3) return false;
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param String $word1
     * @param String $word2
     * @return Boolean
     */
    function checkAlmostEquivalent($word1, $word2) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($word1);
        for ($i = 0; $i < $n; $i++) {
            $cnt[ord($word1[$i]) - 97]++;
            $cnt[ord($word2[$i]) - 97]--;
        }
        foreach ($cnt as $c) {
            if (abs($c) > 3) {
                return false;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func checkAlmostEquivalent(_ word1: String, _ word2: String) -> Bool {
        var diff = [Int](repeating: 0, count: 26)
        let aValue = UInt32(ascii: "a")
        for (c1, c2) in zip(word1.unicodeScalars, word2.unicodeScalars) {
            diff[Int(c1.value - aValue)] += 1
            diff[Int(c2.value - aValue)] -= 1
        }
        for v in diff {
            if abs(v) > 3 { return false }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkAlmostEquivalent(word1: String, word2: String): Boolean {
        val diff = IntArray(26)
        for (i in word1.indices) {
            diff[word1[i] - 'a']++
            diff[word2[i] - 'a']--
        }
        for (d in diff) {
            if (kotlin.math.abs(d) > 3) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool checkAlmostEquivalent(String word1, String word2) {
    List<int> cnt = List.filled(26, 0);
    for (int i = 0; i < word1.length; i++) {
      cnt[word1.codeUnitAt(i) - 97]++;
      cnt[word2.codeUnitAt(i) - 97]--;
    }
    for (int v in cnt) {
      if (v.abs() > 3) return false;
    }
    return true;
  }
}
```

## Golang

```go
func checkAlmostEquivalent(word1 string, word2 string) bool {
	var cnt [26]int
	for i := 0; i < len(word1); i++ {
		cnt[word1[i]-'a']++
		cnt[word2[i]-'a']--
	}
	for _, v := range cnt {
		if v > 3 || v < -3 {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def check_almost_equivalent(word1, word2)
  cnt = Array.new(26, 0)
  n = word1.length
  i = 0
  while i < n
    cnt[word1.getbyte(i) - 97] += 1
    cnt[word2.getbyte(i) - 97] -= 1
    i += 1
  end
  cnt.each do |c|
    return false if c.abs > 3
  end
  true
end
```

## Scala

```scala
object Solution {
    def checkAlmostEquivalent(word1: String, word2: String): Boolean = {
        val cnt = new Array[Int](26)
        var i = 0
        while (i < word1.length) {
            cnt(word1.charAt(i) - 'a') += 1
            cnt(word2.charAt(i) - 'a') -= 1
            i += 1
        }
        for (v <- cnt) {
            if (math.abs(v) > 3) return false
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_almost_equivalent(word1: String, word2: String) -> bool {
        let mut cnt = [0i32; 26];
        let b1 = word1.as_bytes();
        let b2 = word2.as_bytes();
        for i in 0..b1.len() {
            cnt[(b1[i] - b'a') as usize] += 1;
            cnt[(b2[i] - b'a') as usize] -= 1;
        }
        cnt.iter().all(|&x| x.abs() <= 3)
    }
}
```

## Racket

```racket
(define/contract (check-almost-equivalent word1 word2)
  (-> string? string? boolean?)
  (let* ((n (string-length word1))
         (cnt (make-vector 26 0)))
    (for ([i (in-range n)])
      (let* ((c1 (char->integer (string-ref word1 i)))
             (c2 (char->integer (string-ref word2 i)))
             (idx1 (- c1 (char->integer #\a)))
             (idx2 (- c2 (char->integer #\a))))
        (vector-set! cnt idx1 (+ 1 (vector-ref cnt idx1)))
        (vector-set! cnt idx2 (- (vector-ref cnt idx2) 1))))
    (let loop ((i 0))
      (if (= i 26)
          #t
          (if (> (abs (vector-ref cnt i)) 3)
              #f
              (loop (+ i 1)))))))
```

## Erlang

```erlang
-module(solution).
-export([check_almost_equivalent/2]).

-spec check_almost_equivalent(Word1 :: unicode:unicode_binary(), Word2 :: unicode:unicode_binary()) -> boolean().
check_almost_equivalent(Word1, Word2) ->
    DiffMap = diff_counts(Word1, Word2, #{}),
    maps:fold(fun(_K, V, Acc) -> Acc andalso (erlang:abs(V) =< 3) end,
              true, DiffMap).

diff_counts(<<>>, <<>>, Map) -> Map;
diff_counts(<<C1, Rest1/binary>>, <<C2, Rest2/binary>>, Map) ->
    Char1 = C1 - $a,
    Char2 = C2 - $a,
    M1 = maps:update_with(Char1, fun(V) -> V + 1 end, 1, Map),
    M2 = maps:update_with(Char2, fun(V) -> V - 1 end, -1, M1),
    diff_counts(Rest1, Rest2, M2).
```

## Elixir

```elixir
defmodule Solution do
  @spec check_almost_equivalent(word1 :: String.t(), word2 :: String.t()) :: boolean()
  def check_almost_equivalent(word1, word2) do
    bytes1 = :binary.bin_to_list(word1)
    bytes2 = :binary.bin_to_list(word2)

    cnt =
      Enum.reduce(Enum.zip(bytes1, bytes2), :array.new(26, default: 0), fn {b1, b2}, acc ->
        idx1 = b1 - ?a
        idx2 = b2 - ?a

        acc1 = :array.set(idx1, (:array.get(idx1, acc) + 1), acc)
        :array.set(idx2, (:array.get(idx2, acc1) - 1), acc1)
      end)

    Enum.all?(0..25, fn i ->
      diff = :array.get(i, cnt)
      abs(diff) <= 3
    end)
  end
end
```
