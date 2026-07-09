# 1850. Minimum Adjacent Swaps to Reach the Kth Smallest Number

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int getMinSwaps(string num, int k) {
        string target = num;
        for (int i = 0; i < k; ++i) {
            next_permutation(target.begin(), target.end());
        }
        long long swaps = 0;
        string cur = num;
        int n = cur.size();
        for (int i = 0; i < n; ++i) {
            if (cur[i] == target[i]) continue;
            int j = i + 1;
            while (j < n && cur[j] != target[i]) ++j;
            while (j > i) {
                swap(cur[j], cur[j - 1]);
                ++swaps;
                --j;
            }
        }
        return static_cast<int>(swaps);
    }
};
```

## Java

```java
class Solution {
    public int getMinSwaps(String num, int k) {
        char[] target = num.toCharArray();
        // generate kth next permutation
        for (int step = 0; step < k; step++) {
            nextPermutation(target);
        }
        char[] source = num.toCharArray();
        int n = source.length;
        int swaps = 0;
        for (int i = 0; i < n; i++) {
            if (source[i] == target[i]) continue;
            int j = i + 1;
            while (j < n && source[j] != target[i]) {
                j++;
            }
            // bring the character at j to position i
            while (j > i) {
                char tmp = source[j];
                source[j] = source[j - 1];
                source[j - 1] = tmp;
                swaps++;
                j--;
            }
        }
        return swaps;
    }

    private void nextPermutation(char[] arr) {
        int n = arr.length;
        int i = n - 2;
        while (i >= 0 && arr[i] >= arr[i + 1]) {
            i--;
        }
        if (i < 0) return; // no further permutation, but problem guarantees existence
        int j = n - 1;
        while (arr[j] <= arr[i]) {
            j--;
        }
        swap(arr, i, j);
        reverse(arr, i + 1, n - 1);
    }

    private void swap(char[] arr, int i, int j) {
        char tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    private void reverse(char[] arr, int l, int r) {
        while (l < r) {
            swap(arr, l++, r--);
        }
    }
}
```

## Python

```python
class Solution(object):
    def getMinSwaps(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: int
        """
        def next_permutation(arr):
            i = len(arr) - 2
            while i >= 0 and arr[i] >= arr[i + 1]:
                i -= 1
            if i == -1:
                return
            j = len(arr) - 1
            while arr[j] <= arr[i]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
            l, r = i + 1, len(arr) - 1
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        original = list(num)
        target = original[:]
        for _ in range(k):
            next_permutation(target)

        cur = original[:]
        swaps = 0
        n = len(cur)
        for i in range(n):
            if cur[i] == target[i]:
                continue
            j = i + 1
            while cur[j] != target[i]:
                j += 1
            while j > i:
                cur[j], cur[j - 1] = cur[j - 1], cur[j]
                swaps += 1
                j -= 1
        return swaps
```

## Python3

```python
class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def next_permutation(arr):
            i = len(arr) - 2
            while i >= 0 and arr[i] >= arr[i + 1]:
                i -= 1
            if i == -1:
                return False
            j = len(arr) - 1
            while arr[j] <= arr[i]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1:] = reversed(arr[i + 1:])
            return True

        orig = list(num)
        target = orig[:]
        for _ in range(k):
            next_permutation(target)

        s = orig[:]
        swaps = 0
        n = len(s)
        for i in range(n):
            if s[i] == target[i]:
                continue
            j = i + 1
            while j < n and s[j] != target[i]:
                j += 1
            while j > i:
                s[j], s[j - 1] = s[j - 1], s[j]
                swaps += 1
                j -= 1
        return swaps
```

## C

```c
#include <stdlib.h>
#include <string.h>

static char* strDup(const char *s) {
    size_t len = strlen(s);
    char *p = (char*)malloc(len + 1);
    if (p) memcpy(p, s, len + 1);
    return p;
}

int getMinSwaps(char* num, int k) {
    int n = (int)strlen(num);
    char *orig = strDup(num);
    char *target = strDup(num);

    for (int step = 0; step < k; ++step) {
        int i = n - 2;
        while (i >= 0 && target[i] >= target[i + 1]) --i;
        if (i < 0) break; // no further permutation, shouldn't happen per constraints

        int j = n - 1;
        while (target[j] <= target[i]) --j;

        char tmp = target[i];
        target[i] = target[j];
        target[j] = tmp;

        int l = i + 1, r = n - 1;
        while (l < r) {
            char t2 = target[l];
            target[l++] = target[r];
            target[r--] = t2;
        }
    }

    long long swaps = 0;
    for (int i = 0; i < n; ++i) {
        if (orig[i] == target[i]) continue;
        int j = i + 1;
        while (j < n && orig[j] != target[i]) ++j;
        while (j > i) {
            char t2 = orig[j - 1];
            orig[j - 1] = orig[j];
            orig[j] = t2;
            ++swaps;
            --j;
        }
    }

    free(orig);
    free(target);
    return (int)swaps;
}
```

## Csharp

```csharp
public class Solution
{
    public int GetMinSwaps(string num, int k)
    {
        char[] cur = num.ToCharArray();
        for (int repeat = 0; repeat < k; ++repeat)
            NextPermutation(cur);

        char[] target = cur;
        char[] orig = num.ToCharArray();

        int swaps = 0;
        int n = orig.Length;

        for (int i = 0; i < n; i++)
        {
            if (orig[i] == target[i]) continue;

            int j = i + 1;
            while (j < n && orig[j] != target[i]) j++;

            while (j > i)
            {
                char tmp = orig[j];
                orig[j] = orig[j - 1];
                orig[j - 1] = tmp;
                swaps++;
                j--;
            }
        }

        return swaps;
    }

    private void NextPermutation(char[] arr)
    {
        int n = arr.Length;
        int i = n - 2;
        while (i >= 0 && arr[i] >= arr[i + 1]) i--;

        // problem guarantees a next permutation exists
        int j = n - 1;
        while (arr[j] <= arr[i]) j--;

        char tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;

        int left = i + 1, right = n - 1;
        while (left < right)
        {
            char t = arr[left];
            arr[left] = arr[right];
            arr[right] = t;
            left++;
            right--;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string} num
 * @param {number} k
 * @return {number}
 */
var getMinSwaps = function(num, k) {
    // Helper to compute next permutation in-place (array of chars)
    const nextPermutation = (arr) => {
        let i = arr.length - 2;
        while (i >= 0 && arr[i] >= arr[i + 1]) i--;
        if (i < 0) return; // already highest, but problem guarantees existence
        let j = arr.length - 1;
        while (arr[j] <= arr[i]) j--;
        [arr[i], arr[j]] = [arr[j], arr[i]];
        // reverse suffix i+1..end
        let left = i + 1, right = arr.length - 1;
        while (left < right) {
            [arr[left], arr[right]] = [arr[right], arr[left]];
            left++;
            right--;
        }
    };
    
    const original = num.split('');
    const curPerm = original.slice();
    for (let t = 0; t < k; ++t) {
        nextPermutation(curPerm);
    }
    const target = curPerm;
    
    // Compute minimal adjacent swaps to transform original into target
    let swaps = 0;
    const cur = original.slice(); // mutable copy
    const n = cur.length;
    for (let i = 0; i < n; ++i) {
        if (cur[i] === target[i]) continue;
        let j = i + 1;
        while (j < n && cur[j] !== target[i]) j++;
        // bring element at j to position i
        while (j > i) {
            [cur[j], cur[j - 1]] = [cur[j - 1], cur[j]];
            swaps++;
            j--;
        }
    }
    return swaps;
};
```

## Typescript

```typescript
function getMinSwaps(num: string, k: number): number {
    const n = num.length;
    // compute kth next permutation
    const targetArr = num.split('');
    for (let step = 0; step < k; ++step) {
        nextPermutation(targetArr);
    }

    const source = num.split('');
    let swaps = 0;

    for (let i = 0; i < n; ++i) {
        if (source[i] === targetArr[i]) continue;
        let j = i + 1;
        while (j < n && source[j] !== targetArr[i]) j++;
        // bring character at j to position i
        while (j > i) {
            [source[j], source[j - 1]] = [source[j - 1], source[j]];
            swaps++;
            j--;
        }
    }

    return swaps;
}

function nextPermutation(arr: string[]): void {
    let i = arr.length - 2;
    while (i >= 0 && arr[i] >= arr[i + 1]) i--;
    if (i < 0) return; // highest permutation, not expected per constraints

    let j = arr.length - 1;
    while (arr[j] <= arr[i]) j--;

    [arr[i], arr[j]] = [arr[j], arr[i]];

    let left = i + 1,
        right = arr.length - 1;
    while (left < right) {
        [arr[left], arr[right]] = [arr[right], arr[left]];
        left++;
        right--;
    }
}
```

## Php

```php
class Solution {

    /**
     * @param String $num
     * @param Integer $k
     * @return Integer
     */
    function getMinSwaps($num, $k) {
        $source = str_split($num);
        $target = $source;

        // generate kth next permutation
        for ($cnt = 0; $cnt < $k; $cnt++) {
            $this->nextPermutation($target);
        }

        $swaps = 0;
        $n = count($source);
        for ($i = 0; $i < $n; $i++) {
            if ($source[$i] === $target[$i]) continue;

            // find the position of the needed digit
            $j = $i + 1;
            while ($j < $n && $source[$j] !== $target[$i]) {
                $j++;
            }

            // bring it to position i by adjacent swaps
            while ($j > $i) {
                $tmp = $source[$j];
                $source[$j] = $source[$j - 1];
                $source[$j - 1] = $tmp;
                $j--;
                $swaps++;
            }
        }

        return $swaps;
    }

    private function nextPermutation(&$arr) {
        $n = count($arr);
        // find first decreasing element from the right
        for ($i = $n - 2; $i >= 0; $i--) {
            if ($arr[$i] < $arr[$i + 1]) {
                break;
            }
        }
        if ($i < 0) return false; // already highest permutation

        // find element just larger than arr[i] to the right
        for ($j = $n - 1; $j > $i; $j--) {
            if ($arr[$j] > $arr[$i]) {
                break;
            }
        }

        // swap them
        $tmp = $arr[$i];
        $arr[$i] = $arr[$j];
        $arr[$j] = $tmp;

        // reverse the suffix starting at i+1
        $left = $i + 1;
        $right = $n - 1;
        while ($left < $right) {
            $tmp = $arr[$left];
            $arr[$left] = $arr[$right];
            $arr[$right] = $tmp;
            $left++;
            $right--;
        }
        return true;
    }
}
```

## Swift

```swift
class Solution {
    func getMinSwaps(_ num: String, _ k: Int) -> Int {
        var target = Array(num)
        for _ in 0..<k {
            _ = nextPermutation(&target)
        }
        var original = Array(num)
        let n = original.count
        var swaps = 0
        for i in 0..<n {
            if original[i] == target[i] { continue }
            var j = i + 1
            while j < n && original[j] != target[i] {
                j += 1
            }
            while j > i {
                original.swapAt(j, j - 1)
                swaps += 1
                j -= 1
            }
        }
        return swaps
    }

    private func nextPermutation(_ nums: inout [Character]) -> Bool {
        let n = nums.count
        var i = n - 2
        while i >= 0 && nums[i] >= nums[i + 1] {
            i -= 1
        }
        if i < 0 { return false }
        var j = n - 1
        while nums[j] <= nums[i] {
            j -= 1
        }
        nums.swapAt(i, j)
        var left = i + 1
        var right = n - 1
        while left < right {
            nums.swapAt(left, right)
            left += 1
            right -= 1
        }
        return true
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun getMinSwaps(num: String, k: Int): Int {
        val n = num.length
        // Generate kth next permutation
        val targetArr = num.toCharArray()
        repeat(k) { nextPermutation(targetArr) }
        val target = String(targetArr)

        // Compute minimum adjacent swaps to transform original into target
        val cur = num.toCharArray()
        var swaps = 0
        for (i in 0 until n) {
            if (cur[i] == target[i]) continue
            var j = i + 1
            while (j < n && cur[j] != target[i]) {
                j++
            }
            // Bring character at position j to i by swapping leftwards
            while (j > i) {
                val tmp = cur[j]
                cur[j] = cur[j - 1]
                cur[j - 1] = tmp
                swaps++
                j--
            }
        }
        return swaps
    }

    private fun nextPermutation(arr: CharArray) {
        var i = arr.size - 2
        while (i >= 0 && arr[i] >= arr[i + 1]) {
            i--
        }
        if (i < 0) return // already highest permutation, shouldn't happen per problem guarantees

        var j = arr.size - 1
        while (arr[j] <= arr[i]) {
            j--
        }
        // swap i and j
        val tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

        // reverse from i+1 to end
        var left = i + 1
        var right = arr.size - 1
        while (left < right) {
            val t = arr[left]
            arr[left] = arr[right]
            arr[right] = t
            left++
            right--
        }
    }
}
```

## Dart

```dart
class Solution {
  int getMinSwaps(String num, int k) {
    List<String> original = num.split('');
    List<String> cur = List.from(original);
    int n = cur.length;

    // Generate the kth next permutation
    for (int step = 0; step < k; ++step) {
      // Find first decreasing element from the right
      int i = n - 2;
      while (i >= 0 && cur[i].compareTo(cur[i + 1]) >= 0) {
        i--;
      }
      // Since kth wonderful number exists, i will be valid
      int j = n - 1;
      while (cur[j].compareTo(cur[i]) <= 0) {
        j--;
      }
      // Swap i and j
      String tmp = cur[i];
      cur[i] = cur[j];
      cur[j] = tmp;

      // Reverse the suffix starting at i+1
      int left = i + 1, right = n - 1;
      while (left < right) {
        String t = cur[left];
        cur[left] = cur[right];
        cur[right] = t;
        left++;
        right--;
      }
    }

    List<String> target = cur;

    // Count minimum adjacent swaps to transform original into target
    int swaps = 0;
    List<String> arr = List.from(original);
    for (int i = 0; i < n; ++i) {
      if (arr[i] == target[i]) continue;
      int j = i + 1;
      while (j < n && arr[j] != target[i]) {
        j++;
      }
      // Bring the matching digit to position i
      while (j > i) {
        String t = arr[j];
        arr[j] = arr[j - 1];
        arr[j - 1] = t;
        swaps++;
        j--;
      }
    }

    return swaps;
  }
}
```

## Golang

```go
package main

func getMinSwaps(num string, k int) int {
	orig := []byte(num)
	cur := make([]byte, len(orig))
	copy(cur, orig)

	for i := 0; i < k; i++ {
		nextPermutation(cur)
	}
	return minAdjacentSwaps(orig, cur)
}

func nextPermutation(a []byte) {
	n := len(a)
	i := n - 2
	for i >= 0 && a[i] >= a[i+1] {
		i--
	}
	if i >= 0 {
		j := n - 1
		for a[j] <= a[i] {
			j--
		}
		a[i], a[j] = a[j], a[i]
	}
	// reverse suffix starting at i+1
	l, r := i+1, n-1
	for l < r {
		a[l], a[r] = a[r], a[l]
		l++
		r--
	}
}

func minAdjacentSwaps(orig, target []byte) int {
	n := len(orig)
	swaps := 0
	for i := 0; i < n; i++ {
		if orig[i] == target[i] {
			continue
		}
		j := i + 1
		for j < n && orig[j] != target[i] {
			j++
		}
		for j > i {
			orig[j], orig[j-1] = orig[j-1], orig[j]
			swaps++
			j--
		}
	}
	return swaps
}
```

## Ruby

```ruby
def next_permutation(arr)
  i = arr.length - 2
  while i >= 0 && arr[i] >= arr[i + 1]
    i -= 1
  end
  return false if i < 0

  j = arr.length - 1
  while arr[j] <= arr[i]
    j -= 1
  end
  arr[i], arr[j] = arr[j], arr[i]

  left = i + 1
  right = arr.length - 1
  while left < right
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
  end
  true
end

# @param {String} num
# @param {Integer} k
# @return {Integer}
def get_min_swaps(num, k)
  original = num.chars
  target = original.clone

  k.times { next_permutation(target) }

  arr = original.clone
  swaps = 0
  n = arr.length

  (0...n).each do |i|
    next if arr[i] == target[i]

    j = i + 1
    j += 1 while j < n && arr[j] != target[i]

    while j > i
      arr[j], arr[j - 1] = arr[j - 1], arr[j]
      swaps += 1
      j -= 1
    end
  end

  swaps
end
```

## Scala

```scala
object Solution {
    def getMinSwaps(num: String, k: Int): Int = {
        val original = num.toCharArray
        var perm = num.toCharArray

        // generate the kth next permutation
        for (_ <- 0 until k) {
            nextPermutation(perm)
        }
        val target = perm.clone()

        minSwaps(original, target)
    }

    private def nextPermutation(a: Array[Char]): Unit = {
        var i = a.length - 2
        while (i >= 0 && a(i) >= a(i + 1)) i -= 1

        if (i >= 0) {
            var j = a.length - 1
            while (a(j) <= a(i)) j -= 1
            val tmp = a(i)
            a(i) = a(j)
            a(j) = tmp
        }

        var l = i + 1
        var r = a.length - 1
        while (l < r) {
            val tmp = a(l)
            a(l) = a(r)
            a(r) = tmp
            l += 1
            r -= 1
        }
    }

    private def minSwaps(original: Array[Char], target: Array[Char]): Int = {
        val cur = original.clone()
        var swaps = 0
        val n = cur.length

        for (i <- 0 until n) {
            if (cur(i) != target(i)) {
                var j = i + 1
                while (j < n && cur(j) != target(i)) j += 1
                while (j > i) {
                    val tmp = cur(j)
                    cur(j) = cur(j - 1)
                    cur(j - 1) = tmp
                    swaps += 1
                    j -= 1
                }
            }
        }
        swaps
    }
}
```

## Rust

```rust
impl Solution {
    pub fn get_min_swaps(num: String, k: i32) -> i32 {
        let mut original: Vec<char> = num.chars().collect();
        let mut target = original.clone();

        for _ in 0..k {
            Self::next_permutation(&mut target);
        }

        let n = original.len();
        let mut cur = original;
        let mut swaps: i32 = 0;

        for i in 0..n {
            if cur[i] == target[i] {
                continue;
            }
            let mut j = i + 1;
            while j < n && cur[j] != target[i] {
                j += 1;
            }
            while j > i {
                cur.swap(j, j - 1);
                swaps += 1;
                j -= 1;
            }
        }

        swaps
    }

    fn next_permutation(arr: &mut Vec<char>) {
        let n = arr.len();
        if n < 2 {
            return;
        }
        // Find the first index i from the right such that arr[i] < arr[i + 1]
        let mut i_opt = None;
        for i in (0..n - 1).rev() {
            if arr[i] < arr[i + 1] {
                i_opt = Some(i);
                break;
            }
        }

        if let Some(i) = i_opt {
            // Find the smallest element greater than arr[i] to the right
            let mut j = n - 1;
            while arr[j] <= arr[i] {
                j -= 1;
            }
            arr.swap(i, j);
            // Reverse the suffix starting at i + 1
            arr[i + 1..].reverse();
        } else {
            // Entire array is non-increasing; reverse to get smallest permutation
            arr.reverse();
        }
    }
}
```

## Racket

```racket
(define/contract (get-min-swaps num k)
  (-> string? exact-integer? exact-integer?)
  (let* ([n (string-length num)]
         [orig (list->vector (string->list num))]
         [target (list->vector (string->list num))])
    ;; swap two positions in a vector
    (define (swap! v i j)
      (let ((tmp (vector-ref v i)))
        (vector-set! v i (vector-ref v j))
        (vector-set! v j tmp)))
    ;; generate next permutation in place
    (define (next-permutation! v)
      (let* ([len (vector-length v)]
             [i (let loop ((idx (- len 2)))
                  (if (< idx 0) -1
                      (if (char<? (vector-ref v idx) (vector-ref v (+ idx 1)))
                          idx
                          (loop (- idx 1)))) )])
        (when (>= i 0)
          (let ([j (let loop ((idx (- len 1)))
                     (if (char>? (vector-ref v idx) (vector-ref v i))
                         idx
                         (loop (- idx 1))))])
            (swap! v i j)
            ;; reverse suffix after i
            (let rev-loop ((l (+ i 1)) (r (- len 1)))
              (when (< l r)
                (swap! v l r)
                (rev-loop (+ l 1) (- r 1))))))))
    ;; apply next permutation k times to obtain the target wonderful number
    (for ([cnt (in-range k)])
      (next-permutation! target))
    ;; compute minimal adjacent swaps from original to target
    (define source (list->vector (string->list num)))
    (define swaps 0)
    (for ([i (in-range n)])
      (when (not (char=? (vector-ref source i) (vector-ref target i)))
        (let find ((j (+ i 1)))
          (if (char=? (vector-ref source j) (vector-ref target i))
              (let move ((pos j))
                (when (> pos i)
                  (swap! source pos (- pos 1))
                  (set! swaps (+ swaps 1))
                  (move (- pos 1))))
              (find (+ j 1))))))
    swaps))
```

## Erlang

```erlang
-module(solution).
-export([get_min_swaps/2]).

-spec get_min_swaps(Num :: unicode:unicode_binary(), K :: integer()) -> integer().
get_min_swaps(Num, K) ->
    Orig = binary_to_list(Num),
    Target = kth_permutation(Orig, K),
    min_swaps(Orig, Target).

%% Apply next permutation K times
kth_permutation(L, 0) -> L;
kth_permutation(L, K) ->
    kth_permutation(next_perm(L), K - 1).

%% Compute next lexicographic permutation of a list of integers (digits)
next_perm(L) ->
    Rev = lists:reverse(L),
    {PrefixRev, Pivot, Suffix} = find_pivot(Rev, []),
    Prefix = lists:reverse(PrefixRev),
    RevSuffix = lists:reverse(Suffix),               % ascending order
    {Succ, RevRest} = pick_successor(Pivot, RevSuffix),
    SuffixMinusSucc = lists:reverse(RevRest),       % still descending
    Remaining = SuffixMinusSucc ++ [Pivot],
    NewSuffix = lists:reverse(Remaining),           % ascending after reversal
    Prefix ++ [Succ] ++ NewSuffix.

%% Find pivot in reversed list; returns {PrefixRev, Pivot, Suffix}
find_pivot([X|Rest], Acc) ->
    case Acc of
        [] -> find_pivot(Rest, [X]);
        [Prev|_] when X >= Prev -> find_pivot(Rest, [X|Acc]);
        _ -> {Rest, X, Acc}
    end.

%% From ascending list (RevSuffix), pick smallest element > Pivot and return rest list
pick_successor(Pivot, [H|T]) ->
    if H > Pivot ->
            {H, T};
       true ->
            {Succ, Rest} = pick_successor(Pivot, T),
            {Succ, [H|Rest]}
    end.

%% Minimum adjacent swaps to transform Orig into Target
min_swaps(Orig, Target) -> min_swaps(0, Orig, Target).

min_swaps(I, Curr, Target) ->
    Len = length(Curr),
    if I >= Len -> 0;
       true ->
            Desired = lists:nth(I + 1, Target),
            case lists:nth(I + 1, Curr) of
                Desired ->
                    min_swaps(I + 1, Curr, Target);
                _ ->
                    J = find_pos(Curr, Desired, I + 1),
                    Swaps = J - I,
                    NewCurr = move_elem(Curr, I, J),
                    Sw = min_swaps(I + 1, NewCurr, Target),
                    Swaps + Sw
            end
    end.

%% Find position (0‑based) of Val starting from IndexStart
find_pos([H|T], Val, Idx) ->
    if H == Val -> Idx;
       true -> find_pos(T, Val, Idx + 1)
    end.

%% Move element at FromIdx left to ToIdx by adjacent swaps
move_elem(List, ToIdx, FromIdx) when FromIdx > ToIdx ->
    {Prefix, Rest1} = split_at(ToIdx, List),
    LenMid = FromIdx - ToIdx,
    {MidWithElem, Rest2} = split_at(LenMid, Rest1),
    Elem = lists:last(MidWithElem),
    MidLen = length(MidWithElem) - 1,
    Mid = case MidLen of
              0 -> [];
              _ -> lists:sublist(MidWithElem, 1, MidLen)
          end,
    Prefix ++ [Elem] ++ Mid ++ Rest2.

%% Split list at N (first N elements), returns {FirstN, Rest}
split_at(0, L) -> {[], L};
split_at(N, [H|T]) when N > 0 ->
    {Pref, Rest} = split_at(N - 1, T),
    {[H|Pref], Rest}.
```

## Elixir

```elixir
defmodule Solution do
  @spec get_min_swaps(num :: String.t(), k :: integer) :: integer
  def get_min_swaps(num, k) do
    chars = String.graphemes(num)
    target = kth_permutation(chars, k)
    min_swaps(chars, target)
  end

  # ---------- kth permutation ----------
  defp kth_permutation(chars, 0), do: chars

  defp kth_permutation(chars, k) do
    next = next_permutation(chars)
    kth_permutation(next, k - 1)
  end

  # ---------- next permutation ----------
  defp next_permutation(chars) do
    n = length(chars)
    i = find_i(chars, n - 2)

    j = find_j(chars, i, n - 1)

    swapped = swap(chars, i, j)
    reverse_suffix(swapped, i + 1)
  end

  defp find_i(_chars, -1), do: -1

  defp find_i(chars, idx) do
    if Enum.at(chars, idx) < Enum.at(chars, idx + 1) do
      idx
    else
      find_i(chars, idx - 1)
    end
  end

  defp find_j(_chars, _i, -1), do: -1

  defp find_j(chars, i, idx) do
    if Enum.at(chars, idx) > Enum.at(chars, i) do
      idx
    else
      find_j(chars, i, idx - 1)
    end
  end

  defp swap(list, a, b) do
    val_a = Enum.at(list, a)
    val_b = Enum.at(list, b)

    list
    |> List.replace_at(a, val_b)
    |> List.replace_at(b, val_a)
  end

  defp reverse_suffix(chars, start_idx) do
    {prefix, suffix} = Enum.split(chars, start_idx)
    prefix ++ Enum.reverse(suffix)
  end

  # ---------- minimum adjacent swaps ----------
  defp min_swaps(orig, target), do: do_swaps(orig, target, 0, 0)

  defp do_swaps(_orig, _target, idx, acc) when idx == length(_orig), do: acc

  defp do_swaps(orig, target, idx, acc) do
    if Enum.at(orig, idx) == Enum.at(target, idx) do
      do_swaps(orig, target, idx + 1, acc)
    else
      j = find_pos(orig, idx + 1, Enum.at(target, idx))
      {new_orig, swaps} = bring_to_front(orig, idx, j)
      do_swaps(new_orig, target, idx + 1, acc + swaps)
    end
  end

  defp find_pos(list, pos, val) do
    if Enum.at(list, pos) == val do
      pos
    else
      find_pos(list, pos + 1, val)
    end
  end

  defp bring_to_front(list, i, j) when j > i do
    positions = Enum.to_list((i + 1)..j) |> Enum.reverse()

    new_list =
      Enum.reduce(positions, list, fn pos, acc ->
        a = Enum.at(acc, pos)
        b = Enum.at(acc, pos - 1)

        acc
        |> List.replace_at(pos, b)
        |> List.replace_at(pos - 1, a)
      end)

    {new_list, j - i}
  end

  defp bring_to_front(list, _i, _j), do: {list, 0}
end
```
