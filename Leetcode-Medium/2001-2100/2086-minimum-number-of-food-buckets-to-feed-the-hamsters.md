# 2086. Minimum Number of Food Buckets to Feed the Hamsters

## Cpp

```cpp
class Solution {
public:
    int minimumBuckets(string hamsters) {
        int n = hamsters.size();
        vector<bool> bucket(n, false);
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            if (hamsters[i] != 'H') continue;
            // already fed by left bucket?
            if (i > 0 && bucket[i - 1]) continue;
            // try to place bucket on the right
            if (i + 1 < n && hamsters[i + 1] == '.' && !bucket[i + 1]) {
                bucket[i + 1] = true;
                ++ans;
            }
            // otherwise, place bucket on the left
            else if (i > 0 && hamsters[i - 1] == '.' && !bucket[i - 1]) {
                bucket[i - 1] = true;
                ++ans;
            } else {
                return -1; // impossible to feed this hamster
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minimumBuckets(String hamsters) {
        char[] arr = hamsters.toCharArray();
        int n = arr.length;
        int buckets = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] != 'H') continue;
            // Check if already fed by an existing bucket
            boolean fed = false;
            if (i - 1 >= 0 && arr[i - 1] == 'B') fed = true;
            if (i + 1 < n && arr[i + 1] == 'B') fed = true;
            if (fed) continue;
            // Prefer placing bucket to the right
            if (i + 1 < n && arr[i + 1] == '.') {
                arr[i + 1] = 'B';
                buckets++;
            } else if (i - 1 >= 0 && arr[i - 1] == '.') {
                arr[i - 1] = 'B';
                buckets++;
            } else {
                return -1;
            }
        }
        return buckets;
    }
}
```

## Python

```python
class Solution(object):
    def minimumBuckets(self, hamsters):
        """
        :type hamsters: str
        :rtype: int
        """
        n = len(hamsters)
        placed = [False] * n  # bucket placements
        ans = 0
        i = 0
        while i < n:
            if hamsters[i] == 'H':
                # already fed by a left bucket?
                if i > 0 and placed[i - 1]:
                    i += 1
                    continue
                # try to place bucket on the right
                if i + 1 < n and hamsters[i + 1] == '.':
                    placed[i + 1] = True
                    ans += 1
                    i += 2  # skip the bucket position
                # otherwise, place on the left if possible
                elif i - 1 >= 0 and hamsters[i - 1] == '.' and not placed[i - 1]:
                    placed[i - 1] = True
                    ans += 1
                    i += 1
                else:
                    return -1
            else:
                i += 1
        return ans
```

## Python3

```python
class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        s = list(hamsters)
        n = len(s)
        ans = 0
        i = 0
        while i < n:
            if s[i] == 'H':
                # already fed by a bucket on the left
                if i > 0 and s[i - 1] == 'B':
                    i += 1
                    continue
                # try to place bucket on the right
                if i + 1 < n and s[i + 1] == '.':
                    s[i + 1] = 'B'
                    ans += 1
                # otherwise place on the left if possible
                elif i - 1 >= 0 and s[i - 1] == '.':
                    s[i - 1] = 'B'
                    ans += 1
                else:
                    return -1
            i += 1
        return ans
```

## C

```c
#include <string.h>
#include <stdlib.h>

int minimumBuckets(char* hamsters) {
    int n = strlen(hamsters);
    char *bucket = (char *)calloc(n, sizeof(char));
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        if (hamsters[i] != 'H') continue;
        // already fed by left bucket?
        if (i > 0 && bucket[i - 1]) continue;
        // try to place at i+1
        if (i + 1 < n && hamsters[i + 1] == '.' && !bucket[i + 1]) {
            bucket[i + 1] = 1;
            ++ans;
        } else if (i - 1 >= 0 && hamsters[i - 1] == '.' && !bucket[i - 1]) {
            bucket[i - 1] = 1;
            ++ans;
        } else {
            free(bucket);
            return -1;
        }
    }
    free(bucket);
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumBuckets(string hamsters) {
        int n = hamsters.Length;
        bool[] bucket = new bool[n];
        char[] s = hamsters.ToCharArray();
        int ans = 0;

        for (int i = 0; i < n; i++) {
            if (s[i] != 'H') continue;

            // Already fed by a bucket on the left
            if (i > 0 && bucket[i - 1]) continue;

            // Try to place a bucket on the right
            if (i + 1 < n && s[i + 1] == '.' && !bucket[i + 1]) {
                bucket[i + 1] = true;
                ans++;
            }
            // Otherwise, try left side
            else if (i > 0 && s[i - 1] == '.' && !bucket[i - 1]) {
                bucket[i - 1] = true;
                ans++;
            } 
            else {
                return -1; // impossible to feed this hamster
            }
        }

        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} hamsters
 * @return {number}
 */
var minimumBuckets = function(hamsters) {
    const n = hamsters.length;
    const bucket = new Array(n).fill(false);
    let ans = 0;
    for (let i = 0; i < n; ++i) {
        if (hamsters[i] !== 'H') continue;
        // already fed by an existing bucket
        if ((i > 0 && bucket[i - 1]) || (i + 1 < n && bucket[i + 1])) continue;
        // try to place a bucket at i+1 first
        if (i + 1 < n && hamsters[i + 1] === '.' && !bucket[i + 1]) {
            bucket[i + 1] = true;
            ++ans;
        } else if (i - 1 >= 0 && hamsters[i - 1] === '.' && !bucket[i - 1]) {
            bucket[i - 1] = true;
            ++ans;
        } else {
            return -1;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function minimumBuckets(hamsters: string): number {
    const n = hamsters.length;
    const bucket = new Array<boolean>(n).fill(false);
    let ans = 0;
    for (let i = 0; i < n; i++) {
        if (hamsters[i] !== 'H') continue;
        // Already fed by a bucket on the left
        if (i > 0 && bucket[i - 1]) continue;
        // Try to place bucket on the right
        if (i + 1 < n && hamsters[i + 1] === '.' && !bucket[i + 1]) {
            bucket[i + 1] = true;
            ans++;
        } else if (i - 1 >= 0 && hamsters[i - 1] === '.' && !bucket[i - 1]) {
            // Otherwise place on the left
            bucket[i - 1] = true;
            ans++;
        } else {
            return -1; // impossible to feed this hamster
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $hamsters
     * @return Integer
     */
    function minimumBuckets($hamsters) {
        $n = strlen($hamsters);
        $s = str_split($hamsters);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === 'H') {
                // already fed by a bucket on the left
                if ($i > 0 && $s[$i - 1] === 'B') {
                    continue;
                }
                // try to place bucket on the right
                if ($i + 1 < $n && $s[$i + 1] === '.') {
                    $ans++;
                    $s[$i + 1] = 'B';
                } elseif ($i - 1 >= 0 && $s[$i - 1] === '.') { // otherwise on the left
                    $ans++;
                    $s[$i - 1] = 'B';
                } else {
                    return -1; // impossible to feed this hamster
                }
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func minimumBuckets(_ hamsters: String) -> Int {
        let chars = Array(hamsters)
        let n = chars.count
        var bucket = [Bool](repeating: false, count: n)
        var i = 0
        var ans = 0
        
        while i < n {
            if chars[i] == "H" {
                // Already fed by a bucket on the left?
                if i > 0 && bucket[i - 1] {
                    i += 1
                    continue
                }
                
                // Prefer placing bucket to the right
                if i + 1 < n && chars[i + 1] == "." {
                    ans += 1
                    bucket[i + 1] = true
                    i += 2   // skip current hamster and the spot where we placed the bucket
                } else if i - 1 >= 0 && chars[i - 1] == "." {
                    // Otherwise place to the left
                    ans += 1
                    bucket[i - 1] = true
                    i += 1
                } else {
                    return -1   // impossible to feed this hamster
                }
            } else {
                i += 1
            }
        }
        
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumBuckets(hamsters: String): Int {
        val n = hamsters.length
        val placed = BooleanArray(n)
        var ans = 0
        var i = 0
        while (i < n) {
            if (hamsters[i] == 'H') {
                // Already fed by a bucket on the left?
                if (i > 0 && placed[i - 1]) {
                    i++
                    continue
                }
                // Prefer placing a bucket to the right.
                if (i + 1 < n && hamsters[i + 1] == '.' && !placed[i + 1]) {
                    placed[i + 1] = true
                    ans++
                    i += 2   // skip the bucket position
                } else if (i - 1 >= 0 && hamsters[i - 1] == '.' && !placed[i - 1]) {
                    placed[i - 1] = true
                    ans++
                    i++      // move to next index
                } else {
                    return -1
                }
            } else {
                i++
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  int minimumBuckets(String hamsters) {
    List<String> arr = hamsters.split('');
    int n = arr.length;
    int ans = 0;

    for (int i = 0; i < n; i++) {
      if (arr[i] == 'H') {
        bool fed = false;
        if (i - 1 >= 0 && arr[i - 1] == 'B') fed = true;
        if (i + 1 < n && arr[i + 1] == 'B') fed = true;
        if (fed) continue;

        if (i + 1 < n && arr[i + 1] == '.') {
          arr[i + 1] = 'B';
          ans++;
        } else if (i - 1 >= 0 && arr[i - 1] == '.') {
          arr[i - 1] = 'B';
          ans++;
        } else {
          return -1;
        }
      }
    }

    return ans;
  }
}
```

## Golang

```go
func minimumBuckets(hamsters string) int {
	n := len(hamsters)
	used := make([]bool, n)
	buckets := 0

	for i := 0; i < n; i++ {
		if hamsters[i] != 'H' {
			continue
		}
		// already fed by a bucket on the left
		if i > 0 && used[i-1] {
			continue
		}
		// try to place bucket on the right
		if i+1 < n && hamsters[i+1] == '.' && !used[i+1] {
			used[i+1] = true
			buckets++
		} else if i-1 >= 0 && hamsters[i-1] == '.' && !used[i-1] { // otherwise on the left
			used[i-1] = true
			buckets++
		} else {
			return -1
		}
	}
	return buckets
}
```

## Ruby

```ruby
def minimum_buckets(hamsters)
  s = hamsters.chars
  n = s.length
  buckets = 0
  i = 0
  while i < n
    if s[i] == 'H'
      if i > 0 && s[i - 1] == 'B'
        # already fed by left bucket
      else
        if i + 1 < n && s[i + 1] == '.'
          s[i + 1] = 'B'
          buckets += 1
        elsif i - 1 >= 0 && s[i - 1] == '.'
          s[i - 1] = 'B'
          buckets += 1
        else
          return -1
        end
      end
    end
    i += 1
  end
  buckets
end
```

## Scala

```scala
object Solution {
    def minimumBuckets(hamsters: String): Int = {
        val n = hamsters.length
        val placed = new Array[Boolean](n)
        var buckets = 0
        var i = 0
        while (i < n) {
            if (hamsters(i) == 'H') {
                // already fed by a bucket on the left?
                if (i > 0 && placed(i - 1)) {
                    // nothing to do
                } else {
                    // try to place at i+1 first
                    if (i + 1 < n && hamsters(i + 1) == '.' && !placed(i + 1)) {
                        placed(i + 1) = true
                        buckets += 1
                    } else if (i - 1 >= 0 && hamsters(i - 1) == '.' && !placed(i - 1)) {
                        placed(i - 1) = true
                        buckets += 1
                    } else {
                        return -1
                    }
                }
            }
            i += 1
        }
        buckets
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_buckets(hamsters: String) -> i32 {
        let bytes = hamsters.as_bytes();
        let n = bytes.len();
        let mut placed = vec![false; n];
        let mut ans: i32 = 0;
        for i in 0..n {
            if bytes[i] == b'H' {
                // Check if already fed by an existing bucket
                let fed = (i > 0 && placed[i - 1]) || (i + 1 < n && placed[i + 1]);
                if fed {
                    continue;
                }
                // Prefer placing a bucket to the right
                if i + 1 < n && bytes[i + 1] == b'.' && !placed[i + 1] {
                    placed[i + 1] = true;
                    ans += 1;
                } else if i > 0 && bytes[i - 1] == b'.' && !placed[i - 1] {
                    placed[i - 1] = true;
                    ans += 1;
                } else {
                    return -1;
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define/contract (minimum-buckets hamsters)
  (-> string? exact-integer?)
  (let* ((v (string->vector hamsters))
         (n (vector-length v)))
    (let loop ((i 0) (cnt 0))
      (cond
        [(>= i n) cnt]
        [(char=? (vector-ref v i) #\H)
         (if (and (> i 0) (char=? (vector-ref v (- i 1)) #\B))
             (loop (+ i 1) cnt)
             (cond
               [(and (< i (- n 1)) (char=? (vector-ref v (+ i 1)) #\.))
                (vector-set! v (+ i 1) #\B)
                (loop (+ i 1) (+ cnt 1))]
               [(and (> i 0) (char=? (vector-ref v (- i 1)) #\.))
                (vector-set! v (- i 1) #\B)
                (loop (+ i 1) (+ cnt 1))]
               [else -1]))]
        [else (loop (+ i 1) cnt)]))))
```

## Erlang

```erlang
-spec minimum_buckets(Hamsters :: unicode:unicode_binary()) -> integer().
minimum_buckets(Hamsters) ->
    Len = byte_size(Hamsters),
    loop(0, Len, Hamsters, #{}).

loop(I, Len, _Ham, Buckets) when I >= Len ->
    maps:size(Buckets);
loop(I, Len, Ham, Buckets) ->
    Char = binary:at(Ham, I),
    case Char of
        $H ->
            LeftFed = (I > 0) andalso maps:is_key(I - 1, Buckets),
            if
                LeftFed ->
                    loop(I + 1, Len, Ham, Buckets);
                true ->
                    RightIdx = I + 1,
                    RightOk = RightIdx < Len andalso binary:at(Ham, RightIdx) == $.,
                    case RightOk andalso not maps:is_key(RightIdx, Buckets) of
                        true ->
                            NewBuckets = maps:put(RightIdx, true, Buckets),
                            loop(I + 1, Len, Ham, NewBuckets);
                        false ->
                            LeftIdx = I - 1,
                            LeftOk = LeftIdx >= 0 andalso binary:at(Ham, LeftIdx) == $.,
                            case LeftOk andalso not maps:is_key(LeftIdx, Buckets) of
                                true ->
                                    NewBuckets2 = maps:put(LeftIdx, true, Buckets),
                                    loop(I + 1, Len, Ham, NewBuckets2);
                                false -> -1
                            end
                    end
            end;
        $. ->
            loop(I + 1, Len, Ham, Buckets)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_buckets(hamsters :: String.t) :: integer
  def minimum_buckets(hamsters) do
    chars = :binary.bin_to_list(hamsters) |> List.to_tuple()
    len = tuple_size(chars)

    {possible, buckets} =
      Enum.reduce_while(0..len - 1, {true, MapSet.new()}, fn i, {_ok, set} ->
        case elem(chars, i) do
          ?H ->
            cond do
              # already fed by a bucket on the left
              i > 0 and MapSet.member?(set, i - 1) ->
                {:cont, {true, set}}

              # try to place bucket on the right
              i + 1 < len and elem(chars, i + 1) == ?. and not MapSet.member?(set, i + 1) ->
                {:cont, {true, MapSet.put(set, i + 1)}}

              # try to place bucket on the left
              i > 0 and elem(chars, i - 1) == ?. and not MapSet.member?(set, i - 1) ->
                {:cont, {true, MapSet.put(set, i - 1)}}

              # cannot feed this hamster
              true ->
                {:halt, {false, set}}
            end

          _ ->
            {:cont, {true, set}}
        end
      end)

    if possible, do: MapSet.size(buckets), else: -1
  end
end
```
