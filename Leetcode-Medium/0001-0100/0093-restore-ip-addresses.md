# 0093. Restore IP Addresses

## Cpp

```cpp
class Solution {
    std::vector<std::string> result;
    std::string current;
    std::string s;
    
    void dfs(int idx, int segment) {
        int n = s.size();
        if (segment == 4) {
            if (idx == n) result.push_back(current);
            return;
        }
        int remainingSeg = 4 - segment;
        int remainingChars = n - idx;
        if (remainingChars < remainingSeg || remainingChars > remainingSeg * 3) return;
        
        for (int len = 1; len <= 3 && idx + len <= n; ++len) {
            if (len > 1 && s[idx] == '0') break; // leading zero not allowed
            int val = std::stoi(s.substr(idx, len));
            if (val > 255) continue;
            
            int savedLen = current.size();
            if (!current.empty()) current.push_back('.');
            current.append(s, idx, len);
            
            dfs(idx + len, segment + 1);
            
            current.resize(savedLen);
        }
    }
    
public:
    std::vector<std::string> restoreIpAddresses(std::string str) {
        s = std::move(str);
        if (s.empty() || s.size() > 12) return {};
        dfs(0, 0);
        return result;
    }
};
```

## Java

```java
class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> result = new ArrayList<>();
        if (s == null || s.length() < 4 || s.length() > 12) {
            return result;
        }
        backtrack(s, 0, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(String s, int start, List<String> current, List<String> result) {
        if (current.size() == 4) {
            if (start == s.length()) {
                result.add(String.join(".", current));
            }
            return;
        }

        int remainingSegments = 4 - current.size();
        int remainingChars = s.length() - start;
        if (remainingChars < remainingSegments || remainingChars > remainingSegments * 3) {
            return; // prune impossible paths
        }

        for (int len = 1; len <= 3 && start + len <= s.length(); len++) {
            String part = s.substring(start, start + len);
            if (isValid(part)) {
                current.add(part);
                backtrack(s, start + len, current, result);
                current.remove(current.size() - 1);
            }
        }
    }

    private boolean isValid(String str) {
        if (str.length() > 1 && str.charAt(0) == '0') {
            return false;
        }
        int val = Integer.parseInt(str);
        return val <= 255;
    }
}
```

## Python

```python
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n < 4 or n > 12:
            return []
        
        res = []
        
        def backtrack(start, parts):
            # parts is list of current segments
            if len(parts) == 4:
                if start == n:
                    res.append('.'.join(parts))
                return
            # prune: remaining chars must fit into remaining slots (1-3 each)
            remaining_parts = 4 - len(parts)
            min_needed = remaining_parts  # at least 1 char per part
            max_allowed = remaining_parts * 3
            remaining_chars = n - start
            if remaining_chars < min_needed or remaining_chars > max_allowed:
                return
            
            # try segment lengths 1 to 3
            for l in range(1, 4):
                if start + l > n:
                    break
                seg = s[start:start+l]
                # leading zero check
                if (seg[0] == '0' and l > 1) or int(seg) > 255:
                    continue
                backtrack(start + l, parts + [seg])
        
        backtrack(0, [])
        return res
```

## Python3

```python
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n < 4 or n > 12:
            return []
        
        res: List[str] = []

        def is_valid(seg: str) -> bool:
            # no leading zeros unless the segment is exactly "0"
            if len(seg) > 1 and seg[0] == '0':
                return False
            return int(seg) <= 255

        def backtrack(start: int, parts: List[str]) -> None:
            # If we already have 4 parts, check if we've consumed all characters
            if len(parts) == 4:
                if start == n:
                    res.append('.'.join(parts))
                return
            
            # prune: remaining chars must fit into remaining slots (1-3 each)
            remaining_parts = 4 - len(parts)
            min_needed = remaining_parts          # at least 1 char per part
            max_allowed = remaining_parts * 3     # at most 3 chars per part
            remaining_len = n - start
            if remaining_len < min_needed or remaining_len > max_allowed:
                return
            
            # try segments of length 1 to 3
            for l in range(1, 4):
                if start + l > n:
                    break
                seg = s[start:start + l]
                if is_valid(seg):
                    parts.append(seg)
                    backtrack(start + l, parts)
                    parts.pop()
        
        backtrack(0, [])
        return res
```

## C

```c
/****
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>
#include <string.h>

static int isValidSegment(const char *s, int start, int len) {
    if (len > 1 && s[start] == '0') return 0;          // leading zero
    int val = 0;
    for (int i = 0; i < len; ++i) {
        val = val * 10 + (s[start + i] - '0');
        if (val > 255) return 0;
    }
    return 1;
}

static void addResult(char ***res, int *size, int *cap, const char *ip, int len) {
    if (*size >= *cap) {
        *cap = (*cap == 0) ? 16 : (*cap * 2);
        *res = realloc(*res, (*cap) * sizeof(char*));
    }
    (*res)[*size] = (char*)malloc(len + 1);
    memcpy((*res)[*size], ip, len);
    (*res)[*size][len] = '\0';
    (*size)++;
}

static void backtrack(const char *s, int slen, int start,
                      int seg, char *path, int pathLen,
                      char ***res, int *size, int *cap) {
    if (seg == 4) {
        if (start == slen) {
            addResult(res, size, cap, path, pathLen);
        }
        return;
    }

    // remaining segments after this one
    int remainSeg = 4 - seg - 1;
    for (int l = 1; l <= 3 && start + l <= slen; ++l) {
        int remainChars = slen - (start + l);
        if (remainChars < remainSeg || remainChars > remainSeg * 3)
            continue; // prune impossible lengths

        if (!isValidSegment(s, start, l))
            continue;

        // copy segment
        memcpy(path + pathLen, s + start, l);
        int newPathLen = pathLen + l;
        if (seg < 3) {
            path[newPathLen] = '.';
            newPathLen++;
        }
        backtrack(s, slen, start + l, seg + 1, path, newPathLen,
                  res, size, cap);
        // no need to undo, next iteration overwrites
    }
}

char** restoreIpAddresses(char* s, int* returnSize) {
    *returnSize = 0;
    char **result = NULL;
    int capacity = 0;

    int len = strlen(s);
    if (len < 4 || len > 12)
        return result;

    char path[16]; // max "255.255.255.255" + '\0' = 16
    backtrack(s, len, 0, 0, path, 0, &result, returnSize, &capacity);
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public IList<string> RestoreIpAddresses(string s)
    {
        var result = new List<string>();
        if (s == null || s.Length < 4 || s.Length > 12) return result;
        var segments = new string[4];
        Dfs(s, 0, 0, segments, result);
        return result;
    }

    private void Dfs(string s, int index, int segIdx, string[] segments, List<string> result)
    {
        if (segIdx == 4)
        {
            if (index == s.Length)
                result.Add(string.Join(".", segments));
            return;
        }

        // remaining characters must fit into remaining segments
        int remainingSegments = 4 - segIdx;
        int remainingChars = s.Length - index;
        if (remainingChars < remainingSegments || remainingChars > remainingSegments * 3) return;

        for (int len = 1; len <= 3 && index + len <= s.Length; len++)
        {
            // leading zero check
            if (len > 1 && s[index] == '0') break;

            string part = s.Substring(index, len);
            int val = 0;
            // parse manually to avoid overhead
            for (int i = 0; i < len; i++)
                val = val * 10 + (s[index + i] - '0');

            if (val > 255) continue;

            segments[segIdx] = part;
            Dfs(s, index + len, segIdx + 1, segments, result);
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @return {string[]}
 */
var restoreIpAddresses = function(s) {
    const res = [];
    const n = s.length;
    if (n < 4 || n > 12) return res;

    const backtrack = (start, parts, path) => {
        if (parts === 4) {
            if (start === n) res.push(path.join('.'));
            return;
        }

        const remainingParts = 4 - parts;
        const remainingChars = n - start;
        if (remainingChars < remainingParts || remainingChars > remainingParts * 3) return;

        for (let len = 1; len <= 3 && start + len <= n; len++) {
            const seg = s.substring(start, start + len);
            if (seg.length > 1 && seg[0] === '0') break;
            const val = Number(seg);
            if (val > 255) continue;
            path.push(seg);
            backtrack(start + len, parts + 1, path);
            path.pop();
        }
    };

    backtrack(0, 0, []);
    return res;
};
```

## Typescript

```typescript
function restoreIpAddresses(s: string): string[] {
    const result: string[] = [];
    if (s.length < 4 || s.length > 12) return result;

    const backtrack = (start: number, parts: string[]) => {
        if (parts.length === 4) {
            if (start === s.length) result.push(parts.join('.'));
            return;
        }

        const remaining = s.length - start;
        const needed = 4 - parts.length;
        if (remaining < needed || remaining > needed * 3) return;

        for (let len = 1; len <= 3 && start + len <= s.length; len++) {
            const segment = s.substring(start, start + len);
            if (segment[0] === '0' && len > 1) continue;
            const val = parseInt(segment, 10);
            if (val > 255) continue;

            parts.push(segment);
            backtrack(start + len, parts);
            parts.pop();
        }
    };

    backtrack(0, []);
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @return String[]
     */
    function restoreIpAddresses($s) {
        $len = strlen($s);
        if ($len < 4 || $len > 12) {
            return [];
        }
        $result = [];
        $this->backtrack($s, 0, [], $result);
        return $result;
    }

    private function backtrack(string $s, int $start, array &$segments, array &$result) {
        if (count($segments) == 4) {
            if ($start == strlen($s)) {
                $result[] = implode('.', $segments);
            }
            return;
        }

        $remainingSegments = 4 - count($segments);
        $maxLen = min(3, strlen($s) - $start - ($remainingSegments - 1));
        for ($len = 1; $len <= $maxLen; $len++) {
            if ($start + $len > strlen($s)) {
                break;
            }
            $segment = substr($s, $start, $len);
            if ($this->isValid($segment)) {
                $segments[] = $segment;
                $this->backtrack($s, $start + $len, $segments, $result);
                array_pop($segments);
            }
        }
    }

    private function isValid(string $seg): bool {
        if (strlen($seg) > 1 && $seg[0] === '0') {
            return false;
        }
        $val = intval($seg);
        return $val >= 0 && $val <= 255;
    }
}
```

## Swift

```swift
class Solution {
    func restoreIpAddresses(_ s: String) -> [String] {
        var results = [String]()
        let chars = Array(s)
        let n = chars.count
        
        func backtrack(_ index: Int, _ parts: [String]) {
            if parts.count == 4 {
                if index == n {
                    results.append(parts.joined(separator: "."))
                }
                return
            }
            
            // prune impossible lengths
            let remainingSegments = 4 - parts.count
            let remainingChars = n - index
            if remainingChars < remainingSegments || remainingChars > remainingSegments * 3 {
                return
            }
            
            for len in 1...3 {
                if index + len > n { break }
                // leading zero check
                if chars[index] == "0" && len > 1 { continue }
                let segment = String(chars[index..<(index + len)])
                if let val = Int(segment), val <= 255 {
                    backtrack(index + len, parts + [segment])
                }
            }
        }
        
        backtrack(0, [])
        return results
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun restoreIpAddresses(s: String): List<String> {
        val result = mutableListOf<String>()
        if (s.length < 4 || s.length > 12) return result

        fun backtrack(start: Int, parts: MutableList<String>) {
            if (parts.size == 4) {
                if (start == s.length) {
                    result.add(parts.joinToString("."))
                }
                return
            }

            val remainingParts = 4 - parts.size
            val remainingLen = s.length - start
            if (remainingLen < remainingParts || remainingLen > remainingParts * 3) return

            for (len in 1..3) {
                if (start + len > s.length) break
                if (len != 1 && s[start] == '0') continue
                val segment = s.substring(start, start + len)
                if (segment.toInt() > 255) continue
                parts.add(segment)
                backtrack(start + len, parts)
                parts.removeAt(parts.size - 1)
            }
        }

        backtrack(0, mutableListOf())
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> restoreIpAddresses(String s) {
    List<String> res = [];
    if (s.length < 4 || s.length > 12) return res;
    _backtrack(s, 0, [], res);
    return res;
  }

  void _backtrack(String s, int index, List<String> path, List<String> res) {
    if (path.length == 4) {
      if (index == s.length) {
        res.add(path.join('.'));
      }
      return;
    }

    int remaining = s.length - index;
    int needed = 4 - path.length;
    if (remaining < needed || remaining > needed * 3) return;

    for (int len = 1; len <= 3 && index + len <= s.length; ++len) {
      String segment = s.substring(index, index + len);
      if (!_isValid(segment)) continue;
      path.add(segment);
      _backtrack(s, index + len, path, res);
      path.removeLast();
    }
  }

  bool _isValid(String seg) {
    if (seg.length > 1 && seg[0] == '0') return false;
    int val = int.parse(seg);
    return val <= 255;
  }
}
```

## Golang

```go
import (
	"strconv"
	"strings"
)

func restoreIpAddresses(s string) []string {
	var result []string
	if len(s) < 4 || len(s) > 12 {
		return result
	}
	var dfs func(start int, parts []string)
	dfs = func(start int, parts []string) {
		if len(parts) == 4 {
			if start == len(s) {
				result = append(result, strings.Join(parts, "."))
			}
			return
		}
		remaining := len(s) - start
		need := 4 - len(parts)
		if remaining < need || remaining > need*3 {
			return
		}
		for l := 1; l <= 3 && start+l <= len(s); l++ {
			seg := s[start : start+l]
			if seg[0] == '0' && l > 1 {
				continue
			}
			val, _ := strconv.Atoi(seg)
			if val > 255 {
				continue
			}
			dfs(start+l, append(parts, seg))
		}
	}
	dfs(0, []string{})
	return result
}
```

## Ruby

```ruby
def restore_ip_addresses(s)
  res = []
  return res if s.length < 4 || s.length > 12

  valid = lambda do |seg|
    return false if seg.length > 1 && seg[0] == '0'
    seg.to_i <= 255
  end

  dfs = nil
  dfs = lambda do |start_idx, parts|
    if parts.size == 4
      res << parts.join('.') if start_idx == s.length
      return
    end

    remaining = s.length - start_idx
    needed = 4 - parts.size
    return if remaining < needed || remaining > needed * 3

    (1..3).each do |len|
      break if start_idx + len > s.length
      seg = s[start_idx, len]
      next unless valid.call(seg)
      dfs.call(start_idx + len, parts + [seg])
    end
  end

  dfs.call(0, [])
  res
end
```

## Scala

```scala
object Solution {
    def restoreIpAddresses(s: String): List[String] = {
        if (s.length < 4 || s.length > 12) return Nil

        val result = scala.collection.mutable.ListBuffer.empty[String]

        def isValid(str: String): Boolean = {
            if (str.length > 1 && str.charAt(0) == '0') false
            else {
                val v = str.toInt
                v <= 255
            }
        }

        def backtrack(start: Int, parts: List[String]): Unit = {
            if (parts.size == 4) {
                if (start == s.length) {
                    result += parts.mkString(".")
                }
                return
            }

            val remainingParts = 4 - parts.size
            // prune based on remaining length
            for (len <- 1 to 3) {
                if (start + len > s.length) return
                val remainLen = s.length - (start + len)
                if (remainLen < remainingParts - 1 || remainLen > (remainingParts - 1) * 3) {
                    // not enough or too many characters left for the rest parts
                } else {
                    val segment = s.substring(start, start + len)
                    if (isValid(segment)) {
                        backtrack(start + len, parts :+ segment)
                    }
                }
            }
        }

        backtrack(0, Nil)
        result.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn restore_ip_addresses(s: String) -> Vec<String> {
        let n = s.len();
        let mut ans = Vec::new();
        if n < 4 || n > 12 {
            return ans;
        }

        let is_valid = |seg: &str| -> bool {
            if seg.is_empty() {
                return false;
            }
            if seg.len() > 1 && seg.as_bytes()[0] == b'0' {
                return false;
            }
            // seg length is at most 3 by construction
            let val: u32 = seg.parse().unwrap();
            val <= 255
        };

        for i in 1..=3 {
            if i >= n { break; }
            for j in 1..=3 {
                if i + j >= n { break; }
                for k in 1..=3 {
                    let first_three = i + j + k;
                    if first_three >= n { break; }
                    let l4 = n - first_three;
                    if l4 < 1 || l4 > 3 { continue; }

                    let a = &s[0..i];
                    let b = &s[i..i + j];
                    let c = &s[i + j..first_three];
                    let d = &s[first_three..];

                    if is_valid(a) && is_valid(b) && is_valid(c) && is_valid(d) {
                        ans.push(format!("{}.{}.{}.{}", a, b, c, d));
                    }
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (restore-ip-addresses s)
  (-> string? (listof string?))
  (let ([n (string-length s)]
        [results '()])
    (letrec
        ((valid?
           (lambda (seg)
             (let* ([len (string-length seg)])
               (and (> len 0) (<= len 3)
                    (or (not (= (string-ref seg 0) #\0)) (= len 1))
                    (let ([num (string->number seg)])
                      (and num (<= num 255)))))))
         (add-result
           (lambda (parts)
             (set! results (cons (string-join (reverse parts) ".") results))))
         (dfs
           (lambda (idx parts)
             (cond
               [(= (length parts) 4)
                (when (= idx n)
                  (add-result parts))]
               [else
                (for ([len (in-range 1 4)])
                  (let ([next (+ idx len)])
                    (when (<= next n)
                      (define seg (substring s idx next))
                      (when (valid? seg)
                        (dfs next (cons seg parts))))))]))))
      (dfs 0 '())
      (reverse results)))
```

## Erlang

```erlang
-spec restore_ip_addresses(unicode:unicode_binary()) -> [unicode:unicode_binary()].
restore_ip_addresses(S) ->
    helper(S, 0, []).

%% Recursive backtracking helper
helper(S, Start, Dots) ->
    Size = byte_size(S),
    Remaining = Size - Start,
    PartsLeft = 4 - length(Dots),
    if
        Remaining > PartsLeft * 3 orelse Remaining < PartsLeft ->
            [];
        true ->
            case PartsLeft of
                1 ->
                    Len = Remaining,
                    case valid(S, Start, Len) of
                        true -> [build_address(S, Dots ++ [Len])];
                        false -> []
                    end;
                _ ->
                    MaxLen = erlang:min(3, Remaining),
                    lists:foldl(
                      fun(Len, Acc) ->
                          case valid(S, Start, Len) of
                              true ->
                                  Acc ++ helper(S, Start + Len, Dots ++ [Len]);
                              false -> Acc
                          end
                      end,
                      [],
                      lists:seq(1, MaxLen)
                    )
            end
    end.

%% Validate a segment of length Len starting at Index
valid(S, Index, Len) ->
    Sub = binary:part(S, {Index, Len}),
    case Len of
        1 -> true;
        _ ->
            case binary:at(Sub, 0) of
                $0 -> false;
                _ ->
                    if Len < 3 -> true;
                       Len == 3 ->
                           case binary_to_integer(Sub) =< 255 of
                               true -> true;
                               false -> false
                           end
                    end
            end
    end.

%% Build the final IP address string from segment lengths
build_address(S, Lengths) ->
    {_, Iolist} =
        lists:foldl(
          fun(Len, {Pos, Acc}) ->
              Part = binary:part(S, {Pos, Len}),
              NewAcc = case Acc of
                           [] -> [Part];
                           _  -> [<<".">>, Part | Acc]
                       end,
              {Pos + Len, NewAcc}
          end,
          {0, []},
          Lengths),
    iolist_to_binary(lists:reverse(Iolist)).
```

## Elixir

```elixir
defmodule Solution do
  @spec restore_ip_addresses(s :: String.t) :: [String.t]
  def restore_ip_addresses(s) do
    if byte_size(s) > 12, do: [], else dfs(s, 0, [], [])
  end

  defp dfs(_s, start, parts, acc) when length(parts) == 4 do
    if start == byte_size(_s) do
      [Enum.join(Enum.reverse(parts), ".") | acc]
    else
      acc
    end
  end

  defp dfs(s, start, parts, acc) do
    max_len = min(3, byte_size(s) - start)

    Enum.reduce(1..max_len, acc, fn len, a ->
      segment_bin = :binary.part(s, start, len)
      segment = to_string(segment_bin)

      if valid?(segment) do
        dfs(s, start + len, [segment | parts], a)
      else
        a
      end
    end)
  end

  defp valid?(seg) do
    cond do
      byte_size(seg) > 1 and :binary.at(seg, 0) == ?0 -> false
      true ->
        case Integer.parse(seg) do
          {num, ""} when num <= 255 -> true
          _ -> false
        end
    end
  end
end
```
