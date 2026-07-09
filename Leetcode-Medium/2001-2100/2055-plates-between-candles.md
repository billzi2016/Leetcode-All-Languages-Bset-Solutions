# 2055. Plates Between Candles

## Cpp

```cpp
class Solution {
public:
    vector<int> platesBetweenCandles(string s, vector<vector<int>>& queries) {
        int n = s.size();
        vector<int> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = pref[i] + (s[i] == '*');
        }
        vector<int> leftCandle(n, -1), rightCandle(n, -1);
        int last = -1;
        for (int i = 0; i < n; ++i) {
            if (s[i] == '|') last = i;
            leftCandle[i] = last;
        }
        last = -1;
        for (int i = n - 1; i >= 0; --i) {
            if (s[i] == '|') last = i;
            rightCandle[i] = last;
        }
        vector<int> ans;
        ans.reserve(queries.size());
        for (auto& q : queries) {
            int l = q[0], r = q[1];
            int left = rightCandle[l];
            int right = leftCandle[r];
            if (left == -1 || right == -1 || left >= right) {
                ans.push_back(0);
            } else {
                ans.push_back(pref[right] - pref[left + 1]);
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int[] platesBetweenCandles(String s, int[][] queries) {
        int n = s.length();
        int[] pref = new int[n + 1];
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] + (s.charAt(i) == '*' ? 1 : 0);
        }
        int[] leftCandle = new int[n];
        int last = -1;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '|') last = i;
            leftCandle[i] = last;
        }
        int[] rightCandle = new int[n];
        last = -1;
        for (int i = n - 1; i >= 0; i--) {
            if (s.charAt(i) == '|') last = i;
            rightCandle[i] = last;
        }
        int m = queries.length;
        int[] ans = new int[m];
        for (int i = 0; i < m; i++) {
            int l = queries[i][0];
            int r = queries[i][1];
            int leftIdx = rightCandle[l];
            int rightIdx = leftCandle[r];
            if (leftIdx == -1 || rightIdx == -1 || leftIdx >= rightIdx) {
                ans[i] = 0;
            } else {
                ans[i] = pref[rightIdx + 1] - pref[leftIdx];
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def platesBetweenCandles(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(s)
        # prefix sum of plates '*'
        pref = [0] * (n + 1)
        for i, ch in enumerate(s):
            pref[i + 1] = pref[i] + (ch == '*')
        
        # nearest candle to the left (including self if candle)
        prev_candle = [-1] * n
        last = -1
        for i, ch in enumerate(s):
            if ch == '|':
                last = i
            prev_candle[i] = last
        
        # nearest candle to the right (including self if candle)
        next_candle = [-1] * n
        last = -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                last = i
            next_candle[i] = last
        
        ans = []
        for l, r in queries:
            left = next_candle[l]
            right = prev_candle[r]
            if left == -1 or right == -1 or left >= right:
                ans.append(0)
            else:
                ans.append(pref[right] - pref[left + 1])
        return ans
```

## Python3

```python
from typing import List

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        # Prefix sum of plates
        pref = [0] * (n + 1)
        for i, ch in enumerate(s):
            pref[i + 1] = pref[i] + (ch == '*')
        
        # Nearest candle to the left (including self)
        left_candle = [-1] * n
        last = -1
        for i, ch in enumerate(s):
            if ch == '|':
                last = i
            left_candle[i] = last
        
        # Nearest candle to the right (including self)
        right_candle = [-1] * n
        nxt = -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                nxt = i
            right_candle[i] = nxt
        
        ans = []
        for l, r in queries:
            left = right_candle[l]
            right = left_candle[r]
            if left == -1 or right == -1 or left >= right:
                ans.append(0)
            else:
                ans.append(pref[right] - pref[left + 1])
        return ans
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* platesBetweenCandles(char* s, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    int n = 0;
    while (s[n] != '\0') n++;
    
    // Prefix sum of plates
    int *pref = (int*)malloc((n + 1) * sizeof(int));
    pref[0] = 0;
    for (int i = 0; i < n; ++i) {
        pref[i + 1] = pref[i] + (s[i] == '*');
    }
    
    // Nearest candle to the left (including self)
    int *prevCandle = (int*)malloc(n * sizeof(int));
    int last = -1;
    for (int i = 0; i < n; ++i) {
        if (s[i] == '|') last = i;
        prevCandle[i] = last;
    }
    
    // Nearest candle to the right (including self)
    int *nextCandle = (int*)malloc(n * sizeof(int));
    int nxt = -1;
    for (int i = n - 1; i >= 0; --i) {
        if (s[i] == '|') nxt = i;
        nextCandle[i] = nxt;
    }
    
    int *ans = (int*)malloc(queriesSize * sizeof(int));
    for (int q = 0; q < queriesSize; ++q) {
        int l = queries[q][0];
        int r = queries[q][1];
        int left = nextCandle[l];
        int right = prevCandle[r];
        if (left == -1 || right == -1 || left >= right) {
            ans[q] = 0;
        } else {
            // plates between left and right candles, exclusive
            ans[q] = pref[right] - pref[left + 1];
        }
    }
    
    free(pref);
    free(prevCandle);
    free(nextCandle);
    
    *returnSize = queriesSize;
    return ans;
}
```

## Csharp

```csharp
using System;

public class Solution {
    public int[] PlatesBetweenCandles(string s, int[][] queries) {
        int n = s.Length;
        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + (s[i] == '*' ? 1 : 0);
        }

        int[] leftPrev = new int[n];
        int lastCandle = -1;
        for (int i = 0; i < n; i++) {
            if (s[i] == '|') lastCandle = i;
            leftPrev[i] = lastCandle;
        }

        int[] rightNext = new int[n];
        int nextCandle = -1;
        for (int i = n - 1; i >= 0; i--) {
            if (s[i] == '|') nextCandle = i;
            rightNext[i] = nextCandle;
        }

        int m = queries.Length;
        int[] answer = new int[m];
        for (int i = 0; i < m; i++) {
            int l = queries[i][0];
            int r = queries[i][1];

            int leftCandle = rightNext[l];
            int rightCandle = leftPrev[r];

            if (leftCandle == -1 || rightCandle == -1 || leftCandle >= rightCandle) {
                answer[i] = 0;
            } else {
                answer[i] = prefix[rightCandle] - prefix[leftCandle + 1];
            }
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number[][]} queries
 * @return {number[]}
 */
var platesBetweenCandles = function(s, queries) {
    const n = s.length;
    const prefix = new Array(n);
    for (let i = 0; i < n; ++i) {
        const add = s[i] === '*' ? 1 : 0;
        prefix[i] = (i > 0 ? prefix[i - 1] : 0) + add;
    }
    
    const prev = new Array(n);
    let last = -1;
    for (let i = 0; i < n; ++i) {
        if (s[i] === '|') last = i;
        prev[i] = last;
    }
    
    const next = new Array(n);
    let nxt = -1;
    for (let i = n - 1; i >= 0; --i) {
        if (s[i] === '|') nxt = i;
        next[i] = nxt;
    }
    
    const ans = new Array(queries.length);
    for (let q = 0; q < queries.length; ++q) {
        const [l, r] = queries[q];
        const leftCandle = next[l];
        const rightCandle = prev[r];
        if (leftCandle === -1 || rightCandle === -1 || leftCandle >= rightCandle) {
            ans[q] = 0;
        } else {
            ans[q] = prefix[rightCandle] - prefix[leftCandle];
        }
    }
    return ans;
};
```

## Typescript

```typescript
function platesBetweenCandles(s: string, queries: number[][]): number[] {
    const n = s.length;
    const pre = new Array<number>(n + 1).fill(0);
    for (let i = 0; i < n; ++i) {
        pre[i + 1] = pre[i] + (s[i] === '*' ? 1 : 0);
    }

    const nextCandle = new Array<number>(n).fill(-1);
    let nxt = -1;
    for (let i = n - 1; i >= 0; --i) {
        if (s[i] === '|') nxt = i;
        nextCandle[i] = nxt;
    }

    const prevCandle = new Array<number>(n).fill(-1);
    let prv = -1;
    for (let i = 0; i < n; ++i) {
        if (s[i] === '|') prv = i;
        prevCandle[i] = prv;
    }

    const ans: number[] = new Array<number>(queries.length);
    for (let i = 0; i < queries.length; ++i) {
        const left = queries[i][0];
        const right = queries[i][1];
        const lCand = nextCandle[left];
        const rCand = prevCandle[right];
        if (lCand === -1 || rCand === -1 || lCand >= rCand) {
            ans[i] = 0;
        } else {
            ans[i] = pre[rCand] - pre[lCand + 1];
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param String $s
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function platesBetweenCandles($s, $queries) {
        $n = strlen($s);
        // prefix sum of plates
        $pref = array_fill(0, $n + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $pref[$i + 1] = $pref[$i] + ($s[$i] === '*' ? 1 : 0);
        }

        // nearest candle to the right (including self)
        $nextCandle = array_fill(0, $n, -1);
        $next = -1;
        for ($i = $n - 1; $i >= 0; $i--) {
            if ($s[$i] === '|') {
                $next = $i;
            }
            $nextCandle[$i] = $next;
        }

        // nearest candle to the left (including self)
        $prevCandle = array_fill(0, $n, -1);
        $prev = -1;
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '|') {
                $prev = $i;
            }
            $prevCandle[$i] = $prev;
        }

        $ans = [];
        foreach ($queries as $q) {
            [$l, $r] = $q;
            $leftIdx  = $nextCandle[$l];
            $rightIdx = $prevCandle[$r];

            if ($leftIdx === -1 || $rightIdx === -1 || $leftIdx >= $rightIdx) {
                $ans[] = 0;
            } else {
                // plates strictly between leftIdx and rightIdx
                $plates = $pref[$rightIdx] - $pref[$leftIdx + 1];
                $ans[] = $plates;
            }
        }

        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func platesBetweenCandles(_ s: String, _ queries: [[Int]]) -> [Int] {
        let chars = Array(s)
        let n = chars.count
        var prefix = [Int](repeating: 0, count: n + 1)
        for i in 0..<n {
            prefix[i + 1] = prefix[i] + (chars[i] == "*" ? 1 : 0)
        }
        
        var leftCandle = [Int](repeating: -1, count: n)
        var last = -1
        for i in 0..<n {
            if chars[i] == "|" {
                last = i
            }
            leftCandle[i] = last
        }
        
        var rightCandle = [Int](repeating: -1, count: n)
        var next = -1
        for i in stride(from: n - 1, through: 0, by: -1) {
            if chars[i] == "|" {
                next = i
            }
            rightCandle[i] = next
        }
        
        var result = [Int]()
        result.reserveCapacity(queries.count)
        for q in queries {
            let l = q[0]
            let r = q[1]
            let leftIdx = rightCandle[l]
            let rightIdx = leftCandle[r]
            if leftIdx == -1 || rightIdx == -1 || leftIdx >= rightIdx {
                result.append(0)
            } else {
                let plates = prefix[rightIdx] - prefix[leftIdx + 1]
                result.append(plates)
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun platesBetweenCandles(s: String, queries: Array<IntArray>): IntArray {
        val n = s.length
        val prefix = IntArray(n + 1)
        for (i in 0 until n) {
            prefix[i + 1] = prefix[i] + if (s[i] == '*') 1 else 0
        }
        val prev = IntArray(n) { -1 }
        var last = -1
        for (i in 0 until n) {
            if (s[i] == '|') last = i
            prev[i] = last
        }
        val next = IntArray(n) { -1 }
        var nxt = -1
        for (i in n - 1 downTo 0) {
            if (s[i] == '|') nxt = i
            next[i] = nxt
        }
        val m = queries.size
        val ans = IntArray(m)
        for (idx in 0 until m) {
            val l = queries[idx][0]
            val r = queries[idx][1]
            val leftCandle = next[l]
            val rightCandle = prev[r]
            if (leftCandle == -1 || rightCandle == -1 || leftCandle >= rightCandle) {
                ans[idx] = 0
            } else {
                ans[idx] = prefix[rightCandle] - prefix[leftCandle + 1]
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> platesBetweenCandles(String s, List<List<int>> queries) {
    int n = s.length;
    // nearest candle on the left (including self)
    List<int> leftCandle = List.filled(n, -1);
    int last = -1;
    for (int i = 0; i < n; i++) {
      if (s[i] == '|') last = i;
      leftCandle[i] = last;
    }
    // nearest candle on the right (including self)
    List<int> rightCandle = List.filled(n, -1);
    last = -1;
    for (int i = n - 1; i >= 0; i--) {
      if (s[i] == '|') last = i;
      rightCandle[i] = last;
    }
    // prefix sum of plates '*'
    List<int> pref = List.filled(n + 1, 0);
    for (int i = 0; i < n; i++) {
      pref[i + 1] = pref[i] + (s[i] == '*' ? 1 : 0);
    }

    List<int> ans = [];
    for (var q in queries) {
      int l = q[0];
      int r = q[1];
      int lc = rightCandle[l]; // first candle >= l
      int rc = leftCandle[r];   // last candle <= r
      if (lc == -1 || rc == -1 || lc >= rc) {
        ans.add(0);
      } else {
        int plates = pref[rc] - pref[lc + 1];
        ans.add(plates);
      }
    }
    return ans;
  }
}
```

## Golang

```go
func platesBetweenCandles(s string, queries [][]int) []int {
	n := len(s)
	prefix := make([]int, n+1)

	// prefix sum of plates '*'
	for i := 0; i < n; i++ {
		prefix[i+1] = prefix[i]
		if s[i] == '*' {
			prefix[i+1]++
		}
	}

	// nearest candle to the left (including current)
	leftCandle := make([]int, n)
	last := -1
	for i := 0; i < n; i++ {
		if s[i] == '|' {
			last = i
		}
		leftCandle[i] = last
	}

	// nearest candle to the right (including current)
	rightCandle := make([]int, n)
	next := -1
	for i := n - 1; i >= 0; i-- {
		if s[i] == '|' {
			next = i
		}
		rightCandle[i] = next
	}

	ans := make([]int, len(queries))
	for idx, q := range queries {
		l, r := q[0], q[1]
		first := rightCandle[l] // first candle >= l
		last := leftCandle[r]   // last candle <= r

		if first == -1 || last == -1 || first >= last {
			ans[idx] = 0
		} else {
			ans[idx] = prefix[last+1] - prefix[first]
		}
	}
	return ans
}
```

## Ruby

```ruby
def plates_between_candles(s, queries)
  n = s.length
  prefix = Array.new(n + 1, 0)
  (0...n).each do |i|
    prefix[i + 1] = prefix[i] + (s[i] == '*' ? 1 : 0)
  end

  left_candle = Array.new(n, -1)
  last = -1
  (0...n).each do |i|
    last = i if s[i] == '|'
    left_candle[i] = last
  end

  right_candle = Array.new(n, -1)
  nxt = -1
  (n - 1).downto(0) do |i|
    nxt = i if s[i] == '|'
    right_candle[i] = nxt
  end

  ans = []
  queries.each do |l, r|
    left = right_candle[l]
    right = left_candle[r]
    if left == -1 || right == -1 || left >= right
      ans << 0
    else
      ans << (prefix[right] - prefix[left + 1])
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def platesBetweenCandles(s: String, queries: Array[Array[Int]]): Array[Int] = {
        val n = s.length
        // Prefix sum of plates '*'
        val prefix = new Array[Int](n + 1)
        var i = 0
        while (i < n) {
            prefix(i + 1) = prefix(i) + (if (s.charAt(i) == '*') 1 else 0)
            i += 1
        }

        // nearest candle at or after each position
        val nextCandle = new Array[Int](n)
        var next = -1
        i = n - 1
        while (i >= 0) {
            if (s.charAt(i) == '|') next = i
            nextCandle(i) = next
            i -= 1
        }

        // nearest candle at or before each position
        val prevCandle = new Array[Int](n)
        var prev = -1
        i = 0
        while (i < n) {
            if (s.charAt(i) == '|') prev = i
            prevCandle(i) = prev
            i += 1
        }

        val ans = new Array[Int](queries.length)
        var qIdx = 0
        while (qIdx < queries.length) {
            val l = queries(qIdx)(0)
            val r = queries(qIdx)(1)
            val leftC = nextCandle(l)
            val rightC = prevCandle(r)

            if (leftC == -1 || rightC == -1 || leftC >= rightC) {
                ans(qIdx) = 0
            } else {
                ans(qIdx) = prefix(rightC) - prefix(leftC + 1)
            }
            qIdx += 1
        }

        ans
    }
}
```

## Rust

```rust
impl Solution {
    pub fn plates_between_candles(s: String, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let bytes = s.as_bytes();
        let n = bytes.len();

        // Prefix sum of plates ('*')
        let mut pref = vec![0usize; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + if bytes[i] == b'*' { 1 } else { 0 };
        }

        // Nearest candle to the left (including self)
        let mut prev = vec![n; n];
        let mut last = n;
        for i in 0..n {
            if bytes[i] == b'|' {
                last = i;
            }
            prev[i] = last;
        }

        // Nearest candle to the right (including self)
        let mut next = vec![n; n];
        let mut nxt = n;
        for i in (0..n).rev() {
            if bytes[i] == b'|' {
                nxt = i;
            }
            next[i] = nxt;
        }

        let mut ans = Vec::with_capacity(queries.len());
        for q in queries.iter() {
            let l = q[0] as usize;
            let r = q[1] as usize;

            let left_candle = if l < n { next[l] } else { n };
            let right_candle = if r < n { prev[r] } else { n };

            if left_candle == n || right_candle == n || left_candle >= right_candle {
                ans.push(0);
            } else {
                // plates between (left_candle, right_candle)
                let plates = pref[right_candle] - pref[left_candle + 1];
                ans.push(plates as i32);
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (plates-between-candles s queries)
  (-> string? (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ([n (string-length s)]
         [prefix (make-vector (+ n 1) 0)]
         [leftCandle (make-vector n -1)]
         [rightCandle (make-vector n -1)])
    ;; build prefix sum of plates
    (for ([i (in-range n)])
      (define prev (vector-ref prefix i))
      (vector-set! prefix (add1 i)
                   (+ prev (if (char=? (string-ref s i) #\*)
                              1
                              0))))
    ;; nearest candle to the left (including self)
    (let ([last -1])
      (for ([i (in-range n)])
        (when (char=? (string-ref s i) #\|)
          (set! last i))
        (vector-set! leftCandle i last)))
    ;; nearest candle to the right (including self)
    (let ([next -1])
      (for ([i (in-range (sub1 n) -1 -1)])
        (when (char=? (string-ref s i) #\|)
          (set! next i))
        (vector-set! rightCandle i next)))
    ;; answer queries
    (map (lambda (qr)
           (define l (first qr))
           (define r (second qr))
           (define left-idx (vector-ref rightCandle l))   ; first candle ≥ l
           (define right-idx (vector-ref leftCandle r))   ; last candle ≤ r
           (if (or (= left-idx -1)
                   (= right-idx -1)
                   (>= left-idx right-idx))
               0
               (- (vector-ref prefix right-idx)
                  (vector-ref prefix (+ left-idx 1)))))
         queries)))
```

## Erlang

```erlang
-spec plates_between_candles(S :: unicode:unicode_binary(), Queries :: [[integer()]]) -> [integer()].
plates_between_candles(S, Queries) ->
    Len = byte_size(S),
    StrList = binary_to_list(S),

    %% prefix sum of plates
    {_, _, PrefRev} =
        lists:foldl(
            fun(Char, {Idx, Sum, Acc}) ->
                NewSum = case Char of $* -> Sum + 1; _ -> Sum end,
                {Idx + 1, NewSum, [NewSum | Acc]}
            end,
            {0, 0, []},
            StrList),
    PrefTuple = list_to_tuple([0 | lists:reverse(PrefRev)]),   % size Len+1

    %% nearest candle to the left (including itself)
    {_, _, LeftRev} =
        lists:foldl(
            fun(Char, {Idx, LastCandle, Acc}) ->
                NewLast = case Char of $| -> Idx; _ -> LastCandle end,
                {Idx + 1, NewLast, [NewLast | Acc]}
            end,
            {0, -1, []},
            StrList),
    LeftTuple = list_to_tuple(lists:reverse(LeftRev)),        % size Len

    %% nearest candle to the right (including itself)
    RevStr = lists:reverse(StrList),
    {_, _, RevRightRev} =
        lists:foldl(
            fun(Char, {Idx, LastCandle, Acc}) ->
                NewLast = case Char of $| -> Idx; _ -> LastCandle end,
                {Idx + 1, NewLast, [NewLast | Acc]}
            end,
            {0, -1, []},
            RevStr),
    %% convert reversed indices to original positions
    RightList =
        [case V of
             -1 -> -1;
             _ -> Len - 1 - V
         end || V <- RevRightRev],
    RightTuple = list_to_tuple(RightList),                    % size Len

    %% answer each query
    lists:map(
      fun([L, R]) ->
          LeftC = element(L + 1, RightTuple),
          RightC = element(R + 1, LeftTuple),
          case (LeftC == -1) orelse (RightC == -1) orelse (LeftC >= RightC) of
              true -> 0;
              false ->
                  PlatesRight = element(RightC + 1, PrefTuple),
                  PlatesLeft = element(LeftC + 2, PrefTuple),
                  PlatesRight - PlatesLeft
          end
      end,
      Queries).
```

## Elixir

```elixir
defmodule Solution do
  @spec plates_between_candles(s :: String.t(), queries :: [[integer]]) :: [integer]
  def plates_between_candles(s, queries) do
    bytes = :binary.bin_to_list(s)
    n = length(bytes)

    # Forward pass: prefix sum of plates and nearest candle on the left
    {pref_rev, prev_rev, _cnt, _last} =
      Enum.reduce(Enum.with_index(bytes), {[], [], 0, -1}, fn {c, i},
          {pref_acc, prev_acc, cnt, last_candle} ->
        new_cnt = if c == ?*, do: cnt + 1, else: cnt
        pref_acc2 = [new_cnt | pref_acc]
        new_last = if c == ?|, do: i, else: last_candle
        prev_acc2 = [new_last | prev_acc]
        {pref_acc2, prev_acc2, new_cnt, new_last}
      end)

    prefix = List.to_tuple(Enum.reverse(pref_rev))
    prev_candle = List.to_tuple(Enum.reverse(prev_rev))

    # Convert bytes to tuple for O(1) access in backward pass
    char_tuple = List.to_tuple(bytes)

    # Backward pass: nearest candle on the right
    {next_rev, _} =
      Enum.reduce(0..(n - 1), {[], n}, fn offset, {acc, nxt} ->
        i = n - 1 - offset
        c = elem(char_tuple, i)
        new_nxt = if c == ?|, do: i, else: nxt
        {[new_nxt | acc], new_nxt}
      end)

    next_candle = List.to_tuple(next_rev)

    # Answer each query
    Enum.map(queries, fn [l, r] ->
      left = elem(next_candle, l)
      right = elem(prev_candle, r)

      if left == n or right == -1 or left >= right do
        0
      else
        elem(prefix, right) - elem(prefix, left)
      end
    end)
  end
end
```
