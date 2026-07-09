# 1649. Create Sorted Array through Instructions

## Cpp

```cpp
class Solution {
public:
    int createSortedArray(vector<int>& instructions) {
        const int MOD = 1000000007;
        int maxVal = 0;
        for (int v : instructions) if (v > maxVal) maxVal = v;
        vector<int> bit(maxVal + 2, 0);
        auto update = [&](int idx) {
            for (; idx < (int)bit.size(); idx += idx & -idx)
                ++bit[idx];
        };
        auto query = [&](int idx) {
            int sum = 0;
            for (; idx > 0; idx -= idx & -idx)
                sum += bit[idx];
            return sum;
        };
        long long cost = 0;
        for (int i = 0; i < (int)instructions.size(); ++i) {
            int x = instructions[i];
            int less = query(x - 1);
            int greater = i - query(x);
            cost += min(less, greater);
            if (cost >= MOD) cost %= MOD;
            update(x);
        }
        return (int)(cost % MOD);
    }
};
```

## Java

```java
class Solution {
    private static final int MOD = 1_000_000_007;
    public int createSortedArray(int[] instructions) {
        int maxVal = 0;
        for (int v : instructions) if (v > maxVal) maxVal = v;
        Fenwick fenwick = new Fenwick(maxVal + 2);
        long cost = 0;
        int inserted = 0;
        for (int x : instructions) {
            int less = fenwick.query(x - 1);
            int greater = inserted - fenwick.query(x);
            cost += Math.min(less, greater);
            if (cost >= MOD) cost %= MOD;
            fenwick.update(x, 1);
            inserted++;
        }
        return (int)(cost % MOD);
    }

    private static class Fenwick {
        int n;
        int[] bit;
        Fenwick(int size) {
            n = size;
            bit = new int[n + 1];
        }
        void update(int idx, int delta) {
            for (int i = idx; i <= n; i += i & -i) {
                bit[i] += delta;
            }
        }
        int query(int idx) {
            int sum = 0;
            for (int i = idx; i > 0; i -= i & -i) {
                sum += bit[i];
            }
            return sum;
        }
    }
}
```

## Python

```python
class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7

        class Fenwick:
            __slots__ = ('n', 'bit')
            def __init__(self, n):
                self.n = n
                self.bit = [0] * (n + 1)
            def update(self, i, delta):
                while i <= self.n:
                    self.bit[i] += delta
                    i += i & -i
            def query(self, i):
                s = 0
                while i > 0:
                    s += self.bit[i]
                    i -= i & -i
                return s

        max_val = max(instructions)
        ft = Fenwick(max_val + 2)

        total_cost = 0
        for idx, val in enumerate(instructions):
            less = ft.query(val - 1)
            greater = idx - ft.query(val)   # numbers already inserted minus those <= val
            total_cost += min(less, greater)
            if total_cost >= MOD:
                total_cost %= MOD
            ft.update(val, 1)

        return total_cost % MOD
```

## Python3

```python
from typing import List

class FenwickTree:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, idx: int, delta: int) -> None:
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def query(self, idx: int) -> int:
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & -idx
        return s

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        max_val = max(instructions)
        ft = FenwickTree(max_val + 2)  # extra space for safety
        total_cost = 0
        inserted = 0

        for x in instructions:
            left = ft.query(x - 1)          # count of elements < x
            right = inserted - ft.query(x)   # count of elements > x
            total_cost += min(left, right)
            if total_cost >= MOD:
                total_cost %= MOD
            ft.update(x, 1)
            inserted += 1

        return total_cost % MOD
```

## C

```c
#include <stdlib.h>

static void bitAdd(int *bit, int n, int idx, int val) {
    while (idx <= n) {
        bit[idx] += val;
        idx += idx & -idx;
    }
}

static int bitSum(int *bit, int idx) {
    int res = 0;
    while (idx > 0) {
        res += bit[idx];
        idx -= idx & -idx;
    }
    return res;
}

int createSortedArray(int* instructions, int instructionsSize){
    const int MOD = 1000000007;
    if (instructionsSize == 0) return 0;

    int maxVal = 0;
    for (int i = 0; i < instructionsSize; ++i)
        if (instructions[i] > maxVal) maxVal = instructions[i];

    int size = maxVal + 2;               // BIT indices from 1..maxVal
    int *bit = (int*)calloc(size, sizeof(int));
    long long cost = 0;

    for (int i = 0; i < instructionsSize; ++i) {
        int x = instructions[i];
        int less = bitSum(bit, x - 1);
        int greater = i - bitSum(bit, x);   // i elements already inserted
        cost += (less < greater ? less : greater);
        if (cost >= MOD) cost %= MOD;
        bitAdd(bit, size - 1, x, 1);
    }

    free(bit);
    return (int)(cost % MOD);
}
```

## Csharp

```csharp
using System;

public class Solution
{
    private const int MOD = 1000000007;

    public int CreateSortedArray(int[] instructions)
    {
        int maxVal = 0;
        foreach (int v in instructions)
            if (v > maxVal) maxVal = v;

        FenwickTree ft = new FenwickTree(maxVal + 2);
        long cost = 0;

        for (int i = 0; i < instructions.Length; i++)
        {
            int x = instructions[i];
            int less = ft.Query(x - 1);
            int greater = i - ft.Query(x); // elements already inserted minus those <= x
            cost += Math.Min(less, greater);
            if (cost >= MOD) cost %= MOD;
            ft.Update(x, 1);
        }

        return (int)(cost % MOD);
    }

    private class FenwickTree
    {
        private readonly int[] tree;

        public FenwickTree(int size)
        {
            tree = new int[size];
        }

        public void Update(int index, int delta)
        {
            for (int i = index; i < tree.Length; i += i & -i)
                tree[i] += delta;
        }

        public int Query(int index)
        {
            int sum = 0;
            for (int i = index; i > 0; i -= i & -i)
                sum += tree[i];
            return sum;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} instructions
 * @return {number}
 */
var createSortedArray = function(instructions) {
    const MOD = 1000000007;
    const MAX_VAL = 100000; // given constraints
    
    class Fenwick {
        constructor(n) {
            this.n = n;
            this.tree = new Array(n + 2).fill(0);
        }
        update(i, delta) {
            for (let x = i; x <= this.n; x += x & -x) {
                this.tree[x] += delta;
            }
        }
        query(i) {
            let sum = 0;
            for (let x = i; x > 0; x -= x & -x) {
                sum += this.tree[x];
            }
            return sum;
        }
    }
    
    const bit = new Fenwick(MAX_VAL);
    let cost = 0;
    
    for (let i = 0; i < instructions.length; ++i) {
        const val = instructions[i];
        const less = bit.query(val - 1);
        const notGreater = bit.query(val); // count of elements <= val
        const greater = i - notGreater;   // total inserted so far is i
        cost += Math.min(less, greater);
        if (cost >= MOD) cost %= MOD;
        bit.update(val, 1);
    }
    
    return cost % MOD;
};
```

## Typescript

```typescript
function createSortedArray(instructions: number[]): number {
    const MOD = 1000000007;
    let maxVal = 0;
    for (const v of instructions) if (v > maxVal) maxVal = v;
    const bit = new Fenwick(maxVal + 2);
    let cost = 0;
    let processed = 0;
    for (const val of instructions) {
        const less = bit.query(val - 1);
        const greater = processed - less;
        cost = (cost + Math.min(less, greater)) % MOD;
        bit.update(val, 1);
        processed++;
    }
    return cost;
}

class Fenwick {
    private tree: number[];
    private n: number;
    constructor(n: number) {
        this.n = n;
        this.tree = new Array(n + 2).fill(0);
    }
    update(i: number, delta: number): void {
        while (i <= this.n) {
            this.tree[i] += delta;
            i += i & -i;
        }
    }
    query(i: number): number {
        let sum = 0;
        while (i > 0) {
            sum += this.tree[i];
            i -= i & -i;
        }
        return sum;
    }
}
```

## Php

```php
<?php
class Fenwick {
    public $tree;
    public $size;
    public function __construct($n) {
        $this->size = $n;
        $this->tree = array_fill(0, $n + 2, 0);
    }
    public function update($index, $delta) {
        for ($i = $index; $i <= $this->size; $i += $i & (-$i)) {
            $this->tree[$i] += $delta;
        }
    }
    public function query($index) {
        $sum = 0;
        for ($i = $index; $i > 0; $i -= $i & (-$i)) {
            $sum += $this->tree[$i];
        }
        return $sum;
    }
}
class Solution {

    /**
     * @param Integer[] $instructions
     * @return Integer
     */
    function createSortedArray($instructions) {
        $mod = 1000000007;
        if (empty($instructions)) {
            return 0;
        }
        $maxVal = max($instructions);
        $bit = new Fenwick($maxVal + 2);
        $cost = 0;
        $processed = 0;
        foreach ($instructions as $x) {
            $less = $bit->query($x - 1);
            $greater = $processed - $bit->query($x);
            $cost += min($less, $greater);
            if ($cost >= $mod) {
                $cost %= $mod;
            }
            $bit->update($x, 1);
            $processed++;
        }
        return $cost % $mod;
    }
}
?>
```

## Swift

```swift
class Solution {
    func createSortedArray(_ instructions: [Int]) -> Int {
        let MOD = 1_000_000_007
        let maxVal = 100_000
        var bit = FenwickTree(size: maxVal + 2)
        var totalInserted = 0
        var cost: Int64 = 0
        
        for val in instructions {
            let left = bit.query(val - 1)                 // count of elements < val
            let right = totalInserted - bit.query(val)    // count of elements > val
            cost += Int64(min(left, right))
            if cost >= Int64(MOD) { cost %= Int64(MOD) }
            bit.update(val, delta: 1)
            totalInserted += 1
        }
        return Int(cost % Int64(MOD))
    }
}

struct FenwickTree {
    let size: Int
    var tree: [Int]
    
    init(size: Int) {
        self.size = size
        self.tree = Array(repeating: 0, count: size + 1)
    }
    
    mutating func update(_ index: Int, delta: Int) {
        var i = index
        while i <= size {
            tree[i] += delta
            i += i & -i
        }
    }
    
    func query(_ index: Int) -> Int {
        if index <= 0 { return 0 }
        var i = index
        var res = 0
        while i > 0 {
            res += tree[i]
            i -= i & -i
        }
        return res
    }
}
```

## Kotlin

```kotlin
class Solution {
    private val MOD = 1_000_000_007L
    private class Fenwick(val n: Int) {
        private val tree = IntArray(n + 2)
        fun update(idx: Int, delta: Int) {
            var i = idx
            while (i <= n) {
                tree[i] += delta
                i += i and -i
            }
        }

        fun query(idx: Int): Int {
            var res = 0
            var i = idx
            while (i > 0) {
                res += tree[i]
                i -= i and -i
            }
            return res
        }
    }

    fun createSortedArray(instructions: IntArray): Int {
        if (instructions.isEmpty()) return 0
        val maxVal = instructions.maxOrNull() ?: 0
        val bit = Fenwick(maxVal + 2)
        var totalInserted = 0
        var cost = 0L
        for (v in instructions) {
            val less = bit.query(v - 1)
            val greater = totalInserted - bit.query(v)
            cost += kotlin.math.min(less, greater).toLong()
            if (cost >= MOD) cost %= MOD
            bit.update(v, 1)
            totalInserted++
        }
        return (cost % MOD).toInt()
    }
}
```

## Golang

```go
func createSortedArray(instructions []int) int {
	const MOD = 1000000007
	maxVal := 0
	for _, v := range instructions {
		if v > maxVal {
			maxVal = v
		}
	}
	bit := make([]int, maxVal+2)

	update := func(idx, delta int) {
		for idx < len(bit) {
			bit[idx] += delta
			idx += idx & -idx
		}
	}
	query := func(idx int) int {
		sum := 0
		for idx > 0 {
			sum += bit[idx]
			idx -= idx & -idx
		}
		return sum
	}

	totalInserted := 0
	var cost int64
	for _, v := range instructions {
		less := query(v - 1)
		greater := totalInserted - query(v)
		if less < greater {
			cost += int64(less)
		} else {
			cost += int64(greater)
		}
		update(v, 1)
		totalInserted++
	}
	return int(cost % MOD)
}
```

## Ruby

```ruby
def create_sorted_array(instructions)
  mod = 1_000_000_007
  max_val = instructions.max
  size = max_val + 2
  bit = Array.new(size, 0)

  update = lambda do |i, delta|
    while i < size
      bit[i] += delta
      i += i & -i
    end
  end

  query = lambda do |i|
    sum = 0
    while i > 0
      sum += bit[i]
      i -= i & -i
    end
    sum
  end

  total = 0
  processed = 0
  instructions.each do |x|
    less = query.call(x - 1)
    greater = processed - query.call(x)
    total += less < greater ? less : greater
    total %= mod
    update.call(x, 1)
    processed += 1
  end

  total % mod
end
```

## Scala

```scala
object Solution {
    def createSortedArray(instructions: Array[Int]): Int = {
        val MOD = 1000000007L
        if (instructions.isEmpty) return 0
        val maxVal = instructions.max

        class BIT(val size: Int) {
            private val tree = new Array[Int](size + 2)
            def update(idx: Int, delta: Int): Unit = {
                var i = idx
                while (i <= size) {
                    tree(i) += delta
                    i += i & -i
                }
            }
            def query(idx: Int): Int = {
                var sum = 0
                var i = idx
                while (i > 0) {
                    sum += tree(i)
                    i -= i & -i
                }
                sum
            }
        }

        val bit = new BIT(maxVal + 2)
        var total: Long = 0L
        var inserted = 0

        for (x <- instructions) {
            val less = if (x > 1) bit.query(x - 1) else 0
            val leq = bit.query(x)
            val greater = inserted - leq
            total += Math.min(less, greater)
            if (total >= MOD) total %= MOD
            bit.update(x, 1)
            inserted += 1
        }

        (total % MOD).toInt
    }
}
```

## Rust

```rust
impl Solution {
    pub fn create_sorted_array(instructions: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let max_val = *instructions.iter().max().unwrap() as usize;

        struct Fenwick {
            tree: Vec<i32>,
        }
        impl Fenwick {
            fn new(size: usize) -> Self {
                Fenwick { tree: vec![0; size + 1] }
            }
            fn update(&mut self, mut idx: usize, delta: i32) {
                let n = self.tree.len();
                while idx < n {
                    self.tree[idx] += delta;
                    idx += idx & (!idx + 1);
                }
            }
            fn query(&self, mut idx: usize) -> i32 {
                let mut sum = 0;
                while idx > 0 {
                    sum += self.tree[idx];
                    idx &= idx - 1;
                }
                sum
            }
        }

        let mut bit = Fenwick::new(max_val + 2);
        let mut cost: i64 = 0;

        for (i, &v) in instructions.iter().enumerate() {
            let x = v as usize;
            let less = bit.query(x - 1) as i64;
            let leq = bit.query(x) as i64;
            let total_inserted = i as i64;
            let greater = total_inserted - leq;
            cost += std::cmp::min(less, greater);
            if cost >= MOD {
                cost %= MOD;
            }
            bit.update(x, 1);
        }

        (cost % MOD) as i32
    }
}
```
