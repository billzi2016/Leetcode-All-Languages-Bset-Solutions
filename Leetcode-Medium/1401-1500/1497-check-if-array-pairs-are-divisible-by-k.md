# 1497. Check If Array Pairs Are Divisible by k

## Cpp

```cpp
class Solution {
public:
    bool canArrange(vector<int>& arr, int k) {
        vector<int> cnt(k, 0);
        for (int x : arr) {
            int r = ((x % k) + k) % k;
            ++cnt[r];
        }
        if (cnt[0] % 2 != 0) return false;
        if (k % 2 == 0 && cnt[k / 2] % 2 != 0) return false;
        int limit = k / 2;
        for (int i = 1; i <= limit; ++i) {
            if (i == k - i) continue; // already handled when k even
            if (cnt[i] != cnt[k - i]) return false;
        }
        return true;
    }
};
```

## Java

```java
class Solution {
    public boolean canArrange(int[] arr, int k) {
        int[] freq = new int[k];
        for (int num : arr) {
            int mod = ((num % k) + k) % k;
            freq[mod]++;
        }
        // remainder 0 must pair among themselves
        if ((freq[0] & 1) == 1) return false;
        // handle remainders i and k-i
        for (int i = 1; i <= k / 2; i++) {
            int opposite = k - i;
            if (i == opposite) { // when k is even and i == k/2
                if ((freq[i] & 1) == 1) return false;
            } else {
                if (freq[i] != freq[opposite]) return false;
            }
        }
        return true;
    }
}
```

## Python

```python
class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        freq = [0] * k
        for x in arr:
            freq[x % k] += 1

        if freq[0] % 2 != 0:
            return False

        half = k // 2
        for i in range(1, half + 1):
            if i == k - i:  # when k is even and i == k/2
                if freq[i] % 2 != 0:
                    return False
            else:
                if freq[i] != freq[k - i]:
                    return False

        return True
```

## Python3

```python
from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [0] * k
        for num in arr:
            freq[num % k] += 1

        # remainder 0 must pair among themselves
        if freq[0] % 2 != 0:
            return False

        # handle remainders i and k-i
        limit = k // 2
        for i in range(1, limit + 1):
            j = k - i
            if i == j:  # when k is even and i == k/2
                if freq[i] % 2 != 0:
                    return False
            else:
                if freq[i] != freq[j]:
                    return False

        return True
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

bool canArrange(int* arr, int arrSize, int k) {
    if (arrSize % 2 != 0) return false;
    int *freq = calloc((size_t)k, sizeof(int));
    for (int i = 0; i < arrSize; ++i) {
        long long val = arr[i];
        int rem = (int)(((val % k) + k) % k);
        freq[rem]++;
    }
    bool ok = true;
    if (freq[0] % 2 != 0) ok = false;
    if (ok && k % 2 == 0) {
        if (freq[k / 2] % 2 != 0) ok = false;
    }
    for (int i = 1; i < k && ok; ++i) {
        int j = k - i;
        if (i >= j) break;
        if (freq[i] != freq[j]) {
            ok = false;
            break;
        }
    }
    free(freq);
    return ok;
}
```

## Csharp

```csharp
public class Solution
{
    public bool CanArrange(int[] arr, int k)
    {
        int[] freq = new int[k];
        foreach (int num in arr)
        {
            int rem = ((num % k) + k) % k;
            freq[rem]++;
        }

        // Remainder 0 must appear an even number of times
        if (freq[0] % 2 != 0) return false;

        // If k is even, remainder k/2 must also appear an even number of times
        if (k % 2 == 0 && freq[k / 2] % 2 != 0) return false;

        int limit = k / 2;
        for (int i = 1; i <= limit; i++)
        {
            // Skip the middle case when k is even (already handled)
            if (k % 2 == 0 && i == k - i) continue;
            if (freq[i] != freq[k - i]) return false;
        }

        return true;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @param {number} k
 * @return {boolean}
 */
var canArrange = function(arr, k) {
    const freq = new Array(k).fill(0);
    for (let num of arr) {
        const mod = ((num % k) + k) % k;
        freq[mod]++;
    }
    // remainder 0 must pair among themselves
    if (freq[0] % 2 !== 0) return false;
    // handle each remainder
    for (let i = 1; i < k; i++) {
        const complement = k - i;
        if (i === complement) { // i == k/2 when k even
            if (freq[i] % 2 !== 0) return false;
        } else if (i < complement) {
            if (freq[i] !== freq[complement]) return false;
        }
    }
    return true;
};
```

## Typescript

```typescript
function canArrange(arr: number[], k: number): boolean {
    const freq = new Array(k).fill(0);
    for (const num of arr) {
        const rem = ((num % k) + k) % k;
        freq[rem]++;
    }
    // Remainder 0 must appear an even number of times
    if (freq[0] % 2 !== 0) return false;
    // If k is even, remainder k/2 must also appear an even number of times
    if (k % 2 === 0 && freq[k / 2] % 2 !== 0) return false;

    const half = Math.floor(k / 2);
    for (let i = 1; i <= half; i++) {
        if (i === k - i) continue; // already handled when k is even
        if (freq[i] !== freq[k - i]) return false;
    }
    return true;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Boolean
     */
    function canArrange($arr, $k) {
        // Frequency array for remainders 0..k-1
        $freq = array_fill(0, $k, 0);
        foreach ($arr as $num) {
            $rem = ($num % $k + $k) % $k; // handle negative numbers
            $freq[$rem]++;
        }

        for ($i = 0; $i < $k; $i++) {
            if ($i == 0) {
                if ($freq[0] % 2 != 0) {
                    return false;
                }
            } elseif (2 * $i == $k) { // when k is even and i == k/2
                if ($freq[$i] % 2 != 0) {
                    return false;
                }
            } else {
                if ($freq[$i] != $freq[$k - $i]) {
                    return false;
                }
            }
        }

        return true;
    }
}
```

## Swift

```swift
class Solution {
    func canArrange(_ arr: [Int], _ k: Int) -> Bool {
        var freq = Array(repeating: 0, count: k)
        for num in arr {
            let mod = ((num % k) + k) % k
            freq[mod] += 1
        }
        // Remainder 0 must appear even number of times
        if freq[0] % 2 != 0 { return false }
        var i = 1
        while i < k {
            let complement = k - i
            if i == complement { // when k is even and remainder equals k/2
                if freq[i] % 2 != 0 { return false }
            } else {
                if freq[i] != freq[complement] { return false }
            }
            i += 1
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun canArrange(arr: IntArray, k: Int): Boolean {
        val freq = IntArray(k)
        for (num in arr) {
            var rem = num % k
            if (rem < 0) rem += k
            freq[rem]++
        }
        // remainder 0 must appear even number of times
        if (freq[0] % 2 != 0) return false

        val half = k / 2
        if (k % 2 == 0) {
            // for even k, remainder k/2 must also be even
            if (freq[half] % 2 != 0) return false
            // check pairs for remainders i and k-i where i < k/2
            for (i in 1 until half) {
                if (freq[i] != freq[k - i]) return false
            }
        } else {
            // for odd k, check all i from 1 to floor(k/2)
            for (i in 1..half) {
                if (freq[i] != freq[k - i]) return false
            }
        }
        return true
    }
}
```

## Dart

```dart
class Solution {
  bool canArrange(List<int> arr, int k) {
    List<int> freq = List.filled(k, 0);
    for (int x in arr) {
      int rem = ((x % k) + k) % k;
      freq[rem]++;
    }
    if (freq[0] % 2 != 0) return false;
    for (int i = 1; i < k; ++i) {
      int j = k - i;
      if (i > j) break;
      if (i == j) {
        if (freq[i] % 2 != 0) return false;
      } else {
        if (freq[i] != freq[j]) return false;
      }
    }
    return true;
  }
}
```

## Golang

```go
func canArrange(arr []int, k int) bool {
	if len(arr)%2 != 0 {
		return false
	}
	freq := make([]int, k)
	for _, v := range arr {
		mod := ((v % k) + k) % k
		freq[mod]++
	}
	if freq[0]%2 != 0 {
		return false
	}
	if k%2 == 0 && freq[k/2]%2 != 0 {
		return false
	}
	for r := 1; r < k; r++ {
		if r == k-r { // handles the case when k is even and r == k/2, already checked
			continue
		}
		if freq[r] != freq[k-r] {
			return false
		}
	}
	return true
}
```

## Ruby

```ruby
def can_arrange(arr, k)
  freq = Array.new(k, 0)
  arr.each { |x| freq[x % k] += 1 }

  (0...k).each do |i|
    if i == 0
      return false if freq[i].odd?
    elsif i * 2 == k
      return false if freq[i].odd?
    else
      return false unless freq[i] == freq[k - i]
    end
  end

  true
end
```

## Scala

```scala
object Solution {
    def canArrange(arr: Array[Int], k: Int): Boolean = {
        val freq = new Array[Int](k)
        for (x <- arr) {
            var r = x % k
            if (r < 0) r += k
            freq(r) += 1
        }
        // remainder 0 must appear even times
        if ((freq(0) & 1) == 1) return false
        // if k is even, remainder k/2 must also appear even times
        if (k % 2 == 0 && (freq(k / 2) & 1) == 1) return false

        var i = 1
        val limit = k / 2
        while (i < limit) {
            if (freq(i) != freq(k - i)) return false
            i += 1
        }
        true
    }
}
```

## Rust

```rust
impl Solution {
    pub fn can_arrange(arr: Vec<i32>, k: i32) -> bool {
        let k_usize = k as usize;
        if k_usize == 0 {
            return false;
        }
        let mut freq = vec![0usize; k_usize];
        for &x in &arr {
            // ((x % k) + k) % k ensures non‑negative remainder
            let rem = ((x % k + k) % k) as usize;
            freq[rem] += 1;
        }
        // Remainder 0 must appear an even number of times
        if freq[0] % 2 != 0 {
            return false;
        }
        for r in 1..k_usize {
            let complement = (k_usize - r) % k_usize;
            if r == complement {
                // This happens when k is even and r == k/2
                if freq[r] % 2 != 0 {
                    return false;
                }
            } else if freq[r] != freq[complement] {
                return false;
            }
        }
        true
    }
}
```

## Racket

```racket
#lang racket
(require racket/contract)

(define/contract (can-arrange arr k)
  (-> (listof exact-integer?) exact-integer? boolean?)
  (let* ([freq (make-vector k 0)])
    ;; count remainders
    (for ([x (in-list arr)])
      (let ([rem (modulo x k)])
        (vector-set! freq rem (+ 1 (vector-ref freq rem)))))
    (define possible #t)
    ;; remainder 0 must appear even times
    (when (odd? (vector-ref freq 0))
      (set! possible #f))
    ;; check other remainders
    (for ([i (in-range 1 k)] #:break (not possible))
      (let* ([j (- k i)])
        (cond
          [(= i j) ; when k is even and i == k/2
           (when (odd? (vector-ref freq i))
             (set! possible #f))]
          [(< i j)
           (when (not (= (vector-ref freq i) (vector-ref freq j)))
             (set! possible #f))])))
    possible))
```

## Erlang

```erlang
-spec can_arrange(Arr :: [integer()], K :: integer()) -> boolean().
can_arrange(Arr, K) ->
    Counts = build_counts(Arr, K, #{}),
    check_counts(0, K, Counts).

build_counts([], _, M) -> M;
build_counts([X|Xs], K, M) ->
    R = ((X rem K) + K) rem K,
    NewM = case maps:is_key(R, M) of
        true -> maps:put(R, maps:get(R, M) + 1, M);
        false -> maps:put(R, 1, M)
    end,
    build_counts(Xs, K, NewM).

check_counts(I, K, Counts) when I >= K ->
    true;
check_counts(I, K, Counts) ->
    case I of
        0 ->
            C = maps:get(0, Counts, 0),
            if C rem 2 =:= 0 -> check_counts(I+1, K, Counts);
               true -> false
            end;
        _ when (K rem 2 =:= 0) andalso I == K div 2 ->
            C = maps:get(I, Counts, 0),
            if C rem 2 =:= 0 -> check_counts(I+1, K, Counts);
               true -> false
            end;
        _ ->
            C = maps:get(I, Counts, 0),
            D = maps:get(K - I, Counts, 0),
            if C =:= D -> check_counts(I+1, K, Counts);
               true -> false
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec can_arrange(arr :: [integer], k :: integer) :: boolean
  def can_arrange(arr, k) do
    freq =
      Enum.reduce(arr, %{}, fn x, acc ->
        r = Integer.mod(x, k)
        Map.update(acc, r, 1, &(&1 + 1))
      end)

    0..(k - 1)
    |> Enum.all?(fn i ->
      cond do
        i == 0 ->
          rem(Map.get(freq, 0, 0), 2) == 0

        k - i == i ->
          rem(Map.get(freq, i, 0), 2) == 0

        true ->
          cnt_i = Map.get(freq, i, 0)
          cnt_j = Map.get(freq, k - i, 0)
          cnt_i == cnt_j
      end
    end)
  end
end
```
