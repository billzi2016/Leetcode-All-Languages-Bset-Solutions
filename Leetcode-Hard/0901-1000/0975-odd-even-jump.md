# 0975. Odd Even Jump

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int oddEvenJumps(vector<int>& arr) {
        int n = arr.size();
        if (n == 0) return 0;
        vector<int> nextHigher(n, -1), nextLower(n, -1);
        
        // Next higher
        vector<pair<int,int>> order;
        order.reserve(n);
        for (int i = 0; i < n; ++i) order.emplace_back(arr[i], i);
        sort(order.begin(), order.end()); // ascending by value then index
        
        stack<int> st;
        for (auto &p : order) {
            int idx = p.second;
            while (!st.empty() && idx > st.top()) {
                nextHigher[st.top()] = idx;
                st.pop();
            }
            st.push(idx);
        }
        
        // Next lower
        order.clear();
        for (int i = 0; i < n; ++i) order.emplace_back(arr[i], i);
        sort(order.begin(), order.end(),
             [](const pair<int,int>& a, const pair<int,int>& b){
                 if (a.first != b.first) return a.first > b.first; // descending value
                 return a.second < b.second;
             });
        
        while (!st.empty()) st.pop();
        for (auto &p : order) {
            int idx = p.second;
            while (!st.empty() && idx > st.top()) {
                nextLower[st.top()] = idx;
                st.pop();
            }
            st.push(idx);
        }
        
        vector<char> goodOdd(n, 0), goodEven(n, 0);
        goodOdd[n-1] = goodEven[n-1] = 1;
        for (int i = n - 2; i >= 0; --i) {
            if (nextHigher[i] != -1)
                goodOdd[i] = goodEven[nextHigher[i]];
            if (nextLower[i] != -1)
                goodEven[i] = goodOdd[nextLower[i]];
        }
        
        int ans = 0;
        for (int i = 0; i < n; ++i) ans += goodOdd[i];
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int oddEvenJumps(int[] arr) {
        int n = arr.length;
        if (n == 0) return 0;

        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;

        // Next higher jump
        Arrays.sort(idx, (a, b) -> {
            if (arr[a] != arr[b]) return Integer.compare(arr[a], arr[b]);
            return Integer.compare(a, b);
        });
        int[] nextHigher = new int[n];
        Arrays.fill(nextHigher, -1);
        int[] stack = new int[n];
        int sp = 0;
        for (int i : idx) {
            while (sp > 0 && i > stack[sp - 1]) {
                nextHigher[stack[--sp]] = i;
            }
            stack[sp++] = i;
        }

        // Next lower jump
        Arrays.sort(idx, (a, b) -> {
            if (arr[a] != arr[b]) return Integer.compare(arr[b], arr[a]); // descending value
            return Integer.compare(a, b);
        });
        int[] nextLower = new int[n];
        Arrays.fill(nextLower, -1);
        sp = 0;
        for (int i : idx) {
            while (sp > 0 && i > stack[sp - 1]) {
                nextLower[stack[--sp]] = i;
            }
            stack[sp++] = i;
        }

        boolean[] goodOdd = new boolean[n];
        boolean[] goodEven = new boolean[n];
        goodOdd[n - 1] = true;
        goodEven[n - 1] = true;

        for (int i = n - 2; i >= 0; i--) {
            if (nextHigher[i] != -1) {
                goodOdd[i] = goodEven[nextHigher[i]];
            }
            if (nextLower[i] != -1) {
                goodEven[i] = goodOdd[nextLower[i]];
            }
        }

        int count = 0;
        for (boolean b : goodOdd) if (b) count++;
        return count;
    }
}
```

## Python

```python
class Solution(object):
    def oddEvenJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        odd_next = [-1] * n
        even_next = [-1] * n

        # compute next higher indices for odd jumps
        order = sorted(range(n), key=lambda i: (arr[i], i))
        stack = []
        for idx in order:
            while stack and stack[-1] < idx:
                odd_next[stack.pop()] = idx
            stack.append(idx)

        # compute next lower indices for even jumps
        order = sorted(range(n), key=lambda i: (-arr[i], i))
        stack = []
        for idx in order:
            while stack and stack[-1] < idx:
                even_next[stack.pop()] = idx
            stack.append(idx)

        odd_good = [False] * n
        even_good = [False] * n
        odd_good[-1] = even_good[-1] = True

        for i in range(n - 2, -1, -1):
            if odd_next[i] != -1:
                odd_good[i] = even_good[odd_next[i]]
            if even_next[i] != -1:
                even_good[i] = odd_good[even_next[i]]

        return sum(odd_good)
```

## Python3

```python
class Solution:
    def oddEvenJumps(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        # helper to compute next indices using monotonic stack
        def make_next(sorted_pairs):
            nxt = [-1] * n
            stack = []
            for _, idx in sorted_pairs:
                while stack and stack[-1] < idx:
                    prev = stack.pop()
                    nxt[prev] = idx
                stack.append(idx)
            return nxt

        # next higher: sort by value asc, then index asc
        sorted_inc = sorted(((val, i) for i, val in enumerate(arr)), key=lambda x: (x[0], x[1]))
        next_higher = make_next(sorted_inc)

        # next lower: sort by value desc, then index asc
        sorted_dec = sorted(((val, i) for i, val in enumerate(arr)), key=lambda x: (-x[0], x[1]))
        next_lower = make_next(sorted_dec)

        good_odd = [False] * n
        good_even = [False] * n
        good_odd[-1] = good_even[-1] = True

        for i in range(n - 2, -1, -1):
            hi = next_higher[i]
            lo = next_lower[i]
            if hi != -1:
                good_odd[i] = good_even[hi]
            if lo != -1:
                good_even[i] = good_odd[lo]

        return sum(good_odd)
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct {
    int val;
    int idx;
} Pair;

static int cmpOdd(const void *a, const void *b) {
    const Pair *pa = (const Pair *)a;
    const Pair *pb = (const Pair *)b;
    if (pa->val != pb->val) return pa->val - pb->val;          // ascending value
    return pa->idx - pb->idx;                                 // tie by index
}

static int cmpEven(const void *a, const void *b) {
    const Pair *pa = (const Pair *)a;
    const Pair *pb = (const Pair *)b;
    if (pa->val != pb->val) return pb->val - pa->val;          // descending value
    return pa->idx - pb->idx;                                 // tie by index
}

int oddEvenJumps(int* arr, int arrSize) {
    if (arrSize <= 1) return arrSize;

    Pair *pairs = (Pair *)malloc(sizeof(Pair) * arrSize);
    for (int i = 0; i < arrSize; ++i) {
        pairs[i].val = arr[i];
        pairs[i].idx = i;
    }

    int *nextHigher = (int *)malloc(sizeof(int) * arrSize);
    int *nextLower  = (int *)malloc(sizeof(int) * arrSize);
    for (int i = 0; i < arrSize; ++i) {
        nextHigher[i] = -1;
        nextLower[i] = -1;
    }

    // Compute next higher (odd jumps)
    qsort(pairs, arrSize, sizeof(Pair), cmpOdd);
    int *stack = (int *)malloc(sizeof(int) * arrSize);
    int top = -1;
    for (int i = 0; i < arrSize; ++i) {
        int idx = pairs[i].idx;
        while (top >= 0 && idx > stack[top]) {
            nextHigher[stack[top]] = idx;
            --top;
        }
        stack[++top] = idx;
    }

    // Compute next lower (even jumps)
    qsort(pairs, arrSize, sizeof(Pair), cmpEven);
    top = -1;
    for (int i = 0; i < arrSize; ++i) {
        int idx = pairs[i].idx;
        while (top >= 0 && idx > stack[top]) {
            nextLower[stack[top]] = idx;
            --top;
        }
        stack[++top] = idx;
    }

    bool *oddReach = (bool *)malloc(sizeof(bool) * arrSize);
    bool *evenReach = (bool *)malloc(sizeof(bool) * arrSize);
    memset(oddReach, 0, sizeof(bool) * arrSize);
    memset(evenReach, 0, sizeof(bool) * arrSize);

    oddReach[arrSize - 1] = true;
    evenReach[arrSize - 1] = true;

    for (int i = arrSize - 2; i >= 0; --i) {
        if (nextHigher[i] != -1)
            oddReach[i] = evenReach[nextHigher[i]];
        else
            oddReach[i] = false;

        if (nextLower[i] != -1)
            evenReach[i] = oddReach[nextLower[i]];
        else
            evenReach[i] = false;
    }

    int count = 0;
    for (int i = 0; i < arrSize; ++i) {
        if (oddReach[i]) ++count;
    }

    free(pairs);
    free(nextHigher);
    free(nextLower);
    free(stack);
    free(oddReach);
    free(evenReach);

    return count;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int OddEvenJumps(int[] arr) {
        int n = arr.Length;
        if (n == 0) return 0;

        int[] nextHigher = new int[n];
        int[] nextLower = new int[n];
        for (int i = 0; i < n; i++) {
            nextHigher[i] = -1;
            nextLower[i] = -1;
        }

        // indices sorted by value asc, then index asc
        int[] indices = new int[n];
        for (int i = 0; i < n; i++) indices[i] = i;
        Array.Sort(indices, (a, b) => {
            if (arr[a] == arr[b]) return a.CompareTo(b);
            return arr[a].CompareTo(arr[b]);
        });

        var stack = new Stack<int>();
        foreach (int idx in indices) {
            while (stack.Count > 0 && idx > stack.Peek()) {
                nextHigher[stack.Pop()] = idx;
            }
            stack.Push(idx);
        }

        // indices sorted by value desc, then index asc
        Array.Sort(indices, (a, b) => {
            if (arr[a] == arr[b]) return a.CompareTo(b);
            return arr[b].CompareTo(arr[a]); // descending value
        });

        stack.Clear();
        foreach (int idx in indices) {
            while (stack.Count > 0 && idx > stack.Peek()) {
                nextLower[stack.Pop()] = idx;
            }
            stack.Push(idx);
        }

        bool[] odd = new bool[n];
        bool[] even = new bool[n];
        odd[n - 1] = true;
        even[n - 1] = true;

        for (int i = n - 2; i >= 0; i--) {
            if (nextHigher[i] != -1) odd[i] = even[nextHigher[i]];
            if (nextLower[i] != -1) even[i] = odd[nextLower[i]];
        }

        int count = 0;
        for (int i = 0; i < n; i++) {
            if (odd[i]) count++;
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var oddEvenJumps = function(arr) {
    const n = arr.length;
    if (n === 0) return 0;

    // helper to compute next indices using monotonic stack after sorting
    const makeNext = (indices) => {
        const next = new Array(n).fill(-1);
        const stack = [];
        for (const idx of indices) {
            while (stack.length && idx > stack[stack.length - 1]) {
                const prev = stack.pop();
                next[prev] = idx;
            }
            stack.push(idx);
        }
        return next;
    };

    // indices sorted by value asc, then index asc -> for odd jumps (next higher)
    const ascIndices = Array.from({length: n}, (_, i) => i).sort((i, j) => {
        if (arr[i] !== arr[j]) return arr[i] - arr[j];
        return i - j;
    });
    const nextHigher = makeNext(ascIndices);

    // indices sorted by value desc, then index asc -> for even jumps (next lower)
    const descIndices = Array.from({length: n}, (_, i) => i).sort((i, j) => {
        if (arr[i] !== arr[j]) return arr[j] - arr[i];
        return i - j;
    });
    const nextLower = makeNext(descIndices);

    const odd = new Array(n).fill(false);
    const even = new Array(n).fill(false);
    odd[n - 1] = true;
    even[n - 1] = true;

    for (let i = n - 2; i >= 0; --i) {
        if (nextHigher[i] !== -1) {
            odd[i] = even[nextHigher[i]];
        }
        if (nextLower[i] !== -1) {
            even[i] = odd[nextLower[i]];
        }
    }

    let count = 0;
    for (let i = 0; i < n; ++i) {
        if (odd[i]) ++count;
    }
    return count;
};
```

## Typescript

```typescript
function oddEvenJumps(arr: number[]): number {
    const n = arr.length;
    const nextHigher = new Array<number>(n).fill(-1);
    const nextLower = new Array<number>(n).fill(-1);

    const buildNext = (order: number[], target: number[]) => {
        const stack: number[] = [];
        for (const idx of order) {
            while (stack.length && stack[stack.length - 1] < idx) {
                const prev = stack.pop()!;
                target[prev] = idx;
            }
            stack.push(idx);
        }
    };

    // indices sorted by value asc, then index asc
    const asc = Array.from({ length: n }, (_, i) => i).sort((a, b) => {
        if (arr[a] !== arr[b]) return arr[a] - arr[b];
        return a - b;
    });
    buildNext(asc, nextHigher);

    // indices sorted by value desc, then index asc
    const desc = Array.from({ length: n }, (_, i) => i).sort((a, b) => {
        if (arr[a] !== arr[b]) return arr[b] - arr[a];
        return a - b;
    });
    buildNext(desc, nextLower);

    const odd = new Array<boolean>(n);
    const even = new Array<boolean>(n);
    odd[n - 1] = true;
    even[n - 1] = true;

    for (let i = n - 2; i >= 0; --i) {
        odd[i] = nextHigher[i] !== -1 ? even[nextHigher[i]] : false;
        even[i] = nextLower[i] !== -1 ? odd[nextLower[i]] : false;
    }

    let count = 0;
    for (let i = 0; i < n; ++i) {
        if (odd[i]) ++count;
    }
    return count;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function oddEvenJumps($arr) {
        $n = count($arr);
        if ($n == 0) return 0;

        $nextHigher = array_fill(0, $n, -1);
        $nextLower  = array_fill(0, $n, -1);

        // Next higher (odd jumps)
        $indices = range(0, $n - 1);
        usort($indices, function ($i, $j) use ($arr) {
            if ($arr[$i] == $arr[$j]) {
                return $i <=> $j;
            }
            return $arr[$i] <=> $arr[$j];
        });
        $stack = [];
        foreach ($indices as $idx) {
            while (!empty($stack) && end($stack) < $idx) {
                $prev = array_pop($stack);
                $nextHigher[$prev] = $idx;
            }
            $stack[] = $idx;
        }

        // Next lower (even jumps)
        $indicesDesc = range(0, $n - 1);
        usort($indicesDesc, function ($i, $j) use ($arr) {
            if ($arr[$i] == $arr[$j]) {
                return $i <=> $j;
            }
            // descending by value
            return $arr[$j] <=> $arr[$i];
        });
        $stack = [];
        foreach ($indicesDesc as $idx) {
            while (!empty($stack) && end($stack) < $idx) {
                $prev = array_pop($stack);
                $nextLower[$prev] = $idx;
            }
            $stack[] = $idx;
        }

        // DP tables
        $goodOdd  = array_fill(0, $n, false);
        $goodEven = array_fill(0, $n, false);
        $goodOdd[$n - 1] = true;
        $goodEven[$n - 1] = true;

        for ($i = $n - 2; $i >= 0; --$i) {
            $hi = $nextHigher[$i];
            if ($hi != -1) {
                $goodOdd[$i] = $goodEven[$hi];
            }
            $lo = $nextLower[$i];
            if ($lo != -1) {
                $goodEven[$i] = $goodOdd[$lo];
            }
        }

        $count = 0;
        for ($i = 0; $i < $n; ++$i) {
            if ($goodOdd[$i]) {
                $count++;
            }
        }
        return $count;
    }
}
```

## Swift

```swift
class Solution {
    func oddEvenJumps(_ arr: [Int]) -> Int {
        let n = arr.count
        if n == 0 { return 0 }
        var nextHigher = Array(repeating: -1, count: n)
        var nextLower = Array(repeating: -1, count: n)

        // Compute next higher indices for odd jumps
        var indices = Array(0..<n)
        indices.sort {
            if arr[$0] == arr[$1] { return $0 < $1 }
            return arr[$0] < arr[$1]
        }
        var stack = [Int]()
        for idx in indices {
            while let last = stack.last, last < idx {
                nextHigher[stack.removeLast()] = idx
            }
            stack.append(idx)
        }

        // Compute next lower indices for even jumps
        indices.sort {
            if arr[$0] == arr[$1] { return $0 < $1 }
            return arr[$0] > arr[$1]
        }
        stack.removeAll()
        for idx in indices {
            while let last = stack.last, last < idx {
                nextLower[stack.removeLast()] = idx
            }
            stack.append(idx)
        }

        var oddReachable = Array(repeating: false, count: n)
        var evenReachable = Array(repeating: false, count: n)
        oddReachable[n - 1] = true
        evenReachable[n - 1] = true

        if n > 1 {
            for i in stride(from: n - 2, through: 0, by: -1) {
                let nh = nextHigher[i]
                if nh != -1 {
                    oddReachable[i] = evenReachable[nh]
                }
                let nl = nextLower[i]
                if nl != -1 {
                    evenReachable[i] = oddReachable[nl]
                }
            }
        }

        var result = 0
        for i in 0..<n where oddReachable[i] {
            result += 1
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun oddEvenJumps(arr: IntArray): Int {
        val n = arr.size
        if (n == 0) return 0

        val nextHigher = IntArray(n) { -1 }
        val nextLower = IntArray(n) { -1 }

        // Next higher indices for odd jumps
        val sortedIdxAsc = (0 until n).sortedWith(Comparator { i, j ->
            if (arr[i] != arr[j]) {
                arr[i].compareTo(arr[j])
            } else {
                i.compareTo(j)
            }
        })
        val stackHigher = java.util.ArrayDeque<Int>()
        for (idx in sortedIdxAsc) {
            while (!stackHigher.isEmpty() && stackHigher.peekLast() < idx) {
                val prev = stackHigher.removeLast()
                nextHigher[prev] = idx
            }
            stackHigher.addLast(idx)
        }

        // Next lower indices for even jumps
        val sortedIdxDesc = (0 until n).sortedWith(Comparator { i, j ->
            if (arr[i] != arr[j]) {
                arr[j].compareTo(arr[i]) // descending by value
            } else {
                i.compareTo(j)
            }
        })
        val stackLower = java.util.ArrayDeque<Int>()
        for (idx in sortedIdxDesc) {
            while (!stackLower.isEmpty() && stackLower.peekLast() < idx) {
                val prev = stackLower.removeLast()
                nextLower[prev] = idx
            }
            stackLower.addLast(idx)
        }

        val odd = BooleanArray(n)
        val even = BooleanArray(n)
        odd[n - 1] = true
        even[n - 1] = true

        for (i in n - 2 downTo 0) {
            val hi = nextHigher[i]
            if (hi != -1) odd[i] = even[hi]

            val lo = nextLower[i]
            if (lo != -1) even[i] = odd[lo]
        }

        var count = 0
        for (i in 0 until n) {
            if (odd[i]) count++
        }
        return count
    }
}
```

## Dart

```dart
class Solution {
  int oddEvenJumps(List<int> arr) {
    int n = arr.length;
    List<int> oddNext = List.filled(n, -1);
    List<int> evenNext = List.filled(n, -1);

    // Compute next higher (odd jumps)
    List<int> idxs = List.generate(n, (i) => i);
    idxs.sort((a, b) {
      if (arr[a] == arr[b]) return a.compareTo(b);
      return arr[a].compareTo(arr[b]);
    });
    List<int> stack = [];
    for (int i in idxs) {
      while (stack.isNotEmpty && stack.last < i) {
        oddNext[stack.removeLast()] = i;
      }
      stack.add(i);
    }

    // Compute next lower (even jumps)
    idxs.sort((a, b) {
      if (arr[a] == arr[b]) return a.compareTo(b);
      return arr[b].compareTo(arr[a]); // descending
    });
    stack.clear();
    for (int i in idxs) {
      while (stack.isNotEmpty && stack.last < i) {
        evenNext[stack.removeLast()] = i;
      }
      stack.add(i);
    }

    List<bool> goodOdd = List.filled(n, false);
    List<bool> goodEven = List.filled(n, false);
    goodOdd[n - 1] = true;
    goodEven[n - 1] = true;

    for (int i = n - 2; i >= 0; i--) {
      if (oddNext[i] != -1) {
        goodOdd[i] = goodEven[oddNext[i]];
      }
      if (evenNext[i] != -1) {
        goodEven[i] = goodOdd[evenNext[i]];
      }
    }

    int ans = 0;
    for (bool v in goodOdd) {
      if (v) ans++;
    }
    return ans;
  }
}
```

## Golang

```go
import "sort"

func oddEvenJumps(arr []int) int {
	n := len(arr)
	if n == 0 {
		return 0
	}
	nextHigher := make([]int, n)
	nextLower := make([]int, n)
	for i := 0; i < n; i++ {
		nextHigher[i] = -1
		nextLower[i] = -1
	}

	type pair struct{ val, idx int }
	pairs := make([]pair, n)
	for i, v := range arr {
		pairs[i] = pair{v, i}
	}

	sort.Slice(pairs, func(i, j int) bool {
		if pairs[i].val == pairs[j].val {
			return pairs[i].idx < pairs[j].idx
		}
		return pairs[i].val < pairs[j].val
	})
	stack := []int{}
	for _, p := range pairs {
		idx := p.idx
		for len(stack) > 0 && stack[len(stack)-1] < idx {
			prevIdx := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			nextHigher[prevIdx] = idx
		}
		stack = append(stack, idx)
	}

	sort.Slice(pairs, func(i, j int) bool {
		if pairs[i].val == pairs[j].val {
			return pairs[i].idx < pairs[j].idx
		}
		return pairs[i].val > pairs[j].val
	})
	stack = []int{}
	for _, p := range pairs {
		idx := p.idx
		for len(stack) > 0 && stack[len(stack)-1] < idx {
			prevIdx := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			nextLower[prevIdx] = idx
		}
		stack = append(stack, idx)
	}

	odd := make([]bool, n)
	even := make([]bool, n)
	odd[n-1] = true
	even[n-1] = true

	for i := n - 2; i >= 0; i-- {
		if nextHigher[i] != -1 {
			odd[i] = even[nextHigher[i]]
		}
		if nextLower[i] != -1 {
			even[i] = odd[nextLower[i]]
		}
	}

	cnt := 0
	for _, v := range odd {
		if v {
			cnt++
		}
	}
	return cnt
}
```

## Ruby

```ruby
def odd_even_jumps(arr)
  n = arr.length
  next_higher = Array.new(n, -1)
  next_lower = Array.new(n, -1)

  # Odd jumps: smallest greater-or-equal value
  sorted = (0...n).to_a.sort_by { |i| [arr[i], i] }
  stack = []
  sorted.each do |i|
    while !stack.empty? && i > stack[-1]
      prev = stack.pop
      next_higher[prev] = i
    end
    stack << i
  end

  # Even jumps: largest less-or-equal value
  sorted = (0...n).to_a.sort_by { |i| [-arr[i], i] }
  stack = []
  sorted.each do |i|
    while !stack.empty? && i > stack[-1]
      prev = stack.pop
      next_lower[prev] = i
    end
    stack << i
  end

  good_odd = Array.new(n, false)
  good_even = Array.new(n, false)
  good_odd[n - 1] = true
  good_even[n - 1] = true

  (n - 2).downto(0) do |i|
    if next_higher[i] != -1
      good_odd[i] = good_even[next_higher[i]]
    end
    if next_lower[i] != -1
      good_even[i] = good_odd[next_lower[i]]
    end
  end

  good_odd.count(true)
end
```

## Scala

```scala
object Solution {
    def oddEvenJumps(arr: Array[Int]): Int = {
        val n = arr.length
        if (n == 0) return 0

        val nextHigher = Array.fill(n)(-1)
        val nextLower = Array.fill(n)(-1)

        // Next higher jump indices
        val idxSorted = (0 until n).toArray.sortWith { (i, j) =>
            if (arr(i) != arr(j)) arr(i) < arr(j) else i < j
        }
        val stackHigher = new scala.collection.mutable.Stack[Int]()
        for (idx <- idxSorted) {
            while (stackHigher.nonEmpty && stackHigher.top < idx) {
                val prev = stackHigher.pop()
                nextHigher(prev) = idx
            }
            stackHigher.push(idx)
        }

        // Next lower jump indices
        val idxSortedDesc = (0 until n).toArray.sortWith { (i, j) =>
            if (arr(i) != arr(j)) arr(i) > arr(j) else i < j
        }
        val stackLower = new scala.collection.mutable.Stack[Int]()
        for (idx <- idxSortedDesc) {
            while (stackLower.nonEmpty && stackLower.top < idx) {
                val prev = stackLower.pop()
                nextLower(prev) = idx
            }
            stackLower.push(idx)
        }

        // DP tables: can reach end with odd/even jump from i
        val canOdd = Array.fill(n)(false)
        val canEven = Array.fill(n)(false)
        canOdd(n - 1) = true
        canEven(n - 1) = true

        for (i <- (n - 2) to 0 by -1) {
            if (nextHigher(i) != -1) canOdd(i) = canEven(nextHigher(i))
            if (nextLower(i) != -1) canEven(i) = canOdd(nextLower(i))
        }

        var count = 0
        for (i <- 0 until n) if (canOdd(i)) count += 1
        count
    }
}
```

## Rust

```rust
use std::cmp::Reverse;

impl Solution {
    pub fn odd_even_jumps(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        if n == 0 {
            return 0;
        }
        let mut next_higher: Vec<Option<usize>> = vec![None; n];
        let mut next_lower: Vec<Option<usize>> = vec![None; n];

        // Compute next higher jumps
        let mut order: Vec<usize> = (0..n).collect();
        order.sort_by_key(|&i| (arr[i], i));
        let mut stack: Vec<usize> = Vec::new();
        for &i in order.iter() {
            while let Some(&last) = stack.last() {
                if last < i {
                    next_higher[last] = Some(i);
                    stack.pop();
                } else {
                    break;
                }
            }
            stack.push(i);
        }

        // Compute next lower jumps
        let mut order_low: Vec<usize> = (0..n).collect();
        order_low.sort_by_key(|&i| (Reverse(arr[i]), i));
        stack.clear();
        for &i in order_low.iter() {
            while let Some(&last) = stack.last() {
                if last < i {
                    next_lower[last] = Some(i);
                    stack.pop();
                } else {
                    break;
                }
            }
            stack.push(i);
        }

        // DP to determine good starting indices
        let mut good_odd = vec![false; n];
        let mut good_even = vec![false; n];
        good_odd[n - 1] = true;
        good_even[n - 1] = true;

        for i in (0..n - 1).rev() {
            if let Some(j) = next_higher[i] {
                good_odd[i] = good_even[j];
            }
            if let Some(j) = next_lower[i] {
                good_even[i] = good_odd[j];
            }
        }

        good_odd.iter().filter(|&&b| b).count() as i32
    }
}
```

## Racket

```racket
(define/contract (odd-even-jumps arr)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length arr))
         (v (list->vector arr))
         (indices (for/list ([i (in-range n)]) i))
         (odd-sorted
          (sort indices
                (lambda (i j)
                  (or (< (vector-ref v i) (vector-ref v j))
                      (and (= (vector-ref v i) (vector-ref v j))
                           (< i j))))))
         (even-sorted
          (sort indices
                (lambda (i j)
                  (or (> (vector-ref v i) (vector-ref v j))
                      (and (= (vector-ref v i) (vector-ref v j))
                           (< i j))))))
         (odd-next
          (let ((next (make-vector n -1))
                (stack '()))
            (for ([idx odd-sorted])
              (let loop ()
                (when (and (not (null? stack)) (< (car stack) idx))
                  (vector-set! next (car stack) idx)
                  (set! stack (cdr stack))
                  (loop)))
              (set! stack (cons idx stack)))
            next))
         (even-next
          (let ((next (make-vector n -1))
                (stack '()))
            (for ([idx even-sorted])
              (let loop ()
                (when (and (not (null? stack)) (< (car stack) idx))
                  (vector-set! next (car stack) idx)
                  (set! stack (cdr stack))
                  (loop)))
              (set! stack (cons idx stack)))
            next))
         (can-odd (make-vector n #f))
         (can-even (make-vector n #f)))
    (when (> n 0)
      (vector-set! can-odd (- n 1) #t)
      (vector-set! can-even (- n 1) #t))
    (for ([i (in-range (- n 2) -1 -1)])
      (let ((oddIdx (vector-ref odd-next i))
            (evenIdx (vector-ref even-next i)))
        (when (>= oddIdx 0)
          (vector-set! can-odd i (vector-ref can-even oddIdx)))
        (when (>= evenIdx 0)
          (vector-set! can-even i (vector-ref can-odd evenIdx)))))
    (let ((cnt 0))
      (for ([i (in-range n)])
        (when (vector-ref can-odd i)
          (set! cnt (+ cnt 1))))
      cnt)))
```

## Erlang

```erlang
-module(solution).
-export([odd_even_jumps/1]).

-spec odd_even_jumps(Arr :: [integer()]) -> integer().
odd_even_jumps(Arr) ->
    N = length(Arr),
    Indices = lists:seq(0, N - 1),
    PairList = lists:zip(Arr, Indices),

    % next higher jumps
    SortedHigher = lists:sort(PairList),
    NextHigherMap = build_next_map(SortedHigher, #{}),

    % next lower jumps (use negative values for descending order)
    NegPairs = [{-V, Idx} || {V, Idx} <- PairList],
    SortedLower = lists:sort(NegPairs),
    NextLowerMap = build_next_map(SortedLower, #{}),

    % dynamic programming from right to left
    OMap0 = maps:put(N - 1, true, #{}),
    EMap0 = maps:put(N - 1, true, #{}),
    {OddMap, _EvenMap} = dp(N - 2, NextHigherMap, NextLowerMap, OMap0, EMap0),

    % count indices where odd jump can reach the end
    lists:foldl(
        fun({_Idx, true}, Acc) -> Acc + 1;
           (_, Acc) -> Acc
        end,
        0,
        maps:to_list(OddMap)
    ).

%% Build map of next index using monotonic stack technique.
build_next_map(SortedList, InitMap) ->
    build_next_map(SortedList, [], InitMap).

build_next_map([], _Stack, Map) -> Map;
build_next_map([{_Val, Idx} | Rest], Stack, Map) ->
    {NewStack, NewMap} = pop_set(Idx, Stack, Map),
    build_next_map(Rest, [Idx | NewStack], NewMap).

pop_set(_CurrentIdx, [], Map) -> {[], Map};
pop_set(CurrentIdx, [Top | Rest] = Stack, Map) when CurrentIdx > Top ->
    UpdatedMap = maps:put(Top, CurrentIdx, Map),
    pop_set(CurrentIdx, Rest, UpdatedMap);
pop_set(_CurrentIdx, Stack, Map) -> {Stack, Map}.

%% DP recursion.
dp(I, _NH, _NL, OMap, EMap) when I < 0 ->
    {OMap, EMap};
dp(I, NH, NL, OMap, EMap) ->
    OddVal = case maps:find(I, NH) of
                 {ok, J} -> maps:get(J, EMap, false);
                 error   -> false
             end,
    EvenVal = case maps:find(I, NL) of
                  {ok, J} -> maps:get(J, OMap, false);
                  error   -> false
              end,
    NewOMap = maps:put(I, OddVal, OMap),
    NewEMap = maps:put(I, EvenVal, EMap),
    dp(I - 1, NH, NL, NewOMap, NewEMap).
```

## Elixir

```elixir
defmodule Solution do
  @spec odd_even_jumps(arr :: [integer]) :: integer
  def odd_even_jumps(arr) do
    n = length(arr)

    pairs = Enum.with_index(arr) |> Enum.map(fn {v, i} -> {v, i} end)

    # next higher (odd jumps)
    sorted_higher = Enum.sort_by(pairs, fn {v, i} -> {v, i} end)

    {_stack_h, next_higher} =
      Enum.reduce(sorted_higher, {[], :array.new(n, default: -1)}, fn {_v, idx},
                                                                      {stack, a} ->
        {new_stack, new_a} = pop_and_set(stack, idx, a)
        {[idx | new_stack], new_a}
      end)

    # next lower (even jumps)
    sorted_lower = Enum.sort_by(pairs, fn {v, i} -> {-v, i} end)

    {_stack_l, next_lower} =
      Enum.reduce(sorted_lower, {[], :array.new(n, default: -1)}, fn {_v, idx},
                                                                      {stack, a} ->
        {new_stack, new_a} = pop_and_set(stack, idx, a)
        {[idx | new_stack], new_a}
      end)

    # DP arrays for odd/even reachability
    odd_arr = :array.set(n - 1, true, :array.new(n, default: false))
    even_arr = :array.set(n - 1, true, :array.new(n, default: false))

    indices =
      if n > 1 do
        Enum.to_list(0..(n - 2)) |> Enum.reverse()
      else
        []
      end

    {final_odd, _final_even} =
      Enum.reduce(indices, {odd_arr, even_arr}, fn i, {odd_a, even_a} ->
        odd_next = :array.get(i, next_higher)

        odd_val =
          if odd_next != -1 do
            :array.get(odd_next, even_a)
          else
            false
          end

        even_next = :array.get(i, next_lower)

        even_val =
          if even_next != -1 do
            :array.get(even_next, odd_a)
          else
            false
          end

        { :array.set(i, odd_val, odd_a), :array.set(i, even_val, even_a) }
      end)

    Enum.reduce(0..(n - 1), 0, fn i, acc ->
      if :array.get(i, final_odd), do: acc + 1, else: acc
    end)
  end

  defp pop_and_set([], _idx, arr), do: {[], arr}

  defp pop_and_set([top | rest] = stack, idx, arr) when idx > top do
    new_arr = :array.set(top, idx, arr)
    pop_and_set(rest, idx, new_arr)
  end

  defp pop_and_set(stack, _idx, arr), do: {stack, arr}
end
```
