# 0859. Buddy Strings

## Cpp

```cpp
class Solution {
public:
    bool buddyStrings(string s, string goal) {
        if (s.size() != goal.size()) return false;
        if (s == goal) {
            int cnt[26] = {0};
            for (char c : s) {
                if (++cnt[c - 'a'] >= 2) return true;
            }
            return false;
        }
        vector<int> diff;
        for (int i = 0; i < (int)s.size(); ++i) {
            if (s[i] != goal[i]) {
                diff.push_back(i);
                if (diff.size() > 2) return false;
            }
        }
        return diff.size() == 2 && s[diff[0]] == goal[diff[1]] && s[diff[1]] == goal[diff[0]];
    }
};
```

## Java

```java
class Solution {
    public boolean buddyStrings(String s, String goal) {
        if (s.length() != goal.length()) return false;
        if (s.equals(goal)) {
            int[] cnt = new int[26];
            for (int i = 0; i < s.length(); i++) {
                int idx = s.charAt(i) - 'a';
                cnt[idx]++;
                if (cnt[idx] > 1) return true;
            }
            return false;
        } else {
            int first = -1, second = -1;
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) != goal.charAt(i)) {
                    if (first == -1) {
                        first = i;
                    } else if (second == -1) {
                        second = i;
                    } else {
                        return false; // more than 2 mismatches
                    }
                }
            }
            if (second == -1) return false; // less than 2 mismatches
            return s.charAt(first) == goal.charAt(second) && s.charAt(second) == goal.charAt(first);
        }
    }
}
```

## Python

```python
class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False

        if s == goal:
            # Need at least one duplicate character to swap and keep string unchanged
            seen = set()
            for ch in s:
                if ch in seen:
                    return True
                seen.add(ch)
            return False

        # Find positions where characters differ
        diff = []
        for i, (a, b) in enumerate(zip(s, goal)):
            if a != b:
                diff.append(i)
                if len(diff) > 2:
                    return False

        if len(diff) != 2:
            return False

        i, j = diff
        return s[i] == goal[j] and s[j] == goal[i]
```

## Python3

```python
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            # Need at least one duplicate character to swap and keep string unchanged
            return len(set(s)) < len(s)
        diff = []
        for i, (a, b) in enumerate(zip(s, goal)):
            if a != b:
                diff.append(i)
                if len(diff) > 2:
                    return False
        if len(diff) != 2:
            return False
        i, j = diff
        return s[i] == goal[j] and s[j] == goal[i]
```

## C

```c
#include <stdbool.h>
#include <string.h>

bool buddyStrings(char* s, char* goal) {
    int n = strlen(s);
    if (n != (int)strlen(goal)) return false;

    int diff[2];
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        if (s[i] != goal[i]) {
            if (cnt < 2) diff[cnt] = i;
            ++cnt;
            if (cnt > 2) return false;
        }
    }

    if (cnt == 0) {
        int freq[26] = {0};
        for (int i = 0; i < n; ++i) {
            int idx = s[i] - 'a';
            if (++freq[idx] > 1) return true;
        }
        return false;
    }

    if (cnt != 2) return false;

    int i = diff[0], j = diff[1];
    return s[i] == goal[j] && s[j] == goal[i];
}
```

## Csharp

```csharp
public class Solution
{
    public bool BuddyStrings(string s, string goal)
    {
        if (s.Length != goal.Length) return false;

        if (s == goal)
        {
            int[] count = new int[26];
            foreach (char c in s)
            {
                int idx = c - 'a';
                count[idx]++;
                if (count[idx] > 1) return true;
            }
            return false;
        }

        int first = -1, second = -1;
        for (int i = 0; i < s.Length; i++)
        {
            if (s[i] != goal[i])
            {
                if (first == -1)
                    first = i;
                else if (second == -1)
                    second = i;
                else
                    return false; // more than two mismatches
            }
        }

        if (second == -1) return false; // less than two mismatches

        return s[first] == goal[second] && s[second] == goal[first];
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {string} goal
 * @return {boolean}
 */
var buddyStrings = function(s, goal) {
    if (s.length !== goal.length) return false;
    
    if (s === goal) {
        const seen = new Set();
        for (const ch of s) {
            if (seen.has(ch)) return true;
            seen.add(ch);
        }
        return false;
    }
    
    const diff = [];
    for (let i = 0; i < s.length; i++) {
        if (s[i] !== goal[i]) {
            diff.push(i);
            if (diff.length > 2) return false;
        }
    }
    
    return diff.length === 2 &&
           s[diff[0]] === goal[diff[1]] &&
           s[diff[1]] === goal[diff[0]];
};
```

## Typescript

```typescript
function buddyStrings(s: string, goal: string): boolean {
    if (s.length !== goal.length) return false;
    const n = s.length;

    if (s === goal) {
        const seen = new Set<string>();
        for (const ch of s) {
            if (seen.has(ch)) return true;
            seen.add(ch);
        }
        return false;
    }

    const diff: number[] = [];
    for (let i = 0; i < n; i++) {
        if (s[i] !== goal[i]) {
            diff.push(i);
            if (diff.length > 2) return false;
        }
    }

    if (diff.length !== 2) return false;
    const [i, j] = diff;
    return s[i] === goal[j] && s[j] === goal[i];
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param String $goal
     * @return Boolean
     */
    function buddyStrings($s, $goal) {
        if (strlen($s) !== strlen($goal)) {
            return false;
        }

        if ($s === $goal) {
            $seen = [];
            $len = strlen($s);
            for ($i = 0; $i < $len; $i++) {
                $c = $s[$i];
                if (isset($seen[$c])) {
                    return true;
                }
                $seen[$c] = true;
            }
            return false;
        }

        $diff = [];
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] !== $goal[$i]) {
                $diff[] = $i;
                if (count($diff) > 2) {
                    return false;
                }
            }
        }

        if (count($diff) !== 2) {
            return false;
        }

        $i1 = $diff[0];
        $i2 = $diff[1];

        return ($s[$i1] === $goal[$i2]) && ($s[$i2] === $goal[$i1]);
    }
}
```

## Swift

```swift
class Solution {
    func buddyStrings(_ s: String, _ goal: String) -> Bool {
        if s.count != goal.count { return false }
        let n = s.count
        let sArr = Array(s)
        let gArr = Array(goal)
        
        if s == goal {
            var seen = Set<Character>()
            for ch in sArr {
                if seen.contains(ch) { return true }
                seen.insert(ch)
            }
            return false
        } else {
            var diff: [Int] = []
            for i in 0..<n {
                if sArr[i] != gArr[i] {
                    diff.append(i)
                    if diff.count > 2 { return false }
                }
            }
            if diff.count != 2 { return false }
            let i = diff[0], j = diff[1]
            return sArr[i] == gArr[j] && sArr[j] == gArr[i]
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun buddyStrings(s: String, goal: String): Boolean {
        if (s.length != goal.length) return false
        if (s == goal) {
            val seen = HashSet<Char>()
            for (c in s) {
                if (!seen.add(c)) return true
            }
            return false
        } else {
            var first = -1
            var second = -1
            for (i in s.indices) {
                if (s[i] != goal[i]) {
                    when {
                        first == -1 -> first = i
                        second == -1 -> second = i
                        else -> return false
                    }
                }
            }
            if (second == -1) return false
            return s[first] == goal[second] && s[second] == goal[first]
        }
    }
}
```

## Dart

```dart
class Solution {
  bool buddyStrings(String s, String goal) {
    if (s.length != goal.length) return false;
    if (s == goal) {
      var seen = <String>{};
      for (int i = 0; i < s.length; i++) {
        String ch = s[i];
        if (seen.contains(ch)) return true;
        seen.add(ch);
      }
      return false;
    } else {
      List<int> diff = [];
      for (int i = 0; i < s.length; i++) {
        if (s[i] != goal[i]) {
          diff.add(i);
          if (diff.length > 2) return false;
        }
      }
      if (diff.length != 2) return false;
      int i = diff[0], j = diff[1];
      return s[i] == goal[j] && s[j] == goal[i];
    }
  }
}
```

## Golang

```go
func buddyStrings(s string, goal string) bool {
	if len(s) != len(goal) {
		return false
	}
	if s == goal {
		var cnt [26]int
		for i := 0; i < len(s); i++ {
			idx := s[i] - 'a'
			cnt[idx]++
			if cnt[idx] > 1 {
				return true
			}
		}
		return false
	}
	diff := make([]int, 0, 2)
	for i := 0; i < len(s); i++ {
		if s[i] != goal[i] {
			diff = append(diff, i)
			if len(diff) > 2 {
				return false
			}
		}
	}
	if len(diff) != 2 {
		return false
	}
	i, j := diff[0], diff[1]
	return s[i] == goal[j] && s[j] == goal[i]
}
```

## Ruby

```ruby
def buddy_strings(s, goal)
  return false unless s.length == goal.length

  if s == goal
    seen = {}
    s.each_char do |ch|
      return true if seen[ch]
      seen[ch] = true
    end
    return false
  else
    diff = []
    s.length.times do |i|
      diff << i if s[i] != goal[i]
      return false if diff.size > 2
    end
    diff.size == 2 && s[diff[0]] == goal[diff[1]] && s[diff[1]] == goal[diff[0]]
  end
end
```

## Scala

```scala
object Solution {
  def buddyStrings(s: String, goal: String): Boolean = {
    if (s.length != goal.length) return false
    if (s == goal) {
      val seen = scala.collection.mutable.HashSet[Char]()
      for (c <- s) {
        if (!seen.add(c)) return true
      }
      false
    } else {
      val diffs = scala.collection.mutable.ArrayBuffer[Int]()
      var i = 0
      while (i < s.length && diffs.size <= 2) {
        if (s(i) != goal(i)) diffs += i
        i += 1
      }
      if (diffs.size != 2) return false
      val i1 = diffs(0)
      val i2 = diffs(1)
      s(i1) == goal(i2) && s(i2) == goal(i1)
    }
  }
}
```

## Rust

```rust
impl Solution {
    pub fn buddy_strings(s: String, goal: String) -> bool {
        if s.len() != goal.len() {
            return false;
        }
        let sb = s.as_bytes();
        let gb = goal.as_bytes();

        if s == goal {
            // Need at least one duplicate character to swap and keep the string unchanged
            let mut seen = [false; 26];
            for &c in sb {
                let idx = (c - b'a') as usize;
                if seen[idx] {
                    return true;
                }
                seen[idx] = true;
            }
            return false;
        } else {
            let mut diffs = Vec::with_capacity(2);
            for i in 0..sb.len() {
                if sb[i] != gb[i] {
                    diffs.push(i);
                    if diffs.len() > 2 {
                        return false;
                    }
                }
            }
            if diffs.len() != 2 {
                return false;
            }
            let i = diffs[0];
            let j = diffs[1];
            sb[i] == gb[j] && sb[j] == gb[i]
        }
    }
}
```

## Racket

```racket
(define/contract (buddy-strings s goal)
  (-> string? string? boolean?)
  (if (not (= (string-length s) (string-length goal)))
      #false
      (let ((n (string-length s)))
        (if (string=? s goal)
            ;; need at least one duplicate character
            (let ((counts (make-vector 26 0))
                  (found #false))
              (for ([i (in-range n)])
                (let* ((c (char->integer (string-ref s i)))
                       (idx (- c (char->integer #\a))))
                  (vector-set! counts idx (+ (vector-ref counts idx) 1))
                  (when (>= (vector-ref counts idx) 2)
                    (set! found #true))))
              found)
            ;; check mismatched positions
            (let ((diff '()))
              (for ([i (in-range n)])
                (unless (char=? (string-ref s i) (string-ref goal i))
                  (set! diff (cons i diff))))
              (if (= (length diff) 2)
                  (let* ((i1 (second diff))   ; earlier index
                         (i2 (first diff))    ; later index
                         (c1s (string-ref s i1))
                         (c1g (string-ref goal i1))
                         (c2s (string-ref s i2))
                         (c2g (string-ref goal i2)))
                    (and (char=? c1s c2g) (char=? c2s c1g)))
                  #false))))))
```

## Erlang

```erlang
-module(solution).
-export([buddy_strings/2]).

-spec buddy_strings(S :: unicode:unicode_binary(), Goal :: unicode:unicode_binary()) -> boolean().
buddy_strings(S, Goal) ->
    case byte_size(S) =:= byte_size(Goal) of
        false -> false;
        true ->
            if S =:= Goal ->
                has_duplicate(S);
               true ->
                mismatches(S, Goal)
            end
    end.

has_duplicate(Bin) ->
    has_duplicate(binary_to_list(Bin), #{}).

has_duplicate([], _) -> false;
has_duplicate([H|T], Seen) ->
    case maps:is_key(H, Seen) of
        true -> true;
        false -> has_duplicate(T, maps:put(H, true, Seen))
    end.

mismatches(S, Goal) ->
    ListS = binary_to_list(S),
    ListG = binary_to_list(Goal),
    case collect_mismatches(ListS, ListG, [], 0) of
        {ok, [{A,B},{C,D}], 2} when A =:= D, B =:= C -> true;
        _ -> false
    end.

collect_mismatches([], [], Acc, Count) ->
    {ok, lists:reverse(Acc), Count};
collect_mismatches([Hs|Ts], [Hg|Tg], Acc, Count) ->
    if Hs =:= Hg ->
        collect_mismatches(Ts, Tg, Acc, Count);
       true ->
        case Count of
            2 -> {error, too_many};
            _ -> collect_mismatches(Ts, Tg, [{Hs,Hg}|Acc], Count+1)
        end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec buddy_strings(s :: String.t(), goal :: String.t()) :: boolean()
  def buddy_strings(s, goal) do
    if byte_size(s) != byte_size(goal) do
      false
    else
      if s == goal do
        bytes = :binary.bin_to_list(s)
        has_duplicate?(bytes, MapSet.new())
      else
        s_bytes = :binary.bin_to_list(s)
        g_bytes = :binary.bin_to_list(goal)
        mismatches = find_mismatches(s_bytes, g_bytes, [])
        case mismatches do
          [{a1, b1}, {a2, b2}] -> a1 == b2 and a2 == b1
          _ -> false
        end
      end
    end
  end

  defp has_duplicate?([], _set), do: false
  defp has_duplicate?([h | t], set) do
    if MapSet.member?(set, h) do
      true
    else
      has_duplicate?(t, MapSet.put(set, h))
    end
  end

  defp find_mismatches([], [], acc), do: Enum.reverse(acc)
  defp find_mismatches([sh | st], [gh | gt], acc) do
    if sh == gh do
      find_mismatches(st, gt, acc)
    else
      find_mismatches(st, gt, [{sh, gh} | acc])
    end
  end
end
```
