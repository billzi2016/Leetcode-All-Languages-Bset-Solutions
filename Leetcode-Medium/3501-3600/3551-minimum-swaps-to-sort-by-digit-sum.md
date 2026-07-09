# 3551. Minimum Swaps to Sort by Digit Sum

## Cpp

```cpp
class Solution {
public:
    int digitSum(int x) {
        int sum = 0;
        while (x > 0) {
            sum += x % 10;
            x /= 10;
        }
        return sum;
    }
    
    int minSwaps(vector<int>& nums) {
        int n = nums.size();
        vector<int> sortedVals = nums;
        sort(sortedVals.begin(), sortedVals.end(), [&](int a, int b){
            int sa = digitSum(a);
            int sb = digitSum(b);
            if (sa != sb) return sa < sb;
            return a < b;
        });
        
        unordered_map<int,int> targetPos;
        targetPos.reserve(n * 2);
        for (int i = 0; i < n; ++i) {
            targetPos[sortedVals[i]] = i;
        }
        
        vector<int> perm(n);
        for (int i = 0; i < n; ++i) {
            perm[i] = targetPos[nums[i]];
        }
        
        vector<char> visited(n, 0);
        int cycles = 0;
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                int cur = i;
                while (!visited[cur]) {
                    visited[cur] = 1;
                    cur = perm[cur];
                }
                ++cycles;
            }
        }
        return n - cycles;
    }
};
```

## Java

```java
class Solution {
    public int minSwaps(int[] nums) {
        int n = nums.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;

        java.util.Arrays.sort(idx, (a, b) -> {
            int sumA = digitSum(nums[a]);
            int sumB = digitSum(nums[b]);
            if (sumA != sumB) return Integer.compare(sumA, sumB);
            return Integer.compare(nums[a], nums[b]);
        });

        int[] targetPos = new int[n];
        for (int pos = 0; pos < n; pos++) {
            targetPos[idx[pos]] = pos;
        }

        boolean[] visited = new boolean[n];
        int swaps = 0;
        for (int i = 0; i < n; i++) {
            if (visited[i]) continue;
            int cur = i;
            int cycleLen = 0;
            while (!visited[cur]) {
                visited[cur] = true;
                cur = targetPos[cur];
                cycleLen++;
            }
            if (cycleLen > 1) swaps += cycleLen - 1;
        }
        return swaps;
    }

    private int digitSum(int x) {
        int sum = 0;
        while (x > 0) {
            sum += x % 10;
            x /= 10;
        }
        return sum;
    }
}
```

## Python

```python
class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        sorted_nums = sorted(nums, key=lambda v: (digit_sum(v), v))
        target_idx = {num: i for i, num in enumerate(sorted_nums)}
        perm = [target_idx[num] for num in nums]

        visited = [False] * n
        cycles = 0
        for i in range(n):
            if not visited[i]:
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = perm[j]
                cycles += 1

        return n - cycles
```

## Python3

```python
class Solution:
    def minSwaps(self, nums):
        n = len(nums)

        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        # Pair: (digit sum, value, original index)
        paired = [(digit_sum(v), v, i) for i, v in enumerate(nums)]
        paired.sort(key=lambda x: (x[0], x[1]))

        # target position for each original index
        target_pos = [0] * n
        for sorted_idx, (_, _, orig_idx) in enumerate(paired):
            target_pos[orig_idx] = sorted_idx

        visited = [False] * n
        cycles = 0

        for i in range(n):
            if not visited[i]:
                cur = i
                while not visited[cur]:
                    visited[cur] = True
                    cur = target_pos[cur]
                cycles += 1

        return n - cycles
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int val;
    int idx;
    int sum;
} Node;

static int digitSum(int x) {
    int s = 0;
    while (x > 0) {
        s += x % 10;
        x /= 10;
    }
    return s;
}

static int cmpNode(const void *a, const void *b) {
    const Node *na = (const Node *)a;
    const Node *nb = (const Node *)b;
    if (na->sum != nb->sum)
        return na->sum - nb->sum;
    return na->val - nb->val;
}

int minSwaps(int* nums, int numsSize) {
    if (numsSize <= 1) return 0;

    Node *arr = (Node *)malloc(numsSize * sizeof(Node));
    for (int i = 0; i < numsSize; ++i) {
        arr[i].val = nums[i];
        arr[i].idx = i;
        arr[i].sum = digitSum(nums[i]);
    }

    qsort(arr, numsSize, sizeof(Node), cmpNode);

    int *pos = (int *)malloc(numsSize * sizeof(int));
    for (int i = 0; i < numsSize; ++i) {
        pos[arr[i].idx] = i;
    }
    free(arr);

    char *vis = (char *)calloc(numsSize, sizeof(char));
    int swaps = 0;

    for (int i = 0; i < numsSize; ++i) {
        if (vis[i]) continue;
        int cycleSize = 0;
        int j = i;
        while (!vis[j]) {
            vis[j] = 1;
            j = pos[j];
            ++cycleSize;
        }
        if (cycleSize > 1)
            swaps += cycleSize - 1;
    }

    free(pos);
    free(vis);
    return swaps;
}
```

## Csharp

```csharp
public class Solution
{
    public int MinSwaps(int[] nums)
    {
        int n = nums.Length;
        // indices sorted by digit sum then value
        int[] idx = new int[n];
        for (int i = 0; i < n; i++) idx[i] = i;

        Array.Sort(idx, (a, b) =>
        {
            int sa = DigitSum(nums[a]);
            int sb = DigitSum(nums[b]);
            if (sa != sb) return sa.CompareTo(sb);
            return nums[a].CompareTo(nums[b]);
        });

        // map value -> target position
        var posMap = new Dictionary<int, int>(n);
        for (int i = 0; i < n; i++)
        {
            posMap[nums[idx[i]]] = i;
        }

        // permutation: where each current index should go
        int[] perm = new int[n];
        for (int i = 0; i < n; i++)
        {
            perm[i] = posMap[nums[i]];
        }

        bool[] visited = new bool[n];
        int cycles = 0;
        for (int i = 0; i < n; i++)
        {
            if (visited[i]) continue;
            int cur = i;
            while (!visited[cur])
            {
                visited[cur] = true;
                cur = perm[cur];
            }
            cycles++;
        }

        return n - cycles;
    }

    private static int DigitSum(int x)
    {
        int sum = 0;
        while (x > 0)
        {
            sum += x % 10;
            x /= 10;
        }
        return sum;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minSwaps = function(nums) {
    const digitSum = (x) => {
        let sum = 0;
        while (x > 0) {
            sum += x % 10;
            x = Math.trunc(x / 10);
        }
        return sum;
    };
    
    const n = nums.length;
    // Sorted order according to digit sum, then value
    const sorted = [...nums].sort((a, b) => {
        const sa = digitSum(a), sb = digitSum(b);
        if (sa !== sb) return sa - sb;
        return a - b;
    });
    
    // Map each number to its target index in the sorted array
    const targetIdx = new Map();
    for (let i = 0; i < n; ++i) {
        targetIdx.set(sorted[i], i);
    }
    
    const visited = new Array(n).fill(false);
    let swaps = 0;
    
    for (let i = 0; i < n; ++i) {
        if (visited[i]) continue;
        // Determine where the element at position i should go
        let j = i;
        let cycleSize = 0;
        while (!visited[j]) {
            visited[j] = true;
            const val = nums[j];
            j = targetIdx.get(val);
            ++cycleSize;
        }
        if (cycleSize > 1) swaps += cycleSize - 1;
    }
    
    return swaps;
};
```

## Typescript

```typescript
function minSwaps(nums: number[]): number {
    const digitSum = (num: number): number => {
        let sum = 0;
        while (num > 0) {
            sum += num % 10;
            num = Math.trunc(num / 10);
        }
        return sum;
    };

    const sorted = [...nums]
        .map(v => ({ val: v }))
        .sort((a, b) => {
            const sa = digitSum(a.val);
            const sb = digitSum(b.val);
            if (sa !== sb) return sa - sb;
            return a.val - b.val;
        });

    const indexMap = new Map<number, number>();
    for (let i = 0; i < sorted.length; ++i) {
        indexMap.set(sorted[i].val, i);
    }

    const targetPos = nums.map(v => indexMap.get(v)!);
    const n = nums.length;
    const visited = new Array<boolean>(n).fill(false);
    let cycles = 0;

    for (let i = 0; i < n; ++i) {
        if (visited[i]) continue;
        let cur = i;
        let size = 0;
        while (!visited[cur]) {
            visited[cur] = true;
            cur = targetPos[cur];
            ++size;
        }
        if (size > 0) cycles++;
    }

    return n - cycles;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minSwaps($nums) {
        $n = count($nums);
        $info = [];
        for ($i = 0; $i < $n; $i++) {
            $info[] = [
                'val' => $nums[$i],
                'idx' => $i,
                'sum' => $this->digitSum($nums[$i])
            ];
        }

        usort($info, function ($a, $b) {
            if ($a['sum'] == $b['sum']) {
                return $a['val'] <=> $b['val'];
            }
            return $a['sum'] <=> $b['sum'];
        });

        $targetPos = array_fill(0, $n, 0);
        for ($sortedIdx = 0; $sortedIdx < $n; $sortedIdx++) {
            $origIdx = $info[$sortedIdx]['idx'];
            $targetPos[$origIdx] = $sortedIdx;
        }

        $visited = array_fill(0, $n, false);
        $swaps = 0;

        for ($i = 0; $i < $n; $i++) {
            if ($visited[$i] || $targetPos[$i] == $i) {
                continue;
            }
            $cycleSize = 0;
            $j = $i;
            while (!$visited[$j]) {
                $visited[$j] = true;
                $j = $targetPos[$j];
                $cycleSize++;
            }
            if ($cycleSize > 0) {
                $swaps += $cycleSize - 1;
            }
        }

        return $swaps;
    }

    private function digitSum($num) {
        $sum = 0;
        while ($num > 0) {
            $sum += $num % 10;
            $num = intdiv($num, 10);
        }
        return $sum;
    }
}
```

## Swift

```swift
class Solution {
    func minSwaps(_ nums: [Int]) -> Int {
        let n = nums.count
        let sorted = nums.sorted { (a, b) -> Bool in
            let sa = digitSum(a)
            let sb = digitSum(b)
            if sa == sb { return a < b }
            return sa < sb
        }
        var targetIndex = [Int: Int](minimumCapacity: n)
        for (idx, val) in sorted.enumerated() {
            targetIndex[val] = idx
        }
        var perm = [Int](repeating: 0, count: n)
        for i in 0..<n {
            perm[i] = targetIndex[nums[i]]!
        }
        var visited = [Bool](repeating: false, count: n)
        var cycles = 0
        for i in 0..<n {
            if !visited[i] {
                var j = i
                while !visited[j] {
                    visited[j] = true
                    j = perm[j]
                }
                cycles += 1
            }
        }
        return n - cycles
    }

    private func digitSum(_ x: Int) -> Int {
        var num = x
        var sum = 0
        while num > 0 {
            sum += num % 10
            num /= 10
        }
        return sum
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minSwaps(nums: IntArray): Int {
        val n = nums.size
        // Compute digit sum for a number
        fun digitSum(x: Int): Int {
            var v = x
            var s = 0
            while (v > 0) {
                s += v % 10
                v /= 10
            }
            return s
        }

        // Sorted values according to digit sum then value
        val sorted = nums.toMutableList()
        sorted.sortWith(compareBy<Int>({ digitSum(it) }, { it }))

        // Map each value to its target index in the sorted order
        val posMap = HashMap<Int, Int>(n)
        for (i in 0 until n) {
            posMap[sorted[i]] = i
        }

        // Permutation: where each current index should go
        val perm = IntArray(n) { idx -> posMap[nums[idx]]!! }

        var swaps = 0
        val visited = BooleanArray(n)
        for (i in 0 until n) {
            if (!visited[i]) {
                var j = i
                var cycleSize = 0
                while (!visited[j]) {
                    visited[j] = true
                    j = perm[j]
                    cycleSize++
                }
                if (cycleSize > 1) swaps += cycleSize - 1
            }
        }
        return swaps
    }
}
```

## Dart

```dart
class Solution {
  int minSwaps(List<int> nums) {
    int n = nums.length;
    List<int> idx = List.generate(n, (i) => i);

    int digitSum(int x) {
      int sum = 0;
      while (x > 0) {
        sum += x % 10;
        x ~/= 10;
      }
      return sum;
    }

    idx.sort((a, b) {
      int sa = digitSum(nums[a]);
      int sb = digitSum(nums[b]);
      if (sa != sb) return sa - sb;
      return nums[a] - nums[b];
    });

    List<int> targetPos = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      targetPos[idx[i]] = i;
    }

    List<bool> visited = List.filled(n, false);
    int swaps = 0;

    for (int i = 0; i < n; i++) {
      if (visited[i] || targetPos[i] == i) continue;
      int cycleLen = 0;
      int j = i;
      while (!visited[j]) {
        visited[j] = true;
        j = targetPos[j];
        cycleLen++;
      }
      swaps += cycleLen - 1;
    }

    return swaps;
  }
}
```

## Golang

```go
import "sort"

func minSwaps(nums []int) int {
	n := len(nums)
	if n <= 1 {
		return 0
	}
	type item struct {
		val int
		sum int
	}
	arr := make([]item, n)
	for i, v := range nums {
		arr[i] = item{val: v, sum: digitSum(v)}
	}
	sort.Slice(arr, func(i, j int) bool {
		if arr[i].sum != arr[j].sum {
			return arr[i].sum < arr[j].sum
		}
		return arr[i].val < arr[j].val
	})
	target := make(map[int]int, n)
	for i, it := range arr {
		target[it.val] = i
	}
	pos := make([]int, n)
	for i, v := range nums {
		pos[i] = target[v]
	}
	visited := make([]bool, n)
	cycles := 0
	for i := 0; i < n; i++ {
		if visited[i] || pos[i] == i {
			continue
		}
		j := i
		for !visited[j] {
			visited[j] = true
			j = pos[j]
		}
		cycles++
	}
	return n - cycles
}

func digitSum(x int) int {
	sum := 0
	for x > 0 {
		sum += x % 10
		x /= 10
	}
	return sum
}
```

## Ruby

```ruby
def min_swaps(nums)
  n = nums.length
  digit_sum = lambda do |x|
    s = 0
    while x > 0
      s += x % 10
      x /= 10
    end
    s
  end

  sorted = nums.each_with_index.map { |val, idx| [val, idx] }
  sorted.sort_by! { |val, _| [digit_sum.call(val), val] }

  target_pos = Array.new(n)
  sorted.each_with_index do |(_, orig_idx), j|
    target_pos[orig_idx] = j
  end

  visited = Array.new(n, false)
  cycles = 0

  (0...n).each do |i|
    next if visited[i]
    cur = i
    while !visited[cur]
      visited[cur] = true
      cur = target_pos[cur]
    end
    cycles += 1
  end

  n - cycles
end
```

## Scala

```scala
object Solution {
    def minSwaps(nums: Array[Int]): Int = {
        val n = nums.length

        def digitSum(x: Int): Int = {
            var v = x
            var s = 0
            while (v > 0) {
                s += v % 10
                v /= 10
            }
            s
        }

        // Sorted order according to digit sum, then value
        val sorted = nums.clone()
        java.util.Arrays.sort(sorted, new java.util.Comparator[Int] {
            override def compare(a: Int, b: Int): Int = {
                val da = digitSum(a)
                val db = digitSum(b)
                if (da != db) Integer.compare(da, db) else Integer.compare(a, b)
            }
        })

        // Map each value to its target index in the sorted array
        val idxMap = new java.util.HashMap[Int, Int](n * 2)
        var i = 0
        while (i < n) {
            idxMap.put(sorted(i), i)
            i += 1
        }

        // Count swaps via cycle decomposition
        val visited = new Array[Boolean](n)
        var swaps = 0

        var start = 0
        while (start < n) {
            if (!visited(start)) {
                var cycleSize = 0
                var j = start
                while (!visited(j)) {
                    visited(j) = true
                    val targetIdx = idxMap.get(nums(j))
                    j = targetIdx
                    cycleSize += 1
                }
                if (cycleSize > 1) swaps += cycleSize - 1
            }
            start += 1
        }

        swaps
    }
}
```

## Rust

```rust
impl Solution {
    pub fn min_swaps(nums: Vec<i32>) -> i32 {
        fn digit_sum(mut x: i32) -> i32 {
            let mut sum = 0;
            while x > 0 {
                sum += x % 10;
                x /= 10;
            }
            sum
        }

        let n = nums.len();
        if n <= 1 {
            return 0;
        }

        // (digit_sum, value, original_index)
        let mut sorted: Vec<(i32, i32, usize)> = nums
            .iter()
            .enumerate()
            .map(|(i, &v)| (digit_sum(v), v, i))
            .collect();

        sorted.sort_by(|a, b| {
            if a.0 != b.0 {
                a.0.cmp(&b.0)
            } else {
                a.1.cmp(&b.1)
            }
        });

        // target position for each original index
        let mut target = vec![0usize; n];
        for (pos, &(_, _, orig_idx)) in sorted.iter().enumerate() {
            target[orig_idx] = pos;
        }

        // count cycles in the permutation
        let mut visited = vec![false; n];
        let mut cycles = 0usize;

        for i in 0..n {
            if visited[i] {
                continue;
            }
            let mut j = i;
            let mut len = 0usize;
            while !visited[j] {
                visited[j] = true;
                j = target[j];
                len += 1;
            }
            if len > 0 {
                cycles += 1;
            }
        }

        (n - cycles) as i32
    }
}
```

## Racket

```racket
#lang racket

(require racket/list)

(define/contract (min-swaps nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((digit-sum
          (lambda (n)
            (let loop ((x n) (s 0))
              (if (= x 0) s (loop (quotient x 10) (+ s (remainder x 10)))))))
         (sorted
          (sort nums
                (lambda (a b)
                  (let ((da (digit-sum a)) (db (digit-sum b)))
                    (if (= da db)
                        (< a b)
                        (< da db))))))
         (h (make-hash))
         (_ (for ([v sorted] [i (in-naturals)])
              (hash-set! h v i)))
         (n (length nums))
         (perm (make-vector n))
         (_ (for ([v nums] [i (in-naturals)])
              (vector-set! perm i (hash-ref h v))))
         (visited (make-vector n #f))
         (cycles
          (let loop ((i 0) (cnt 0))
            (if (= i n)
                cnt
                (if (vector-ref visited i)
                    (loop (+ i 1) cnt)
                    (begin
                      (let bfs ((j i))
                        (when (not (vector-ref visited j))
                          (vector-set! visited j #t)
                          (bfs (vector-ref perm j))))
                      (loop (+ i 1) (+ cnt 1))))))))
    (- n cycles)))
```

## Erlang

```erlang
-module(solution).
-export([min_swaps/1]).

-spec min_swaps(Nums :: [integer()]) -> integer().
min_swaps(Nums) ->
    Sorted = lists:sort(fun(A, B) ->
        DS_A = digit_sum(A),
        DS_B = digit_sum(B),
        if
            DS_A < DS_B -> true;
            DS_A > DS_B -> false;
            true -> A < B
        end
    end, Nums),
    Map = build_map(Sorted, 0, #{}),
    PermList = [maps:get(V, Map) || V <- Nums],
    PermTuple = list_to_tuple(PermList),
    N = length(Nums),
    Visited0 = erlang:make_tuple(N, false),
    {Cycles, _} = count_cycles(0, N, PermTuple, Visited0),
    N - Cycles.

digit_sum(0) -> 0;
digit_sum(N) when N > 0 ->
    digit_sum(N, 0).

digit_sum(0, Acc) -> Acc;
digit_sum(N, Acc) ->
    digit_sum(N div 10, Acc + (N rem 10)).

build_map([], _Idx, Acc) -> Acc;
build_map([H | T], Idx, Acc) ->
    NewAcc = maps:put(H, Idx, Acc),
    build_map(T, Idx + 1, NewAcc).

count_cycles(Idx, N, _PermTuple, Visited) when Idx == N ->
    {0, Visited};
count_cycles(Idx, N, PermTuple, Visited) ->
    case element(Idx + 1, Visited) of
        true ->
            count_cycles(Idx + 1, N, PermTuple, Visited);
        false ->
            Visited1 = setelement(Idx + 1, Visited, true),
            NextIdx = element(Idx + 1, PermTuple),
            {Visited2, _} = traverse_cycle(NextIdx, PermTuple, Visited1),
            {RestCycles, FinalVis} = count_cycles(Idx + 1, N, PermTuple, Visited2),
            {RestCycles + 1, FinalVis}
    end.

traverse_cycle(CurIdx, PermTuple, Visited) ->
    case element(CurIdx + 1, Visited) of
        true -> {Visited, CurIdx};
        false ->
            NextIdx = element(CurIdx + 1, PermTuple),
            Visited1 = setelement(CurIdx + 1, Visited, true),
            traverse_cycle(NextIdx, PermTuple, Visited1)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec min_swaps(nums :: [integer]) :: integer
  def min_swaps(nums) do
    sorted = Enum.sort_by(nums, fn x -> {digit_sum(x), x} end)
    index_map = Enum.with_index(sorted) |> Enum.into(%{}, fn {v, i} -> {v, i} end)

    orig_tuple = :erlang.list_to_tuple(nums)
    n = tuple_size(orig_tuple)
    visited = :erlang.make_tuple(n, false)

    {_final_visited, swaps} =
      0..(n - 1)
      |> Enum.reduce({visited, 0}, fn i, {vis, acc} ->
        if :erlang.element(i + 1, vis) do
          {vis, acc}
        else
          {new_vis, cycle_len} = traverse(i, orig_tuple, index_map, vis, 0)
          added = if cycle_len > 0, do: cycle_len - 1, else: 0
          {new_vis, acc + added}
        end
      end)

    swaps
  end

  defp digit_sum(0), do: 0
  defp digit_sum(x) when x < 10, do: x
  defp digit_sum(x), do: Integer.digits(x) |> Enum.sum()

  defp traverse(idx, orig, map, visited, cnt) do
    if :erlang.element(idx + 1, visited) do
      {visited, cnt}
    else
      visited = :erlang.setelement(idx + 1, visited, true)
      val = :erlang.element(idx + 1, orig)
      target_idx = Map.fetch!(map, val)
      traverse(target_idx, orig, map, visited, cnt + 1)
    end
  end
end
```
