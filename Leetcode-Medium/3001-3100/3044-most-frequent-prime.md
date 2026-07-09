# 3044. Most Frequent Prime

## Cpp

```cpp
class Solution {
public:
    bool isPrime(int n) {
        if (n < 2) return false;
        if (n % 2 == 0) return n == 2;
        for (int i = 3; i * 1LL * i <= n; i += 2)
            if (n % i == 0) return false;
        return true;
    }
    
    int mostFrequentPrime(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        unordered_map<int,int> freq;
        const vector<pair<int,int>> dirs = {{-1,-1},{-1,0},{-1,1},
                                            {0,-1},{0,1},
                                            {1,-1},{1,0},{1,1}};
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int start = mat[i][j];
                for (auto [dx, dy] : dirs) {
                    long long num = start;
                    int x = i + dx, y = j + dy;
                    while (x >= 0 && x < m && y >= 0 && y < n) {
                        num = num * 10 + mat[x][y];
                        if (num > 10 && isPrime((int)num))
                            ++freq[(int)num];
                        x += dx;
                        y += dy;
                    }
                }
            }
        }
        int best = -1, bestCnt = 0;
        for (auto &p : freq) {
            if (p.second > bestCnt || (p.second == bestCnt && p.first > best)) {
                bestCnt = p.second;
                best = p.first;
            }
        }
        return bestCnt ? best : -1;
    }
};
```

## Java

```java
class Solution {
    public int mostFrequentPrime(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        // 8 directions
        int[] dx = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dy = {-1, 0, 1, -1, 1, -1, 0, 1};

        java.util.Map<Integer, Integer> freq = new java.util.HashMap<>();

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int start = mat[i][j];
                for (int dir = 0; dir < 8; ++dir) {
                    int x = i + dx[dir];
                    int y = j + dy[dir];
                    long num = start;
                    while (x >= 0 && x < m && y >= 0 && y < n) {
                        num = num * 10 + mat[x][y];
                        if (num > 10 && isPrime((int) num)) {
                            int val = (int) num;
                            freq.put(val, freq.getOrDefault(val, 0) + 1);
                        }
                        x += dx[dir];
                        y += dy[dir];
                    }
                }
            }
        }

        if (freq.isEmpty()) return -1;

        int bestPrime = -1;
        int bestCount = 0;
        for (java.util.Map.Entry<Integer, Integer> e : freq.entrySet()) {
            int prime = e.getKey();
            int cnt = e.getValue();
            if (cnt > bestCount || (cnt == bestCount && prime > bestPrime)) {
                bestCount = cnt;
                bestPrime = prime;
            }
        }
        return bestPrime;
    }

    private boolean isPrime(int x) {
        if (x < 2) return false;
        if (x % 2 == 0) return x == 2;
        for (int i = 3; i * i <= x; i += 2) {
            if (x % i == 0) return false;
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def mostFrequentPrime(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        dirs = [(-1,-1), (-1,0), (-1,1),
                (0,-1),          (0,1),
                (1,-1),  (1,0),  (1,1)]
        
        def is_prime(x):
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True
        
        freq = {}
        for i in range(m):
            for j in range(n):
                start_digit = mat[i][j]
                for dx, dy in dirs:
                    num = start_digit
                    x, y = i + dx, j + dy
                    while 0 <= x < m and 0 <= y < n:
                        num = num * 10 + mat[x][y]
                        if num > 10 and is_prime(num):
                            freq[num] = freq.get(num, 0) + 1
                        x += dx
                        y += dy
        
        if not freq:
            return -1
        max_count = max(freq.values())
        candidates = [p for p, c in freq.items() if c == max_count]
        return max(candidates)
```

## Python3

```python
import sys
from typing import List
from collections import defaultdict

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        # sieve up to 999999 (6 digits max)
        limit = 1000000
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(limit ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False

        dirs = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),           (0, 1),
                (1, -1),  (1, 0),  (1, 1)]

        freq = defaultdict(int)

        for i in range(m):
            for j in range(n):
                for dx, dy in dirs:
                    x, y = i, j
                    num = 0
                    while 0 <= x < m and 0 <= y < n:
                        num = num * 10 + mat[x][y]
                        if num > 10 and is_prime[num]:
                            freq[num] += 1
                        x += dx
                        y += dy

        if not freq:
            return -1

        max_cnt = max(freq.values())
        candidates = [num for num, cnt in freq.items() if cnt == max_cnt]
        return max(candidates)
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <math.h>

static int isPrime(int x) {
    if (x < 2) return 0;
    if (x % 2 == 0) return x == 2;
    for (int i = 3; i * i <= x; i += 2)
        if (x % i == 0) return 0;
    return 1;
}

int mostFrequentPrime(int** mat, int matSize, int* matColSize) {
    int m = matSize;
    int n = matColSize[0];
    const int MAXV = 1000000;               // 6 digits max (999999)
    int *freq = (int *)calloc(MAXV + 1, sizeof(int));
    if (!freq) return -1;

    int dirs[8][2] = {
        {-1, -1}, {-1, 0}, {-1, 1},
        {0, -1},          {0, 1},
        {1, -1},  {1, 0}, {1, 1}
    };

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            int startDigit = mat[i][j];
            for (int d = 0; d < 8; ++d) {
                int x = i, y = j;
                long num = startDigit;
                while (1) {
                    x += dirs[d][0];
                    y += dirs[d][1];
                    if (x < 0 || x >= m || y < 0 || y >= n) break;
                    num = num * 10 + mat[x][y];
                    if (num > 10 && isPrime((int)num)) {
                        freq[(int)num] += 1;
                    }
                }
            }
        }
    }

    int bestFreq = 0;
    int answer = -1;
    for (int v = 11; v <= MAXV; ++v) {   // primes are >10
        if (freq[v] > 0) {
            if (freq[v] > bestFreq || (freq[v] == bestFreq && v > answer)) {
                bestFreq = freq[v];
                answer = v;
            }
        }
    }

    free(freq);
    return answer;
}
```

## Csharp

```csharp
public class Solution
{
    public int MostFrequentPrime(int[][] mat)
    {
        int m = mat.Length;
        int n = mat[0].Length;
        int[] dx = new int[] { -1, -1, -1, 0, 0, 1, 1, 1 };
        int[] dy = new int[] { -1, 0, 1, -1, 1, -1, 0, 1 };

        var freq = new Dictionary<int, int>();

        bool IsPrime(int x)
        {
            if (x < 2) return false;
            if (x % 2 == 0) return x == 2;
            for (int i = 3; i * i <= x; i += 2)
                if (x % i == 0) return false;
            return true;
        }

        for (int i = 0; i < m; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                foreach (var dir in System.Linq.Enumerable.Range(0, 8))
                {
                    int x = i, y = j;
                    int num = mat[x][y];
                    int len = 1;

                    while (true)
                    {
                        x += dx[dir];
                        y += dy[dir];
                        if (x < 0 || x >= m || y < 0 || y >= n) break;

                        num = num * 10 + mat[x][y];
                        ++len;
                        if (len >= 2 && num > 10 && IsPrime(num))
                        {
                            if (freq.ContainsKey(num)) freq[num]++; else freq[num] = 1;
                        }
                    }
                }
            }
        }

        int best = -1;
        int bestCount = 0;
        foreach (var kvp in freq)
        {
            int val = kvp.Key, cnt = kvp.Value;
            if (cnt > bestCount || (cnt == bestCount && val > best))
            {
                bestCount = cnt;
                best = val;
            }
        }

        return best;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} mat
 * @return {number}
 */
var mostFrequentPrime = function(mat) {
    const m = mat.length;
    const n = mat[0].length;
    const dirs = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1],          [0, 1],
        [1, -1],  [1, 0], [1, 1]
    ];
    const freq = new Map();
    const isPrime = (num) => {
        if (num < 2) return false;
        if (num % 2 === 0) return num === 2;
        for (let i = 3; i * i <= num; i += 2) {
            if (num % i === 0) return false;
        }
        return true;
    };
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            const start = mat[i][j];
            for (const [dx, dy] of dirs) {
                let x = i + dx, y = j + dy;
                let num = start;
                while (x >= 0 && x < m && y >= 0 && y < n) {
                    num = num * 10 + mat[x][y];
                    if (num > 10 && isPrime(num)) {
                        freq.set(num, (freq.get(num) || 0) + 1);
                    }
                    x += dx;
                    y += dy;
                }
            }
        }
    }
    let best = -1, bestCnt = 0;
    for (const [prime, cnt] of freq.entries()) {
        if (cnt > bestCnt || (cnt === bestCnt && prime > best)) {
            bestCnt = cnt;
            best = prime;
        }
    }
    return best;
};
```

## Typescript

```typescript
function mostFrequentPrime(mat: number[][]): number {
    const m = mat.length;
    const n = mat[0].length;
    const dirs = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1],           [0, 1],
        [1, -1],  [1, 0],  [1, 1]
    ];
    
    const isPrime = (num: number): boolean => {
        if (num < 2) return false;
        if (num % 2 === 0) return num === 2;
        for (let i = 3; i * i <= num; i += 2) {
            if (num % i === 0) return false;
        }
        return true;
    };
    
    const freq = new Map<number, number>();
    
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            for (const [dx, dy] of dirs) {
                let x = i;
                let y = j;
                let num = 0;
                let steps = 0;
                while (x >= 0 && x < m && y >= 0 && y < n) {
                    num = num * 10 + mat[x][y];
                    if (steps >= 1) { // length at least 2
                        if (num > 10 && isPrime(num)) {
                            freq.set(num, (freq.get(num) ?? 0) + 1);
                        }
                    }
                    x += dx;
                    y += dy;
                    steps++;
                }
            }
        }
    }
    
    let best = -1;
    let bestCnt = 0;
    for (const [val, cnt] of freq.entries()) {
        if (cnt > bestCnt || (cnt === bestCnt && val > best)) {
            bestCnt = cnt;
            best = val;
        }
    }
    return best;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @return Integer
     */
    function mostFrequentPrime($mat) {
        $m = count($mat);
        $n = count($mat[0]);
        // 8 possible directions
        $dirs = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1],           [0, 1],
            [1, -1],  [1, 0],  [1, 1]
        ];
        $freq = [];

        // prime checking function
        $isPrime = function($num) {
            if ($num <= 1) return false;
            if ($num == 2) return true;
            if ($num % 2 == 0) return false;
            for ($i = 3; $i * $i <= $num; $i += 2) {
                if ($num % $i == 0) return false;
            }
            return true;
        };

        for ($i = 0; $i < $m; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                foreach ($dirs as $d) {
                    $dx = $d[0];
                    $dy = $d[1];
                    $x = $i;
                    $y = $j;
                    $num = $mat[$i][$j];
                    while (true) {
                        $x += $dx;
                        $y += $dy;
                        if ($x < 0 || $x >= $m || $y < 0 || $y >= $n) break;
                        $num = $num * 10 + $mat[$x][$y];
                        if ($num > 10 && $isPrime($num)) {
                            if (!isset($freq[$num])) $freq[$num] = 0;
                            $freq[$num]++;
                        }
                    }
                }
            }
        }

        if (empty($freq)) return -1;

        $bestPrime = -1;
        $bestCount = 0;
        foreach ($freq as $prime => $cnt) {
            if ($cnt > $bestCount || ($cnt == $bestCount && $prime > $bestPrime)) {
                $bestCount = $cnt;
                $bestPrime = $prime;
            }
        }

        return $bestPrime;
    }
}
```

## Swift

```swift
class Solution {
    func mostFrequentPrime(_ mat: [[Int]]) -> Int {
        let m = mat.count
        let n = mat[0].count
        let dirs = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1),           (0, 1),
                    (1, -1),  (1, 0),  (1, 1)]
        
        var freq = [Int: Int]()
        
        func isPrime(_ x: Int) -> Bool {
            if x < 2 { return false }
            if x % 2 == 0 { return x == 2 }
            var i = 3
            while i * i <= x {
                if x % i == 0 { return false }
                i += 2
            }
            return true
        }
        
        for i in 0..<m {
            for j in 0..<n {
                let startVal = mat[i][j]
                for (dx, dy) in dirs {
                    var x = i
                    var y = j
                    var value = startVal
                    while true {
                        x += dx
                        y += dy
                        if x < 0 || x >= m || y < 0 || y >= n { break }
                        value = value * 10 + mat[x][y]
                        if value > 10 && isPrime(value) {
                            freq[value, default: 0] += 1
                        }
                    }
                }
            }
        }
        
        var bestNum = -1
        var bestCnt = 0
        for (num, cnt) in freq {
            if cnt > bestCnt || (cnt == bestCnt && num > bestNum) {
                bestCnt = cnt
                bestNum = num
            }
        }
        return bestNum
    }
}
```

## Kotlin

```kotlin
class Solution {
    private fun isPrime(num: Int): Boolean {
        if (num < 2) return false
        if (num % 2 == 0) return num == 2
        var i = 3
        while (i * i <= num) {
            if (num % i == 0) return false
            i += 2
        }
        return true
    }

    fun mostFrequentPrime(mat: Array<IntArray>): Int {
        val m = mat.size
        val n = mat[0].size
        val dirs = arrayOf(
            intArrayOf(-1, -1), intArrayOf(-1, 0), intArrayOf(-1, 1),
            intArrayOf(0, -1),                 intArrayOf(0, 1),
            intArrayOf(1, -1), intArrayOf(1, 0), intArrayOf(1, 1)
        )
        val freq = HashMap<Int, Int>()

        for (i in 0 until m) {
            for (j in 0 until n) {
                for (d in dirs) {
                    var x = i
                    var y = j
                    var num = mat[i][j]
                    while (true) {
                        x += d[0]
                        y += d[1]
                        if (x !in 0 until m || y !in 0 until n) break
                        num = num * 10 + mat[x][y]
                        if (num > 10 && isPrime(num)) {
                            freq[num] = (freq[num] ?: 0) + 1
                        }
                    }
                }
            }
        }

        var bestNum = -1
        var bestFreq = 0
        for ((k, v) in freq) {
            if (v > bestFreq || (v == bestFreq && k > bestNum)) {
                bestFreq = v
                bestNum = k
            }
        }
        return bestNum
    }
}
```

## Dart

```dart
class Solution {
  int mostFrequentPrime(List<List<int>> mat) {
    int m = mat.length;
    int n = mat[0].length;
    const List<List<int>> dirs = [
      [-1, -1],
      [-1, 0],
      [-1, 1],
      [0, -1],
      [0, 1],
      [1, -1],
      [1, 0],
      [1, 1]
    ];
    Map<int, int> freq = {};

    bool isPrime(int num) {
      if (num < 2) return false;
      if (num == 2 || num == 3) return true;
      if (num % 2 == 0 || num % 3 == 0) return false;
      for (int i = 5; i * i <= num; i += 6) {
        if (num % i == 0 || num % (i + 2) == 0) return false;
      }
      return true;
    }

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        for (var d in dirs) {
          int dx = d[0];
          int dy = d[1];
          int x = i;
          int y = j;
          int num = 0;
          int len = 0;
          while (x >= 0 && x < m && y >= 0 && y < n) {
            num = num * 10 + mat[x][y];
            ++len;
            if (len >= 2 && num > 10 && isPrime(num)) {
              freq[num] = (freq[num] ?? 0) + 1;
            }
            x += dx;
            y += dy;
          }
        }
      }
    }

    int bestPrime = -1;
    int bestCount = 0;
    freq.forEach((prime, count) {
      if (count > bestCount || (count == bestCount && prime > bestPrime)) {
        bestCount = count;
        bestPrime = prime;
      }
    });
    return bestPrime;
  }
}
```

## Golang

```go
func mostFrequentPrime(mat [][]int) int {
    rows := len(mat)
    cols := len(mat[0])
    dirs := [8][2]int{{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}}
    freq := make(map[int]int)

    isPrime := func(n int) bool {
        if n < 2 {
            return false
        }
        if n%2 == 0 {
            return n == 2
        }
        for i := 3; i*i <= n; i += 2 {
            if n%i == 0 {
                return false
            }
        }
        return true
    }

    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            for _, d := range dirs {
                x, y := i, j
                num := 0
                steps := 0
                for x >= 0 && x < rows && y >= 0 && y < cols {
                    num = num*10 + mat[x][y]
                    steps++
                    if steps >= 2 && num > 10 && isPrime(num) {
                        freq[num]++
                    }
                    x += d[0]
                    y += d[1]
                }
            }
        }
    }

    bestNum := -1
    bestCnt := 0
    for val, cnt := range freq {
        if cnt > bestCnt || (cnt == bestCnt && val > bestNum) {
            bestCnt = cnt
            bestNum = val
        }
    }
    return bestNum
}
```

## Ruby

```ruby
def most_frequent_prime(mat)
  m = mat.length
  n = mat[0].length
  max_len = [m, n].max
  limit = ('9' * max_len).to_i

  is_prime = Array.new(limit + 1, true)
  if limit >= 0
    is_prime[0] = false
    is_prime[1] = false if limit >= 1
  end
  p = 2
  while p * p <= limit
    if is_prime[p]
      (p * p).step(limit, p) { |i| is_prime[i] = false }
    end
    p += 1
  end

  freq = Hash.new(0)
  dirs = [-1, 0, 1].product([-1, 0, 1]) - [[0, 0]]

  m.times do |i|
    n.times do |j|
      start_digit = mat[i][j]
      dirs.each do |dx, dy|
        x = i
        y = j
        num = start_digit
        loop do
          x += dx
          y += dy
          break unless x.between?(0, m - 1) && y.between?(0, n - 1)
          num = num * 10 + mat[x][y]
          if num > 10 && is_prime[num]
            freq[num] += 1
          end
        end
      end
    end
  end

  return -1 if freq.empty?
  max_freq = freq.values.max
  freq.select { |k, v| v == max_freq }.keys.max
end
```

## Scala

```scala
object Solution {
    def mostFrequentPrime(mat: Array[Array[Int]]): Int = {
        val m = mat.length
        val n = mat(0).length
        val dirs = Array(
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1), (1, 0), (1, 1)
        )
        val freq = scala.collection.mutable.Map[Int, Int]().withDefaultValue(0)

        def isPrime(x: Int): Boolean = {
            if (x < 2) false
            else if (x % 2 == 0) x == 2
            else {
                var d = 3
                val limit = math.sqrt(x).toInt
                while (d <= limit) {
                    if (x % d == 0) return false
                    d += 2
                }
                true
            }
        }

        for (i <- 0 until m; j <- 0 until n) {
            for ((dx, dy) <- dirs) {
                var x = i
                var y = j
                var value = 0
                var steps = 0
                while (x >= 0 && x < m && y >= 0 && y < n) {
                    value = value * 10 + mat(x)(y)
                    if (steps >= 1 && value > 10 && isPrime(value)) {
                        freq(value) += 1
                    }
                    steps += 1
                    x += dx
                    y += dy
                }
            }
        }

        var bestNum = -1
        var bestCnt = 0
        for ((num, cnt) <- freq) {
            if (cnt > bestCnt || (cnt == bestCnt && num > bestNum)) {
                bestCnt = cnt
                bestNum = num
            }
        }
        if (bestCnt == 0) -1 else bestNum
    }
}
```

## Rust

```rust
use std::collections::HashMap;

fn is_prime(n: i32) -> bool {
    if n <= 1 {
        return false;
    }
    if n == 2 {
        return true;
    }
    if n % 2 == 0 {
        return false;
    }
    let mut d = 3;
    while d * d <= n {
        if n % d == 0 {
            return false;
        }
        d += 2;
    }
    true
}

impl Solution {
    pub fn most_frequent_prime(mat: Vec<Vec<i32>>) -> i32 {
        let m = mat.len();
        let n = mat[0].len();
        let dirs = [
            (-1i32, -1i32),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ];
        let mut freq: HashMap<i32, i32> = HashMap::new();

        for i in 0..m {
            for j in 0..n {
                let start = mat[i][j];
                for &(dx, dy) in &dirs {
                    let mut x = i as i32;
                    let mut y = j as i32;
                    let mut num = start;
                    loop {
                        x += dx;
                        y += dy;
                        if x < 0 || x >= m as i32 || y < 0 || y >= n as i32 {
                            break;
                        }
                        num = num * 10 + mat[x as usize][y as usize];
                        if num > 10 && is_prime(num) {
                            *freq.entry(num).or_insert(0) += 1;
                        }
                    }
                }
            }
        }

        let mut best_val = -1;
        let mut best_cnt = 0;
        for (val, cnt) in freq {
            if cnt > best_cnt || (cnt == best_cnt && val > best_val) {
                best_cnt = cnt;
                best_val = val;
            }
        }

        if best_cnt == 0 { -1 } else { best_val }
    }
}
```

## Racket

```racket
(define/contract (most-frequent-prime mat)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((rows (list->vector (map list->vector mat)))
         (m (vector-length rows))
         (n (if (= m 0) 0 (vector-length (vector-ref rows 0))))
         (dirs '((-1 0) (1 0) (0 -1) (0 1) (-1 -1) (-1 1) (1 -1) (1 1)))
         (freq (make-hash)))
    (define (in-bounds? x y)
      (and (>= x 0) (< x m) (>= y 0) (< y n)))
    (define (prime? num)
      (cond [(< num 2) #f]
            [(= num 2) #t]
            [(even? num) #f]
            [else
             (let loop ((d 3))
               (if (> (* d d) num)
                   #t
                   (if (= (remainder num d) 0)
                       #f
                       (loop (+ d 2)))))]))
    (for* ([i (in-range m)]
           [j (in-range n)])
      (let ((start (vector-ref (vector-ref rows i) j)))
        (for ([dir dirs])
          (define dx (first dir))
          (define dy (second dir))
          (let loop ((x (+ i dx)) (y (+ j dy)) (num start))
            (when (in-bounds? x y)
              (let ((new-num (+ (* num 10) (vector-ref (vector-ref rows x) y))))
                (when (> new-num 10)
                  (when (prime? new-num)
                    (hash-set! freq new-num (add1 (hash-ref freq new-num 0)))))
                (loop (+ x dx) (+ y dy) new-num)))))))
    (if (= (hash-count freq) 0)
        -1
        (let* ((maxcnt (apply max (hash-values freq)))
               (cands (for/list ([(k v) (in-hash freq)] #:when (= v maxcnt)) k))
               (ans (apply max cands)))
          ans))))
```

## Erlang

```erlang
-spec most_frequent_prime(Mat :: [[integer()]]) -> integer().
most_frequent_prime(Mat) ->
    M = length(Mat),
    N = length(hd(Mat)),
    Directions = [{-1,-1},{-1,0},{-1,1},
                  {0,-1},          {0,1},
                  {1,-1},{1,0},{1,1}],
    FreqMap = lists:foldl(
        fun({I, Row}, Acc) ->
            lists:foldl(
                fun({J, _Val}, Acc2) ->
                    lists:foldl(
                        fun(Dir, Acc3) -> collect_numbers(I, J, Dir, Mat, M, N, Acc3) end,
                        Acc2,
                        Directions)
                end,
                Acc,
                indexed_row(Row))
        end,
        #{},
        indexed_rows(Mat)),
    case maps:size(FreqMap) of
        0 -> -1;
        _ ->
            {BestPrime,_} = maps:fold(
                fun(K, V, {BestK, BestV}) ->
                    if V > BestV; (V == BestV andalso K > BestK) -> {K, V};
                       true -> {BestK, BestV}
                    end
                end,
                {-1,0},
                FreqMap),
            BestPrime
    end.

%% helpers

indexed_rows(Mat) ->
    lists:zip(lists:seq(0, length(Mat)-1), Mat).

indexed_row(Row) ->
    lists:zip(lists:seq(0, length(Row)-1), Row).

collect_numbers(I, J, {Dx, Dy}, Mat, M, N, Map) ->
    Start = get_cell(Mat, I, J),
    walk(I+Dx, J+Dy, Dx, Dy, Start, Mat, M, N, Map).

walk(I, J, Dx, Dy, CurNum, _Mat, M, N, Map)
        when I >= 0, I < M, J >= 0, J < N ->
    Digit = get_cell(_Mat, I, J),
    NewNum = CurNum * 10 + Digit,
    UpdatedMap =
        if NewNum > 10, is_prime(NewNum) ->
                maps:update_with(NewNum, fun(C) -> C + 1 end, 1, Map);
           true -> Map
        end,
    walk(I+Dx, J+Dy, Dx, Dy, NewNum, _Mat, M, N, UpdatedMap);
walk(_, _, _, _, _, _, _, _, Map) ->
    Map.

get_cell(Mat, I, J) ->
    Row = lists:nth(I + 1, Mat),
    lists:nth(J + 1, Row).

is_prime(N) when N < 2 -> false;
is_prime(2) -> true;
is_prime(N) when N rem 2 =:= 0 -> false;
is_prime(N) ->
    Max = trunc(math:sqrt(N)),
    is_prime(N, 3, Max).

is_prime(_N, I, Max) when I > Max -> true;
is_prime(N, I, Max) ->
    if N rem I =:= 0 -> false;
       true -> is_prime(N, I + 2, Max)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec most_frequent_prime(mat :: [[integer]]) :: integer
  def most_frequent_prime(mat) do
    m = length(mat)
    n = length(List.first(mat))
    dirs = [{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}]

    counts =
      Enum.reduce(0..(m - 1), %{}, fn i, acc ->
        Enum.reduce(0..(n - 1), acc, fn j, acc2 ->
          start_digit = get(mat, i, j)

          Enum.reduce(dirs, acc2, fn {dx, dy}, acc3 ->
            process_direction(mat, m, n, i, j, start_digit, dx, dy, acc3)
          end)
        end)
      end)

    if map_size(counts) == 0 do
      -1
    else
      {prime, _cnt} = Enum.max_by(counts, fn {p, c} -> {c, p} end)
      prime
    end
  end

  defp process_direction(mat, m, n, i, j, start_digit, dx, dy, counts) do
    x = i + dx
    y = j + dy

    if in_bounds?(x, y, m, n) do
      num = start_digit * 10 + get(mat, x, y)
      counts = maybe_add(counts, num)

      walk(mat, m, n, x + dx, y + dy, dx, dy, num, counts)
    else
      counts
    end
  end

  defp walk(_mat, _m, _n, x, y, _dx, _dy, _cur_num, counts) when not in_bounds?(x, y, _m, _n),
    do: counts

  defp walk(mat, m, n, x, y, dx, dy, cur_num, counts) do
    new_num = cur_num * 10 + get(mat, x, y)
    counts = maybe_add(counts, new_num)

    walk(mat, m, n, x + dx, y + dy, dx, dy, new_num, counts)
  end

  defp maybe_add(map, num) do
    if num > 10 and is_prime(num) do
      Map.update(map, num, 1, &(&1 + 1))
    else
      map
    end
  end

  defp in_bounds?(x, y, m, n), do: x >= 0 and x < m and y >= 0 and y < n

  defp get(mat, i, j) do
    mat |> Enum.at(i) |> Enum.at(j)
  end

  defp is_prime(2), do: true
  defp is_prime(n) when n < 2 or rem(n, 2) == 0, do: false

  defp is_prime(n) do
    limit = :math.sqrt(n) |> trunc()
    Enum.reduce_while(3..limit, true, fn i, _acc ->
      if rem(n, i) == 0, do: {:halt, false}, else: {:cont, true}
    end)
  end
end
```
