# 2201. Count Artifacts That Can Be Extracted

## Cpp

```cpp
class Solution {
public:
    int digArtifacts(int n, vector<vector<int>>& artifacts, vector<vector<int>>& dig) {
        unordered_set<int> dug;
        dug.reserve(dig.size() * 2);
        for (const auto& d : dig) {
            dug.insert(d[0] * n + d[1]);
        }
        int extracted = 0;
        for (const auto& a : artifacts) {
            bool canExtract = true;
            for (int r = a[0]; r <= a[2] && canExtract; ++r) {
                for (int c = a[1]; c <= a[3]; ++c) {
                    if (!dug.count(r * n + c)) {
                        canExtract = false;
                        break;
                    }
                }
            }
            if (canExtract) ++extracted;
        }
        return extracted;
    }
};
```

## Java

```java
class Solution {
    public int digArtifacts(int n, int[][] artifacts, int[][] dig) {
        boolean[][] dug = new boolean[n][n];
        for (int[] d : dig) {
            dug[d[0]][d[1]] = true;
        }
        int count = 0;
        for (int[] a : artifacts) {
            boolean canExtract = true;
            for (int r = a[0]; r <= a[2] && canExtract; r++) {
                for (int c = a[1]; c <= a[3]; c++) {
                    if (!dug[r][c]) {
                        canExtract = false;
                        break;
                    }
                }
            }
            if (canExtract) {
                count++;
            }
        }
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def digArtifacts(self, n, artifacts, dig):
        """
        :type n: int
        :type artifacts: List[List[int]]
        :type dig: List[List[int]]
        :rtype: int
        """
        dug = set((r, c) for r, c in dig)
        extracted = 0
        for r1, c1, r2, c2 in artifacts:
            complete = True
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if (r, c) not in dug:
                        complete = False
                        break
                if not complete:
                    break
            if complete:
                extracted += 1
        return extracted
```

## Python3

```python
from typing import List

class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        dug = set((r, c) for r, c in dig)
        extracted = 0
        for r1, c1, r2, c2 in artifacts:
            all_dug = True
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if (r, c) not in dug:
                        all_dug = False
                        break
                if not all_dug:
                    break
            if all_dug:
                extracted += 1
        return extracted
```

## C

```c
#include <stdlib.h>

int digArtifacts(int n, int** artifacts, int artifactsSize, int* artifactsColSize,
                 int** dig, int digSize, int* digColSize) {
    char *dug = (char *)calloc((size_t)n * n, sizeof(char));
    for (int i = 0; i < digSize; ++i) {
        int r = dig[i][0];
        int c = dig[i][1];
        dug[r * n + c] = 1;
    }

    int extracted = 0;
    for (int i = 0; i < artifactsSize; ++i) {
        int r1 = artifacts[i][0];
        int c1 = artifacts[i][1];
        int r2 = artifacts[i][2];
        int c2 = artifacts[i][3];
        int ok = 1;
        for (int r = r1; r <= r2 && ok; ++r) {
            for (int c = c1; c <= c2; ++c) {
                if (!dug[r * n + c]) {
                    ok = 0;
                    break;
                }
            }
        }
        if (ok) extracted++;
    }

    free(dug);
    return extracted;
}
```

## Csharp

```csharp
public class Solution
{
    public int DigArtifacts(int n, int[][] artifacts, int[][] dig)
    {
        var dug = new System.Collections.Generic.HashSet<int>();
        foreach (var d in dig)
        {
            int key = d[0] * n + d[1];
            dug.Add(key);
        }

        int extracted = 0;
        foreach (var a in artifacts)
        {
            bool allDug = true;
            for (int r = a[0]; r <= a[2] && allDug; r++)
            {
                for (int c = a[1]; c <= a[3]; c++)
                {
                    if (!dug.Contains(r * n + c))
                    {
                        allDug = false;
                        break;
                    }
                }
            }
            if (allDug) extracted++;
        }

        return extracted;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} artifacts
 * @param {number[][]} dig
 * @return {number}
 */
var digArtifacts = function(n, artifacts, dig) {
    const dugSet = new Set();
    for (const [r, c] of dig) {
        dugSet.add(r + ',' + c);
    }
    
    let extracted = 0;
    for (const art of artifacts) {
        const [r1, c1, r2, c2] = art;
        let allDug = true;
        for (let r = r1; r <= r2 && allDug; r++) {
            for (let c = c1; c <= c2; c++) {
                if (!dugSet.has(r + ',' + c)) {
                    allDug = false;
                    break;
                }
            }
        }
        if (allDug) extracted++;
    }
    
    return extracted;
};
```

## Typescript

```typescript
function digArtifacts(n: number, artifacts: number[][], dig: number[][]): number {
    const dug = new Set<number>();
    for (const [r, c] of dig) {
        dug.add(r * n + c);
    }
    let extracted = 0;
    for (const [r1, c1, r2, c2] of artifacts) {
        let canExtract = true;
        for (let r = r1; r <= r2 && canExtract; r++) {
            for (let c = c1; c <= c2; c++) {
                if (!dug.has(r * n + c)) {
                    canExtract = false;
                    break;
                }
            }
        }
        if (canExtract) extracted++;
    }
    return extracted;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $artifacts
     * @param Integer[][] $dig
     * @return Integer
     */
    function digArtifacts($n, $artifacts, $dig) {
        $dug = [];
        foreach ($dig as $cell) {
            $key = $cell[0] . ',' . $cell[1];
            $dug[$key] = true;
        }

        $extracted = 0;
        foreach ($artifacts as $a) {
            [$r1, $c1, $r2, $c2] = $a;
            $canExtract = true;
            for ($i = $r1; $i <= $r2 && $canExtract; $i++) {
                for ($j = $c1; $j <= $c2; $j++) {
                    $key = $i . ',' . $j;
                    if (!isset($dug[$key])) {
                        $canExtract = false;
                        break;
                    }
                }
            }
            if ($canExtract) {
                $extracted++;
            }
        }

        return $extracted;
    }
}
```

## Swift

```swift
class Solution {
    func digArtifacts(_ n: Int, _ artifacts: [[Int]], _ dig: [[Int]]) -> Int {
        var dugSet = Set<Int>()
        for d in dig {
            let key = d[0] * n + d[1]
            dugSet.insert(key)
        }
        
        var extracted = 0
        for a in artifacts {
            let r1 = a[0], c1 = a[1], r2 = a[2], c2 = a[3]
            var canExtract = true
            for r in r1...r2 {
                for c in c1...c2 {
                    if !dugSet.contains(r * n + c) {
                        canExtract = false
                        break
                    }
                }
                if !canExtract { break }
            }
            if canExtract {
                extracted += 1
            }
        }
        return extracted
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun digArtifacts(n: Int, artifacts: Array<IntArray>, dig: Array<IntArray>): Int {
        val dug = Array(n) { BooleanArray(n) }
        for (d in dig) {
            dug[d[0]][d[1]] = true
        }
        var count = 0
        for (a in artifacts) {
            var ok = true
            for (r in a[0]..a[2]) {
                for (c in a[1]..a[3]) {
                    if (!dug[r][c]) {
                        ok = false
                        break
                    }
                }
                if (!ok) break
            }
            if (ok) count++
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int digArtifacts(int n, List<List<int>> artifacts, List<List<int>> dig) {
    final Set<int> dugSet = {};
    for (var d in dig) {
      dugSet.add(d[0] * n + d[1]);
    }
    int count = 0;
    for (var a in artifacts) {
      bool allDug = true;
      for (int r = a[0]; r <= a[2]; ++r) {
        for (int c = a[1]; c <= a[3]; ++c) {
          if (!dugSet.contains(r * n + c)) {
            allDug = false;
            break;
          }
        }
        if (!allDug) break;
      }
      if (allDug) count++;
    }
    return count;
  }
}
```

## Golang

```go
func digArtifacts(n int, artifacts [][]int, dig [][]int) int {
	dug := make(map[int]struct{}, len(dig))
	for _, d := range dig {
		key := d[0]*n + d[1]
		dug[key] = struct{}{}
	}
	count := 0
	for _, a := range artifacts {
		r1, c1, r2, c2 := a[0], a[1], a[2], a[3]
		full := true
		for i := r1; i <= r2 && full; i++ {
			for j := c1; j <= c2; j++ {
				if _, ok := dug[i*n+j]; !ok {
					full = false
					break
				}
			}
		}
		if full {
			count++
		}
	}
	return count
}
```

## Ruby

```ruby
def dig_artifacts(n, artifacts, dig)
  require 'set'
  dug = Set.new
  dig.each { |r, c| dug.add([r, c]) }

  count = 0
  artifacts.each do |r1, c1, r2, c2|
    fully = true
    (r1..r2).each do |r|
      (c1..c2).each do |c|
        unless dug.include?([r, c])
          fully = false
          break
        end
      end
      break unless fully
    end
    count += 1 if fully
  end

  count
end
```

## Scala

```scala
object Solution {
  def digArtifacts(n: Int, artifacts: Array[Array[Int]], dig: Array[Array[Int]]): Int = {
    val dug = Array.ofDim[Boolean](n, n)
    var i = 0
    while (i < dig.length) {
      val r = dig(i)(0)
      val c = dig(i)(1)
      dug(r)(c) = true
      i += 1
    }

    var count = 0
    var aIdx = 0
    while (aIdx < artifacts.length) {
      val art = artifacts(aIdx)
      val r1 = art(0)
      val c1 = art(1)
      val r2 = art(2)
      val c2 = art(3)

      var allDug = true
      var r = r1
      while (r <= r2 && allDug) {
        var c = c1
        while (c <= c2 && allDug) {
          if (!dug(r)(c)) allDug = false
          c += 1
        }
        r += 1
      }

      if (allDug) count += 1
      aIdx += 1
    }

    count
  }
}
```

## Rust

```rust
impl Solution {
    pub fn dig_artifacts(n: i32, artifacts: Vec<Vec<i32>>, dig: Vec<Vec<i32>>) -> i32 {
        let n_usize = n as usize;
        let mut dug = vec![vec![false; n_usize]; n_usize];
        for d in dig.iter() {
            let r = d[0] as usize;
            let c = d[1] as usize;
            dug[r][c] = true;
        }
        let mut ans = 0i32;
        for art in artifacts.iter() {
            let r1 = art[0] as usize;
            let c1 = art[1] as usize;
            let r2 = art[2] as usize;
            let c2 = art[3] as usize;
            let mut ok = true;
            for i in r1..=r2 {
                for j in c1..=c2 {
                    if !dug[i][j] {
                        ok = false;
                        break;
                    }
                }
                if !ok {
                    break;
                }
            }
            if ok {
                ans += 1;
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (dig-artifacts n artifacts dig)
  (-> exact-integer? (listof (listof exact-integer?)) (listof (listof exact-integer?)) exact-integer?)
  (let ((dug-set (make-hash)))
    (for ([cell dig])
      (hash-set! dug-set (list (first cell) (second cell)) #t))
    (define (artifact-extracted? r1 c1 r2 c2)
      (for/and ([r (in-range r1 (+ r2 1))]
                [c (in-range c1 (+ c2 1))])
        (hash-has-key? dug-set (list r c))))
    (let loop ((arts artifacts) (cnt 0))
      (if (null? arts)
          cnt
          (let* ((a (car arts))
                 (r1 (list-ref a 0))
                 (c1 (list-ref a 1))
                 (r2 (list-ref a 2))
                 (c2 (list-ref a 3)))
            (loop (cdr arts) (+ cnt (if (artifact-extracted? r1 c1 r2 c2) 1 0))))))))
```

## Erlang

```erlang
-module(solution).
-export([dig_artifacts/3]).

-spec dig_artifacts(N :: integer(), Artifacts :: [[integer()]], Dig :: [[integer()]]) -> integer().
dig_artifacts(_N, Artifacts, Dig) ->
    DigMap = maps:from_list([{ {R, C}, true } || [R, C] <- Dig]),
    count_extracted(Artifacts, DigMap, 0).

count_extracted([], _DigMap, Acc) ->
    Acc;
count_extracted([Artifact | Rest], DigMap, Acc) ->
    case artifact_extracted(Artifact, DigMap) of
        true -> count_extracted(Rest, DigMap, Acc + 1);
        false -> count_extracted(Rest, DigMap, Acc)
    end.

artifact_extracted([R1, C1, R2, C2], DigMap) ->
    check_cells(R1, C1, R2, C2, C1, DigMap).

check_cells(R, _C, R2, _C2, _CStart, _DigMap) when R > R2 ->
    true;
check_cells(R, C, R2, C2, CStart, DigMap) ->
    case maps:is_key({R, C}, DigMap) of
        true ->
            if C < C2 ->
                    check_cells(R, C + 1, R2, C2, CStart, DigMap);
               true -> % C == C2, move to next row
                    check_cells(R + 1, CStart, R2, C2, CStart, DigMap)
            end;
        false ->
            false
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec dig_artifacts(integer, [[integer]], [[integer]]) :: integer
  def dig_artifacts(_n, artifacts, dig) do
    dug_set =
      Enum.reduce(dig, MapSet.new(), fn [r, c], acc ->
        MapSet.put(acc, {r, c})
      end)

    Enum.count(artifacts, fn [r1, c1, r2, c2] ->
      all_dug?(r1, c1, r2, c2, dug_set)
    end)
  end

  defp all_dug?(r1, c1, r2, c2, dug_set) do
    Enum.all?(r1..r2, fn r ->
      Enum.all?(c1..c2, fn c ->
        MapSet.member?(dug_set, {r, c})
      end)
    end)
  end
end
```
