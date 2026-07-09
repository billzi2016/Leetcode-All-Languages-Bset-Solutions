# 1569. Number of Ways to Reorder Array to Get Same BST

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
    static const int MOD = 1'000'000'007;
    vector<long long> fact, invFact;
    
    long long modPow(long long a, long long e) {
        long long r = 1;
        while (e) {
            if (e & 1) r = r * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return r;
    }
    
    long long C(int n, int k) {
        if (k < 0 || k > n) return 0;
        return fact[n] * invFact[k] % MOD * invFact[n - k] % MOD;
    }
    
    long long dfs(const vector<int>& nums) {
        int m = nums.size();
        if (m <= 2) return 1;
        vector<int> left, right;
        left.reserve(m);
        right.reserve(m);
        for (int i = 1; i < m; ++i) {
            if (nums[i] < nums[0]) left.push_back(nums[i]);
            else right.push_back(nums[i]);
        }
        long long waysLeft = dfs(left);
        long long waysRight = dfs(right);
        long long comb = C((int)left.size() + (int)right.size(), (int)left.size());
        return ((comb * waysLeft) % MOD) * waysRight % MOD;
    }
    
public:
    int numOfWays(vector<int>& nums) {
        int n = nums.size();
        fact.resize(n + 1);
        invFact.resize(n + 1);
        fact[0] = 1;
        for (int i = 1; i <= n; ++i) fact[i] = fact[i - 1] * i % MOD;
        invFact[n] = modPow(fact[n], MOD - 2);
        for (int i = n; i > 0; --i) invFact[i - 1] = invFact[i] * i % MOD;
        
        long long total = dfs(nums);
        total = (total - 1 + MOD) % MOD; // exclude original ordering
        return (int)total;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private long[][] comb;

    public int numOfWays(int[] nums) {
        int n = nums.length;
        buildComb(n);
        List<Integer> list = new ArrayList<>(n);
        for (int v : nums) list.add(v);
        long ways = dfs(list);
        ways = (ways - 1 + MOD) % MOD; // exclude original ordering
        return (int) ways;
    }

    private void buildComb(int n) {
        comb = new long[n + 1][n + 1];
        for (int i = 0; i <= n; i++) {
            comb[i][0] = comb[i][i] = 1;
            for (int j = 1; j < i; j++) {
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD;
            }
        }
    }

    private long dfs(List<Integer> nodes) {
        int size = nodes.size();
        if (size <= 2) return 1L;

        int root = nodes.get(0);
        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();

        for (int i = 1; i < size; i++) {
            int v = nodes.get(i);
            if (v < root) left.add(v);
            else right.add(v);
        }

        long leftWays = dfs(left);
        long rightWays = dfs(right);
        long waysCombine = comb[size - 1][left.size()];

        return (((waysCombine * leftWays) % MOD) * rightWays) % MOD;
    }
}
```

## Python

```python
import sys

class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        # precompute binomial coefficients up to n
        comb = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            comb[i][0] = comb[i][i] = 1
            for j in range(1, i):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

        sys.setrecursionlimit(2000)

        def dfs(arr):
            m = len(arr)
            if m <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            left_ways = dfs(left)
            right_ways = dfs(right)
            total = comb[m - 1][len(left)]
            total = (total * left_ways) % MOD
            total = (total * right_ways) % MOD
            return total

        result = dfs(nums) - 1
        return result % MOD
```

## Python3

```python
import sys

sys.setrecursionlimit(3000)

class Solution:
    def numOfWays(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        def nCr(N, R):
            if R < 0 or R > N:
                return 0
            return fact[N] * inv_fact[R] % MOD * inv_fact[N - R] % MOD

        def dfs(arr):
            m = len(arr)
            if m <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            ways_left = dfs(left)
            ways_right = dfs(right)
            comb = nCr(m - 1, len(left))
            return comb * ways_left % MOD * ways_right % MOD

        return (dfs(nums) - 1) % MOD
```

## C

```c
#include <stdlib.h>

#define MOD 1000000007

static long long C[1001][1001];

static long long dfs(const int *arr, int n) {
    if (n <= 2) return 1;
    int root = arr[0];
    int *left = (int *)malloc((n - 1) * sizeof(int));
    int *right = (int *)malloc((n - 1) * sizeof(int));
    int l = 0, r = 0;
    for (int i = 1; i < n; ++i) {
        if (arr[i] < root)
            left[l++] = arr[i];
        else
            right[r++] = arr[i];
    }
    long long leftWays = dfs(left, l);
    long long rightWays = dfs(right, r);
    free(left);
    free(right);
    long long ways = C[n - 1][l];
    ways = (ways * leftWays) % MOD;
    ways = (ways * rightWays) % MOD;
    return ways;
}

int numOfWays(int* nums, int numsSize) {
    for (int i = 0; i <= numsSize; ++i) {
        C[i][0] = C[i][i] = 1;
        for (int j = 1; j < i; ++j) {
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
        }
    }
    long long total = dfs(nums, numsSize);
    int result = (int)((total - 1 + MOD) % MOD);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    private const int MOD = 1000000007;
    private long[,] _comb;

    public int NumOfWays(int[] nums)
    {
        int n = nums.Length;
        _comb = new long[n + 1, n + 1];
        for (int i = 0; i <= n; i++)
        {
            _comb[i, 0] = 1;
            _comb[i, i] = 1;
            for (int j = 1; j < i; j++)
            {
                _comb[i, j] = (_comb[i - 1, j - 1] + _comb[i - 1, j]) % MOD;
            }
        }

        var list = new List<int>(nums);
        long totalWays = Dfs(list);
        int result = (int)((totalWays - 1 + MOD) % MOD);
        return result;
    }

    private long Dfs(List<int> seq)
    {
        if (seq.Count <= 2) return 1;

        var left = new List<int>();
        var right = new List<int>();
        int root = seq[0];

        for (int i = 1; i < seq.Count; i++)
        {
            if (seq[i] < root)
                left.Add(seq[i]);
            else
                right.Add(seq[i]);
        }

        long leftWays = Dfs(left);
        long rightWays = Dfs(right);

        int m = seq.Count - 1;          // total nodes excluding root
        int k = left.Count;             // nodes in left subtree

        long ways = _comb[m, k];
        ways = (ways * leftWays) % MOD;
        ways = (ways * rightWays) % MOD;

        return ways;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var numOfWays = function(nums) {
    const MOD = 1000000007n;
    const n = nums.length;

    // precompute factorials and inverse factorials modulo MOD
    const fact = new Array(n + 1);
    const invFact = new Array(n + 1);
    fact[0] = 1n;
    for (let i = 1; i <= n; ++i) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }
    const modPow = (base, exp) => {
        let result = 1n;
        let b = base % MOD;
        let e = exp;
        while (e > 0n) {
            if (e & 1n) result = (result * b) % MOD;
            b = (b * b) % MOD;
            e >>= 1n;
        }
        return result;
    };
    invFact[n] = modPow(fact[n], MOD - 2n);
    for (let i = n; i >= 1; --i) {
        invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;
    }
    const comb = (nn, kk) => {
        if (kk < 0 || kk > nn) return 0n;
        return (((fact[nn] * invFact[kk]) % MOD) * invFact[nn - kk]) % MOD;
    };

    const dfs = (arr) => {
        const m = arr.length;
        if (m <= 2) return 1n; // only one ordering
        const root = arr[0];
        const left = [];
        const right = [];
        for (let i = 1; i < m; ++i) {
            const v = arr[i];
            if (v < root) left.push(v);
            else right.push(v);
        }
        const leftWays = dfs(left);
        const rightWays = dfs(right);
        const waysMerge = comb(m - 1, left.length);
        let res = (waysMerge * leftWays) % MOD;
        res = (res * rightWays) % MOD;
        return res;
    };

    const total = dfs(nums);
    const answer = (total - 1n + MOD) % MOD; // exclude original ordering
    return Number(answer);
};
```

## Typescript

```typescript
function numOfWays(nums: number[]): number {
    const MOD = 1000000007n;
    const n = nums.length;
    const comb: bigint[][] = Array.from({ length: n + 1 }, () => Array(n + 1).fill(0n));
    for (let i = 0; i <= n; i++) {
        comb[i][0] = 1n;
        comb[i][i] = 1n;
        for (let j = 1; j < i; j++) {
            comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD;
        }
    }

    function dfs(arr: number[]): bigint {
        const m = arr.length;
        if (m <= 2) return 1n;
        const root = arr[0];
        const left: number[] = [];
        const right: number[] = [];
        for (let i = 1; i < m; i++) {
            if (arr[i] < root) left.push(arr[i]);
            else right.push(arr[i]);
        }
        const leftWays = dfs(left);
        const rightWays = dfs(right);
        let res = comb[m - 1][left.length];
        res = (res * leftWays) % MOD;
        res = (res * rightWays) % MOD;
        return res;
    }

    const total = dfs(nums);
    const ans = (total - 1n + MOD) % MOD;
    return Number(ans);
}
```

## Php

```php
class Solution {
    const MOD = 1000000007;
    private $fact = [];
    private $invFact = [];

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function numOfWays($nums) {
        $n = count($nums);
        $this->precompute($n);
        $ans = $this->dfs($nums);
        $ans = ($ans - 1 + self::MOD) % self::MOD;
        return $ans;
    }

    private function precompute(int $n): void {
        $this->fact = array_fill(0, $n + 1, 1);
        for ($i = 1; $i <= $n; $i++) {
            $this->fact[$i] = (int)(($this->fact[$i - 1] * $i) % self::MOD);
        }
        $this->invFact = array_fill(0, $n + 1, 1);
        $this->invFact[$n] = $this->modPow($this->fact[$n], self::MOD - 2);
        for ($i = $n; $i > 0; $i--) {
            $this->invFact[$i - 1] = (int)(($this->invFact[$i] * $i) % self::MOD);
        }
    }

    private function modPow(int $base, int $exp): int {
        $mod = self::MOD;
        $result = 1;
        $base %= $mod;
        while ($exp > 0) {
            if ($exp & 1) {
                $result = (int)(($result * $base) % $mod);
            }
            $base = (int)(($base * $base) % $mod);
            $exp >>= 1;
        }
        return $result;
    }

    private function nCr(int $n, int $k): int {
        if ($k < 0 || $k > $n) return 0;
        $res = $this->fact[$n];
        $res = (int)(($res * $this->invFact[$k]) % self::MOD);
        $res = (int)(($res * $this->invFact[$n - $k]) % self::MOD);
        return $res;
    }

    private function dfs(array $nums): int {
        $len = count($nums);
        if ($len <= 2) return 1;

        $root = $nums[0];
        $left = [];
        $right = [];

        for ($i = 1; $i < $len; $i++) {
            if ($nums[$i] < $root) {
                $left[] = $nums[$i];
            } else {
                $right[] = $nums[$i];
            }
        }

        $waysLeft = $this->dfs($left);
        $waysRight = $this->dfs($right);
        $comb = $this->nCr($len - 1, count($left));

        $ans = (int)((($comb * $waysLeft) % self::MOD) * $waysRight % self::MOD);
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    private let MOD: Int64 = 1_000_000_007
    private var fact: [Int64] = []
    private var invFact: [Int64] = []

    func numOfWays(_ nums: [Int]) -> Int {
        let n = nums.count
        // precompute factorials and inverse factorials
        fact = Array(repeating: 0, count: n + 1)
        invFact = Array(repeating: 0, count: n + 1)
        fact[0] = 1
        if n > 0 {
            for i in 1...n {
                fact[i] = (fact[i - 1] * Int64(i)) % MOD
            }
            invFact[n] = modPow(fact[n], MOD - 2)
            if n > 0 {
                for i in stride(from: n, through: 1, by: -1) {
                    invFact[i - 1] = (invFact[i] * Int64(i)) % MOD
                }
            }
        }

        let totalWays = dfs(nums)
        var answer = (totalWays - 1) % MOD
        if answer < 0 { answer += MOD }
        return Int(answer)
    }

    private func dfs(_ arr: [Int]) -> Int64 {
        let m = arr.count
        if m <= 2 { return 1 }
        let root = arr[0]
        var left: [Int] = []
        var right: [Int] = []
        left.reserveCapacity(m)
        right.reserveCapacity(m)
        for i in 1..<m {
            let v = arr[i]
            if v < root {
                left.append(v)
            } else {
                right.append(v)
            }
        }
        let leftWays = dfs(left)
        let rightWays = dfs(right)
        let combVal = combination(m - 1, left.count)
        var res = combVal
        res = (res * leftWays) % MOD
        res = (res * rightWays) % MOD
        return res
    }

    private func combination(_ n: Int, _ k: Int) -> Int64 {
        if k < 0 || k > n { return 0 }
        return (((fact[n] * invFact[k]) % MOD) * invFact[n - k]) % MOD
    }

    private func modPow(_ base: Int64, _ exp: Int64) -> Int64 {
        var result: Int64 = 1
        var b = base % MOD
        var e = exp
        while e > 0 {
            if (e & 1) == 1 {
                result = (result * b) % MOD
            }
            b = (b * b) % MOD
            e >>= 1
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1_000_000_007L
    private lateinit var fact: LongArray
    private lateinit var invFact: LongArray

    fun numOfWays(nums: IntArray): Int {
        precompute(nums.size)
        val totalWays = dfs(nums.toList())
        val ans = (totalWays - 1 + MOD) % MOD
        return ans.toInt()
    }

    private fun precompute(n: Int) {
        fact = LongArray(n + 1)
        invFact = LongArray(n + 1)
        fact[0] = 1L
        for (i in 1..n) {
            fact[i] = fact[i - 1] * i % MOD
        }
        invFact[n] = modPow(fact[n], MOD - 2)
        for (i in n downTo 1) {
            invFact[i - 1] = invFact[i] * i % MOD
        }
    }

    private fun binom(n: Int, k: Int): Long {
        if (k < 0 || k > n) return 0L
        return fact[n] * invFact[k] % MOD * invFact[n - k] % MOD
    }

    private fun modPow(base: Long, exp: Long): Long {
        var b = base % MOD
        var e = exp
        var res = 1L
        while (e > 0) {
            if ((e and 1L) == 1L) res = res * b % MOD
            b = b * b % MOD
            e = e shr 1
        }
        return res
    }

    private fun dfs(list: List<Int>): Long {
        val size = list.size
        if (size <= 2) return 1L
        val root = list[0]
        val left = mutableListOf<Int>()
        val right = mutableListOf<Int>()
        for (i in 1 until size) {
            val v = list[i]
            if (v < root) left.add(v) else right.add(v)
        }
        val leftWays = dfs(left)
        val rightWays = dfs(right)
        val comb = binom(left.size + right.size, left.size)
        return ((comb * leftWays % MOD) * rightWays) % MOD
    }
}
```

## Dart

```dart
import 'dart:math';

class Solution {
  static const int _mod = 1000000007;
  late List<int> _fact;
  late List<int> _invFact;

  int numOfWays(List<int> nums) {
    int n = nums.length;
    _precomputeFactorials(n);
    int totalWays = _dfs(nums);
    int result = (totalWays - 1) % _mod;
    if (result < 0) result += _mod;
    return result;
  }

  void _precomputeFactorials(int n) {
    _fact = List.filled(n + 1, 1);
    for (int i = 1; i <= n; i++) {
      _fact[i] = (_fact[i - 1] * i) % _mod;
    }
    _invFact = List.filled(n + 1, 1);
    _invFact[n] = _modPow(_fact[n], _mod - 2);
    for (int i = n; i > 0; i--) {
      _invFact[i - 1] = (_invFact[i] * i) % _mod;
    }
  }

  int _comb(int n, int k) {
    if (k < 0 || k > n) return 0;
    return (((_fact[n] * _invFact[k]) % _mod) * _invFact[n - k]) % _mod;
  }

  int _dfs(List<int> arr) {
    int len = arr.length;
    if (len <= 2) return 1;
    List<int> left = [];
    List<int> right = [];
    int root = arr[0];
    for (int i = 1; i < len; i++) {
      if (arr[i] < root) {
        left.add(arr[i]);
      } else {
        right.add(arr[i]);
      }
    }
    int leftWays = _dfs(left);
    int rightWays = _dfs(right);
    int ways = _comb(len - 1, left.length);
    ways = ((ways * leftWays) % _mod * rightWays) % _mod;
    return ways;
  }

  int _modPow(int base, int exp) {
    int result = 1;
    int b = base % _mod;
    while (exp > 0) {
      if ((exp & 1) == 1) {
        result = (result * b) % _mod;
      }
      b = (b * b) % _mod;
      exp >>= 1;
    }
    return result;
  }
}
```

## Golang

```go
package main

import "fmt"

const MOD int64 = 1000000007

var comb [][]int64

func initComb(n int) {
	comb = make([][]int64, n+1)
	for i := 0; i <= n; i++ {
		comb[i] = make([]int64, i+1)
		comb[i][0] = 1
		comb[i][i] = 1
		for j := 1; j < i; j++ {
			comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD
		}
	}
}

func dfs(nums []int) int64 {
	if len(nums) <= 2 {
		return 1
	}
	root := nums[0]
	left := make([]int, 0)
	right := make([]int, 0)
	for _, v := range nums[1:] {
		if v < root {
			left = append(left, v)
		} else {
			right = append(right, v)
		}
	}
	leftWays := dfs(left) % MOD
	rightWays := dfs(right) % MOD
	ways := (comb[len(nums)-1][len(left)] * ((leftWays * rightWays) % MOD)) % MOD
	return ways
}

func numOfWays(nums []int) int {
	initComb(len(nums))
	ans := dfs(nums)
	ans = (ans - 1 + MOD) % MOD
	return int(ans)
}

// The following main function is only for local testing and will be ignored by LeetCode.
func main() {
	fmt.Println(numOfWays([]int{2, 1, 3}))          // 1
	fmt.Println(numOfWays([]int{3, 4, 5, 1, 2}))   // 5
	fmt.Println(numOfWays([]int{1, 2, 3}))          // 0
}
```

## Ruby

```ruby
MOD = 1_000_000_007

def mod_pow(a, e, mod)
  res = 1
  base = a % mod
  while e > 0
    res = (res * base) % mod if (e & 1) == 1
    base = (base * base) % mod
    e >>= 1
  end
  res
end

# @param {Integer[]} nums
# @return {Integer}
def num_of_ways(nums)
  n = nums.length
  $fact = Array.new(n + 1, 1)
  (1..n).each { |i| $fact[i] = ($fact[i - 1] * i) % MOD }
  $inv_fact = Array.new(n + 1, 1)
  $inv_fact[n] = mod_pow($fact[n], MOD - 2, MOD)
  (n - 1).downto(0) { |i| $inv_fact[i] = ($inv_fact[i + 1] * (i + 1)) % MOD }

  helper = nil
  helper = ->(arr) do
    return 1 if arr.length <= 2

    root = arr[0]
    left = []
    right = []

    arr[1..-1].each do |v|
      if v < root
        left << v
      else
        right << v
      end
    end

    left_ways = helper.call(left)
    right_ways = helper.call(right)

    comb = $fact[arr.length - 1]
    comb = (comb * $inv_fact[left.length]) % MOD
    comb = (comb * $inv_fact[(arr.length - 1) - left.length]) % MOD

    ((comb * left_ways) % MOD * right_ways) % MOD
  end

  ans = helper.call(nums)
  (ans - 1) % MOD
end
```

## Scala

```scala
object Solution {
  private val MOD = 1000000007L

  def numOfWays(nums: Array[Int]): Int = {
    val n = nums.length
    val comb = Array.ofDim[Long](n + 1, n + 1)

    var i = 0
    while (i <= n) {
      comb(i)(0) = 1L
      comb(i)(i) = 1L
      var j = 1
      while (j < i) {
        comb(i)(j) = (comb(i - 1)(j - 1) + comb(i - 1)(j)) % MOD
        j += 1
      }
      i += 1
    }

    def dfs(arr: Array[Int]): Long = {
      val m = arr.length
      if (m <= 2) return 1L

      val root = arr(0)
      val leftBuf = new scala.collection.mutable.ArrayBuffer[Int]()
      val rightBuf = new scala.collection.mutable.ArrayBuffer[Int]()

      var idx = 1
      while (idx < m) {
        val v = arr(idx)
        if (v < root) leftBuf += v else rightBuf += v
        idx += 1
      }

      val leftArr = leftBuf.toArray
      val rightArr = rightBuf.toArray

      val leftWays = dfs(leftArr)
      val rightWays = dfs(rightArr)

      val ways = comb(m - 1)(leftArr.length)
      ((ways * leftWays) % MOD * rightWays) % MOD
    }

    val ans = (dfs(nums) - 1 + MOD) % MOD
    ans.toInt
  }
}
```

## Rust

```rust
impl Solution {
    pub fn num_of_ways(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len();
        // precompute binomial coefficients C[i][j] for 0 <= i,j <= n
        let mut comb = vec![vec![0i64; n + 1]; n + 1];
        for i in 0..=n {
            comb[i][0] = 1;
            comb[i][i] = 1;
            for j in 1..i {
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD;
            }
        }

        fn dfs(slice: &[i32], comb: &Vec<Vec<i64>>, modulo: i64) -> i64 {
            if slice.len() <= 2 {
                return 1;
            }
            let root = slice[0];
            let mut left = Vec::new();
            let mut right = Vec::new();
            for &v in &slice[1..] {
                if v < root {
                    left.push(v);
                } else {
                    right.push(v);
                }
            }
            let left_ways = dfs(&left, comb, modulo);
            let right_ways = dfs(&right, comb, modulo);
            let l = left.len();
            let r = right.len();
            (comb[l + r][l] * left_ways % modulo) * right_ways % modulo
        }

        let total = dfs(&nums, &comb, MOD);
        ((total - 1 + MOD) % MOD) as i32
    }
}
```

## Racket

```racket
(define MOD 1000000007)

;; build Pascal's triangle modulo MOD up to n
(define (build-comb n)
  (let ([c (make-vector (+ n 1) #f)])
    ;; initialize rows
    (for ([i (in-range (+ n 1))])
      (vector-set! c i (make-vector (+ n 1) 0))
      (vector-set! (vector-ref c i) 0 1)
      (vector-set! (vector-ref c i) i 1))
    ;; fill triangle
    (for ([i (in-range 2 (+ n 1))])
      (let ([row (vector-ref c i)]
            [prev (vector-ref c (- i 1))])
        (for ([j (in-range 1 i)])
          (let* ([val (+ (vector-ref prev (- j 1))
                         (vector-ref prev j))]
                 [val-mod (modulo val MOD)])
            (vector-set! row j val-mod)))))
    c))

;; modular multiplication
(define (mul a b)
  (modulo (* a b) MOD))

;; recursive count of ways for a given list, using precomputed comb table
(define (dfs lst comb)
  (let ([len (length lst)])
    (if (< len 3)
        1
        (let* ([root (car lst)]
               [rest (cdr lst)]
               [left (filter (lambda (x) (< x root)) rest)]
               [right (filter (lambda (x) (> x root)) rest)]
               [left-ways (dfs left comb)]
               [right-ways (dfs right comb)]
               [comb-val (vector-ref (vector-ref comb (- len 1))
                                     (length left))]
               [res (mul comb-val left-ways)])
          (modulo (* res right-ways) MOD)))))

(define/contract (num-of-ways nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length nums)]
         [comb (build-comb n)]
         [total (dfs nums comb)])
    (modulo (- total 1) MOD)))
```

## Erlang

```erlang
-module(solution).
-export([num_of_ways/1]).

-define(MOD, 1000000007).

num_of_ways(Nums) ->
    N = length(Nums),
    {Fact, InvFact} = build_fact_inv(N, ?MOD),
    Ways = dfs(Nums, Fact, InvFact, ?MOD),
    (Ways - 1 + ?MOD) rem ?MOD.

%% ------------------------------------------------------------------
%% Recursive computation of number of ways
%% ------------------------------------------------------------------
dfs(List, Fact, InvFact, Mod) ->
    Len = length(List),
    case Len < 3 of
        true -> 1;
        false ->
            [Root|Rest] = List,
            {Left, Right} = partition(Rest, Root, [], []),
            LWays = dfs(Left, Fact, InvFact, Mod),
            RWays = dfs(Right, Fact, InvFact, Mod),
            LeftSize = length(Left),
            TotalMinus1 = Len - 1,
            Comb = comb(TotalMinus1, LeftSize, Fact, InvFact, Mod),
            ((Comb * LWays) rem Mod * RWays) rem Mod
    end.

comb(N, K, Fact, InvFact, Mod) ->
    F = element(N+1, Fact),
    I1 = element(K+1, InvFact),
    I2 = element(N-K+1, InvFact),
    ((F * I1) rem Mod * I2) rem Mod.

%% ------------------------------------------------------------------
%% Partition remaining elements into left/right subtrees preserving order
%% ------------------------------------------------------------------
partition([], _Root, LAcc, RAcc) ->
    {lists:reverse(LAcc), lists:reverse(RAcc)};
partition([X|Xs], Root, LAcc, RAcc) ->
    if X < Root ->
            partition(Xs, Root, [X|LAcc], RAcc);
       true ->
            partition(Xs, Root, LAcc, [X|RAcc])
    end.

%% ------------------------------------------------------------------
%% Precompute factorials and inverse factorials
%% ------------------------------------------------------------------
build_fact_inv(N, Mod) ->
    FactList = build_fact_list(N, Mod),
    {FactTuple, InvFactTuple} = build_inv_fact(FactList, N, Mod),
    {FactTuple, InvFactTuple}.

build_fact_list(N, Mod) -> build_fact_list(0, N, Mod, [1]).
build_fact_list(I, N, _Mod, Acc) when I == N ->
    lists:reverse(Acc);
build_fact_list(I, N, Mod, Acc) ->
    Prev = hd(Acc),
    New = (Prev * (I+1)) rem Mod,
    build_fact_list(I+1, N, Mod, [New|Acc]).

build_inv_fact(FactList, N, Mod) ->
    FactTuple = list_to_tuple(FactList),
    InvN = pow_mod(element(N+1, FactTuple), Mod-2, Mod),
    InvFactList = build_inv_desc(N, InvN, [], FactTuple, Mod),
    {FactTuple, list_to_tuple(InvFactList)}.

build_inv_desc(0, InvCurr, Acc, _FactTuple, _Mod) ->
    lists:reverse([InvCurr|Acc]);
build_inv_desc(I, InvCurr, Acc, FactTuple, Mod) when I > 0 ->
    NewAcc = [InvCurr | Acc],
    InvPrev = (InvCurr * I) rem Mod,
    build_inv_desc(I-1, InvPrev, NewAcc, FactTuple, Mod).

%% ------------------------------------------------------------------
%% Modular exponentiation
%% ------------------------------------------------------------------
pow_mod(_Base, 0, _Mod) -> 1;
pow_mod(Base, Exp, Mod) when Exp band 1 =:= 1 ->
    (Base * pow_mod((Base*Base) rem Mod, Exp bsr 1, Mod)) rem Mod;
pow_mod(Base, Exp, Mod) ->
    pow_mod((Base*Base) rem Mod, Exp bsr 1, Mod).
```

## Elixir

```elixir
defmodule Solution do
  @mod 1_000_000_007

  @spec num_of_ways(nums :: [integer]) :: integer
  def num_of_ways(nums) do
    n = length(nums)
    fact = build_fact(n)
    inv_fact = build_inv_fact(fact)
    ways = dfs(nums, fact, inv_fact)
    rem(ways - 1 + @mod, @mod)
  end

  defp build_fact(n) do
    {list_rev, _} =
      Enum.reduce(0..n, {[], 1}, fn i, {acc, prev} ->
        cur = if i == 0, do: 1, else: rem(prev * i, @mod)
        {[cur | acc], cur}
      end)

    Enum.reverse(list_rev)
  end

  defp build_inv_fact(fact) do
    n = length(fact) - 1
    inv_last = mod_pow(Enum.at(fact, n), @mod - 2)

    {list_rev, _} =
      Enum.reduce((n - 1)..0, {[], inv_last}, fn i, {acc, cur_next} ->
        cur = rem(cur_next * (i + 1), @mod)
        {[cur | acc], cur}
      end)

    [inv_last | list_rev] |> Enum.reverse()
  end

  defp mod_pow(_base, 0), do: 1

  defp mod_pow(base, exp) when exp > 0 do
    base = rem(base, @mod)

    if rem(exp, 2) == 0 do
      half = mod_pow(base, div(exp, 2))
      rem(half * half, @mod)
    else
      rem(base * mod_pow(base, exp - 1), @mod)
    end
  end

  defp comb(n, k, fact, inv_fact) do
    if k < 0 or k > n do
      0
    else
      res = Enum.at(fact, n)
      res = rem(res * Enum.at(inv_fact, k), @mod)
      res = rem(res * Enum.at(inv_fact, n - k), @mod)
      res
    end
  end

  defp dfs(nums, fact, inv_fact) do
    len = length(nums)

    if len < 3 do
      1
    else
      [root | rest] = nums

      {left, right} =
        Enum.split_with(rest, fn x -> x < root end)

      left_len = length(left)
      total = len - 1

      ways_left = dfs(left, fact, inv_fact)
      ways_right = dfs(right, fact, inv_fact)

      comb_val = comb(total, left_len, fact, inv_fact)

      res = rem(comb_val * ways_left, @mod)
      res = rem(res * ways_right, @mod)
      res
    end
  end
end
```
