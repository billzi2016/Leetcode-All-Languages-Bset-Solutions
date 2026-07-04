# 0205. Isomorphic Strings

## Cpp

```cpp
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.size() != t.size()) return false;
        int mapST[256];
        int mapTS[256];
        fill(begin(mapST), end(mapST), -1);
        fill(begin(mapTS), end(mapTS), -1);
        for (int i = 0; i < (int)s.size(); ++i) {
            unsigned char c1 = s[i];
            unsigned char c2 = t[i];
            if (mapST[c1] == -1 && mapTS[c2] == -1) {
                mapST[c1] = i;
                mapTS[c2] = i;
            } else if (mapST[c1] != mapTS[c2]) {
                return false;
            }
        }
        return true;
    }
};
```

## Java

```java
import java.util.Arrays;

class Solution {
    public boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length()) return false;
        int[] mapST = new int[256];
        int[] mapTS = new int[256];
        Arrays.fill(mapST, -1);
        Arrays.fill(mapTS, -1);
        for (int i = 0; i < s.length(); i++) {
            char c1 = s.charAt(i);
            char c2 = t.charAt(i);
            if (mapST[c1] == -1 && mapTS[c2] == -1) {
                mapST[c1] = c2;
                mapTS[c2] = c1;
            } else {
                if (mapST[c1] != c2) return false;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        map_s = {}
        map_t = {}
        for ch_s, ch_t in zip(s, t):
            if ch_s in map_s:
                if map_s[ch_s] != ch_t:
                    return False
            else:
                map_s[ch_s] = ch_t
            if ch_t in map_t:
                if map_t[ch_t] != ch_s:
                    return False
            else:
                map_t[ch_t] = ch_s
        return True
```

## Python3

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s = {}
        map_t = {}
        for c1, c2 in zip(s, t):
            if c1 not in map_s and c2 not in map_t:
                map_s[c1] = c2
                map_t[c2] = c1
            elif map_s.get(c1) != c2 or map_t.get(c2) != c1:
                return False
        return True
```

## C

```c
#include <stdbool.h>

bool isIsomorphic(char* s, char* t) {
    int mapS[256];
    int mapT[256];
    for (int i = 0; i < 256; ++i) {
        mapS[i] = -1;
        mapT[i] = -1;
    }
    int i;
    for (i = 0; s[i] && t[i]; ++i) {
        unsigned char cs = (unsigned char)s[i];
        unsigned char ct = (unsigned char)t[i];
        if (mapS[cs] == -1 && mapT[ct] == -1) {
            mapS[cs] = mapT[ct] = i;
        } else if (mapS[cs] != i || mapT[ct] != i) {
            return false;
        }
    }
    if (s[i] || t[i]) return false;
    return true;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsIsomorphic(string s, string t) {
        if (s.Length != t.Length) return false;
        var map = new System.Collections.Generic.Dictionary<char, char>();
        var used = new System.Collections.Generic.HashSet<char>();
        for (int i = 0; i < s.Length; i++) {
            char cs = s[i];
            char ct = t[i];
            if (!map.ContainsKey(cs)) {
                if (used.Contains(ct)) return false;
                map[cs] = ct;
                used.Add(ct);
            } else {
                if (map[cs] != ct) return false;
            }
        }
        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    if (s.length !== t.length) return false;
    const mapST = new Map();
    const mapTS = new Map();
    for (let i = 0; i < s.length; i++) {
        const c1 = s[i];
        const c2 = t[i];
        if (!mapST.has(c1) && !mapTS.has(c2)) {
            mapST.set(c1, c2);
            mapTS.set(c2, c1);
        } else {
            if (mapST.get(c1) !== c2 || mapTS.get(c2) !== c1) {
                return false;
            }
        }
    }
    return true;
};
```

## Typescript

```typescript
function isIsomorphic(s: string, t: string): boolean {
    if (s.length !== t.length) return false;
    const mapST = new Map<string, string>();
    const mapTS = new Map<string, string>();
    for (let i = 0; i < s.length; i++) {
        const cs = s[i];
        const ct = t[i];
        if (mapST.has(cs)) {
            if (mapST.get(cs) !== ct) return false;
        } else {
            mapST.set(cs, ct);
        }
        if (mapTS.has(ct)) {
            if (mapTS.get(ct) !== cs) return false;
        } else {
            mapTS.set(ct, cs);
        }
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Boolean
     */
    function isIsomorphic($s, $t) {
        $n = strlen($s);
        if ($n !== strlen($t)) {
            return false;
        }
        $mapST = [];
        $mapTS = [];
        for ($i = 0; $i < $n; $i++) {
            $c1 = $s[$i];
            $c2 = $t[$i];

            if (isset($mapST[$c1])) {
                if ($mapST[$c1] !== $c2) {
                    return false;
                }
            } else {
                $mapST[$c1] = $c2;
            }

            if (isset($mapTS[$c2])) {
                if ($mapTS[$c2] !== $c1) {
                    return false;
                }
            } else {
                $mapTS[$c2] = $c1;
            }
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func isIsomorphic(_ s: String, _ t: String) -> Bool {
        if s.count != t.count { return false }
        var mapping = [Character: Character]()
        var used = Set<Character>()
        let sArr = Array(s)
        let tArr = Array(t)
        for i in 0..<sArr.count {
            let sc = sArr[i]
            let tc = tArr[i]
            if let mapped = mapping[sc] {
                if mapped != tc { return false }
            } else {
                if used.contains(tc) { return false }
                mapping[sc] = tc
                used.insert(tc)
            }
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isIsomorphic(s: String, t: String): Boolean {
        if (s.length != t.length) return false
        val map = IntArray(256) { -1 }
        val rev = IntArray(256) { -1 }
        for (i in s.indices) {
            val c1 = s[i].code
            val c2 = t[i].code
            if (map[c1] == -1 && rev[c2] == -1) {
                map[c1] = c2
                rev[c2] = c1
            } else if (map[c1] != c2) {
                return false
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool isIsomorphic(String s, String t) {
    if (s.length != t.length) return false;
    final Map<int, int> mapping = {};
    final Set<int> used = {};

    for (int i = 0; i < s.length; ++i) {
      int sc = s.codeUnitAt(i);
      int tc = t.codeUnitAt(i);

      if (mapping.containsKey(sc)) {
        if (mapping[sc] != tc) return false;
      } else {
        if (used.contains(tc)) return false;
        mapping[sc] = tc;
        used.add(tc);
      }
    }

    return true;
  }
}
```

## Golang

```go
func isIsomorphic(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	mapping := make(map[byte]byte)
	used := make(map[byte]bool)

	for i := 0; i < len(s); i++ {
		cs := s[i]
		ct := t[i]

		if mapped, ok := mapping[cs]; ok {
			if mapped != ct {
				return false
			}
		} else {
			if used[ct] {
				return false
			}
			mapping[cs] = ct
			used[ct] = true
		}
	}
	return true
}
```

## Ruby

```ruby
def is_isomorphic(s, t)
  return false unless s.length == t.length
  map_s = {}
  map_t = {}

  s.each_char.with_index do |ch, i|
    ch2 = t[i]

    if map_s.key?(ch)
      return false unless map_s[ch] == ch2
    else
      map_s[ch] = ch2
    end

    if map_t.key?(ch2)
      return false unless map_t[ch2] == ch
    else
      map_t[ch2] = ch
    end
  end

  true
end
```

## Scala

```scala
object Solution {
    def isIsomorphic(s: String, t: String): Boolean = {
        if (s.length != t.length) return false
        val map = scala.collection.mutable.Map[Char, Char]()
        val used = scala.collection.mutable.Set[Char]()
        for (i <- 0 until s.length) {
            val c1 = s(i)
            val c2 = t(i)
            map.get(c1) match {
                case Some(ch) =>
                    if (ch != c2) return false
                case None =>
                    if (used.contains(c2)) return false
                    map(c1) = c2
                    used += c2
            }
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_isomorphic(s: String, t: String) -> bool {
        let s_bytes = s.as_bytes();
        let t_bytes = t.as_bytes();
        if s_bytes.len() != t_bytes.len() {
            return false;
        }
        let mut map_s = [0i32; 256];
        let mut map_t = [0i32; 256];
        for (i, (&cs, &ct)) in s_bytes.iter().zip(t_bytes.iter()).enumerate() {
            let idx = (i + 1) as i32;
            if map_s[cs as usize] != map_t[ct as usize] {
                return false;
            }
            map_s[cs as usize] = idx;
            map_t[ct as usize] = idx;
        }
        true
    }
}
```

## Racket

```racket
(define/contract (is-isomorphic s t)
  (-> string? string? boolean?)
  (let ((n (string-length s)))
    (if (not (= n (string-length t)))
        #false
        (let ((map-st (make-hash))
              (map-ts (make-hash))
              (result #true))
          (for ([i (in-range n)])
            (when result
              (define cs (string-ref s i))
              (define ct (string-ref t i))
              (define existing-s (hash-ref map-st cs #f))
              (define existing-t (hash-ref map-ts ct #f))
              (cond
                [(and existing-s (not (char=? existing-s ct)))
                 (set! result #false)]
                [(and existing-t (not (char=? existing-t cs)))
                 (set! result #false)]
                [else
                 (hash-set! map-st cs ct)
                 (hash-set! map-ts ct cs)])))
          result))))
```

## Erlang

```erlang
-spec is_isomorphic(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> boolean().
is_isomorphic(S, T) ->
    loop(S, T, #{}, #{}).

loop(<<>>, <<>>, _MapST, _MapTS) -> true;
loop(_, _, _MapST, _MapTS) -> false;
loop(<<SChar, SRest/binary>>, <<TChar, TRest/binary>>, MapST, MapTS) ->
    case maps:find(SChar, MapST) of
        error ->
            case maps:is_key(TChar, MapTS) of
                true -> false;
                false ->
                    NewMapST = maps:put(SChar, TChar, MapST),
                    NewMapTS = maps:put(TChar, SChar, MapTS),
                    loop(SRest, TRest, NewMapST, NewMapTS)
            end;
        {ok, ExistingT} ->
            if
                ExistingT =:= TChar -> loop(SRest, TRest, MapST, MapTS);
                true -> false
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_isomorphic(s :: String.t(), t :: String.t()) :: boolean()
  def is_isomorphic(s, t) do
    if byte_size(s) != byte_size(t) do
      false
    else
      cs = String.to_charlist(s)
      ct = String.to_charlist(t)

      result =
        Enum.reduce_while(Enum.zip(cs, ct), {%{}, %{}}, fn {c1, c2}, {map_s_t, map_t_s} ->
          case Map.get(map_s_t, c1) do
            nil ->
              if Map.has_key?(map_t_s, c2) do
                {:halt, :error}
              else
                {:cont,
                 {Map.put(map_s_t, c1, c2), Map.put(map_t_s, c2, c1)}}
              end

            ^c2 ->
              {:cont, {map_s_t, map_t_s}}

            _ ->
              {:halt, :error}
          end
        end)

      result != :error
    end
  end
end
```
