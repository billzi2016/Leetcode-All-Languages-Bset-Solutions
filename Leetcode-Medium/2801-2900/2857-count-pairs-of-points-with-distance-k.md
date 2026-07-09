# 2857. Count Pairs of Points With Distance k

## Cpp

```cpp
class Solution {
public:
    int countPairs(vector<vector<int>>& coordinates, int k) {
        unordered_map<long long,int> freq;
        long long ans = 0;
        const int SHIFT = 21; // since coordinates <= 1e6 < 2^20
        for (const auto& p : coordinates) {
            int x = p[0];
            int y = p[1];
            for (int dx = 0; dx <= k; ++dx) {
                int dy = k - dx;
                int tx = x ^ dx;
                int ty = y ^ dy;
                long long key = ((long long)tx << SHIFT) | (long long)ty;
                auto it = freq.find(key);
                if (it != freq.end()) ans += it->second;
            }
            long long curKey = ((long long)x << SHIFT) | (long long)y;
            ++freq[curKey];
        }
        return (int)ans;
    }
};
```

## Java

```java
class Solution {
    public int countPairs(List<List<Integer>> coordinates, int k) {
        Map<Long, Integer> freq = new HashMap<>();
        long ans = 0;
        for (List<Integer> point : coordinates) {
            int x = point.get(0);
            int y = point.get(1);
            for (int dx = 0; dx <= k; ++dx) {
                int dy = k - dx;
                int prevX = x ^ dx;
                int prevY = y ^ dy;
                long key = ((long) prevX << 21) | prevY;
                Integer cnt = freq.get(key);
                if (cnt != null) ans += cnt;
            }
            long curKey = ((long) x << 21) | y;
            freq.put(curKey, freq.getOrDefault(curKey, 0) + 1);
        }
        return (int) ans;
    }
}
```

## Python

```python
class Solution(object):
    def countPairs(self, coordinates, k):
        """
        :type coordinates: List[List[int]]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        freq = defaultdict(int)
        ans = 0
        for x, y in coordinates:
            for dx in range(k + 1):
                dy = k - dx
                ans += freq.get((x ^ dx, y ^ dy), 0)
            freq[(x, y)] += 1
        return ans
```

## Python3

```python
class Solution:
    def countPairs(self, coordinates, k):
        from collections import defaultdict
        freq = defaultdict(int)
        ans = 0
        for x, y in coordinates:
            for dx in range(k + 1):
                dy = k - dx
                xp = x ^ dx
                yp = y ^ dy
                ans += freq.get((xp, yp), 0)
            freq[(x, y)] += 1
        return ans
```

## C

```c
#include <stdlib.h>
#include <stdint.h>
#include <limits.h>

typedef struct {
    uint64_t key;
    int cnt;
} Entry;

static inline uint64_t make_key(int x, int y) {
    return ((uint64_t)(unsigned)x << 32) | (unsigned)y;
}

/* Find slot for a given key (existing or empty). */
static Entry* find_slot(Entry *table, int cap, uint64_t key) {
    uint64_t h = key * 11400714819323198485ULL; // Fibonacci hashing
    int idx = (int)(h & (uint64_t)(cap - 1));
    while (table[idx].key != UINT64_MAX && table[idx].key != key) {
        idx = (idx + 1) & (cap - 1);
    }
    return &table[idx];
}

int countPairs(int** coordinates, int coordinatesSize, int* coordinatesColSize, int k) {
    if (coordinatesSize < 2) return 0;
    
    int cap = 1;
    while (cap < coordinatesSize * 2) cap <<= 1;   // load factor <= 0.5
    Entry *table = (Entry *)malloc(sizeof(Entry) * cap);
    for (int i = 0; i < cap; ++i) table[i].key = UINT64_MAX, table[i].cnt = 0;
    
    long long ans = 0;
    for (int i = 0; i < coordinatesSize; ++i) {
        int x = coordinates[i][0];
        int y = coordinates[i][1];
        for (int dx = 0; dx <= k; ++dx) {
            int dy = k - dx;
            int tx = x ^ dx;
            int ty = y ^ dy;
            uint64_t tkey = make_key(tx, ty);
            Entry *e = find_slot(table, cap, tkey);
            if (e->key != UINT64_MAX) ans += e->cnt;
        }
        uint64_t curKey = make_key(x, y);
        Entry *c = find_slot(table, cap, curKey);
        if (c->key == UINT64_MAX) {
            c->key = curKey;
            c->cnt = 1;
        } else {
            c->cnt += 1;
        }
    }
    
    free(table);
    return (int)ans;
}
```

## Csharp

```csharp
public class Solution {
    public int CountPairs(IList<IList<int>> coordinates, int k) {
        var freq = new Dictionary<long, int>();
        long result = 0;
        const int SHIFT = 21; // enough to separate x and y (values up to ~1e6)
        foreach (var pt in coordinates) {
            int x = pt[0];
            int y = pt[1];
            for (int dx = 0; dx <= k; ++dx) {
                int dy = k - dx;
                int tx = x ^ dx;
                int ty = y ^ dy;
                long key = ((long)tx << SHIFT) | (uint)ty;
                if (freq.TryGetValue(key, out int cnt)) {
                    result += cnt;
                }
            }
            long curKey = ((long)x << SHIFT) | (uint)y;
            freq[curKey] = freq.GetValueOrDefault(curKey) + 1;
        }
        return (int)result;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} coordinates
 * @param {number} k
 * @return {number}
 */
var countPairs = function(coordinates, k) {
    const freq = new Map();
    let result = 0;
    for (const [x, y] of coordinates) {
        for (let dx = 0; dx <= k; ++dx) {
            const dy = k - dx;
            const tx = x ^ dx;
            const ty = y ^ dy;
            const key = tx + ',' + ty;
            if (freq.has(key)) result += freq.get(key);
        }
        const curKey = x + ',' + y;
        freq.set(curKey, (freq.get(curKey) || 0) + 1);
    }
    return result;
};
```

## Typescript

```typescript
function countPairs(coordinates: number[][], k: number): number {
    const freq = new Map<string, number>();
    let ans = 0;
    for (const [x, y] of coordinates) {
        for (let dx = 0; dx <= k; ++dx) {
            const dy = k - dx;
            const nx = x ^ dx;
            const ny = y ^ dy;
            const key = `${nx},${ny}`;
            const cnt = freq.get(key);
            if (cnt !== undefined) ans += cnt;
        }
        const curKey = `${x},${y}`;
        freq.set(curKey, (freq.get(curKey) ?? 0) + 1);
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $coordinates
     * @param Integer $k
     * @return Integer
     */
    function countPairs($coordinates, $k) {
        $map = [];
        $ans = 0;
        foreach ($coordinates as $point) {
            [$x, $y] = $point;
            for ($dx = 0; $dx <= $k; ++$dx) {
                $dy = $k - $dx;
                $tx = $x ^ $dx;
                $ty = $y ^ $dy;
                $key = $tx . ',' . $ty;
                if (isset($map[$key])) {
                    $ans += $map[$key];
                }
            }
            $curKey = $x . ',' . $y;
            if (!isset($map[$curKey])) {
                $map[$curKey] = 0;
            }
            $map[$curKey]++;
        }
        return $ans;
    }
}
```

## Swift

```swift
struct Pair: Hashable {
    let x: Int
    let y: Int
}

class Solution {
    func countPairs(_ coordinates: [[Int]], _ k: Int) -> Int {
        var freq = [Pair: Int]()
        var result = 0
        for point in coordinates {
            let x = point[0]
            let y = point[1]
            for a in 0...k {
                let b = k - a
                let targetX = x ^ a
                let targetY = y ^ b
                if let cnt = freq[Pair(x: targetX, y: targetY)] {
                    result += cnt
                }
            }
            let key = Pair(x: x, y: y)
            freq[key, default: 0] += 1
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countPairs(coordinates: List<List<Int>>, k: Int): Int {
        val freq = HashMap<Long, Int>()
        var result = 0L
        for (pt in coordinates) {
            val x1 = pt[0]
            val y1 = pt[1]
            for (xorX in 0..k) {
                val xorY = k - xorX
                val needX = x1 xor xorX
                val needY = y1 xor xorY
                val key = (needX.toLong() shl 32) or (needY.toLong() and 0xffffffffL)
                result += freq.getOrDefault(key, 0).toLong()
            }
            val curKey = (x1.toLong() shl 32) or (y1.toLong() and 0xffffffffL)
            freq[curKey] = freq.getOrDefault(curKey, 0) + 1
        }
        return result.toInt()
    }
}
```

## Dart

```dart
class Solution {
  int countPairs(List<List<int>> coordinates, int k) {
    const int SHIFT = 20; // since xi, yi <= 1e6 < 2^20
    final Map<int, int> freq = {};
    int ans = 0;
    for (var pt in coordinates) {
      int x = pt[0];
      int y = pt[1];
      for (int xd = 0; xd <= k; ++xd) {
        int yd = k - xd;
        int x2 = x ^ xd;
        int y2 = y ^ yd;
        int key = (x2 << SHIFT) | y2;
        ans += freq[key] ?? 0;
      }
      int curKey = (x << SHIFT) | y;
      freq[curKey] = (freq[curKey] ?? 0) + 1;
    }
    return ans;
  }
}
```

## Golang

```go
func countPairs(coordinates [][]int, k int) int {
	m := make(map[uint64]int)
	ans := 0
	for _, p := range coordinates {
		x, y := p[0], p[1]
		for dx := 0; dx <= k; dx++ {
			dy := k - dx
			tx := x ^ dx
			ty := y ^ dy
			key := (uint64(tx) << 32) | uint64(ty)
			if cnt, ok := m[key]; ok {
				ans += cnt
			}
		}
		curKey := (uint64(x) << 32) | uint64(y)
		m[curKey]++
	}
	return ans
}
```

## Ruby

```ruby
def count_pairs(coordinates, k)
  freq = Hash.new(0)
  ans = 0
  coordinates.each do |x1, y1|
    (0..k).each do |dx|
      dy = k - dx
      x2 = x1 ^ dx
      y2 = y1 ^ dy
      ans += freq[[x2, y2]]
    end
    freq[[x1, y1]] += 1
  end
  ans
end
```

## Scala

```scala
object Solution {
    def countPairs(coordinates: List[List[Int]], k: Int): Int = {
        import scala.collection.mutable

        val freq = mutable.Map[(Int, Int), Int]().withDefaultValue(0)
        var ans: Long = 0L

        for (pt <- coordinates) {
            val x1 = pt(0)
            val y1 = pt(1)

            var xorX = 0
            while (xorX <= k) {
                val xorY = k - xorX
                val tx = x1 ^ xorX
                val ty = y1 ^ xorY
                ans += freq((tx, ty))
                xorX += 1
            }

            freq((x1, y1)) = freq((x1, y1)) + 1
        }

        ans.toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_pairs(coordinates: Vec<Vec<i32>>, k: i32) -> i32 {
        use std::collections::HashMap;
        let mut freq: HashMap<(i32, i32), i64> = HashMap::new();
        let mut ans: i64 = 0;
        let k_usize = k as usize;

        for pt in coordinates.iter() {
            let x = pt[0];
            let y = pt[1];

            for dx_usize in 0..=k_usize {
                let dx = dx_usize as i32;
                let dy = k - dx; // dy >= 0 because dx <= k
                let cx = x ^ dx;
                let cy = y ^ dy;
                if let Some(cnt) = freq.get(&(cx, cy)) {
                    ans += *cnt;
                }
            }

            *freq.entry((x, y)).or_insert(0) += 1;
        }

        ans as i32
    }
}
```

## Racket

```racket
(define/contract (count-pairs coordinates k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ((hash (make-hash))
         (ans 0))
    (for ([pt coordinates])
      (match-define (list x1 y1) pt)
      (for ([x (in-range 0 (+ k 1))])
        (let* ((y (- k x))
               (x2 (bitwise-xor x1 x))
               (y2 (bitwise-xor y1 y))
               (key (list x2 y2)))
          (set! ans (+ ans (hash-ref hash key 0)))))
      (let ((key (list x1 y1)))
        (hash-set! hash key (+ 1 (hash-ref hash key 0)))))
    ans))
```

## Erlang

```erlang
-module(solution).
-export([count_pairs/2]).
-spec count_pairs(Coordinates :: [[integer()]], K :: integer()) -> integer().
count_pairs(Coordinates, K) ->
    {_, Ans} = lists:foldl(fun(Point, {Map, Acc}) ->
        [X1, Y1] = Point,
        Count = count_matches(K, X1, Y1, Map),
        NewMap = maps:update_with({X1, Y1},
                                  fun(C) -> C + 1 end,
                                  1,
                                  Map),
        {NewMap, Acc + Count}
    end, {#{}, 0}, Coordinates),
    Ans.

count_matches(K, X1, Y1, Map) ->
    count_matches(0, K, X1, Y1, Map, 0).

count_matches(X, K, X1, Y1, Map, Acc) when X =< K ->
    Y = K - X,
    X2 = bxor(X1, X),
    Y2 = bxor(Y1, Y),
    C = maps:get({X2, Y2}, Map, 0),
    count_matches(X + 1, K, X1, Y1, Map, Acc + C);
count_matches(_, _, _, _, _, Acc) ->
    Acc.
```

## Elixir

```elixir
defmodule Solution do
  require Bitwise

  @spec count_pairs(coordinates :: [[integer]], k :: integer) :: integer
  def count_pairs(coordinates, k) do
    range = 0..k

    {ans, _} =
      Enum.reduce(coordinates, {0, %{}}, fn [x, y], {acc, freq_map} ->
        contrib =
          Enum.reduce(range, 0, fn a, sum ->
            b = k - a
            xp = Bitwise.bxor(x, a)
            yp = Bitwise.bxor(y, b)

            sum + Map.get(freq_map, {xp, yp}, 0)
          end)

        new_acc = acc + contrib
        new_map = Map.update(freq_map, {x, y}, 1, &(&1 + 1))
        {new_acc, new_map}
      end)

    ans
  end
end
```
