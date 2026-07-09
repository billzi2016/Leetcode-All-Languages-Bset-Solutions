# 2976. Minimum Cost to Convert String I

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long minimumCost(string source, string target, vector<char>& original, vector<char>& changed, vector<int>& cost) {
        const long long INF = (1LL << 60);
        long long dist[26][26];
        for (int i = 0; i < 26; ++i)
            for (int j = 0; j < 26; ++j)
                dist[i][j] = (i == j) ? 0 : INF;

        int m = original.size();
        for (int i = 0; i < m; ++i) {
            int u = original[i] - 'a';
            int v = changed[i] - 'a';
            long long c = cost[i];
            if (c < dist[u][v]) dist[u][v] = c;
        }

        for (int k = 0; k < 26; ++k)
            for (int i = 0; i < 26; ++i) {
                if (dist[i][k] == INF) continue;
                for (int j = 0; j < 26; ++j) {
                    if (dist[k][j] == INF) continue;
                    long long nd = dist[i][k] + dist[k][j];
                    if (nd < dist[i][j]) dist[i][j] = nd;
                }
            }

        long long total = 0;
        int n = source.size();
        for (int i = 0; i < n; ++i) {
            char a = source[i], b = target[i];
            if (a == b) continue;
            long long d = dist[a - 'a'][b - 'a'];
            if (d == INF) return -1;
            total += d;
        }
        return total;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public long minimumCost(String source, String target, char[] original, char[] changed, int[] cost) {
        final long INF = Long.MAX_VALUE / 4;
        long[][] dist = new long[26][26];
        for (int i = 0; i < 26; i++) {
            Arrays.fill(dist[i], INF);
            dist[i][i] = 0;
        }
        int m = original.length;
        for (int i = 0; i < m; i++) {
            int u = original[i] - 'a';
            int v = changed[i] - 'a';
            long c = cost[i];
            if (c < dist[u][v]) {
                dist[u][v] = c;
            }
        }
        for (int k = 0; k < 26; k++) {
            for (int i = 0; i < 26; i++) {
                if (dist[i][k] == INF) continue;
                for (int j = 0; j < 26; j++) {
                    if (dist[k][j] == INF) continue;
                    long nd = dist[i][k] + dist[k][j];
                    if (nd < dist[i][j]) {
                        dist[i][j] = nd;
                    }
                }
            }
        }
        long total = 0;
        int n = source.length();
        for (int i = 0; i < n; i++) {
            char sc = source.charAt(i);
            char tc = target.charAt(i);
            if (sc == tc) continue;
            int u = sc - 'a';
            int v = tc - 'a';
            long d = dist[u][v];
            if (d == INF) return -1;
            total += d;
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        INF = 10**15
        # initialize distance matrix
        dist = [[INF] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0

        # set direct conversion costs (keep minimum if multiple edges)
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - 97
            v = ord(c) - 97
            if w < dist[u][v]:
                dist[u][v] = w

        # Floyd-Warshall to compute all-pairs shortest paths
        for k in range(26):
            dk = dist[k]
            for i in range(26):
                dik = dist[i][k]
                if dik == INF:
                    continue
                di = dist[i]
                nd = dik + 0  # placeholder for readability
                for j in range(26):
                    new_cost = dik + dk[j]
                    if new_cost < di[j]:
                        di[j] = new_cost

        total = 0
        for sc, tc in zip(source, target):
            if sc == tc:
                continue
            u = ord(sc) - 97
            v = ord(tc) - 97
            d = dist[u][v]
            if d >= INF:
                return -1
            total += d
        return total
```

## Python3

```python
from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = 10**15
        # Initialize distance matrix for 26 letters
        dist = [[INF] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0

        # Set direct conversion costs (keep minimal if multiple edges)
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - 97
            v = ord(c) - 97
            if w < dist[u][v]:
                dist[u][v] = w

        # Floyd-Warshall to compute all-pairs shortest paths
        for k in range(26):
            dk = dist[k]
            for i in range(26):
                dik = dist[i][k]
                if dik == INF:
                    continue
                di = dist[i]
                for j in range(26):
                    nd = dik + dk[j]
                    if nd < di[j]:
                        di[j] = nd

        total = 0
        for s_char, t_char in zip(source, target):
            if s_char == t_char:
                continue
            u = ord(s_char) - 97
            v = ord(t_char) - 97
            d = dist[u][v]
            if d >= INF:
                return -1
            total += d

        return total
```

## C

```c
#include <limits.h>
#include <string.h>

long long minimumCost(char* source, char* target, char* original, int originalSize,
                      char* changed, int changedSize, int* cost, int costSize) {
    const long long INF = (1LL<<60);
    long long dist[26][26];
    
    for (int i = 0; i < 26; ++i)
        for (int j = 0; j < 26; ++j)
            dist[i][j] = (i == j) ? 0 : INF;
    
    for (int i = 0; i < originalSize; ++i) {
        int u = original[i] - 'a';
        int v = changed[i] - 'a';
        long long c = cost[i];
        if (c < dist[u][v]) dist[u][v] = c;
    }
    
    for (int k = 0; k < 26; ++k)
        for (int i = 0; i < 26; ++i)
            if (dist[i][k] != INF)
                for (int j = 0; j < 26; ++j)
                    if (dist[k][j] != INF && dist[i][k] + dist[k][j] < dist[i][j])
                        dist[i][j] = dist[i][k] + dist[k][j];
    
    long long total = 0;
    size_t n = strlen(source);
    for (size_t idx = 0; idx < n; ++idx) {
        char a = source[idx];
        char b = target[idx];
        if (a == b) continue;
        int u = a - 'a';
        int v = b - 'a';
        if (dist[u][v] == INF) return -1;
        total += dist[u][v];
    }
    return total;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public long MinimumCost(string source, string target, char[] original, char[] changed, int[] cost) {
        const long INF = long.MaxValue / 4;
        long[,] dist = new long[26, 26];
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < 26; j++) {
                dist[i, j] = (i == j) ? 0 : INF;
            }
        }

        int m = original.Length;
        for (int i = 0; i < m; i++) {
            int u = original[i] - 'a';
            int v = changed[i] - 'a';
            long c = cost[i];
            if (c < dist[u, v]) dist[u, v] = c;
        }

        for (int k = 0; k < 26; k++) {
            for (int i = 0; i < 26; i++) {
                if (dist[i, k] == INF) continue;
                for (int j = 0; j < 26; j++) {
                    if (dist[k, j] == INF) continue;
                    long nd = dist[i, k] + dist[k, j];
                    if (nd < dist[i, j]) dist[i, j] = nd;
                }
            }
        }

        long total = 0;
        int n = source.Length;
        for (int i = 0; i < n; i++) {
            int s = source[i] - 'a';
            int t = target[i] - 'a';
            if (s == t) continue;
            long d = dist[s, t];
            if (d == INF) return -1;
            total += d;
        }
        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} source
 * @param {string} target
 * @param {character[]} original
 * @param {character[]} changed
 * @param {number[]} cost
 * @return {number}
 */
var minimumCost = function(source, target, original, changed, cost) {
    const N = 26;
    const INF = 1e18; // sufficiently large
    
    // Initialize distance matrix
    const dist = Array.from({ length: N }, () => Array(N).fill(INF));
    for (let i = 0; i < N; i++) dist[i][i] = 0;
    
    // Direct conversion edges, keep minimal cost if multiple edges exist
    for (let i = 0; i < original.length; i++) {
        const u = original[i].charCodeAt(0) - 97;
        const v = changed[i].charCodeAt(0) - 97;
        if (cost[i] < dist[u][v]) dist[u][v] = cost[i];
    }
    
    // Floyd‑Warshall to compute all‑pairs shortest paths
    for (let k = 0; k < N; k++) {
        for (let i = 0; i < N; i++) {
            if (dist[i][k] === INF) continue;
            const ik = dist[i][k];
            for (let j = 0; j < N; j++) {
                if (dist[k][j] === INF) continue;
                const nd = ik + dist[k][j];
                if (nd < dist[i][j]) dist[i][j] = nd;
            }
        }
    }
    
    // Accumulate total minimal cost for each position
    let total = 0;
    for (let i = 0; i < source.length; i++) {
        const s = source.charCodeAt(i) - 97;
        const t = target.charCodeAt(i) - 97;
        if (s === t) continue;
        const d = dist[s][t];
        if (d === INF) return -1;
        total += d;
    }
    
    return total;
};
```

## Typescript

```typescript
function minimumCost(source: string, target: string, original: string[], changed: string[], cost: number[]): number {
    const INF = Number.MAX_SAFE_INTEGER;
    const N = 26;
    const dist: number[][] = Array.from({ length: N }, () => Array(N).fill(INF));
    for (let i = 0; i < N; i++) dist[i][i] = 0;

    for (let i = 0; i < original.length; i++) {
        const u = original[i].charCodeAt(0) - 97;
        const v = changed[i].charCodeAt(0) - 97;
        if (cost[i] < dist[u][v]) dist[u][v] = cost[i];
    }

    for (let k = 0; k < N; k++) {
        for (let i = 0; i < N; i++) {
            if (dist[i][k] === INF) continue;
            const ik = dist[i][k];
            for (let j = 0; j < N; j++) {
                if (dist[k][j] === INF) continue;
                const nd = ik + dist[k][j];
                if (nd < dist[i][j]) dist[i][j] = nd;
            }
        }
    }

    let total = 0;
    for (let i = 0; i < source.length; i++) {
        const s = source.charCodeAt(i) - 97;
        const t = target.charCodeAt(i) - 97;
        if (s === t) continue;
        const d = dist[s][t];
        if (d === INF) return -1;
        total += d;
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param String $source
     * @param String $target
     * @param String[] $original
     * @param String[] $changed
     * @param Integer[] $cost
     * @return Integer
     */
    function minimumCost($source, $target, $original, $changed, $cost) {
        $INF = 10**15; // sufficiently large
        
        // Initialize distance matrix
        $dist = array_fill(0, 26, array_fill(0, 26, $INF));
        for ($i = 0; $i < 26; $i++) {
            $dist[$i][$i] = 0;
        }
        
        $m = count($original);
        for ($i = 0; $i < $m; $i++) {
            $u = ord($original[$i]) - 97;
            $v = ord($changed[$i]) - 97;
            $c = $cost[$i];
            if ($c < $dist[$u][$v]) {
                $dist[$u][$v] = $c;
            }
        }
        
        // Floyd-Warshall
        for ($k = 0; $k < 26; $k++) {
            for ($i = 0; $i < 26; $i++) {
                if ($dist[$i][$k] == $INF) continue;
                for ($j = 0; $j < 26; $j++) {
                    if ($dist[$k][$j] == $INF) continue;
                    $new = $dist[$i][$k] + $dist[$k][$j];
                    if ($new < $dist[$i][$j]) {
                        $dist[$i][$j] = $new;
                    }
                }
            }
        }
        
        $len = strlen($source);
        $total = 0;
        for ($idx = 0; $idx < $len; $idx++) {
            $sChar = $source[$idx];
            $tChar = $target[$idx];
            if ($sChar === $tChar) continue;
            $u = ord($sChar) - 97;
            $v = ord($tChar) - 97;
            $d = $dist[$u][$v];
            if ($d == $INF) {
                return -1;
            }
            $total += $d;
        }
        
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func minimumCost(_ source: String, _ target: String, _ original: [Character], _ changed: [Character], _ cost: [Int]) -> Int {
        let INF = Int.max / 4
        var dist = Array(repeating: Array(repeating: INF, count: 26), count: 26)
        for i in 0..<26 { dist[i][i] = 0 }
        
        for (o, c, w) in zip(zip(original, changed), cost) {
            let u = Int(o.0.asciiValue! - Character("a").asciiValue!)
            let v = Int(o.1.asciiValue! - Character("a").asciiValue!)
            if w < dist[u][v] {
                dist[u][v] = w
            }
        }
        
        for k in 0..<26 {
            for i in 0..<26 where dist[i][k] < INF {
                let ik = dist[i][k]
                for j in 0..<26 where dist[k][j] < INF {
                    let nd = ik + dist[k][j]
                    if nd < dist[i][j] {
                        dist[i][j] = nd
                    }
                }
            }
        }
        
        let sChars = Array(source)
        let tChars = Array(target)
        var total = 0
        for idx in 0..<sChars.count {
            let sc = sChars[idx]
            let tc = tChars[idx]
            if sc == tc { continue }
            let u = Int(sc.asciiValue! - Character("a").asciiValue!)
            let v = Int(tc.asciiValue! - Character("a").asciiValue!)
            let d = dist[u][v]
            if d >= INF {
                return -1
            }
            total += d
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumCost(source: String, target: String, original: CharArray, changed: CharArray, cost: IntArray): Long {
        val INF = Long.MAX_VALUE / 4
        val sz = 26
        val dist = Array(sz) { LongArray(sz) { INF } }
        for (i in 0 until sz) dist[i][i] = 0L

        for (i in original.indices) {
            val u = original[i] - 'a'
            val v = changed[i] - 'a'
            val c = cost[i].toLong()
            if (c < dist[u][v]) dist[u][v] = c
        }

        for (k in 0 until sz) {
            for (i in 0 until sz) {
                val ik = dist[i][k]
                if (ik == INF) continue
                for (j in 0 until sz) {
                    val kj = dist[k][j]
                    if (kj == INF) continue
                    val nd = ik + kj
                    if (nd < dist[i][j]) dist[i][j] = nd
                }
            }
        }

        var total = 0L
        for (idx in source.indices) {
            val s = source[idx]
            val t = target[idx]
            if (s == t) continue
            val d = dist[s - 'a'][t - 'a']
            if (d >= INF) return -1L
            total += d
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int minimumCost(String source, String target, List<String> original,
      List<String> changed, List<int> cost) {
    const int INF = 1 << 60;
    // Initialize distance matrix
    List<List<int>> dist =
        List.generate(26, (_) => List.filled(26, INF), growable: false);
    for (int i = 0; i < 26; ++i) {
      dist[i][i] = 0;
    }

    // Direct conversion edges (keep minimal cost for duplicates)
    for (int i = 0; i < original.length; ++i) {
      int u = original[i].codeUnitAt(0) - 97;
      int v = changed[i].codeUnitAt(0) - 97;
      if (cost[i] < dist[u][v]) {
        dist[u][v] = cost[i];
      }
    }

    // Floyd‑Warshall to compute all‑pairs shortest paths
    for (int k = 0; k < 26; ++k) {
      for (int i = 0; i < 26; ++i) {
        if (dist[i][k] == INF) continue;
        for (int j = 0; j < 26; ++j) {
          if (dist[k][j] == INF) continue;
          int nd = dist[i][k] + dist[k][j];
          if (nd < dist[i][j]) {
            dist[i][j] = nd;
          }
        }
      }
    }

    // Accumulate total minimal cost
    int total = 0;
    for (int i = 0; i < source.length; ++i) {
      int sIdx = source.codeUnitAt(i) - 97;
      int tIdx = target.codeUnitAt(i) - 97;
      if (sIdx == tIdx) continue;
      int d = dist[sIdx][tIdx];
      if (d >= INF) return -1;
      total += d;
    }
    return total;
  }
}
```

## Golang

```go
func minimumCost(source string, target string, original []byte, changed []byte, cost []int) int64 {
	const INF int64 = 1<<60 - 1

	// distance matrix
	var dist [26][26]int64
	for i := 0; i < 26; i++ {
		for j := 0; j < 26; j++ {
			if i == j {
				dist[i][j] = 0
			} else {
				dist[i][j] = INF
			}
		}
	}

	// initialize edges with minimal cost
	m := len(original)
	for i := 0; i < m; i++ {
		u := int(original[i] - 'a')
		v := int(changed[i] - 'a')
		w := int64(cost[i])
		if w < dist[u][v] {
			dist[u][v] = w
		}
	}

	// Floyd‑Warshall
	for k := 0; k < 26; k++ {
		for i := 0; i < 26; i++ {
			if dist[i][k] == INF {
				continue
			}
			for j := 0; j < 26; j++ {
				if dist[k][j] == INF {
					continue
				}
				if nd := dist[i][k] + dist[k][j]; nd < dist[i][j] {
					dist[i][j] = nd
				}
			}
		}
	}

	var total int64 = 0
	n := len(source)
	for i := 0; i < n; i++ {
		s := int(source[i] - 'a')
		t := int(target[i] - 'a')
		if s == t {
			continue
		}
		if dist[s][t] == INF {
			return -1
		}
		total += dist[s][t]
	}
	return total
}
```

## Ruby

```ruby
def minimum_cost(source, target, original, changed, cost)
  n = source.length
  inf = (1 << 60)

  dist = Array.new(26) { Array.new(26, inf) }
  26.times { |i| dist[i][i] = 0 }

  m = original.length
  m.times do |i|
    u = original[i].ord - 97
    v = changed[i].ord - 97
    c = cost[i]
    dist[u][v] = c if c < dist[u][v]
  end

  26.times do |k|
    26.times do |i|
      next if dist[i][k] == inf
      26.times do |j|
        nd = dist[i][k] + dist[k][j]
        dist[i][j] = nd if nd < dist[i][j]
      end
    end
  end

  total = 0
  n.times do |idx|
    s = source[idx].ord - 97
    t = target[idx].ord - 97
    next if s == t
    d = dist[s][t]
    return -1 if d == inf
    total += d
  end

  total
end
```

## Scala

```scala
object Solution {
  def minimumCost(source: String, target: String, original: Array[Char], changed: Array[Char], cost: Array[Int]): Long = {
    val N = 26
    val INF = Long.MaxValue / 4
    val dist = Array.ofDim[Long](N, N)

    var i = 0
    while (i < N) {
      var j = 0
      while (j < N) {
        if (i == j) dist(i)(j) = 0L else dist(i)(j) = INF
        j += 1
      }
      i += 1
    }

    val m = original.length
    var idx = 0
    while (idx < m) {
      val u = original(idx) - 'a'
      val v = changed(idx) - 'a'
      val c = cost(idx).toLong
      if (c < dist(u)(v)) dist(u)(v) = c
      idx += 1
    }

    var k = 0
    while (k < N) {
      var i2 = 0
      while (i2 < N) {
        if (dist(i2)(k) != INF) {
          var j2 = 0
          while (j2 < N) {
            if (dist(k)(j2) != INF) {
              val via = dist(i2)(k) + dist(k)(j2)
              if (via < dist(i2)(j2)) dist(i2)(j2) = via
            }
            j2 += 1
          }
        }
        i2 += 1
      }
      k += 1
    }

    var total: Long = 0L
    val len = source.length
    var pos = 0
    while (pos < len) {
      val s = source.charAt(pos) - 'a'
      val t = target.charAt(pos) - 'a'
      if (s != t) {
        val d = dist(s)(t)
        if (d == INF) return -1L
        total += d
      }
      pos += 1
    }

    total
  }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_cost(
        source: String,
        target: String,
        original: Vec<char>,
        changed: Vec<char>,
        cost: Vec<i32>,
    ) -> i64 {
        const INF: i64 = i64::MAX / 4;
        let mut dist = [[INF; 26]; 26];
        for i in 0..26 {
            dist[i][i] = 0;
        }
        for i in 0..original.len() {
            let u = (original[i] as u8 - b'a') as usize;
            let v = (changed[i] as u8 - b'a') as usize;
            let w = cost[i] as i64;
            if w < dist[u][v] {
                dist[u][v] = w;
            }
        }

        for k in 0..26 {
            for i in 0..26 {
                if dist[i][k] == INF {
                    continue;
                }
                for j in 0..26 {
                    if dist[k][j] == INF {
                        continue;
                    }
                    let nd = dist[i][k] + dist[k][j];
                    if nd < dist[i][j] {
                        dist[i][j] = nd;
                    }
                }
            }
        }

        let s_bytes = source.as_bytes();
        let t_bytes = target.as_bytes();
        let mut total: i64 = 0;
        for idx in 0..s_bytes.len() {
            let a = (s_bytes[idx] - b'a') as usize;
            let b = (t_bytes[idx] - b'a') as usize;
            if a == b {
                continue;
            }
            let d = dist[a][b];
            if d >= INF / 2 {
                return -1;
            }
            total += d;
        }
        total
    }
}
```

## Racket

```racket
(define/contract (minimum-cost source target original changed cost)
  (-> string? string? (listof char?) (listof char?) (listof exact-integer?) exact-integer?)
  (let* ((n (string-length source))
         (INF (expt 2 60))
         (dist (make-vector 26)))
    ;; initialize distance matrix
    (for ([i 0 26])
      (define row (make-vector 26 INF))
      (vector-set! dist i row)
      (vector-set! row i 0))
    ;; set direct conversion costs (keep minimum if multiple edges)
    (for ([o original] [c changed] [w cost])
      (let* ((oi (- (char->integer o) (char->integer #\a)))
             (ci (- (char->integer c) (char->integer #\a))))
        (when (< w (vector-ref (vector-ref dist oi) ci))
          (vector-set! (vector-ref dist oi) ci w))))
    ;; Floyd‑Warshall all‑pairs shortest paths
    (for ([k 0 26])
      (for ([i 0 26])
        (let ((dik (vector-ref (vector-ref dist i) k)))
          (when (< dik INF)
            (for ([j 0 26])
              (let* ((dkj (vector-ref (vector-ref dist k) j))
                     (new (+ dik dkj)))
                (when (< new (vector-ref (vector-ref dist i) j))
                  (vector-set! (vector-ref dist i) j new))))))))
    ;; compute total minimal cost
    (let loop ((idx 0) (total 0))
      (if (= idx n)
          total
          (let* ((sc (string-ref source idx))
                 (tc (string-ref target idx)))
            (if (char=? sc tc)
                (loop (+ idx 1) total)
                (let* ((si (- (char->integer sc) (char->integer #\a)))
                       (ti (- (char->integer tc) (char->integer #\a)))
                       (cst (vector-ref (vector-ref dist si) ti)))
                  (if (>= cst INF)
                      -1
                      (loop (+ idx 1) (+ total cst))))))))))
```

## Erlang

```erlang
-module(solution).
-export([minimum_cost/5]).

-define(INF, 1000000000000000).

-spec minimum_cost(Source :: unicode:unicode_binary(),
                   Target :: unicode:unicode_binary(),
                   Original :: [char()], Changed :: [char()],
                   Cost :: [integer()]) -> integer().
minimum_cost(Source, Target, Original, Changed, Cost) ->
    Inf = ?INF,
    InitPairs = [{ {I,J},
                  if I == J -> 0; true -> Inf end}
                || I <- lists:seq(0,25), J <- lists:seq(0,25)],
    Map0 = maps:from_list(InitPairs),
    EdgeMap = add_edges(Original, Changed, Cost, Map0),
    FinalMap = floyd_warshall(EdgeMap, Inf),
    compute_total(binary:bin_to_list(Source), binary:bin_to_list(Target), FinalMap, Inf).

add_edges([], [], [], Map) -> Map;
add_edges([O|Os], [C|Cs], [W|Ws], Map) ->
    IdxO = O - $a,
    IdxC = C - $a,
    Key = {IdxO,IdxC},
    Prev = maps:get(Key, Map),
    NewCost = if W < Prev -> W; true -> Prev end,
    add_edges(Os, Cs, Ws, maps:put(Key, NewCost, Map)).

floyd_warshall(Map, _Inf) ->
    lists:foldl(fun(K, M1) ->
        lists:foldl(fun(I, M2) ->
            lists:foldl(fun(J, M3) ->
                D_ik = maps:get({I,K}, M3),
                D_kj = maps:get({K,J}, M3),
                D_ij = maps:get({I,J}, M3),
                New = D_ik + D_kj,
                if New < D_ij -> maps:put({I,J}, New, M3); true -> M3 end
            end, M2, lists:seq(0,25))
        end, M1, lists:seq(0,25))
    end, Map, lists:seq(0,25)).

compute_total([], [], _Map, _Inf) -> 0;
compute_total([S|Ss], [T|Ts], Map, Inf) ->
    if S =:= T ->
            compute_total(Ss, Ts, Map, Inf);
       true ->
            IdxS = S - $a,
            IdxT = T - $a,
            Cost = maps:get({IdxS,IdxT}, Map),
            if Cost >= Inf -> -1;
               true ->
                    Rest = compute_total(Ss, Ts, Map, Inf),
                    if Rest == -1 -> -1; true -> Rest + Cost end
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @inf 1_000_000_000

  @spec minimum_cost(String.t(), String.t(), [char()], [char()], [integer()]) :: integer()
  def minimum_cost(source, target, original, changed, cost) do
    # build initial distance matrix
    dist0 =
      for i <- 0..25 do
        for j <- 0..25 do
          if i == j, do: 0, else: @inf
        end
      end

    dist1 =
      Enum.zip([original, changed, cost])
      |> Enum.reduce(dist0, fn {o, c, w}, acc ->
        oi = idx(o)
        ci = idx(c)

        put_min(acc, oi, ci, w)
      end)

    # Floyd‑Warshall
    dist =
      Enum.reduce(0..25, dist1, fn k, d_k ->
        Enum.reduce(0..25, d_k, fn i, d_i ->
          dik = get(d_i, i, k)

          Enum.reduce(0..25, d_i, fn j, d_j ->
            dkj = get(d_j, k, j)
            dij = get(d_j, i, j)

            if dik < @inf and dkj < @inf and dik + dkj < dij do
              put(d_j, i, j, dik + dkj)
            else
              d_j
            end
          end)
        end)
      end)

    # compute total cost
    src = :binary.bin_to_list(source)
    tgt = :binary.bin_to_list(target)

    Enum.zip(src, tgt)
    |> Enum.reduce_while(0, fn {s, t}, acc ->
      if s == t do
        {:cont, acc}
      else
        si = s - ?a
        ti = t - ?a
        cst = get(dist, si, ti)

        if cst >= @inf do
          {:halt, -1}
        else
          {:cont, acc + cst}
        end
      end
    end)
  end

  # helpers ---------------------------------------------------------

  defp idx(c) when is_integer(c), do: c - ?a
  defp idx(<<ch>>), do: ch - ?a

  defp get(matrix, i, j) do
    row = Enum.at(matrix, i)
    Enum.at(row, j)
  end

  defp put(matrix, i, j, val) do
    row = Enum.at(matrix, i)
    new_row = List.replace_at(row, j, val)
    List.replace_at(matrix, i, new_row)
  end

  defp put_min(matrix, i, j, val) do
    current = get(matrix, i, j)

    if val < current do
      put(matrix, i, j, val)
    else
      matrix
    end
  end
end
```
