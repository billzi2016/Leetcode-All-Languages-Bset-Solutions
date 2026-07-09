# 0753. Cracking the Safe

## Cpp

```cpp
class Solution {
    int K;
    std::unordered_set<std::string> vis;
    std::string ans;
    
    void dfs(const std::string& node) {
        for (int i = 0; i < K; ++i) {
            std::string edge = node + char('0' + i);
            if (vis.insert(edge).second) { // not visited before
                dfs(edge.substr(1));
                ans.push_back(char('0' + i));
            }
        }
    }
public:
    std::string crackSafe(int n, int k) {
        K = k;
        std::string start(n > 1 ? n - 1 : 0, '0');
        dfs(start);
        return start + ans;
    }
};
```

## Java

```java
class Solution {
    public String crackSafe(int n, int k) {
        if (n == 0) return "";
        int mod = (int) Math.pow(k, n - 1);
        int totalEdges = (int) Math.pow(k, n);
        boolean[] visited = new boolean[totalEdges];
        StringBuilder sb = new StringBuilder();
        dfs(0, k, mod, visited, sb);
        // prepend (n-1) zeros
        for (int i = 0; i < n - 1; ++i) {
            sb.append('0');
        }
        return sb.reverse().toString();
    }

    private void dfs(int node, int k, int mod, boolean[] visited, StringBuilder sb) {
        for (int d = 0; d < k; ++d) {
            int edge = node * k + d;
            if (!visited[edge]) {
                visited[edge] = true;
                int nextNode = edge % mod;
                dfs(nextNode, k, mod, visited, sb);
                sb.append((char) ('0' + d));
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        visited = set()
        ans = []

        start = "0" * (n - 1)

        def dfs(node):
            for x in range(k):
                edge = node + str(x)
                if edge not in visited:
                    visited.add(edge)
                    dfs(edge[1:])
                    ans.append(str(x))

        dfs(start)
        return start + "".join(reversed(ans))
```

## Python3

```python
import sys
from collections import defaultdict

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        sys.setrecursionlimit(10000)
        start = '0' * (n - 1)
        nxt = defaultdict(int)
        seq = []

        def dfs(node: str):
            while nxt[node] < k:
                x = nxt[node]
                nxt[node] += 1
                next_node = node[1:] + str(x) if n > 1 else ''
                dfs(next_node)
                seq.append(str(x))

        dfs(start)
        return start + ''.join(reversed(seq))
```

## C

```c
#include <stdlib.h>

static void dfs(int node, int k, int totalNodes, int *edgeIdx, char *edgesRes, int *pos) {
    while (edgeIdx[node] < k) {
        int digit = edgeIdx[node]++;
        int nextNode = (node * k + digit) % totalNodes;
        dfs(nextNode, k, totalNodes, edgeIdx, edgesRes, pos);
        edgesRes[(*pos)++] = '0' + digit;
    }
}

char* crackSafe(int n, int k) {
    int totalEdges = 1;
    for (int i = 0; i < n; ++i) totalEdges *= k;

    int totalNodes = (n == 1) ? 1 : totalEdges / k; // k^(n-1)

    int *edgeIdx = (int *)calloc(totalNodes, sizeof(int));
    char *edgesRes = (char *)malloc(totalEdges);
    int pos = 0;

    dfs(0, k, totalNodes, edgeIdx, edgesRes, &pos);

    int resultLen = totalEdges + n - 1;
    char *ans = (char *)malloc(resultLen + 1); // +1 for null terminator

    int idx = 0;
    for (int i = 0; i < n - 1; ++i) ans[idx++] = '0';

    for (int i = totalEdges - 1; i >= 0; --i) {
        ans[idx++] = edgesRes[i];
    }
    ans[idx] = '\0';

    free(edgeIdx);
    free(edgesRes);
    return ans;
}
```

## Csharp

```csharp
public class Solution
{
    public string CrackSafe(int n, int k)
    {
        var visited = new HashSet<string>();
        var sb = new System.Text.StringBuilder();
        string start = new string('0', n - 1);

        void Dfs(string node)
        {
            for (int i = 0; i < k; i++)
            {
                string edge = node + i;
                if (!visited.Contains(edge))
                {
                    visited.Add(edge);
                    Dfs(edge.Substring(1));
                    sb.Append(i);
                }
            }
        }

        Dfs(start);

        var chars = sb.ToString().ToCharArray();
        System.Array.Reverse(chars);
        return start + new string(chars);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var crackSafe = function(n, k) {
    const start = '0'.repeat(n - 1);
    const visited = new Set();
    const ans = [];

    function dfs(node) {
        for (let x = 0; x < k; ++x) {
            const edge = node + x;
            if (!visited.has(edge)) {
                visited.add(edge);
                dfs(edge.slice(1));
                ans.push(x);
            }
        }
    }

    dfs(start);
    return start + ans.reverse().join('');
};
```

## Typescript

```typescript
function crackSafe(n: number, k: number): string {
    const visited = new Set<string>();
    const sequence: number[] = [];

    function dfs(node: string) {
        for (let i = 0; i < k; i++) {
            const edge = node + i;
            if (!visited.has(edge)) {
                visited.add(edge);
                dfs(edge.slice(1));
                sequence.push(i);
            }
        }
    }

    const start = '0'.repeat(n - 1);
    dfs(start);
    return start + sequence.reverse().join('');
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return String
     */
    function crackSafe($n, $k) {
        $node = str_repeat('0', $n - 1);
        $visited = [];
        $sequence = [];

        $dfs = function ($curr) use (&$dfs, &$visited, $k, &$sequence) {
            for ($i = 0; $i < $k; $i++) {
                $edge = $curr . $i;
                if (!isset($visited[$edge])) {
                    $visited[$edge] = true;
                    $next = substr($edge, 1);
                    $dfs($next);
                    $sequence[] = (string)$i;
                }
            }
        };

        $dfs($node);
        return $node . implode('', array_reverse($sequence));
    }
}
```

## Swift

```swift
class Solution {
    func crackSafe(_ n: Int, _ k: Int) -> String {
        func intPow(_ base: Int, _ exp: Int) -> Int {
            var result = 1
            for _ in 0..<exp { result *= base }
            return result
        }
        
        let totalEdges = intPow(k, n)               // k^n
        let nodeBase = intPow(k, max(0, n - 1))     // k^(n-1)
        var visited = [Bool](repeating: false, count: totalEdges)
        var seq = [Character]()
        
        func dfs(_ node: Int) {
            for d in 0..<k {
                let edge = node * k + d
                if !visited[edge] {
                    visited[edge] = true
                    let nextNode = edge % nodeBase   // drop the oldest digit
                    dfs(nextNode)
                    seq.append(Character(UnicodeScalar(d + 48)!))
                }
            }
        }
        
        dfs(0)
        let prefix = String(repeating: "0", count: n - 1)
        return prefix + String(seq.reversed())
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun crackSafe(n: Int, k: Int): String {
        val start = "0".repeat(n - 1)
        val visited = HashSet<String>()
        val path = StringBuilder()
        fun dfs(node: String) {
            for (i in 0 until k) {
                val edge = node + i
                if (!visited.contains(edge)) {
                    visited.add(edge)
                    dfs(edge.substring(1))
                    path.append(i)
                }
            }
        }
        dfs(start)
        val result = StringBuilder()
        result.append(start)
        for (i in path.length - 1 downTo 0) {
            result.append(path[i])
        }
        return result.toString()
    }
}
```

## Dart

```dart
class Solution {
  String crackSafe(int n, int k) {
    int powK(int base, int exp) {
      int res = 1;
      for (int i = 0; i < exp; i++) res *= base;
      return res;
    }

    int totalEdges = powK(k, n);
    int mod = powK(k, n - 1); // number of nodes, k^(n-1)
    List<bool> visited = List.filled(totalEdges, false);
    List<int> path = [];

    void dfs(int node) {
      for (int digit = 0; digit < k; digit++) {
        int edgeId = node * k + digit;
        if (!visited[edgeId]) {
          visited[edgeId] = true;
          int nextNode = (node * k + digit) % mod;
          dfs(nextNode);
          path.add(digit);
        }
      }
    }

    dfs(0);

    StringBuffer sb = StringBuffer();
    // prepend n-1 zeros
    for (int i = 0; i < n - 1; i++) sb.write('0');
    // append reversed path digits
    for (int i = path.length - 1; i >= 0; i--) {
      sb.write(path[i].toString());
    }
    return sb.toString();
  }
}
```

## Golang

```go
func ipow(a, b int) int {
	result := 1
	for b > 0 {
		if b&1 == 1 {
			result *= a
		}
		a *= a
		b >>= 1
	}
	return result
}

func crackSafe(n int, k int) string {
	total := ipow(k, n)
	mod := 1
	if n > 1 {
		mod = ipow(k, n-1)
	}
	visited := make([]bool, total)
	sb := make([]byte, 0, total)

	var dfs func(node int)
	dfs = func(node int) {
		for d := 0; d < k; d++ {
			edgeID := node*k + d
			if !visited[edgeID] {
				visited[edgeID] = true
				nextNode := (node*k + d) % mod
				dfs(nextNode)
				sb = append(sb, byte('0'+d))
			}
		}
	}

	dfs(0)

	res := make([]byte, 0, total+n-1)
	for i := 0; i < n-1; i++ {
		res = append(res, '0')
	}
	for i := len(sb) - 1; i >= 0; i-- {
		res = append(res, sb[i])
	}
	return string(res)
}
```

## Ruby

```ruby
def crack_safe(n, k)
  mod = k ** (n - 1)
  edges = Array.new(mod) { [] }
  0.upto(mod - 1) do |node|
    (0...k).each { |d| edges[node] << d }
  end
  ans = []
  dfs = nil
  dfs = lambda do |node|
    while !edges[node].empty?
      d = edges[node].pop
      next_node = ((node * k + d) % mod)
      dfs.call(next_node)
      ans << d
    end
  end
  dfs.call(0)
  ("0" * (n - 1)) + ans.reverse.map(&:to_s).join
end
```

## Scala

```scala
object Solution {
    def crackSafe(n: Int, k: Int): String = {
        val pow = Math.pow(k.toDouble, (n - 1).toDouble).toInt
        val totalEdges = pow * k
        val visited = new Array[Boolean](totalEdges)
        val sb = new StringBuilder

        def dfs(node: Int): Unit = {
            var d = 0
            while (d < k) {
                val edge = node * k + d
                if (!visited(edge)) {
                    visited(edge) = true
                    val nextNode = ((node % pow) * k + d)
                    dfs(nextNode)
                    sb.append(d)
                }
                d += 1
            }
        }

        dfs(0)

        val result = new StringBuilder
        // prepend (n-1) zeros as the starting node
        for (_ <- 0 until n - 1) result.append('0')
        // append the recorded digits in reverse order
        var i = sb.length - 1
        while (i >= 0) {
            result.append(sb.charAt(i))
            i -= 1
        }
        result.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn crack_safe(n: i32, k: i32) -> String {
        fn dfs(node: usize, k: usize, mod_val: usize, visited: &mut Vec<bool>, ans: &mut Vec<char>) {
            for x in 0..k {
                let edge = node * k + x;
                if !visited[edge] {
                    visited[edge] = true;
                    let next_node = edge % mod_val;
                    dfs(next_node, k, mod_val, visited, ans);
                    ans.push((b'0' + x as u8) as char);
                }
            }
        }

        let k_usize = k as usize;
        let n_usize = n as usize;

        let total_edges = k_usize.pow(n as u32);
        let mod_val = if n == 1 { 1 } else { k_usize.pow((n - 1) as u32) };

        let mut visited = vec![false; total_edges];
        let mut ans: Vec<char> = Vec::new();

        dfs(0, k_usize, mod_val, &mut visited, &mut ans);

        let mut result = String::new();
        for _ in 0..n_usize.saturating_sub(1) {
            result.push('0');
        }
        for c in ans.iter().rev() {
            result.push(*c);
        }
        result
    }
}
```

## Racket

```racket
(define/contract (crack-safe n k)
  (-> exact-integer? exact-integer? string?)
  (let* ((mod (if (= n 1) 1 (expt k (- n 1))))
         (next-index (make-vector mod 0))
         (ans '()))
    (define (dfs u)
      (let loop ()
        (let ((idx (vector-ref next-index u)))
          (when (< idx k)
            (vector-set! next-index u (+ idx 1))
            (let* ((d idx)
                   (v (if (= n 1) 0 (modulo (+ (* u k) d) mod))))
              (dfs v)
              (set! ans (cons (integer->char (+ 48 d)) ans)))
            (loop)))))
    (dfs 0)
    (let* ((prefix (make-string (- n 1) #\0))
           (suffix (list->string (reverse ans))))
      (string-append prefix suffix))))
```

## Erlang

```erlang
-spec crack_safe(N :: integer(), K :: integer()) -> unicode:unicode_binary().
crack_safe(N, K) ->
    Mod = pow_int(K, N - 1),
    {_, Digits} = dfs(0, K, Mod, #{}),
    RevDigits = lists:reverse(Digits),
    Prefix = if
        N > 1 -> lists:duplicate(N - 1, $0);
        true -> []
    end,
    Chars = Prefix ++ [ $0 + D || D <- RevDigits ],
    list_to_binary(Chars).

pow_int(_, 0) -> 1;
pow_int(Base, Exp) when Exp > 0 ->
    Base * pow_int(Base, Exp - 1).

dfs(Node, K, Mod, Visited) ->
    {Visited2, Digits} = lists:foldl(
        fun(D, {VisAcc, Acc}) ->
            Edge = Node * K + D,
            case maps:is_key(Edge, VisAcc) of
                true -> {VisAcc, Acc};
                false ->
                    Vis1 = maps:put(Edge, true, VisAcc),
                    NextNode = Edge rem Mod,
                    {Vis2, SubAcc} = dfs(NextNode, K, Mod, Vis1),
                    {Vis2, SubAcc ++ [D] ++ Acc}
            end
        end,
        {Visited, []},
        lists:seq(0, K - 1)
    ),
    {Visited2, Digits}.
```

## Elixir

```elixir
defmodule Solution do
  @spec crack_safe(n :: integer, k :: integer) :: String.t()
  def crack_safe(n, k) do
    mod = :math.pow(k, n - 1) |> trunc()
    start_node = 0

    {_, digits_rev} = dfs(start_node, k, mod, %{}, [])
    prefix = if n > 1, do: String.duplicate("0", n - 1), else: ""
    prefix <> Enum.join(digits_rev)
  end

  defp dfs(node, k, mod, idx_map, acc) do
    {cnt, idx_map} = Map.get_and_update(idx_map, node, fn
      nil -> {0, 1}
      cnt when cnt < k - 1 -> {cnt, cnt + 1}
      cnt -> {cnt, cnt}
    end)

    if cnt < k do
      d = cnt
      next_node = rem(node * k + d, mod)
      {idx_map, acc} = dfs(next_node, k, mod, idx_map, acc)
      acc = [Integer.to_string(d) | acc]
      dfs(node, k, mod, idx_map, acc)
    else
      {idx_map, acc}
    end
  end
end
```
