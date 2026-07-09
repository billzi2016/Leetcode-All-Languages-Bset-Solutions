# 2840. Check if Strings Can be Made Equal With Operations II

## Cpp

```cpp
class Solution {
public:
    bool checkStrings(string s1, string s2) {
        int evenCnt[26] = {0}, oddCnt[26] = {0};
        for (int i = 0; i < (int)s1.size(); ++i) {
            if (i % 2 == 0) {
                ++evenCnt[s1[i] - 'a'];
                ++evenCnt[s2[i] - 'a'];
            } else {
                ++oddCnt[s1[i] - 'a'];
                ++oddCnt[s2[i] - 'a'];
            }
        }
        // Since we added counts from both strings, each character count should be even if they match.
        for (int i = 0; i < 26; ++i) {
            if (evenCnt[i] % 2 != 0 || oddCnt[i] % 2 != 0) return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean checkStrings(String s1, String s2) {
        int n = s1.length();
        int[] even = new int[26];
        int[] odd = new int[26];
        for (int i = 0; i < n; i++) {
            char c1 = s1.charAt(i);
            char c2 = s2.charAt(i);
            if ((i & 1) == 0) {
                even[c1 - 'a']++;
                even[c2 - 'a']--;
            } else {
                odd[c1 - 'a']++;
                odd[c2 - 'a']--;
            }
        }
        for (int i = 0; i < 26; i++) {
            if (even[i] != 0 || odd[i] != 0) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def checkStrings(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False
        even_cnt = [0] * 26
        odd_cnt = [0] * 26
        for i, (c1, c2) in enumerate(zip(s1, s2)):
            idx1 = ord(c1) - 97
            idx2 = ord(c2) - 97
            if i % 2 == 0:
                even_cnt[idx1] += 1
                even_cnt[idx2] -= 1
            else:
                odd_cnt[idx1] += 1
                odd_cnt[idx2] -= 1
        return all(v == 0 for v in even_cnt) and all(v == 0 for v in odd_cnt)
```

## Python3

```python
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even = [0] * 26
        odd = [0] * 26
        for i, ch in enumerate(s1):
            idx = ord(ch) - 97
            if i & 1:
                odd[idx] += 1
            else:
                even[idx] += 1
        for i, ch in enumerate(s2):
            idx = ord(ch) - 97
            if i & 1:
                odd[idx] -= 1
            else:
                even[idx] -= 1
        return all(v == 0 for v in even) and all(v == 0 for v in odd)
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool checkStrings(char* s1, char* s2) {
    int n = strlen(s1);
    int cnt_even[26] = {0};
    int cnt_odd[26]  = {0};

    for (int i = 0; i < n; ++i) {
        if ((i & 1) == 0)
            ++cnt_even[s1[i] - 'a'];
        else
            ++cnt_odd[s1[i] - 'a'];
    }

    for (int i = 0; i < n; ++i) {
        if ((i & 1) == 0)
            --cnt_even[s2[i] - 'a'];
        else
            --cnt_odd[s2[i] - 'a'];
    }

    for (int k = 0; k < 26; ++k) {
        if (cnt_even[k] != 0 || cnt_odd[k] != 0)
            return false;
    }
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool CheckStrings(string s1, string s2) {
        int n = s1.Length;
        int[] even1 = new int[26];
        int[] odd1 = new int[26];
        int[] even2 = new int[26];
        int[] odd2 = new int[26];

        for (int i = 0; i < n; i++) {
            int idx1 = s1[i] - 'a';
            int idx2 = s2[i] - 'a';
            if ((i & 1) == 0) {
                even1[idx1]++;
                even2[idx2]++;
            } else {
                odd1[idx1]++;
                odd2[idx2]++;
            }
        }

        for (int i = 0; i < 26; i++) {
            if (even1[i] != even2[i] || odd1[i] != odd2[i]) return false;
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkStrings = function(s1, s2) {
    if (s1.length !== s2.length) return false;
    const even1 = new Array(26).fill(0);
    const odd1 = new Array(26).fill(0);
    const even2 = new Array(26).fill(0);
    const odd2 = new Array(26).fill(0);
    
    for (let i = 0; i < s1.length; ++i) {
        const c1 = s1.charCodeAt(i) - 97;
        const c2 = s2.charCodeAt(i) - 97;
        if ((i & 1) === 0) { // even index
            ++even1[c1];
            ++even2[c2];
        } else {
            ++odd1[c1];
            ++odd2[c2];
        }
    }
    
    for (let i = 0; i < 26; ++i) {
        if (even1[i] !== even2[i] || odd1[i] !== odd2[i]) return false;
    }
    return true;
};
```

## Typescript

```typescript
function checkStrings(s1: string, s2: string): boolean {
    const n = s1.length;
    const even = new Array(26).fill(0);
    const odd = new Array(26).fill(0);
    for (let i = 0; i < n; i++) {
        const idx = s1.charCodeAt(i) - 97;
        if ((i & 1) === 0) even[idx]++; else odd[idx]++;
    }
    for (let i = 0; i < n; i++) {
        const idx = s2.charCodeAt(i) - 97;
        if ((i & 1) === 0) even[idx]--; else odd[idx]--;
    }
    for (let k = 0; k < 26; k++) {
        if (even[k] !== 0 || odd[k] !== 0) return false;
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @return Boolean
     */
    function checkStrings($s1, $s2) {
        $n = strlen($s1);
        if ($n !== strlen($s2)) {
            return false;
        }

        $even1 = array_fill(0, 26, 0);
        $odd1  = array_fill(0, 26, 0);
        $even2 = array_fill(0, 26, 0);
        $odd2  = array_fill(0, 26, 0);

        for ($i = 0; $i < $n; $i++) {
            $c1 = ord($s1[$i]) - 97;
            $c2 = ord($s2[$i]) - 97;

            if (($i & 1) === 0) { // even index
                $even1[$c1]++;
                $even2[$c2]++;
            } else { // odd index
                $odd1[$c1]++;
                $odd2[$c2]++;
            }
        }

        for ($i = 0; $i < 26; $i++) {
            if ($even1[$i] !== $even2[$i] || $odd1[$i] !== $odd2[$i]) {
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
    func checkStrings(_ s1: String, _ s2: String) -> Bool {
        let a1 = Array(s1.utf8)
        let a2 = Array(s2.utf8)
        var even = [Int](repeating: 0, count: 26)
        var odd = [Int](repeating: 0, count: 26)
        for i in 0..<a1.count {
            let idx1 = Int(a1[i] - 97)
            let idx2 = Int(a2[i] - 97)
            if i & 1 == 0 {
                even[idx1] += 1
                even[idx2] -= 1
            } else {
                odd[idx1] += 1
                odd[idx2] -= 1
            }
        }
        for v in even where v != 0 { return false }
        for v in odd where v != 0 { return false }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun checkStrings(s1: String, s2: String): Boolean {
        val n = s1.length
        val even1 = IntArray(26)
        val odd1 = IntArray(26)
        val even2 = IntArray(26)
        val odd2 = IntArray(26)

        for (i in 0 until n) {
            val c1 = s1[i] - 'a'
            val c2 = s2[i] - 'a'
            if (i % 2 == 0) {
                even1[c1]++
                even2[c2]++
            } else {
                odd1[c1]++
                odd2[c2]++
            }
        }

        for (j in 0 until 26) {
            if (even1[j] != even2[j] || odd1[j] != odd2[j]) return false
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool checkStrings(String s1, String s2) {
    int n = s1.length;
    List<List<int>> cnt1 = List.generate(2, (_) => List.filled(26, 0));
    List<List<int>> cnt2 = List.generate(2, (_) => List.filled(26, 0));

    for (int i = 0; i < n; i++) {
      int idx1 = s1.codeUnitAt(i) - 97;
      int parity = i % 2;
      cnt1[parity][idx1]++;

      int idx2 = s2.codeUnitAt(i) - 97;
      cnt2[parity][idx2]++;
    }

    for (int p = 0; p < 2; p++) {
      for (int c = 0; c < 26; c++) {
        if (cnt1[p][c] != cnt2[p][c]) return false;
      }
    }
    return true;
  }
}
```

## Golang

```go
func checkStrings(s1 string, s2 string) bool {
	if len(s1) != len(s2) {
		return false
	}
	var evenCnt, oddCnt [26]int
	for i := 0; i < len(s1); i++ {
		a := int(s1[i] - 'a')
		b := int(s2[i] - 'a')
		if i%2 == 0 {
			evenCnt[a]++
			evenCnt[b]--
		} else {
			oddCnt[a]++
			oddCnt[b]--
		}
	}
	for _, v := range evenCnt {
		if v != 0 {
			return false
		}
	}
	for _, v := range oddCnt {
		if v != 0 {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def check_strings(s1, s2)
  return false unless s1.length == s2.length

  even1 = Array.new(26, 0)
  odd1  = Array.new(26, 0)
  even2 = Array.new(26, 0)
  odd2  = Array.new(26, 0)

  s1.each_char.with_index do |ch, i|
    idx = ch.ord - 97
    if i.even?
      even1[idx] += 1
    else
      odd1[idx] += 1
    end
  end

  s2.each_char.with_index do |ch, i|
    idx = ch.ord - 97
    if i.even?
      even2[idx] += 1
    else
      odd2[idx] += 1
    end
  end

  even1 == even2 && odd1 == odd2
end
```

## Scala

```scala
object Solution {
    def checkStrings(s1: String, s2: String): Boolean = {
        val n = s1.length
        val even1 = Array.ofDim[Int](26)
        val odd1  = Array.ofDim[Int](26)
        val even2 = Array.ofDim[Int](26)
        val odd2  = Array.ofDim[Int](26)

        var i = 0
        while (i < n) {
            val c1 = s1.charAt(i) - 'a'
            if ((i & 1) == 0) even1(c1) += 1 else odd1(c1) += 1

            val c2 = s2.charAt(i) - 'a'
            if ((i & 1) == 0) even2(c2) += 1 else odd2(c2) += 1
            i += 1
        }

        even1.sameElements(even2) && odd1.sameElements(odd2)
    }
}
```

## Rust

```rust
impl Solution {
    pub fn check_strings(s1: String, s2: String) -> bool {
        if s1.len() != s2.len() {
            return false;
        }
        let b1 = s1.as_bytes();
        let b2 = s2.as_bytes();

        let mut even1 = [0i32; 26];
        let mut odd1 = [0i32; 26];
        let mut even2 = [0i32; 26];
        let mut odd2 = [0i32; 26];

        for (i, &c) in b1.iter().enumerate() {
            let idx = (c - b'a') as usize;
            if i % 2 == 0 {
                even1[idx] += 1;
            } else {
                odd1[idx] += 1;
            }
        }

        for (i, &c) in b2.iter().enumerate() {
            let idx = (c - b'a') as usize;
            if i % 2 == 0 {
                even2[idx] += 1;
            } else {
                odd2[idx] += 1;
            }
        }

        even1 == even2 && odd1 == odd2
    }
}
```

## Racket

```racket
(define/contract (check-strings s1 s2)
  (-> string? string? boolean?)
  (if (not (= (string-length s1) (string-length s2)))
      #f
      (let* ((n (string-length s1))
             (cnt-even (make-vector 26 0))
             (cnt-odd (make-vector 26 0))
             (base (char->integer #\a)))
        (let loop ((i 0))
          (when (< i n)
            (define c1 (- (char->integer (string-ref s1 i)) base))
            (define c2 (- (char->integer (string-ref s2 i)) base))
            (if (even? i)
                (begin
                  (vector-set! cnt-even c1 (+ 1 (vector-ref cnt-even c1)))
                  (vector-set! cnt-even c2 (- (vector-ref cnt-even c2) 1)))
                (begin
                  (vector-set! cnt-odd c1 (+ 1 (vector-ref cnt-odd c1)))
                  (vector-set! cnt-odd c2 (- (vector-ref cnt-odd c2) 1))))
            (loop (+ i 1))))
        (let loop ((i 0))
          (cond
            [(= i 26) #t]
            [(or (not (= (vector-ref cnt-even i) 0))
                 (not (= (vector-ref cnt-odd i) 0))) #f]
            [else (loop (+ i 1))])))))
```

## Erlang

```erlang
-module(solution).
-export([check_strings/2]).

-spec check_strings(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> boolean().
check_strings(S1, S2) ->
    if
        byte_size(S1) =/= byte_size(S2) -> false;
        true ->
            {EvenMap1, OddMap1} = count_parity(S1),
            {EvenMap2, OddMap2} = count_parity(S2),
            EvenMap1 =:= EvenMap2 andalso OddMap1 =:= OddMap2
    end.

count_parity(Bin) -> count_parity(Bin, 0, #{}, #{}).

count_parity(<<>>, _Idx, EvenMap, OddMap) ->
    {EvenMap, OddMap};
count_parity(<<Char:8, Rest/binary>>, Idx, EvenMap, OddMap) ->
    case (Idx band 1) of
        0 -> % even index
            NewEven = maps:update_with(Char, fun(C) -> C + 1 end, 1, EvenMap),
            count_parity(Rest, Idx + 1, NewEven, OddMap);
        1 -> % odd index
            NewOdd = maps:update_with(Char, fun(C) -> C + 1 end, 1, OddMap),
            count_parity(Rest, Idx + 1, EvenMap, NewOdd)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec check_strings(s1 :: String.t(), s2 :: String.t()) :: boolean()
  def check_strings(s1, s2) do
    if byte_size(s1) != byte_size(s2) do
      false
    else
      {even1, odd1} = count_parities(s1)
      {even2, odd2} = count_parities(s2)

      even1 == even2 and odd1 == odd2
    end
  end

  defp count_parities(str) do
    bytes = :binary.bin_to_list(str)

    Enum.reduce(Enum.with_index(bytes), {%{}, %{}}, fn {b, idx}, {even_map, odd_map} ->
      char = <<b>>

      if rem(idx, 2) == 0 do
        {Map.update(even_map, char, 1, &(&1 + 1)), odd_map}
      else
        {even_map, Map.update(odd_map, char, 1, &(&1 + 1))}
      end
    end)
  end
end
```
