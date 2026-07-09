# 0756. Pyramid Transition Matrix

## Cpp

```cpp
class Solution {
public:
    bool pyramidTransition(string bottom, vector<string>& allowed) {
        // mapping from pair (a,b) to list of possible top chars
        vector<char> mp[6][6];
        for (const string& s : allowed) {
            int a = s[0] - 'A';
            int b = s[1] - 'A';
            mp[a][b].push_back(s[2]);
        }
        unordered_set<string> dead;
        function<bool(const string&)> dfs = [&](const string& cur)->bool{
            if (cur.size() == 1) return true;
            if (dead.count(cur)) return false;
            string next;
            function<bool(int)> build = [&](int idx)->bool{
                if (idx == (int)cur.size() - 1) {
                    // completed one upper level, recurse
                    return dfs(next);
                }
                int a = cur[idx] - 'A';
                int b = cur[idx+1] - 'A';
                for (char top : mp[a][b]) {
                    next.push_back(top);
                    if (build(idx + 1)) return true;
                    next.pop_back();
                }
                return false;
            };
            bool ok = build(0);
            if (!ok) dead.insert(cur);
            return ok;
        };
        return dfs(bottom);
    }
};
```

## Java

```java
class Solution {
    private java.util.Map<String, java.util.List<Character>> allowedMap;
    private java.util.Set<String> failedCache;

    public boolean pyramidTransition(String bottom, java.util.List<String> allowed) {
        allowedMap = new java.util.HashMap<>();
        for (String s : allowed) {
            String key = s.substring(0, 2);
            char val = s.charAt(2);
            allowedMap.computeIfAbsent(key, k -> new java.util.ArrayList<>()).add(val);
        }
        failedCache = new java.util.HashSet<>();
        return dfs(bottom);
    }

    private boolean dfs(String bottom) {
        if (bottom.length() == 1) {
            return true;
        }
        if (failedCache.contains(bottom)) {
            return false;
        }

        // Prepare possible characters for each adjacent pair
        java.util.List<char[]> options = new java.util.ArrayList<>();
        for (int i = 0; i < bottom.length() - 1; i++) {
            String key = "" + bottom.charAt(i) + bottom.charAt(i + 1);
            java.util.List<Character> list = allowedMap.get(key);
            if (list == null || list.isEmpty()) {
                failedCache.add(bottom);
                return false;
            }
            char[] arr = new char[list.size()];
            for (int j = 0; j < list.size(); j++) {
                arr[j] = list.get(j);
            }
            options.add(arr);
        }

        // Backtrack to build the next level
        StringBuilder sb = new StringBuilder();
        boolean canBuild = backtrack(0, sb, options);
        if (!canBuild) {
            failedCache.add(bottom);
        }
        return canBuild;
    }

    private boolean backtrack(int idx, StringBuilder sb, java.util.List<char[]> options) {
        if (idx == options.size()) {
            // Completed one upper level string
            return dfs(sb.toString());
        }
        char[] candidates = options.get(idx);
        for (char c : candidates) {
            sb.append(c);
            if (backtrack(idx + 1, sb, options)) {
                return true;
            }
            sb.deleteCharAt(sb.length() - 1);
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        from collections import defaultdict

        # map each pair of lower blocks to possible upper blocks
        pair_to_tops = defaultdict(list)
        for a in allowed:
            pair_to_tops[a[:2]].append(a[2])

        memo = {}

        def can_build(row):
            if len(row) == 1:
                return True
            if row in memo:
                return memo[row]

            # backtrack to generate possible next rows
            def dfs(idx, path):
                if idx == len(row) - 1:
                    next_row = ''.join(path)
                    return can_build(next_row)

                pair = row[idx:idx + 2]
                if pair not in pair_to_tops:
                    return False

                for ch in pair_to_tops[pair]:
                    path.append(ch)
                    if dfs(idx + 1, path):
                        return True
                    path.pop()
                return False

            res = dfs(0, [])
            memo[row] = res
            return res

        return can_build(bottom)
```

## Python3

```python
from typing import List
from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        pair_to_tops = defaultdict(list)
        for s in allowed:
            pair_to_tops[s[:2]].append(s[2])

        memo = set()

        def can_build(row: str) -> bool:
            if len(row) == 1:
                return True
            if row in memo:
                return False

            # backtrack to construct the next level string
            def build(idx: int, nxt: str) -> bool:
                if idx == len(row) - 1:
                    return can_build(nxt)
                pair = row[idx:idx+2]
                if pair not in pair_to_tops:
                    return False
                for ch in pair_to_tops[pair]:
                    if build(idx + 1, nxt + ch):
                        return True
                return False

            if not build(0, ""):
                memo.add(row)
                return False
            return True

        return can_build(bottom)
```

## C

```c
#include <stdbool.h>
#include <string.h>

static int allowedMap[6][6];

static bool dfs(char *cur, int n);
static bool buildNext(char *cur, int n, int pos, char *next);

bool pyramidTransition(char* bottom, char** allowed, int allowedSize) {
    memset(allowedMap, 0, sizeof(allowedMap));
    for (int i = 0; i < allowedSize; ++i) {
        char *s = allowed[i];
        int a = s[0] - 'A';
        int b = s[1] - 'A';
        int c = s[2] - 'A';
        if (a >= 0 && a < 6 && b >= 0 && b < 6 && c >= 0 && c < 6) {
            allowedMap[a][b] |= (1 << c);
        }
    }
    return dfs(bottom, (int)strlen(bottom));
}

static bool dfs(char *cur, int n) {
    if (n == 1) return true;
    char next[7]; // max length is 6, plus null terminator
    return buildNext(cur, n, 0, next);
}

static bool buildNext(char *cur, int n, int pos, char *next) {
    if (pos == n - 1) {
        // completed building the upper level string of length n-1
        next[pos] = '\0';
        return dfs(next, n - 1);
    }
    int a = cur[pos] - 'A';
    int b = cur[pos + 1] - 'A';
    if (a < 0 || a >= 6 || b < 0 || b >= 6) return false;
    int mask = allowedMap[a][b];
    if (mask == 0) return false;
    for (int bit = 0; bit < 6; ++bit) {
        if (mask & (1 << bit)) {
            next[pos] = 'A' + bit;
            if (buildNext(cur, n, pos + 1, next))
                return true;
        }
    }
    return false;
}
```

## Csharp

```csharp
public class Solution
{
    private Dictionary<string, List<char>> _map;
    private HashSet<string> _memo;

    public bool PyramidTransition(string bottom, IList<string> allowed)
    {
        _map = new Dictionary<string, List<char>>();
        foreach (var s in allowed)
        {
            var key = s.Substring(0, 2);
            var top = s[2];
            if (!_map.ContainsKey(key))
                _map[key] = new List<char>();
            _map[key].Add(top);
        }
        _memo = new HashSet<string>();
        return Dfs(bottom);
    }

    private bool Dfs(string cur)
    {
        if (cur.Length == 1) return true;
        if (_memo.Contains(cur)) return false;

        var next = new char[cur.Length - 1];
        bool canBuild = BuildNext(0, cur, next);
        if (!canBuild) _memo.Add(cur);
        return canBuild;
    }

    private bool BuildNext(int idx, string cur, char[] next)
    {
        if (idx == cur.Length - 1)
            return Dfs(new string(next));

        var pair = "" + cur[idx] + cur[idx + 1];
        if (!_map.TryGetValue(pair, out var tops)) return false;

        foreach (var top in tops)
        {
            next[idx] = top;
            if (BuildNext(idx + 1, cur, next))
                return true;
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} bottom
 * @param {string[]} allowed
 * @return {boolean}
 */
var pyramidTransition = function(bottom, allowed) {
    const pairMap = new Map(); // key: two chars, value: array of possible top chars
    for (const s of allowed) {
        const key = s[0] + s[1];
        if (!pairMap.has(key)) pairMap.set(key, []);
        pairMap.get(key).push(s[2]);
    }

    const memoFail = new Set(); // rows that cannot lead to a solution

    function canBuild(row) {
        if (row.length === 1) return true;
        if (memoFail.has(row)) return false;

        const nextRows = [];

        // backtrack to generate all possible strings for the row above
        function build(pos, path) {
            if (pos === row.length - 1) {
                nextRows.push(path);
                return;
            }
            const key = row[pos] + row[pos + 1];
            const tops = pairMap.get(key);
            if (!tops) return; // dead end
            for (const ch of tops) {
                build(pos + 1, path + ch);
            }
        }

        build(0, '');

        for (const nxt of nextRows) {
            if (canBuild(nxt)) return true;
        }

        memoFail.add(row);
        return false;
    }

    return canBuild(bottom);
};
```

## Typescript

```typescript
function pyramidTransition(bottom: string, allowed: string[]): boolean {
    const pairMap = new Map<string, string[]>();
    for (const s of allowed) {
        const key = s[0] + s[1];
        if (!pairMap.has(key)) pairMap.set(key, []);
        pairMap.get(key)!.push(s[2]);
    }

    const dead = new Set<string>();

    function canBuild(row: string): boolean {
        if (row.length === 1) return true;
        if (dead.has(row)) return false;

        const options: string[][] = [];
        for (let i = 0; i < row.length - 1; ++i) {
            const key = row[i] + row[i + 1];
            const tops = pairMap.get(key);
            if (!tops) {
                dead.add(row);
                return false;
            }
            options.push(tops);
        }

        const n = options.length;
        const cur: string[] = new Array(n);

        function dfs(pos: number): boolean {
            if (pos === n) {
                const nextRow = cur.join('');
                if (canBuild(nextRow)) return true;
                return false;
            }
            for (const ch of options[pos]) {
                cur[pos] = ch;
                if (dfs(pos + 1)) return true;
            }
            return false;
        }

        const ok = dfs(0);
        if (!ok) dead.add(row);
        return ok;
    }

    return canBuild(bottom);
}
```

## Php

```php
class Solution {
    /**
     * @var array
     */
    private $map = [];

    /**
     * @var array
     */
    private $memo = [];

    /**
     * @param String $bottom
     * @param String[] $allowed
     * @return Boolean
     */
    function pyramidTransition($bottom, $allowed) {
        foreach ($allowed as $s) {
            $key = $s[0] . $s[1];
            if (!isset($this->map[$key])) {
                $this->map[$key] = [];
            }
            $this->map[$key][] = $s[2];
        }
        return $this->dfs($bottom);
    }

    private function dfs($row) {
        $len = strlen($row);
        if ($len == 1) {
            return true;
        }
        if (isset($this->memo[$row])) {
            return false;
        }
        $nextRows = [];
        $this->buildNextRows($row, 0, "", $nextRows);
        foreach ($nextRows as $next) {
            if ($this->dfs($next)) {
                return true;
            }
        }
        $this->memo[$row] = false;
        return false;
    }

    private function buildNextRows($row, $idx, $path, &$result) {
        $n = strlen($row);
        if ($idx == $n - 1) {
            $result[] = $path;
            return;
        }
        $key = $row[$idx] . $row[$idx + 1];
        if (!isset($this->map[$key])) {
            return;
        }
        foreach ($this->map[$key] as $c) {
            $this->buildNextRows($row, $idx + 1, $path . $c, $result);
        }
    }
}
```

## Swift

```swift
class Solution {
    func pyramidTransition(_ bottom: String, _ allowed: [String]) -> Bool {
        var map = [String: [Character]]()
        for s in allowed {
            let chars = Array(s)
            let key = String([chars[0], chars[1]])
            map[key, default: []].append(chars[2])
        }
        
        var memo = [String: Bool]()
        
        func dfs(_ cur: String) -> Bool {
            if cur.count == 1 { return true }
            if let cached = memo[cur] { return cached }
            
            let chars = Array(cur)
            var nextRows = [String]()
            var path = [Character]()
            
            func build(_ idx: Int) {
                if idx == chars.count - 1 {
                    nextRows.append(String(path))
                    return
                }
                let key = String([chars[idx], chars[idx + 1]])
                guard let tops = map[key] else { return }
                for t in tops {
                    path.append(t)
                    build(idx + 1)
                    path.removeLast()
                }
            }
            
            build(0)
            
            var can = false
            for next in nextRows {
                if dfs(next) {
                    can = true
                    break
                }
            }
            memo[cur] = can
            return can
        }
        
        return dfs(bottom)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun pyramidTransition(bottom: String, allowed: List<String>): Boolean {
        val map = HashMap<String, MutableList<Char>>()
        for (s in allowed) {
            val key = "${s[0]}${s[1]}"
            map.computeIfAbsent(key) { mutableListOf() }.add(s[2])
        }
        val failed = HashSet<String>()
        fun dfs(row: String): Boolean {
            if (row.length == 1) return true
            if (failed.contains(row)) return false
            val sb = StringBuilder()
            fun backtrack(pos: Int): Boolean {
                if (pos == row.length - 1) {
                    return dfs(sb.toString())
                }
                val key = "${row[pos]}${row[pos + 1]}"
                val tops = map[key] ?: return false
                for (c in tops) {
                    sb.append(c)
                    if (backtrack(pos + 1)) return true
                    sb.setLength(sb.length - 1)
                }
                return false
            }
            val ok = backtrack(0)
            if (!ok) failed.add(row)
            return ok
        }
        return dfs(bottom)
    }
}
```

## Dart

```dart
class Solution {
  bool pyramidTransition(String bottom, List<String> allowed) {
    // Build mapping from pair of blocks to possible top blocks
    final Map<String, List<String>> map = {};
    for (var s in allowed) {
      final key = s.substring(0, 2);
      map.putIfAbsent(key, () => []).add(s[2]);
    }

    final Map<String, bool> memo = {};

    bool dfs(String level) {
      if (level.length == 1) return true;
      if (memo.containsKey(level)) return memo[level]!;

      bool found = false;

      void backtrack(int idx, StringBuffer sb) {
        if (found) return; // early exit
        if (idx == level.length - 1) {
          if (dfs(sb.toString())) {
            found = true;
          }
          return;
        }

        final pair = level.substring(idx, idx + 2);
        final tops = map[pair];
        if (tops == null) return;

        for (var top in tops) {
          sb.write(top);
          backtrack(idx + 1, sb);
          sb.length = sb.length - 1; // revert
          if (found) break;
        }
      }

      backtrack(0, StringBuffer());
      memo[level] = found;
      return found;
    }

    return dfs(bottom);
  }
}
```

## Golang

```go
func pyramidTransition(bottom string, allowed []string) bool {
    // map from pair (as two-byte array) to possible top characters
    mp := make(map[[2]byte][]byte)
    for _, s := range allowed {
        a, b, c := s[0], s[1], s[2]
        key := [2]byte{a, b}
        mp[key] = append(mp[key], c)
    }

    memo := make(map[string]bool)

    var dfs func(string) bool
    dfs = func(cur string) bool {
        if len(cur) == 1 {
            return true
        }
        if v, ok := memo[cur]; ok {
            return v
        }

        // backtrack to build all possible strings for the next level
        var build func(int, []byte) bool
        build = func(idx int, path []byte) bool {
            if idx == len(cur)-1 {
                if dfs(string(path)) {
                    return true
                }
                return false
            }
            key := [2]byte{cur[idx], cur[idx+1]}
            tops, ok := mp[key]
            if !ok {
                return false
            }
            for _, t := range tops {
                if build(idx+1, append(path, t)) {
                    return true
                }
            }
            return false
        }

        res := build(0, []byte{})
        memo[cur] = res
        return res
    }

    return dfs(bottom)
}
```

## Ruby

```ruby
def pyramid_transition(bottom, allowed)
  pair_map = Hash.new { |h, k| h[k] = [] }
  allowed.each do |s|
    pair = s[0, 2]
    top = s[2]
    pair_map[pair] << top
  end

  memo = {}

  dfs = nil
  dfs = lambda do |cur_bottom|
    return true if cur_bottom.length == 1
    return false if memo.key?(cur_bottom)

    build_next = nil
    build_next = lambda do |idx, next_row|
      if idx == cur_bottom.length - 1
        return dfs.call(next_row)
      end

      pair = cur_bottom[idx, 2]
      tops = pair_map[pair]
      return false if tops.empty?

      tops.each do |c|
        return true if build_next.call(idx + 1, next_row + c)
      end
      false
    end

    result = build_next.call(0, "")
    memo[cur_bottom] = !result
    result
  end

  dfs.call(bottom)
end
```

## Scala

```scala
object Solution {
    import scala.collection.mutable.{ArrayBuffer, ListBuffer, Set, StringBuilder}

    def pyramidTransition(bottom: String, allowed: List[String]): Boolean = {
        // Build mapping from pair to possible top blocks
        val tempMap = scala.collection.mutable.Map[String, ListBuffer[Char]]()
        for (s <- allowed) {
            val key = s.substring(0, 2)
            val top = s.charAt(2)
            tempMap.getOrElseUpdate(key, ListBuffer()) += top
        }
        val allowedMap: Map[String, List[Char]] = tempMap.toMap.map { case (k, v) => k -> v.toList }

        val failed = Set[String]()

        def canBuild(row: String): Boolean = {
            if (row.length == 1) return true
            if (failed.contains(row)) return false

            val nextRows = ArrayBuffer[String]()

            // Generate all possible rows for the level above current row
            def generate(pos: Int, sb: StringBuilder): Unit = {
                if (pos == row.length - 1) {
                    nextRows += sb.toString()
                    return
                }
                val key = "" + row.charAt(pos) + row.charAt(pos + 1)
                allowedMap.get(key) match {
                    case Some(chars) =>
                        for (c <- chars) {
                            sb.append(c)
                            generate(pos + 1, sb)
                            sb.setLength(sb.length - 1)
                        }
                    case None => // no possible block, dead end
                }
            }

            generate(0, new StringBuilder())

            for (nextRow <- nextRows) {
                if (canBuild(nextRow)) return true
            }

            failed += row
            false
        }

        canBuild(bottom)
    }
}
```

## Rust

```rust
use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn pyramid_transition(bottom: String, allowed: Vec<String>) -> bool {
        // Build mapping from pair (bottom left, bottom right) to possible top blocks
        let mut map: HashMap<(u8, u8), Vec<u8>> = HashMap::new();
        for s in allowed {
            let b = s.as_bytes();
            if b.len() == 3 {
                map.entry((b[0], b[1]))
                    .or_insert_with(Vec::new)
                    .push(b[2]);
            }
        }

        // Recursive helper with memoization
        fn dfs(row: &str, map: &HashMap<(u8, u8), Vec<u8>>, memo: &mut HashSet<String>) -> bool {
            if row.len() == 1 {
                return true;
            }
            if memo.contains(row) {
                return false;
            }

            let bytes = row.as_bytes();

            // Backtrack to generate all possible rows above the current one
            fn backtrack(
                pos: usize,
                cur_row: &[u8],
                map: &HashMap<(u8, u8), Vec<u8>>,
                building: &mut Vec<u8>,
                memo: &mut HashSet<String>,
            ) -> bool {
                if pos == cur_row.len() - 1 {
                    let next = String::from_utf8(building.clone()).unwrap();
                    return dfs(&next, map, memo);
                }
                let key = (cur_row[pos], cur_row[pos + 1]);
                if let Some(cands) = map.get(&key) {
                    for &c in cands {
                        building.push(c);
                        if backtrack(pos + 1, cur_row, map, building, memo) {
                            return true;
                        }
                        building.pop();
                    }
                }
                false
            }

            let mut building: Vec<u8> = Vec::with_capacity(bytes.len() - 1);
            let ok = backtrack(0, bytes, map, &mut building, memo);
            if !ok {
                memo.insert(row.to_string());
            }
            ok
        }

        let mut memo = HashSet::new();
        dfs(&bottom, &map, &mut memo)
    }
}
```

## Racket

```racket
#lang racket

(provide pyramid-transition)

(define/contract (pyramid-transition bottom allowed)
  (-> string? (listof string?) boolean?)
  (let* ((allowed-map (make-hash))
         (memo (make-hash)))
    ;; build mapping from pair -> list of possible tops
    (for ([s allowed])
      (let* ((c1 (string-ref s 0))
             (c2 (string-ref s 1))
             (top (string-ref s 2))
             (key (string c1 c2)))
        (hash-set! allowed-map key
                   (cons top (hash-ref allowed-map key '())))))
    ;; recursive helpers
    (letrec ((build-next
              (lambda (bottom idx acc)
                (if (= idx (- (string-length bottom) 1))
                    (list (list->string (reverse acc)))
                    (let* ((c1 (string-ref bottom idx))
                           (c2 (string-ref bottom (+ idx 1)))
                           (key (string c1 c2))
                           (tops (hash-ref allowed-map key '())))
                      (if (null? tops)
                          '()
                          (apply append
                                 (map (lambda (top)
                                        (build-next bottom (+ idx 1) (cons top acc)))
                                      tops))))))

             (can-build?
              (lambda (bottom)
                (cond [(= (string-length bottom) 1) #t]
                      [else
                       (if (hash-has-key? memo bottom)
                           (hash-ref memo bottom)
                           (let ((next-levels (build-next bottom 0 '()))
                                 (result
                                  (let loop ((cands next-levels))
                                    (cond [(null? cands) #f]
                                          [(can-build? (car cands)) #t]
                                          [else (loop (cdr cands))]))))
                             (hash-set! memo bottom result)
                             result))])))
      (can-build? bottom))))
```

## Erlang

```erlang
-module(solution).
-export([pyramid_transition/2]).

-spec pyramid_transition(Bottom :: unicode:unicode_binary(),
                         Allowed :: [unicode:unicode_binary()]) -> boolean().
pyramid_transition(Bottom, Allowed) ->
    Map = build_map(Allowed),
    BottomList = binary_to_list(Bottom),
    can_build(BottomList, Map).

build_map(Allowed) ->
    lists:foldl(fun(Str, Acc) ->
        case binary_to_list(Str) of
            [C1, C2, T] ->
                Key = {C1, C2},
                case maps:is_key(Key, Acc) of
                    true -> maps:update(Key, fun(Old) -> [T | Old] end, Acc);
                    false -> maps:put(Key, [T], Acc)
                end;
            _ -> Acc
        end
    end, #{}, Allowed).

can_build([_], _) ->
    true;
can_build(Level, Map) ->
    NextLevels = gen_next(Level, Map),
    lists:any(fun(NL) -> can_build(NL, Map) end, NextLevels).

gen_next([X, Y], Map) ->
    case maps:get({X, Y}, Map, []) of
        [] -> [];
        Tops -> [ [Top] || Top <- Tops ]
    end;
gen_next([X, Y | Rest], Map) ->
    case maps:get({X, Y}, Map, []) of
        [] -> [];
        Tops ->
            RestNext = gen_next([Y | Rest], Map),
            [ [Top | NL] || Top <- Tops, NL <- RestNext ]
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec pyramid_transition(bottom :: String.t(), allowed :: [String.t()]) :: boolean()
  def pyramid_transition(bottom, allowed) do
    pair_map = build_pair_map(allowed)
    dfs(bottom, pair_map)
  end

  defp build_pair_map(allowed) do
    Enum.reduce(allowed, %{}, fn <<a, b, c>>, acc ->
      key = <<a, b>>
      Map.update(acc, key, [c], &[c | &1])
    end)
  end

  defp dfs(row, pair_map) when byte_size(row) == 1, do: true

  defp dfs(row, pair_map) do
    next_rows = gen_next_rows(row, pair_map)

    Enum.any?(next_rows, fn nxt -> dfs(nxt, pair_map) end)
  end

  defp gen_next_rows(row, pair_map) do
    chars = :binary.bin_to_list(row)
    build(chars, [], pair_map)
  end

  # Base case: exactly two characters left to form a top block
  defp build([a, b], cur, pair_map) do
    key = <<a, b>>
    case Map.get(pair_map, key) do
      nil -> []
      tops ->
        Enum.map(tops, fn top_char ->
          :binary.list_to_bin(Enum.reverse([top_char | cur]))
        end)
    end
  end

  # Recursive case: more than two characters remain
  defp build([a, b | rest], cur, pair_map) when rest != [] do
    key = <<a, b>>
    case Map.get(pair_map, key) do
      nil -> []
      tops ->
        Enum.flat_map(tops, fn top_char ->
          build([b | rest], [top_char | cur], pair_map)
        end)
    end
  end
end
```
