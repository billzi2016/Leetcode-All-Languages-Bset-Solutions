# 2998. Minimum Number of Operations to Make X and Y Equal

## Cpp

```cpp
class Solution {
public:
    int minimumOperationsToMakeEqual(int x, int y) {
        if (x == y) return 0;
        if (y >= x) return y - x; // only increments needed
        
        int U = x + (x - y); // upper bound as per hint
        int maxVal = max(U, y) + 5;
        vector<int> dist(maxVal + 1, -1);
        queue<int> q;
        auto push = [&](int v, int d){
            if (v < 1 || v > maxVal) return;
            if (dist[v] != -1) return;
            dist[v] = d;
            q.push(v);
        };
        
        dist[x] = 0;
        q.push(x);
        while (!q.empty()) {
            int cur = q.front(); q.pop();
            int dcur = dist[cur];
            if (cur == y) return dcur;
            
            // increment
            push(cur + 1, dcur + 1);
            // decrement
            push(cur - 1, dcur + 1);
            // division by any divisor >1
            for (int i = 2; i * i <= cur; ++i) {
                if (cur % i == 0) {
                    int nxt1 = cur / i;
                    push(nxt1, dcur + 1);
                    int d2 = cur / i;
                    if (d2 > 1) {
                        int nxt2 = cur / d2; // which equals i
                        push(nxt2, dcur + 1);
                    }
                }
            }
            // also divisor equal to cur itself gives result 1
            if (cur > 1) {
                push(1, dcur + 1);
            }
        }
        return x - y; // fallback, though BFS should find answer
    }
};
```

## Java

```java
class Solution {
    public int minimumOperationsToMakeEqual(int x, int y) {
        if (y >= x) return y - x;
        int upper = 2 * x - y; // U = x + (x - y)
        int[] dist = new int[upper + 2];
        for (int i = 0; i < dist.length; i++) dist[i] = -1;
        java.util.ArrayDeque<Integer> q = new java.util.ArrayDeque<>();
        dist[x] = 0;
        q.add(x);
        while (!q.isEmpty()) {
            int v = q.poll();
            if (v == y) return dist[v];
            int nd = dist[v] + 1;
            // increment
            if (v + 1 <= upper && dist[v + 1] == -1) {
                dist[v + 1] = nd;
                q.add(v + 1);
            }
            // decrement
            if (v - 1 >= 1 && dist[v - 1] == -1) {
                dist[v - 1] = nd;
                q.add(v - 1);
            }
            // division by any divisor > 1
            if (v > 1) {
                // divide to get 1 directly (by divisor v)
                if (dist[1] == -1) {
                    dist[1] = nd;
                    q.add(1);
                }
                for (int d = 2; d * d <= v; ++d) {
                    if (v % d == 0) {
                        int n1 = v / d; // result of dividing by d
                        if (n1 >= 1 && n1 <= upper && dist[n1] == -1) {
                            dist[n1] = nd;
                            q.add(n1);
                        }
                        int n2 = d; // result of dividing by v/d
                        if (n2 >= 1 && n2 <= upper && dist[n2] == -1) {
                            dist[n2] = nd;
                            q.add(n2);
                        }
                    }
                }
            }
        }
        return x - y; // fallback, should not reach here
    }
}
```

## Python

```python
class Solution(object):
    def minimumOperationsToMakeEqual(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if y >= x:
            return y - x

        # Upper bound for BFS search space
        max_val = x + (x - y)

        from collections import deque
        q = deque()
        q.append((x, 0))
        visited = set([x])

        while q:
            cur, steps = q.popleft()
            if cur == y:
                return steps

            # operation: increment
            nxt = cur + 1
            if nxt <= max_val and nxt not in visited:
                visited.add(nxt)
                q.append((nxt, steps + 1))

            # operation: decrement
            nxt = cur - 1
            if nxt >= 1 and nxt not in visited:
                visited.add(nxt)
                q.append((nxt, steps + 1))

            # operation: divide by any proper divisor >1
            limit = int(cur ** 0.5) + 1
            for d in range(2, limit):
                if cur % d == 0:
                    div = cur // d
                    # divisor d
                    if d != cur and d not in visited:
                        visited.add(d)
                        q.append((d, steps + 1))
                    # counterpart divisor cur//d
                    if div != cur and div not in visited:
                        visited.add(div)
                        q.append((div, steps + 1))

        return x - y  # fallback, should never reach here
```

## Python3

```python
class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if y >= x:
            return y - x

        # Upper bound for values we need to consider
        max_val = x + (x - y)

        from collections import deque
        q = deque()
        q.append((x, 0))
        visited = [False] * (max_val + 2)  # index up to max_val+1 safely
        visited[x] = True

        while q:
            cur, steps = q.popleft()
            if cur == y:
                return steps

            # operation: increment
            nxt = cur + 1
            if nxt <= max_val and not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, steps + 1))

            # operation: decrement
            nxt = cur - 1
            if nxt >= 1 and not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, steps + 1))

            # operation: divide by any divisor > 1
            v = cur
            d = 2
            while d * d <= v:
                if v % d == 0:
                    # divisor d
                    nxt = v // d
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.append((nxt, steps + 1))
                    # paired divisor v//d (if different)
                    other = v // d
                    if other != d:
                        nxt2 = v // other  # which is d
                        if not visited[nxt2]:
                            visited[nxt2] = True
                            q.append((nxt2, steps + 1))
                d += 1
            # also divisor equal to v (gives 1)
            if v > 1 and not visited[1]:
                visited[1] = True
                q.append((1, steps + 1))

        return x - y  # fallback, though BFS should have found answer
```

## C

```c
#include <bits/stdc++.h>
using namespace std;

int minimumOperationsToMakeEqual(int x, int y) {
    if (y >= x) return y - x;
    int limit = x + (x - y);               // upper bound for BFS
    vector<int> dist(limit + 2, -1);
    queue<int> q;
    dist[x] = 0;
    q.push(x);
    while (!q.empty()) {
        int cur = q.front(); q.pop();
        if (cur == y) return dist[cur];
        int ndist = dist[cur] + 1;

        // increment
        if (cur + 1 <= limit && dist[cur + 1] == -1) {
            dist[cur + 1] = ndist;
            q.push(cur + 1);
        }
        // decrement
        if (cur - 1 >= 1 && dist[cur - 1] == -1) {
            dist[cur - 1] = ndist;
            q.push(cur - 1);
        }

        if (cur > 1) {
            // division by cur -> 1
            if (dist[1] == -1) {
                dist[1] = ndist;
                q.push(1);
            }
            for (int i = 2; i * i <= cur; ++i) {
                if (cur % i == 0) {
                    int div1 = i;          // divisor
                    int div2 = cur / i;    // counterpart divisor

                    int nxt1 = cur / div1; // quotient when dividing by div1
                    if (nxt1 <= limit && dist[nxt1] == -1) {
                        dist[nxt1] = ndist;
                        q.push(nxt1);
                    }
                    int nxt2 = cur / div2; // quotient when dividing by div2 (equals i)
                    if (nxt2 <= limit && dist[nxt2] == -1) {
                        dist[nxt2] = ndist;
                        q.push(nxt2);
                    }
                }
            }
        }
    }
    return -1; // should never reach here
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumOperationsToMakeEqual(int x, int y) {
        if (y >= x) return y - x;

        int maxVal = x + (x - y); // upper bound for BFS
        int[] dist = new int[maxVal + 1];
        for (int i = 0; i <= maxVal; i++) dist[i] = -1;

        Queue<int> q = new Queue<int>();
        dist[x] = 0;
        q.Enqueue(x);

        while (q.Count > 0) {
            int cur = q.Dequeue();
            if (cur == y) return dist[cur];
            int nextDist = dist[cur] + 1;

            // increment
            if (cur + 1 <= maxVal && dist[cur + 1] == -1) {
                dist[cur + 1] = nextDist;
                q.Enqueue(cur + 1);
            }
            // decrement
            if (cur - 1 >= 1 && dist[cur - 1] == -1) {
                dist[cur - 1] = nextDist;
                q.Enqueue(cur - 1);
            }

            // division operations
            if (cur > 1) {
                // divide by cur -> 1
                if (dist[1] == -1) {
                    dist[1] = nextDist;
                    q.Enqueue(1);
                }
                for (int i = 2; i * i <= cur; i++) {
                    if (cur % i == 0) {
                        int d1 = i;
                        int nxt1 = cur / d1;
                        if (nxt1 >= 1 && nxt1 <= maxVal && dist[nxt1] == -1) {
                            dist[nxt1] = nextDist;
                            q.Enqueue(nxt1);
                        }

                        int d2 = cur / i;
                        if (d2 != d1) {
                            int nxt2 = cur / d2; // equals i
                            if (nxt2 >= 1 && nxt2 <= maxVal && dist[nxt2] == -1) {
                                dist[nxt2] = nextDist;
                                q.Enqueue(nxt2);
                            }
                        }
                    }
                }
            }
        }

        return -1; // should never reach here
    }
}
```

## Javascript

```javascript
/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var minimumOperationsToMakeEqual = function(x, y) {
    if (y >= x) return y - x; // only increments needed
    
    const U = x + (x - y); // upper bound for BFS
    const maxVal = Math.max(U, y) + 2;
    const visited = new Uint8Array(maxVal);
    const dist = new Int32Array(maxVal);
    
    const queue = new Array(maxVal);
    let head = 0, tail = 0;
    
    queue[tail++] = x;
    visited[x] = 1;
    dist[x] = 0;
    
    while (head < tail) {
        const cur = queue[head++];
        const dcur = dist[cur];
        if (cur === y) return dcur;
        
        // increment
        if (cur + 1 < maxVal && !visited[cur + 1]) {
            visited[cur + 1] = 1;
            dist[cur + 1] = dcur + 1;
            queue[tail++] = cur + 1;
        }
        // decrement
        if (cur - 1 >= 1 && !visited[cur - 1]) {
            visited[cur - 1] = 1;
            dist[cur - 1] = dcur + 1;
            queue[tail++] = cur - 1;
        }
        // division by any divisor >1
        for (let d = 2; d * d <= cur; ++d) {
            if (cur % d === 0) {
                const q = cur / d;
                if (!visited[q]) {
                    visited[q] = 1;
                    dist[q] = dcur + 1;
                    queue[tail++] = q;
                }
                // also consider divisor itself as divisor for division? operation is divide by divisor, not replace with divisor.
                // So we only need the quotient.
            }
        }
    }
    
    // fallback (should never reach here)
    return x - y;
};
```

## Typescript

```typescript
function minimumOperationsToMakeEqual(x: number, y: number): number {
    if (y >= x) return y - x;

    const maxVal = x + (x - y);
    const limit = Math.max(maxVal, y);
    const visited = new Uint8Array(limit + 2);

    const q: number[] = [];
    const dist: number[] = [];
    let head = 0;

    q.push(x);
    dist.push(0);
    visited[x] = 1;

    while (head < q.length) {
        const cur = q[head];
        const d = dist[head];
        head++;

        if (cur === y) return d;

        // decrement
        if (cur - 1 >= 1 && !visited[cur - 1]) {
            visited[cur - 1] = 1;
            q.push(cur - 1);
            dist.push(d + 1);
        }

        // increment
        if (cur + 1 <= limit && !visited[cur + 1]) {
            visited[cur + 1] = 1;
            q.push(cur + 1);
            dist.push(d + 1);
        }

        // direct division to 1
        if (cur > 1 && !visited[1]) {
            visited[1] = 1;
            q.push(1);
            dist.push(d + 1);
        }

        // divide by any divisor > 1
        const sqrt = Math.floor(Math.sqrt(cur));
        for (let i = 2; i <= sqrt; ++i) {
            if (cur % i === 0) {
                const nxt1 = cur / i;
                if (!visited[nxt1]) {
                    visited[nxt1] = 1;
                    q.push(nxt1);
                    dist.push(d + 1);
                }
                // the counterpart divisor gives quotient i
                if (!visited[i]) {
                    visited[i] = 1;
                    q.push(i);
                    dist.push(d + 1);
                }
            }
        }
    }

    // Fallback (should not reach here)
    return x - y;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $x
     * @param Integer $y
     * @return Integer
     */
    function minimumOperationsToMakeEqual($x, $y) {
        if ($x == $y) return 0;
        if ($y > $x) {
            // only increments are useful
            return $y - $x;
        }

        // y < x : use BFS with an upper bound
        $U = $x + ($x - $y); // safe upper limit
        if ($U < 1) $U = 1;

        $dist = array_fill(0, $U + 1, -1);
        $queue = new SplQueue();

        $dist[$x] = 0;
        $queue->enqueue($x);

        while (!$queue->isEmpty()) {
            $cur = $queue->dequeue();
            $dcur = $dist[$cur];
            if ($cur == $y) return $dcur;

            // increment
            if ($cur + 1 <= $U && $dist[$cur + 1] == -1) {
                $dist[$cur + 1] = $dcur + 1;
                $queue->enqueue($cur + 1);
            }
            // decrement
            if ($cur - 1 >= 1 && $dist[$cur - 1] == -1) {
                $dist[$cur - 1] = $dcur + 1;
                $queue->enqueue($cur - 1);
            }

            // division by any divisor > 1
            // include division by itself -> result 1
            if ($cur > 1 && $dist[1] == -1) {
                $dist[1] = $dcur + 1;
                $queue->enqueue(1);
            }
            for ($d = 2; $d * $d <= $cur; $d++) {
                if ($cur % $d == 0) {
                    // divisor d
                    $next = intdiv($cur, $d);
                    if ($next >= 1 && $next <= $U && $dist[$next] == -1) {
                        $dist[$next] = $dcur + 1;
                        $queue->enqueue($next);
                    }
                    // paired divisor cur / d
                    $paired = $d; // since dividing by (cur/d) yields d
                    if ($paired >= 1 && $paired <= $U && $dist[$paired] == -1) {
                        $dist[$paired] = $dcur + 1;
                        $queue->enqueue($paired);
                    }
                }
            }
        }

        // fallback, should never reach here because direct decrement is always possible
        return $x - $y;
    }
}
```

## Swift

```swift
class Solution {
    func minimumOperationsToMakeEqual(_ x: Int, _ y: Int) -> Int {
        if y >= x { return y - x }
        let limit = x + (x - y)
        var visited = [Bool](repeating: false, count: limit + 2)
        var dist = [Int](repeating: 0, count: limit + 2)
        var queue = [Int]()
        var head = 0
        queue.append(x)
        visited[x] = true
        
        while head < queue.count {
            let cur = queue[head]
            head += 1
            if cur == y { return dist[cur] }
            let nd = dist[cur] + 1
            
            // increment
            if cur + 1 <= limit && !visited[cur + 1] {
                visited[cur + 1] = true
                dist[cur + 1] = nd
                queue.append(cur + 1)
            }
            // decrement
            if cur - 1 >= 1 && !visited[cur - 1] {
                visited[cur - 1] = true
                dist[cur - 1] = nd
                queue.append(cur - 1)
            }
            // division operations
            if cur > 1 {
                // divide by itself -> 1
                if !visited[1] {
                    visited[1] = true
                    dist[1] = nd
                    queue.append(1)
                }
                var i = 2
                while i * i <= cur {
                    if cur % i == 0 {
                        let res1 = cur / i   // divide by i
                        if !visited[res1] {
                            visited[res1] = true
                            dist[res1] = nd
                            queue.append(res1)
                        }
                        let res2 = i          // divide by (cur/i)
                        if !visited[res2] {
                            visited[res2] = true
                            dist[res2] = nd
                            queue.append(res2)
                        }
                    }
                    i += 1
                }
            }
        }
        return x - y
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumOperationsToMakeEqual(x: Int, y: Int): Int {
        if (y >= x) return y - x

        val maxVal = x + (x - y)
        val limit = maxOf(maxVal, y)

        val visited = BooleanArray(limit + 2)
        val dist = IntArray(limit + 2) { -1 }
        val queue: ArrayDeque<Int> = ArrayDeque()

        visited[x] = true
        dist[x] = 0
        queue.add(x)

        while (queue.isNotEmpty()) {
            val cur = queue.removeFirst()
            if (cur == y) return dist[cur]

            // increment
            var nxt = cur + 1
            if (nxt <= limit && !visited[nxt]) {
                visited[nxt] = true
                dist[nxt] = dist[cur] + 1
                queue.add(nxt)
            }

            // decrement
            nxt = cur - 1
            if (nxt >= 1 && !visited[nxt]) {
                visited[nxt] = true
                dist[nxt] = dist[cur] + 1
                queue.add(nxt)
            }

            // division by any divisor > 1
            var d = 2
            while (d * d <= cur) {
                if (cur % d == 0) {
                    val divResult = cur / d
                    if (!visited[divResult]) {
                        visited[divResult] = true
                        dist[divResult] = dist[cur] + 1
                        queue.add(divResult)
                    }
                    // also the counterpart divisor
                    if (!visited[d]) {
                        visited[d] = true
                        dist[d] = dist[cur] + 1
                        queue.add(d)
                    }
                }
                d++
            }
        }

        // Fallback (should not reach here)
        return x - y
    }
}
```

## Dart

```dart
class Solution {
  int minimumOperationsToMakeEqual(int x, int y) {
    if (y >= x) return y - x;

    int upper = x + (x - y);
    List<int> dist = List.filled(upper + 1, -1);
    List<int> queue = [];
    int head = 0;

    queue.add(x);
    dist[x] = 0;

    while (head < queue.length) {
      int cur = queue[head++];
      int steps = dist[cur];
      if (cur == y) return steps;

      // decrement
      if (cur - 1 >= 1 && dist[cur - 1] == -1) {
        dist[cur - 1] = steps + 1;
        queue.add(cur - 1);
      }
      // increment within bound
      if (cur + 1 <= upper && dist[cur + 1] == -1) {
        dist[cur + 1] = steps + 1;
        queue.add(cur + 1);
      }

      // division by any divisor > 1
      Set<int> divisors = {};
      for (int d = 2; d * d <= cur; ++d) {
        if (cur % d == 0) {
          divisors.add(d);
          divisors.add(cur ~/ d);
        }
      }
      // also division by itself to get 1
      if (cur > 1) divisors.add(cur);

      for (int div in divisors) {
        int nxt = cur ~/ div;
        if (dist[nxt] == -1) {
          dist[nxt] = steps + 1;
          queue.add(nxt);
        }
      }
    }

    // Fallback, should never reach here because decrement path always works
    return x - y;
  }
}
```

## Golang

```go
func minimumOperationsToMakeEqual(x int, y int) int {
	if x == y {
		return 0
	}
	if y > x {
		return y - x
	}

	maxVal := x + (x - y)
	visited := make([]bool, maxVal+2)

	type pair struct {
		val   int
		steps int
	}
	queue := []pair{{x, 0}}
	visited[x] = true

	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]

		if cur.val == y {
			return cur.steps
		}

		// increment
		if cur.val+1 <= maxVal && !visited[cur.val+1] {
			visited[cur.val+1] = true
			queue = append(queue, pair{cur.val + 1, cur.steps + 1})
		}
		// decrement
		if cur.val-1 >= 1 && !visited[cur.val-1] {
			visited[cur.val-1] = true
			queue = append(queue, pair{cur.val - 1, cur.steps + 1})
		}
		// divisions by any divisor > 1
		v := cur.val
		if v > 1 && !visited[1] {
			visited[1] = true
			queue = append(queue, pair{1, cur.steps + 1})
		}
		for d := 2; d*d <= v; d++ {
			if v%d == 0 {
				nd := v / d // result of dividing by d
				if !visited[nd] {
					visited[nd] = true
					queue = append(queue, pair{nd, cur.steps + 1})
				}
				other := d // result of dividing by (v/d)
				if !visited[other] {
					visited[other] = true
					queue = append(queue, pair{other, cur.steps + 1})
				}
			}
		}
	}

	// Fallback (should not reach here)
	return x - y
}
```

## Ruby

```ruby
def minimum_operations_to_make_equal(x, y)
  return y - x if y >= x

  upper = 2 * x - y
  max_val = upper
  dist = Array.new(max_val + 1, -1)

  queue = []
  front = 0
  dist[x] = 0
  queue << x

  while front < queue.size
    cur = queue[front]
    front += 1
    dcur = dist[cur]

    return dcur if cur == y

    # increment
    inc = cur + 1
    if inc <= max_val && dist[inc] == -1
      dist[inc] = dcur + 1
      queue << inc
    end

    # decrement
    dec = cur - 1
    if dec >= 1 && dist[dec] == -1
      dist[dec] = dcur + 1
      queue << dec
    end

    # division by proper divisors (>1 and <cur)
    if cur > 1
      limit = Math.sqrt(cur).to_i
      i = 2
      while i <= limit
        if cur % i == 0
          res1 = cur / i   # divisor i
          if dist[res1] == -1
            dist[res1] = dcur + 1
            queue << res1
          end

          res2 = i         # divisor cur/i
          if dist[res2] == -1
            dist[res2] = dcur + 1
            queue << res2
          end
        end
        i += 1
      end
    end
  end

  x - y
end
```

## Scala

```scala
object Solution {
    def minimumOperationsToMakeEqual(x: Int, y: Int): Int = {
        if (y >= x) return y - x

        val maxU = x + (x - y)
        val limit = maxU
        val visited = Array.fill(limit + 1)(-1)
        import scala.collection.mutable.ArrayDeque
        val q = new ArrayDeque[Int]()
        visited(x) = 0
        q.append(x)

        while (q.nonEmpty) {
            val cur = q.removeHead()
            val steps = visited(cur)
            if (cur == y) return steps

            // increment
            if (cur + 1 <= limit && visited(cur + 1) == -1) {
                visited(cur + 1) = steps + 1
                q.append(cur + 1)
            }
            // decrement
            if (cur - 1 >= 1 && visited(cur - 1) == -1) {
                visited(cur - 1) = steps + 1
                q.append(cur - 1)
            }

            // division by any divisor > 1
            var d = 2
            while (d * d <= cur) {
                if (cur % d == 0) {
                    val nxt1 = cur / d
                    if (visited(nxt1) == -1) {
                        visited(nxt1) = steps + 1
                        q.append(nxt1)
                    }
                    val otherDiv = cur / d
                    if (otherDiv != d) {
                        // dividing by otherDiv gives result d
                        if (visited(d) == -1) {
                            visited(d) = steps + 1
                            q.append(d)
                        }
                    }
                }
                d += 1
            }
            // divisor equal to cur -> result 1
            if (cur > 1 && visited(1) == -1) {
                visited(1) = steps + 1
                q.append(1)
            }
        }

        // Should never reach here
        x - y
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_operations_to_make_equal(x: i32, y: i32) -> i32 {
        if y >= x {
            return y - x;
        }
        // Upper bound for values we need to consider
        let max_limit = (x + (x - y)) as usize;
        let mut visited = vec![false; max_limit + 2];
        use std::collections::VecDeque;
        let mut q: VecDeque<(i32, i32)> = VecDeque::new();
        q.push_back((x, 0));
        visited[x as usize] = true;

        while let Some((v, d)) = q.pop_front() {
            if v == y {
                return d;
            }
            // increment
            if (v + 1) as usize <= max_limit && !visited[(v + 1) as usize] {
                visited[(v + 1) as usize] = true;
                q.push_back((v + 1, d + 1));
            }
            // decrement
            if v - 1 >= 1 && !visited[(v - 1) as usize] {
                visited[(v - 1) as usize] = true;
                q.push_back((v - 1, d + 1));
            }
            // division by any divisor > 1 (including itself)
            let mut i = 2i32;
            while i * i <= v {
                if v % i == 0 {
                    let div1 = i;
                    let nxt1 = v / div1;
                    if !visited[nxt1 as usize] {
                        visited[nxt1 as usize] = true;
                        q.push_back((nxt1, d + 1));
                    }
                    let div2 = v / i;
                    if div2 != div1 {
                        let nxt2 = v / div2; // which equals i
                        if !visited[nxt2 as usize] {
                            visited[nxt2 as usize] = true;
                            q.push_back((nxt2, d + 1));
                        }
                    }
                }
                i += 1;
            }
            // divisor equal to v -> result is 1
            if v != 1 && !visited[1] {
                visited[1] = true;
                q.push_back((1, d + 1));
            }
        }
        // Fallback (should not reach here)
        x - y
    }
}
```

## Racket

```racket
(define/contract (minimum-operations-to-make-equal x y)
  (-> exact-integer? exact-integer? exact-integer?)
  (cond [(= x y) 0]
        [(>= y x) (- y x)]
        [else
         (let* ([U (+ x (- x y))]                ; upper bound = 2*x - y
                [max-val U]
                [dist (make-vector (add1 max-val) -1)]
                [queue (make-vector (+ 1 max-val) 0)])
           (vector-set! dist x 0)
           (vector-set! queue 0 x)
           (let loop ((head 0) (tail 1))
             (if (= head tail)
                 -1
                 (let* ([v (vector-ref queue head)]
                        [d (vector-ref dist v)])
                   (if (= v y)
                       d
                       (begin
                         (define (try-add n)
                           (when (and (>= n 1) (<= n max-val)
                                      (= (vector-ref dist n) -1))
                             (vector-set! dist n (+ d 1))
                             (vector-set! queue tail n)
                             (set! tail (+ tail 1))))
                         ;; increment
                         (try-add (+ v 1))
                         ;; decrement
                         (try-add (- v 1))
                         ;; division neighbors
                         (let ([limit (inexact->exact (floor (sqrt v)))])
                           (for ([i (in-range 2 (add1 limit))])
                             (when (= (remainder v i) 0)
                               (define q1 (quotient v i))
                               (try-add q1)
                               (when (not (= i q1))
                                 (try-add i)))))
                         (loop (+ head 1) tail))))))])))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_operations_to_make_equal/2]).

-spec minimum_operations_to_make_equal(X :: integer(), Y :: integer()) -> integer().
minimum_operations_to_make_equal(X, Y) when Y >= X ->
    Y - X;
minimum_operations_to_make_equal(X, Y) ->
    Limit = X + (X - Y),
    bfs(queue:from_list([{X, 0}]), #{X => true}, Limit, Y).

bfs(Queue, Visited, Limit, Target) ->
    case queue:out(Queue) of
        {empty, _} ->
            % Should never happen with given constraints
            -1;
        {{value, {Val, Dist}}, RestQueue} ->
            if Val =:= Target ->
                    Dist;
               true ->
                    NextVals = next_states(Val, Limit),
                    {NewQueue, NewVisited} =
                        lists:foldl(
                            fun(N, {QAcc, VAcc}) ->
                                case maps:is_key(N, VAcc) of
                                    true -> {QAcc, VAcc};
                                    false ->
                                        {queue:in({N, Dist + 1}, QAcc), maps:put(N, true, VAcc)}
                                end
                            end,
                            {RestQueue, Visited},
                            NextVals),
                    bfs(NewQueue, NewVisited, Limit, Target)
            end
    end.

next_states(V, Limit) ->
    Inc = if V + 1 =< Limit -> [V + 1]; true -> [] end,
    Dec = if V - 1 >= 1 -> [V - 1]; true -> [] end,
    Div = division_results(V),
    Inc ++ Dec ++ Div.

division_results(V) ->
    % always can divide by itself to get 1
    Base = [1],
    MaxI = trunc(math:sqrt(V)),
    lists:foldl(
        fun(I, Acc) ->
            if I * I > V -> Acc;
               true ->
                    if V rem I =:= 0 ->
                            Q1 = V div I,
                            Q2 = I,
                            [Q1, Q2 | Acc];
                       true -> Acc
                    end
            end
        end,
        Base,
        lists:seq(2, MaxI)
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_operations_to_make_equal(x :: integer, y :: integer) :: integer
  def minimum_operations_to_make_equal(x, y) when y >= x do
    y - x
  end

  def minimum_operations_to_make_equal(x, y) do
    limit = x + (x - y)
    start_queue = :queue.in({x, 0}, :queue.new())
    visited = :maps.put(x, true, :maps.new())
    bfs(start_queue, visited, y, limit)
  end

  defp bfs(queue, visited, target, limit) do
    case :queue.out(queue) do
      {:empty, _} ->
        -1

      {{:value, {cur, dist}}, q} ->
        if cur == target do
          dist
        else
          next_dist = dist + 1

          {q1, v1} = enqueue_if_valid(cur + 1, next_dist, limit, q, visited)
          {q2, v2} = enqueue_if_valid(cur - 1, next_dist, limit, q1, v1)

          {q3, v3} =
            if cur > 1 do
              # division by itself gives 1
              {q_tmp, v_tmp} = enqueue_if_valid(1, next_dist, limit, q2, v2)
              max = :math.sqrt(cur) |> trunc()

              Enum.reduce(2..max, {q_tmp, v_tmp}, fn i, {qq, vv} ->
                if rem(cur, i) == 0 do
                  nx1 = div(cur, i)
                  {qq1, vv1} = enqueue_if_valid(nx1, next_dist, limit, qq, vv)

                  nx2 = i
                  enqueue_if_valid(nx2, next_dist, limit, qq1, vv1)
                else
                  {qq, vv}
                end
              end)
            else
              {q2, v2}
            end

          bfs(q3, v3, target, limit)
        end
    end
  end

  defp enqueue_if_valid(nx, dist, limit, queue, visited) do
    if nx >= 1 and nx <= limit and not :maps.is_key(nx, visited) do
      {:queue.in({nx, dist}, queue), :maps.put(nx, true, visited)}
    else
      {queue, visited}
    end
  end
end
```
