# 3160. Find the Number of Distinct Colors Among the Balls

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> queryResults(int limit, vector<vector<int>>& queries) {
        int n = queries.size();
        vector<int> result;
        result.reserve(n);
        
        unordered_map<long long, int> ballMap;
        ballMap.reserve(n * 2);
        unordered_map<int, int> colorCount;
        colorCount.reserve(n * 2);
        
        for (const auto& q : queries) {
            long long ball = q[0];
            int color = q[1];
            
            auto itBall = ballMap.find(ball);
            if (itBall != ballMap.end()) {
                int prevColor = itBall->second;
                auto itPrev = colorCount.find(prevColor);
                if (--(itPrev->second) == 0) {
                    colorCount.erase(itPrev);
                }
            }
            
            ballMap[ball] = color;
            ++colorCount[color];
            result.push_back((int)colorCount.size());
        }
        
        return result;
    }
};
```

## Java

```java
class Solution {
    public int[] queryResults(int limit, int[][] queries) {
        int n = queries.length;
        int[] result = new int[n];
        java.util.HashMap<Integer, Integer> ballMap = new java.util.HashMap<>();
        java.util.HashMap<Integer, Integer> colorCount = new java.util.HashMap<>();

        for (int i = 0; i < n; i++) {
            int ball = queries[i][0];
            int color = queries[i][1];

            if (ballMap.containsKey(ball)) {
                int prevColor = ballMap.get(ball);
                int cnt = colorCount.get(prevColor) - 1;
                if (cnt == 0) {
                    colorCount.remove(prevColor);
                } else {
                    colorCount.put(prevColor, cnt);
                }
            }

            ballMap.put(ball, color);
            colorCount.put(color, colorCount.getOrDefault(color, 0) + 1);

            result[i] = colorCount.size();
        }

        return result;
    }
}
```

## Python

```python
class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ball_to_color = {}
        color_cnt = {}
        res = []
        for ball, color in queries:
            # If the ball already has a color, decrement its count
            if ball in ball_to_color:
                prev = ball_to_color[ball]
                cnt = color_cnt[prev] - 1
                if cnt == 0:
                    del color_cnt[prev]
                else:
                    color_cnt[prev] = cnt
            # Assign new color to the ball
            ball_to_color[ball] = color
            color_cnt[color] = color_cnt.get(color, 0) + 1
            res.append(len(color_cnt))
        return res
```

## Python3

```python
from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_to_color = {}
        color_count = {}
        result = []
        for ball, color in queries:
            if ball in ball_to_color:
                prev = ball_to_color[ball]
                cnt = color_count[prev] - 1
                if cnt == 0:
                    del color_count[prev]
                else:
                    color_count[prev] = cnt
            ball_to_color[ball] = color
            color_count[color] = color_count.get(color, 0) + 1
            result.append(len(color_count))
        return result
```

## C

```c
#include <stdlib.h>

typedef struct {
    int *keys;
    int *vals;
    char *used;   // 0 = empty, 1 = occupied
    int cap;      // power of two
} IntIntMap;

static int nextPowerOfTwo(int n) {
    unsigned int v = (unsigned int)n;
    v--;
    v |= v >> 1;
    v |= v >> 2;
    v |= v >> 4;
    v |= v >> 8;
    v |= v >> 16;
    v++;
    return (int)v;
}

static void initMap(IntIntMap *m, int capacity) {
    m->cap = nextPowerOfTwo(capacity);
    m->keys = (int *)malloc(m->cap * sizeof(int));
    m->vals = (int *)malloc(m->cap * sizeof(int));
    m->used = (char *)calloc(m->cap, sizeof(char));
}

static void freeMap(IntIntMap *m) {
    free(m->keys);
    free(m->vals);
    free(m->used);
}

/* return pointer to value if key exists, otherwise NULL */
static int* mapGet(IntIntMap *m, int key) {
    unsigned int h = (unsigned int)key * 2654435761u;
    int idx = h & (m->cap - 1);
    while (m->used[idx]) {
        if (m->keys[idx] == key)
            return &m->vals[idx];
        idx = (idx + 1) & (m->cap - 1);
    }
    return NULL;
}

/* insert or update key with value; returns pointer to the stored value */
static int* mapPut(IntIntMap *m, int key, int value) {
    unsigned int h = (unsigned int)key * 2654435761u;
    int idx = h & (m->cap - 1);
    while (m->used[idx]) {
        if (m->keys[idx] == key) {
            m->vals[idx] = value;
            return &m->vals[idx];
        }
        idx = (idx + 1) & (m->cap - 1);
    }
    m->used[idx] = 1;
    m->keys[idx] = key;
    m->vals[idx] = value;
    return &m->vals[idx];
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* queryResults(int limit, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)limit; // unused
    int *result = (int *)malloc(queriesSize * sizeof(int));
    IntIntMap ballMap;
    IntIntMap colorCountMap;
    initMap(&ballMap, queriesSize * 2 + 4);
    initMap(&colorCountMap, queriesSize * 2 + 4);

    int distinctColors = 0;

    for (int i = 0; i < queriesSize; ++i) {
        int ball = queries[i][0];
        int color = queries[i][1];

        int *prevColorPtr = mapGet(&ballMap, ball);
        if (prevColorPtr) {
            int prevColor = *prevColorPtr;
            int *cntPrev = mapGet(&colorCountMap, prevColor);
            if (cntPrev) {
                (*cntPrev)--;
                if (*cntPrev == 0)
                    distinctColors--;
            }
        }

        mapPut(&ballMap, ball, color);

        int *cntNew = mapGet(&colorCountMap, color);
        if (cntNew) {
            if (*cntNew == 0)
                distinctColors++;
            (*cntNew)++;
        } else {
            mapPut(&colorCountMap, color, 1);
            distinctColors++;
        }

        result[i] = distinctColors;
    }

    freeMap(&ballMap);
    freeMap(&colorCountMap);

    *returnSize = queriesSize;
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] QueryResults(int limit, int[][] queries)
    {
        var ballMap = new Dictionary<int, int>();
        var colorCount = new Dictionary<int, int>();
        int n = queries.Length;
        var result = new int[n];

        for (int i = 0; i < n; i++)
        {
            int ball = queries[i][0];
            int color = queries[i][1];

            if (ballMap.TryGetValue(ball, out int prevColor))
            {
                // Decrease count of the previous color
                if (colorCount[prevColor] == 1)
                    colorCount.Remove(prevColor);
                else
                    colorCount[prevColor]--;
            }

            ballMap[ball] = color;

            if (colorCount.ContainsKey(color))
                colorCount[color]++;
            else
                colorCount[color] = 1;

            result[i] = colorCount.Count;
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} limit
 * @param {number[][]} queries
 * @return {number[]}
 */
var queryResults = function(limit, queries) {
    const ballMap = new Map();      // ball index -> current color
    const colorCount = new Map();   // color -> number of balls with this color
    const res = new Array(queries.length);
    
    for (let i = 0; i < queries.length; ++i) {
        const [ball, color] = queries[i];
        const prevColor = ballMap.get(ball);
        
        if (prevColor !== undefined) {
            if (prevColor !== color) {
                // decrement count of previous color
                const cntPrev = colorCount.get(prevColor);
                if (cntPrev === 1) {
                    colorCount.delete(prevColor);
                } else {
                    colorCount.set(prevColor, cntPrev - 1);
                }
                
                // increment count of new color
                colorCount.set(color, (colorCount.get(color) || 0) + 1);
                ballMap.set(ball, color);
            }
            // if same color, nothing changes
        } else {
            // ball was uncolored
            colorCount.set(color, (colorCount.get(color) || 0) + 1);
            ballMap.set(ball, color);
        }
        
        res[i] = colorCount.size;
    }
    
    return res;
};
```

## Typescript

```typescript
function queryResults(limit: number, queries: number[][]): number[] {
    const ballMap = new Map<number, number>();
    const colorCount = new Map<number, number>();
    const result: number[] = [];

    for (const [ball, color] of queries) {
        if (ballMap.has(ball)) {
            const prevColor = ballMap.get(ball)!;
            const prevCnt = (colorCount.get(prevColor) ?? 0) - 1;
            if (prevCnt === 0) {
                colorCount.delete(prevColor);
            } else {
                colorCount.set(prevColor, prevCnt);
            }
        }

        ballMap.set(ball, color);
        const newCnt = (colorCount.get(color) ?? 0) + 1;
        colorCount.set(color, newCnt);

        result.push(colorCount.size);
    }

    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $limit
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function queryResults($limit, $queries) {
        $ballMap = [];      // ball index => current color
        $colorCount = [];   // color => number of balls with this color
        $result = [];

        foreach ($queries as $q) {
            $ball = $q[0];
            $color = $q[1];

            if (isset($ballMap[$ball])) {
                $prevColor = $ballMap[$ball];
                // decrement count of previous color
                $colorCount[$prevColor]--;
                if ($colorCount[$prevColor] === 0) {
                    unset($colorCount[$prevColor]);
                }
            }

            // assign new color to ball
            $ballMap[$ball] = $color;
            if (isset($colorCount[$color])) {
                $colorCount[$color]++;
            } else {
                $colorCount[$color] = 1;
            }

            $result[] = count($colorCount);
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func queryResults(_ limit: Int, _ queries: [[Int]]) -> [Int] {
        var ballMap = [Int: Int]()
        var colorCount = [Int: Int]()
        var result = [Int]()
        result.reserveCapacity(queries.count)
        
        for q in queries {
            let ball = q[0]
            let newColor = q[1]
            
            if let prevColor = ballMap[ball] {
                if let cnt = colorCount[prevColor] {
                    if cnt == 1 {
                        colorCount.removeValue(forKey: prevColor)
                    } else {
                        colorCount[prevColor] = cnt - 1
                    }
                }
            }
            
            ballMap[ball] = newColor
            if let cnt = colorCount[newColor] {
                colorCount[newColor] = cnt + 1
            } else {
                colorCount[newColor] = 1
            }
            
            result.append(colorCount.count)
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun queryResults(limit: Int, queries: Array<IntArray>): IntArray {
        val n = queries.size
        val result = IntArray(n)
        val ballMap = HashMap<Int, Int>()
        val colorCount = HashMap<Int, Int>()
        var distinctColors = 0
        for (i in 0 until n) {
            val ball = queries[i][0]
            val color = queries[i][1]
            val prevColor = ballMap.put(ball, color)
            if (prevColor != null) {
                val cntPrev = colorCount[prevColor]!! - 1
                if (cntPrev == 0) {
                    colorCount.remove(prevColor)
                    distinctColors--
                } else {
                    colorCount[prevColor] = cntPrev
                }
            }
            val cntNew = (colorCount[color] ?: 0) + 1
            if (cntNew == 1) distinctColors++
            colorCount[color] = cntNew
            result[i] = distinctColors
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<int> queryResults(int limit, List<List<int>> queries) {
    final Map<int, int> ballMap = {};
    final Map<int, int> colorCount = {};
    final int n = queries.length;
    final List<int> result = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      final int ball = queries[i][0];
      final int color = queries[i][1];
      if (ballMap.containsKey(ball)) {
        final int prevColor = ballMap[ball]!;
        final int newCnt = colorCount[prevColor]! - 1;
        if (newCnt == 0) {
          colorCount.remove(prevColor);
        } else {
          colorCount[prevColor] = newCnt;
        }
      }
      ballMap[ball] = color;
      colorCount[color] = (colorCount[color] ?? 0) + 1;
      result[i] = colorCount.length;
    }
    return result;
  }
}
```

## Golang

```go
func queryResults(limit int, queries [][]int) []int {
	ballMap := make(map[int]int)
	colorCount := make(map[int]int)
	result := make([]int, len(queries))
	distinct := 0

	for i, q := range queries {
		ball, col := q[0], q[1]

		if prevCol, ok := ballMap[ball]; ok {
			if cnt := colorCount[prevCol] - 1; cnt == 0 {
				delete(colorCount, prevCol)
				distinct--
			} else {
				colorCount[prevCol] = cnt
			}
		}

		ballMap[ball] = col
		if cnt, ok := colorCount[col]; ok {
			colorCount[col] = cnt + 1
		} else {
			colorCount[col] = 1
			distinct++
		}
		result[i] = distinct
	}
	return result
}
```

## Ruby

```ruby
def query_results(limit, queries)
  ball_map = {}
  color_count = Hash.new(0)
  distinct = 0
  result = []

  queries.each do |ball, color|
    if ball_map.key?(ball)
      prev_color = ball_map[ball]
      new_cnt = color_count[prev_color] - 1
      if new_cnt == 0
        color_count.delete(prev_color)
        distinct -= 1
      else
        color_count[prev_color] = new_cnt
      end
    end

    if color_count.key?(color)
      color_count[color] += 1
    else
      color_count[color] = 1
      distinct += 1
    end

    ball_map[ball] = color
    result << distinct
  end

  result
end
```

## Scala

```scala
import scala.collection.mutable

object Solution {
  def queryResults(limit: Int, queries: Array[Array[Int]]): Array[Int] = {
    val ballMap = mutable.HashMap[Int, Int]()
    val colorCount = mutable.HashMap[Int, Int]()
    val n = queries.length
    val result = new Array[Int](n)

    var i = 0
    while (i < n) {
      val q = queries(i)
      val ball = q(0)
      val color = q(1)

      ballMap.get(ball) match {
        case Some(prevColor) =>
          val prevCnt = colorCount(prevColor) - 1
          if (prevCnt == 0) colorCount -= prevColor
          else colorCount.update(prevColor, prevCnt)
        case None => // do nothing
      }

      ballMap.update(ball, color)
      val newCnt = colorCount.getOrElse(color, 0) + 1
      colorCount.update(color, newCnt)

      result(i) = colorCount.size
      i += 1
    }

    result
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn query_results(limit: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut ball_map: HashMap<i32, i32> = HashMap::new(); // ball -> color
        let mut color_cnt: HashMap<i32, i32> = HashMap::new(); // color -> count
        let mut result: Vec<i32> = Vec::with_capacity(queries.len());

        for q in queries.iter() {
            let ball = q[0];
            let color = q[1];

            if let Some(prev_color) = ball_map.get(&ball).cloned() {
                // Decrease count of previous color
                if let Some(cnt) = color_cnt.get_mut(&prev_color) {
                    *cnt -= 1;
                    if *cnt == 0 {
                        color_cnt.remove(&prev_color);
                    }
                }
            }

            ball_map.insert(ball, color);
            *color_cnt.entry(color).or_insert(0) += 1;

            result.push(color_cnt.len() as i32);
        }

        result
    }
}
```

## Racket

```racket
(define/contract (query-results limit queries)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ((ball->color (make-hash))
         (color-count (make-hash)))
    (let loop ((qs queries) (acc '()))
      (if (null? qs)
          (reverse acc)
          (let* ((pair (car qs))
                 (ball (first pair))
                 (col  (second pair)))
            ;; remove previous color if ball was already colored
            (when (hash-has-key? ball->color ball)
              (let ((prev (hash-ref ball->color ball)))
                (define prevcnt (hash-ref color-count prev))
                (if (= prevcnt 1)
                    (hash-remove! color-count prev)
                    (hash-set! color-count prev (- prevcnt 1)))))
            ;; assign new color
            (hash-set! ball->color ball col)
            (hash-set! color-count col (+ 1 (hash-ref color-count col 0)))
            (loop (cdr qs) (cons (hash-count color-count) acc)))))))
```

## Erlang

```erlang
-spec query_results(Limit :: integer(), Queries :: [[integer()]]) -> [integer()].
query_results(_Limit, Queries) ->
    {_, _, _, RevRes} =
        lists:foldl(
            fun([Ball, Color], {BallMap, ColorMap, Distinct, Res}) ->
                case maps:is_key(Ball, BallMap) of
                    true ->
                        PrevColor = maps:get(Ball, BallMap),
                        PrevCount = maps:get(PrevColor, ColorMap),
                        NewPrevCount = PrevCount - 1,
                        {ColorMap1, Distinct1} =
                            if NewPrevCount == 0 ->
                                    {maps:remove(PrevColor, ColorMap), Distinct - 1};
                               true ->
                                    {maps:put(PrevColor, NewPrevCount, ColorMap), Distinct}
                            end,
                        case maps:is_key(Color, ColorMap1) of
                            true ->
                                Cur = maps:get(Color, ColorMap1),
                                ColorMap2 = maps:put(Color, Cur + 1, ColorMap1),
                                Distinct2 = Distinct1;
                            false ->
                                ColorMap2 = maps:put(Color, 1, ColorMap1),
                                Distinct2 = Distinct1 + 1
                        end,
                        BallMap2 = maps:put(Ball, Color, BallMap),
                        {BallMap2, ColorMap2, Distinct2, [Distinct2 | Res]};
                    false ->
                        case maps:is_key(Color, ColorMap) of
                            true ->
                                Cur = maps:get(Color, ColorMap),
                                ColorMap1 = maps:put(Color, Cur + 1, ColorMap),
                                Distinct1 = Distinct;
                            false ->
                                ColorMap1 = maps:put(Color, 1, ColorMap),
                                Distinct1 = Distinct + 1
                        end,
                        BallMap2 = maps:put(Ball, Color, BallMap),
                        {BallMap2, ColorMap1, Distinct1, [Distinct1 | Res]}
                end
            end,
            {#{}, #{}, 0, []},
            Queries),
    lists:reverse(RevRes).
```

## Elixir

```elixir
defmodule Solution do
  @spec query_results(limit :: integer, queries :: [[integer]]) :: [integer]
  def query_results(_limit, queries) do
    {rev_res, _ball_map, _color_cnt} =
      Enum.reduce(queries, {[], %{}, %{}}, fn [ball, color], {acc, ball_map, color_cnt} ->
        case Map.fetch(ball_map, ball) do
          {:ok, prev_color} ->
            # Decrease count of previous color
            cnt = Map.get(color_cnt, prev_color)
            updated_color_cnt =
              if cnt == 1 do
                Map.delete(color_cnt, prev_color)
              else
                Map.put(color_cnt, prev_color, cnt - 1)
              end

            # Increase count of new color
            inc_cnt = Map.get(updated_color_cnt, color, 0) + 1
            new_ball_map = Map.put(ball_map, ball, color)
            new_color_cnt = Map.put(updated_color_cnt, color, inc_cnt)

            {[map_size(new_color_cnt) | acc], new_ball_map, new_color_cnt}

          :error ->
            # Ball was uncolored before
            inc_cnt = Map.get(color_cnt, color, 0) + 1
            new_ball_map = Map.put(ball_map, ball, color)
            new_color_cnt = Map.put(color_cnt, color, inc_cnt)

            {[map_size(new_color_cnt) | acc], new_ball_map, new_color_cnt}
        end
      end)

    Enum.reverse(rev_res)
  end
end
```
