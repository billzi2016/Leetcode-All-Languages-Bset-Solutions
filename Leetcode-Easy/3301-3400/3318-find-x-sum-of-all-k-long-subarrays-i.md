# 3318. Find X-Sum of All K-Long Subarrays I

## Cpp

```cpp
class Solution {
public:
    vector<int> findXSum(vector<int>& nums, int k, int x) {
        int n = nums.size();
        vector<int> ans;
        for (int i = 0; i + k <= n; ++i) {
            unordered_map<int,int> cnt;
            for (int j = i; j < i + k; ++j) {
                cnt[nums[j]]++;
            }
            vector<int> distinct;
            distinct.reserve(cnt.size());
            for (auto &p : cnt) distinct.push_back(p.first);
            sort(distinct.begin(), distinct.end());
            int limit = min(x, (int)distinct.size());
            long long sum = 0;
            for (int d = 0; d < limit; ++d) {
                int val = distinct[d];
                sum += 1LL * val * cnt[val];
            }
            ans.push_back((int)sum);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] findXSum(int[] nums, int k, int x) {
        int n = nums.length;
        int m = n - k + 1;
        int[] answer = new int[m];
        for (int i = 0; i < m; i++) {
            java.util.Map<Integer, Integer> freq = new java.util.HashMap<>();
            for (int j = i; j < i + k; j++) {
                freq.put(nums[j], freq.getOrDefault(nums[j], 0) + 1);
            }
            java.util.List<Integer> keys = new java.util.ArrayList<>(freq.keySet());
            java.util.Collections.sort(keys);
            int limit = Math.min(x, keys.size());
            int sum = 0;
            for (int d = 0; d < limit; d++) {
                int val = keys.get(d);
                sum += val * freq.get(val);
            }
            answer[i] = sum;
        }
        return answer;
    }
}
```

## Python

```python
class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(nums)
        ans = []
        for i in range(n - k + 1):
            window = nums[i:i + k]
            freq = {}
            total = 0
            for v in window:
                freq[v] = freq.get(v, 0) + 1
                total += v
            distinct_vals = sorted(freq.keys())
            if len(distinct_vals) < x:
                ans.append(total)
            else:
                s = 0
                for val in distinct_vals[:x]:
                    s += val * freq[val]
                ans.append(s)
        return ans
```

## Python3

```python
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n - k + 1):
            window = nums[i:i + k]
            freq = {}
            for v in window:
                freq[v] = freq.get(v, 0) + 1
            distinct_vals = sorted(freq.keys())
            if len(distinct_vals) <= x:
                result.append(sum(window))
            else:
                total = 0
                for val in distinct_vals[:x]:
                    total += val * freq[val]
                result.append(total)
        return result
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findXSum(int* nums, int numsSize, int k, int x, int* returnSize) {
    int windows = numsSize - k + 1;
    int* ans = (int*)malloc(windows * sizeof(int));
    *returnSize = windows;
    
    for (int i = 0; i < windows; ++i) {
        int freq[51] = {0};
        for (int j = i; j < i + k; ++j) {
            freq[nums[j]]++;
        }
        int sum = 0;
        int distinctTaken = 0;
        for (int v = 1; v <= 50; ++v) {
            if (freq[v] > 0) {
                if (distinctTaken < x) {
                    sum += v * freq[v];
                    distinctTaken++;
                } else {
                    // already have x distinct smallest values, ignore larger ones
                    break;
                }
            }
        }
        /* If there are fewer than x distinct numbers, the loop above adds all of them,
           which matches the definition that the x‑sum equals the sum of the whole array. */
        ans[i] = sum;
    }
    
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public int[] FindXSum(int[] nums, int k, int x) {
        int n = nums.Length;
        int[] answer = new int[n - k + 1];
        int[] freq = new int[51]; // values are in [1,50]

        // initialize first window
        for (int i = 0; i < k; ++i) {
            freq[nums[i]]++;
        }

        for (int start = 0; start <= n - k; ++start) {
            answer[start] = ComputeXSum(freq, x);
            if (start + k == n) break;
            int outVal = nums[start];
            int inVal = nums[start + k];
            freq[outVal]--;
            freq[inVal]++;
        }

        return answer;
    }

    private int ComputeXSum(int[] freq, int x) {
        int distinct = 0;
        int sum = 0;
        for (int val = 1; val <= 50; ++val) {
            if (freq[val] == 0) continue;
            distinct++;
            if (distinct > x) break;
            sum += val * freq[val];
        }
        // If there are fewer than x distinct values, the loop adds all of them,
        // which equals the sum of the whole subarray.
        return sum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} x
 * @return {number[]}
 */
var findXSum = function(nums, k, x) {
    const n = nums.length;
    const res = [];
    for (let i = 0; i <= n - k; ++i) {
        const freq = new Map();
        for (let j = i; j < i + k; ++j) {
            freq.set(nums[j], (freq.get(nums[j]) || 0) + 1);
        }
        const distinctVals = Array.from(freq.keys()).sort((a, b) => a - b);
        let cnt = Math.min(x, distinctVals.length);
        let sum = 0;
        for (let d = 0; d < cnt; ++d) {
            const val = distinctVals[d];
            sum += val * freq.get(val);
        }
        res.push(sum);
    }
    return res;
};
```

## Typescript

```typescript
function findXSum(nums: number[], k: number, x: number): number[] {
    const n = nums.length;
    const ans: number[] = [];
    for (let i = 0; i <= n - k; ++i) {
        const freq = new Map<number, number>();
        let total = 0;
        for (let j = i; j < i + k; ++j) {
            const v = nums[j];
            total += v;
            freq.set(v, (freq.get(v) ?? 0) + 1);
        }
        if (freq.size <= x) {
            ans.push(total);
            continue;
        }
        const entries: [number, number][] = Array.from(freq.entries());
        entries.sort((a, b) => {
            if (b[1] !== a[1]) return b[1] - a[1]; // higher frequency first
            return b[0] - a[0]; // tie -> larger value first
        });
        let sum = 0;
        for (let t = 0; t < x; ++t) {
            const [val, cnt] = entries[t];
            sum += val * cnt;
        }
        ans.push(sum);
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer $x
     * @return Integer[]
     */
    function findXSum($nums, $k, $x) {
        $n = count($nums);
        $answer = [];

        for ($i = 0; $i <= $n - $k; $i++) {
            // frequency array for values 1..50
            $freq = array_fill(0, 51, 0);
            $totalSum = 0;

            for ($j = $i; $j < $i + $k; $j++) {
                $val = $nums[$j];
                $freq[$val]++;
                $totalSum += $val;
            }

            // count distinct elements
            $distinct = 0;
            for ($v = 1; $v <= 50; $v++) {
                if ($freq[$v] > 0) $distinct++;
            }

            if ($distinct <= $x) {
                $answer[] = $totalSum;
                continue;
            }

            // collect (frequency, value) pairs
            $pairs = [];
            for ($v = 1; $v <= 50; $v++) {
                if ($freq[$v] > 0) {
                    $pairs[] = [$freq[$v], $v];
                }
            }

            // sort by frequency descending, then value descending
            usort($pairs, function($a, $b) {
                if ($a[0] == $b[0]) {
                    return $b[1] <=> $a[1]; // larger value first
                }
                return $b[0] <=> $a[0];
            });

            $xSum = 0;
            for ($t = 0; $t < $x; $t++) {
                $xSum += $pairs[$t][0] * $pairs[$t][1];
            }

            $answer[] = $xSum;
        }

        return $answer;
    }
}
```

## Swift

```swift
class Solution {
    func findXSum(_ nums: [Int], _ k: Int, _ x: Int) -> [Int] {
        let n = nums.count
        var answer = [Int]()
        for i in 0...(n - k) {
            var freq = [Int:Int]()
            for j in i..<(i + k) {
                freq[nums[j], default: 0] += 1
            }
            var items = [(value: Int, count: Int)]()
            items.reserveCapacity(freq.count)
            for (v, c) in freq {
                items.append((v, c))
            }
            items.sort { a, b in
                if a.count != b.count {
                    return a.count > b.count
                } else {
                    return a.value > b.value
                }
            }
            var sum = 0
            let limit = min(x, items.count)
            for idx in 0..<limit {
                let e = items[idx]
                sum += e.value * e.count
            }
            answer.append(sum)
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findXSum(nums: IntArray, k: Int, x: Int): IntArray {
        val n = nums.size
        val res = IntArray(n - k + 1)
        for (i in 0..n - k) {
            val freq = HashMap<Int, Int>()
            for (j in i until i + k) {
                freq[nums[j]] = (freq[nums[j]] ?: 0) + 1
            }
            val distinctVals = freq.keys.sorted()
            var sum = 0L
            var cnt = 0
            for (v in distinctVals) {
                if (cnt >= x) break
                sum += v.toLong() * (freq[v] ?: 0)
                cnt++
            }
            res[i] = sum.toInt()
        }
        return res
    }
}
```

## Dart

```dart
class Solution {
  List<int> findXSum(List<int> nums, int k, int x) {
    int n = nums.length;
    List<int> answer = [];
    for (int i = 0; i <= n - k; ++i) {
      Map<int, int> freq = {};
      for (int j = i; j < i + k; ++j) {
        freq[nums[j]] = (freq[nums[j]] ?? 0) + 1;
      }
      List<int> distinct = freq.keys.toList()..sort();
      int sum = 0;
      int taken = 0;
      for (int val in distinct) {
        if (taken == x) break;
        sum += val * freq[val]!;
        taken++;
      }
      answer.add(sum);
    }
    return answer;
  }
}
```

## Golang

```go
import "sort"

func findXSum(nums []int, k int, x int) []int {
	n := len(nums)
	ans := make([]int, n-k+1)

	for i := 0; i <= n-k; i++ {
		freq := make(map[int]int)
		for j := i; j < i+k; j++ {
			freq[nums[j]]++
		}

		type pair struct{ val, cnt int }
		pairs := make([]pair, 0, len(freq))
		for v, c := range freq {
			pairs = append(pairs, pair{v, c})
		}

		sort.Slice(pairs, func(a, b int) bool {
			if pairs[a].cnt != pairs[b].cnt {
				return pairs[a].cnt > pairs[b].cnt
			}
			return pairs[a].val > pairs[b].val
		})

		limit := x
		if len(pairs) < limit {
			limit = len(pairs)
		}
		sum := 0
		for t := 0; t < limit; t++ {
			sum += pairs[t].val * pairs[t].cnt
		}
		ans[i] = sum
	}

	return ans
}
```

## Ruby

```ruby
def find_x_sum(nums, k, x)
  n = nums.length
  result = []
  (0..n - k).each do |i|
    freq = Hash.new(0)
    nums[i, k].each { |v| freq[v] += 1 }
    sorted = freq.map { |val, cnt| [cnt, val] }.sort_by { |cnt, val| [-cnt, -val] }
    sum = 0
    sorted.first(x).each { |cnt, val| sum += cnt * val }
    result << sum
  end
  result
end
```

## Scala

```scala
object Solution {
    def findXSum(nums: Array[Int], k: Int, x: Int): Array[Int] = {
        val n = nums.length
        val result = new Array[Int](n - k + 1)
        for (i <- 0 until n - k + 1) {
            val cnt = new Array[Int](51)
            var totalSum = 0
            var distinct = 0
            var j = i
            while (j < i + k) {
                val v = nums(j)
                if (cnt(v) == 0) distinct += 1
                cnt(v) += 1
                totalSum += v
                j += 1
            }
            if (distinct <= x) {
                result(i) = totalSum
            } else {
                val pairs = scala.collection.mutable.ArrayBuffer.empty[(Int, Int)]
                var v = 1
                while (v <= 50) {
                    if (cnt(v) > 0) pairs.append((cnt(v), v))
                    v += 1
                }
                val sorted = pairs.sortWith { case ((f1, val1), (f2, val2)) =>
                    if (f1 != f2) f1 > f2 else val1 > val2
                }
                var sum = 0
                var idx = 0
                while (idx < x) {
                    val (freq, value) = sorted(idx)
                    sum += freq * value
                    idx += 1
                }
                result(i) = sum
            }
        }
        result
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_x_sum(nums: Vec<i32>, k: i32, x: i32) -> Vec<i32> {
        use std::collections::{HashMap, HashSet};
        let n = nums.len();
        let k_usize = k as usize;
        let x_usize = x as usize;
        let mut result = Vec::with_capacity(n - k_usize + 1);
        for start in 0..=n - k_usize {
            // frequency map for current window
            let mut freq: HashMap<i32, i32> = HashMap::new();
            for &val in &nums[start..start + k_usize] {
                *freq.entry(val).or_insert(0) += 1;
            }
            // collect (value, count) and sort by descending count then descending value
            let mut pairs: Vec<(i32, i32)> = freq.iter().map(|(&v, &c)| (v, c)).collect();
            pairs.sort_unstable_by(|a, b| {
                if a.1 != b.1 {
                    b.1.cmp(&a.1) // descending count
                } else {
                    b.0.cmp(&a.0) // descending value for tie
                }
            });
            let take = std::cmp::min(x_usize, pairs.len());
            let mut selected: HashSet<i32> = HashSet::new();
            for i in 0..take {
                selected.insert(pairs[i].0);
            }
            // compute sum of elements whose value is selected
            let mut sum = 0i32;
            for &val in &nums[start..start + k_usize] {
                if selected.contains(&val) {
                    sum += val;
                }
            }
            result.push(sum);
        }
        result
    }
}
```

## Racket

```racket
(require racket/list)
(require racket/hash)

(define (x-sum lst x)
  (let ((ht (make-hash)))
    (for ([v lst])
      (hash-update! ht v add1 0))
    (define pairs
      (hash-map ht (lambda (k v) (list v k)))) ; (freq value)
    (define sorted
      (sort pairs (lambda (a b)
                    (or (> (first a) (first b))
                        (and (= (first a) (first b)) (> (second a) (second b)))))))
    (let loop ((i 0) (sum 0) (len (length sorted)))
      (if (or (= i x) (= i len))
          sum
          (let* ((pair (list-ref sorted i))
                 (freq (first pair))
                 (val (second pair)))
            (loop (+ i 1) (+ sum (* freq val)) len))))))

(define/contract (find-x-sum nums k x)
  (-> (listof exact-integer?) exact-integer? exact-integer? (listof exact-integer?))
  (let loop ((i 0) (n (length nums)) (res '()))
    (if (> i (- n k))
        (reverse res)
        (let* ((sub (take (drop nums i) k))
               (xs (x-sum sub x)))
          (loop (+ i 1) n (cons xs res))))))
```

## Erlang

```erlang
-spec find_x_sum(Nums :: [integer()], K :: integer(), X :: integer()) -> [integer()].
find_x_sum(Nums, K, X) ->
    N = length(Nums),
    MaxStart = N - K,
    lists:map(
        fun(I) ->
            Sub = lists:sublist(Nums, I + 1, K),
            window_xsum(Sub, X)
        end,
        lists:seq(0, MaxStart)
    ).

window_xsum(Sub, X) ->
    FreqMap = freq(Sub, #{}),
    Sorted = lists:sort(
        fun({V1, C1}, {V2, C2}) ->
            case C1 == C2 of
                true -> V1 > V2;
                false -> C1 > C2
            end
        end,
        [{Val, Count} || {Val, Count} <- maps:to_list(FreqMap)]
    ),
    Selected = lists:sublist(Sorted, X),
    lists:foldl(fun({V, C}, Acc) -> Acc + V * C end, 0, Selected).

freq([], Map) -> Map;
freq([H | T], Map) ->
    Count = maps:get(H, Map, 0),
    freq(T, maps:put(H, Count + 1, Map)).
```

## Elixir

```elixir
defmodule Solution do
  @spec find_x_sum(nums :: [integer], k :: integer, x :: integer) :: [integer]
  def find_x_sum(nums, k, x) do
    n = length(nums)
    max_val = 50

    0..(n - k)
    |> Enum.map(fn i ->
      freq = :array.new(max_val + 1, default: 0)

      # count frequencies in the window
      Enum.reduce(i..(i + k - 1), freq, fn idx, acc ->
        val = Enum.at(nums, idx)
        current = :array.get(val, acc)
        :array.set(val, current + 1, acc)
      end)
      |> compute_sum(x, max_val)
    end)
  end

  defp compute_sum(freq_array, x, max_val) do
    {sum, distinct_seen, _} =
      Enum.reduce(1..max_val, {0, 0, false}, fn v, {s, d, stop} ->
        if stop do
          {s, d, true}
        else
          cnt = :array.get(v, freq_array)
          if cnt > 0 do
            nd = d + 1
            ns = s + v * cnt
            if nd == x do
              # we have reached exactly x distinct; continue adding this value but stop after it
              {ns, nd, true}
            else
              {ns, nd, false}
            end
          else
            {s, d, false}
          end
        end
      end)

    sum
  end
end
```
