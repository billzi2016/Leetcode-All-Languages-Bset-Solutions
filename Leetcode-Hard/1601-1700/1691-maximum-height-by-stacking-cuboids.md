# 1691. Maximum Height by Stacking Cuboids

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxHeight(vector<vector<int>>& cuboids) {
        for (auto &c : cuboids) sort(c.begin(), c.end()); // orient each cuboid
        sort(cuboids.begin(), cuboids.end(), [](const vector<int>& a, const vector<int>& b){
            if (a[0] != b[0]) return a[0] < b[0];
            if (a[1] != b[1]) return a[1] < b[1];
            return a[2] < b[2];
        });
        cuboids.insert(cuboids.begin(), {0,0,0}); // dummy base
        int n = cuboids.size();
        vector<int> dp(n, 0);
        for (int i = 0; i < n; ++i) dp[i] = cuboids[i][2];
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            ans = max(ans, dp[i]);
            for (int j = i + 1; j < n; ++j) {
                if (cuboids[i][0] <= cuboids[j][0] &&
                    cuboids[i][1] <= cuboids[j][1] &&
                    cuboids[i][2] <= cuboids[j][2]) {
                    dp[j] = max(dp[j], dp[i] + cuboids[j][2]);
                }
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int maxHeight(int[][] cuboids) {
        int n = cuboids.length;
        // Sort dimensions within each cuboid so that we can treat the largest as height
        for (int[] c : cuboids) {
            java.util.Arrays.sort(c);
        }
        // Sort cuboids lexicographically by their sorted dimensions
        java.util.Arrays.sort(cuboids, (a, b) -> {
            if (a[0] != b[0]) return a[0] - b[0];
            if (a[1] != b[1]) return a[1] - b[1];
            return a[2] - b[2];
        });
        // Add a dummy cuboid at the beginning to simplify DP
        int[][] arr = new int[n + 1][3];
        arr[0] = new int[]{0, 0, 0};
        for (int i = 0; i < n; i++) {
            arr[i + 1] = cuboids[i];
        }
        int[] dp = new int[n + 1];
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            dp[i] = arr[i][2]; // height of current cuboid alone
            for (int j = 0; j < i; j++) {
                if (arr[j][0] <= arr[i][0] && arr[j][1] <= arr[i][1] && arr[j][2] <= arr[i][2]) {
                    dp[i] = Math.max(dp[i], dp[j] + arr[i][2]);
                }
            }
            ans = Math.max(ans, dp[i]);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def maxHeight(self, cuboids):
        """
        :type cuboids: List[List[int]]
        :rtype: int
        """
        # Sort dimensions of each cuboid so that we can treat orientation uniformly
        for c in cuboids:
            c.sort()
        # Sort cuboids lexicographically to enable DP similar to LIS
        cuboids.sort()
        n = len(cuboids)
        dp = [0] * n
        max_h = 0
        for i in range(n):
            cur_h = cuboids[i][2]
            best = 0
            for j in range(i):
                if (cuboids[j][0] <= cuboids[i][0] and
                    cuboids[j][1] <= cuboids[i][1] and
                    cuboids[j][2] <= cuboids[i][2]):
                    if dp[j] > best:
                        best = dp[j]
            dp[i] = cur_h + best
            if dp[i] > max_h:
                max_h = dp[i]
        return max_h
```

## Python3

```python
from typing import List

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # Sort dimensions of each cuboid so that we can treat the largest as height
        for c in cuboids:
            c.sort()
        # Sort cuboids lexicographically to enable DP ordering
        cuboids.sort()
        # Add a dummy cuboid to simplify transitions
        cuboids = [[0, 0, 0]] + cuboids
        n = len(cuboids)
        dp = [0] * n
        for i in range(n):
            height_i = cuboids[i][2]
            dp[i] = height_i
            for j in range(i):
                if (cuboids[j][0] <= cuboids[i][0] and
                    cuboids[j][1] <= cuboids[i][1] and
                    cuboids[j][2] <= cuboids[i][2]):
                    dp[i] = max(dp[i], dp[j] + height_i)
        return max(dp)
```

## C

```c
#include <stdlib.h>

typedef struct {
    int d[3];
} Cuboid;

static void sort_three(int *a, int *b, int *c) {
    if (*a > *b) { int t = *a; *a = *b; *b = t; }
    if (*b > *c) { int t = *b; *b = *c; *c = t; }
    if (*a > *b) { int t = *a; *a = *b; *b = t; }
}

static int cuboid_cmp(const void *p, const void *q) {
    const Cuboid *x = (const Cuboid *)p;
    const Cuboid *y = (const Cuboid *)q;
    if (x->d[0] != y->d[0]) return x->d[0] - y->d[0];
    if (x->d[1] != y->d[1]) return x->d[1] - y->d[1];
    return x->d[2] - y->d[2];
}

int maxHeight(int** cuboids, int cuboidsSize, int* cuboidsColSize){
    if (cuboidsSize == 0) return 0;
    Cuboid *arr = (Cuboid *)malloc(sizeof(Cuboid) * cuboidsSize);
    for (int i = 0; i < cuboidsSize; ++i) {
        int a = cuboids[i][0];
        int b = cuboids[i][1];
        int c = cuboids[i][2];
        sort_three(&a, &b, &c);
        arr[i].d[0] = a;
        arr[i].d[1] = b;
        arr[i].d[2] = c; // largest dimension will be used as height
    }
    qsort(arr, cuboidsSize, sizeof(Cuboid), cuboid_cmp);

    int dp[101] = {0};
    int ans = 0;
    for (int i = 0; i < cuboidsSize; ++i) {
        dp[i] = arr[i].d[2]; // height of this cuboid
        for (int j = 0; j < i; ++j) {
            if (arr[j].d[0] <= arr[i].d[0] &&
                arr[j].d[1] <= arr[i].d[1] &&
                arr[j].d[2] <= arr[i].d[2]) {
                if (dp[j] + arr[i].d[2] > dp[i])
                    dp[i] = dp[j] + arr[i].d[2];
            }
        }
        if (dp[i] > ans) ans = dp[i];
    }

    free(arr);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxHeight(int[][] cuboids)
    {
        int n = cuboids.Length;
        // Sort dimensions inside each cuboid so that we can treat the largest as height
        for (int i = 0; i < n; i++)
        {
            Array.Sort(cuboids[i]);
        }

        // Sort cuboids lexicographically by their sorted dimensions
        Array.Sort(cuboids, (a, b) =>
        {
            if (a[0] != b[0]) return a[0] - b[0];
            if (a[1] != b[1]) return a[1] - b[1];
            return a[2] - b[2];
        });

        int[] dp = new int[n];
        int answer = 0;

        for (int i = 0; i < n; i++)
        {
            dp[i] = cuboids[i][2]; // height of the current cuboid
            for (int j = 0; j < i; j++)
            {
                if (cuboids[j][0] <= cuboids[i][0] &&
                    cuboids[j][1] <= cuboids[i][1] &&
                    cuboids[j][2] <= cuboids[i][2])
                {
                    dp[i] = Math.Max(dp[i], dp[j] + cuboids[i][2]);
                }
            }
            answer = Math.Max(answer, dp[i]);
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} cuboids
 * @return {number}
 */
var maxHeight = function(cuboids) {
    // Normalize each cuboid by sorting its dimensions (rotate to make height the largest)
    const normalized = cuboids.map(arr => arr.slice().sort((a, b) => a - b));
    
    // Sort cuboids lexicographically so that a valid stacking order can be found via DP
    normalized.sort((a, b) => {
        if (a[0] !== b[0]) return a[0] - b[0];
        if (a[1] !== b[1]) return a[1] - b[1];
        return a[2] - b[2];
    });
    
    // Add a dummy cuboid to simplify DP base case
    normalized.unshift([0, 0, 0]);
    
    const n = normalized.length;
    const dp = new Array(n).fill(0);
    let answer = 0;
    
    for (let i = 1; i < n; ++i) {
        const cur = normalized[i];
        dp[i] = cur[2]; // height of current cuboid alone
        for (let j = 0; j < i; ++j) {
            const prev = normalized[j];
            if (prev[0] <= cur[0] && prev[1] <= cur[1] && prev[2] <= cur[2]) {
                dp[i] = Math.max(dp[i], dp[j] + cur[2]);
            }
        }
        answer = Math.max(answer, dp[i]);
    }
    
    return answer;
};
```

## Typescript

```typescript
function maxHeight(cuboids: number[][]): number {
    // Sort dimensions within each cuboid so that we can treat the largest as height
    for (const c of cuboids) {
        c.sort((a, b) => a - b);
    }
    // Lexicographically sort cuboids to enable DP ordering
    cuboids.sort((a, b) => {
        if (a[0] !== b[0]) return a[0] - b[0];
        if (a[1] !== b[1]) return a[1] - b[1];
        return a[2] - b[2];
    });
    // Add a dummy cuboid to simplify transitions
    cuboids.unshift([0, 0, 0]);
    const m = cuboids.length;
    const dp = new Array(m).fill(0);
    let maxTotal = 0;
    for (let i = 1; i < m; ++i) {
        dp[i] = cuboids[i][2]; // height when placed alone
        for (let j = 0; j < i; ++j) {
            if (
                cuboids[j][0] <= cuboids[i][0] &&
                cuboids[j][1] <= cuboids[i][1] &&
                cuboids[j][2] <= cuboids[i][2]
            ) {
                dp[i] = Math.max(dp[i], dp[j] + cuboids[i][2]);
            }
        }
        maxTotal = Math.max(maxTotal, dp[i]);
    }
    return maxTotal;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $cuboids
     * @return Integer
     */
    function maxHeight($cuboids) {
        // Sort dimensions of each cuboid so that we can treat the largest as height
        foreach ($cuboids as &$c) {
            sort($c);
        }
        unset($c);

        // Add a dummy cuboid to simplify DP initialization
        $cuboids[] = [0, 0, 0];

        // Sort all cuboids lexicographically (by width, then length, then height)
        usort($cuboids, function ($a, $b) {
            if ($a[0] == $b[0]) {
                if ($a[1] == $b[1]) {
                    return $a[2] <=> $b[2];
                }
                return $a[1] <=> $b[1];
            }
            return $a[0] <=> $b[0];
        });

        $n = count($cuboids);
        $dp = array_fill(0, $n, 0);
        $maxHeight = 0;

        for ($i = 0; $i < $n; $i++) {
            // Height of current cuboid is its largest dimension (index 2 after sorting)
            $dp[$i] = $cuboids[$i][2];
            for ($j = 0; $j < $i; $j++) {
                if ($cuboids[$j][0] <= $cuboids[$i][0] &&
                    $cuboids[$j][1] <= $cuboids[$i][1] &&
                    $cuboids[$j][2] <= $cuboids[$i][2]) {
                    $dp[$i] = max($dp[$i], $dp[$j] + $cuboids[$i][2]);
                }
            }
            $maxHeight = max($maxHeight, $dp[$i]);
        }

        return $maxHeight;
    }
}
```

## Swift

```swift
class Solution {
    func maxHeight(_ cuboids: [[Int]]) -> Int {
        var boxes = cuboids.map { $0.sorted() }
        boxes.sort { (a, b) -> Bool in
            if a[0] != b[0] { return a[0] < b[0] }
            if a[1] != b[1] { return a[1] < b[1] }
            return a[2] < b[2]
        }

        let n = boxes.count
        var dp = Array(repeating: 0, count: n)
        var result = 0

        for i in 0..<n {
            dp[i] = boxes[i][2] // height of current cuboid
            for j in 0..<i {
                if boxes[j][0] <= boxes[i][0] &&
                    boxes[j][1] <= boxes[i][1] &&
                    boxes[j][2] <= boxes[i][2] {
                    dp[i] = max(dp[i], dp[j] + boxes[i][2])
                }
            }
            result = max(result, dp[i])
        }

        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxHeight(cuboids: Array<IntArray>): Int {
        // Sort dimensions of each cuboid so that we can treat orientation uniformly
        for (c in cuboids) {
            c.sort()
        }
        // Sort cuboids lexicographically by their sorted dimensions
        cuboids.sortWith(compareBy<IntArray>({ it[0] }, { it[1] }, { it[2] }))
        // Add a dummy cuboid to simplify DP transitions
        val all = mutableListOf<IntArray>()
        all.add(intArrayOf(0, 0, 0))
        for (c in cuboids) {
            all.add(c)
        }
        val m = all.size
        val dp = IntArray(m)
        var answer = 0
        for (i in 1 until m) {
            dp[i] = all[i][2] // height of current cuboid alone
            for (j in 0 until i) {
                if (all[j][0] <= all[i][0] &&
                    all[j][1] <= all[i][1] &&
                    all[j][2] <= all[i][2]) {
                    dp[i] = maxOf(dp[i], dp[j] + all[i][2])
                }
            }
            answer = maxOf(answer, dp[i])
        }
        return answer
    }
}
```

## Golang

```go
import "sort"

func maxHeight(cuboids [][]int) int {
	// Sort dimensions inside each cuboid so that we can treat the largest as height
	for _, c := range cuboids {
		sort.Ints(c)
	}
	// Lexicographically sort cuboids
	sort.Slice(cuboids, func(i, j int) bool {
		if cuboids[i][0] != cuboids[j][0] {
			return cuboids[i][0] < cuboids[j][0]
		}
		if cuboids[i][1] != cuboids[j][1] {
			return cuboids[i][1] < cuboids[j][1]
		}
		return cuboids[i][2] < cuboids[j][2]
	})

	n := len(cuboids)
	// Add a dummy cuboid at index 0
	all := make([][3]int, n+1)
	all[0] = [3]int{0, 0, 0}
	for i := 0; i < n; i++ {
		all[i+1] = [3]int{cuboids[i][0], cuboids[i][1], cuboids[i][2]}
	}

	dp := make([]int, n+1)
	maxH := 0
	for i := 1; i <= n; i++ {
		dp[i] = all[i][2] // at least its own height
		for j := 0; j < i; j++ {
			if all[j][0] <= all[i][0] && all[j][1] <= all[i][1] && all[j][2] <= all[i][2] {
				if dp[j]+all[i][2] > dp[i] {
					dp[i] = dp[j] + all[i][2]
				}
			}
		}
		if dp[i] > maxH {
			maxH = dp[i]
		}
	}
	return maxH
}
```

## Ruby

```ruby
# @param {Integer[][]} cuboids
# @return {Integer}
def max_height(cuboids)
  # Sort dimensions of each cuboid so that we can treat orientation uniformly
  sorted = cuboids.map { |c| c.sort }
  # Add a dummy cuboid to simplify DP initialization
  sorted << [0, 0, 0]
  # Sort all cuboids lexicographically (by width, then length, then height)
  sorted.sort_by! { |c| [c[0], c[1], c[2]] }

  n = sorted.size
  dp = Array.new(n, 0)
  max_h = 0

  (0...n).each do |i|
    # Height of the current cuboid is its largest dimension after sorting
    dp[i] = sorted[i][2]
    (0...i).each do |j|
      if sorted[j][0] <= sorted[i][0] && sorted[j][1] <= sorted[i][1] && sorted[j][2] <= sorted[i][2]
        dp[i] = [dp[i], dp[j] + sorted[i][2]].max
      end
    end
    max_h = [max_h, dp[i]].max
  end

  max_h
end
```

## Scala

```scala
object Solution {
  def maxHeight(cuboids: Array[Array[Int]]): Int = {
    // Sort dimensions within each cuboid
    val normalized = cuboids.map(_.sorted)

    // Lexicographic sort of cuboids
    java.util.Arrays.sort(normalized, new java.util.Comparator[Array[Int]] {
      override def compare(a: Array[Int], b: Array[Int]): Int = {
        if (a(0) != b(0)) a(0) - b(0)
        else if (a(1) != b(1)) a(1) - b(1)
        else a(2) - b(2)
      }
    })

    val n = normalized.length
    val dp = new Array[Int](n)
    var answer = 0

    for (i <- 0 until n) {
      dp(i) = normalized(i)(2) // height of current cuboid
      for (j <- 0 until i) {
        if (normalized(j)(0) <= normalized(i)(0) &&
            normalized(j)(1) <= normalized(i)(1) &&
            normalized(j)(2) <= normalized(i)(2)) {
          dp(i) = math.max(dp(i), dp(j) + normalized(i)(2))
        }
      }
      answer = math.max(answer, dp(i))
    }

    answer
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_height(cuboids: Vec<Vec<i32>>) -> i32 {
        let mut cubes = cuboids;
        for c in cubes.iter_mut() {
            c.sort();
        }
        cubes.sort();

        let n = cubes.len();
        let mut dp = vec![0i32; n];
        let mut ans = 0i32;

        for i in 0..n {
            dp[i] = cubes[i][2];
            for j in 0..i {
                if cubes[j][0] <= cubes[i][0]
                    && cubes[j][1] <= cubes[i][1]
                    && cubes[j][2] <= cubes[i][2]
                {
                    dp[i] = dp[i].max(dp[j] + cubes[i][2]);
                }
            }
            ans = ans.max(dp[i]);
        }

        ans
    }
}
```
