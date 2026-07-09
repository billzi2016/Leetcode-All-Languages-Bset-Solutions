# 2379. Minimum Recolors to Get K Consecutive Black Blocks

## Cpp

```cpp
class Solution {
public:
    int minimumRecolors(string blocks, int k) {
        int n = blocks.size();
        int whites = 0;
        for (int i = 0; i < k; ++i) {
            if (blocks[i] == 'W') ++whites;
        }
        int ans = whites;
        for (int i = k; i < n; ++i) {
            if (blocks[i - k] == 'W') --whites;
            if (blocks[i] == 'W') ++whites;
            ans = min(ans, whites);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minimumRecolors(String blocks, int k) {
        int n = blocks.length();
        int whiteCount = 0;
        for (int i = 0; i < k; i++) {
            if (blocks.charAt(i) == 'W') {
                whiteCount++;
            }
        }
        int minRecolors = whiteCount;
        for (int i = k; i < n; i++) {
            if (blocks.charAt(i - k) == 'W') {
                whiteCount--;
            }
            if (blocks.charAt(i) == 'W') {
                whiteCount++;
            }
            if (whiteCount < minRecolors) {
                minRecolors = whiteCount;
            }
        }
        return minRecolors;
    }
}
```

## Python

```python
class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        n = len(blocks)
        # Count white blocks in the first window of size k
        white = sum(1 for i in range(k) if blocks[i] == 'W')
        ans = white
        # Slide the window across the string
        for i in range(k, n):
            if blocks[i] == 'W':
                white += 1
            if blocks[i - k] == 'W':
                white -= 1
            if white < ans:
                ans = white
        return ans
```

## Python3

```python
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        # Count whites in the first window of size k
        white_cnt = sum(1 for i in range(k) if blocks[i] == 'W')
        min_recolors = white_cnt

        # Slide the window across the string
        for i in range(k, n):
            if blocks[i] == 'W':
                white_cnt += 1
            if blocks[i - k] == 'W':
                white_cnt -= 1
            if white_cnt < min_recolors:
                min_recolors = white_cnt

        return min_recolors
```

## C

```c
#include <string.h>

int minimumRecolors(char* blocks, int k) {
    int n = (int)strlen(blocks);
    int whites = 0;
    for (int i = 0; i < k; ++i) {
        if (blocks[i] == 'W') whites++;
    }
    int ans = whites;
    for (int i = k; i < n; ++i) {
        if (blocks[i] == 'W') whites++;
        if (blocks[i - k] == 'W') whites--;
        if (whites < ans) ans = whites;
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinimumRecolors(string blocks, int k)
    {
        int n = blocks.Length;
        int whiteCount = 0;
        for (int i = 0; i < k; i++)
        {
            if (blocks[i] == 'W') whiteCount++;
        }
        int minRecolors = whiteCount;

        for (int i = k; i < n; i++)
        {
            if (blocks[i - k] == 'W') whiteCount--;
            if (blocks[i] == 'W') whiteCount++;
            if (whiteCount < minRecolors) minRecolors = whiteCount;
        }

        return minRecolors;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} blocks
 * @param {number} k
 * @return {number}
 */
var minimumRecolors = function(blocks, k) {
    const n = blocks.length;
    let whiteCount = 0;
    // count whites in the first window
    for (let i = 0; i < k; ++i) {
        if (blocks[i] === 'W') whiteCount++;
    }
    let minRecolors = whiteCount;
    // slide the window
    for (let i = k; i < n; ++i) {
        if (blocks[i] === 'W') whiteCount++;
        if (blocks[i - k] === 'W') whiteCount--;
        if (whiteCount < minRecolors) minRecolors = whiteCount;
    }
    return minRecolors;
};
```

## Typescript

```typescript
function minimumRecolors(blocks: string, k: number): number {
    let whiteCount = 0;
    for (let i = 0; i < k; i++) {
        if (blocks[i] === 'W') whiteCount++;
    }
    let minRecolors = whiteCount;
    for (let i = k; i < blocks.length; i++) {
        if (blocks[i - k] === 'W') whiteCount--;
        if (blocks[i] === 'W') whiteCount++;
        if (whiteCount < minRecolors) minRecolors = whiteCount;
    }
    return minRecolors;
}
```

## Php

```php
class Solution {

    /**
     * @param String $blocks
     * @param Integer $k
     * @return Integer
     */
    function minimumRecolors($blocks, $k) {
        $n = strlen($blocks);
        $white = 0;
        for ($i = 0; $i < $k; $i++) {
            if ($blocks[$i] === 'W') {
                $white++;
            }
        }
        $minRecolors = $white;
        for ($i = $k; $i < $n; $i++) {
            if ($blocks[$i - $k] === 'W') {
                $white--;
            }
            if ($blocks[$i] === 'W') {
                $white++;
            }
            if ($white < $minRecolors) {
                $minRecolors = $white;
            }
        }
        return $minRecolors;
    }
}
```

## Swift

```swift
class Solution {
    func minimumRecolors(_ blocks: String, _ k: Int) -> Int {
        let chars = Array(blocks)
        var whiteCount = 0
        for i in 0..<k {
            if chars[i] == "W" { whiteCount += 1 }
        }
        var minOps = whiteCount
        var left = 0
        for right in k..<chars.count {
            if chars[left] == "W" { whiteCount -= 1 }
            left += 1
            if chars[right] == "W" { whiteCount += 1 }
            minOps = min(minOps, whiteCount)
        }
        return minOps
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumRecolors(blocks: String, k: Int): Int {
        var whites = 0
        for (i in 0 until k) {
            if (blocks[i] == 'W') whites++
        }
        var minOps = whites
        for (i in k until blocks.length) {
            if (blocks[i - k] == 'W') whites--
            if (blocks[i] == 'W') whites++
            if (whites < minOps) minOps = whites
        }
        return minOps
    }
}
```

## Dart

```dart
class Solution {
  int minimumRecolors(String blocks, int k) {
    int n = blocks.length;
    int whiteCount = 0;
    for (int i = 0; i < k; i++) {
      if (blocks[i] == 'W') whiteCount++;
    }
    int minRecolors = whiteCount;
    for (int i = k; i < n; i++) {
      if (blocks[i] == 'W') whiteCount++;
      if (blocks[i - k] == 'W') whiteCount--;
      if (whiteCount < minRecolors) minRecolors = whiteCount;
    }
    return minRecolors;
  }
}
```

## Golang

```go
func minimumRecolors(blocks string, k int) int {
    n := len(blocks)
    whiteCount := 0
    for i := 0; i < k; i++ {
        if blocks[i] == 'W' {
            whiteCount++
        }
    }
    minWhite := whiteCount
    for i := k; i < n; i++ {
        if blocks[i] == 'W' {
            whiteCount++
        }
        if blocks[i-k] == 'W' {
            whiteCount--
        }
        if whiteCount < minWhite {
            minWhite = whiteCount
        }
    }
    return minWhite
}
```

## Ruby

```ruby
# @param {String} blocks
# @param {Integer} k
# @return {Integer}
def minimum_recolors(blocks, k)
  n = blocks.length
  # Count whites in the first window of size k
  white_count = 0
  (0...k).each do |i|
    white_count += 1 if blocks[i] == 'W'
  end
  min_recolors = white_count

  # Slide the window across the string
  (k...n).each do |right|
    left = right - k
    white_count -= 1 if blocks[left] == 'W'
    white_count += 1 if blocks[right] == 'W'
    min_recolors = [min_recolors, white_count].min
  end

  min_recolors
end
```

## Scala

```scala
object Solution {
    def minimumRecolors(blocks: String, k: Int): Int = {
        val n = blocks.length
        var whiteCount = 0
        // count whites in the first window
        for (i <- 0 until k) {
            if (blocks.charAt(i) == 'W') whiteCount += 1
        }
        var minRecolors = whiteCount
        // slide the window
        for (i <- k until n) {
            if (blocks.charAt(i - k) == 'W') whiteCount -= 1
            if (blocks.charAt(i) == 'W') whiteCount += 1
            if (whiteCount < minRecolors) minRecolors = whiteCount
        }
        minRecolors
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_recolors(blocks: String, k: i32) -> i32 {
        let bytes = blocks.as_bytes();
        let n = bytes.len();
        let k = k as usize;
        let mut white = 0usize;
        for i in 0..k {
            if bytes[i] == b'W' {
                white += 1;
            }
        }
        let mut ans = white;
        for i in k..n {
            if bytes[i - k] == b'W' {
                white -= 1;
            }
            if bytes[i] == b'W' {
                white += 1;
            }
            if white < ans {
                ans = white;
            }
        }
        ans as i32
    }
}
```

## Racket

```racket
(define/contract (minimum-recolors blocks k)
  (-> string? exact-integer? exact-integer?)
  (let* ((n (string-length blocks))
         ;; count whites in the first window [0, k)
         (initial-count
          (let loop ((i 0) (c 0))
            (if (= i k)
                c
                (loop (+ i 1)
                      (+ c (if (char=? (string-ref blocks i) #\W) 1 0))))))
         (min-count initial-count))
    ;; slide the window from position k to n-1
    (let loop ((i k) (curr initial-count) (best min-count))
      (if (= i n)
          best
          (let* ((out-char (string-ref blocks (- i k)))
                 (in-char  (string-ref blocks i))
                 (new-curr (+ curr
                              (if (char=? in-char #\W) 1 0)
                              (if (char=? out-char #\W) -1 0))))
            (loop (+ i 1) new-curr (min best new-curr)))))))
```

## Erlang

```erlang
-spec minimum_recolors(Blocks :: unicode:unicode_binary(), K :: integer()) -> integer().
minimum_recolors(Blocks, K) ->
    List = binary:bin_to_list(Blocks),
    InitCount = count_whites(lists:sublist(List, K)),
    N = length(List),
    slide(K, InitCount, InitCount, List, K, N).

count_whites([]) -> 0;
count_whites([H|T]) ->
    (if H == $W -> 1; true -> 0 end) + count_whites(T).

slide(Index, Count, Min, _List, _K, N) when Index >= N ->
    Min;
slide(Index, Count, Min, List, K, N) ->
    NewChar = lists:nth(Index + 1, List),
    OldChar = lists:nth(Index - K + 1, List),
    DeltaNew = if NewChar == $W -> 1; true -> 0 end,
    DeltaOld = if OldChar == $W -> 1; true -> 0 end,
    Count1 = Count + DeltaNew - DeltaOld,
    Min1 = erlang:min(Min, Count1),
    slide(Index + 1, Count1, Min1, List, K, N).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_recolors(blocks :: String.t(), k :: integer) :: integer
  def minimum_recolors(blocks, k) do
    chars = String.to_charlist(blocks)
    tuple = List.to_tuple(chars)
    n = tuple_size(tuple)

    whites =
      Enum.reduce(0..(k - 1), 0, fn i, acc ->
        if elem(tuple, i) == ?W, do: acc + 1, else: acc
      end)

    if n == k do
      whites
    else
      {_final_w, min_whites} =
        Enum.reduce(k..(n - 1), {whites, whites}, fn i, {w, m} ->
          w = if elem(tuple, i - k) == ?W, do: w - 1, else: w
          w = if elem(tuple, i) == ?W, do: w + 1, else: w
          {w, min(m, w)}
        end)

      min_whites
    end
  end
end
```
