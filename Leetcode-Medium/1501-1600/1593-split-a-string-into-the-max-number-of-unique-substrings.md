# 1593. Split a String Into the Max Number of Unique Substrings

## Cpp

```cpp
class Solution {
public:
    int maxUniqueSplit(string s) {
        unordered_set<string> seen;
        return dfs(0, s, seen);
    }
private:
    int dfs(int idx, const string& s, unordered_set<string>& seen) {
        if (idx == s.size()) return 0;
        int best = 0;
        for (int end = idx + 1; end <= s.size(); ++end) {
            string sub = s.substr(idx, end - idx);
            if (seen.find(sub) != seen.end()) continue;
            seen.insert(sub);
            best = max(best, 1 + dfs(end, s, seen));
            seen.erase(sub);
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public int maxUniqueSplit(String s) {
        return dfs(s, 0, new java.util.HashSet<>());
    }
    
    private int dfs(String s, int start, java.util.Set<String> seen) {
        if (start == s.length()) {
            return 0;
        }
        int best = 0;
        for (int end = start + 1; end <= s.length(); ++end) {
            String sub = s.substring(start, end);
            if (seen.contains(sub)) continue;
            seen.add(sub);
            int cur = 1 + dfs(s, end, seen);
            if (cur > best) best = cur;
            seen.remove(sub);
        }
        return best;
    }
}
```

## Python

```python
class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        seen = set()
        
        def dfs(start):
            if start == n:
                return 0
            best = 0
            # try all possible substrings starting at 'start'
            for end in range(start + 1, n + 1):
                sub = s[start:end]
                if sub not in seen:
                    seen.add(sub)
                    best = max(best, 1 + dfs(end))
                    seen.remove(sub)
            return best
        
        return dfs(0)
```

## Python3

```python
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        seen = set()
        
        from functools import lru_cache
        
        @lru_cache(maxsize=None)
        def dfs(i):
            if i == n:
                return 0
            best = 0
            # try all substrings starting at i
            for j in range(i + 1, n + 1):
                sub = s[i:j]
                if sub not in seen:
                    seen.add(sub)
                    best = max(best, 1 + dfs(j))
                    seen.remove(sub)
            return best
        
        return dfs(0)
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int best;

static void dfs(const char *s, int n, int start, char **used, int usedCount) {
    if (start == n) {
        if (usedCount > best) best = usedCount;
        return;
    }
    /* pruning: even if we split every remaining character separately,
       we cannot beat current best */
    if (usedCount + (n - start) <= best) return;

    for (int end = start + 1; end <= n; ++end) {
        int len = end - start;
        char buf[17];                     // max length is 16
        memcpy(buf, s + start, len);
        buf[len] = '\0';

        int unique = 1;
        for (int i = 0; i < usedCount; ++i) {
            if (strcmp(used[i], buf) == 0) {
                unique = 0;
                break;
            }
        }
        if (!unique) continue;

        char *copy = (char *)malloc(len + 1);
        memcpy(copy, buf, len + 1);
        used[usedCount] = copy;

        dfs(s, n, end, used, usedCount + 1);

        free(copy);
    }
}

int maxUniqueSplit(char* s) {
    int n = (int)strlen(s);
    char **used = (char **)malloc(sizeof(char *) * n); // at most n substrings
    best = 0;
    dfs(s, n, 0, used, 0);
    free(used);
    return best;
}
```

## Csharp

```csharp
public class Solution
{
    public int MaxUniqueSplit(string s)
    {
        var seen = new HashSet<string>();
        return Dfs(0);

        int Dfs(int start)
        {
            if (start == s.Length) return 0;
            int best = 0;
            for (int end = start + 1; end <= s.Length; ++end)
            {
                string sub = s.Substring(start, end - start);
                if (!seen.Contains(sub))
                {
                    seen.Add(sub);
                    int cur = 1 + Dfs(end);
                    if (cur > best) best = cur;
                    seen.Remove(sub);
                }
            }
            return best;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var maxUniqueSplit = function(s) {
    let maxCount = 0;
    const seen = new Set();

    function dfs(start) {
        // If reached end, update answer
        if (start === s.length) {
            maxCount = Math.max(maxCount, seen.size);
            return;
        }
        // Prune: even if we take each remaining character as a separate substring,
        // we cannot beat current best.
        if (seen.size + (s.length - start) <= maxCount) return;

        for (let end = start + 1; end <= s.length; ++end) {
            const sub = s.slice(start, end);
            if (!seen.has(sub)) {
                seen.add(sub);
                dfs(end);
                seen.delete(sub);
            }
        }
    }

    dfs(0);
    return maxCount;
};
```

## Typescript

```typescript
function maxUniqueSplit(s: string): number {
    const seen = new Set<string>();
    const n = s.length;

    function dfs(idx: number): number {
        if (idx === n) return 0;
        let best = 0;
        for (let end = idx + 1; end <= n; ++end) {
            const sub = s.slice(idx, end);
            if (!seen.has(sub)) {
                seen.add(sub);
                const cur = 1 + dfs(end);
                if (cur > best) best = cur;
                seen.delete(sub);
            }
        }
        return best;
    }

    return dfs(0);
}
```

## Php

```php
class Solution {
    private $max = 0;
    private $n = 0;

    /**
     * @param String $s
     * @return Integer
     */
    function maxUniqueSplit($s) {
        $this->max = 0;
        $this->n = strlen($s);
        $used = [];
        $this->dfs($s, 0, $used);
        return $this->max;
    }

    private function dfs($s, $start, &$used) {
        if ($start == $this->n) {
            $cnt = count($used);
            if ($cnt > $this->max) {
                $this->max = $cnt;
            }
            return;
        }

        // Prune if even taking each remaining character as a separate substring cannot beat current max
        $potential = count($used) + ($this->n - $start);
        if ($potential <= $this->max) {
            return;
        }

        for ($end = $start + 1; $end <= $this->n; $end++) {
            $sub = substr($s, $start, $end - $start);
            if (!isset($used[$sub])) {
                $used[$sub] = true;
                $this->dfs($s, $end, $used);
                unset($used[$sub]);
            }
        }
    }
}
```

## Swift

```swift
class Solution {
    func maxUniqueSplit(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var seen = Set<String>()
        var best = 0
        
        func dfs(_ index: Int, _ count: Int) {
            if index == n {
                if count > best { best = count }
                return
            }
            // Prune if even taking each remaining character separately can't beat current best
            if count + (n - index) <= best { return }
            
            var cur = ""
            for i in index..<n {
                cur.append(chars[i])
                if !seen.contains(cur) {
                    seen.insert(cur)
                    dfs(i + 1, count + 1)
                    seen.remove(cur)
                }
            }
        }
        
        dfs(0, 0)
        return best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxUniqueSplit(s: String): Int {
        val used = HashSet<String>()
        fun dfs(idx: Int): Int {
            if (idx == s.length) return 0
            var best = 0
            for (end in idx + 1..s.length) {
                val sub = s.substring(idx, end)
                if (!used.contains(sub)) {
                    used.add(sub)
                    val cur = 1 + dfs(end)
                    if (cur > best) best = cur
                    used.remove(sub)
                }
            }
            return best
        }
        return dfs(0)
    }
}
```

## Dart

```dart
class Solution {
  int maxUniqueSplit(String s) {
    final Set<String> seen = {};

    int dfs(int start) {
      if (start == s.length) return 0;
      int best = 0;
      for (int end = start + 1; end <= s.length; ++end) {
        String sub = s.substring(start, end);
        if (!seen.contains(sub)) {
          seen.add(sub);
          int cnt = 1 + dfs(end);
          if (cnt > best) best = cnt;
          seen.remove(sub);
        }
      }
      return best;
    }

    return dfs(0);
  }
}
```

## Golang

```go
func maxUniqueSplit(s string) int {
	seen := make(map[string]struct{})
	var dfs func(int) int
	dfs = func(idx int) int {
		if idx == len(s) {
			return 0
		}
		maxCount := 0
		for end := idx + 1; end <= len(s); end++ {
			sub := s[idx:end]
			if _, ok := seen[sub]; !ok {
				seen[sub] = struct{}{}
				cnt := 1 + dfs(end)
				if cnt > maxCount {
					maxCount = cnt
				}
				delete(seen, sub)
			}
		}
		return maxCount
	}
	return dfs(0)
}
```

## Ruby

```ruby
def max_unique_split(s)
  require 'set'
  n = s.length
  max = 0
  seen = Set.new

  dfs = nil
  dfs = ->(idx, count) do
    # prune if even taking each remaining character as a separate substring can't beat current max
    return if count + (n - idx) <= max

    if idx == n
      max = [max, count].max
      next
    end

    (idx + 1).upto(n) do |j|
      sub = s[idx...j]
      unless seen.include?(sub)
        seen.add(sub)
        dfs.call(j, count + 1)
        seen.delete(sub)
      end
    end
  end

  dfs.call(0, 0)
  max
end
```

## Scala

```scala
object Solution {
  def maxUniqueSplit(s: String): Int = {
    val seen = scala.collection.mutable.HashSet[String]()
    val n = s.length

    def dfs(start: Int): Int = {
      if (start == n) return 0
      var best = 0
      var end = start + 1
      while (end <= n) {
        val sub = s.substring(start, end)
        if (!seen.contains(sub)) {
          seen.add(sub)
          val cnt = 1 + dfs(end)
          if (cnt > best) best = cnt
          seen.remove(sub)
        }
        end += 1
      }
      best
    }

    dfs(0)
  }
}
```

## Rust

```rust
impl Solution {
    pub fn max_unique_split(s: String) -> i32 {
        fn dfs(s: &str, start: usize, seen: &mut std::collections::HashSet<String>) -> i32 {
            if start == s.len() {
                return 0;
            }
            let mut best = 0;
            for end in start + 1..=s.len() {
                let sub = &s[start..end];
                if !seen.contains(sub) {
                    seen.insert(sub.to_string());
                    let cnt = 1 + dfs(s, end, seen);
                    if cnt > best {
                        best = cnt;
                    }
                    seen.remove(sub);
                }
            }
            best
        }

        let mut used = std::collections::HashSet::new();
        dfs(&s, 0, &mut used) as i32
    }
}
```

## Racket

```racket
(define/contract (max-unique-split s)
  (-> string? exact-integer?)
  (let* ((n (string-length s))
         (seen (make-hash))
         (best (box 0)))
    (define (dfs start cnt)
      ;; prune if even taking each remaining char as a new substring can't beat best
      (when (> (+ cnt (- n start)) (unbox best))
        (if (= start n)
            (let ([newcnt cnt])
              (when (> newcnt (unbox best))
                (set-box! best newcnt)))
            (for ([end (in-range (add1 start) (add1 n))])
              (define sub (substring s start end))
              (unless (hash-has-key? seen sub)
                (hash-set! seen sub #t)
                (dfs end (+ cnt 1))
                (hash-remove! seen sub)))))))
    (dfs 0 0)
    (unbox best)))
```

## Erlang

```erlang
-module(solution).
-export([max_unique_split/1]).

-spec max_unique_split(S :: unicode:unicode_binary()) -> integer().
max_unique_split(S) ->
    dfs(S, 0, sets:new()).

dfs(S, Start, Used) ->
    Len = byte_size(S),
    if
        Start == Len ->
            0;
        true ->
            max_split_loop(S, Start, Start + 1, Len, Used, 0)
    end.

max_split_loop(_S, _Start, End, Len, _Used, Max) when End > Len ->
    Max;
max_split_loop(S, Start, End, Len, Used, Max) ->
    Sub = binary:part(S, {Start, End - Start}),
    case sets:is_element(Sub, Used) of
        true ->
            max_split_loop(S, Start, End + 1, Len, Used, Max);
        false ->
            NewUsed = sets:add_element(Sub, Used),
            Rec = 1 + dfs(S, End, NewUsed),
            NewMax = if Rec > Max -> Rec; true -> Max end,
            max_split_loop(S, Start, End + 1, Len, Used, NewMax)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_unique_split(s :: String.t()) :: integer()
  def max_unique_split(s) do
    dfs(s, 0, MapSet.new())
  end

  defp dfs(s, start, seen) do
    n = String.length(s)

    if start == n do
      0
    else
      Enum.reduce((start + 1)..n, 0, fn finish, best ->
        sub = String.slice(s, start, finish - start)

        if MapSet.member?(seen, sub) do
          best
        else
          cnt = 1 + dfs(s, finish, MapSet.put(seen, sub))
          if cnt > best, do: cnt, else: best
        end
      end)
    end
  end
end
```
