# 1803. Count Pairs With XOR in a Range

## Cpp

```cpp
class Solution {
public:
    struct TrieNode {
        int child[2];
        int cnt;
        TrieNode() { child[0] = child[1] = -1; cnt = 0; }
    };
    
    class Trie {
    public:
        vector<TrieNode> nodes;
        static const int MAX_BIT = 14; // since nums[i], low, high <= 20000 < 2^15
        
        Trie() { nodes.emplace_back(); }
        
        void insert(int num) {
            int cur = 0;
            for (int i = MAX_BIT; i >= 0; --i) {
                int bit = (num >> i) & 1;
                if (nodes[cur].child[bit] == -1) {
                    nodes[cur].child[bit] = nodes.size();
                    nodes.emplace_back();
                }
                cur = nodes[cur].child[bit];
                ++nodes[cur].cnt;
            }
        }
        
        int countLessOrEqual(int num, int K) const {
            if (K < 0) return 0;
            int cur = 0;
            int res = 0;
            for (int i = MAX_BIT; i >= 0 && cur != -1; --i) {
                int nBit = (num >> i) & 1;
                int kBit = (K   >> i) & 1;
                if (kBit == 1) {
                    int childZero = nodes[cur].child[nBit];
                    if (childZero != -1) res += nodes[childZero].cnt;
                    cur = nodes[cur].child[1 - nBit];
                } else {
                    cur = nodes[cur].child[nBit];
                }
            }
            return res;
        }
    };
    
    int countPairs(vector<int>& nums, int low, int high) {
        long long ans = 0;
        Trie trie;
        for (size_t i = 0; i < nums.size(); ++i) {
            if (i > 0) {
                ans += trie.countLessOrEqual(nums[i], high);
                ans -= trie.countLessOrEqual(nums[i], low - 1);
            }
            trie.insert(nums[i]);
        }
        return static_cast<int>(ans);
    }
};
```

## Java

```java
class Solution {
    private static class TrieNode {
        TrieNode[] child = new TrieNode[2];
        int count;
    }

    private final TrieNode root = new TrieNode();
    private static final int MAX_BIT = 14; // since nums[i] <= 20000 < 2^15

    public int countPairs(int[] nums, int low, int high) {
        int ans = 0;
        for (int num : nums) {
            int cntHigh = query(num, high);
            int cntLowMinusOne = query(num, low - 1);
            ans += cntHigh - cntLowMinusOne;
            insert(num);
        }
        return ans;
    }

    private void insert(int num) {
        TrieNode node = root;
        for (int i = MAX_BIT; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (node.child[bit] == null) {
                node.child[bit] = new TrieNode();
            }
            node = node.child[bit];
            node.count++;
        }
    }

    private int query(int num, int K) {
        if (K < 0) return 0;
        TrieNode node = root;
        int cnt = 0;
        for (int i = MAX_BIT; i >= 0 && node != null; i--) {
            int bitNum = (num >> i) & 1;
            int bitK = (K >> i) & 1;
            if (bitK == 1) {
                TrieNode childZero = node.child[bitNum];
                if (childZero != null) cnt += childZero.count;
                node = node.child[1 - bitNum];
            } else {
                node = node.child[bitNum];
            }
        }
        if (node != null) cnt += node.count;
        return cnt;
    }
}
```

## Python

```python
class Solution(object):
    def countPairs(self, nums, low, high):
        """
        :type nums: List[int]
        :type low: int
        :type high: int
        :rtype: int
        """
        MAX_BIT = 14  # since nums[i] <= 20000 < 2^15

        class TrieNode:
            __slots__ = ('child', 'cnt')
            def __init__(self):
                self.child = [None, None]
                self.cnt = 0

        def insert(root, num):
            node = root
            for i in range(MAX_BIT, -1, -1):
                b = (num >> i) & 1
                if not node.child[b]:
                    node.child[b] = TrieNode()
                node = node.child[b]
                node.cnt += 1

        def query(root, num, K):
            node = root
            total = 0
            for i in range(MAX_BIT, -1, -1):
                if not node:
                    break
                b = (num >> i) & 1
                kbit = (K >> i) & 1
                if kbit == 1:
                    # add counts where xor bit is 0 (child matching b)
                    if node.child[b]:
                        total += node.child[b].cnt
                    # move to branch where xor bit is 1
                    node = node.child[1 - b]
                else:
                    # must take xor bit 0 path
                    node = node.child[b]
            return total

        def count_le(K):
            root = TrieNode()
            ans = 0
            for num in nums:
                ans += query(root, num, K)
                insert(root, num)
            return ans

        return count_le(high) - count_le(low - 1)
```

## Python3

```python
from typing import List

class TrieNode:
    __slots__ = ('children', 'cnt')
    def __init__(self):
        self.children = [None, None]
        self.cnt = 0

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        MAX_BIT = 15  # since nums[i] <= 20000 < 2^15
        
        def insert(root: TrieNode, num: int) -> None:
            node = root
            for i in range(MAX_BIT, -1, -1):
                b = (num >> i) & 1
                if not node.children[b]:
                    node.children[b] = TrieNode()
                node = node.children[b]
                node.cnt += 1

        def query(root: TrieNode, num: int, K: int) -> int:
            node = root
            cnt = 0
            for i in range(MAX_BIT, -1, -1):
                if not node:
                    break
                b = (num >> i) & 1
                k = (K >> i) & 1
                if k == 1:
                    # add all numbers where current xor bit is 0
                    child = node.children[b]
                    if child:
                        cnt += child.cnt
                    # move to branch where xor bit is 1 to continue matching K's prefix
                    node = node.children[1 - b]
                else:
                    # must keep xor bit 0
                    node = node.children[b]
            return cnt

        def count_le(K: int) -> int:
            root = TrieNode()
            total = 0
            for num in nums:
                total += query(root, num, K)
                insert(root, num)
            return total

        return count_le(high) - count_le(low - 1)
```

## C

```c
#include <stddef.h>

static const int MAX_BIT = 14;               // enough for values up to 2^15-1 (32767)

typedef struct {
    int child[2];
    int cnt;
} Node;

static long long countLE(const int *nums, int n, int K) {
    /* maximum nodes needed: (n+1)*(MAX_BIT+1) */
    static Node trie[400005];
    int nodeCnt = 1;                         // root is index 0
    trie[0].child[0] = trie[0].child[1] = -1;
    trie[0].cnt = 0;

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        int num = nums[i];

        /* query how many previous numbers give xor <= K */
        int node = 0;
        long long cur = 0;
        for (int b = MAX_BIT; b >= 0; --b) {
            if (node == -1) break;
            int nBit = (num >> b) & 1;
            int kBit = (K   >> b) & 1;
            if (kBit) {
                int sameChild = trie[node].child[nBit];
                if (sameChild != -1) cur += trie[sameChild].cnt;
                node = trie[node].child[1 ^ nBit];
            } else {
                node = trie[node].child[nBit];
            }
        }
        ans += cur;

        /* insert current number into the trie */
        node = 0;
        for (int b = MAX_BIT; b >= 0; --b) {
            int bit = (num >> b) & 1;
            if (trie[node].child[bit] == -1) {
                trie[node].child[bit] = nodeCnt;
                trie[nodeCnt].child[0] = trie[nodeCnt].child[1] = -1;
                trie[nodeCnt].cnt = 0;
                ++nodeCnt;
            }
            node = trie[node].child[bit];
            ++trie[node].cnt;
        }
    }
    return ans;
}

int countPairs(int* nums, int numsSize, int low, int high) {
    long long totalHigh = countLE(nums, numsSize, high);
    long long totalLowMinusOne = countLE(nums, numsSize, low - 1);
    return (int)(totalHigh - totalLowMinusOne);
}
```

## Csharp

```csharp
public class Solution
{
    private const int MAX_BIT = 14; // since nums[i], low, high <= 20000 < 2^15

    private class TrieNode
    {
        public TrieNode[] Child = new TrieNode[2];
        public int Count;
    }

    public int CountPairs(int[] nums, int low, int high)
    {
        return Count(nums, high) - Count(nums, low - 1);
    }

    private int Count(int[] nums, int k)
    {
        if (k < 0) return 0;
        TrieNode root = new TrieNode();
        int result = 0;
        foreach (int num in nums)
        {
            result += Query(root, num, k);
            Insert(root, num);
        }
        return result;
    }

    private void Insert(TrieNode root, int num)
    {
        TrieNode node = root;
        for (int i = MAX_BIT; i >= 0; --i)
        {
            int bit = (num >> i) & 1;
            if (node.Child[bit] == null)
                node.Child[bit] = new TrieNode();
            node = node.Child[bit];
            node.Count++;
        }
    }

    private int Query(TrieNode root, int num, int k)
    {
        TrieNode node = root;
        int cnt = 0;
        for (int i = MAX_BIT; i >= 0 && node != null; --i)
        {
            int nBit = (num >> i) & 1;
            int kBit = (k >> i) & 1;

            if (kBit == 1)
            {
                // Add all numbers where xor bit is 0 (same bit)
                TrieNode sameChild = node.Child[nBit];
                if (sameChild != null)
                    cnt += sameChild.Count;

                // Move to branch where xor bit is 1 (different bit) to continue matching k
                node = node.Child[1 - nBit];
            }
            else
            {
                // Must follow the branch where xor bit is 0 (same bit)
                node = node.Child[nBit];
            }
        }

        if (node != null)
            cnt += node.Count;

        return cnt;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countPairs = function(nums, low, high) {
    const MAX_BIT = 14; // since nums[i] <= 20000 < 2^15

    class TrieNode {
        constructor() {
            this.child = [null, null];
            this.cnt = 0;
        }
    }

    const root = new TrieNode();

    function insert(num) {
        let node = root;
        for (let i = MAX_BIT; i >= 0; i--) {
            const bit = (num >> i) & 1;
            if (!node.child[bit]) node.child[bit] = new TrieNode();
            node = node.child[bit];
            node.cnt++;
        }
    }

    function countLessOrEqual(num, K) {
        if (K < 0) return 0;
        let node = root;
        let ans = 0;
        for (let i = MAX_BIT; i >= 0 && node; i--) {
            const nBit = (num >> i) & 1;
            const kBit = (K >> i) & 1;
            if (kBit === 1) {
                // add counts where xor bit is 0 (same as nBit)
                const sameChild = node.child[nBit];
                if (sameChild) ans += sameChild.cnt;
                // move to branch where xor bit is 1 (opposite)
                node = node.child[1 - nBit];
            } else {
                // must keep xor bit 0
                node = node.child[nBit];
            }
        }
        return ans;
    }

    function countPairsWithK(K) {
        let total = 0;
        for (const num of nums) {
            total += countLessOrEqual(num, K);
            insert(num);
        }
        // reset trie for next use
        root.child[0] = null;
        root.child[1] = null;
        return total;
    }

    const highCount = countPairsWithK(high);
    // rebuild trie for low-1 counting
    const lowMinusOneCount = countPairsWithK(low - 1);
    return highCount - lowMinusOneCount;
};
```

## Typescript

```typescript
function countPairs(nums: number[], low: number, high: number): number {
    const MAX_BIT = 14; // enough for values up to 20000

    class Node {
        cnt: number;
        child: (Node | null)[];
        constructor() {
            this.cnt = 0;
            this.child = [null, null];
        }
    }

    const root = new Node();

    function insert(num: number): void {
        let node = root;
        for (let i = MAX_BIT; i >= 0; --i) {
            const bit = (num >> i) & 1;
            if (!node.child[bit]) node.child[bit] = new Node();
            node = node.child[bit]!;
            node.cnt += 1;
        }
    }

    // count of previously inserted numbers x such that (num xor x) < limit
    function query(num: number, limit: number): number {
        let node: Node | null = root;
        let ans = 0;
        for (let i = MAX_BIT; i >= 0 && node !== null; --i) {
            const bitNum = (num >> i) & 1;
            const bitLim = (limit >> i) & 1;
            if (bitLim === 1) {
                // take xor bit 0 -> child[bitNum]
                const sameChild = node.child[bitNum];
                if (sameChild) ans += sameChild.cnt;
                // move to xor bit 1 path
                node = node.child[bitNum ^ 1];
            } else {
                // must keep xor bit 0
                node = node.child[bitNum];
            }
        }
        return ans;
    }

    let result = 0;
    const highLimit = high + 1; // convert <=high to <high+1

    for (const num of nums) {
        // pairs with xor in [low, high] = (<high+1) - (<low)
        result += query(num, highLimit) - query(num, low);
        insert(num);
    }

    return result;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $low
     * @param Integer $high
     * @return Integer
     */
    function countPairs($nums, $low, $high) {
        return $this->countLessOrEqual($nums, $high) - $this->countLessOrEqual($nums, $low - 1);
    }
    
    private function countLessOrEqual($nums, $K) {
        if ($K < 0) return 0;
        $MAX_BIT = 14; // since nums[i] <= 20000 (< 2^15)
        $trie = [];
        $trie[] = ['next' => [-1, -1], 'cnt' => 0]; // root
        $res = 0;
        foreach ($nums as $num) {
            $res += $this->query($trie, $num, $K, $MAX_BIT);
            $this->insert($trie, $num, $MAX_BIT);
        }
        return $res;
    }
    
    private function insert(&$trie, $num, $MAX_BIT) {
        $node = 0;
        for ($bit = $MAX_BIT; $bit >= 0; $bit--) {
            $b = ($num >> $bit) & 1;
            if ($trie[$node]['next'][$b] == -1) {
                $trie[] = ['next' => [-1, -1], 'cnt' => 0];
                $trie[$node]['next'][$b] = count($trie) - 1;
            }
            $node = $trie[$node]['next'][$b];
            $trie[$node]['cnt']++;
        }
    }
    
    private function query(&$trie, $num, $K, $MAX_BIT) {
        $node = 0;
        $count = 0;
        for ($bit = $MAX_BIT; $bit >= 0; $bit--) {
            if ($node == -1) break;
            $nBit = ($num >> $bit) & 1;
            $kBit = ($K >> $bit) & 1;
            if ($kBit == 1) {
                $same = $trie[$node]['next'][$nBit];
                if ($same != -1) {
                    $count += $trie[$same]['cnt'];
                }
                $node = $trie[$node]['next'][1 - $nBit];
            } else {
                $node = $trie[$node]['next'][$nBit];
            }
        }
        if ($node != -1) {
            $count += $trie[$node]['cnt'];
        }
        return $count;
    }
}
```

## Swift

```swift
class TrieNode {
    var child: [TrieNode?] = [nil, nil]
    var cnt: Int = 0
}

class Solution {
    func countPairs(_ nums: [Int], _ low: Int, _ high: Int) -> Int {
        let upToHigh = countLessThan(nums, high + 1)
        let upToLowMinusOne = countLessThan(nums, low)
        return upToHigh - upToLowMinusOne
    }
    
    private func countLessThan(_ nums: [Int], _ limit: Int) -> Int {
        if limit <= 0 { return 0 }
        let root = TrieNode()
        var result = 0
        for num in nums {
            result += query(root, num, limit)
            insert(root, num)
        }
        return result
    }
    
    private func insert(_ node: TrieNode, _ num: Int) {
        var cur: TrieNode? = node
        for i in stride(from: 14, through: 0, by: -1) {
            let bit = (num >> i) & 1
            if cur?.child[bit] == nil {
                cur?.child[bit] = TrieNode()
            }
            cur = cur?.child[bit]
            cur?.cnt += 1
        }
    }
    
    private func query(_ node: TrieNode, _ num: Int, _ limit: Int) -> Int {
        var cur: TrieNode? = node
        var total = 0
        for i in stride(from: 14, through: 0, by: -1) {
            guard let current = cur else { break }
            let nBit = (num >> i) & 1
            let kBit = (limit >> i) & 1
            if kBit == 1 {
                if let childNode = current.child[nBit] {
                    total += childNode.cnt
                }
                cur = current.child[1 - nBit]
            } else {
                cur = current.child[nBit]
            }
        }
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    private class TrieNode {
        val child = arrayOfNulls<TrieNode>(2)
        var cnt = 0
    }

    private val MAX_BIT = 14  // since nums[i], low, high <= 20000 < 2^15

    fun countPairs(nums: IntArray, low: Int, high: Int): Int {
        val root = TrieNode()
        var result = 0L

        for (num in nums) {
            result += query(root, num, high + 1)
            result -= query(root, num, low)
            insert(root, num)
        }
        return result.toInt()
    }

    private fun insert(root: TrieNode, num: Int) {
        var node = root
        for (i in MAX_BIT downTo 0) {
            val bit = (num shr i) and 1
            if (node.child[bit] == null) {
                node.child[bit] = TrieNode()
            }
            node = node.child[bit]!!
            node.cnt++
        }
    }

    // counts how many previously inserted numbers x satisfy (num xor x) < limit
    private fun query(root: TrieNode, num: Int, limit: Int): Long {
        var node: TrieNode? = root
        var count = 0L
        for (i in MAX_BIT downTo 0) {
            if (node == null) break
            val bitNum = (num shr i) and 1
            val bitLim = (limit shr i) and 1
            if (bitLim == 1) {
                // add all numbers where xor bit is 0 (same as bitNum)
                node.child[bitNum]?.let { count += it.cnt.toLong() }
                // move to branch where xor bit is 1 (opposite bit)
                node = node.child[1 - bitNum]
            } else {
                // must keep xor bit 0
                node = node.child[bitNum]
            }
        }
        return count
    }
}
```

## Golang

```go
type trieNode struct {
	child [2]*trieNode
	cnt   int
}

const maxBit = 14 // since nums[i], low, high ≤ 20000 < 2^15

func insert(root *trieNode, num int) {
	node := root
	for i := maxBit; i >= 0; i-- {
		bit := (num >> i) & 1
		if node.child[bit] == nil {
			node.child[bit] = &trieNode{}
		}
		node = node.child[bit]
		node.cnt++
	}
}

func query(root *trieNode, num, k int) int {
	if root == nil || k < 0 {
		return 0
	}
	node := root
	ans := 0
	for i := maxBit; i >= 0 && node != nil; i-- {
		nbit := (num >> i) & 1
		kbit := (k >> i) & 1
		if kbit == 1 {
			// xor bit = 0 -> ybit = nbit, all such numbers are valid
			if node.child[nbit] != nil {
				ans += node.child[nbit].cnt
			}
			// continue with xor bit = 1 -> ybit = 1-nbit
			node = node.child[1-nbit]
		} else { // kbit == 0, must keep xor bit 0
			node = node.child[nbit]
		}
	}
	if node != nil {
		ans += node.cnt
	}
	return ans
}

func countXorLE(nums []int, k int) int {
	if k < 0 {
		return 0
	}
	root := &trieNode{}
	total := 0
	for _, v := range nums {
		total += query(root, v, k)
		insert(root, v)
	}
	return total
}

func countPairs(nums []int, low int, high int) int {
	return countXorLE(nums, high) - countXorLE(nums, low-1)
}
```

## Ruby

```ruby
class TrieNode
  attr_accessor :children, :cnt
  def initialize
    @children = [nil, nil]
    @cnt = 0
  end
end

class Trie
  MAX_BIT = 14
  def initialize
    @root = TrieNode.new
  end

  def insert(num)
    node = @root
    (MAX_BIT).downto(0) do |i|
      bit = (num >> i) & 1
      node.children[bit] ||= TrieNode.new
      node = node.children[bit]
      node.cnt += 1
    end
  end

  def query(num, k)
    return 0 if k < 0
    node = @root
    count = 0
    (MAX_BIT).downto(0) do |i|
      break unless node
      bit = (num >> i) & 1
      kb = (k >> i) & 1
      if kb == 1
        same_child = node.children[bit]
        count += same_child.cnt if same_child
        node = node.children[1 - bit]
      else
        node = node.children[bit]
      end
    end
    count += node.cnt if node
    count
  end
end

def count_leq(nums, k)
  return 0 if k < 0
  trie = Trie.new
  total = 0
  nums.each do |num|
    total += trie.query(num, k)
    trie.insert(num)
  end
  total
end

# @param {Integer[]} nums
# @param {Integer} low
# @param {Integer} high
# @return {Integer}
def count_pairs(nums, low, high)
  count_leq(nums, high) - count_leq(nums, low - 1)
end
```

## Scala

```scala
object Solution {
    def countPairs(nums: Array[Int], low: Int, high: Int): Int = {
        val maxBit = 14 // since nums[i] <= 20000 < 2^15
        class Node {
            var child = new Array[Node](2)
            var cnt: Int = 0
        }
        def insert(root: Node, num: Int): Unit = {
            var node = root
            for (i <- maxBit to 0 by -1) {
                val b = (num >> i) & 1
                if (node.child(b) == null) node.child(b) = new Node()
                node = node.child(b)
                node.cnt += 1
            }
        }
        def query(root: Node, num: Int, limit: Int): Long = {
            var node = root
            var ans: Long = 0L
            for (i <- maxBit to 0 by -1) {
                if (node == null) return ans
                val bNum = (num >> i) & 1
                val bLim = (limit >> i) & 1
                if (bLim == 1) {
                    val zeroBranch = node.child(bNum)
                    if (zeroBranch != null) ans += zeroBranch.cnt
                    node = node.child(1 - bNum)
                } else {
                    node = node.child(bNum)
                }
            }
            if (node != null) ans += node.cnt
            ans
        }
        def countAtMost(k: Int): Long = {
            val root = new Node()
            var total: Long = 0L
            for (num <- nums) {
                total += query(root, num, k)
                insert(root, num)
            }
            total
        }
        val highCount = countAtMost(high)
        val lowMinusOneCount = if (low > 0) countAtMost(low - 1) else 0L
        (highCount - lowMinusOneCount).toInt
    }
}
```

## Rust

```rust
pub struct Solution;

impl Solution {
    pub fn count_pairs(nums: Vec<i32>, low: i32, high: i32) -> i32 {
        #[derive(Clone)]
        struct Node {
            child: [i32; 2],
            cnt: i32,
        }

        fn max_bit(nums: &[i32], k: i32) -> i32 {
            let mut mx = k;
            for &v in nums {
                if v > mx {
                    mx = v;
                }
            }
            let mut bit = 0;
            while (1 << bit) <= mx {
                bit += 1;
            }
            if bit == 0 { 0 } else { bit - 1 }
        }

        fn insert(trie: &mut Vec<Node>, num: i32, max_bit: i32) {
            let mut node = 0usize;
            for bpos in (0..=max_bit).rev() {
                let bit = ((num >> bpos) & 1) as usize;
                if trie[node].child[bit] == -1 {
                    trie.push(Node { child: [-1, -1], cnt: 0 });
                    let new_idx = (trie.len() - 1) as i32;
                    trie[node].child[bit] = new_idx;
                }
                node = trie[node].child[bit] as usize;
                trie[node].cnt += 1;
            }
        }

        fn query(trie: &Vec<Node>, num: i32, k: i32, max_bit: i32) -> i32 {
            let mut ans = 0i32;
            let mut node_opt: Option<usize> = Some(0);
            for bpos in (0..=max_bit).rev() {
                if node_opt.is_none() {
                    break;
                }
                let node = node_opt.unwrap();
                let bit = ((num >> bpos) & 1) as usize;
                let kbit = (k >> bpos) & 1;
                if kbit == 1 {
                    let same_idx = trie[node].child[bit];
                    if same_idx != -1 {
                        ans += trie[same_idx as usize].cnt;
                    }
                    node_opt = if trie[node].child[1 - bit] != -1 {
                        Some(trie[node].child[1 - bit] as usize)
                    } else {
                        None
                    };
                } else {
                    node_opt = if trie[node].child[bit] != -1 {
                        Some(trie[node].child[bit] as usize)
                    } else {
                        None
                    };
                }
            }
            ans
        }

        fn count_leq(nums: &[i32], k: i32, max_bit: i32) -> i64 {
            if k < 0 {
                return 0;
            }
            let mut trie = vec![Node { child: [-1, -1], cnt: 0 }];
            let mut res: i64 = 0;
            for &num in nums.iter() {
                let cnt = query(&trie, num, k, max_bit);
                res += cnt as i64;
                insert(&mut trie, num, max_bit);
            }
            res
        }

        let maxb = max_bit(&nums, high);
        let high_cnt = count_leq(&nums, high, maxb);
        let low_cnt = if low > 0 {
            count_leq(&nums, low - 1, maxb)
        } else {
            0
        };
        (high_cnt - low_cnt) as i32
    }
}
```

## Racket

```racket
(define/contract (count-pairs nums low high)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)

  (let* ([max-val (apply max (append nums (list high))))
         [max-bit (max 0 (- (integer-length max-val) 1))])
    (define (get-bit x b)
      (bitwise-and (arithmetic-shift x (- b)) 1))

    (define (count-le K)
      (if (< K 0)
          0
          (let* ([max-nodes (* (+ (length nums) 1) (+ max-bit 2))]
                 [nodes (make-vector max-nodes #f)]
                 [node-count (box 1)])
            (vector-set! nodes 0 (vector -1 -1 0))

            (define (inc-root)
              (let ([root (vector-ref nodes 0)])
                (vector-set! root 2 (+ (vector-ref root 2) 1))))

            (define (insert num)
              (inc-root)
              (let loop ((idx 0) (bit max-bit))
                (when (>= bit 0)
                  (define nbit (get-bit num bit))
                  (define node (vector-ref nodes idx))
                  (define child-idx (vector-ref node nbit))
                  (define new-child
                    (if (= child-idx -1)
                        (let ([newIdx (unbox node-count)])
                          (set-box! node-count (+ (unbox node-count) 1))
                          (vector-set! nodes newIdx (vector -1 -1 0))
                          (vector-set! node nbit newIdx)
                          newIdx)
                        child-idx))
                  (let ([child-node (vector-ref nodes new-child)])
                    (vector-set! child-node 2 (+ (vector-ref child-node 2) 1)))
                  (loop new-child (- bit 1)))))

            (define (query num K)
              (let loop ((idx 0) (bit max-bit) (acc 0))
                (if (or (= idx -1) (< bit 0))
                    acc
                    (let* ([nbit (get-bit num bit)]
                           [kbit (get-bit K bit)]
                           [node (vector-ref nodes idx)])
                      (if (= kbit 1)
                          (let* ([same-child (vector-ref node nbit)]
                                 [add (if (= same-child -1) 0
                                          (vector-ref (vector-ref nodes same-child) 2))]
                                 [opp-child (vector-ref node (- 1 nbit))])
                            (loop opp-child (- bit 1) (+ acc add)))
                          (let ([next-child (vector-ref node nbit)])
                            (loop next-child (- bit 1) acc)))))))

            (define total 0)
            (for ([num nums])
              (set! total (+ total (query num K)))
              (insert num))
            total)))

    (- (count-le high) (count-le (- low 1)))))
```
