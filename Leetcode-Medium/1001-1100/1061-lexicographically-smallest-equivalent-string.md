# 1061. Lexicographically Smallest Equivalent String

## Cpp

```cpp
class Solution {
public:
    string smallestEquivalentString(string s1, string s2, string baseStr) {
        vector<int> parent(26);
        iota(parent.begin(), parent.end(), 0);
        
        function<int(int)> find = [&](int x) -> int {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        };
        
        auto unite = [&](int a, int b) {
            int ra = find(a), rb = find(b);
            if (ra == rb) return;
            if (ra < rb) parent[rb] = ra;
            else parent[ra] = rb;
        };
        
        for (size_t i = 0; i < s1.size(); ++i) {
            unite(s1[i] - 'a', s2[i] - 'a');
        }
        
        string result;
        result.reserve(baseStr.size());
        for (char c : baseStr) {
            int r = find(c - 'a');
            result.push_back(char('a' + r));
        }
        return result;
    }
};
```

## Java

```java
class Solution {
    private int[] parent = new int[26];

    private int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    private void union(int a, int b) {
        int ra = find(a);
        int rb = find(b);
        if (ra == rb) return;
        // attach larger root to smaller root to keep minimal character as representative
        if (ra < rb) {
            parent[rb] = ra;
        } else {
            parent[ra] = rb;
        }
    }

    public String smallestEquivalentString(String s1, String s2, String baseStr) {
        for (int i = 0; i < 26; i++) parent[i] = i;

        int n = s1.length();
        for (int i = 0; i < n; i++) {
            int a = s1.charAt(i) - 'a';
            int b = s2.charAt(i) - 'a';
            union(a, b);
        }

        StringBuilder sb = new StringBuilder();
        for (char ch : baseStr.toCharArray()) {
            int idx = ch - 'a';
            int rep = find(idx);
            sb.append((char) ('a' + rep));
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        parent = list(range(26))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            # attach larger index to smaller to keep smallest lexicographic root
            if ra < rb:
                parent[rb] = ra
            else:
                parent[ra] = rb

        for c1, c2 in zip(s1, s2):
            union(ord(c1) - 97, ord(c2) - 97)

        result = []
        for ch in baseStr:
            root = find(ord(ch) - 97)
            result.append(chr(root + 97))
        return ''.join(result)
```

## Python3

```python
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            # make the smaller character the root
            if ra < rb:
                parent[rb] = ra
            else:
                parent[ra] = rb

        for c1, c2 in zip(s1, s2):
            union(ord(c1) - 97, ord(c2) - 97)

        # compress all paths to ensure direct mapping
        for i in range(26):
            parent[i] = find(i)

        result = []
        for ch in baseStr:
            idx = ord(ch) - 97
            result.append(chr(parent[idx] + 97))
        return ''.join(result)
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int parent[26];

static int find_set(int x) {
    if (parent[x] != x)
        parent[x] = find_set(parent[x]);
    return parent[x];
}

static void union_set(char a, char b) {
    int ra = find_set(a - 'a');
    int rb = find_set(b - 'a');
    if (ra == rb) return;
    if (ra < rb)
        parent[rb] = ra;
    else
        parent[ra] = rb;
}

char* smallestEquivalentString(char* s1, char* s2, char* baseStr) {
    for (int i = 0; i < 26; ++i) parent[i] = i;

    size_t len = strlen(s1);
    for (size_t i = 0; i < len; ++i)
        union_set(s1[i], s2[i]);

    size_t n = strlen(baseStr);
    char* res = (char*)malloc(n + 1);
    for (size_t i = 0; i < n; ++i) {
        int r = find_set(baseStr[i] - 'a');
        res[i] = (char)(r + 'a');
    }
    res[n] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string SmallestEquivalentString(string s1, string s2, string baseStr)
    {
        int[] parent = new int[26];
        for (int i = 0; i < 26; i++) parent[i] = i;

        int Find(int x)
        {
            if (parent[x] != x) parent[x] = Find(parent[x]);
            return parent[x];
        }

        void Union(int a, int b)
        {
            int ra = Find(a);
            int rb = Find(b);
            if (ra == rb) return;
            if (ra < rb) parent[rb] = ra;
            else parent[ra] = rb;
        }

        for (int i = 0; i < s1.Length; i++)
        {
            Union(s1[i] - 'a', s2[i] - 'a');
        }

        var sb = new System.Text.StringBuilder();
        foreach (char ch in baseStr)
        {
            int r = Find(ch - 'a');
            sb.Append((char)('a' + r));
        }
        return sb.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} baseStr
 * @return {string}
 */
var smallestEquivalentString = function(s1, s2, baseStr) {
    const parent = new Array(26);
    for (let i = 0; i < 26; i++) parent[i] = i;

    const find = (x) => {
        if (parent[x] !== x) parent[x] = find(parent[x]);
        return parent[x];
    };

    const union = (a, b) => {
        let ra = find(a), rb = find(b);
        if (ra === rb) return;
        // keep the smaller character as root
        if (ra < rb) parent[rb] = ra;
        else parent[ra] = rb;
    };

    for (let i = 0; i < s1.length; i++) {
        const a = s1.charCodeAt(i) - 97;
        const b = s2.charCodeAt(i) - 97;
        union(a, b);
    }

    let result = '';
    for (const ch of baseStr) {
        const idx = ch.charCodeAt(0) - 97;
        const rep = find(idx);
        result += String.fromCharCode(rep + 97);
    }
    return result;
};
```

## Typescript

```typescript
function smallestEquivalentString(s1: string, s2: string, baseStr: string): string {
    const parent = new Array(26);
    for (let i = 0; i < 26; i++) parent[i] = i;

    const find = (x: number): number => {
        if (parent[x] !== x) parent[x] = find(parent[x]);
        return parent[x];
    };

    const union = (a: number, b: number) => {
        let ra = find(a);
        let rb = find(b);
        if (ra === rb) return;
        // attach larger root to smaller (lexicographically smallest)
        if (ra < rb) {
            parent[rb] = ra;
        } else {
            parent[ra] = rb;
        }
    };

    const n = s1.length;
    for (let i = 0; i < n; i++) {
        const a = s1.charCodeAt(i) - 97;
        const b = s2.charCodeAt(i) - 97;
        union(a, b);
    }

    let result = '';
    for (const ch of baseStr) {
        const idx = ch.charCodeAt(0) - 97;
        const root = find(idx);
        result += String.fromCharCode(root + 97);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @param String $baseStr
     * @return String
     */
    function smallestEquivalentString($s1, $s2, $baseStr) {
        // Initialize Union-Find parent array for 26 letters
        $parent = range(0, 25);

        // Find with path compression
        $find = function($x) use (&$parent, &$find) {
            if ($parent[$x] !== $x) {
                $parent[$x] = $find($parent[$x]);
            }
            return $parent[$x];
        };

        $len = strlen($s1);
        for ($i = 0; $i < $len; $i++) {
            $a = ord($s1[$i]) - 97;
            $b = ord($s2[$i]) - 97;

            $ra = $find($a);
            $rb = $find($b);

            if ($ra !== $rb) {
                // Attach the larger root to the smaller (lexicographically smallest)
                if ($ra < $rb) {
                    $parent[$rb] = $ra;
                } else {
                    $parent[$ra] = $rb;
                }
            }
        }

        // Build result using the smallest equivalent character for each in baseStr
        $result = '';
        $bLen = strlen($baseStr);
        for ($i = 0; $i < $bLen; $i++) {
            $cIdx = ord($baseStr[$i]) - 97;
            $root = $find($cIdx);
            $result .= chr($root + 97);
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func smallestEquivalentString(_ s1: String, _ s2: String, _ baseStr: String) -> String {
        var parent = Array(0..<26)
        
        func find(_ x: Int) -> Int {
            if parent[x] != x {
                parent[x] = find(parent[x])
            }
            return parent[x]
        }
        
        func union(_ a: Int, _ b: Int) {
            let ra = find(a)
            let rb = find(b)
            if ra == rb { return }
            if ra < rb {
                parent[rb] = ra
            } else {
                parent[ra] = rb
            }
        }
        
        let arr1 = Array(s1.utf8)
        let arr2 = Array(s2.utf8)
        for i in 0..<arr1.count {
            let a = Int(arr1[i] - 97)
            let b = Int(arr2[i] - 97)
            union(a, b)
        }
        
        var result = ""
        for ch in baseStr.utf8 {
            let idx = Int(ch - 97)
            let root = find(idx)
            let newChar = Character(UnicodeScalar(root + 97)!)
            result.append(newChar)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun smallestEquivalentString(s1: String, s2: String, baseStr: String): String {
        val parent = IntArray(26) { it }

        fun find(x: Int): Int {
            if (parent[x] != x) {
                parent[x] = find(parent[x])
            }
            return parent[x]
        }

        fun union(a: Int, b: Int) {
            var ra = find(a)
            var rb = find(b)
            if (ra == rb) return
            if (ra < rb) {
                parent[rb] = ra
            } else {
                parent[ra] = rb
            }
        }

        for (i in s1.indices) {
            union(s1[i] - 'a', s2[i] - 'a')
        }

        val sb = StringBuilder()
        for (ch in baseStr) {
            val root = find(ch - 'a')
            sb.append('a' + root)
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String smallestEquivalentString(String s1, String s2, String baseStr) {
    List<int> parent = List.generate(26, (i) => i);

    int find(int x) {
      if (parent[x] != x) {
        parent[x] = find(parent[x]);
      }
      return parent[x];
    }

    void union(int a, int b) {
      int ra = find(a);
      int rb = find(b);
      if (ra == rb) return;
      if (ra < rb) {
        parent[rb] = ra;
      } else {
        parent[ra] = rb;
      }
    }

    for (int i = 0; i < s1.length; ++i) {
      int a = s1.codeUnitAt(i) - 97;
      int b = s2.codeUnitAt(i) - 97;
      union(a, b);
    }

    StringBuffer sb = StringBuffer();
    for (int i = 0; i < baseStr.length; ++i) {
      int idx = baseStr.codeUnitAt(i) - 97;
      int r = find(idx);
      sb.writeCharCode(r + 97);
    }
    return sb.toString();
  }
}
```

## Golang

```go
func smallestEquivalentString(s1 string, s2 string, baseStr string) string {
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
		if ra == rb {
			return
		}
		if ra < rb {
			parent[rb] = ra
		} else {
			parent[ra] = rb
		}
	}
	for i := 0; i < len(s1); i++ {
		union(int(s1[i]-'a'), int(s2[i]-'a'))
	}
	res := make([]byte, len(baseStr))
	for i, ch := range []byte(baseStr) {
		root := find(int(ch - 'a'))
		res[i] = byte('a' + root)
	}
	return string(res)
}
```

## Ruby

```ruby
def smallest_equivalent_string(s1, s2, base_str)
  parent = (0...26).to_a
  find = lambda do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end
  union = lambda do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    return if ra == rb
    if ra < rb
      parent[rb] = ra
    else
      parent[ra] = rb
    end
  end

  s1.each_char.with_index { |ch, i| union.call(ch.ord - 97, s2[i].ord - 97) }

  base_str.chars.map { |ch| ((find.call(ch.ord - 97)) + 97).chr }.join
end
```

## Scala

```scala
object Solution {
    def smallestEquivalentString(s1: String, s2: String, baseStr: String): String = {
        val parent = (0 until 26).toArray

        def find(x: Int): Int = {
            var p = x
            while (parent(p) != p) {
                p = parent(p)
            }
            var cur = x
            while (parent(cur) != cur) {
                val nxt = parent(cur)
                parent(cur) = p
                cur = nxt
            }
            p
        }

        def union(a: Int, b: Int): Unit = {
            var ra = find(a)
            var rb = find(b)
            if (ra == rb) return
            if (ra < rb) parent(rb) = ra else parent(ra) = rb
        }

        for (i <- 0 until s1.length) {
            val a = s1.charAt(i) - 'a'
            val b = s2.charAt(i) - 'a'
            union(a, b)
        }

        val sb = new StringBuilder
        for (ch <- baseStr) {
            val root = find(ch - 'a')
            sb.append((root + 'a').toChar)
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn smallest_equivalent_string(s1: String, s2: String, base_str: String) -> String {
        let mut parent: Vec<usize> = (0..26).collect();
        let b1 = s1.as_bytes();
        let b2 = s2.as_bytes();

        for i in 0..b1.len() {
            let a = (b1[i] - b'a') as usize;
            let b = (b2[i] - b'a') as usize;
            let ra = Self::find(a, &mut parent);
            let rb = Self::find(b, &mut parent);
            if ra != rb {
                if ra < rb {
                    parent[rb] = ra;
                } else {
                    parent[ra] = rb;
                }
            }
        }

        let mut result = String::with_capacity(base_str.len());
        for ch in base_str.bytes() {
            let idx = (ch - b'a') as usize;
            let r = Self::find(idx, &mut parent);
            result.push((r as u8 + b'a') as char);
        }
        result
    }

    fn find(x: usize, parent: &mut Vec<usize>) -> usize {
        if parent[x] != x {
            let root = Self::find(parent[x], parent);
            parent[x] = root;
        }
        parent[x]
    }
}
```

## Racket

```racket
(define/contract (smallest-equivalent-string s1 s2 baseStr)
  (-> string? string? string? string?)
  (let* ((n (string-length s1))
         (parent (make-vector 26)))
    ;; initialize parent pointers
    (for ([i (in-range 26)])
      (vector-set! parent i i))
    (define (char-index c)
      (- (char->integer c) (char->integer #\a)))
    (define (find x)
      (let loop ((v x))
        (let ((p (vector-ref parent v)))
          (if (= p v)
              v
              (let ((root (loop p)))
                (vector-set! parent v root)
                root)))))
    (define (union a b)
      (let* ((ra (find a))
             (rb (find b)))
        (when (not (= ra rb))
          (if (< ra rb)
              (vector-set! parent rb ra)
              (vector-set! parent ra rb)))))
    ;; process equivalence pairs
    (for ([i (in-range n)])
      (let* ((c1 (string-ref s1 i))
             (c2 (string-ref s2 i))
             (idx1 (char-index c1))
             (idx2 (char-index c2)))
        (union idx1 idx2)))
    ;; build the smallest equivalent string
    (list->string
     (for/list ([i (in-range (string-length baseStr))])
       (let* ((c (string-ref baseStr i))
              (idx (char-index c))
              (root (find idx)))
         (integer->char (+ root (char->integer #\a))))))))
```

## Erlang

```erlang
-spec smallest_equivalent_string(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary(), BaseStr :: unicode:unicode_binary()) -> unicode:unicode_binary().
smallest_equivalent_string(S1, S2, BaseStr) ->
    Parent0 = maps:from_list([{I, I} || I <- lists:seq(0, 25)]),
    Pairs = lists:zip(binary_to_list(S1), binary_to_list(S2)),
    MapAfterUnion = union_all(Pairs, Parent0),
    ResultList = map_base(binary_to_list(BaseStr), MapAfterUnion, []),
    list_to_binary(ResultList).

union_all([], Map) ->
    Map;
union_all([{C1, C2} | Rest], Map) ->
    A = C1 - $a,
    B = C2 - $a,
    {RootA, Map1} = find(Map, A),
    {RootB, Map2} = find(Map1, B),
    NewMap =
        case RootA == RootB of
            true -> Map2;
            false ->
                if RootA < RootB ->
                        maps:put(RootB, RootA, Map2);
                   true ->
                        maps:put(RootA, RootB, Map2)
                end
        end,
    union_all(Rest, NewMap).

find(Map, X) ->
    Parent = maps:get(X, Map),
    if Parent == X ->
            {X, Map};
       true ->
            {Root, M1} = find(Map, Parent),
            M2 = maps:put(X, Root, M1),
            {Root, M2}
    end.

map_base([], _Map, Acc) ->
    lists:reverse(Acc);
map_base([C | Rest], Map, Acc) ->
    Index = C - $a,
    {Root, NewMap} = find(Map, Index),
    Char = Root + $a,
    map_base(Rest, NewMap, [Char | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_equivalent_string(s1 :: String.t, s2 :: String.t, base_str :: String.t) :: String.t
  def smallest_equivalent_string(s1, s2, base_str) do
    parent = Enum.to_list(0..25)

    parent =
      Enum.zip(String.to_charlist(s1), String.to_charlist(s2))
      |> Enum.reduce(parent, fn {c1, c2}, par ->
        union(c1 - ?a, c2 - ?a, par)
      end)

    map =
      for i <- 0..25 do
        {root, _} = find(i, parent)
        {i, <<(root + ?a)::utf8>>}
      end
      |> Enum.into(%{})

    String.to_charlist(base_str)
    |> Enum.map(fn c -> Map.get(map, c - ?a) end)
    |> List.to_string()
  end

  defp find(x, parent) do
    p = Enum.at(parent, x)

    if p == x do
      {x, parent}
    else
      {root, new_parent} = find(p, parent)
      updated_parent = List.replace_at(new_parent, x, root)
      {root, updated_parent}
    end
  end

  defp union(a, b, parent) do
    {ra, pa} = find(a, parent)
    {rb, pb} = find(b, pa)

    if ra == rb do
      pb
    else
      if ra < rb do
        List.replace_at(pb, rb, ra)
      else
        List.replace_at(pb, ra, rb)
      end
    end
  end
end
```
