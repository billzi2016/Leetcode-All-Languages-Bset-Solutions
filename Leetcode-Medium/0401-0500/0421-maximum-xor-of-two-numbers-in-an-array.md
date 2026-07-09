# 0421. Maximum XOR of Two Numbers in an Array

## Cpp

```cpp
class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        const int HIGH_BIT = 30; // since nums[i] <= 2^31 - 1
        struct Node {
            int child[2];
            Node() { child[0] = child[1] = -1; }
        };
        vector<Node> trie(1); // root at index 0
        
        auto insert = [&](int num) {
            int node = 0;
            for (int k = HIGH_BIT; k >= 0; --k) {
                int b = (num >> k) & 1;
                if (trie[node].child[b] == -1) {
                    trie[node].child[b] = trie.size();
                    trie.emplace_back();
                }
                node = trie[node].child[b];
            }
        };
        
        auto query = [&](int num) {
            int node = 0;
            int xorVal = 0;
            for (int k = HIGH_BIT; k >= 0; --k) {
                int b = (num >> k) & 1;
                int toggled = b ^ 1;
                if (trie[node].child[toggled] != -1) {
                    xorVal |= (1 << k);
                    node = trie[node].child[toggled];
                } else {
                    node = trie[node].child[b];
                }
            }
            return xorVal;
        };
        
        for (int num : nums) insert(num);
        int maxXor = 0;
        for (int num : nums) {
            maxXor = max(maxXor, query(num));
        }
        return maxXor;
    }
};
```

## Java

```java
class Solution {
    private static class Node {
        Node[] child = new Node[2];
    }

    public int findMaximumXOR(int[] nums) {
        Node root = new Node();
        // Build trie
        for (int num : nums) {
            Node cur = root;
            for (int i = 30; i >= 0; i--) { // numbers are non‑negative, highest bit is 30
                int bit = (num >> i) & 1;
                if (cur.child[bit] == null) {
                    cur.child[bit] = new Node();
                }
                cur = cur.child[bit];
            }
        }

        int maxXor = 0;
        // Query trie for each number
        for (int num : nums) {
            Node cur = root;
            int xor = 0;
            for (int i = 30; i >= 0; i--) {
                int bit = (num >> i) & 1;
                int toggled = bit ^ 1;
                if (cur.child[toggled] != null) {
                    xor |= (1 << i);
                    cur = cur.child[toggled];
                } else {
                    cur = cur.child[bit];
                }
            }
            if (xor > maxXor) {
                maxXor = xor;
            }
        }
        return maxXor;
    }
}
```

## Python

```python
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_xor = 0
        mask = 0
        for i in range(31, -1, -1):
            mask |= (1 << i)
            prefixes = set()
            for num in nums:
                prefixes.add(num & mask)
            candidate = max_xor | (1 << i)
            found = False
            for p in prefixes:
                if (candidate ^ p) in prefixes:
                    found = True
                    break
            if found:
                max_xor = candidate
        return max_xor
```

## Python3

```python
from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        mask = 0
        for i in range(31, -1, -1):
            mask |= (1 << i)
            prefixes = {num & mask for num in nums}
            candidate = max_xor | (1 << i)
            for p in prefixes:
                if (candidate ^ p) in prefixes:
                    max_xor = candidate
                    break
        return max_xor
```

## C

```c
#include <stdlib.h>

int findMaximumXOR(int* nums, int numsSize){
    if (numsSize < 2) return 0;
    const int MAX_BITS = 31;               // bits 30..0 for numbers <= 2^31-1
    int maxNodes = (numsSize + 1) * 32;    // enough nodes for all inserts
    int (*trie)[2] = malloc(maxNodes * sizeof(int[2]));
    if (!trie) return 0;
    for (int i = 0; i < maxNodes; ++i) {
        trie[i][0] = -1;
        trie[i][1] = -1;
    }
    int nodeCount = 1; // root is index 0

    /* insert first number */
    int cur = 0;
    for (int k = MAX_BITS - 1; k >= 0; --k) {
        int bit = (nums[0] >> k) & 1;
        if (trie[cur][bit] == -1) {
            trie[cur][bit] = nodeCount++;
        }
        cur = trie[cur][bit];
    }

    int ans = 0;

    for (int i = 1; i < numsSize; ++i) {
        /* query maximum xor with existing numbers */
        cur = 0;
        int curXor = 0;
        for (int k = MAX_BITS - 1; k >= 0; --k) {
            int bit = (nums[i] >> k) & 1;
            int toggled = bit ^ 1;
            if (trie[cur][toggled] != -1) {
                curXor |= (1 << k);
                cur = trie[cur][toggled];
            } else {
                cur = trie[cur][bit];
            }
        }
        if (curXor > ans) ans = curXor;

        /* insert current number into trie */
        cur = 0;
        for (int k = MAX_BITS - 1; k >= 0; --k) {
            int bit = (nums[i] >> k) & 1;
            if (trie[cur][bit] == -1) {
                trie[cur][bit] = nodeCount++;
            }
            cur = trie[cur][bit];
        }
    }

    free(trie);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public int FindMaximumXOR(int[] nums)
    {
        int max = 0;
        int mask = 0;
        for (int i = 30; i >= 0; i--)
        {
            mask |= (1 << i);
            var prefixes = new HashSet<int>();
            foreach (var num in nums)
                prefixes.Add(num & mask);

            int candidate = max | (1 << i);
            bool found = false;
            foreach (var p in prefixes)
            {
                if (prefixes.Contains(p ^ candidate))
                {
                    found = true;
                    break;
                }
            }

            if (found) max = candidate;
        }
        return max;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaximumXOR = function(nums) {
    let max = 0;
    let mask = 0;
    for (let i = 30; i >= 0; i--) {
        mask |= (1 << i);
        const prefixes = new Set();
        for (const num of nums) {
            prefixes.add(num & mask);
        }
        const candidate = max | (1 << i);
        let found = false;
        for (const p of prefixes) {
            if (prefixes.has(p ^ candidate)) {
                found = true;
                break;
            }
        }
        if (found) {
            max = candidate;
        }
    }
    return max;
};
```

## Typescript

```typescript
function findMaximumXOR(nums: number[]): number {
    let maxXor = 0;
    let mask = 0;
    for (let i = 30; i >= 0; i--) {
        mask |= (1 << i);
        const prefixes = new Set<number>();
        for (const num of nums) {
            prefixes.add(num & mask);
        }
        const candidate = maxXor | (1 << i);
        let found = false;
        for (const p of prefixes) {
            if (prefixes.has(p ^ candidate)) {
                found = true;
                break;
            }
        }
        if (found) {
            maxXor = candidate;
        }
    }
    return maxXor;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findMaximumXOR($nums) {
        $maxXor = 0;
        for ($i = 30; $i >= 0; $i--) {
            $candidate = $maxXor | (1 << $i);
            $prefixes = [];
            foreach ($nums as $num) {
                $pref = $num >> $i;
                $prefixes[$pref] = true;
            }
            $found = false;
            foreach ($prefixes as $p => $_) {
                if (isset($prefixes[$candidate ^ $p])) {
                    $found = true;
                    break;
                }
            }
            if ($found) {
                $maxXor = $candidate;
            }
        }
        return $maxXor;
    }
}
```

## Swift

```swift
class Solution {
    func findMaximumXOR(_ nums: [Int]) -> Int {
        var maxXor = 0
        var mask = 0
        for i in stride(from: 31, through: 0, by: -1) {
            mask |= (1 << i)
            var prefixes = Set<Int>()
            for num in nums {
                prefixes.insert(num & mask)
            }
            let candidate = maxXor | (1 << i)
            var found = false
            for p in prefixes {
                if prefixes.contains(p ^ candidate) {
                    found = true
                    break
                }
            }
            if found {
                maxXor = candidate
            }
        }
        return maxXor
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findMaximumXOR(nums: IntArray): Int {
        var maxXor = 0
        var mask = 0
        for (i in 31 downTo 0) {
            mask = mask or (1 shl i)
            val prefixes = HashSet<Int>()
            for (num in nums) {
                prefixes.add(num and mask)
            }
            val candidate = maxXor or (1 shl i)
            var found = false
            for (p in prefixes) {
                if (prefixes.contains(p xor candidate)) {
                    found = true
                    break
                }
            }
            if (found) {
                maxXor = candidate
            }
        }
        return maxXor
    }
}
```

## Dart

```dart
class _TrieNode {
  List<int> child = [-1, -1];
}

class Solution {
  int findMaximumXOR(List<int> nums) {
    const int HIGH_BIT = 30;
    final List<_TrieNode> nodes = [_TrieNode()];

    void insert(int num) {
      int cur = 0;
      for (int k = HIGH_BIT; k >= 0; --k) {
        int b = (num >> k) & 1;
        if (nodes[cur].child[b] == -1) {
          nodes[cur].child[b] = nodes.length;
          nodes.add(_TrieNode());
        }
        cur = nodes[cur].child[b];
      }
    }

    int query(int num) {
      int cur = 0;
      int xor = 0;
      for (int k = HIGH_BIT; k >= 0; --k) {
        int b = (num >> k) & 1;
        int toggled = b ^ 1;
        if (nodes[cur].child[toggled] != -1) {
          xor |= (1 << k);
          cur = nodes[cur].child[toggled];
        } else {
          cur = nodes[cur].child[b];
        }
      }
      return xor;
    }

    insert(nums[0]);
    int maxXor = 0;
    for (int i = 1; i < nums.length; ++i) {
      int candidate = query(nums[i]);
      if (candidate > maxXor) maxXor = candidate;
      insert(nums[i]);
    }
    return maxXor;
  }
}
```

## Golang

```go
func findMaximumXOR(nums []int) int {
    maxXor := 0
    mask := 0
    for i := 31; i >= 0; i-- {
        mask |= (1 << i)
        prefixes := make(map[int]struct{}, len(nums))
        for _, num := range nums {
            prefixes[num&mask] = struct{}{}
        }
        candidate := maxXor | (1 << i)
        found := false
        for p := range prefixes {
            if _, ok := prefixes[p^candidate]; ok {
                found = true
                break
            }
        }
        if found {
            maxXor = candidate
        }
    }
    return maxXor
}
```

## Ruby

```ruby
def find_maximum_xor(nums)
  max_xor = 0
  mask = 0
  31.downto(0) do |i|
    mask |= (1 << i)
    prefixes = {}
    nums.each { |num| prefixes[num & mask] = true }
    candidate = max_xor | (1 << i)
    found = false
    prefixes.each_key do |p|
      if prefixes.key?(candidate ^ p)
        found = true
        break
      end
    end
    max_xor = candidate if found
  end
  max_xor
end
```

## Scala

```scala
object Solution {
    def findMaximumXOR(nums: Array[Int]): Int = {
        var maxXor = 0
        var mask = 0
        for (i <- 31 to 0 by -1) {
            mask |= (1 << i)
            val prefixes = scala.collection.mutable.HashSet[Int]()
            for (num <- nums) {
                prefixes.add(num & mask)
            }
            val candidate = maxXor | (1 << i)
            var found = false
            import scala.util.control.Breaks._
            breakable {
                for (p <- prefixes) {
                    if (prefixes.contains(p ^ candidate)) {
                        found = true
                        break()
                    }
                }
            }
            if (found) maxXor = candidate
        }
        maxXor
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_maximum_xor(nums: Vec<i32>) -> i32 {
        #[derive(Clone)]
        struct Node {
            next: [i32; 2],
        }

        let mut trie = Vec::new();
        trie.push(Node { next: [-1, -1] });

        // Build the trie with all numbers
        for &num in &nums {
            let mut node_idx = 0usize;
            for i in (0..=31).rev() {
                let bit = ((num as u32 >> i) & 1) as usize;
                if trie[node_idx].next[bit] == -1 {
                    trie[node_idx].next[bit] = trie.len() as i32;
                    trie.push(Node { next: [-1, -1] });
                }
                node_idx = trie[node_idx].next[bit] as usize;
            }
        }

        // Query maximum xor for each number
        let mut max_xor: i32 = 0;
        for &num in &nums {
            let mut node_idx = 0usize;
            let mut cur: u32 = 0;
            for i in (0..=31).rev() {
                let bit = ((num as u32 >> i) & 1) as usize;
                let toggled = 1 - bit;
                if trie[node_idx].next[toggled] != -1 {
                    cur |= 1 << i;
                    node_idx = trie[node_idx].next[toggled] as usize;
                } else {
                    node_idx = trie[node_idx].next[bit] as usize;
                }
            }
            if cur as i32 > max_xor {
                max_xor = cur as i32;
            }
        }

        max_xor
    }
}
```

## Racket

```racket
(define/contract (find-maximum-xor nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((i 31) (mask 0) (maxXor 0))
    (if (< i 0)
        maxXor
        (let* ((new-mask (bitwise-ior mask (arithmetic-shift 1 i)))
               (prefixes (make-hash)))
          (for ([num nums])
            (hash-set! prefixes (bitwise-and num new-mask) #t))
          (define candidate (bitwise-ior maxXor (arithmetic-shift 1 i)))
          (define found?
            (let ((found? #f))
              (hash-for-each prefixes
                (lambda (p _)
                  (when (and (not found?)
                             (hash-has-key? prefixes (bitwise-xor p candidate)))
                    (set! found? #t))))
              found?))
          (loop (- i 1) new-mask (if found? candidate maxXor))))) )
```

## Erlang

```erlang
-module(solution).
-export([find_maximum_xor/1]).

-spec find_maximum_xor(Nums :: [integer()]) -> integer().
find_maximum_xor(Nums) ->
    Trie = lists:foldl(fun insert_num/2, #{}, Nums),
    MaxXor = lists:max([query_num(N, Trie) || N <- Nums]),
    MaxXor.

insert_num(Num, Trie) ->
    insert_bit(Num, 30, Trie).

insert_bit(_Num, -1, Trie) -> Trie;
insert_bit(Num, Pos, Trie) ->
    Bit = (Num bsr Pos) band 1,
    Child = maps:get(Bit, Trie, #{}),
    NewChild = insert_bit(Num, Pos-1, Child),
    maps:put(Bit, NewChild, Trie).

query_num(Num, Trie) ->
    query_bit(Num, 30, Trie, 0).

query_bit(_Num, -1, _Trie, Acc) -> Acc;
query_bit(Num, Pos, Trie, Acc) ->
    Desired = 1 - ((Num bsr Pos) band 1),
    case maps:is_key(Desired, Trie) of
        true ->
            NewAcc = Acc bor (1 bsl Pos),
            NextTrie = maps:get(Desired, Trie),
            query_bit(Num, Pos-1, NextTrie, NewAcc);
        false ->
            SameBit = 1 - Desired,
            NextTrie = maps:get(SameBit, Trie),
            query_bit(Num, Pos-1, NextTrie, Acc)
    end.
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec find_maximum_xor(nums :: [integer]) :: integer
  def find_maximum_xor(nums) do
    {max_xor, _mask} =
      Enum.reduce(30..0, {0, 0}, fn i, {max_xor, mask} ->
        new_mask = mask ||| (1 <<< i)

        prefixes =
          nums
          |> Enum.map(fn num -> num &&& new_mask end)
          |> MapSet.new()

        candidate = max_xor ||| (1 <<< i)

        found =
          Enum.any?(prefixes, fn p ->
            MapSet.member?(prefixes, candidate ^^^ p)
          end)

        if found do
          {candidate, new_mask}
        else
          {max_xor, new_mask}
        end
      end)

    max_xor
  end
end
```
