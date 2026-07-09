# 3273. Minimum Amount of Damage Dealt to Bob

## Cpp

```cpp
class Solution {
public:
    long long minDamage(int power, vector<int>& damage, vector<int>& health) {
        int n = damage.size();
        struct Enemy { long long d; long long t; };
        vector<Enemy> v;
        v.reserve(n);
        for (int i = 0; i < n; ++i) {
            long long t = (health[i] + power - 1LL) / power;
            v.push_back({damage[i], t});
        }
        sort(v.begin(), v.end(), [](const Enemy& a, const Enemy& b){
            // compare a.d / a.t > b.d / b.t  => a.d * b.t > b.d * a.t
            long long left = a.d * b.t;
            long long right = b.d * a.t;
            if (left != right) return left > right;
            // tie-breaker not essential, but keep larger damage first
            return a.d > b.d;
        });
        long long curTime = 0;
        long long ans = 0;
        for (const auto& e : v) {
            curTime += e.t;
            ans += e.d * curTime;
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long minDamage(int power, int[] damage, int[] health) {
        int n = damage.length;
        Enemy[] enemies = new Enemy[n];
        for (int i = 0; i < n; i++) {
            int hits = (health[i] + power - 1) / power; // ceil division
            enemies[i] = new Enemy(damage[i], hits);
        }
        java.util.Arrays.sort(enemies, (a, b) -> {
            long left = (long) b.dmg * a.hits;
            long right = (long) a.dmg * b.hits;
            if (left != right) return Long.compare(left, right); // descending dmg/hits
            // tie-breaker: higher damage first (optional)
            return Integer.compare(b.dmg, a.dmg);
        });
        long time = 0L;
        long total = 0L;
        for (Enemy e : enemies) {
            time += e.hits;
            total += (long) e.dmg * time;
        }
        return total;
    }

    private static class Enemy {
        int dmg;
        int hits;
        Enemy(int d, int h) {
            this.dmg = d;
            this.hits = h;
        }
    }
}
```

## Python

```python
class Solution(object):
    def minDamage(self, power, damage, health):
        """
        :type power: int
        :type damage: List[int]
        :type health: List[int]
        :rtype: int
        """
        n = len(damage)
        jobs = []
        for i in range(n):
            t = (health[i] + power - 1) // power  # required seconds to kill enemy i
            d = damage[i]
            jobs.append((t, d))
        
        from functools import cmp_to_key
        def cmp(a, b):
            # compare a.t / a.d  vs  b.t / b.d   without floating point
            left = a[0] * b[1]
            right = b[0] * a[1]
            if left < right:
                return -1
            elif left > right:
                return 1
            else:
                return 0
        
        jobs.sort(key=cmp_to_key(cmp))
        
        total_damage = 0
        cur_time = 0
        for t, d in jobs:
            cur_time += t
            total_damage += d * cur_time
        return total_damage
```

## Python3

```python
from typing import List
import functools

class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        jobs = []
        for h, d in zip(health, damage):
            t = (h + power - 1) // power  # hits needed
            jobs.append((t, d))

        def cmp(a, b):
            lhs = a[0] * b[1]
            rhs = b[0] * a[1]
            if lhs < rhs:
                return -1
            if lhs > rhs:
                return 1
            return 0

        jobs.sort(key=functools.cmp_to_key(cmp))

        cur_time = 0
        total_damage = 0
        for t, d in jobs:
            cur_time += t
            total_damage += d * cur_time
        return total_damage
```

## C

```c
#include <stdlib.h>

struct Enemy {
    int p;   // required seconds to kill
    int w;   // damage per second
};

static int cmpEnemy(const void *a, const void *b) {
    const struct Enemy *e1 = (const struct Enemy *)a;
    const struct Enemy *e2 = (const struct Enemy *)b;
    long long lhs = (long long)e1->p * e2->w;
    long long rhs = (long long)e2->p * e1->w;
    if (lhs < rhs) return -1;
    if (lhs > rhs) return 1;
    return 0;
}

long long minDamage(int power, int* damage, int damageSize, int* health, int healthSize) {
    int n = damageSize; // same as healthSize
    struct Enemy *arr = (struct Enemy *)malloc(sizeof(struct Enemy) * n);
    for (int i = 0; i < n; ++i) {
        arr[i].p = (health[i] + power - 1) / power; // ceil division
        arr[i].w = damage[i];
    }
    qsort(arr, n, sizeof(struct Enemy), cmpEnemy);
    long long curTime = 0;
    long long total = 0;
    for (int i = 0; i < n; ++i) {
        curTime += arr[i].p;
        total += (long long)arr[i].w * curTime;
    }
    free(arr);
    return total;
}
```

## Csharp

```csharp
public class Solution {
    public long MinDamage(int power, int[] damage, int[] health) {
        int n = damage.Length;
        var items = new (int t, int d)[n];
        for (int i = 0; i < n; i++) {
            int t = (health[i] + power - 1) / power; // ceil division
            items[i] = (t, damage[i]);
        }
        Array.Sort(items, (a, b) => {
            long left = (long)a.t * b.d;
            long right = (long)b.t * a.d;
            if (left == right) return 0;
            return left < right ? -1 : 1;
        });
        long cur = 0;
        long total = 0;
        foreach (var it in items) {
            cur += it.t;
            total += (long)it.d * cur;
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} power
 * @param {number[]} damage
 * @param {number[]} health
 * @return {number}
 */
var minDamage = function(power, damage, health) {
    const n = damage.length;
    const enemies = new Array(n);
    for (let i = 0; i < n; ++i) {
        const p = Math.floor((health[i] + power - 1) / power); // ceil
        enemies[i] = { p: p, d: damage[i] };
    }
    enemies.sort((a, b) => {
        const left = a.p * b.d;
        const right = b.p * a.d;
        if (left !== right) return left - right;
        return 0;
    });
    let time = 0;
    let total = 0;
    for (const e of enemies) {
        time += e.p;
        total += e.d * time;
    }
    return total;
};
```

## Typescript

```typescript
function minDamage(power: number, damage: number[], health: number[]): number {
    const n = damage.length;
    const enemies: { t: number; d: number }[] = new Array(n);
    for (let i = 0; i < n; i++) {
        const t = Math.ceil(health[i] / power);
        enemies[i] = { t, d: damage[i] };
    }
    enemies.sort((a, b) => a.t * b.d - b.t * a.d);
    let cur = 0;
    let total = 0;
    for (const e of enemies) {
        cur += e.t;
        total += e.d * cur;
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $power
     * @param Integer[] $damage
     * @param Integer[] $health
     * @return Integer
     */
    function minDamage($power, $damage, $health) {
        $n = count($damage);
        $enemies = [];
        for ($i = 0; $i < $n; ++$i) {
            $ti = intdiv($health[$i] + $power - 1, $power); // hits needed
            $enemies[] = [$ti, $damage[$i]];
        }

        usort($enemies, function ($a, $b) {
            // compare a.ti / a.di with b.ti / b.di using cross multiplication
            $left  = $a[0] * $b[1];
            $right = $b[0] * $a[1];
            if ($left == $right) return 0;
            return ($left < $right) ? -1 : 1;
        });

        $curTime = 0;
        $totalDamage = 0;
        foreach ($enemies as $e) {
            $ti = $e[0];
            $di = $e[1];
            $curTime += $ti;               // completion time of this enemy
            $totalDamage += $di * $curTime;
        }

        return $totalDamage;
    }
}
```

## Swift

```swift
class Solution {
    func minDamage(_ power: Int, _ damage: [Int], _ health: [Int]) -> Int {
        let n = damage.count
        var enemies = [(t: Int, d: Int)]()
        enemies.reserveCapacity(n)
        for i in 0..<n {
            let t = (health[i] + power - 1) / power
            enemies.append((t, damage[i]))
        }
        enemies.sort { a, b in
            let left = Int64(a.t) * Int64(b.d)
            let right = Int64(b.t) * Int64(a.d)
            if left == right {
                return a.d > b.d
            }
            return left < right
        }
        var cur: Int64 = 0
        var total: Int64 = 0
        for e in enemies {
            cur += Int64(e.t)
            total += cur * Int64(e.d)
        }
        return Int(total)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minDamage(power: Int, damage: IntArray, health: IntArray): Long {
        data class Enemy(val dmg: Int, val need: Long)
        val n = damage.size
        val list = ArrayList<Enemy>(n)
        for (i in 0 until n) {
            val need = ((health[i] + power - 1) / power).toLong()
            list.add(Enemy(damage[i], need))
        }
        list.sortWith(compareByDescending<Enemy> { it.dmg })
        var cur = 0L
        var ans = 0L
        for (e in list) {
            cur += e.need
            ans += e.dmg.toLong() * cur
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minDamage(int power, List<int> damage, List<int> health) {
    int n = damage.length;
    List<List<int>> enemies = List.generate(n, (i) {
      int t = (health[i] + power - 1) ~/ power; // attacks needed
      return [damage[i], t];
    });

    enemies.sort((a, b) {
      // Sort by descending damage / time ratio: a before b if a.d * b.t > b.d * a.t
      int left = b[0] * a[1];
      int right = a[0] * b[1];
      return left - right;
    });

    int curTime = 0;
    int totalDamage = 0;
    for (var e in enemies) {
      curTime += e[1];
      totalDamage += e[0] * curTime;
    }
    return totalDamage;
  }
}
```

## Golang

```go
import "sort"

func minDamage(power int, damage []int, health []int) int64 {
	type enemy struct {
		d int
		t int64
	}
	n := len(damage)
	enemies := make([]enemy, n)
	for i := 0; i < n; i++ {
		hits := (health[i] + power - 1) / power
		enemies[i] = enemy{d: damage[i], t: int64(hits)}
	}
	sort.Slice(enemies, func(i, j int) bool {
		left := int64(enemies[i].d) * enemies[j].t
		right := int64(enemies[j].d) * enemies[i].t
		if left == right {
			return enemies[i].d > enemies[j].d
		}
		return left > right
	})
	var cum, ans int64
	for _, e := range enemies {
		cum += e.t
		ans += int64(e.d) * cum
	}
	return ans
}
```

## Ruby

```ruby
def min_damage(power, damage, health)
  n = damage.length
  enemies = Array.new(n) do |i|
    pi = (health[i] + power - 1) / power
    [pi, damage[i]]
  end

  enemies.sort! do |a, b|
    lhs = a[0] * b[1]
    rhs = b[0] * a[1]
    if lhs == rhs
      0
    else
      lhs <=> rhs
    end
  end

  total = 0
  time = 0
  enemies.each do |pi, di|
    time += pi
    total += di * time
  end
  total
end
```

## Scala

```scala
object Solution {
  def minDamage(power: Int, damage: Array[Int], health: Array[Int]): Long = {
    val n = damage.length
    val enemies = new Array[(Long, Long)](n)
    var i = 0
    while (i < n) {
      val t = (health(i).toLong + power - 1L) / power.toLong
      enemies(i) = (t, damage(i).toLong)
      i += 1
    }
    java.util.Arrays.sort(enemies, new java.util.Comparator[(Long, Long)] {
      def compare(a: (Long, Long), b: (Long, Long)): Int = {
        val left = a._1 * b._2
        val right = b._1 * a._2
        if (left < right) -1 else if (left > right) 1 else 0
      }
    })
    var cur: Long = 0L
    var ans: Long = 0L
    i = 0
    while (i < n) {
      val t = enemies(i)._1
      val d = enemies(i)._2
      cur += t
      ans += d * cur
      i += 1
    }
    ans
  }
}
```

## Rust

```rust
impl Solution {
    pub fn min_damage(power: i32, damage: Vec<i32>, health: Vec<i32>) -> i64 {
        let n = damage.len();
        let mut jobs: Vec<(i64, i64)> = Vec::with_capacity(n);
        for i in 0..n {
            let t = (health[i] as i64 + power as i64 - 1) / power as i64;
            jobs.push((t, damage[i] as i64));
        }
        jobs.sort_by(|a, b| {
            let left = a.0 * b.1;
            let right = b.0 * a.1;
            if left < right {
                std::cmp::Ordering::Less
            } else if left > right {
                std::cmp::Ordering::Greater
            } else {
                std::cmp::Ordering::Equal
            }
        });
        let mut cur_time: i64 = 0;
        let mut total_damage: i64 = 0;
        for (t, d) in jobs {
            cur_time += t;
            total_damage += d * cur_time;
        }
        total_damage
    }
}
```

## Racket

```racket
(define/contract (min-damage power damage health)
  (-> exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((pairs
          (map (lambda (h d)
                 (cons (quotient (+ h (- power 1)) power) ; ceil(h / power)
                       d))
               health damage))
         (sorted
          (sort pairs
                (lambda (a b)
                  (< (* (car a) (cdr b))
                     (* (car b) (cdr a)))))))
    (let loop ((lst sorted) (time 0) (ans 0))
      (if (null? lst)
          ans
          (let* ((ti (car (car lst)))
                 (di (cdr (car lst)))
                 (new-time (+ time ti))
                 (new-ans (+ ans (* di new-time))))
            (loop (cdr lst) new-time new-ans))))))
```

## Erlang

```erlang
-spec min_damage(Power :: integer(), Damage :: [integer()], Health :: [integer()]) -> integer().
min_damage(Power, Damage, Health) ->
    Enemies = lists:zipwith(
        fun(H, D) ->
            Ki = (H + Power - 1) div Power,
            {Ki, D}
        end,
        Health,
        Damage),
    Sorted = lists:sort(
        fun({K1, D1}, {K2, D2}) ->
            K1 * D2 < K2 * D1
        end,
        Enemies),
    {Total, _} = lists:foldl(
        fun({Ki, Di}, {AccTot, AccTime}) ->
            NewTime = AccTime + Ki,
            NewTot = AccTot + Di * NewTime,
            {NewTot, NewTime}
        end,
        {0, 0},
        Sorted),
    Total.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_damage(power :: integer, damage :: [integer], health :: [integer]) :: integer
  def min_damage(power, damage, health) do
    enemies =
      Enum.zip(damage, health)
      |> Enum.map(fn {d, h} ->
        t = div(h + power - 1, power)
        {d, t}
      end)

    sorted =
      Enum.sort(enemies, fn {d1, t1}, {d2, t2} ->
        d1 * t2 > d2 * t1
      end)

    {_cum, total} =
      Enum.reduce(sorted, {0, 0}, fn {d, t}, {cum, tot} ->
        new_cum = cum + t
        new_tot = tot + d * new_cum
        {new_cum, new_tot}
      end)

    total
  end
end
```
