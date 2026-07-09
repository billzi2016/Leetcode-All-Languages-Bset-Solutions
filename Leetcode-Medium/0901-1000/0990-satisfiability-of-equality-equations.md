# 0990. Satisfiability of Equality Equations

## Cpp

```cpp
class Solution {
public:
    bool equationsPossible(vector<string>& equations) {
        vector<int> parent(26);
        iota(parent.begin(), parent.end(), 0);
        function<int(int)> find = [&](int x) {
            return parent[x] == x ? x : parent[x] = find(parent[x]);
        };
        auto unite = [&](int a, int b) {
            int ra = find(a), rb = find(b);
            if (ra != rb) parent[ra] = rb;
        };
        
        // First handle all equalities
        for (const string& eq : equations) {
            if (eq[1] == '=') {
                int a = eq[0] - 'a';
                int b = eq[3] - 'a';
                unite(a, b);
            }
        }
        // Then check inequalities
        for (const string& eq : equations) {
            if (eq[1] == '!') {
                int a = eq[0] - 'a';
                int b = eq[3] - 'a';
                if (find(a) == find(b)) return false;
            }
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean equationsPossible(String[] equations) {
        int[] parent = new int[26];
        for (int i = 0; i < 26; i++) parent[i] = i;

        // Process all equalities
        for (String eq : equations) {
            if (eq.charAt(1) == '=') { // "=="
                int x = eq.charAt(0) - 'a';
                int y = eq.charAt(3) - 'a';
                union(parent, x, y);
            }
        }

        // Process all inequalities
        for (String eq : equations) {
            if (eq.charAt(1) == '!') { // "!="
                int x = eq.charAt(0) - 'a';
                int y = eq.charAt(3) - 'a';
                if (find(parent, x) == find(parent, y)) return false;
            }
        }

        return true;
    }

    private int find(int[] parent, int x) {
        if (parent[x] != x) {
            parent[x] = find(parent, parent[x]);
        }
        return parent[x];
    }

    private void union(int[] parent, int x, int y) {
        int rootX = find(parent, x);
        int rootY = find(parent, y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
        }
    }
}
```

## Python

```python
class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        parent = [i for i in range(26)]

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        # First, process all equalities
        for eq in equations:
            if eq[1] == '=':  # "=="
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')
                union(a, b)

        # Then, check inequalities
        for eq in equations:
            if eq[1] == '!':  # "!="
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')
                if find(a) == find(b):
                    return False
        return True
```

## Python3

```python
from typing import List

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [i for i in range(26)]

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x: int, y: int) -> None:
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry

        # Process all equalities
        for eq in equations:
            if eq[1] == '=':
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')
                union(a, b)

        # Check inequalities
        for eq in equations:
            if eq[1] == '!':
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')
                if find(a) == find(b):
                    return False
        return True
```

## C

```c
#include <stdbool.h>

static int parent[26];
static int rankArr[26];

static int find_set(int x) {
    if (parent[x] != x)
        parent[x] = find_set(parent[x]);
    return parent[x];
}

static void union_set(int a, int b) {
    int ra = find_set(a);
    int rb = find_set(b);
    if (ra == rb) return;
    if (rankArr[ra] < rankArr[rb]) {
        parent[ra] = rb;
    } else if (rankArr[ra] > rankArr[rb]) {
        parent[rb] = ra;
    } else {
        parent[rb] = ra;
        rankArr[ra]++;
    }
}

bool equationsPossible(char** equations, int equationsSize) {
    for (int i = 0; i < 26; ++i) {
        parent[i] = i;
        rankArr[i] = 0;
    }

    // Process all equalities first
    for (int i = 0; i < equationsSize; ++i) {
        char *eq = equations[i];
        if (eq[1] == '=' && eq[2] == '=') {
            int a = eq[0] - 'a';
            int b = eq[3] - 'a';
            union_set(a, b);
        }
    }

    // Then check inequalities
    for (int i = 0; i < equationsSize; ++i) {
        char *eq = equations[i];
        if (eq[1] == '!' && eq[2] == '=') {
            int a = eq[0] - 'a';
            int b = eq[3] - 'a';
            if (find_set(a) == find_set(b))
                return false;
        }
    }

    return true;
}
```

## Csharp

```csharp
public class Solution
{
    public bool EquationsPossible(string[] equations)
    {
        int[] parent = new int[26];
        for (int i = 0; i < 26; i++) parent[i] = i;

        foreach (var eq in equations)
        {
            if (eq[1] == '=' && eq[2] == '=')
            {
                int x = eq[0] - 'a';
                int y = eq[3] - 'a';
                Union(parent, x, y);
            }
        }

        foreach (var eq in equations)
        {
            if (eq[1] == '!' && eq[2] == '=')
            {
                int x = eq[0] - 'a';
                int y = eq[3] - 'a';
                if (Find(parent, x) == Find(parent, y))
                    return false;
            }
        }

        return true;
    }

    private int Find(int[] parent, int x)
    {
        if (parent[x] != x)
            parent[x] = Find(parent, parent[x]);
        return parent[x];
    }

    private void Union(int[] parent, int x, int y)
    {
        int px = Find(parent, x);
        int py = Find(parent, y);
        if (px != py) parent[px] = py;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} equations
 * @return {boolean}
 */
var equationsPossible = function(equations) {
    const parent = new Array(26).fill(0).map((_, i) => i);
    
    const find = (x) => {
        if (parent[x] !== x) parent[x] = find(parent[x]);
        return parent[x];
    };
    
    const union = (a, b) => {
        const ra = find(a), rb = find(b);
        if (ra !== rb) parent[ra] = rb;
    };
    
    // First pass: process all equalities
    for (const eq of equations) {
        if (eq[1] === '=') {
            const a = eq.charCodeAt(0) - 97;
            const b = eq.charCodeAt(3) - 97;
            union(a, b);
        }
    }
    
    // Second pass: process all inequalities
    for (const eq of equations) {
        if (eq[1] === '!') {
            const a = eq.charCodeAt(0) - 97;
            const b = eq.charCodeAt(3) - 97;
            if (find(a) === find(b)) return false;
        }
    }
    
    return true;
};
```

## Typescript

```typescript
function equationsPossible(equations: string[]): boolean {
    const parent = new Array(26);
    for (let i = 0; i < 26; i++) parent[i] = i;

    const find = (x: number): number => {
        if (parent[x] !== x) parent[x] = find(parent[x]);
        return parent[x];
    };

    const union = (a: number, b: number) => {
        const pa = find(a);
        const pb = find(b);
        if (pa !== pb) parent[pa] = pb;
    };

    // Process all equalities first
    for (const eq of equations) {
        if (eq[1] === '=') {
            const a = eq.charCodeAt(0) - 97;
            const b = eq.charCodeAt(3) - 97;
            union(a, b);
        }
    }

    // Then check inequalities
    for (const eq of equations) {
        if (eq[1] === '!') {
            const a = eq.charCodeAt(0) - 97;
            const b = eq.charCodeAt(3) - 97;
            if (find(a) === find(b)) return false;
        }
    }

    return true;
}
```

## Php

```php
class Solution {

    private $parent = [];

    private function find($x) {
        if ($this->parent[$x] != $x) {
            $this->parent[$x] = $this->find($this->parent[$x]);
        }
        return $this->parent[$x];
    }

    private function union($x, $y) {
        $rootX = $this->find($x);
        $rootY = $this->find($y);
        if ($rootX != $rootY) {
            $this->parent[$rootX] = $rootY;
        }
    }

    /**
     * @param String[] $equations
     * @return Boolean
     */
    function equationsPossible($equations) {
        // initialize union-find for 26 lowercase letters
        $this->parent = range(0, 25);

        // First pass: process all equality equations
        foreach ($equations as $eq) {
            if ($eq[1] == '=' && $eq[2] == '=') {
                $a = ord($eq[0]) - ord('a');
                $b = ord($eq[3]) - ord('a');
                $this->union($a, $b);
            }
        }

        // Second pass: process all inequality equations
        foreach ($equations as $eq) {
            if ($eq[1] == '!' && $eq[2] == '=') {
                $a = ord($eq[0]) - ord('a');
                $b = ord($eq[3]) - ord('a');
                if ($this->find($a) == $this->find($b)) {
                    return false;
                }
            }
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func equationsPossible(_ equations: [String]) -> Bool {
        var parent = Array(0..<26)
        
        func find(_ x: Int) -> Int {
            if parent[x] != x {
                parent[x] = find(parent[x])
            }
            return parent[x]
        }
        
        func union(_ x: Int, _ y: Int) {
            let rootX = find(x)
            let rootY = find(y)
            if rootX != rootY {
                parent[rootX] = rootY
            }
        }
        
        // First pass: process all equalities
        for eq in equations {
            let chars = Array(eq)
            if chars[1] == "=" { // "=="
                let a = Int(chars[0].unicodeScalars.first!.value - UnicodeScalar("a").value)
                let b = Int(chars[3].unicodeScalars.first!.value - UnicodeScalar("a").value)
                union(a, b)
            }
        }
        
        // Second pass: process all inequalities
        for eq in equations {
            let chars = Array(eq)
            if chars[1] == "!" { // "!="
                let a = Int(chars[0].unicodeScalars.first!.value - UnicodeScalar("a").value)
                let b = Int(chars[3].unicodeScalars.first!.value - UnicodeScalar("a").value)
                if find(a) == find(b) {
                    return false
                }
            }
        }
        
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun equationsPossible(equations: Array<String>): Boolean {
        val parent = IntArray(26) { it }
        val rank = IntArray(26)

        fun find(x: Int): Int {
            var p = x
            while (parent[p] != p) {
                parent[p] = parent[parent[p]]
                p = parent[p]
            }
            return p
        }

        fun union(a: Int, b: Int) {
            var ra = find(a)
            var rb = find(b)
            if (ra == rb) return
            when {
                rank[ra] < rank[rb] -> parent[ra] = rb
                rank[ra] > rank[rb] -> parent[rb] = ra
                else -> {
                    parent[rb] = ra
                    rank[ra]++
                }
            }
        }

        for (eq in equations) {
            if (eq[1] == '=') {
                val a = eq[0] - 'a'
                val b = eq[3] - 'a'
                union(a, b)
            }
        }

        for (eq in equations) {
            if (eq[1] == '!') {
                val a = eq[0] - 'a'
                val b = eq[3] - 'a'
                if (find(a) == find(b)) return false
            }
        }

        return true
    }
}
```

## Dart

```dart
class Solution {
  bool equationsPossible(List<String> equations) {
    // Union-Find for 26 lowercase letters
    List<int> parent = List<int>.generate(26, (i) => i);
    int find(int x) {
      if (parent[x] != x) {
        parent[x] = find(parent[x]);
      }
      return parent[x];
    }
    void union(int a, int b) {
      int pa = find(a);
      int pb = find(b);
      if (pa != pb) {
        parent[pa] = pb;
      }
    }

    // First pass: process all equalities
    for (var eq in equations) {
      if (eq[1] == '=' && eq[2] == '=') {
        int a = eq.codeUnitAt(0) - 97; // 'a' ascii is 97
        int b = eq.codeUnitAt(3) - 97;
        union(a, b);
      }
    }

    // Second pass: process all inequalities
    for (var eq in equations) {
      if (eq[1] == '!' && eq[2] == '=') {
        int a = eq.codeUnitAt(0) - 97;
        int b = eq.codeUnitAt(3) - 97;
        if (find(a) == find(b)) return false;
      }
    }

    return true;
  }
}
```

## Golang

```go
func equationsPossible(equations []string) bool {
    // Union-Find for 26 lowercase letters
    parent := make([]int, 26)
    for i := 0; i < 26; i++ {
        parent[i] = i
    }
    var find func(int) int
    find = func(x int) int {
        if parent[x] != x {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }
    union := func(a, b int) {
        ra, rb := find(a), find(b)
        if ra != rb {
            parent[ra] = rb
        }
    }

    // First pass: process all equalities
    for _, eq := range equations {
        if eq[1] == '=' { // "=="
            a := int(eq[0] - 'a')
            b := int(eq[3] - 'a')
            union(a, b)
        }
    }

    // Second pass: check inequalities
    for _, eq := range equations {
        if eq[1] == '!' { // "!="
            a := int(eq[0] - 'a')
            b := int(eq[3] - 'a')
            if find(a) == find(b) {
                return false
            }
        }
    }
    return true
}
```

## Ruby

```ruby
def equations_possible(equations)
  parent = Array.new(26) { |i| i }

  define_method(:find) do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end

  define_method(:union) do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    parent[ra] = rb unless ra == rb
  end

  # First pass: process all equalities
  equations.each do |eq|
    if eq[1] == '='
      a = eq[0].ord - 97
      b = eq[3].ord - 97
      union.call(a, b)
    end
  end

  # Second pass: check inequalities
  equations.each do |eq|
    if eq[1] == '!'
      a = eq[0].ord - 97
      b = eq[3].ord - 97
      return false if find.call(a) == find.call(b)
    end
  end

  true
end
```

## Scala

```scala
object Solution {
    def equationsPossible(equations: Array[String]): Boolean = {
        val parent = (0 until 26).toArray

        def find(x: Int): Int = {
            var p = x
            while (parent(p) != p) {
                parent(p) = parent(parent(p))
                p = parent(p)
            }
            p
        }

        def union(a: Int, b: Int): Unit = {
            val ra = find(a)
            val rb = find(b)
            if (ra != rb) parent(ra) = rb
        }

        // Process all equalities first
        for (eq <- equations) {
            if (eq.charAt(1) == '=') {
                val a = eq.charAt(0) - 'a'
                val b = eq.charAt(3) - 'a'
                union(a, b)
            }
        }

        // Then check inequalities
        for (eq <- equations) {
            if (eq.charAt(1) == '!') {
                val a = eq.charAt(0) - 'a'
                val b = eq.charAt(3) - 'a'
                if (find(a) == find(b)) return false
            }
        }

        true
    }
}
```

## Rust

```rust
struct UnionFind {
    parent: [usize; 26],
}

impl UnionFind {
    fn new() -> Self {
        let mut p = [0usize; 26];
        for i in 0..26 {
            p[i] = i;
        }
        UnionFind { parent: p }
    }

    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] != x {
            let root = self.find(self.parent[x]);
            self.parent[x] = root;
        }
        self.parent[x]
    }

    fn union(&mut self, a: usize, b: usize) {
        let ra = self.find(a);
        let rb = self.find(b);
        if ra != rb {
            self.parent[ra] = rb;
        }
    }
}

impl Solution {
    pub fn equations_possible(equations: Vec<String>) -> bool {
        let mut uf = UnionFind::new();

        // Process all equality equations first
        for eq in &equations {
            let bytes = eq.as_bytes();
            if bytes[1] == b'=' && bytes[2] == b'=' {
                let a = (bytes[0] - b'a') as usize;
                let b = (bytes[3] - b'a') as usize;
                uf.union(a, b);
            }
        }

        // Then check inequality equations
        for eq in &equations {
            let bytes = eq.as_bytes();
            if bytes[1] == b'!' && bytes[2] == b'=' {
                let a = (bytes[0] - b'a') as usize;
                let b = (bytes[3] - b'a') as usize;
                if uf.find(a) == uf.find(b) {
                    return false;
                }
            }
        }

        true
    }
}
```

## Racket

```racket
(define/contract (equations-possible equations)
  (-> (listof string?) boolean?)
  (let ([parent (make-vector 26)])
    ;; initialize parent pointers
    (for ([i (in-range 26)]) (vector-set! parent i i))
    (define (find x)
      (let loop ((x x))
        (let ([p (vector-ref parent x)])
          (if (= p x)
              x
              (let ([root (loop p)])
                (vector-set! parent x root)
                root)))))
    (define (union a b)
      (let ([ra (find a)] [rb (find b)])
        (when (not (= ra rb))
          (vector-set! parent ra rb))))
    ;; first pass: process all "=="
    (for ([eq equations])
      (when (char=? (string-ref eq 1) #\=)
        (let* ([a (- (char->integer (string-ref eq 0)) (char->integer #\a))]
               [b (- (char->integer (string-ref eq 3)) (char->integer #\a))])
          (union a b))))
    ;; second pass: check all "!="
    (let ([conflict #f])
      (for ([eq equations])
        (when (and (not conflict) (char=? (string-ref eq 1) #\!))
          (let* ([a (- (char->integer (string-ref eq 0)) (char->integer #\a))]
                 [b (- (char->integer (string-ref eq 3)) (char->integer #\a))])
            (when (= (find a) (find b))
              (set! conflict #t)))))
      (not conflict))))
```

## Erlang

```erlang
-module(solution).
-export([equations_possible/1]).

-spec equations_possible(Equations :: [unicode:unicode_binary()]) -> boolean().
equations_possible(Equations) ->
    Parent0 = list_to_tuple(lists:seq(0, 25)),
    Parent1 = lists:foldl(fun(Eq, Par) ->
        case binary:at(Eq, 1) of
            $= ->
                X = idx(binary:at(Eq, 0)),
                Y = idx(binary:at(Eq, 3)),
                union(Par, X, Y);
            _ -> Par
        end
    end, Parent0, Equations),
    case lists:any(fun(Eq) ->
        case binary:at(Eq, 1) of
            $! ->
                X = idx(binary:at(Eq, 0)),
                Y = idx(binary:at(Eq, 3)),
                {RootX, _} = find(Parent1, X),
                {RootY, _} = find(Parent1, Y),
                RootX == RootY;
            _ -> false
        end
    end, Equations) of
        true -> false;
        false -> true
    end.

idx(Char) ->
    Char - $a.

find(Parent, X) ->
    case element(X + 1, Parent) of
        X ->
            {X, Parent};
        P ->
            {Root, NewParent} = find(Parent, P),
            UpdatedParent = setelement(X + 1, NewParent, Root),
            {Root, UpdatedParent}
    end.

union(Parent, X, Y) ->
    {RootX, Parent1} = find(Parent, X),
    {RootY, Parent2} = find(Parent1, Y),
    if
        RootX == RootY -> Parent2;
        true -> setelement(RootX + 1, Parent2, RootY)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec equations_possible(equations :: [String.t]) :: boolean
  def equations_possible(equations) do
    parent = init_parent()

    parent_eq =
      Enum.reduce(equations, parent, fn eq, acc ->
        <<v1, o1, o2, v2>> = eq

        if o1 == ?= and o2 == ?= do
          union(acc, v1 - ?a, v2 - ?a)
        else
          acc
        end
      end)

    Enum.reduce_while(equations, true, fn eq, _acc ->
      <<v1, o1, o2, v2>> = eq

      if o1 == ?! do
        r1 = root(parent_eq, v1 - ?a)
        r2 = root(parent_eq, v2 - ?a)

        if r1 == r2 do
          {:halt, false}
        else
          {:cont, true}
        end
      else
        {:cont, true}
      end
    end)
  end

  defp init_parent do
    Enum.reduce(0..25, %{}, fn i, acc -> Map.put(acc, i, i) end)
  end

  defp find(parent, x) do
    p = Map.get(parent, x)

    if p == x do
      {parent, x}
    else
      {parent2, root} = find(parent, p)
      new_parent = Map.put(parent2, x, root)
      {new_parent, root}
    end
  end

  defp union(parent, x, y) do
    {parent1, rx} = find(parent, x)
    {parent2, ry} = find(parent1, y)

    if rx != ry do
      Map.put(parent2, rx, ry)
    else
      parent2
    end
  end

  defp root(parent, x) do
    p = Map.get(parent, x)

    if p == x do
      x
    else
      root(parent, p)
    end
  end
end
```
