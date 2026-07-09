# 0942. DI String Match

## Cpp

```cpp
class Solution {
public:
    vector<int> diStringMatch(string s) {
        int n = s.size();
        int lo = 0, hi = n;
        vector<int> ans;
        ans.reserve(n + 1);
        for (char c : s) {
            if (c == 'I') {
                ans.push_back(lo++);
            } else { // 'D'
                ans.push_back(hi--);
            }
        }
        ans.push_back(lo); // lo == hi at this point
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] diStringMatch(String s) {
        int n = s.length();
        int[] result = new int[n + 1];
        int low = 0, high = n;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == 'I') {
                result[i] = low++;
            } else { // 'D'
                result[i] = high--;
            }
        }
        result[n] = low; // low == high at this point
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        n = len(s)
        low, high = 0, n
        res = []
        for ch in s:
            if ch == 'I':
                res.append(low)
                low += 1
            else:  # 'D'
                res.append(high)
                high -= 1
        res.append(low)  # low == high at this point
        return res
```

## Python3

```python
from typing import List

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        lo, hi = 0, n
        ans = []
        for ch in s:
            if ch == 'I':
                ans.append(lo)
                lo += 1
            else:
                ans.append(hi)
                hi -= 1
        ans.append(lo)  # lo == hi at this point
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* diStringMatch(char* s, int* returnSize) {
    int n = (int)strlen(s);
    int *perm = (int*)malloc((n + 1) * sizeof(int));
    int lo = 0, hi = n;
    for (int i = 0; i < n; ++i) {
        if (s[i] == 'I') {
            perm[i] = lo++;
        } else { // 'D'
            perm[i] = hi--;
        }
    }
    perm[n] = lo; // lo == hi
    *returnSize = n + 1;
    return perm;
}
```

## Csharp

```csharp
public class Solution {
    public int[] DiStringMatch(string s) {
        int n = s.Length;
        int low = 0, high = n;
        int[] ans = new int[n + 1];
        for (int i = 0; i < n; i++) {
            if (s[i] == 'I') {
                ans[i] = low++;
            } else { // 'D'
                ans[i] = high--;
            }
        }
        ans[n] = low; // low == high at this point
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number[]}
 */
var diStringMatch = function(s) {
    const n = s.length;
    let lo = 0, hi = n;
    const res = new Array(n + 1);
    for (let i = 0; i < n; ++i) {
        if (s[i] === 'I') {
            res[i] = lo++;
        } else { // 'D'
            res[i] = hi--;
        }
    }
    // last remaining number
    res[n] = lo; // lo == hi at this point
    return res;
};
```

## Typescript

```typescript
function diStringMatch(s: string): number[] {
    const n = s.length;
    let low = 0, high = n;
    const result: number[] = new Array(n + 1);
    for (let i = 0; i < n; i++) {
        if (s[i] === 'I') {
            result[i] = low++;
        } else {
            result[i] = high--;
        }
    }
    result[n] = low; // low == high at this point
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param string $s
     * @return int[]
     */
    function diStringMatch($s) {
        $n = strlen($s);
        $low = 0;
        $high = $n;
        $result = [];

        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === 'I') {
                $result[] = $low;
                $low++;
            } else { // 'D'
                $result[] = $high;
                $high--;
            }
        }

        // The last remaining number
        $result[] = $low; // low == high at this point

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func diStringMatch(_ s: String) -> [Int] {
        let n = s.count
        var low = 0
        var high = n
        var result = [Int]()
        result.reserveCapacity(n + 1)
        for ch in s {
            if ch == "I" {
                result.append(low)
                low += 1
            } else { // 'D'
                result.append(high)
                high -= 1
            }
        }
        result.append(low) // low == high at this point
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun diStringMatch(s: String): IntArray {
        val n = s.length
        val result = IntArray(n + 1)
        var low = 0
        var high = n
        for (i in 0 until n) {
            if (s[i] == 'I') {
                result[i] = low++
            } else {
                result[i] = high--
            }
        }
        result[n] = low // low and high are equal here
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> diStringMatch(String s) {
    int n = s.length;
    int low = 0, high = n;
    List<int> ans = List.filled(n + 1, 0);
    for (int i = 0; i < n; i++) {
      if (s[i] == 'I') {
        ans[i] = low++;
      } else {
        ans[i] = high--;
      }
    }
    ans[n] = low; // low == high at this point
    return ans;
  }
}
```

## Golang

```go
func diStringMatch(s string) []int {
	n := len(s)
	low, high := 0, n
	res := make([]int, n+1)
	for i, ch := range s {
		if ch == 'I' {
			res[i] = low
			low++
		} else { // 'D'
			res[i] = high
			high--
		}
	}
	res[n] = low // low == high at this point
	return res
}
```

## Ruby

```ruby
def di_string_match(s)
  n = s.length
  low = 0
  high = n
  result = []
  s.each_char do |ch|
    if ch == 'I'
      result << low
      low += 1
    else
      result << high
      high -= 1
    end
  end
  result << low
  result
end
```

## Scala

```scala
object Solution {
    def diStringMatch(s: String): Array[Int] = {
        val n = s.length
        val ans = new Array[Int](n + 1)
        var low = 0
        var high = n
        for (i <- 0 until n) {
            if (s.charAt(i) == 'I') {
                ans(i) = low
                low += 1
            } else {
                ans(i) = high
                high -= 1
            }
        }
        ans(n) = low // low and high are equal here
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn di_string_match(s: String) -> Vec<i32> {
        let n = s.len() as i32;
        let mut lo = 0i32;
        let mut hi = n;
        let mut res = Vec::with_capacity((n + 1) as usize);
        for ch in s.bytes() {
            if ch == b'I' {
                res.push(lo);
                lo += 1;
            } else { // 'D'
                res.push(hi);
                hi -= 1;
            }
        }
        res.push(lo); // lo == hi now
        res
    }
}
```

## Racket

```racket
(define/contract (di-string-match s)
  (-> string? (listof exact-integer?))
  (let* ((n (string-length s))
         (low0 0)
         (high0 n))
    (let loop ((i 0) (low low0) (high high0) (acc '()))
      (if (= i n)
          (reverse (cons low acc)) ; low == high at this point
          (let ((c (string-ref s i)))
            (if (char=? c #\I)
                (loop (+ i 1) (+ low 1) high (cons low acc))
                (loop (+ i 1) low (- high 1) (cons high acc))))))))
```

## Erlang

```erlang
-module(solution).
-export([di_string_match/1]).

-spec di_string_match(S :: unicode:unicode_binary()) -> [integer()].
di_string_match(S) ->
    N = byte_size(S),
    build_perm(S, 0, N, []).

build_perm(<<>>, Low, _High, Acc) ->
    lists:reverse([Low | Acc]);
build_perm(<<$I, Rest/binary>>, Low, High, Acc) ->
    build_perm(Rest, Low + 1, High, [Low | Acc]);
build_perm(<<$D, Rest/binary>>, Low, High, Acc) ->
    build_perm(Rest, Low, High - 1, [High | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec di_string_match(s :: String.t) :: [integer]
  def di_string_match(s) do
    n = String.length(s)
    chars = String.to_charlist(s)

    {rev_res, low, _high} =
      Enum.reduce(chars, {[], 0, n}, fn ch, {acc, lo, hi} ->
        if ch == ?I do
          {[lo | acc], lo + 1, hi}
        else
          {[hi | acc], lo, hi - 1}
        end
      end)

    [low | rev_res] |> Enum.reverse()
  end
end
```
