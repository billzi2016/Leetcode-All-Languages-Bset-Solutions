# 2791. Count Paths That Can Form a Palindrome in a Tree

## Cpp

```cpp
class Solution {
public:
    long long countPalindromePaths(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> children(n);
        for (int i = 1; i < n; ++i) {
            children[parent[i]].push_back(i);
        }
        unordered_map<int,int> cnt;
        cnt.reserve(n * 2);
        cnt.max_load_factor(0.7);
        long long ans = 0;
        // iterative DFS stack: pair of node and its mask
        vector<pair<int,int>> stk;
        stk.emplace_back(0, 0); // root mask is 0
        while (!stk.empty()) {
            auto [node, curMask] = stk.back();
            stk.pop_back();
            // count pairs with previously seen nodes
            auto itSame = cnt.find(curMask);
            if (itSame != cnt.end()) ans += itSame->second;
            for (int b = 0; b < 26; ++b) {
                int target = curMask ^ (1 << b);
                auto it = cnt.find(target);
                if (it != cnt.end()) ans += it->second;
            }
            // record current mask
            ++cnt[curMask];
            // push children
            for (int child : children[node]) {
                int childMask = curMask ^ (1 << (s[child] - 'a'));
                stk.emplace_back(child, childMask);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public long countPalindromePaths(List<Integer> parent, String s) {
        int n = parent.size();
        List<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int i = 1; i < n; i++) {
            int p = parent.get(i);
            adj[p].add(i);
            adj[i].add(p);
        }
        int[] mask = new int[n];
        boolean[] visited = new boolean[n];
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(0);
        visited[0] = true;
        while (!stack.isEmpty()) {
            int node = stack.pop();
            for (int nb : adj[node]) {
                if (!visited[nb]) {
                    visited[nb] = true;
                    mask[nb] = mask[node] ^ (1 << (s.charAt(nb) - 'a'));
                    stack.push(nb);
                }
            }
        }
        Map<Integer, Integer> freq = new HashMap<>();
        long ans = 0L;
        for (int i = 0; i < n; i++) {
            int m = mask[i];
            ans += freq.getOrDefault(m, 0);
            for (int b = 0; b < 26; b++) {
                int mm = m ^ (1 << b);
                ans += freq.getOrDefault(mm, 0);
            }
            freq.put(m, freq.getOrDefault(m, 0) + 1);
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def countPalindromePaths(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: int
        """
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            p = parent[i]
            children[p].append(i)

        masks = [0] * n
        stack = [0]
        while stack:
            node = stack.pop()
            cur_mask = masks[node]
            for child in children[node]:
                bit = 1 << (ord(s[child]) - 97)
                masks[child] = cur_mask ^ bit
                stack.append(child)

        from collections import defaultdict
        cnt = defaultdict(int)
        ans = 0
        for m in masks:
            ans += cnt[m]
            for b in range(26):
                ans += cnt[m ^ (1 << b)]
            cnt[m] += 1
        return ans
```

## Python3

```python
class Solution:
    def countPalindromePaths(self, parent: list[int], s: str) -> int:
        from collections import defaultdict

        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            p = parent[i]
            children[p].append(i)

        mask = [0] * n
        freq = defaultdict(int)
        ans = 0
        stack = [0]

        while stack:
            u = stack.pop()
            m = mask[u]

            # pairs with same mask
            ans += freq[m]
            # pairs differing by exactly one bit
            for b in range(26):
                ans += freq[m ^ (1 << b)]

            freq[m] += 1

            for v in children[u]:
                bit = ord(s[v]) - 97
                mask[v] = m ^ (1 << bit)
                stack.append(v)

        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

long long countPalindromePaths(int* parent, int parentSize, char* s) {
    int n = parentSize;
    if (n <= 1) return 0LL;

    /* build adjacency list */
    int *head = (int*)malloc(n * sizeof(int));
    int mEdges = 2 * (n - 1);
    int *to   = (int*)malloc(mEdges * sizeof(int));
    int *next = (int*)malloc(mEdges * sizeof(int));
    for (int i = 0; i < n; ++i) head[i] = -1;
    int ecnt = 0;
    for (int i = 1; i < n; ++i) {
        int p = parent[i];
        to[ecnt] = i;   next[ecnt] = head[p]; head[p] = ecnt++;
        to[ecnt] = p;   next[ecnt] = head[i]; head[i] = ecnt++;
    }

    /* compute mask for each node using stack DFS */
    int *mask = (int*)malloc(n * sizeof(int));
    char *vis = (char*)calloc(n, 1);
    int *stack = (int*)malloc(n * sizeof(int));
    int sp = 0;
    stack[sp++] = 0;
    vis[0] = 1;
    mask[0] = 0;

    while (sp) {
        int u = stack[--sp];
        for (int e = head[u]; e != -1; e = next[e]) {
            int v = to[e];
            if (vis[v]) continue;
            vis[v] = 1;
            mask[v] = mask[u] ^ (1 << (s[v] - 'a'));
            stack[sp++] = v;
        }
    }

    free(head);
    free(to);
    free(next);
    free(vis);
    free(stack);

    /* frequency array for masks: size 2^26 */
    const int SZ = 1 << 26;               // 67,108,864
    uint32_t *freq = (uint32_t*)calloc(SZ, sizeof(uint32_t));

    long long ans = 0;
    for (int i = 0; i < n; ++i) {
        int m = mask[i];
        ans += freq[m];                     // xor == 0
        for (int b = 0; b < 26; ++b) {
            int m2 = m ^ (1 << b);
            ans += freq[m2];                // xor has exactly one bit set
        }
        ++freq[m];
    }

    free(mask);
    free(freq);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long CountPalindromePaths(IList<int> parent, string s) {
        int n = parent.Count;
        var adj = new List<(int to, char ch)>[n];
        for (int i = 0; i < n; i++) adj[i] = new List<(int, char)>();
        for (int i = 1; i < n; i++) {
            int p = parent[i];
            char c = s[i];
            adj[p].Add((i, c));
            adj[i].Add((p, c));
        }

        int[] mask = new int[n];
        bool[] visited = new bool[n];
        var stack = new Stack<int>();
        stack.Push(0);
        visited[0] = true;
        mask[0] = 0;

        while (stack.Count > 0) {
            int node = stack.Pop();
            foreach (var (to, ch) in adj[node]) {
                if (!visited[to]) {
                    visited[to] = true;
                    mask[to] = mask[node] ^ (1 << (ch - 'a'));
                    stack.Push(to);
                }
            }
        }

        var cnt = new Dictionary<int, int>();
        long ans = 0;
        foreach (int m in mask) {
            if (cnt.TryGetValue(m, out int same)) ans += same;
            for (int k = 0; k < 26; k++) {
                int target = m ^ (1 << k);
                if (cnt.TryGetValue(target, out int val)) ans += val;
            }
            if (cnt.ContainsKey(m))
                cnt[m] = cnt[m] + 1;
            else
                cnt[m] = 1;
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} parent
 * @param {string} s
 * @return {number}
 */
var countPalindromePaths = function(parent, s) {
    const n = parent.length;
    const children = Array.from({ length: n }, () => []);
    for (let i = 1; i < n; i++) {
        const p = parent[i];
        children[p].push(i);
    }

    const freq = new Map(); // mask -> count
    let ans = 0;
    const stack = [{ node: 0, mask: 0 }];

    while (stack.length) {
        const { node, mask } = stack.pop();

        // pairs with previously seen masks
        ans += freq.get(mask) || 0;
        for (let b = 0; b < 26; b++) {
            const key = mask ^ (1 << b);
            ans += freq.get(key) || 0;
        }

        freq.set(mask, (freq.get(mask) || 0) + 1);

        // process children
        for (const child of children[node]) {
            const chMask = mask ^ (1 << (s.charCodeAt(child) - 97));
            stack.push({ node: child, mask: chMask });
        }
    }

    return ans;
};
```

## Typescript

```typescript
function countPalindromePaths(parent: number[], s: string): number {
    const n = parent.length;
    const masks = new Uint32Array(n);
    for (let i = 1; i < n; i++) {
        const p = parent[i];
        const bit = 1 << (s.charCodeAt(i) - 97);
        masks[i] = masks[p] ^ bit;
    }
    const freq = new Map<number, number>();
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const m = masks[i];
        ans += freq.get(m) ?? 0;
        for (let k = 0; k < 26; k++) {
            const cnt = freq.get(m ^ (1 << k)) ?? 0;
            ans += cnt;
        }
        freq.set(m, (freq.get(m) ?? 0) + 1);
    }
    return ans;
}
```

## Php

```php
class Solution {
    /**
     * @param Integer[] $parent
     * @param String $s
     * @return Integer
     */
    function countPalindromePaths($parent, $s) {
        $n = count($parent);
        // Build children adjacency list
        $children = array_fill(0, $n, []);
        for ($i = 1; $i < $n; ++$i) {
            $p = $parent[$i];
            $children[$p][] = $i;
        }

        // Compute mask for each node (parity of letters from root to node)
        $mask = array_fill(0, $n, 0);
        $queue = new SplQueue();
        $queue->enqueue(0);
        while (!$queue->isEmpty()) {
            $node = $queue->dequeue();
            foreach ($children[$node] as $child) {
                $chIdx = ord($s[$child]) - 97; // 'a' => 0
                $mask[$child] = $mask[$node] ^ (1 << $chIdx);
                $queue->enqueue($child);
            }
        }

        // Count pairs using hashmap of mask frequencies
        $cnt = [];
        $ans = 0;
        for ($i = 0; $i < $n; ++$i) {
            $m = $mask[$i];
            if (isset($cnt[$m])) {
                $ans += $cnt[$m];
            }
            // masks differing by exactly one bit
            for ($k = 0; $k < 26; ++$k) {
                $key = $m ^ (1 << $k);
                if (isset($cnt[$key])) {
                    $ans += $cnt[$key];
                }
            }
            $cnt[$m] = ($cnt[$m] ?? 0) + 1;
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countPalindromePaths(_ parent: [Int], _ s: String) -> Int {
        let n = parent.count
        var children = [[Int]](repeating: [], count: n)
        if n > 1 {
            for i in 1..<n {
                let p = parent[i]
                children[p].append(i)
            }
        }
        
        let sBytes = Array(s.utf8)   // characters for edges, index matches node
        var masks = [Int](repeating: 0, count: n)
        
        // DFS to compute mask for each node
        var stack: [(node: Int, mask: Int)] = [(0, 0)]
        while let (node, curMask) = stack.popLast() {
            masks[node] = curMask
            for child in children[node] {
                let chIdx = Int(sBytes[child] - 97)   // 'a' -> 0
                let newMask = curMask ^ (1 << chIdx)
                stack.append((child, newMask))
            }
        }
        
        var freq = [Int: Int]()
        var ans: Int64 = 0
        
        for m in masks {
            if let same = freq[m] {
                ans += Int64(same)          // xor == 0
            }
            for b in 0..<26 {               // xor has exactly one bit set
                let target = m ^ (1 << b)
                if let cnt = freq[target] {
                    ans += Int64(cnt)
                }
            }
            freq[m, default: 0] += 1
        }
        
        return Int(ans)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countPalindromePaths(parent: List<Int>, s: String): Long {
        val n = parent.size
        val mask = IntArray(n)
        val children = Array(n) { mutableListOf<Int>() }
        for (i in 1 until n) {
            val p = parent[i]
            children[p].add(i)
        }
        val stack = java.util.ArrayDeque<Int>()
        stack.add(0)
        mask[0] = 0
        while (!stack.isEmpty()) {
            val node = stack.removeLast()
            for (child in children[node]) {
                val bit = s[child] - 'a'
                mask[child] = mask[node] xor (1 shl bit)
                stack.add(child)
            }
        }

        val freq = java.util.HashMap<Int, Int>()
        var ans = 0L
        for (m in mask) {
            ans += freq.getOrDefault(m, 0).toLong()
            for (b in 0 until 26) {
                val m2 = m xor (1 shl b)
                ans += freq.getOrDefault(m2, 0).toLong()
            }
            freq[m] = freq.getOrDefault(m, 0) + 1
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int countPalindromePaths(List<int> parent, String s) {
    int n = parent.length;
    List<List<int>> children = List.generate(n, (_) => []);
    for (int i = 1; i < n; i++) {
      int p = parent[i];
      children[p].add(i);
    }

    List<int> mask = List.filled(n, 0);
    List<int> stack = [0];
    while (stack.isNotEmpty) {
      int node = stack.removeLast();
      for (int child in children[node]) {
        int bit = 1 << (s.codeUnitAt(child) - 97);
        mask[child] = mask[node] ^ bit;
        stack.add(child);
      }
    }

    Map<int, int> freq = {};
    int ans = 0;
    for (int i = 0; i < n; i++) {
      int m = mask[i];
      ans += freq[m] ?? 0;
      for (int b = 0; b < 26; b++) {
        int target = m ^ (1 << b);
        ans += freq[target] ?? 0;
      }
      freq[m] = (freq[m] ?? 0) + 1;
    }

    return ans;
  }
}
```

## Golang

```go
func countPalindromePaths(parent []int, s string) int64 {
    n := len(parent)
    masks := make([]int, n)
    for i := 1; i < n; i++ {
        p := parent[i]
        c := s[i] - 'a'
        masks[i] = masks[p] ^ (1 << uint(c))
    }
    freq := make(map[int]int64)
    var ans int64
    for _, m := range masks {
        if cnt, ok := freq[m]; ok {
            ans += cnt
        }
        for b := 0; b < 26; b++ {
            mm := m ^ (1 << b)
            if cnt, ok := freq[mm]; ok {
                ans += cnt
            }
        }
        freq[m]++
    }
    return ans
}
```

## Ruby

```ruby
def count_palindrome_paths(parent, s)
  n = parent.length
  children = Array.new(n) { [] }
  (1...n).each do |i|
    p = parent[i]
    children[p] << i
  end

  cnt = Hash.new(0)
  ans = 0
  stack = [[0, 0]] # [node, mask]

  while !stack.empty?
    node, mask = stack.pop

    ans += cnt[mask]
    26.times do |i|
      ans += cnt[mask ^ (1 << i)]
    end
    cnt[mask] += 1

    children[node].each do |ch|
      ch_mask = mask ^ (1 << (s.getbyte(ch) - 97))
      stack << [ch, ch_mask]
    end
  end

  ans
end
```

## Scala

```scala
import scala.collection.mutable.{ArrayBuffer, HashMap}

object Solution {
  def countPalindromePaths(parent: List[Int], s: String): Long = {
    val n = parent.length
    val par = parent.toArray
    // build children adjacency list
    val children = Array.fill(n)(new ArrayBuffer[Int]())
    var i = 1
    while (i < n) {
      children(par(i)).append(i)
      i += 1
    }

    // compute mask for each node (parity from root to node)
    val masks = new Array[Int](n)
    val stackNode = new Array[Int](n)
    val stackMask = new Array[Int](n)
    var top = 0
    stackNode(top) = 0
    stackMask(top) = 0
    while (top >= 0) {
      val node = stackNode(top)
      val curMask = stackMask(top)
      top -= 1
      masks(node) = curMask
      val chIter = children(node).iterator
      while (chIter.hasNext) {
        val child = chIter.next()
        val bit = 1 << (s.charAt(child) - 'a')
        top += 1
        stackNode(top) = child
        stackMask(top) = curMask ^ bit
      }
    }

    // count pairs using frequency map
    val freq = new HashMap[Int, Long]()
    var ans: Long = 0L
    i = 0
    while (i < n) {
      val m = masks(i)
      ans += freq.getOrElse(m, 0L)
      var b = 0
      while (b < 26) {
        val m2 = m ^ (1 << b)
        ans += freq.getOrElse(m2, 0L)
        b += 1
      }
      freq.put(m, freq.getOrElse(m, 0L) + 1L)
      i += 1
    }

    ans
  }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn count_palindrome_paths(parent: Vec<i32>, s: String) -> i64 {
        let n = parent.len();
        // Build adjacency list
        let mut children: Vec<Vec<usize>> = vec![Vec::new(); n];
        for i in 1..n {
            let p = parent[i] as usize;
            children[p].push(i);
        }
        let bytes = s.as_bytes();

        // Compute mask for each node using stack DFS
        let mut masks: Vec<u32> = vec![0; n];
        let mut stack: Vec<(usize, u32)> = Vec::new();
        stack.push((0, 0));
        while let Some((node, cur_mask)) = stack.pop() {
            masks[node] = cur_mask;
            for &ch in children[node].iter() {
                let bit = 1u32 << (bytes[ch] - b'a');
                stack.push((ch, cur_mask ^ bit));
            }
        }

        // Count pairs
        let mut cnt: HashMap<u32, i64> = HashMap::new();
        let mut ans: i64 = 0;
        for &m in masks.iter() {
            if let Some(c) = cnt.get(&m) {
                ans += *c;
            }
            for b in 0..26 {
                let m2 = m ^ (1u32 << b);
                if let Some(c) = cnt.get(&m2) {
                    ans += *c;
                }
            }
            *cnt.entry(m).or_insert(0) += 1;
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (count-palindrome-paths parent s)
  (-> (listof exact-integer?) string? exact-integer?)
  (let* ((n (length parent))
         (parent-vec (list->vector parent))
         (children (make-vector n '()))
         ;; build adjacency list of children
         (void
          (for ([i (in-range 1 n)])
            (let ((p (vector-ref parent-vec i)))
              (vector-set! children p (cons i (vector-ref children p))))))
         (masks (make-vector n 0))
         ;; compute mask for each node via DFS
         (stack (list (cons 0 0)))) ; pair: node . mask
    (let recur ()
      (unless (null? stack)
        (define cur (car stack))
        (set! stack (cdr stack))
        (define node (car cur))
        (define curmask (cdr cur))
        (vector-set! masks node curmask)
        (for ([child (in-list (vector-ref children node))])
          (let* ((ch (string-ref s child))
                 (bit (- (char->integer ch) (char->integer #\a)))
                 (newmask (bitwise-xor curmask (arithmetic-shift 1 bit))))
            (set! stack (cons (cons child newmask) stack))))
        (recur)))
    ;; count valid pairs
    (let ((cnt (make-hash))
          (ans 0))
      (for ([i (in-range n)])
        (define cur (vector-ref masks i))
        (set! ans (+ ans (hash-ref cnt cur 0))) ; xor == 0
        (for ([b (in-range 26)])
          (define target (bitwise-xor cur (arithmetic-shift 1 b)))
          (set! ans (+ ans (hash-ref cnt target 0))))
        (hash-set! cnt cur (+ (hash-ref cnt cur 0) 1)))
      ans)))
```

## Erlang

```erlang
-spec count_palindrome_paths(Parent :: [integer()], S :: unicode:unicode_binary()) -> integer().
count_palindrome_paths(Parent, S) ->
    N = length(Parent),
    CharList = binary_to_list(S),
    ParentT = list_to_tuple(Parent),
    CharT = list_to_tuple(CharList),

    %% Build adjacency map: Node -> [{Child,CharCode}]
    Adj = lists:foldl(
        fun(I, Acc) ->
            P = element(I + 1, ParentT),          % parent of node I
            C = element(I + 1, CharT),            % character code on edge (I,parent)
            maps:update_with(P,
                fun(L) -> [{I, C} | L] end,
                [{I, C}],
                Acc)
        end,
        #{},
        lists:seq(1, N - 1)),

    %% Depth‑first traversal counting valid pairs
    dfs([{0, 0}], Adj, #{}, 0).

%% ------------------------------------------------------------------
%% DFS stack processing
%% ------------------------------------------------------------------
dfs([], _Adj, _Freq, Ans) ->
    Ans;
dfs([{Node, Mask} | RestStack], Adj, Freq, Ans) ->
    CountSame = maps:get(Mask, Freq, 0),
    CountOneBit = count_one_bit_diff(Mask, Freq, 0),

    NewAns = Ans + CountSame + CountOneBit,
    NewFreq = maps:update_with(
        Mask,
        fun(C) -> C + 1 end,
        1,
        Freq),

    Children = maps:get(Node, Adj, []),
    NewStack = lists:foldl(
        fun({Child, CharCode}, Acc) ->
            CharMask = 1 bsl (CharCode - $a),
            [{Child, Mask bxor CharMask} | Acc]
        end,
        RestStack,
        Children),

    dfs(NewStack, Adj, NewFreq, NewAns).

%% ------------------------------------------------------------------
%% Sum frequencies of masks differing by exactly one bit
%% ------------------------------------------------------------------
count_one_bit_diff(_Mask, _Freq, Sum) when Sum >= 0 -> % placeholder to avoid warning
    count_one_bit_diff(0, _Mask, _Freq, Sum).

count_one_bit_diff(I, Mask, Freq, Sum) when I >= 26 ->
    Sum;
count_one_bit_diff(I, Mask, Freq, Sum) ->
    M2 = Mask bxor (1 bsl I),
    C = maps:get(M2, Freq, 0),
    count_one_bit_diff(I + 1, Mask, Freq, Sum + C).
```

## Elixir

```elixir
defmodule Solution do
  use Bitwise

  @spec count_palindrome_paths(parent :: [integer], s :: String.t) :: integer
  def count_palindrome_paths(parent, s) do
    n = length(parent)
    parent_t = List.to_tuple(parent)
    chars_t = String.to_charlist(s) |> List.to_tuple

    adj =
      Enum.reduce(1..(n - 1), %{}, fn i, acc ->
        p = elem(parent_t, i)

        acc
        |> Map.update(p, [i], &[i | &1])
        |> Map.update(i, [p], &[p | &1])
      end)

    dfs([{0, -1, 0}], adj, chars_t, %{}, 0)
  end

  defp dfs([], _adj, _chars_t, _freq, ans), do: ans

  defp dfs([{node, parent_node, mask} | rest], adj, chars_t, freq, ans) do
    same = Map.get(freq, mask, 0)
    ans1 = ans + same

    ans2 =
      Enum.reduce(0..25, ans1, fn b, acc ->
        other = mask ^ (1 <<< b)
        acc + Map.get(freq, other, 0)
      end)

    freq1 = Map.update(freq, mask, 1, &(&1 + 1))

    children = Map.get(adj, node, [])

    new_stack =
      Enum.reduce(children, rest, fn child, acc ->
        if child == parent_node do
          acc
        else
          char_code = elem(chars_t, child)
          bit = 1 <<< (char_code - ?a)
          child_mask = mask ^ bit
          [{child, node, child_mask} | acc]
        end
      end)

    dfs(new_stack, adj, chars_t, freq1, ans2)
  end
end
```
