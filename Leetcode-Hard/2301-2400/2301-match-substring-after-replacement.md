# 2301. Match Substring After Replacement

## Cpp

```cpp
class Solution {
public:
    bool matchReplacement(string s, string sub, vector<vector<char>>& mappings) {
        unordered_map<char, unordered_set<char>> mp;
        for (auto &p : mappings) {
            if (p.size() == 2)
                mp[p[0]].insert(p[1]);
        }
        int n = s.size(), m = sub.size();
        for (int i = 0; i + m <= n; ++i) {
            bool ok = true;
            for (int j = 0; j < m; ++j) {
                char a = sub[j];
                char b = s[i + j];
                if (a == b) continue;
                if (mp.find(a) == mp.end() || mp[a].find(b) == mp[a].end()) {
                    ok = false;
                    break;
                }
            }
            if (ok) return true;
        }
        return false;
    }
};
```

## Java

```java
class Solution {
    public boolean matchReplacement(String s, String sub, char[][] mappings) {
        int n = s.length();
        int m = sub.length();
        if (m > n) return false;
        boolean[][] canReplace = new boolean[128][128];
        for (char[] map : mappings) {
            if (map.length == 2) {
                char oldc = map[0];
                char newc = map[1];
                canReplace[oldc][newc] = true;
            }
        }
        outer:
        for (int i = 0; i <= n - m; i++) {
            for (int j = 0; j < m; j++) {
                char cs = s.charAt(i + j);
                char csub = sub.charAt(j);
                if (cs == csub) continue;
                if (!canReplace[csub][cs]) {
                    continue outer;
                }
            }
            return true;
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def matchReplacement(self, s, sub, mappings):
        """
        :type s: str
        :type sub: str
        :type mappings: List[List[str]]
        :rtype: bool
        """
        # Build mapping from original character to possible replacements
        repl = {}
        for old, new in mappings:
            if old not in repl:
                repl[old] = set()
            repl[old].add(new)

        n, m = len(s), len(sub)
        for i in range(n - m + 1):
            ok = True
            for j in range(m):
                sc = s[i + j]
                pc = sub[j]
                if sc == pc:
                    continue
                if pc not in repl or sc not in repl[pc]:
                    ok = False
                    break
            if ok:
                return True
        return False
```

## Python3

```python
from typing import List

class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        trans = {}
        for old, new in mappings:
            trans.setdefault(old, set()).add(new)

        n, m = len(s), len(sub)
        for i in range(n - m + 1):
            ok = True
            for k in range(m):
                sc = s[i + k]
                pc = sub[k]
                if sc == pc:
                    continue
                if pc not in trans or sc not in trans[pc]:
                    ok = False
                    break
            if ok:
                return True
        return False
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool matchReplacement(char* s, char* sub, char** mappings, int mappingsSize, int* mappingsColSize) {
    bool can[256][256] = {false};
    for (int i = 0; i < mappingsSize; ++i) {
        unsigned char oldc = (unsigned char)mappings[i][0];
        unsigned char newc = (unsigned char)mappings[i][1];
        can[oldc][newc] = true;
    }
    
    int n = strlen(s);
    int m = strlen(sub);
    if (m > n) return false;
    
    for (int start = 0; start <= n - m; ++start) {
        bool ok = true;
        for (int j = 0; j < m; ++j) {
            unsigned char a = (unsigned char)sub[j];
            unsigned char b = (unsigned char)s[start + j];
            if (a == b) continue;
            if (!can[a][b]) { ok = false; break; }
        }
        if (ok) return true;
    }
    
    return false;
}
```

## Csharp

```csharp
public class Solution {
    public bool MatchReplacement(string s, string sub, char[][] mappings) {
        var map = new Dictionary<char, HashSet<char>>();
        foreach (var pair in mappings) {
            char oldc = pair[0];
            char newc = pair[1];
            if (!map.TryGetValue(oldc, out var set)) {
                set = new HashSet<char>();
                map[oldc] = set;
            }
            set.Add(newc);
        }

        int n = s.Length, m = sub.Length;
        for (int i = 0; i <= n - m; i++) {
            bool ok = true;
            for (int j = 0; j < m; j++) {
                char sc = s[i + j];
                char pc = sub[j];
                if (sc == pc) continue;
                if (!map.TryGetValue(pc, out var set) || !set.Contains(sc)) {
                    ok = false;
                    break;
                }
            }
            if (ok) return true;
        }
        return false;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} sub
 * @param {character[][]} mappings
 * @return {boolean}
 */
var matchReplacement = function(s, sub, mappings) {
    const n = s.length;
    const m = sub.length;
    const replaceMap = new Map();
    
    for (const [oldChar, newChar] of mappings) {
        if (!replaceMap.has(oldChar)) replaceMap.set(oldChar, new Set());
        replaceMap.get(oldChar).add(newChar);
    }
    
    for (let i = 0; i <= n - m; i++) {
        let ok = true;
        for (let j = 0; j < m; j++) {
            const sc = s[i + j];
            const subc = sub[j];
            if (sc === subc) continue;
            const set = replaceMap.get(subc);
            if (!set || !set.has(sc)) {
                ok = false;
                break;
            }
        }
        if (ok) return true;
    }
    
    return false;
};
```

## Typescript

```typescript
function matchReplacement(s: string, sub: string, mappings: string[][]): boolean {
    const n = s.length;
    const m = sub.length;
    const map = new Map<string, Set<string>>();
    for (const [oldc, newc] of mappings) {
        if (!map.has(oldc)) map.set(oldc, new Set());
        map.get(oldc)!.add(newc);
    }
    for (let i = 0; i <= n - m; i++) {
        let ok = true;
        for (let j = 0; j < m; j++) {
            const sc = s[i + j];
            const subc = sub[j];
            if (sc === subc) continue;
            const set = map.get(subc);
            if (!set || !set.has(sc)) {
                ok = false;
                break;
            }
        }
        if (ok) return true;
    }
    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $sub
     * @param String[][] $mappings
     * @return Boolean
     */
    function matchReplacement($s, $sub, $mappings) {
        $lenS = strlen($s);
        $lenSub = strlen($sub);
        // Build replacement map: old => set of possible new chars
        $map = [];
        foreach ($mappings as $pair) {
            $old = $pair[0];
            $new = $pair[1];
            if (!isset($map[$old])) {
                $map[$old] = [];
            }
            $map[$old][$new] = true;
        }

        for ($i = 0; $i <= $lenS - $lenSub; $i++) {
            $ok = true;
            for ($j = 0; $j < $lenSub; $j++) {
                $cSub = $sub[$j];
                $cS   = $s[$i + $j];
                if ($cSub === $cS) {
                    continue;
                }
                if (!isset($map[$cSub]) || !isset($map[$cSub][$cS])) {
                    $ok = false;
                    break;
                }
            }
            if ($ok) {
                return true;
            }
        }

        return false;
    }
}
```

## Swift

```swift
class Solution {
    func matchReplacement(_ s: String, _ sub: String, _ mappings: [[Character]]) -> Bool {
        let sArr = Array(s)
        let subArr = Array(sub)
        var replaceMap = [Character: Set<Character>]()
        for pair in mappings where pair.count == 2 {
            let oldChar = pair[0]
            let newChar = pair[1]
            replaceMap[oldChar, default: Set<Character>()].insert(newChar)
        }
        
        let n = sArr.count
        let m = subArr.count
        if m > n { return false }
        
        for i in 0...(n - m) {
            var match = true
            for j in 0..<m {
                let sc = sArr[i + j]
                let pc = subArr[j]
                if sc == pc { continue }
                if let set = replaceMap[pc], set.contains(sc) {
                    continue
                } else {
                    match = false
                    break
                }
            }
            if match { return true }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun matchReplacement(s: String, sub: String, mappings: Array<CharArray>): Boolean {
        val n = s.length
        val m = sub.length
        if (m > n) return false

        // Build mapping from old character to set of possible new characters
        val replaceMap = HashMap<Char, MutableSet<Char>>()
        for (pair in mappings) {
            val oldChar = pair[0]
            val newChar = pair[1]
            replaceMap.computeIfAbsent(oldChar) { HashSet() }.add(newChar)
        }

        // Try each possible starting index in s
        for (start in 0..(n - m)) {
            var ok = true
            for (j in 0 until m) {
                val cSub = sub[j]
                val cS = s[start + j]
                if (cSub == cS) continue
                val possible = replaceMap[cSub]
                if (possible == null || !possible.contains(cS)) {
                    ok = false
                    break
                }
            }
            if (ok) return true
        }
        return false
    }
}
```

## Dart

```dart
class Solution {
  bool matchReplacement(String s, String sub, List<List<String>> mappings) {
    final Map<String, Set<String>> map = {};
    for (var pair in mappings) {
      final oldChar = pair[0];
      final newChar = pair[1];
      map.putIfAbsent(oldChar, () => <String>{}).add(newChar);
    }

    final int n = s.length;
    final int m = sub.length;

    for (int i = 0; i <= n - m; ++i) {
      bool ok = true;
      for (int j = 0; j < m; ++j) {
        final String cS = s[i + j];
        final String cSub = sub[j];
        if (cS == cSub) continue;
        final Set<String>? allowed = map[cSub];
        if (allowed != null && allowed.contains(cS)) continue;
        ok = false;
        break;
      }
      if (ok) return true;
    }

    return false;
  }
}
```

## Golang

```go
func matchReplacement(s string, sub string, mappings [][]byte) bool {
    // Build replacement map: old -> set of possible new characters
    repl := make(map[byte]map[byte]bool)
    for _, m := range mappings {
        if len(m) < 2 {
            continue
        }
        oldChar, newChar := m[0], m[1]
        if repl[oldChar] == nil {
            repl[oldChar] = make(map[byte]bool)
        }
        repl[oldChar][newChar] = true
    }

    n, mlen := len(s), len(sub)
    if mlen > n {
        return false
    }

    // Check each possible window in s
    for i := 0; i <= n-mlen; i++ {
        match := true
        for j := 0; j < mlen; j++ {
            sc := sub[j]
            tc := s[i+j]
            if sc == tc {
                continue
            }
            if set, ok := repl[sc]; !ok || !set[tc] {
                match = false
                break
            }
        }
        if match {
            return true
        }
    }
    return false
}
```

## Ruby

```ruby
def match_replacement(s, sub, mappings)
  n = s.length
  m = sub.length
  return false if m > n

  require 'set'
  map = Hash.new { |h, k| h[k] = Set.new }
  mappings.each do |old_char, new_char|
    map[old_char].add(new_char)
  end

  (0..n - m).each do |i|
    ok = true
    j = 0
    while j < m
      sc = s[i + j]
      subc = sub[j]
      if sc == subc
        # match directly
      elsif map[subc].include?(sc)
        # valid replacement
      else
        ok = false
        break
      end
      j += 1
    end
    return true if ok
  end

  false
end
```

## Scala

```scala
object Solution {
    def matchReplacement(s: String, sub: String, mappings: Array[Array[Char]]): Boolean = {
        val replaceMap = scala.collection.mutable.Map[Char, Set[Char]]()
        for (pair <- mappings) {
            val oldc = pair(0)
            val newc = pair(1)
            replaceMap.update(oldc, replaceMap.getOrElse(oldc, Set.empty) + newc)
        }
        val n = s.length
        val m = sub.length
        if (m > n) return false
        for (i <- 0 to n - m) {
            var ok = true
            var j = 0
            while (j < m && ok) {
                val cSub = sub.charAt(j)
                val cS   = s.charAt(i + j)
                if (cSub != cS) {
                    replaceMap.get(cSub) match {
                        case Some(set) => if (!set.contains(cS)) ok = false
                        case None      => ok = false
                    }
                }
                j += 1
            }
            if (ok) return true
        }
        false
    }
}
```

## Rust

```rust
use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn match_replacement(s: String, sub: String, mappings: Vec<Vec<char>>) -> bool {
        // Build mapping from old char to set of possible new chars
        let mut map: HashMap<char, HashSet<char>> = HashMap::new();
        for pair in mappings.iter() {
            if pair.len() != 2 { continue; }
            let old_c = pair[0];
            let new_c = pair[1];
            map.entry(old_c).or_insert_with(HashSet::new).insert(new_c);
        }

        let s_chars: Vec<char> = s.chars().collect();
        let sub_chars: Vec<char> = sub.chars().collect();

        if sub_chars.is_empty() || s_chars.len() < sub_chars.len() {
            return false;
        }

        let n = s_chars.len();
        let m = sub_chars.len();

        for i in 0..=n - m {
            let mut ok = true;
            for j in 0..m {
                let sc = s_chars[i + j];
                let pc = sub_chars[j];
                if sc == pc {
                    continue;
                }
                match map.get(&pc) {
                    Some(set) if set.contains(&sc) => {}
                    _ => {
                        ok = false;
                        break;
                    }
                }
            }
            if ok {
                return true;
            }
        }

        false
    }
}
```

## Racket

```racket
(require racket/set)

(define/contract (match-replacement s sub mappings)
  (-> string? string? (listof (listof char?)) boolean?)
  (let* ((len-s   (string-length s))
         (len-sub (string-length sub))
         (map-hash (make-hash)))
    ;; build mapping from old char to set of possible new chars
    (for ([pair mappings])
      (define old (first pair))
      (define new (second pair))
      (hash-set! map-hash old
                 (let ((existing (hash-ref map-hash old #f)))
                   (if existing
                       (set-add existing new)
                       (set new)))))
    ;; check if sub can match s starting at index i
    (define (match-at? i)
      (let loop ((j 0))
        (cond [(= j len-sub) #t]
              [else
               (let* ((c-sub (string-ref sub j))
                      (c-s   (string-ref s (+ i j))))
                 (if (char=? c-sub c-s)
                     (loop (add1 j))
                     (let ((new-set (hash-ref map-hash c-sub #f)))
                       (if (and new-set (set-member? new-set c-s))
                           (loop (add1 j))
                           #f))))])))
    ;; try all possible start positions
    (let search ((i 0))
      (cond [(> i (- len-s len-sub)) #f]
            [(match-at? i) #t]
            [else (search (add1 i))])))))
```

## Erlang

```erlang
-module(solution).
-export([match_replacement/3]).

-spec match_replacement(S :: unicode:unicode_binary(),
                        Sub :: unicode:unicode_binary(),
                        Mappings :: [[char()]]) -> boolean().
match_replacement(S, Sub, Mappings) ->
    SubList = unicode:characters_to_list(Sub),
    SList = unicode:characters_to_list(S),
    Map = build_map(Mappings),
    LenSub = length(SubList),
    LenS = length(SList),
    case LenSub > LenS of
        true -> false;
        false ->
            MaxStart = LenS - LenSub,
            loop(0, MaxStart, SList, SubList, Map)
    end.

build_map(Mappings) ->
    lists:foldl(fun([OldBin, NewBin], Acc) ->
        [OldChar] = unicode:characters_to_list(OldBin),
        [NewChar] = unicode:characters_to_list(NewBin),
        case maps:get(OldChar, Acc, undefined) of
            undefined ->
                maps:put(OldChar, #{NewChar => true}, Acc);
            Set ->
                maps:put(OldChar, Set#{NewChar => true}, Acc)
        end
    end, #{}, Mappings).

loop(Start, MaxStart, SList, SubList, Map) when Start =< MaxStart ->
    Window = lists:sublist(SList, Start + 1, length(SubList)),
    case match_window(SubList, Window, Map) of
        true -> true;
        false -> loop(Start + 1, MaxStart, SList, SubList, Map)
    end;
loop(_, _, _, _, _) ->
    false.

match_window([], [], _Map) -> true;
match_window([C1|T1], [C2|T2], Map) ->
    if C1 == C2 ->
            match_window(T1, T2, Map);
       true ->
            case maps:get(C1, Map, undefined) of
                undefined -> false;
                Set ->
                    case maps:is_key(C2, Set) of
                        true -> match_window(T1, T2, Map);
                        false -> false
                    end
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec match_replacement(String.t(), String.t(), [[char]]) :: boolean()
  def match_replacement(s, sub, mappings) do
    s_list = String.graphemes(s)
    sub_list = String.graphemes(sub)
    m = length(sub_list)
    n = length(s_list)

    repl_map =
      Enum.reduce(mappings, %{}, fn [old, new], acc ->
        Map.update(acc, old, MapSet.new([new]), &MapSet.put(&1, new))
      end)

    max_start = n - m

    if max_start < 0 do
      false
    else
      Enum.any?(0..max_start, fn start -> match_window?(s_list, sub_list, repl_map, start) end)
    end
  end

  defp match_window?(s_list, sub_list, repl_map, start) do
    window = Enum.slice(s_list, start, length(sub_list))

    Enum.zip(sub_list, window)
    |> Enum.all?(fn {c_sub, c_s} ->
      if c_sub == c_s do
        true
      else
        case Map.get(repl_map, c_sub) do
          nil -> false
          set -> MapSet.member?(set, c_s)
        end
      end
    end)
  end
end
```
