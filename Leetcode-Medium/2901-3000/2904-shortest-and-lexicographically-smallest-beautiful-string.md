# 2904. Shortest and Lexicographically Smallest Beautiful String

## Cpp

```cpp
class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        int n = s.size();
        vector<int> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = pref[i] + (s[i] == '1');
        }
        string best = "";
        int minLen = n + 1;
        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j) {
                int ones = pref[j + 1] - pref[i];
                if (ones == k) {
                    int len = j - i + 1;
                    string cur = s.substr(i, len);
                    if (len < minLen) {
                        minLen = len;
                        best = cur;
                    } else if (len == minLen && cur < best) {
                        best = cur;
                    }
                    // Since increasing j will only increase length,
                    // we can break to keep shortest for this i.
                    break;
                }
            }
        }
        return best;
    }
};
```

## Java

```java
class Solution {
    public String shortestBeautifulSubstring(String s, int k) {
        int n = s.length();
        int bestLen = Integer.MAX_VALUE;
        String best = "";
        for (int i = 0; i < n; i++) {
            int cnt = 0;
            for (int j = i; j < n; j++) {
                if (s.charAt(j) == '1') cnt++;
                if (cnt == k) {
                    int len = j - i + 1;
                    String cand = s.substring(i, j + 1);
                    if (len < bestLen) {
                        bestLen = len;
                        best = cand;
                    } else if (len == bestLen && cand.compareTo(best) < 0) {
                        best = cand;
                    }
                    break; // shortest for this start index
                }
            }
        }
        return bestLen == Integer.MAX_VALUE ? "" : best;
    }
}
```

## Python

```python
class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i+1] = pref[i] + (s[i] == '1')
        
        best_len = float('inf')
        best_sub = ""
        for i in range(n):
            # early break if remaining length can't beat current best
            if n - i < best_len:
                # still need to check because maybe shorter not found yet
                pass
            for j in range(i+1, n+1):
                cnt = pref[j] - pref[i]
                if cnt == k:
                    cur_len = j - i
                    cur_sub = s[i:j]
                    if cur_len < best_len or (cur_len == best_len and cur_sub < best_sub):
                        best_len = cur_len
                        best_sub = cur_sub
                    # Since we are looking for shortest for this start, we can break after first match
                    break
                elif cnt > k:
                    # further j will only increase count, so break
                    break
        return best_sub if best_len != float('inf') else ""
```

## Python3

```python
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        best_len = float('inf')
        best_sub = ""
        for i in range(n):
            cnt = 0
            for j in range(i, n):
                if s[j] == '1':
                    cnt += 1
                if cnt == k:
                    cur_len = j - i + 1
                    cur_sub = s[i:j+1]
                    if cur_len < best_len or (cur_len == best_len and cur_sub < best_sub):
                        best_len = cur_len
                        best_sub = cur_sub
                    break
                if cnt > k:
                    break
        return best_sub if best_len != float('inf') else ""
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <limits.h>

char* shortestBeautifulSubstring(char* s, int k) {
    int n = strlen(s);
    int pref[101] = {0};
    for (int i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] + (s[i] == '1');
    }

    int bestLen = INT_MAX;
    char bestStr[101];
    int found = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = i; j < n; ++j) {
            int ones = pref[j + 1] - pref[i];
            if (ones == k) {
                int len = j - i + 1;
                if (len < bestLen) {
                    bestLen = len;
                    memcpy(bestStr, s + i, len);
                    bestStr[len] = '\0';
                    found = 1;
                } else if (len == bestLen) {
                    int cmp = strncmp(s + i, bestStr, len);
                    if (cmp < 0) {
                        memcpy(bestStr, s + i, len);
                        bestStr[len] = '\0';
                    }
                }
                break; // shortest for this start index
            } else if (ones > k) {
                break;
            }
        }
    }

    if (!found) {
        char *res = (char *)malloc(1);
        res[0] = '\0';
        return res;
    }

    char *res = (char *)malloc(bestLen + 1);
    memcpy(res, bestStr, bestLen);
    res[bestLen] = '\0';
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string ShortestBeautifulSubstring(string s, int k)
    {
        int n = s.Length;
        int[] pref = new int[n + 1];
        for (int i = 0; i < n; i++)
            pref[i + 1] = pref[i] + (s[i] == '1' ? 1 : 0);

        int bestLen = int.MaxValue;
        string best = "";
        bool found = false;

        for (int i = 0; i < n; i++)
        {
            for (int j = i; j < n; j++)
            {
                int cnt = pref[j + 1] - pref[i];
                if (cnt == k)
                {
                    int len = j - i + 1;
                    string sub = s.Substring(i, len);
                    if (!found || len < bestLen ||
                        (len == bestLen && string.CompareOrdinal(sub, best) < 0))
                    {
                        bestLen = len;
                        best = sub;
                        found = true;
                    }
                    break; // shortest for this i
                }
                else if (cnt > k)
                {
                    break; // cannot reach exactly k later
                }
            }
        }

        return found ? best : "";
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var shortestBeautifulSubstring = function(s, k) {
    const n = s.length;
    let bestLen = Infinity;
    let bestStr = "";
    for (let i = 0; i < n; i++) {
        let cnt = 0;
        for (let j = i; j < n; j++) {
            if (s[j] === '1') cnt++;
            if (cnt === k) {
                const len = j - i + 1;
                const sub = s.substring(i, j + 1);
                if (len < bestLen || (len === bestLen && sub < bestStr)) {
                    bestLen = len;
                    bestStr = sub;
                }
                break; // shortest for this start index
            }
        }
    }
    return bestLen === Infinity ? "" : bestStr;
};
```

## Typescript

```typescript
function shortestBeautifulSubstring(s: string, k: number): string {
    const n = s.length;
    let minLen = Number.MAX_SAFE_INTEGER;
    let best = "";
    for (let i = 0; i < n; i++) {
        let cnt = 0;
        for (let j = i; j < n; j++) {
            if (s[j] === '1') cnt++;
            if (cnt === k) {
                const len = j - i + 1;
                const sub = s.substring(i, j + 1);
                if (len < minLen) {
                    minLen = len;
                    best = sub;
                } else if (len === minLen && sub < best) {
                    best = sub;
                }
                break; // shortest for this i
            }
        }
    }
    return minLen === Number.MAX_SAFE_INTEGER ? "" : best;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function shortestBeautifulSubstring($s, $k) {
        $n = strlen($s);
        $minLen = PHP_INT_MAX;
        $best = "";
        for ($i = 0; $i < $n; $i++) {
            $cnt = 0;
            for ($j = $i; $j < $n; $j++) {
                if ($s[$j] === '1') {
                    $cnt++;
                }
                if ($cnt == $k) {
                    $len = $j - $i + 1;
                    $sub = substr($s, $i, $len);
                    if ($len < $minLen || ($len == $minLen && strcmp($sub, $best) < 0)) {
                        $minLen = $len;
                        $best = $sub;
                    }
                    break; // shortest for this i
                } elseif ($cnt > $k) {
                    break; // cannot become exactly k later
                }
            }
        }
        return $best;
    }
}
```

## Swift

```swift
class Solution {
    func shortestBeautifulSubstring(_ s: String, _ k: Int) -> String {
        let chars = Array(s)
        let n = chars.count
        var minLen = Int.max
        var best = ""
        
        for i in 0..<n {
            var count = 0
            for j in i..<n {
                if chars[j] == "1" { count += 1 }
                
                if count == k {
                    let len = j - i + 1
                    let candidate = String(chars[i...j])
                    if len < minLen {
                        minLen = len
                        best = candidate
                    } else if len == minLen && candidate < best {
                        best = candidate
                    }
                    break   // shortest for this start index
                } else if count > k {
                    break   // cannot reach exactly k later
                }
            }
        }
        
        return minLen == Int.max ? "" : best
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun shortestBeautifulSubstring(s: String, k: Int): String {
        val n = s.length
        var bestLen = Int.MAX_VALUE
        var bestStr = ""
        for (i in 0 until n) {
            var cnt = 0
            for (j in i until n) {
                if (s[j] == '1') cnt++
                if (cnt == k) {
                    val len = j - i + 1
                    val cand = s.substring(i, j + 1)
                    if (len < bestLen) {
                        bestLen = len
                        bestStr = cand
                    } else if (len == bestLen && cand < bestStr) {
                        bestStr = cand
                    }
                    break
                }
            }
        }
        return if (bestLen == Int.MAX_VALUE) "" else bestStr
    }
}
```

## Dart

```dart
class Solution {
  String shortestBeautifulSubstring(String s, int k) {
    int n = s.length;
    List<int> pref = List.filled(n + 1, 0);
    for (int i = 0; i < n; i++) {
      pref[i + 1] = pref[i] + (s.codeUnitAt(i) == 49 ? 1 : 0); // '1' ascii 49
    }

    int bestLen = n + 1;
    String best = '';

    for (int i = 0; i < n; i++) {
      for (int j = i; j < n; j++) {
        int cnt = pref[j + 1] - pref[i];
        if (cnt == k) {
          int len = j - i + 1;
          String sub = s.substring(i, j + 1);
          if (len < bestLen ||
              (len == bestLen && (best.isEmpty || sub.compareTo(best) < 0))) {
            bestLen = len;
            best = sub;
          }
          break; // shortest for this i
        } else if (cnt > k) {
          break; // further extension can't reduce count of '1's
        }
      }
    }

    return best;
  }
}
```

## Golang

```go
func shortestBeautifulSubstring(s string, k int) string {
	n := len(s)
	minLen := n + 1
	ans := ""
	for i := 0; i < n; i++ {
		cnt := 0
		for j := i; j < n; j++ {
			if s[j] == '1' {
				cnt++
			}
			if cnt == k {
				length := j - i + 1
				sub := s[i : j+1]
				if length < minLen {
					minLen = length
					ans = sub
				} else if length == minLen && sub < ans {
					ans = sub
				}
				break
			}
		}
	}
	if minLen > n {
		return ""
	}
	return ans
}
```

## Ruby

```ruby
def shortest_beautiful_substring(s, k)
  n = s.length
  min_len = Float::INFINITY
  best = nil

  (0...n).each do |i|
    cnt = 0
    (i...n).each do |j|
      cnt += 1 if s[j] == '1'
      if cnt == k
        len = j - i + 1
        substr = s[i..j]
        if len < min_len || (len == min_len && (best.nil? || substr < best))
          min_len = len
          best = substr
        end
        break
      elsif cnt > k
        break
      end
    end
  end

  best ? best : ""
end
```

## Scala

```scala
object Solution {
    def shortestBeautifulSubstring(s: String, k: Int): String = {
        val n = s.length
        var minLen = Int.MaxValue
        var ans = ""
        for (i <- 0 until n) {
            var cnt = 0
            var j = i
            while (j < n && cnt < k) {
                if (s.charAt(j) == '1') cnt += 1
                j += 1
            }
            if (cnt == k) {
                val len = j - i
                val cand = s.substring(i, j)
                if (len < minLen) {
                    minLen = len
                    ans = cand
                } else if (len == minLen && cand < ans) {
                    ans = cand
                }
            }
        }
        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn shortest_beautiful_substring(s: String, k: i32) -> String {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let target = k as usize;
        let mut min_len = usize::MAX;
        let mut ans = String::new();

        for i in 0..n {
            let mut cnt = 0usize;
            for j in i..n {
                if bytes[j] == b'1' {
                    cnt += 1;
                }
                if cnt == target {
                    let len = j - i + 1;
                    if len < min_len {
                        min_len = len;
                        ans = s[i..j + 1].to_string();
                    } else if len == min_len {
                        let cand = &s[i..j + 1];
                        if cand < ans.as_str() {
                            ans = cand.to_string();
                        }
                    }
                    break;
                } else if cnt > target {
                    break;
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (shortest-beautiful-substring s k)
  (-> string? exact-integer? string?)
  (let* ((n (string-length s))
         (best-len (+ n 1))
         (best-str ""))
    (for ([i (in-range n)])
      (let loop ((j i) (cnt 0))
        (when (< j n)
          (define new-cnt
            (if (char=? (string-ref s j) #\1) (+ cnt 1) cnt))
          (cond
            [(= new-cnt k)
             (define len (- j i -1)) ; length = j-i+1
             (define substr (substring s i (+ j 1)))
             (if (< len best-len)
                 (begin
                   (set! best-len len)
                   (set! best-str substr))
                 (when (and (= len best-len) (string<? substr best-str))
                   (set! best-str substr)))]
            [(< new-cnt k)
             (loop (+ j 1) new-cnt)])))
      )
    best-str))
```

## Erlang

```erlang
-module(solution).
-export([shortest_beautiful_substring/2]).

-spec shortest_beautiful_substring(unicode:unicode_binary(), integer()) -> unicode:unicode_binary().
shortest_beautiful_substring(S, K) ->
    N = byte_size(S),
    List = binary_to_list(S),
    {BestLen, BestSub} = outer(0, N, K, S, List, N + 1, <<>>),
    case BestLen of
        L when L =< N -> BestSub;
        _ -> <<>>
    end.

outer(I, N, _K, _S, _List, BestLen, BestSub) when I >= N ->
    {BestLen, BestSub};
outer(I, N, K, S, List, BestLen, BestSub) ->
    case find_candidate(I, K, N, S, List) of
        none ->
            outer(I + 1, N, K, S, List, BestLen, BestSub);
        {Len, Sub} ->
            NewBest =
                if Len < BestLen -> {Len, Sub};
                   Len == BestLen andalso (BestSub =:= <<>> orelse Sub < BestSub) -> {Len, Sub};
                   true -> {BestLen, BestSub}
                end,
            {NewBestLen, NewBestSub} = NewBest,
            outer(I + 1, N, K, S, List, NewBestLen, NewBestSub)
    end.

find_candidate(I, K, N, S, List) ->
    find_candidate(I, 0, I, K, N, S, List).

find_candidate(_I, _Count, J, _K, N, _S, _List) when J >= N ->
    none;
find_candidate(I, Count, J, K, N, S, List) ->
    Char = lists:nth(J + 1, List),
    NewCount = case Char of
        $1 -> Count + 1;
        _ -> Count
    end,
    if NewCount == K ->
            Len = J - I + 1,
            Sub = binary:part(S, {I, Len}),
            {Len, Sub};
       true ->
            find_candidate(I, NewCount, J + 1, K, N, S, List)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec shortest_beautiful_substring(s :: String.t(), k :: integer()) :: String.t()
  def shortest_beautiful_substring(s, k) do
    chars = String.graphemes(s)
    n = length(chars)

    {min_len, best} =
      Enum.reduce(0..(n - 1), {nil, ""}, fn i, {cur_min, cur_best} ->
        case find_from(i, chars, k) do
          nil ->
            {cur_min, cur_best}

          {len, sub} ->
            cond do
              cur_min == nil or len < cur_min ->
                {len, sub}

              len == cur_min and sub < cur_best ->
                {len, sub}

              true ->
                {cur_min, cur_best}
            end
        end
      end)

    if min_len == nil, do: "", else: best
  end

  defp find_from(start, chars, k) do
    n = length(chars)
    do_find(start, start, 0, n, chars, k)
  end

  defp do_find(_i, j, _cnt, n, _chars, _k) when j == n, do: nil

  defp do_find(i, j, cnt, n, chars, k) do
    cnt = cnt + if Enum.at(chars, j) == "1", do: 1, else: 0

    cond do
      cnt == k ->
        len = j - i + 1
        sub = Enum.slice(chars, i, len) |> Enum.join()
        {len, sub}

      cnt > k ->
        nil

      true ->
        do_find(i, j + 1, cnt, n, chars, k)
    end
  end
end
```
