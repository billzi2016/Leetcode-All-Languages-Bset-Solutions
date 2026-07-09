# 2053. Kth Distinct String in an Array

## Cpp

```cpp
class Solution {
public:
    std::string kthDistinct(std::vector<std::string>& arr, int k) {
        std::unordered_map<std::string, int> freq;
        for (const auto& s : arr) ++freq[s];
        for (const auto& s : arr) {
            if (freq[s] == 1) {
                --k;
                if (k == 0) return s;
            }
        }
        return "";
    }
};
```

## Java

```java
class Solution {
    public String kthDistinct(String[] arr, int k) {
        java.util.Map<String, Integer> freq = new java.util.HashMap<>();
        for (String s : arr) {
            freq.put(s, freq.getOrDefault(s, 0) + 1);
        }
        for (String s : arr) {
            if (freq.get(s) == 1) {
                k--;
                if (k == 0) {
                    return s;
                }
            }
        }
        return "";
    }
}
```

## Python

```python
class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        freq = {}
        for s in arr:
            freq[s] = freq.get(s, 0) + 1

        for s in arr:
            if freq[s] == 1:
                k -= 1
                if k == 0:
                    return s
        return ""
```

## Python3

```python
class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        freq = {}
        for s in arr:
            freq[s] = freq.get(s, 0) + 1
        for s in arr:
            if freq[s] == 1:
                k -= 1
                if k == 0:
                    return s
        return ""
```

## C

```c
#include <string.h>

char* kthDistinct(char** arr, int arrSize, int k) {
    for (int i = 0; i < arrSize; ++i) {
        int cnt = 0;
        for (int j = 0; j < arrSize; ++j) {
            if (strcmp(arr[i], arr[j]) == 0) {
                ++cnt;
            }
        }
        if (cnt == 1) {
            --k;
            if (k == 0) {
                return arr[i];
            }
        }
    }
    return "";
}
```

## Csharp

```csharp
public class Solution {
    public string KthDistinct(string[] arr, int k) {
        var freq = new Dictionary<string, int>();
        foreach (var s in arr) {
            if (freq.ContainsKey(s)) freq[s]++;
            else freq[s] = 1;
        }
        foreach (var s in arr) {
            if (freq[s] == 1) {
                k--;
                if (k == 0) return s;
            }
        }
        return "";
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} arr
 * @param {number} k
 * @return {string}
 */
var kthDistinct = function(arr, k) {
    const freq = new Map();
    for (const s of arr) {
        freq.set(s, (freq.get(s) || 0) + 1);
    }
    for (const s of arr) {
        if (freq.get(s) === 1) {
            k--;
            if (k === 0) return s;
        }
    }
    return "";
};
```

## Typescript

```typescript
function kthDistinct(arr: string[], k: number): string {
    const freq = new Map<string, number>();
    for (const s of arr) {
        freq.set(s, (freq.get(s) ?? 0) + 1);
    }
    for (const s of arr) {
        if ((freq.get(s) ?? 0) === 1) {
            k--;
            if (k === 0) return s;
        }
    }
    return "";
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $arr
     * @param Integer $k
     * @return String
     */
    function kthDistinct($arr, $k) {
        $freq = [];
        foreach ($arr as $s) {
            if (isset($freq[$s])) {
                $freq[$s]++;
            } else {
                $freq[$s] = 1;
            }
        }

        foreach ($arr as $s) {
            if ($freq[$s] === 1) {
                $k--;
                if ($k === 0) {
                    return $s;
                }
            }
        }

        return "";
    }
}
```

## Swift

```swift
class Solution {
    func kthDistinct(_ arr: [String], _ k: Int) -> String {
        var frequency = [String: Int]()
        for s in arr {
            frequency[s, default: 0] += 1
        }
        var seen = 0
        for s in arr {
            if frequency[s] == 1 {
                seen += 1
                if seen == k {
                    return s
                }
            }
        }
        return ""
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun kthDistinct(arr: Array<String>, k: Int): String {
        val freq = HashMap<String, Int>()
        for (s in arr) {
            freq[s] = (freq[s] ?: 0) + 1
        }
        var seen = 0
        for (s in arr) {
            if (freq[s] == 1) {
                seen++
                if (seen == k) return s
            }
        }
        return ""
    }
}
```

## Dart

```dart
class Solution {
  String kthDistinct(List<String> arr, int k) {
    final Map<String, int> freq = {};
    for (var s in arr) {
      freq[s] = (freq[s] ?? 0) + 1;
    }
    for (var s in arr) {
      if (freq[s] == 1) {
        k--;
        if (k == 0) return s;
      }
    }
    return "";
  }
}
```

## Golang

```go
func kthDistinct(arr []string, k int) string {
	freq := make(map[string]int)
	for _, s := range arr {
		freq[s]++
	}
	for _, s := range arr {
		if freq[s] == 1 {
			k--
			if k == 0 {
				return s
			}
		}
	}
	return ""
}
```

## Ruby

```ruby
def kth_distinct(arr, k)
  freq = Hash.new(0)
  arr.each { |s| freq[s] += 1 }
  arr.each do |s|
    if freq[s] == 1
      k -= 1
      return s if k == 0
    end
  end
  ""
end
```

## Scala

```scala
object Solution {
    def kthDistinct(arr: Array[String], k: Int): String = {
        val freq = scala.collection.mutable.Map[String, Int]().withDefaultValue(0)
        for (s <- arr) {
            freq(s) += 1
        }
        var remaining = k
        for (s <- arr) {
            if (freq(s) == 1) {
                remaining -= 1
                if (remaining == 0) return s
            }
        }
        ""
    }
}
```

## Rust

```rust
impl Solution {
    pub fn kth_distinct(arr: Vec<String>, k: i32) -> String {
        use std::collections::HashMap;
        let mut freq: HashMap<String, usize> = HashMap::new();
        for s in &arr {
            *freq.entry(s.clone()).or_insert(0) += 1;
        }
        let mut remaining = k;
        for s in arr {
            if let Some(&1) = freq.get(&s) {
                remaining -= 1;
                if remaining == 0 {
                    return s;
                }
            }
        }
        String::new()
    }
}
```

## Racket

```racket
(define/contract (kth-distinct arr k)
  (-> (listof string?) exact-integer? string?)
  (let ([freq (make-hash)])
    ;; Count frequencies
    (for ([s arr])
      (hash-set! freq s (+ 1 (hash-ref freq s 0))))
    ;; Find kth distinct
    (let loop ((lst arr) (remaining k))
      (cond
        [(null? lst) ""]
        [else
         (define s (car lst))
         (if (= (hash-ref freq s) 1)
             (if (= remaining 1)
                 s
                 (loop (cdr lst) (- remaining 1)))
             (loop (cdr lst) remaining))]))))
```

## Erlang

```erlang
-spec kth_distinct(Arr :: [unicode:unicode_binary()], K :: integer()) -> unicode:unicode_binary().
kth_distinct(Arr, K) ->
    Freq = lists:foldl(
        fun(S, M) ->
            case maps:find(S, M) of
                {ok, C} -> maps:put(S, C + 1, M);
                error   -> maps:put(S, 1, M)
            end
        end,
        #{},
        Arr),
    find_kth(Arr, Freq, K).

find_kth([], _Freq, _K) ->
    <<>>;
find_kth([H|T], Freq, K) ->
    case maps:get(H, Freq) of
        1 ->
            if K =:= 1 -> H;
               true   -> find_kth(T, Freq, K - 1)
            end;
        _ -> find_kth(T, Freq, K)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec kth_distinct(arr :: [String.t()], k :: integer) :: String.t()
  def kth_distinct(arr, k) do
    freq = Enum.reduce(arr, %{}, fn s, acc ->
      Map.update(acc, s, 1, &(&1 + 1))
    end)

    find_kth(arr, freq, k)
  end

  defp find_kth([], _freq, _k), do: ""

  defp find_kth([head | tail], freq, k) do
    if Map.get(freq, head) == 1 do
      if k == 1, do: head, else: find_kth(tail, freq, k - 1)
    else
      find_kth(tail, freq, k)
    end
  end
end
```
