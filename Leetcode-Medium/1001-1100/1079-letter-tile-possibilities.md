# 1079. Letter Tile Possibilities

## Cpp

```cpp
class Solution {
public:
    int numTilePossibilities(string tiles) {
        vector<int> cnt(26, 0);
        for (char c : tiles) cnt[c - 'A']++;
        return dfs(cnt);
    }
private:
    int dfs(vector<int>& cnt) {
        int total = 0;
        for (int i = 0; i < 26; ++i) {
            if (cnt[i] == 0) continue;
            cnt[i]--;
            total += 1;                 // count the sequence formed by this character
            total += dfs(cnt);          // extend further
            cnt[i]++;                   // backtrack
        }
        return total;
    }
};
```

## Java

```java
class Solution {
    public int numTilePossibilities(String tiles) {
        int[] count = new int[26];
        for (char c : tiles.toCharArray()) {
            count[c - 'A']++;
        }
        return dfs(count);
    }

    private int dfs(int[] count) {
        int total = 0;
        for (int i = 0; i < 26; i++) {
            if (count[i] == 0) continue;
            count[i]--;
            total += 1 + dfs(count);
            count[i]++;
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        cnt = [0] * 26
        for ch in tiles:
            cnt[ord(ch) - ord('A')] += 1

        def dfs():
            total = 0
            for i in range(26):
                if cnt[i]:
                    cnt[i] -= 1
                    total += 1 + dfs()
                    cnt[i] += 1
            return total

        return dfs()
```

## Python3

```python
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = [0] * 26
        for ch in tiles:
            cnt[ord(ch) - ord('A')] += 1

        def dfs() -> int:
            total = 0
            for i in range(26):
                if cnt[i] == 0:
                    continue
                cnt[i] -= 1
                total += 1          # count the sequence formed by adding this tile
                total += dfs()      # extend further
                cnt[i] += 1         # backtrack
            return total

        return dfs()
```

## C

```c
#include <stddef.h>

static int backtrack(int cnt[26]) {
    int total = 0;
    for (int i = 0; i < 26; ++i) {
        if (cnt[i] > 0) {
            total += 1;               // count the sequence formed by using this tile
            cnt[i]--;
            total += backtrack(cnt);   // extend further
            cnt[i]++;                  // backtrack
        }
    }
    return total;
}

int numTilePossibilities(char* tiles) {
    int cnt[26] = {0};
    for (char *p = tiles; *p != '\0'; ++p) {
        cnt[*p - 'A']++;
    }
    return backtrack(cnt);
}
```

## Csharp

```csharp
public class Solution
{
    public int NumTilePossibilities(string tiles)
    {
        int[] count = new int[26];
        foreach (char c in tiles)
            count[c - 'A']++;

        return Dfs(count);
    }

    private int Dfs(int[] count)
    {
        int total = 0;
        for (int i = 0; i < 26; i++)
        {
            if (count[i] == 0) continue;
            count[i]--;
            total += 1 + Dfs(count);
            count[i]++;
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} tiles
 * @return {number}
 */
var numTilePossibilities = function(tiles) {
    const cnt = new Array(26).fill(0);
    for (const ch of tiles) {
        cnt[ch.charCodeAt(0) - 65]++;
    }
    
    function dfs() {
        let total = 0;
        for (let i = 0; i < 26; i++) {
            if (cnt[i] === 0) continue;
            cnt[i]--;
            total += 1 + dfs();
            cnt[i]++;
        }
        return total;
    }
    
    return dfs();
};
```

## Typescript

```typescript
function numTilePossibilities(tiles: string): number {
    const count = new Array(26).fill(0);
    for (const ch of tiles) {
        count[ch.charCodeAt(0) - 65]++;
    }

    function dfs(): number {
        let total = 0;
        for (let i = 0; i < 26; i++) {
            if (count[i] === 0) continue;
            count[i]--;
            total += 1 + dfs();
            count[i]++;
        }
        return total;
    }

    return dfs();
}
```

## Php

```php
class Solution {

    /**
     * @param String $tiles
     * @return Integer
     */
    function numTilePossibilities($tiles) {
        $cnt = array_fill(0, 26, 0);
        $n = strlen($tiles);
        for ($i = 0; $i < $n; $i++) {
            $cnt[ord($tiles[$i]) - ord('A')]++;
        }

        $dfs = function (&$c) use (&$dfs) {
            $total = 0;
            for ($i = 0; $i < 26; $i++) {
                if ($c[$i] > 0) {
                    $c[$i]--;
                    $total += 1;               // count the sequence formed by this character
                    $total += $dfs($c);        // extend further
                    $c[$i]++;                  // backtrack
                }
            }
            return $total;
        };

        return $dfs($cnt);
    }
}
```

## Swift

```swift
class Solution {
    func numTilePossibilities(_ tiles: String) -> Int {
        var counts = [Int](repeating: 0, count: 26)
        let base = UnicodeScalar("A").value
        for scalar in tiles.unicodeScalars {
            let idx = Int(scalar.value - base)
            counts[idx] += 1
        }
        
        func dfs(_ cnt: inout [Int]) -> Int {
            var total = 0
            for i in 0..<26 {
                if cnt[i] > 0 {
                    cnt[i] -= 1
                    total += 1               // count the sequence formed by adding this character
                    total += dfs(&cnt)       // extend further
                    cnt[i] += 1              // backtrack
                }
            }
            return total
        }
        
        var mutableCounts = counts
        return dfs(&mutableCounts)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun numTilePossibilities(tiles: String): Int {
        val count = IntArray(26)
        for (c in tiles) {
            count[c - 'A']++
        }

        fun dfs(): Int {
            var total = 0
            for (i in 0 until 26) {
                if (count[i] > 0) {
                    count[i]--
                    total += 1 + dfs()
                    count[i]++
                }
            }
            return total
        }

        return dfs()
    }
}
```

## Dart

```dart
class Solution {
  int numTilePossibilities(String tiles) {
    List<int> cnt = List.filled(26, 0);
    for (int i = 0; i < tiles.length; i++) {
      cnt[tiles.codeUnitAt(i) - 65]++;
    }

    int dfs(List<int> counts) {
      int total = 0;
      for (int i = 0; i < 26; i++) {
        if (counts[i] == 0) continue;
        counts[i]--;
        total += 1 + dfs(counts);
        counts[i]++;
      }
      return total;
    }

    return dfs(cnt);
  }
}
```

## Golang

```go
func numTilePossibilities(tiles string) int {
	count := [26]int{}
	for _, ch := range tiles {
		count[int(ch-'A')]++
	}
	var dfs func() int
	dfs = func() int {
		total := 0
		for i := 0; i < 26; i++ {
			if count[i] == 0 {
				continue
			}
			count[i]--
			total += 1 + dfs()
			count[i]++
		}
		return total
	}
	return dfs()
}
```

## Ruby

```ruby
def num_tile_possibilities(tiles)
  counts = Array.new(26, 0)
  tiles.each_char { |c| counts[c.ord - 'A'.ord] += 1 }

  dfs = nil
  dfs = lambda do
    total = 0
    26.times do |i|
      next if counts[i] == 0
      total += 1
      counts[i] -= 1
      total += dfs.call
      counts[i] += 1
    end
    total
  end

  dfs.call
end
```

## Scala

```scala
object Solution {
    def numTilePossibilities(tiles: String): Int = {
        val cnt = Array.fill(26)(0)
        tiles.foreach(c => cnt(c - 'A') += 1)

        def dfs(): Int = {
            var total = 0
            for (i <- 0 until 26) {
                if (cnt(i) > 0) {
                    cnt(i) -= 1
                    total += 1 + dfs()
                    cnt(i) += 1
                }
            }
            total
        }

        dfs()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn num_tile_possibilities(tiles: String) -> i32 {
        let mut cnt = [0i32; 26];
        for b in tiles.bytes() {
            cnt[(b - b'A') as usize] += 1;
        }
        fn dfs(cnt: &mut [i32; 26]) -> i32 {
            let mut total = 0;
            for i in 0..26 {
                if cnt[i] > 0 {
                    total += 1;
                    cnt[i] -= 1;
                    total += dfs(cnt);
                    cnt[i] += 1;
                }
            }
            total
        }
        dfs(&mut cnt)
    }
}
```

## Racket

```racket
(define/contract (num-tile-possibilities tiles)
  (-> string? exact-integer?)
  (let ((cnt (make-vector 26 0)))
    (for ([ch (in-string tiles)])
      (let* ((idx (- (char->integer ch) (char->integer #\A)))
             (old (vector-ref cnt idx)))
        (vector-set! cnt idx (+ old 1))))
    (define (dfs)
      (let loop ((i 0) (total 0))
        (if (= i 26)
            total
            (let ((c (vector-ref cnt i)))
              (if (> c 0)
                  (begin
                    (vector-set! cnt i (- c 1))
                    (let ((added (+ 1 (dfs))))
                      (vector-set! cnt i c)
                      (loop (+ i 1) (+ total added))))
                  (loop (+ i 1) total))))))
    (dfs)))
```

## Erlang

```erlang
-module(solution).
-export([num_tile_possibilities/1]).

-spec num_tile_possibilities(Tiles :: unicode:unicode_binary()) -> integer().
num_tile_possibilities(Tiles) ->
    Counts = init_counts(binary_to_list(Tiles)),
    dfs_helper(Counts, 0).

init_counts(List) ->
    lists:foldl(fun(C, M) ->
        maps:update_with(C, fun(V) -> V + 1 end, 1, M)
    end, #{}, List).

dfs_helper(Counts, Acc) ->
    maps:fold(fun(_Char, Cnt, Sum) ->
        if Cnt > 0 ->
                NewCounts = maps:update(_Char, Cnt - 1, Counts),
                Sub = dfs_helper(NewCounts, 0),
                Sum + 1 + Sub
            ; true -> Sum
        end
    end, Acc, Counts).
```

## Elixir

```elixir
defmodule Solution do
  @spec num_tile_possibilities(String.t()) :: integer()
  def num_tile_possibilities(tiles) do
    counts =
      String.to_charlist(tiles)
      |> Enum.reduce(List.duplicate(0, 26), fn char, acc ->
        idx = char - ?A
        List.update_at(acc, idx, &(&1 + 1))
      end)

    dfs(counts)
  end

  defp dfs(counts) do
    Enum.reduce(0..25, 0, fn i, total ->
      case Enum.at(counts, i) do
        c when c > 0 ->
          new_counts = List.update_at(counts, i, &(&1 - 1))
          total + 1 + dfs(new_counts)

        _ ->
          total
      end
    end)
  end
end
```
