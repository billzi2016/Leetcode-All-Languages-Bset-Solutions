# 2001. Number of Pairs of Interchangeable Rectangles

## Cpp

```cpp
class Solution {
public:
    long long interchangeableRectangles(vector<vector<int>>& rectangles) {
        unordered_map<long long, long long> freq;
        freq.reserve(rectangles.size() * 2);
        for (const auto& rec : rectangles) {
            int w = rec[0], h = rec[1];
            int g = std::gcd(w, h);
            long long key = ((long long)(w / g) << 32) | (unsigned int)(h / g);
            ++freq[key];
        }
        long long ans = 0;
        for (const auto& kv : freq) {
            long long c = kv.second;
            ans += c * (c - 1) / 2;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long interchangeableRectangles(int[][] rectangles) {
        java.util.Map<Long, Integer> freq = new java.util.HashMap<>();
        long result = 0L;
        for (int[] rect : rectangles) {
            int w = rect[0];
            int h = rect[1];
            int g = gcd(w, h);
            int rw = w / g;
            int rh = h / g;
            long key = ((long) rw << 32) | (rh & 0xffffffffL);
            int count = freq.getOrDefault(key, 0);
            result += count;
            freq.put(key, count + 1);
        }
        return result;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int tmp = a % b;
            a = b;
            b = tmp;
        }
        return a;
    }
}
```

## Python

```python
class Solution(object):
    def interchangeableRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        from math import gcd
        freq = {}
        for w, h in rectangles:
            g = gcd(w, h)
            key = (w // g, h // g)
            freq[key] = freq.get(key, 0) + 1
        ans = 0
        for count in freq.values():
            if count > 1:
                ans += count * (count - 1) // 2
        return ans
```

## Python3

```python
class Solution:
    def interchangeableRectangles(self, rectangles):
        from math import gcd
        freq = {}
        ans = 0
        for w, h in rectangles:
            g = gcd(w, h)
            key = (w // g, h // g)
            cnt = freq.get(key, 0)
            ans += cnt
            freq[key] = cnt + 1
        return ans
```

## C

```c
#include <stdlib.h>

static int gcd(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

typedef struct {
    int w;
    int h;
} Ratio;

static int cmpRatio(const void *a, const void *b) {
    const Ratio *ra = (const Ratio *)a;
    const Ratio *rb = (const Ratio *)b;
    if (ra->w != rb->w) return ra->w - rb->w;
    return ra->h - rb->h;
}

long long interchangeableRectangles(int** rectangles, int rectanglesSize, int* rectanglesColSize) {
    if (rectanglesSize <= 1) return 0LL;
    Ratio *arr = (Ratio *)malloc(rectanglesSize * sizeof(Ratio));
    for (int i = 0; i < rectanglesSize; ++i) {
        int w = rectangles[i][0];
        int h = rectangles[i][1];
        int g = gcd(w, h);
        arr[i].w = w / g;
        arr[i].h = h / g;
    }
    qsort(arr, rectanglesSize, sizeof(Ratio), cmpRatio);
    long long ans = 0, cnt = 1;
    for (int i = 1; i < rectanglesSize; ++i) {
        if (arr[i].w == arr[i - 1].w && arr[i].h == arr[i - 1].h) {
            ++cnt;
        } else {
            ans += cnt * (cnt - 1) / 2;
            cnt = 1;
        }
    }
    ans += cnt * (cnt - 1) / 2;
    free(arr);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long InterchangeableRectangles(int[][] rectangles) {
        var dict = new Dictionary<(int, int), long>();
        long ans = 0;
        foreach (var rec in rectangles) {
            int w = rec[0];
            int h = rec[1];
            int g = Gcd(w, h);
            var key = (w / g, h / g);
            if (dict.TryGetValue(key, out long cnt)) {
                ans += cnt;
                dict[key] = cnt + 1;
            } else {
                dict[key] = 1;
            }
        }
        return ans;
    }

    private int Gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} rectangles
 * @return {number}
 */
var interchangeableRectangles = function(rectangles) {
    const map = new Map();
    
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    
    for (const [w, h] of rectangles) {
        const g = gcd(w, h);
        const key = `${w / g}/${h / g}`;
        map.set(key, (map.get(key) || 0) + 1);
    }
    
    let total = 0;
    for (const cnt of map.values()) {
        total += cnt * (cnt - 1) / 2;
    }
    return total;
};
```

## Typescript

```typescript
function interchangeableRectangles(rectangles: number[][]): number {
    const map = new Map<string, number>();
    let ans = 0;

    const gcd = (a: number, b: number): number => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };

    for (const [w, h] of rectangles) {
        const g = gcd(w, h);
        const key = `${w / g}/${h / g}`;
        const cnt = map.get(key) ?? 0;
        ans += cnt;
        map.set(key, cnt + 1);
    }

    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $rectangles
     * @return Integer
     */
    function interchangeableRectangles($rectangles) {
        $freq = [];
        foreach ($rectangles as $rect) {
            $w = $rect[0];
            $h = $rect[1];
            $g = $this->gcd($w, $h);
            $key = ($w / $g) . '/' . ($h / $g);
            if (!isset($freq[$key])) {
                $freq[$key] = 0;
            }
            $freq[$key]++;
        }

        $ans = 0;
        foreach ($freq as $cnt) {
            if ($cnt > 1) {
                $ans += intdiv($cnt * ($cnt - 1), 2);
            }
        }
        return $ans;
    }

    private function gcd($a, $b) {
        while ($b != 0) {
            $tmp = $a % $b;
            $a = $b;
            $b = $tmp;
        }
        return $a;
    }
}
```

## Swift

```swift
class Solution {
    func interchangeableRectangles(_ rectangles: [[Int]]) -> Int {
        var freq = [Ratio:Int]()
        for rect in rectangles {
            let w = rect[0]
            let h = rect[1]
            let g = gcd(w, h)
            let key = Ratio(w / g, h / g)
            freq[key, default: 0] += 1
        }
        var result: Int64 = 0
        for count in freq.values {
            if count > 1 {
                result += Int64(count) * Int64(count - 1) / 2
            }
        }
        return Int(result)
    }

    private func gcd(_ a: Int, _ b: Int) -> Int {
        var x = a
        var y = b
        while y != 0 {
            let temp = x % y
            x = y
            y = temp
        }
        return x
    }
}

struct Ratio: Hashable {
    let w: Int
    let h: Int

    init(_ w: Int, _ h: Int) {
        self.w = w
        self.h = h
    }

    func hash(into hasher: inout Hasher) {
        hasher.combine(w)
        hasher.combine(h)
    }

    static func == (lhs: Ratio, rhs: Ratio) -> Bool {
        return lhs.w == rhs.w && lhs.h == rhs.h
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun interchangeableRectangles(rectangles: Array<IntArray>): Long {
        val map = HashMap<Long, Int>()
        var result = 0L
        for (rect in rectangles) {
            var w = rect[0]
            var h = rect[1]
            val g = gcd(w, h)
            w /= g
            h /= g
            val key = (w.toLong() shl 32) xor h.toLong()
            val cnt = map.getOrDefault(key, 0)
            result += cnt.toLong()
            map[key] = cnt + 1
        }
        return result
    }

    private fun gcd(a: Int, b: Int): Int {
        var x = a
        var y = b
        while (y != 0) {
            val tmp = x % y
            x = y
            y = tmp
        }
        return x
    }
}
```

## Dart

```dart
class Solution {
  int interchangeableRectangles(List<List<int>> rectangles) {
    final Map<String, int> freq = {};
    int result = 0;
    for (var rect in rectangles) {
      int w = rect[0];
      int h = rect[1];
      int g = _gcd(w, h);
      String key = '${w ~/ g}/${h ~/ g}';
      int count = freq[key] ?? 0;
      result += count;
      freq[key] = count + 1;
    }
    return result;
  }

  int _gcd(int a, int b) {
    while (b != 0) {
      int t = a % b;
      a = b;
      b = t;
    }
    return a;
  }
}
```

## Golang

```go
func interchangeableRectangles(rectangles [][]int) int64 {
	type frac struct {
		w, h int
	}
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}

	counts := make(map[frac]int64)
	var ans int64

	for _, r := range rectangles {
		w, h := r[0], r[1]
		g := gcd(w, h)
		f := frac{w / g, h / g}
		if c, ok := counts[f]; ok {
			ans += c
			counts[f] = c + 1
		} else {
			counts[f] = 1
		}
	}

	return ans
}
```

## Ruby

```ruby
def interchangeable_rectangles(rectangles)
  counts = Hash.new(0)
  ans = 0
  rectangles.each do |w, h|
    g = w.gcd(h)
    key = [w / g, h / g]
    ans += counts[key]
    counts[key] += 1
  end
  ans
end
```

## Scala

```scala
object Solution {
    def interchangeableRectangles(rectangles: Array[Array[Int]]): Long = {
        val freq = scala.collection.mutable.HashMap[(Int, Int), Long]()
        var ans: Long = 0L
        for (rect <- rectangles) {
            val w = rect(0)
            val h = rect(1)
            val g = gcd(w, h)
            val key = (w / g, h / g)
            val cnt = freq.getOrElse(key, 0L)
            ans += cnt
            freq.update(key, cnt + 1)
        }
        ans
    }

    @annotation.tailrec
    private def gcd(a: Int, b: Int): Int = {
        if (b == 0) a else gcd(b, a % b)
    }
}
```

## Rust

```rust
use std::collections::HashMap;

fn gcd(mut a: i32, mut b: i32) -> i32 {
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a
}

impl Solution {
    pub fn interchangeable_rectangles(rectangles: Vec<Vec<i32>>) -> i64 {
        let mut freq: HashMap<(i32, i32), i64> = HashMap::new();
        for rect in rectangles.iter() {
            let w = rect[0];
            let h = rect[1];
            let g = gcd(w, h);
            let key = (w / g, h / g);
            *freq.entry(key).or_insert(0) += 1;
        }
        let mut ans: i64 = 0;
        for &cnt in freq.values() {
            ans += cnt * (cnt - 1) / 2;
        }
        ans
    }
}
```

## Racket

```racket
(require racket/math)

(define/contract (interchangeable-rectangles rectangles)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let ([hash (make-hash)]
        [ans 0])
    (for ([pair rectangles])
      (match pair
        [(list w h)
         (define g (gcd w h))
         (define key (vector (/ w g) (/ h g)))
         (define cnt (hash-ref hash key 0))
         (set! ans (+ ans cnt))
         (hash-set! hash key (+ cnt 1))]))
    ans))
```

## Erlang

```erlang
-spec interchangeable_rectangles(Rectangles :: [[integer()]]) -> integer().
interchangeable_rectangles(Rectangles) ->
    FreqMap = lists:foldl(
        fun([W, H], Acc) ->
            G = erlang:gcd(W, H),
            Key = {W div G, H div G},
            maps:update_with(Key,
                fun(Prev) -> Prev + 1 end,
                1,
                Acc)
        end,
        #{},
        Rectangles),
    maps:fold(
        fun(_Key, Count, Sum) ->
            Sum + (Count * (Count - 1)) div 2
        end,
        0,
        FreqMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec interchangeable_rectangles(rectangles :: [[integer]]) :: integer
  def interchangeable_rectangles(rectangles) do
    freq_map =
      Enum.reduce(rectangles, %{}, fn [w, h], acc ->
        g = Integer.gcd(w, h)
        key = {div(w, g), div(h, g)}
        Map.update(acc, key, 1, &(&1 + 1))
      end)

    Enum.reduce(freq_map, 0, fn {_k, cnt}, sum ->
      sum + div(cnt * (cnt - 1), 2)
    end)
  end
end
```
