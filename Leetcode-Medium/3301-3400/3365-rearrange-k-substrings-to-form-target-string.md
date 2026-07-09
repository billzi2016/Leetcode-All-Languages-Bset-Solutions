# 3365. Rearrange K Substrings to Form Target String

## Cpp

```cpp
class Solution {
public:
    bool isPossibleToRearrange(string s, string t, int k) {
        int n = s.size();
        int block = n / k;
        unordered_map<string, int> cnt;
        cnt.reserve(k * 2);
        for (int i = 0; i < n; i += block) {
            ++cnt[s.substr(i, block)];
        }
        for (int i = 0; i < n; i += block) {
            auto it = cnt.find(t.substr(i, block));
            if (it == cnt.end() || it->second == 0) return false;
            --it->second;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean isPossibleToRearrange(String s, String t, int k) {
        int n = s.length();
        int len = n / k;
        java.util.HashMap<String, Integer> count = new java.util.HashMap<>();
        for (int i = 0; i < n; i += len) {
            String sub = s.substring(i, i + len);
            count.put(sub, count.getOrDefault(sub, 0) + 1);
        }
        for (int i = 0; i < n; i += len) {
            String sub = t.substring(i, i + len);
            Integer c = count.get(sub);
            if (c == null || c == 0) {
                return false;
            }
            if (c == 1) {
                count.remove(sub);
            } else {
                count.put(sub, c - 1);
            }
        }
        return count.isEmpty();
    }
}
```

## Python

```python
class Solution(object):
    def isPossibleToRearrange(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: bool
        """
        n = len(s)
        block_len = n // k
        # Build frequency map for blocks of s
        from collections import Counter
        cnt_s = Counter()
        for i in range(0, n, block_len):
            cnt_s[s[i:i+block_len]] += 1
        cnt_t = Counter()
        for i in range(0, n, block_len):
            cnt_t[t[i:i+block_len]] += 1
        return cnt_s == cnt_t
```

## Python3

```python
class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        block_len = n // k
        from collections import Counter

        cnt_s = Counter()
        for i in range(0, n, block_len):
            cnt_s[s[i:i + block_len]] += 1

        cnt_t = Counter()
        for i in range(0, n, block_len):
            cnt_t[t[i:i + block_len]] += 1

        return cnt_s == cnt_t
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static const char *g_str;
static int g_len;

static int cmp_offsets(const void *a, const void *b) {
    int i = *(const int *)a;
    int j = *(const int *)b;
    return memcmp(g_str + i, g_str + j, g_len);
}

bool isPossibleToRearrange(char* s, char* t, int k) {
    size_t n = strlen(s);
    if (n != strlen(t) || n % k != 0) return false;

    int blockLen = (int)(n / k);

    int *offS = (int *)malloc(k * sizeof(int));
    int *offT = (int *)malloc(k * sizeof(int));
    if (!offS || !offT) {
        free(offS);
        free(offT);
        return false;
    }

    for (int i = 0; i < k; ++i) {
        offS[i] = i * blockLen;
        offT[i] = i * blockLen;
    }

    g_str = s;
    g_len = blockLen;
    qsort(offS, k, sizeof(int), cmp_offsets);

    g_str = t;
    g_len = blockLen;
    qsort(offT, k, sizeof(int), cmp_offsets);

    bool possible = true;
    for (int i = 0; i < k; ++i) {
        if (memcmp(s + offS[i], t + offT[i], blockLen) != 0) {
            possible = false;
            break;
        }
    }

    free(offS);
    free(offT);
    return possible;
}
```

## Csharp

```csharp
public class Solution {
    public bool IsPossibleToRearrange(string s, string t, int k) {
        int n = s.Length;
        int blockLen = n / k;

        var dict = new Dictionary<string, int>(k);
        for (int i = 0; i < n; i += blockLen) {
            string sub = s.Substring(i, blockLen);
            if (dict.TryGetValue(sub, out int cnt)) {
                dict[sub] = cnt + 1;
            } else {
                dict[sub] = 1;
            }
        }

        for (int i = 0; i < n; i += blockLen) {
            string sub = t.Substring(i, blockLen);
            if (!dict.TryGetValue(sub, out int cnt) || cnt == 0) {
                return false;
            }
            dict[sub] = cnt - 1;
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
 * @param {number} k
 * @return {boolean}
 */
var isPossibleToRearrange = function(s, t, k) {
    const n = s.length;
    const blockSize = n / k;
    const freq = new Map();

    for (let i = 0; i < n; i += blockSize) {
        const sub = s.slice(i, i + blockSize);
        freq.set(sub, (freq.get(sub) || 0) + 1);
    }

    for (let i = 0; i < n; i += blockSize) {
        const sub = t.slice(i, i + blockSize);
        const cnt = freq.get(sub);
        if (!cnt) return false;
        if (cnt === 1) freq.delete(sub);
        else freq.set(sub, cnt - 1);
    }

    return true;
};
```

## Typescript

```typescript
function isPossibleToRearrange(s: string, t: string, k: number): boolean {
    const n = s.length;
    const blockSize = n / k;
    const countMap = new Map<string, number>();

    for (let i = 0; i < n; i += blockSize) {
        const sub = s.slice(i, i + blockSize);
        countMap.set(sub, (countMap.get(sub) ?? 0) + 1);
    }

    for (let i = 0; i < n; i += blockSize) {
        const sub = t.slice(i, i + blockSize);
        const cnt = countMap.get(sub);
        if (!cnt) return false;
        if (cnt === 1) countMap.delete(sub);
        else countMap.set(sub, cnt - 1);
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
     * @param Integer $k
     * @return Boolean
     */
    function isPossibleToRearrange($s, $t, $k) {
        $n = strlen($s);
        $len = intdiv($n, $k); // length of each substring

        $freq = [];

        for ($i = 0; $i < $n; $i += $len) {
            $sub = substr($s, $i, $len);
            if (isset($freq[$sub])) {
                $freq[$sub]++;
            } else {
                $freq[$sub] = 1;
            }
        }

        for ($i = 0; $i < $n; $i += $len) {
            $sub = substr($t, $i, $len);
            if (!isset($freq[$sub]) || $freq[$sub] == 0) {
                return false;
            }
            $freq[$sub]--;
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func isPossibleToRearrange(_ s: String, _ t: String, _ k: Int) -> Bool {
        let n = s.count
        let blockLen = n / k
        
        var freq = [Substring: Int]()
        var startIdx = s.startIndex
        for _ in 0..<k {
            let endIdx = s.index(startIdx, offsetBy: blockLen)
            let sub = s[startIdx..<endIdx]
            freq[sub, default: 0] += 1
            startIdx = endIdx
        }
        
        var tStartIdx = t.startIndex
        for _ in 0..<k {
            let tEndIdx = t.index(tStartIdx, offsetBy: blockLen)
            let sub = t[tStartIdx..<tEndIdx]
            if let cnt = freq[sub] {
                if cnt == 1 {
                    freq.removeValue(forKey: sub)
                } else {
                    freq[sub] = cnt - 1
                }
            } else {
                return false
            }
            tStartIdx = tEndIdx
        }
        
        return freq.isEmpty
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun isPossibleToRearrange(s: String, t: String, k: Int): Boolean {
        val n = s.length
        if (n != t.length) return false
        val blockSize = n / k
        val countMap = HashMap<String, Int>()
        var i = 0
        while (i < n) {
            val sub = s.substring(i, i + blockSize)
            countMap[sub] = (countMap[sub] ?: 0) + 1
            i += blockSize
        }
        i = 0
        while (i < n) {
            val sub = t.substring(i, i + blockSize)
            val cnt = countMap[sub] ?: return false
            if (cnt == 1) {
                countMap.remove(sub)
            } else {
                countMap[sub] = cnt - 1
            }
            i += blockSize
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool isPossibleToRearrange(String s, String t, int k) {
    int n = s.length;
    int blockSize = n ~/ k;

    // Count substrings from s
    final Map<String, int> freq = {};
    for (int i = 0; i < k; ++i) {
      String sub = s.substring(i * blockSize, (i + 1) * blockSize);
      freq[sub] = (freq[sub] ?? 0) + 1;
    }

    // Match substrings from t
    for (int i = 0; i < k; ++i) {
      String sub = t.substring(i * blockSize, (i + 1) * blockSize);
      int? cnt = freq[sub];
      if (cnt == null || cnt == 0) return false;
      if (cnt == 1) {
        freq.remove(sub);
      } else {
        freq[sub] = cnt - 1;
      }
    }

    return true;
  }
}
```

## Golang

```go
func isPossibleToRearrange(s string, t string, k int) bool {
	n := len(s)
	if n != len(t) || n%k != 0 {
		return false
	}
	blockSize := n / k
	counts := make(map[string]int, k)

	for i := 0; i < k; i++ {
		sub := s[i*blockSize : (i+1)*blockSize]
		counts[sub]++
	}

	for i := 0; i < k; i++ {
		sub := t[i*blockSize : (i+1)*blockSize]
		if c, ok := counts[sub]; !ok || c == 0 {
			return false
		}
		counts[sub] = c - 1
	}

	return true
}
```

## Ruby

```ruby
def is_possible_to_rearrange(s, t, k)
  n = s.length
  l = n / k
  freq = Hash.new(0)

  i = 0
  while i < n
    sub = s[i, l]
    freq[sub] += 1
    i += l
  end

  j = 0
  while j < n
    sub = t[j, l]
    cnt = freq[sub]
    return false if cnt == 0
    freq[sub] = cnt - 1
    j += l
  end

  true
end
```

## Scala

```scala
object Solution {
    def isPossibleToRearrange(s: String, t: String, k: Int): Boolean = {
        val n = s.length
        val len = n / k
        import scala.collection.mutable

        val freq = mutable.HashMap[String, Int]()

        var i = 0
        while (i < k) {
            val sub = s.substring(i * len, (i + 1) * len)
            freq.put(sub, freq.getOrElse(sub, 0) + 1)
            i += 1
        }

        i = 0
        while (i < k) {
            val sub = t.substring(i * len, (i + 1) * len)
            freq.get(sub) match {
                case Some(cnt) if cnt > 1 => freq.put(sub, cnt - 1)
                case Some(1)             => freq.remove(sub)
                case _                   => return false
            }
            i += 1
        }

        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn is_possible_to_rearrange(s: String, t: String, k: i32) -> bool {
        let len = s.len();
        if len == 0 {
            return true;
        }
        let k_usize = k as usize;
        let block_len = len / k_usize;

        let bytes_s = s.as_bytes();
        let bytes_t = t.as_bytes();

        use std::collections::HashMap;
        let mut cnt: HashMap<Vec<u8>, i32> = HashMap::new();

        for i in 0..k_usize {
            let start = i * block_len;
            let block = bytes_s[start..start + block_len].to_vec();
            *cnt.entry(block).or_insert(0) += 1;
        }

        for i in 0..k_usize {
            let start = i * block_len;
            let block = bytes_t[start..start + block_len].to_vec();
            match cnt.get_mut(&block) {
                Some(v) => {
                    *v -= 1;
                }
                None => return false,
            }
        }

        for v in cnt.values() {
            if *v != 0 {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
(define/contract (is-possible-to-rearrange s t k)
  (-> string? string? exact-integer? boolean?)
  (let* ((n (string-length s))
         (len (/ n k)))
    (let loop-s ((i 0) (cnt (make-hash))) ; count substrings from s
      (if (= i n)
          (let loop-t ((j 0) (cnt cnt))
            (if (= j n)
                #t
                (let* ((sub (substring t j (+ j len)))
                       (c   (hash-ref cnt sub #f)))
                  (cond
                    [(not c) #f]
                    [(= c 1) (hash-remove! cnt sub) (loop-t (+ j len) cnt)]
                    [else    (hash-set! cnt sub (- c 1)) (loop-t (+ j len) cnt)]))))
          (let* ((sub (substring s i (+ i len)))
                 (c   (hash-ref cnt sub 0)))
            (hash-set! cnt sub (+ c 1))
            (loop-s (+ i len) cnt))))))
```

## Erlang

```erlang
-module(solution).
-export([is_possible_to_rearrange/3]).

-spec is_possible_to_rearrange(S :: unicode:unicode_binary(), T :: unicode:unicode_binary(), K :: integer()) -> boolean().
is_possible_to_rearrange(S, T, K) ->
    Len = byte_size(S),
    BlockSize = Len div K,
    MapS = build_map(S, BlockSize, K, 0, #{}),
    check_t(T, BlockSize, K, 0, MapS).

build_map(_Bin, _BlockSize, 0, _Idx, Map) ->
    Map;
build_map(Bin, BlockSize, Count, Idx, Map) ->
    Pos = Idx * BlockSize,
    Sub = binary:part(Bin, {Pos, BlockSize}),
    NewMap = maps:update_with(Sub, fun(C) -> C + 1 end, 1, Map),
    build_map(Bin, BlockSize, Count - 1, Idx + 1, NewMap).

check_t(_Bin, _BlockSize, 0, _Idx, _Map) ->
    true;
check_t(Bin, BlockSize, Count, Idx, Map) ->
    Pos = Idx * BlockSize,
    Sub = binary:part(Bin, {Pos, BlockSize}),
    case maps:get(Sub, Map, undefined) of
        undefined -> false;
        0 -> false;
        C ->
            NewMap = maps:put(Sub, C - 1, Map),
            check_t(Bin, BlockSize, Count - 1, Idx + 1, NewMap)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec is_possible_to_rearrange(s :: String.t(), t :: String.t(), k :: integer) :: boolean()
  def is_possible_to_rearrange(s, t, k) do
    n = byte_size(s)
    block_len = div(n, k)

    freq =
      Enum.reduce(0..(k - 1), %{}, fn i, acc ->
        start = i * block_len
        sub = :binary.part(s, start, block_len)
        Map.update(acc, sub, 1, &(&1 + 1))
      end)

    case Enum.reduce_while(0..(k - 1), freq, fn i, map ->
           start = i * block_len
           sub = :binary.part(t, start, block_len)

           case Map.get(map, sub) do
             nil -> {:halt, false}
             1 -> {:cont, Map.delete(map, sub)}
             cnt when cnt > 1 -> {:cont, Map.put(map, sub, cnt - 1)}
           end
         end) do
      false -> false
      _ -> true
    end
  end
end
```
