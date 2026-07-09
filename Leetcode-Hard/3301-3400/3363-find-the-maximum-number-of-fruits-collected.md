# 3363. Find the Maximum Number of Fruits Collected

## Cpp

```cpp
class Solution {
public:
    long long computeUpper(const vector<vector<int>>& a) {
        int n = a.size();
        const long long NEG = -(1LL<<60);
        vector<long long> prev(n, NEG), cur(n, NEG);
        // start at (0, n-1)
        prev[n-1] = a[0][n-1];
        for (int i = 1; i <= n - 2; ++i) {
            fill(cur.begin(), cur.end(), NEG);
            for (int j = i + 1; j < n; ++j) { // must stay above diagonal: i<j
                long long best = prev[j];
                if (j > 0) best = max(best, prev[j - 1]);
                if (j + 1 < n) best = max(best, prev[j + 1]);
                cur[j] = best + a[i][j];
            }
            swap(prev, cur);
        }
        return prev[n-1]; // value at (n-2, n-1)
    }

    int maxCollectedFruits(vector<vector<int>>& fruits) {
        int n = fruits.size();
        long long diagSum = 0;
        for (int i = 0; i < n; ++i) diagSum += fruits[i][i];

        long long upper = computeUpper(fruits);

        // transpose to reuse the same DP for the lower triangle
        vector<vector<int>> trans(n, vector<int>(n));
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                trans[i][j] = fruits[j][i];

        long long lower = computeUpper(trans);

        return (int)(diagSum + upper + lower);
    }
};
```

## Java

```java
class Solution {
    public int maxCollectedFruits(int[][] fruits) {
        int n = fruits.length;
        long diagSum = 0;
        for (int i = 0; i < n; i++) {
            diagSum += fruits[i][i];
        }
        long above = maxSide(fruits);
        // transpose matrix
        int[][] trans = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                trans[i][j] = fruits[j][i];
            }
        }
        long below = maxSide(trans);
        return (int) (diagSum + above + below);
    }

    private long maxSide(int[][] a) {
        int n = a.length;
        final long NEG = Long.MIN_VALUE / 4;
        long[] prev = new long[n];
        for (int i = 0; i < n; i++) prev[i] = NEG;
        prev[n - 1] = a[0][n - 1]; // start at top‑right corner

        // process rows 1 .. n-2
        for (int i = 1; i <= n - 2; i++) {
            long[] cur = new long[n];
            for (int j = 0; j < n; j++) cur[j] = NEG;
            // column must stay strictly above main diagonal: j > i
            for (int j = i + 1; j < n; j++) {
                long best = prev[j];
                if (j - 1 >= 0) best = Math.max(best, prev[j - 1]);
                if (j + 1 < n) best = Math.max(best, prev[j + 1]);
                cur[j] = best + a[i][j];
            }
            prev = cur;
        }
        // after processing row n-2, the child must be at column n‑1
        return prev[n - 1];
    }
}
```

## Python

```python
class Solution(object):
    def maxCollectedFruits(self, fruits):
        """
        :type fruits: List[List[int]]
        :rtype: int
        """
        n = len(fruits)
        # sum of main diagonal collected by child starting at (0,0)
        diag_sum = 0
        for i in range(n):
            diag_sum += fruits[i][i]

        def upper_path(grid):
            INF_NEG = -10**15
            prev = [INF_NEG] * n
            prev[n - 1] = grid[0][n - 1]  # start at top‑right corner
            if n == 2:
                return prev[n - 1]
            for i in range(1, n - 1):  # rows 1 .. n-2
                cur = [INF_NEG] * n
                start_j = i + 1          # must stay above main diagonal (j > i)
                for j in range(start_j, n):
                    best = prev[j]
                    if j - 1 >= 0:
                        best = max(best, prev[j - 1])
                    if j + 1 < n:
                        best = max(best, prev[j + 1])
                    cur[j] = best + grid[i][j]
                prev = cur
            # after processing row n-2, must be at column n-1 before final move
            return prev[n - 1]

        upper = upper_path(fruits)

        # transpose to reuse the same DP for the lower side (mirror image)
        transposed = [list(row) for row in zip(*fruits)]
        lower = upper_path(transposed)

        return diag_sum + upper + lower
```

## Python3

```python
class Solution:
    def maxCollectedFruits(self, fruits):
        n = len(fruits)
        diag_sum = sum(fruits[i][i] for i in range(n))
        if n == 1:
            return diag_sum

        INF_NEG = -10**15
        prev = [INF_NEG] * n
        prev[n - 1] = fruits[0][n - 1]

        for i in range(1, n - 1):  # rows 1 .. n-2
            cur = [INF_NEG] * n
            start_j = i + 1  # must stay above main diagonal (j > i)
            for j in range(start_j, n):
                best = prev[j]
                if j - 1 >= 0:
                    best = max(best, prev[j - 1])
                if j + 1 < n:
                    best = max(best, prev[j + 1])
                cur[j] = best + fruits[i][j]
            prev = cur

        upper_path = prev[n - 1]  # cell (n-2, n-1)
        return diag_sum + 2 * upper_path
```

## C

```c
int maxCollectedFruits(int** fruits, int fruitsSize, int* fruitsColSize){
    int n = fruitsSize;
    if (n == 0) return 0;

    // sum of main diagonal (child starting at (0,0))
    int diagSum = 0;
    for (int i = 0; i < n; ++i)
        diagSum += fruits[i][i];

    const int NEG_INF = -1000000000;
    int *prev = (int*)malloc(n * sizeof(int));
    int *curr = (int*)malloc(n * sizeof(int));

    // Upper triangle DP (child from top‑right)
    for (int j = 0; j < n; ++j) prev[j] = NEG_INF;
    prev[n - 1] = fruits[0][n - 1];               // start at (0, n-1)

    for (int i = 1; i <= n - 2; ++i){
        for (int j = 0; j < n; ++j) curr[j] = NEG_INF;
        for (int j = i + 1; j < n; ++j){          // keep j > i
            int best = prev[j];
            if (j - 1 >= 0 && prev[j - 1] > best) best = prev[j - 1];
            if (j + 1 < n && prev[j + 1] > best) best = prev[j + 1];
            curr[j] = best + fruits[i][j];
        }
        int *tmp = prev; prev = curr; curr = tmp;
    }
    int upperAns = prev[n - 1];

    // Lower triangle DP (child from bottom‑left) using transposed access
    for (int j = 0; j < n; ++j) prev[j] = NEG_INF;
    prev[n - 1] = fruits[n - 1][0];               // start at (n-1, 0)

    for (int i = 1; i <= n - 2; ++i){
        for (int j = 0; j < n; ++j) curr[j] = NEG_INF;
        for (int j = i + 1; j < n; ++j){          // keep j > i in transposed view
            int best = prev[j];
            if (j - 1 >= 0 && prev[j - 1] > best) best = prev[j - 1];
            if (j + 1 < n && prev[j + 1] > best) best = prev[j + 1];
            curr[j] = best + fruits[j][i];        // transposed access
        }
        int *tmp = prev; prev = curr; curr = tmp;
    }
    int lowerAns = prev[n - 1];

    free(prev);
    free(curr);

    return diagSum + upperAns + lowerAns;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxCollectedFruits(int[][] fruits) {
        int n = fruits.Length;
        long diagSum = 0;
        for (int i = 0; i < n; i++) diagSum += fruits[i][i];

        long upper = CalcUpper(fruits);

        // transpose matrix to reuse the same DP for the lower side
        int[][] trans = new int[n][];
        for (int i = 0; i < n; i++) trans[i] = new int[n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                trans[i][j] = fruits[j][i];

        long lower = CalcUpper(trans);

        long total = diagSum + upper + lower;
        return (int)total;
    }

    private long CalcUpper(int[][] a) {
        int n = a.Length;
        const long NEG = -1L << 60;

        long[] prev = new long[n];
        for (int i = 0; i < n; i++) prev[i] = NEG;
        prev[n - 1] = a[0][n - 1];

        if (n == 2) {
            // only the starting cell contributes
            return prev[n - 1];
        }

        for (int i = 1; i <= n - 2; i++) {
            long[] cur = new long[n];
            for (int j = 0; j < n; j++) cur[j] = NEG;

            // stay strictly above the main diagonal: column > row
            for (int j = i + 1; j < n; j++) {
                long best = prev[j];
                if (j - 1 >= 0) best = Math.Max(best, prev[j - 1]);
                if (j + 1 < n) best = Math.Max(best, prev[j + 1]);
                cur[j] = best + a[i][j];
            }
            prev = cur;
        }

        return prev[n - 1]; // value at (n-2, n-1)
    }
}
```

## Javascript

```javascript
/**
 * @param {number[][]} fruits
 * @return {number}
 */
var maxCollectedFruits = function(fruits) {
    const n = fruits.length;
    let diagSum = 0;
    for (let i = 0; i < n; ++i) diagSum += fruits[i][i];

    const NEG = -1e15;

    // DP for the upper‑triangular child (starts at (0, n-1))
    let prev = new Array(n).fill(NEG);
    prev[n - 1] = fruits[0][n - 1];
    for (let i = 1; i <= n - 2; ++i) {
        const cur = new Array(n).fill(NEG);
        // column must stay strictly above the main diagonal: j > i
        for (let j = i + 1; j < n; ++j) {
            let best = prev[j];
            if (j - 1 >= 0) best = Math.max(best, prev[j - 1]);
            if (j + 1 < n) best = Math.max(best, prev[j + 1]);
            cur[j] = best + fruits[i][j];
        }
        prev = cur;
    }
    const upper = n === 2 ? fruits[0][n - 1] : prev[n - 1];

    // DP for the lower‑triangular child (starts at (n-1, 0))
    // Use transposed matrix to reuse the same logic.
    const t = Array.from({ length: n }, () => new Array(n));
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < n; ++j) {
            t[i][j] = fruits[j][i];
        }
    }

    let prev2 = new Array(n).fill(NEG);
    prev2[n - 1] = t[0][n - 1]; // corresponds to original (n-1,0)
    for (let i = 1; i <= n - 2; ++i) {
        const cur = new Array(n).fill(NEG);
        for (let j = i + 1; j < n; ++j) {
            let best = prev2[j];
            if (j - 1 >= 0) best = Math.max(best, prev2[j - 1]);
            if (j + 1 < n) best = Math.max(best, prev2[j + 1]);
            cur[j] = best + t[i][j];
        }
        prev2 = cur;
    }
    const lower = n === 2 ? fruits[n - 1][0] : prev2[n - 1];

    return diagSum + upper + lower;
};
```

## Typescript

```typescript
function maxCollectedFruits(fruits: number[][]): number {
    const n = fruits.length;
    // sum of main diagonal (child starting at (0,0))
    let diagSum = 0;
    for (let i = 0; i < n; ++i) diagSum += fruits[i][i];

    const dpMax = (mat: number[][]): number => {
        if (n === 2) return mat[0][1];
        let prev = new Array(n).fill(Number.NEGATIVE_INFINITY);
        prev[n - 1] = mat[0][n - 1]; // start at top‑right corner
        for (let i = 1; i <= n - 2; ++i) {
            const curr = new Array(n).fill(Number.NEGATIVE_INFINITY);
            for (let j = i + 1; j < n; ++j) { // must stay above main diagonal: j > i
                let best = prev[j];
                if (j - 1 >= 0) best = Math.max(best, prev[j - 1]);
                if (j + 1 < n) best = Math.max(best, prev[j + 1]);
                curr[j] = best + mat[i][j];
            }
            prev = curr;
        }
        return prev[n - 1]; // reach cell (n‑2, n‑1)
    };

    // DP for child starting at top‑right corner
    const part1 = dpMax(fruits);

    // Transpose matrix to reuse the same DP for the other child
    const transposed: number[][] = Array.from({ length: n }, () => new Array(n));
    for (let i = 0; i < n; ++i) {
        for (let j = 0; j < n; ++j) {
            transposed[i][j] = fruits[j][i];
        }
    }
    const part2 = dpMax(transposed);

    return diagSum + part1 + part2;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[][] $fruits
     * @return Integer
     */
    function maxCollectedFruits($fruits) {
        $n = count($fruits);
        // sum of main diagonal (child at (0,0))
        $diagSum = 0;
        for ($i = 0; $i < $n; ++$i) {
            $diagSum += $fruits[$i][$i];
        }

        // helper to compute max path in upper triangle starting from (0, n-1)
        $compute = function($mat) use ($n) {
            $negInf = -1000000000;
            $dp = array_fill(0, $n, $negInf);
            $dp[$n - 1] = $mat[0][$n - 1]; // start cell

            for ($i = 1; $i <= $n - 2; ++$i) {
                $new = array_fill(0, $n, $negInf);
                // columns where j > i (strictly above main diagonal)
                for ($j = $i + 1; $j < $n; ++$j) {
                    $best = $dp[$j]; // from (i-1, j)
                    if ($j - 1 >= 0) {
                        $best = max($best, $dp[$j - 1]); // from (i-1, j-1)
                    }
                    if ($j + 1 < $n) {
                        $best = max($best, $dp[$j + 1]); // from (i-1, j+1)
                    }
                    $new[$j] = $best + $mat[$i][$j];
                }
                $dp = $new;
            }
            return $dp[$n - 1]; // cell (n-2, n-1)
        };

        // upper triangle contribution
        $upper = $compute($fruits);

        // build transposed matrix for lower triangle computation
        $trans = array_fill(0, $n, []);
        for ($i = 0; $i < $n; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                $trans[$i][$j] = $fruits[$j][$i];
            }
        }

        // lower triangle contribution (symmetric)
        $lower = $compute($trans);

        return $diagSum + $upper + $lower;
    }
}
```

## Swift

```swift
class Solution {
    func maxCollectedFruits(_ fruits: [[Int]]) -> Int {
        let n = fruits.count
        // Sum of main diagonal (child at (0,0))
        var diagSum = 0
        for i in 0..<n {
            diagSum += fruits[i][i]
        }
        
        func computeUpper(_ a: [[Int]]) -> Int {
            let n = a.count
            let negInf = Int.min / 4
            var prev = Array(repeating: negInf, count: n)
            prev[n - 1] = a[0][n - 1]
            if n == 2 { return prev[n - 1] }
            for i in 1..<(n - 1) {
                var cur = Array(repeating: negInf, count: n)
                let startJ = i + 1
                if startJ >= n { continue }
                for j in startJ..<n {
                    var best = prev[j]
                    if j > 0 && prev[j - 1] > best { best = prev[j - 1] }
                    if j + 1 < n && prev[j + 1] > best { best = prev[j + 1] }
                    cur[j] = a[i][j] + best
                }
                prev = cur
            }
            return prev[n - 1]
        }
        
        // Upper region DP (child from top-right)
        let upper = computeUpper(fruits)
        
        // Transpose matrix to reuse same DP for lower region
        var trans = Array(repeating: Array(repeating: 0, count: n), count: n)
        for i in 0..<n {
            for j in 0..<n {
                trans[i][j] = fruits[j][i]
            }
        }
        let lower = computeUpper(trans)
        
        return diagSum + upper + lower
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxCollectedFruits(fruits: Array<IntArray>): Int {
        val n = fruits.size
        var diagSum = 0L
        for (i in 0 until n) {
            diagSum += fruits[i][i].toLong()
        }

        fun compute(mat: Array<IntArray>): Long {
            if (n == 2) return mat[0][n - 1].toLong()
            val negInf = Long.MIN_VALUE / 4
            var prev = LongArray(n) { negInf }
            prev[n - 1] = mat[0][n - 1].toLong()

            for (i in 1 until n - 1) {
                val cur = LongArray(n) { negInf }
                // columns strictly above main diagonal: j > i
                var j = i + 1
                while (j < n) {
                    var best = prev[j]
                    if (j > 0 && prev[j - 1] > best) best = prev[j - 1]
                    if (j + 1 < n && prev[j + 1] > best) best = prev[j + 1]
                    if (best != negInf) {
                        cur[j] = best + mat[i][j]
                    }
                    j++
                }
                prev = cur
            }
            return prev[n - 1]
        }

        val upper = compute(fruits)

        // transpose matrix for the symmetric lower path
        val trans = Array(n) { IntArray(n) }
        for (i in 0 until n) {
            for (j in 0 until n) {
                trans[i][j] = fruits[j][i]
            }
        }
        val lower = compute(trans)

        return (diagSum + upper + lower).toInt()
    }
}
```

## Dart

```dart
class Solution {
  int maxCollectedFruits(List<List<int>> fruits) {
    int n = fruits.length;
    // Sum of main diagonal (child at (0,0))
    int diagSum = 0;
    for (int i = 0; i < n; i++) {
      diagSum += fruits[i][i];
    }

    int computeUpper(List<List<int>> a) {
      const int NEG = -1 << 60; // sufficiently small negative number
      List<int> prev = List.filled(n, NEG);
      prev[n - 1] = a[0][n - 1]; // start at (0, n-1)

      for (int i = 1; i <= n - 2; i++) {
        List<int> cur = List.filled(n, NEG);
        for (int j = i + 1; j < n; j++) { // stay above main diagonal
          int best = prev[j];
          if (j - 1 >= 0 && prev[j - 1] > best) best = prev[j - 1];
          if (j + 1 < n && prev[j + 1] > best) best = prev[j + 1];
          cur[j] = best + a[i][j];
        }
        prev = cur;
      }
      return prev[n - 1]; // value at (n-2, n-1)
    }

    int upper = computeUpper(fruits);

    // Transpose matrix to reuse the same DP for the lower triangle child
    List<List<int>> trans = List.generate(n, (_) => List.filled(n, 0));
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        trans[i][j] = fruits[j][i];
      }
    }

    int lower = computeUpper(trans);

    return diagSum + upper + lower;
  }
}
```

## Golang

```go
func maxCollectedFruits(fruits [][]int) int {
	const neg = -1 << 30 // sufficiently small negative value
	n := len(fruits)

	// sum of main diagonal (child starting at (0,0))
	total := 0
	for i := 0; i < n; i++ {
		total += fruits[i][i]
	}

	// helper to compute maximum collection for the upper‑triangular side
	computeUpper := func(a [][]int) int {
		if n == 1 {
			return 0
		}
		dpPrev := make([]int, n)
		for i := range dpPrev {
			dpPrev[i] = neg
		}
		// start at (0, n-1)
		dpPrev[n-1] = a[0][n-1]

		// process rows 1 .. n-2
		for row := 1; row <= n-2; row++ {
			dpCurr := make([]int, n)
			for i := range dpCurr {
				dpCurr[i] = neg
			}
			for col := row + 1; col < n; col++ { // columns strictly above diagonal
				best := dpPrev[col]
				if col > 0 && dpPrev[col-1] > best {
					best = dpPrev[col-1]
				}
				if col+1 < n && dpPrev[col+1] > best {
					best = dpPrev[col+1]
				}
				dpCurr[col] = best + a[row][col]
			}
			dpPrev = dpCurr
		}

		// final row is n-2 (or 0 when n==2)
		ans := neg
		lastRow := n - 2
		if lastRow < 0 { // n == 1, not possible per constraints
			return 0
		}
		for col := lastRow + 1; col < n; col++ {
			if dpPrev[col] > ans {
				ans = dpPrev[col]
			}
		}
		// when n==2 the loop above runs for row=0, col=n-1 only
		return ans
	}

	upper := computeUpper(fruits)

	// transpose matrix to reuse the same DP for the lower‑triangular side
	trans := make([][]int, n)
	for i := 0; i < n; i++ {
		trans[i] = make([]int, n)
		for j := 0; j < n; j++ {
			trans[i][j] = fruits[j][i]
		}
	}
	lower := computeUpper(trans)

	return total + upper + lower
}
```

## Ruby

```ruby
def upper_path(fruits)
  n = fruits.size
  neg_inf = -1 << 60
  prev = Array.new(n, neg_inf)
  prev[n - 1] = fruits[0][n - 1]

  (1...n - 1).each do |i|
    cur = Array.new(n, neg_inf)
    ((i + 1)...n).each do |j|
      best = prev[j]
      best = [best, prev[j - 1]].max if j - 1 >= 0
      best = [best, prev[j + 1]].max if j + 1 < n
      cur[j] = best + fruits[i][j]
    end
    prev = cur
  end

  prev[n - 1]
end

def max_collected_fruits(fruits)
  n = fruits.size
  diag_sum = 0
  (0...n).each { |i| diag_sum += fruits[i][i] }

  upper = upper_path(fruits)

  trans = Array.new(n) { Array.new(n) }
  (0...n).each do |i|
    (0...n).each do |j|
      trans[i][j] = fruits[j][i]
    end
  end

  lower = upper_path(trans)

  diag_sum + upper + lower
end
```

## Scala

```scala
object Solution {
    def maxCollectedFruits(fruits: Array[Array[Int]]): Int = {
        val n = fruits.length
        var diagSum = 0
        var i = 0
        while (i < n) {
            diagSum += fruits(i)(i)
            i += 1
        }

        def calc(mat: Array[Array[Int]]): Int = {
            val NEG_INF = -1000000000
            var prev = Array.fill(n)(NEG_INF)
            prev(n - 1) = mat(0)(n - 1)

            var row = 1
            while (row < n - 1) {
                val curr = Array.fill(n)(NEG_INF)
                var col = row + 1
                while (col < n) {
                    var best = prev(col)
                    if (col - 1 >= 0) best = math.max(best, prev(col - 1))
                    if (col + 1 < n) best = math.max(best, prev(col + 1))
                    curr(col) = mat(row)(col) + best
                    col += 1
                }
                prev = curr
                row += 1
            }
            prev(n - 1)
        }

        val upper = calc(fruits)

        // transpose the matrix
        val transposed = Array.ofDim[Int](n, n)
        var r = 0
        while (r < n) {
            var c = 0
            while (c < n) {
                transposed(r)(c) = fruits(c)(r)
                c += 1
            }
            r += 1
        }

        val lower = calc(transposed)

        diagSum + upper + lower
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_collected_fruits(fruits: Vec<Vec<i32>>) -> i32 {
        let n = fruits.len();
        // sum of main diagonal (child starting at (0,0))
        let mut diag_sum: i32 = 0;
        for i in 0..n {
            diag_sum += fruits[i][i];
        }

        // helper to compute max sum for a child staying above the main diagonal
        fn calc(mat: &Vec<Vec<i32>>) -> i32 {
            let n = mat.len();
            if n == 2 {
                return mat[0][n - 1];
            }
            let mut prev = vec![i32::MIN; n];
            prev[n - 1] = mat[0][n - 1];
            for i in 1..=n - 2 {
                let mut cur = vec![i32::MIN; n];
                let start = std::cmp::max(i + 1, n - 1 - i);
                for j in start..n {
                    let mut best = prev[j];
                    if j > 0 && prev[j - 1] > best {
                        best = prev[j - 1];
                    }
                    if j + 1 < n && prev[j + 1] > best {
                        best = prev[j + 1];
                    }
                    cur[j] = best + mat[i][j];
                }
                prev = cur;
            }
            prev[n - 1]
        }

        // upper triangle child
        let upper = calc(&fruits);

        // transpose matrix to reuse the same DP for lower triangle child
        let mut transposed: Vec<Vec<i32>> = vec![vec![0; n]; n];
        for i in 0..n {
            for j in 0..n {
                transposed[i][j] = fruits[j][i];
            }
        }
        let lower = calc(&transposed);

        diag_sum + upper + lower
    }
}
```

## Racket

```racket
(define/contract (max-collected-fruits fruits)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ((mat (list->vector (map list->vector fruits)))
         (n (vector-length mat))
         (neg-inf -1000000000) ; sufficiently small sentinel
         
         ;; sum of main diagonal (child starting at (0,0))
         (diag-sum
          (let loop ((i 0) (acc 0))
            (if (= i n)
                acc
                (loop (+ i 1)
                      (+ acc (vector-ref (vector-ref mat i) i))))))
         
         ;; DP for a child starting at top‑right corner, staying above main diagonal
         (compute-upper
          (lambda (m)
            (let loop ((i 1)
                       (prev (let ((v (make-vector n neg-inf)))
                               (vector-set! v (- n 1) (vector-ref (vector-ref m 0) (- n 1)))
                               v)))
              (if (> i (- n 2))
                  (vector-ref prev (- n 1))
                  (let ((cur (make-vector n neg-inf)))
                    (let inner ((j (+ i 1)))
                      (when (<= j (- n 1))
                        (let* ((best (max (vector-ref prev j)
                                          (if (> j 0) (vector-ref prev (- j 1)) neg-inf)
                                          (if (< j (- n 1)) (vector-ref prev (+ j 1)) neg-inf))))
                          (when (> best neg-inf)
                            (vector-set! cur j
                                         (+ best (vector-ref (vector-ref m i) j)))))
                        (inner (+ j 1))))
                    (loop (+ i 1) cur))))))
         
         ;; upper‑triangle contribution
         (upper (compute-upper mat))
         
         ;; transpose matrix to reuse the same DP for the lower‑triangle child
         (transpose
          (let ((t (make-vector n)))
            (let loop-i ((i 0))
              (when (< i n)
                (let ((row (make-vector n)))
                  (let loop-j ((j 0))
                    (when (< j n)
                      (vector-set! row j (vector-ref (vector-ref mat j) i))
                      (loop-j (+ j 1))))
                  (vector-set! t i row)
                  (loop-i (+ i 1)))))
            t))
         
         ;; lower‑triangle contribution
         (lower (compute-upper transpose)))
    (+ diag-sum upper lower)))
```

## Erlang

```erlang
-module(solution).
-export([max_collected_fruits/1]).

-spec max_collected_fruits(Fruits :: [[integer()]]) -> integer().
max_collected_fruits(Fruits) ->
    N = length(Fruits),
    DiagSum = diag_sum(Fruits, N),
    Upper = dp_upper(Fruits, N),
    Transposed = transpose(Fruits, N),
    Lower = dp_upper(Transposed, N),
    DiagSum + Upper + Lower.

diag_sum(Fruits, N) ->
    lists:foldl(
      fun({Idx, Row}, Acc) ->
          Elem = lists:nth(Idx + 1, Row),
          Acc + Elem
      end,
      0,
      lists:zip(lists:seq(0, N - 1), Fruits)
    ).

dp_upper(Grid, N) ->
    NegInf = -1000000000,
    StartCol = N - 1,
    FirstRow = hd(Grid),
    Prev0 = [if I == StartCol -> lists:nth(StartCol + 1, FirstRow); true -> NegInf end
            || I <- lists:seq(0, N - 1)],
    UpperLoop = fun Loop(RowIdx, Prev) ->
        if RowIdx > N - 2 ->
                lists:nth(N, Prev);
           true ->
                Row = lists:nth(RowIdx + 1, Grid),
                Curr = [if J > RowIdx andalso J < N ->
                            MaxPrev = max3(
                                         val(Prev, J, NegInf),
                                         val(Prev, J - 1, NegInf),
                                         val(Prev, J + 1, NegInf)),
                            MaxPrev + lists:nth(J + 1, Row);
                        true -> NegInf
                    end
                    || J <- lists:seq(0, N - 1)],
                Loop(RowIdx + 1, Curr)
        end
    end,
    UpperLoop(1, Prev0).

val(List, Index, NegInf) ->
    case Index of
        I when I < 0; I >= length(List) -> NegInf;
        _ -> lists:nth(Index + 1, List)
    end.

max3(A, B, C) ->
    max(max(A, B), C).

transpose(Fruits, N) ->
    [ [lists:nth(I + 1, lists:nth(J + 1, Fruits)) || I <- lists:seq(0, N - 1)]
      || J <- lists:seq(0, N - 1)
    ].
```

## Elixir

```elixir
defmodule Solution do
  @spec max_collected_fruits(fruits :: [[integer]]) :: integer
  def max_collected_fruits(fruits) do
    n = length(fruits)

    # Convert each row to a tuple for O(1) element access
    rows = Enum.map(fruits, &List.to_tuple/1)

    # Sum of the main diagonal (fixed path from (0,0) to (n-1,n-1))
    diag_sum =
      Enum.reduce(0..(n - 1), 0, fn i, acc ->
        row = Enum.at(rows, i)
        acc + elem(row, i)
      end)

    upper = dp_upper(rows)

    # Transpose the matrix to reuse the same DP for the lower path
    trans_rows =
      for i <- 0..(n - 1) do
        for j <- 0..(n - 1), into: [] do
          row_j = Enum.at(rows, j)
          elem(row_j, i)
        end
        |> List.to_tuple()
      end

    lower = dp_upper(trans_rows)

    diag_sum + upper + lower
  end

  # DP for the child starting at (0, n-1) staying strictly above the main diagonal
  defp dp_upper(rows) do
    n = length(rows)
    neg_inf = -1_000_000_000

    # Initialize previous row array with start position value
    row0 = Enum.at(rows, 0)
    start_val = elem(row0, n - 1)

    prev = :array.new(n, default: neg_inf) |> :array.set(n - 1, start_val)

    # Process rows 1 .. n-2 (if any)
    final_prev =
      if n > 2 do
        Enum.reduce(1..(n - 2), prev, fn i, acc_prev ->
          row_i = Enum.at(rows, i)

          cur =
            Enum.reduce((i + 1)..(n - 1), :array.new(n, default: neg_inf), fn j, acc_cur ->
              best1 = :array.get(j, acc_prev)
              best2 = if j - 1 >= 0, do: :array.get(j - 1, acc_prev), else: neg_inf
              best3 = if j + 1 < n, do: :array.get(j + 1, acc_prev), else: neg_inf

              max_ab = if best1 > best2, do: best1, else: best2
              best = if best3 > max_ab, do: best3, else: max_ab

              val = best + elem(row_i, j)
              :array.set(j, val, acc_cur)
            end)

          cur
        end)
      else
        prev
      end

    :array.get(n - 1, final_prev)
  end
end
```
