# 2515. Shortest Distance to Target String in a Circular Array

## Cpp

```cpp
class Solution {
public:
    int closestTarget(vector<string>& words, string target, int startIndex) {
        int n = words.size();
        int ans = INT_MAX;
        for (int i = 0; i < n; ++i) {
            if (words[i] == target) {
                int diff = abs(i - startIndex);
                int steps = min(diff, n - diff);
                ans = min(ans, steps);
            }
        }
        return ans == INT_MAX ? -1 : ans;
    }
};
```

## Java

```java
class Solution {
    public int closestTarget(String[] words, String target, int startIndex) {
        int n = words.length;
        int minDist = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            if (words[i].equals(target)) {
                int diff = Math.abs(i - startIndex);
                int dist = Math.min(diff, n - diff);
                if (dist < minDist) {
                    minDist = dist;
                }
            }
        }
        return minDist == Integer.MAX_VALUE ? -1 : minDist;
    }
}
```

## Python

```python
class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        n = len(words)
        min_dist = None
        for i, w in enumerate(words):
            if w == target:
                diff = abs(i - startIndex)
                dist = diff if diff <= n - diff else n - diff
                if min_dist is None or dist < min_dist:
                    min_dist = dist
        return -1 if min_dist is None else min_dist
```

## Python3

```python
from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_dist = None
        for i, w in enumerate(words):
            if w == target:
                forward = (i - startIndex) % n
                backward = (startIndex - i) % n
                dist = forward if forward < backward else backward
                if min_dist is None or dist < min_dist:
                    min_dist = dist
        return -1 if min_dist is None else min_dist
```

## C

```c
#include <string.h>
#include <limits.h>
#include <stdlib.h>

int closestTarget(char** words, int wordsSize, char* target, int startIndex) {
    int minDist = INT_MAX;
    for (int i = 0; i < wordsSize; ++i) {
        if (strcmp(words[i], target) == 0) {
            int diff = abs(i - startIndex);
            int dist = diff < (wordsSize - diff) ? diff : (wordsSize - diff);
            if (dist < minDist) {
                minDist = dist;
            }
        }
    }
    return (minDist == INT_MAX) ? -1 : minDist;
}
```

## Csharp

```csharp
public class Solution {
    public int ClosestTarget(string[] words, string target, int startIndex) {
        int n = words.Length;
        int best = int.MaxValue;
        for (int i = 0; i < n; i++) {
            if (words[i] == target) {
                int diff = Math.Abs(i - startIndex);
                int dist = Math.Min(diff, n - diff);
                if (dist < best) best = dist;
            }
        }
        return best == int.MaxValue ? -1 : best;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} words
 * @param {string} target
 * @param {number} startIndex
 * @return {number}
 */
var closestTarget = function(words, target, startIndex) {
    const n = words.length;
    let minDist = Infinity;
    for (let i = 0; i < n; ++i) {
        if (words[i] === target) {
            const clockwise = (i - startIndex + n) % n;
            const counterClockwise = (startIndex - i + n) % n;
            const dist = Math.min(clockwise, counterClockwise);
            if (dist < minDist) minDist = dist;
        }
    }
    return minDist === Infinity ? -1 : minDist;
};
```

## Typescript

```typescript
function closestTarget(words: string[], target: string, startIndex: number): number {
    const n = words.length;
    let minDist = Infinity;
    for (let i = 0; i < n; i++) {
        if (words[i] === target) {
            const diff = Math.abs(i - startIndex);
            const dist = Math.min(diff, n - diff);
            if (dist < minDist) minDist = dist;
        }
    }
    return minDist === Infinity ? -1 : minDist;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $words
     * @param String $target
     * @param Integer $startIndex
     * @return Integer
     */
    function closestTarget($words, $target, $startIndex) {
        $n = count($words);
        $minDist = PHP_INT_MAX;
        foreach ($words as $i => $w) {
            if ($w === $target) {
                $diff = abs($i - $startIndex);
                $dist = min($diff, $n - $diff);
                if ($dist < $minDist) {
                    $minDist = $dist;
                }
            }
        }
        return $minDist === PHP_INT_MAX ? -1 : $minDist;
    }
}
```

## Swift

```swift
class Solution {
    func closestTarget(_ words: [String], _ target: String, _ startIndex: Int) -> Int {
        let n = words.count
        var minDist = Int.max
        for i in 0..<n {
            if words[i] == target {
                let clockwise = (i - startIndex + n) % n
                let counterClockwise = (startIndex - i + n) % n
                let dist = min(clockwise, counterClockwise)
                if dist < minDist {
                    minDist = dist
                }
            }
        }
        return minDist == Int.max ? -1 : minDist
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun closestTarget(words: Array<String>, target: String, startIndex: Int): Int {
        val n = words.size
        var best = Int.MAX_VALUE
        for (i in words.indices) {
            if (words[i] == target) {
                val forward = (i - startIndex + n) % n
                val backward = (startIndex - i + n) % n
                val dist = kotlin.math.min(forward, backward)
                best = kotlin.math.min(best, dist)
            }
        }
        return if (best == Int.MAX_VALUE) -1 else best
    }
}
```

## Dart

```dart
class Solution {
  int closestTarget(List<String> words, String target, int startIndex) {
    int n = words.length;
    int minDist = n + 1; // sentinel larger than any possible distance
    for (int i = 0; i < n; i++) {
      if (words[i] == target) {
        int forward = (i - startIndex + n) % n;
        int backward = (startIndex - i + n) % n;
        int dist = forward < backward ? forward : backward;
        if (dist < minDist) {
          minDist = dist;
        }
      }
    }
    return minDist == n + 1 ? -1 : minDist;
  }
}
```

## Golang

```go
func closestTarget(words []string, target string, startIndex int) int {
	n := len(words)
	minDist := -1
	for i, w := range words {
		if w == target {
			// distance moving forward (right)
			fwd := (i - startIndex + n) % n
			// distance moving backward (left)
			bwd := (startIndex - i + n) % n
			dist := fwd
			if bwd < dist {
				dist = bwd
			}
			if minDist == -1 || dist < minDist {
				minDist = dist
			}
		}
	}
	return minDist
}
```

## Ruby

```ruby
def closest_target(words, target, start_index)
  n = words.length
  min_dist = nil
  words.each_with_index do |w, i|
    next unless w == target
    forward = (i - start_index) % n
    backward = (start_index - i) % n
    dist = forward < backward ? forward : backward
    min_dist = dist if min_dist.nil? || dist < min_dist
  end
  min_dist.nil? ? -1 : min_dist
end
```

## Scala

```scala
object Solution {
    def closestTarget(words: Array[String], target: String, startIndex: Int): Int = {
        val n = words.length
        var best = Int.MaxValue
        for (i <- 0 until n) {
            if (words(i) == target) {
                val cw = (i - startIndex + n) % n
                val ccw = (startIndex - i + n) % n
                val d = math.min(cw, ccw)
                if (d < best) best = d
            }
        }
        if (best == Int.MaxValue) -1 else best
    }
}
```

## Rust

```rust
impl Solution {
    pub fn closest_target(words: Vec<String>, target: String, start_index: i32) -> i32 {
        let n = words.len();
        let mut best = i32::MAX;
        for (i, w) in words.iter().enumerate() {
            if w == &target {
                let diff = ((i as i32) - start_index).abs();
                let dist = std::cmp::min(diff, n as i32 - diff);
                if dist < best {
                    best = dist;
                }
            }
        }
        if best == i32::MAX { -1 } else { best }
    }
}
```

## Racket

```racket
(define/contract (closest-target words target startIndex)
  (-> (listof string?) string? exact-integer? exact-integer?)
  (let* ((n (length words))
         (target-idxs
          (for/list ([i (in-range n)]
                     #:when (string=? (list-ref words i) target))
            i)))
    (if (null? target-idxs)
        -1
        (apply min
               (map (lambda (i)
                      (let ((diff (abs (- i startIndex))))
                        (min diff (- n diff))))
                    target-idxs)))))
```

## Erlang

```erlang
-spec closest_target(Words :: [unicode:unicode_binary()], Target :: unicode:unicode_binary(), StartIndex :: integer()) -> integer().
closest_target(Words, Target, StartIndex) ->
    N = length(Words),
    case find_min_distance(Words, Target, StartIndex, N, 0, undefined) of
        undefined -> -1;
        D -> D
    end.

find_min_distance([], _Target, _StartIndex, _N, _Idx, Min) ->
    Min;
find_min_distance([H|T], Target, StartIndex, N, Idx, Min) ->
    NewMin = case H of
        Target ->
            Diff = erlang:abs(Idx - StartIndex),
            Dist = erlang:min(Diff, N - Diff),
            case Min of
                undefined -> Dist;
                _ when Dist < Min -> Dist;
                _ -> Min
            end;
        _ -> Min
    end,
    find_min_distance(T, Target, StartIndex, N, Idx + 1, NewMin).
```

## Elixir

```elixir
defmodule Solution do
  @spec closest_target(words :: [String.t()], target :: String.t(), start_index :: integer()) :: integer()
  def closest_target(words, target, start_index) do
    n = length(words)

    distances =
      words
      |> Enum.with_index()
      |> Enum.reduce([], fn {word, idx}, acc ->
        if word == target do
          diff = abs(idx - start_index)
          dist = min(diff, n - diff)
          [dist | acc]
        else
          acc
        end
      end)

    case distances do
      [] -> -1
      _ -> Enum.min(distances)
    end
  end
end
```
