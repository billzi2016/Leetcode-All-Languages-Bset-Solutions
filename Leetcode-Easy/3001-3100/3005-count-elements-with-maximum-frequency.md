# 3005. Count Elements With Maximum Frequency

## Cpp

```cpp
class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        unordered_map<int, int> freq;
        for (int num : nums) ++freq[num];
        int maxFreq = 0;
        for (const auto& p : freq) maxFreq = max(maxFreq, p.second);
        int total = 0;
        for (const auto& p : freq) if (p.second == maxFreq) total += p.second;
        return total;
    }
};
```

## Java

```java
class Solution {
    public int maxFrequencyElements(int[] nums) {
        int[] freq = new int[101]; // values are between 1 and 100 inclusive
        int maxFreq = 0;
        for (int num : nums) {
            freq[num]++;
            if (freq[num] > maxFreq) {
                maxFreq = freq[num];
            }
        }
        int total = 0;
        for (int i = 1; i <= 100; i++) {
            if (freq[i] == maxFreq) {
                total += freq[i];
            }
        }
        return total;
    }
}
```

## Python

```python
class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        max_freq = 0
        for num in nums:
            cnt = freq.get(num, 0) + 1
            freq[num] = cnt
            if cnt > max_freq:
                max_freq = cnt
        total = 0
        for cnt in freq.values():
            if cnt == max_freq:
                total += cnt
        return total
```

## Python3

```python
class Solution:
    def maxFrequencyElements(self, nums):
        freq = {}
        max_freq = 0
        for num in nums:
            cnt = freq.get(num, 0) + 1
            freq[num] = cnt
            if cnt > max_freq:
                max_freq = cnt
        total = 0
        for cnt in freq.values():
            if cnt == max_freq:
                total += cnt
        return total
```

## C

```c
#include <stdio.h>

int maxFrequencyElements(int* nums, int numsSize) {
    int freq[101] = {0};
    for (int i = 0; i < numsSize; ++i) {
        int val = nums[i];
        if (val >= 1 && val <= 100) {
            ++freq[val];
        }
    }
    int maxFreq = 0;
    for (int v = 1; v <= 100; ++v) {
        if (freq[v] > maxFreq) {
            maxFreq = freq[v];
        }
    }
    int total = 0;
    for (int v = 1; v <= 100; ++v) {
        if (freq[v] == maxFreq) {
            total += freq[v];
        }
    }
    return total;
}
```

## Csharp

```csharp
public class Solution {
    public int MaxFrequencyElements(int[] nums) {
        var freq = new Dictionary<int, int>();
        foreach (var num in nums) {
            if (freq.ContainsKey(num))
                freq[num]++;
            else
                freq[num] = 1;
        }

        int maxFreq = 0;
        foreach (var kvp in freq) {
            if (kvp.Value > maxFreq)
                maxFreq = kvp.Value;
        }

        int total = 0;
        foreach (var kvp in freq) {
            if (kvp.Value == maxFreq)
                total += kvp.Value;
        }

        return total;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxFrequencyElements = function(nums) {
    const freq = new Map();
    for (const num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }
    let maxFreq = 0;
    for (const count of freq.values()) {
        if (count > maxFreq) maxFreq = count;
    }
    let total = 0;
    for (const count of freq.values()) {
        if (count === maxFreq) total += count;
    }
    return total;
};
```

## Typescript

```typescript
function maxFrequencyElements(nums: number[]): number {
    const freq = new Map<number, number>();
    for (const num of nums) {
        freq.set(num, (freq.get(num) ?? 0) + 1);
    }
    let maxFreq = 0;
    for (const count of freq.values()) {
        if (count > maxFreq) maxFreq = count;
    }
    let total = 0;
    for (const count of freq.values()) {
        if (count === maxFreq) total += count;
    }
    return total;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxFrequencyElements($nums) {
        $counts = [];
        $maxFreq = 0;
        $total = 0;
        foreach ($nums as $num) {
            if (!isset($counts[$num])) {
                $counts[$num] = 1;
            } else {
                $counts[$num]++;
            }
            $cur = $counts[$num];
            if ($cur > $maxFreq) {
                $maxFreq = $cur;
                $total = $cur;
            } elseif ($cur == $maxFreq) {
                $total += $cur;
            }
        }
        return $total;
    }
}
```

## Swift

```swift
class Solution {
    func maxFrequencyElements(_ nums: [Int]) -> Int {
        var freqMap = [Int: Int]()
        var maxFreq = 0
        var total = 0
        
        for num in nums {
            let newCount = (freqMap[num] ?? 0) + 1
            freqMap[num] = newCount
            
            if newCount > maxFreq {
                maxFreq = newCount
                total = newCount
            } else if newCount == maxFreq {
                total += newCount
            }
        }
        
        return total
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun maxFrequencyElements(nums: IntArray): Int {
        val freq = HashMap<Int, Int>()
        var maxFreq = 0
        for (num in nums) {
            val count = (freq[num] ?: 0) + 1
            freq[num] = count
            if (count > maxFreq) {
                maxFreq = count
            }
        }
        var total = 0
        for (cnt in freq.values) {
            if (cnt == maxFreq) {
                total += cnt
            }
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int maxFrequencyElements(List<int> nums) {
    final Map<int, int> freq = {};
    int maxFreq = 0;
    for (var num in nums) {
      int f = (freq[num] ?? 0) + 1;
      freq[num] = f;
      if (f > maxFreq) {
        maxFreq = f;
      }
    }
    int total = 0;
    for (var count in freq.values) {
      if (count == maxFreq) {
        total += count;
      }
    }
    return total;
  }
}
```

## Golang

```go
func maxFrequencyElements(nums []int) int {
	freq := make(map[int]int)
	maxFreq := 0
	for _, v := range nums {
		freq[v]++
		if freq[v] > maxFreq {
			maxFreq = freq[v]
		}
	}
	total := 0
	for _, f := range freq {
		if f == maxFreq {
			total += f
		}
	}
	return total
}
```

## Ruby

```ruby
def max_frequency_elements(nums)
  freq = Hash.new(0)
  nums.each { |num| freq[num] += 1 }
  max_freq = freq.values.max
  total = 0
  freq.each_value do |count|
    total += count if count == max_freq
  end
  total
end
```

## Scala

```scala
object Solution {
    def maxFrequencyElements(nums: Array[Int]): Int = {
        import scala.collection.mutable
        val freq = mutable.Map.empty[Int, Int]
        var maxFreq = 0
        var total = 0
        for (num <- nums) {
            val cnt = freq.getOrElse(num, 0) + 1
            freq.update(num, cnt)
            if (cnt > maxFreq) {
                maxFreq = cnt
                total = cnt
            } else if (cnt == maxFreq) {
                total += cnt
            }
        }
        total
    }
}
```

## Rust

```rust
impl Solution {
    pub fn max_frequency_elements(nums: Vec<i32>) -> i32 {
        let mut freq = vec![0usize; 101];
        for &v in nums.iter() {
            freq[v as usize] += 1;
        }
        let max_freq = *freq.iter().max().unwrap();
        freq.iter()
            .filter(|&&c| c == max_freq)
            .map(|&c| c as i32)
            .sum()
    }
}
```

## Racket

```racket
(define/contract (max-frequency-elements nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ([freq (make-hash)])
    (for-each (lambda (x) (hash-update! freq x add1 0)) nums)
    (define max-freq
      (foldl (lambda (v acc) (if (> v acc) v acc)) 0 (hash-values freq)))
    (foldl (lambda (v acc) (if (= v max-freq) (+ acc v) acc)) 0 (hash-values freq))))
```

## Erlang

```erlang
-spec max_frequency_elements(Nums :: [integer()]) -> integer().
max_frequency_elements(Nums) ->
    {_, _, Total} = lists:foldl(
        fun(N, {Map, MaxF, Tot}) ->
            Freq = maps:get(N, Map, 0) + 1,
            NewMap = maps:put(N, Freq, Map),
            if
                Freq > MaxF -> {NewMap, Freq, Freq};
                Freq == MaxF -> {NewMap, MaxF, Tot + Freq};
                true -> {NewMap, MaxF, Tot}
            end
        end,
        {#{}, 0, 0},
        Nums),
    Total.
```

## Elixir

```elixir
defmodule Solution do
  @spec max_frequency_elements(nums :: [integer]) :: integer
  def max_frequency_elements(nums) do
    freqs =
      Enum.reduce(nums, %{}, fn x, acc ->
        Map.update(acc, x, 1, &(&1 + 1))
      end)

    max_freq = freqs |> Map.values() |> Enum.max()

    freqs
    |> Enum.filter(fn {_k, v} -> v == max_freq end)
    |> Enum.map(fn {_k, v} -> v end)
    |> Enum.sum()
  end
end
```
