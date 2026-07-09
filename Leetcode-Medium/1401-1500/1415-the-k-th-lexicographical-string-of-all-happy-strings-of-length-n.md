# 1415. The k-th Lexicographical String of All Happy Strings of Length n

## Cpp

```cpp
class Solution {
public:
    string getHappyString(int n, int k) {
        if (n <= 0) return "";
        int total = 3 * (1 << (n - 1));
        if (k > total) return "";
        
        int groupSize = 1 << (n - 1); // strings per first character
        char first;
        if (k <= groupSize) {
            first = 'a';
        } else if (k <= 2 * groupSize) {
            first = 'b';
            k -= groupSize;
        } else {
            first = 'c';
            k -= 2 * groupSize;
        }
        
        string res;
        res.push_back(first);
        for (int pos = n - 1; pos > 0; --pos) {
            int half = 1 << (pos - 1); // strings per choice at this position
            char prev = res.back();
            char small, large;
            if (prev == 'a') { small = 'b'; large = 'c'; }
            else if (prev == 'b') { small = 'a'; large = 'c'; }
            else { // prev == 'c'
                small = 'a';
                large = 'b';
            }
            if (k <= half) {
                res.push_back(small);
            } else {
                res.push_back(large);
                k -= half;
            }
        }
        return res;
    }
};
```

## Java

```java
class Solution {
    public String getHappyString(int n, int k) {
        if (n <= 0) return "";
        int total = 3 * (1 << (n - 1));
        if (k > total) return "";
        char[] res = new char[n];
        int idx = k - 1; // zero‑based index
        int groupSize = 1 << (n - 1); // strings per first character
        
        int firstGroup = idx / groupSize; // 0 -> 'a', 1 -> 'b', 2 -> 'c'
        res[0] = (char) ('a' + firstGroup);
        idx %= groupSize;
        
        for (int i = 1; i < n; i++) {
            groupSize >>= 1; // size of each subgroup at this level
            char prev = res[i - 1];
            char small, large;
            if (prev == 'a') {
                small = 'b';
                large = 'c';
            } else if (prev == 'b') {
                small = 'a';
                large = 'c';
            } else { // prev == 'c'
                small = 'a';
                large = 'b';
            }
            if (idx < groupSize) {
                res[i] = small;
            } else {
                res[i] = large;
                idx -= groupSize;
            }
        }
        return new String(res);
    }
}
```

## Python

```python
class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        total = 3 * (1 << (n - 1))
        if k > total:
            return ""
        # Determine first character
        group_size = 1 << (n - 1)  # strings per starting letter
        first_idx = (k - 1) // group_size
        start_char = ['a', 'b', 'c'][first_idx]
        result = start_char
        k = (k - 1) % group_size + 1  # position within the chosen group

        # Build remaining characters
        while len(result) < n:
            group_size //= 2  # strings per each choice at this position
            # two possible next chars in lexicographic order
            opts = [c for c in 'abc' if c != result[-1]]
            opts.sort()
            if k <= group_size:
                result += opts[0]
            else:
                result += opts[1]
                k -= group_size
        return result
```

## Python3

```python
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (1 << (n - 1))
        if k > total:
            return ""
        result = []
        prev = ''
        for i in range(n):
            options = ['a', 'b', 'c']
            if prev:
                options.remove(prev)
            cnt = 1 << (n - i - 1)  # number of strings per option at this position
            for ch in options:
                if k > cnt:
                    k -= cnt
                else:
                    result.append(ch)
                    prev = ch
                    break
        return ''.join(result)
```

## C

```c
#include <stdlib.h>
#include <string.h>

static void dfs(int n, int k, char *cur, int pos, int *cnt, char **res) {
    if (*res) return;
    if (pos == n) {
        (*cnt)++;
        if (*cnt == k) {
            *res = (char *)malloc(n + 1);
            memcpy(*res, cur, n);
            (*res)[n] = '\0';
        }
        return;
    }
    for (int i = 0; i < 3; ++i) {
        char c = 'a' + i;
        if (pos > 0 && cur[pos - 1] == c) continue;
        cur[pos] = c;
        dfs(n, k, cur, pos + 1, cnt, res);
        if (*res) return;
    }
}

char* getHappyString(int n, int k) {
    int total = 3 * (1 << (n - 1));
    if (k > total) {
        char *empty = (char *)malloc(1);
        empty[0] = '\0';
        return empty;
    }

    char cur[11]; // n <= 10
    int cnt = 0;
    char *result = NULL;

    dfs(n, k, cur, 0, &cnt, &result);

    if (!result) {
        char *empty = (char *)malloc(1);
        empty[0] = '\0';
        return empty;
    }
    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public string GetHappyString(int n, int k)
    {
        if (n <= 0) return "";
        int block = 1 << (n - 1);               // number of strings per first character
        int total = 3 * block;                  // total happy strings of length n
        if (k > total) return "";

        int kZeroBased = k - 1;
        char[] result = new char[n];
        char[] firstChars = new char[] { 'a', 'b', 'c' };
        result[0] = firstChars[kZeroBased / block];

        int idxInGroup = kZeroBased % block;    // position within the chosen first‑char group
        int curBlock = block >> 1;              // size of each sub‑group for next positions

        for (int i = 1; i < n; i++)
        {
            char prev = result[i - 1];
            char small, large;
            if (prev == 'a')
            {
                small = 'b';
                large = 'c';
            }
            else if (prev == 'b')
            {
                small = 'a';
                large = 'c';
            }
            else // prev == 'c'
            {
                small = 'a';
                large = 'b';
            }

            int sub = curBlock > 0 ? idxInGroup / curBlock : 0; // 0 -> smallest, 1 -> largest
            if (sub == 0)
            {
                result[i] = small;
            }
            else
            {
                result[i] = large;
                idxInGroup -= curBlock;
            }

            curBlock >>= 1;
        }

        return new string(result);
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var getHappyString = function(n, k) {
    const total = 3 * Math.pow(2, n - 1);
    if (k > total) return "";
    
    const groupSize = Math.pow(2, n - 1);
    let first;
    if (k <= groupSize) {
        first = 'a';
    } else if (k <= 2 * groupSize) {
        first = 'b';
        k -= groupSize;
    } else {
        first = 'c';
        k -= 2 * groupSize;
    }
    
    const nextSmallest = { a: 'b', b: 'a', c: 'a' };
    const nextGreatest = { a: 'c', b: 'c', c: 'b' };
    
    let result = [first];
    let prev = first;
    
    for (let pos = 1; pos < n; pos++) {
        const cnt = Math.pow(2, n - pos - 1);
        if (k <= cnt) {
            const ch = nextSmallest[prev];
            result.push(ch);
            prev = ch;
        } else {
            k -= cnt;
            const ch = nextGreatest[prev];
            result.push(ch);
            prev = ch;
        }
    }
    
    return result.join('');
};
```

## Typescript

```typescript
function getHappyString(n: number, k: number): string {
    const total = 3 * (1 << (n - 1));
    if (k > total) return "";
    
    const firstChars = ['a', 'b', 'c'];
    let blockSize = 1 << (n - 1); // strings per first character
    const firstIdx = Math.floor((k - 1) / blockSize);
    let result = firstChars[firstIdx];
    let prev = result;
    
    let remaining = (k - 1) % blockSize; // zero‑based index within the chosen group
    
    for (let pos = 2; pos <= n; ++pos) {
        blockSize >>= 1; // size of each subgroup at this position
        const options = prev === 'a' ? ['b', 'c']
                       : prev === 'b' ? ['a', 'c']
                       :               ['a', 'b'];
        if (remaining < blockSize) {
            result += options[0];
            prev = options[0];
        } else {
            result += options[1];
            remaining -= blockSize;
            prev = options[1];
        }
    }
    
    return result;
}
```

## Php

```php
class Solution {
    private int $target = 0;
    private int $count = 0;
    private string $answer = '';

    /**
     * @param Integer $n
     * @param Integer $k
     * @return String
     */
    function getHappyString($n, $k) {
        $this->target = $k;
        $this->dfs('', $n);
        return $this->answer;
    }

    private function dfs(string $curr, int $n): void {
        if ($this->answer !== '') {
            return;
        }
        if (strlen($curr) === $n) {
            $this->count++;
            if ($this->count === $this->target) {
                $this->answer = $curr;
            }
            return;
        }
        foreach (['a', 'b', 'c'] as $ch) {
            if ($curr !== '' && $curr[strlen($curr) - 1] === $ch) {
                continue;
            }
            $this->dfs($curr . $ch, $n);
            if ($this->answer !== '') {
                return;
            }
        }
    }
}
```

## Swift

```swift
class Solution {
    func getHappyString(_ n: Int, _ k: Int) -> String {
        let total = 3 * (1 << (n - 1))
        if k > total { return "" }
        
        var remainingK = k
        let groupSize = 1 << (n - 1)
        var result = [Character]()
        
        // Determine first character
        let firstChar: Character
        if remainingK <= groupSize {
            firstChar = "a"
        } else if remainingK <= 2 * groupSize {
            firstChar = "b"
            remainingK -= groupSize
        } else {
            firstChar = "c"
            remainingK -= 2 * groupSize
        }
        result.append(firstChar)
        
        // Build the rest of the string
        for i in 1..<n {
            let prev = result[i - 1]
            let smallest: Character
            let largest: Character
            switch prev {
            case "a":
                smallest = "b"
                largest = "c"
            case "b":
                smallest = "a"
                largest = "c"
            default: // "c"
                smallest = "a"
                largest = "b"
            }
            
            let remainingPositions = n - i - 1
            let subSize = 1 << remainingPositions
            if remainingK <= subSize {
                result.append(smallest)
            } else {
                result.append(largest)
                remainingK -= subSize
            }
        }
        
        return String(result)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getHappyString(n: Int, k: Int): String {
        if (n <= 0) return ""
        val total = 3 * (1 shl (n - 1))
        if (k > total) return ""

        var kk = k
        val sb = StringBuilder()
        val groupSize = 1 shl (n - 1)

        when {
            kk <= groupSize -> sb.append('a')
            kk <= 2 * groupSize -> {
                sb.append('b')
                kk -= groupSize
            }
            else -> {
                sb.append('c')
                kk -= 2 * groupSize
            }
        }

        var remaining = n - 1
        while (remaining > 0) {
            val prev = sb[sb.length - 1]
            val subGroup = 1 shl (remaining - 1)
            if (kk <= subGroup) {
                val nextChar = when (prev) {
                    'a' -> 'b'
                    'b' -> 'a'
                    else -> 'a' // prev == 'c'
                }
                sb.append(nextChar)
            } else {
                kk -= subGroup
                val nextChar = when (prev) {
                    'a' -> 'c'
                    'b' -> 'c'
                    else -> 'b' // prev == 'c'
                }
                sb.append(nextChar)
            }
            remaining--
        }

        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String getHappyString(int n, int k) {
    int total = 3 * (1 << (n - 1));
    if (k > total) return "";
    String answer = "";
    int count = 0;

    void dfs(String cur) {
      if (answer.isNotEmpty) return;
      if (cur.length == n) {
        count++;
        if (count == k) answer = cur;
        return;
      }
      for (var ch in ['a', 'b', 'c']) {
        if (cur.isNotEmpty && cur[cur.length - 1] == ch) continue;
        dfs(cur + ch);
        if (answer.isNotEmpty) return;
      }
    }

    dfs("");
    return answer;
  }
}
```

## Golang

```go
func getHappyString(n int, k int) string {
	if n <= 0 {
		return ""
	}
	total := 3 * (1 << (n - 1))
	if k > total {
		return ""
	}

	groupSize := 1 << (n - 1)
	var first byte
	if k <= groupSize {
		first = 'a'
	} else if k <= 2*groupSize {
		first = 'b'
		k -= groupSize
	} else {
		first = 'c'
		k -= 2 * groupSize
	}

	res := make([]byte, n)
	res[0] = first

	nextSmallest := map[byte]byte{'a': 'b', 'b': 'a', 'c': 'a'}
	nextGreatest := map[byte]byte{'a': 'c', 'b': 'c', 'c': 'b'}

	for i := 1; i < n; i++ {
		prev := res[i-1]
		remaining := n - i - 1
		mid := 1 << remaining // size of each subgroup
		if k <= mid {
			res[i] = nextSmallest[prev]
		} else {
			res[i] = nextGreatest[prev]
			k -= mid
		}
	}
	return string(res)
}
```

## Ruby

```ruby
def get_happy_string(n, k)
  total = 3 * (1 << (n - 1))
  return "" if k > total

  group = 1 << (n - 1)
  result = ""

  if k <= group
    result << 'a'
    offset = 0
  elsif k <= 2 * group
    result << 'b'
    offset = group
  else
    result << 'c'
    offset = 2 * group
  end

  k -= offset

  smallest = { 'a' => 'b', 'b' => 'a', 'c' => 'a' }
  greatest = { 'a' => 'c', 'b' => 'c', 'c' => 'b' }

  (1...n).each do |i|
    subgroup = 1 << (n - i - 1)
    prev = result[-1]
    if k <= subgroup
      result << smallest[prev]
    else
      result << greatest[prev]
      k -= subgroup
    end
  end

  result
end
```

## Scala

```scala
object Solution {
    def getHappyString(n: Int, k: Int): String = {
        var count = 0
        var result = ""
        val sb = new StringBuilder()

        def dfs(): Unit = {
            if (result.nonEmpty) return
            if (sb.length == n) {
                count += 1
                if (count == k) result = sb.toString()
                return
            }
            for (ch <- Array('a', 'b', 'c')) {
                if (sb.isEmpty || sb.charAt(sb.length - 1) != ch) {
                    sb.append(ch)
                    dfs()
                    sb.deleteCharAt(sb.length - 1)
                    if (result.nonEmpty) return
                }
            }
        }

        dfs()
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_happy_string(n: i32, k: i32) -> String {
        let n = n as usize;
        let mut k = k as usize;

        // total number of happy strings of length n
        let total = 3usize * (1usize << (n - 1));
        if k > total {
            return "".to_string();
        }

        // size of each first‑character block
        let block = 1usize << (n - 1);
        let mut result = String::with_capacity(n);
        let mut prev: char;

        // determine the first character and adjust k to be 1‑based within its block
        if k <= block {
            prev = 'a';
        } else if k <= 2 * block {
            prev = 'b';
            k -= block;
        } else {
            prev = 'c';
            k -= 2 * block;
        }
        result.push(prev);

        // build the remaining characters
        for pos in 1..n {
            let rem = n - pos - 1;               // positions left after this one
            let half = 1usize << rem;            // strings per choice at this level

            let (smallest, largest) = match prev {
                'a' => ('b', 'c'),
                'b' => ('a', 'c'),
                'c' => ('a', 'b'),
                _ => unreachable!(),
            };

            if k <= half {
                result.push(smallest);
                prev = smallest;
            } else {
                result.push(largest);
                k -= half;
                prev = largest;
            }
        }

        result
    }
}
```

## Racket

```racket
(define/contract (get-happy-string n k)
  (-> exact-integer? exact-integer? string?)
  (let* ((total (* 3 (expt 2 (- n 1)))))
    (if (> k total)
        ""
        (let* ((group-size (expt 2 (- n 1)))
               (first-char
                 (cond [(<= k group-size) #\a]
                       [(<= k (* 2 group-size)) #\b]
                       [else #\c]))
               (k1 (cond [(<= k group-size) k]
                         [(<= k (* 2 group-size)) (- k group-size)]
                         [else (- k (* 2 group-size))])))
          (define result (make-string n))
          (string-set! result 0 first-char)
          (let loop ((idx 1)               ; next position (0‑based)
                     (prev first-char)
                     (kcur k1))
            (if (= idx n)
                result
                (let* ((mid (expt 2 (- n idx 1)))   ; size of each subgroup for this position
                       (next-char
                         (if (<= kcur mid)
                             (cond [(char=? prev #\a) #\b]
                                   [(char=? prev #\b) #\a]
                                   [else #\a])
                             (cond [(char=? prev #\a) #\c]
                                   [(char=? prev #\b) #\c]
                                   [else #\b]))))
                  (string-set! result idx next-char)
                  (if (<= kcur mid)
                      (loop (+ idx 1) next-char kcur)
                      (loop (+ idx 1) next-char (- kcur mid)))))))))))
```

## Erlang

```erlang
-module(solution).
-export([get_happy_string/2]).

-spec get_happy_string(N :: integer(), K :: integer()) -> unicode:unicode_binary().
get_happy_string(N, K) ->
    Total = 3 * (1 bsl (N - 1)),
    if
        K > Total -> <<>>;
        true ->
            Group = 1 bsl (N - 1),
            {FirstChar, NewK} =
                case K of
                    _ when K =< Group -> {$a, K};
                    _ when K =< 2 * Group -> {$b, K - Group};
                    _ -> {$c, K - 2 * Group}
                end,
            add(N - 1, NewK, FirstChar, [FirstChar])
    end.

add(0, _K, _Prev, Acc) ->
    list_to_binary(lists:reverse(Acc));
add(Remaining, K, Prev, Acc) when Remaining > 0 ->
    Mid = 1 bsl (Remaining - 1),
    {NextChar, NewK} =
        case Prev of
            $a ->
                if K =< Mid -> {$b, K};
                   true -> {$c, K - Mid}
                end;
            $b ->
                if K =< Mid -> {$a, K};
                   true -> {$c, K - Mid}
                end;
            $c ->
                if K =< Mid -> {$a, K};
                   true -> {$b, K - Mid}
                end
        end,
    add(Remaining - 1, NewK, NextChar, [NextChar | Acc]).
```

## Elixir

```elixir
defmodule Solution do
  @spec get_happy_string(n :: integer, k :: integer) :: String.t()
  def get_happy_string(n, k) do
    total = 3 * (1 <<< (n - 1))

    if k > total do
      ""
    else
      group = 1 <<< (n - 1)

      {first_char, k_rem} =
        cond do
          k <= group -> {?a, k}
          k <= 2 * group -> {?b, k - group}
          true -> {?c, k - 2 * group}
        end

      smallest = %{
        ?a => ?b,
        ?b => ?a,
        ?c => ?a
      }

      greatest = %{
        ?a => ?c,
        ?b => ?c,
        ?c => ?b
      }

      {chars, _prev, _k_final} =
        Enum.reduce(2..n, {[first_char], first_char, k_rem}, fn i, {list, prev, cur_k} ->
          rem = n - i
          mid = 1 <<< rem

          if cur_k <= mid do
            ch = Map.get(smallest, prev)
            {list ++ [ch], ch, cur_k}
          else
            ch = Map.get(greatest, prev)
            {list ++ [ch], ch, cur_k - mid}
          end
        end)

      List.to_string(chars)
    end
  end
end
```
