# 0899. Orderly Queue

## Cpp

```cpp
class Solution {
public:
    string orderlyQueue(string s, int k) {
        if (k == 1) {
            string best = s;
            int n = s.size();
            for (int i = 1; i < n; ++i) {
                string cand = s.substr(i) + s.substr(0, i);
                if (cand < best) best = cand;
            }
            return best;
        } else {
            sort(s.begin(), s.end());
            return s;
        }
    }
};
```

## Java

```java
class Solution {
    public String orderlyQueue(String s, int k) {
        if (k == 1) {
            String best = s;
            int n = s.length();
            for (int i = 1; i < n; i++) {
                String rot = s.substring(i) + s.substring(0, i);
                if (rot.compareTo(best) < 0) {
                    best = rot;
                }
            }
            return best;
        } else {
            char[] chars = s.toCharArray();
            java.util.Arrays.sort(chars);
            return new String(chars);
        }
    }
}
```

## Python

```python
class Solution(object):
    def orderlyQueue(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 1:
            best = s
            n = len(s)
            for i in range(1, n):
                rot = s[i:] + s[:i]
                if rot < best:
                    best = rot
            return best
        else:
            return ''.join(sorted(s))
```

## Python3

```python
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            best = s
            n = len(s)
            for i in range(1, n):
                cand = s[i:] + s[:i]
                if cand < best:
                    best = cand
            return best
        else:
            return ''.join(sorted(s))
```

## C

```c
#include <stdlib.h>
#include <string.h>

char* orderlyQueue(char* s, int k) {
    int n = strlen(s);
    if (k == 1) {
        // Find minimal rotation
        char *t = (char*)malloc(2 * n + 1);
        memcpy(t, s, n);
        memcpy(t + n, s, n);
        t[2 * n] = '\0';
        
        char *best = (char*)malloc(n + 1);
        memcpy(best, s, n);
        best[n] = '\0';
        
        for (int i = 1; i < n; ++i) {
            int cmp = strncmp(t + i, best, n);
            if (cmp < 0) {
                memcpy(best, t + i, n);
                best[n] = '\0';
            }
        }
        free(t);
        return best;
    } else {
        // Sort characters
        int cnt[26] = {0};
        for (int i = 0; i < n; ++i) cnt[s[i] - 'a']++;
        
        char *res = (char*)malloc(n + 1);
        int pos = 0;
        for (int c = 0; c < 26; ++c) {
            while (cnt[c]--) {
                res[pos++] = (char)('a' + c);
            }
        }
        res[n] = '\0';
        return res;
    }
}
```

## Csharp

```csharp
public class Solution {
    public string OrderlyQueue(string s, int k) {
        if (k == 1) {
            int n = s.Length;
            string best = s;
            for (int i = 1; i < n; i++) {
                string rotated = s.Substring(i) + s.Substring(0, i);
                if (string.Compare(rotated, best, StringComparison.Ordinal) < 0) {
                    best = rotated;
                }
            }
            return best;
        } else {
            char[] chars = s.ToCharArray();
            Array.Sort(chars);
            return new string(chars);
        }
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
var orderlyQueue = function(s, k) {
    if (k === 1) {
        let best = s;
        const n = s.length;
        for (let i = 1; i < n; ++i) {
            const rot = s.slice(i) + s.slice(0, i);
            if (rot < best) best = rot;
        }
        return best;
    } else {
        return s.split('').sort().join('');
    }
};
```

## Typescript

```typescript
function orderlyQueue(s: string, k: number): string {
    if (k === 1) {
        let best = s;
        const n = s.length;
        for (let i = 1; i < n; ++i) {
            const rot = s.slice(i) + s.slice(0, i);
            if (rot < best) best = rot;
        }
        return best;
    } else {
        return s.split('').sort().join('');
    }
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
    function orderlyQueue($s, $k) {
        if ($k == 1) {
            $n = strlen($s);
            $best = $s;
            for ($i = 1; $i < $n; $i++) {
                $candidate = substr($s, $i) . substr($s, 0, $i);
                if (strcmp($candidate, $best) < 0) {
                    $best = $candidate;
                }
            }
            return $best;
        } else {
            $chars = str_split($s);
            sort($chars);
            return implode('', $chars);
        }
    }
}
```

## Swift

```swift
class Solution {
    func orderlyQueue(_ s: String, _ k: Int) -> String {
        if k == 1 {
            let chars = Array(s)
            let n = chars.count
            var best = s
            for i in 1..<n {
                let rotated = String(chars[i...]) + String(chars[0..<i])
                if rotated < best {
                    best = rotated
                }
            }
            return best
        } else {
            return String(s.sorted())
        }
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun orderlyQueue(s: String, k: Int): String {
        return if (k == 1) {
            var best = s
            val n = s.length
            for (i in 1 until n) {
                val candidate = s.substring(i) + s.substring(0, i)
                if (candidate < best) best = candidate
            }
            best
        } else {
            s.toCharArray().sorted().joinToString("")
        }
    }
}
```

## Dart

```dart
class Solution {
  String orderlyQueue(String s, int k) {
    if (k == 1) {
      String best = s;
      int n = s.length;
      for (int i = 1; i < n; ++i) {
        String candidate = s.substring(i) + s.substring(0, i);
        if (candidate.compareTo(best) < 0) {
          best = candidate;
        }
      }
      return best;
    } else {
      List<String> chars = s.split('');
      chars.sort();
      return chars.join();
    }
  }
}
```

## Golang

```go
import "sort"

func orderlyQueue(s string, k int) string {
	if k == 1 {
		n := len(s)
		best := s
		for i := 1; i < n; i++ {
			rot := s[i:] + s[:i]
			if rot < best {
				best = rot
			}
		}
		return best
	}
	b := []byte(s)
	sort.Slice(b, func(i, j int) bool { return b[i] < b[j] })
	return string(b)
}
```

## Ruby

```ruby
def orderly_queue(s, k)
  if k == 1
    best = s
    n = s.length
    (1...n).each do |i|
      rot = s[i..-1] + s[0...i]
      best = rot if rot < best
    end
    best
  else
    s.chars.sort.join
  end
end
```

## Scala

```scala
object Solution {
    def orderlyQueue(s: String, k: Int): String = {
        if (k == 1) {
            val n = s.length
            var best = s
            for (i <- 1 until n) {
                val cand = s.substring(i) + s.substring(0, i)
                if (cand < best) best = cand
            }
            best
        } else {
            s.toCharArray.sorted.mkString
        }
    }
}
```

## Rust

```rust
impl Solution {
    pub fn orderly_queue(s: String, k: i32) -> String {
        if k == 1 {
            let n = s.len();
            let bytes = s.as_bytes();
            let mut best = 0usize;
            for i in 1..n {
                for j in 0..n {
                    let a = bytes[(i + j) % n];
                    let b = bytes[(best + j) % n];
                    if a < b {
                        best = i;
                        break;
                    } else if a > b {
                        break;
                    }
                }
            }
            let mut res = String::with_capacity(n);
            for i in 0..n {
                res.push(bytes[(best + i) % n] as char);
            }
            res
        } else {
            let mut chars: Vec<char> = s.chars().collect();
            chars.sort_unstable();
            chars.iter().collect()
        }
    }
}
```

## Racket

```racket
(define/contract (orderly-queue s k)
  (-> string? exact-integer? string?)
  (if (= k 1)
      (let* ((n (string-length s))
             (min s))
        (for ([i (in-range 1 n)])
          (let ((rot (string-append (substring s i) (substring s 0 i))))
            (when (string<? rot min)
              (set! min rot))))
        min)
      (list->string (sort (string->list s) char<?))))
```

## Erlang

```erlang
-module(solution).
-export([orderly_queue/2]).

-spec orderly_queue(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
orderly_queue(S, K) when K >= 2 ->
    Sorted = lists:sort(binary_to_list(S)),
    list_to_binary(Sorted);
orderly_queue(S, 1) ->
    Len = byte_size(S),
    find_min_rotation(S, Len, S, 1).

find_min_rotation(_S, Len, Min, I) when I >= Len ->
    Min;
find_min_rotation(S, Len, Min, I) ->
    Prefix = binary:part(S, 0, I),
    Suffix = binary:part(S, I, Len - I),
    Rot = <<Suffix/binary, Prefix/binary>>,
    NewMin = if Rot < Min -> Rot; true -> Min end,
    find_min_rotation(S, Len, NewMin, I + 1).
```

## Elixir

```elixir
defmodule Solution do
  @spec orderly_queue(String.t(), integer()) :: String.t()
  def orderly_queue(s, k) when k == 1 do
    len = String.length(s)

    0..(len - 1)
    |> Enum.map(fn i ->
      suffix = String.slice(s, i, len - i)
      prefix = String.slice(s, 0, i)
      suffix <> prefix
    end)
    |> Enum.min()
  end

  def orderly_queue(s, k) when k >= 2 do
    s
    |> String.graphemes()
    |> Enum.sort()
    |> Enum.join()
  end
end
```
