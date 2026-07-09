# 3265. Count Almost Equal Pairs I

## Cpp

```cpp
class Solution {
public:
    bool canBecome(int src, int target) {
        if (src == target) return true;
        string s = to_string(src);
        int n = s.size();
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                swap(s[i], s[j]);
                if (stoi(s) == target) {
                    swap(s[i], s[j]); // restore before returning
                    return true;
                }
                swap(s[i], s[j]); // restore
            }
        }
        return false;
    }

    bool almostEqual(int a, int b) {
        return canBecome(a, b) || canBecome(b, a);
    }

    int countPairs(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (almostEqual(nums[i], nums[j])) ++ans;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int countPairs(int[] nums) {
        int n = nums.length;
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (almostEqual(nums[i], nums[j])) {
                    ans++;
                }
            }
        }
        return ans;
    }

    private boolean almostEqual(int a, int b) {
        if (a == b) return true;
        // try swapping digits in a
        String sa = Integer.toString(a);
        char[] ca = sa.toCharArray();
        int la = ca.length;
        for (int i = 0; i < la; ++i) {
            for (int j = i + 1; j < la; ++j) {
                if (ca[i] == ca[j]) continue; // swapping identical digits yields same number
                char[] copy = ca.clone();
                char tmp = copy[i];
                copy[i] = copy[j];
                copy[j] = tmp;
                int val = Integer.parseInt(new String(copy));
                if (val == b) return true;
            }
        }
        // try swapping digits in b
        String sb = Integer.toString(b);
        char[] cb = sb.toCharArray();
        int lb = cb.length;
        for (int i = 0; i < lb; ++i) {
            for (int j = i + 1; j < lb; ++j) {
                if (cb[i] == cb[j]) continue;
                char[] copy = cb.clone();
                char tmp = copy[i];
                copy[i] = copy[j];
                copy[j] = tmp;
                int val = Integer.parseInt(new String(copy));
                if (val == a) return true;
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def countPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        reachable = []
        for num in nums:
            s = list(str(num))
            m = set()
            m.add(num)  # no operation
            l = len(s)
            for i in range(l):
                for j in range(i + 1, l):
                    s[i], s[j] = s[j], s[i]
                    m.add(int(''.join(s)))
                    s[i], s[j] = s[j], s[i]  # swap back
            reachable.append(m)

        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] in reachable[i] or nums[i] in reachable[j]:
                    ans += 1
        return ans
```

## Python3

```python
class Solution:
    def countPairs(self, nums):
        from typing import List
        n = len(nums)
        # Precompute reachable numbers (including itself) for each element
        reach = []
        for num in nums:
            s = list(str(num))
            m = set()
            m.add(num)  # no swap
            L = len(s)
            for i in range(L):
                for j in range(i + 1, L):
                    s[i], s[j] = s[j], s[i]
                    # Convert to int (handles leading zeros)
                    m.add(int(''.join(s)))
                    s[i], s[j] = s[j], s[i]  # swap back
            reach.append(m)

        ans = 0
        for i in range(n):
            ri = reach[i]
            for j in range(i + 1, n):
                if ri & reach[j]:
                    ans += 1
        return ans
```

## C

```c
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

static bool canTransform(int from, int target) {
    char s[12];
    int len = sprintf(s, "%d", from);
    for (int i = 0; i < len; ++i) {
        for (int j = i; j < len; ++j) {
            // swap positions i and j
            char tmp = s[i];
            s[i] = s[j];
            s[j] = tmp;

            int val = 0;
            for (int k = 0; k < len; ++k) {
                val = val * 10 + (s[k] - '0');
            }
            if (val == target) {
                return true;
            }

            // swap back
            tmp = s[i];
            s[i] = s[j];
            s[j] = tmp;
        }
    }
    return false;
}

static bool isAlmostEqual(int a, int b) {
    return canTransform(a, b) || canTransform(b, a);
}

int countPairs(int* nums, int numsSize) {
    int ans = 0;
    for (int i = 0; i < numsSize; ++i) {
        for (int j = i + 1; j < numsSize; ++j) {
            if (isAlmostEqual(nums[i], nums[j])) {
                ++ans;
            }
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    private bool IsAlmost(int a, int b) {
        if (a == b) return true;
        string s = a.ToString();
        int n = s.Length;
        char[] chars = s.ToCharArray();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                // swap i and j
                var tmp = chars[i];
                chars[i] = chars[j];
                chars[j] = tmp;
                
                int val = int.Parse(new string(chars));
                if (val == b) return true;
                
                // swap back
                tmp = chars[i];
                chars[i] = chars[j];
                chars[j] = tmp;
            }
        }
        return false;
    }

    public int CountPairs(int[] nums) {
        int count = 0;
        int n = nums.Length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (IsAlmost(nums[i], nums[j]) || IsAlmost(nums[j], nums[i])) {
                    count++;
                }
            }
        }
        return count;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countPairs = function(nums) {
    const n = nums.length;
    let ans = 0;

    const isAlmostEqual = (a, b) => {
        if (a === b) return true;
        const sa = a.toString();
        const sb = b.toString();
        const L = Math.max(sa.length, sb.length);
        const pa = sa.padStart(L, '0');
        const pb = sb.padStart(L, '0');

        // try swapping in a
        let arr = pa.split('');
        for (let i = 0; i < L; i++) {
            for (let j = i + 1; j < L; j++) {
                [arr[i], arr[j]] = [arr[j], arr[i]];
                const valStr = arr.join('').replace(/^0+/, '');
                const val = valStr === '' ? 0 : Number(valStr);
                if (val === b) return true;
                [arr[i], arr[j]] = [arr[j], arr[i]];
            }
        }

        // try swapping in b
        arr = pb.split('');
        for (let i = 0; i < L; i++) {
            for (let j = i + 1; j < L; j++) {
                [arr[i], arr[j]] = [arr[j], arr[i]];
                const valStr = arr.join('').replace(/^0+/, '');
                const val = valStr === '' ? 0 : Number(valStr);
                if (val === a) return true;
                [arr[i], arr[j]] = [arr[j], arr[i]];
            }
        }

        return false;
    };

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (isAlmostEqual(nums[i], nums[j])) ans++;
        }
    }
    return ans;
};
```

## Typescript

```typescript
function countPairs(nums: number[]): number {
    const n = nums.length;
    let ans = 0;

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (isAlmostEqual(nums[i], nums[j])) ans++;
        }
    }

    return ans;
}

function isAlmostEqual(a: number, b: number): boolean {
    if (a === b) return true;

    const sa = a.toString();
    const sb = b.toString();

    // try swapping in a
    for (let p = 0; p < sa.length; p++) {
        for (let q = p + 1; q < sa.length; q++) {
            if (sa[p] === sa[q]) continue;
            const arr = sa.split('');
            [arr[p], arr[q]] = [arr[q], arr[p]];
            if (Number(arr.join('')) === b) return true;
        }
    }

    // try swapping in b
    for (let p = 0; p < sb.length; p++) {
        for (let q = p + 1; q < sb.length; q++) {
            if (sb[p] === sb[q]) continue;
            const arr = sb.split('');
            [arr[p], arr[q]] = [arr[q], arr[p]];
            if (Number(arr.join('')) === a) return true;
        }
    }

    return false;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countPairs($nums) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; ++$i) {
            for ($j = $i + 1; $j < $n; ++$j) {
                if ($this->isAlmostEqual($nums[$i], $nums[$j])) {
                    ++$ans;
                }
            }
        }
        return $ans;
    }

    private function isAlmostEqual($a, $b) {
        if ($a == $b) {
            return true;
        }
        if ($this->canSwapTo($a, $b)) {
            return true;
        }
        if ($this->canSwapTo($b, $a)) {
            return true;
        }
        return false;
    }

    private function canSwapTo($src, $target) {
        $s = strval($src);
        $len = strlen($s);
        for ($i = 0; $i < $len; ++$i) {
            for ($j = $i + 1; $j < $len; ++$j) {
                $arr = str_split($s);
                $tmp = $arr[$i];
                $arr[$i] = $arr[$j];
                $arr[$j] = $tmp;
                $newNum = intval(implode('', $arr));
                if ($newNum == $target) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

## Swift

```swift
class Solution {
    func countPairs(_ nums: [Int]) -> Int {
        var result = 0
        let n = nums.count
        for i in 0..<n {
            for j in (i + 1)..<n {
                if isAlmostEqual(nums[i], nums[j]) {
                    result += 1
                }
            }
        }
        return result
    }
    
    private func isAlmostEqual(_ a: Int, _ b: Int) -> Bool {
        return canTransform(a, to: b) || canTransform(b, to: a)
    }
    
    private func canTransform(_ from: Int, to target: Int) -> Bool {
        if from == target { return true }
        let digits = Array(String(from))
        let len = digits.count
        if len < 2 { return false }
        for i in 0..<len {
            for j in (i + 1)..<len {
                var swapped = digits
                swapped.swapAt(i, j)
                if let val = Int(String(swapped)), val == target {
                    return true
                }
            }
        }
        return false
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countPairs(nums: IntArray): Int {
        val n = nums.size
        // Precompute all numbers reachable by at most one swap (including original)
        val variants = Array(n) { mutableSetOf<Int>() }
        for (idx in 0 until n) {
            val numStr = nums[idx].toString()
            val chars = numStr.toCharArray()
            val set = variants[idx]
            set.add(nums[idx]) // no operation
            val len = chars.size
            for (i in 0 until len) {
                for (j in i + 1 until len) {
                    val ci = chars[i]
                    val cj = chars[j]
                    // swap
                    chars[i] = cj
                    chars[j] = ci
                    set.add(String(chars).toInt())
                    // revert swap
                    chars[i] = ci
                    chars[j] = cj
                }
            }
        }

        var ans = 0
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                val setI = variants[i]
                val setJ = variants[j]
                var ok = false
                if (setI.size <= setJ.size) {
                    for (v in setI) {
                        if (setJ.contains(v)) {
                            ok = true
                            break
                        }
                    }
                } else {
                    for (v in setJ) {
                        if (setI.contains(v)) {
                            ok = true
                            break
                        }
                    }
                }
                if (ok) ans++
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  bool _isAlmostEqual(int a, int b) {
    if (a == b) return true;
    String sa = a.toString();
    List<String> listA = sa.split('');
    int nA = listA.length;
    for (int i = 0; i < nA; ++i) {
      for (int j = i + 1; j < nA; ++j) {
        var tmp = listA[i];
        listA[i] = listA[j];
        listA[j] = tmp;
        int val = int.parse(listA.join(''));
        if (val == b) return true;
        // swap back
        tmp = listA[i];
        listA[i] = listA[j];
        listA[j] = tmp;
      }
    }

    String sb = b.toString();
    List<String> listB = sb.split('');
    int nB = listB.length;
    for (int i = 0; i < nB; ++i) {
      for (int j = i + 1; j < nB; ++j) {
        var tmp = listB[i];
        listB[i] = listB[j];
        listB[j] = tmp;
        int val = int.parse(listB.join(''));
        if (val == a) return true;
        // swap back
        tmp = listB[i];
        listB[i] = listB[j];
        listB[j] = tmp;
      }
    }

    return false;
  }

  int countPairs(List<int> nums) {
    int cnt = 0;
    for (int i = 0; i < nums.length; ++i) {
      for (int j = i + 1; j < nums.length; ++j) {
        if (_isAlmostEqual(nums[i], nums[j])) cnt++;
      }
    }
    return cnt;
  }
}
```

## Golang

```go
import "strconv"

func countPairs(nums []int) int {
	n := len(nums)
	sets := make([]map[int]struct{}, n)

	for idx, num := range nums {
		s := strconv.Itoa(num)
		d := len(s)
		m := make(map[int]struct{})
		// original number
		val, _ := strconv.Atoi(s)
		m[val] = struct{}{}
		// all possible swaps
		b := []byte(s)
		for i := 0; i < d; i++ {
			for j := i + 1; j < d; j++ {
				b[i], b[j] = b[j], b[i]
				v, _ := strconv.Atoi(string(b))
				m[v] = struct{}{}
				b[i], b[j] = b[j], b[i] // restore
			}
		}
		sets[idx] = m
	}

	count := 0
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if nums[i] == nums[j] {
				count++
				continue
			}
			if _, ok := sets[i][nums[j]]; ok {
				count++
			} else if _, ok := sets[j][nums[i]]; ok {
				count++
			}
		}
	}
	return count
}
```

## Ruby

```ruby
def almost_equal?(a, b)
  return true if a == b

  sa = a.to_s
  sb = b.to_s

  # try swapping digits in a
  len_a = sa.length
  (0...len_a).each do |i|
    ((i + 1)...len_a).each do |j|
      chars = sa.chars
      chars[i], chars[j] = chars[j], chars[i]
      return true if chars.join.to_i == b
    end
  end

  # try swapping digits in b
  len_b = sb.length
  (0...len_b).each do |i|
    ((i + 1)...len_b).each do |j|
      chars = sb.chars
      chars[i], chars[j] = chars[j], chars[i]
      return true if chars.join.to_i == a
    end
  end

  false
end

# @param {Integer[]} nums
# @return {Integer}
def count_pairs(nums)
  n = nums.length
  cnt = 0
  (0...n).each do |i|
    ((i + 1)...n).each do |j|
      cnt += 1 if almost_equal?(nums[i], nums[j])
    end
  end
  cnt
end
```

## Scala

```scala
object Solution {
  def countPairs(nums: Array[Int]): Int = {
    var cnt = 0
    val n = nums.length
    for (i <- 0 until n) {
      for (j <- i + 1 until n) {
        if (almostEqual(nums(i), nums(j))) cnt += 1
      }
    }
    cnt
  }

  private def almostEqual(a: Int, b: Int): Boolean = {
    if (a == b) return true
    canSwapTo(a, b) || canSwapTo(b, a)
  }

  private def canSwapTo(src: Int, target: Int): Boolean = {
    val s = src.toString
    val len = s.length
    for (i <- 0 until len) {
      for (j <- i + 1 until len) {
        val arr = s.toCharArray.clone()
        val tmp = arr(i)
        arr(i) = arr(j)
        arr(j) = tmp
        val v = java.lang.Integer.parseInt(new String(arr))
        if (v == target) return true
      }
    }
    false
  }
}
```

## Rust

```rust
impl Solution {
    pub fn count_pairs(nums: Vec<i32>) -> i32 {
        use std::collections::HashSet;

        fn reachable(num: i32) -> HashSet<i32> {
            let s = num.to_string();
            let chars: Vec<char> = s.chars().collect();
            let mut set = HashSet::new();
            set.insert(num);
            let n = chars.len();
            for i in 0..n {
                for j in (i + 1)..n {
                    let mut v = chars.clone();
                    v.swap(i, j);
                    let t: String = v.iter().collect();
                    if let Ok(val) = t.parse::<i32>() {
                        set.insert(val);
                    }
                }
            }
            set
        }

        let n = nums.len();
        let reach: Vec<HashSet<i32>> = nums.iter().map(|&x| reachable(x)).collect();

        let mut ans = 0i32;
        for i in 0..n {
            for j in (i + 1)..n {
                let set_i = &reach[i];
                let set_j = &reach[j];
                if set_i.len() <= set_j.len() {
                    if set_i.iter().any(|v| set_j.contains(v)) {
                        ans += 1;
                    }
                } else {
                    if set_j.iter().any(|v| set_i.contains(v)) {
                        ans += 1;
                    }
                }
            }
        }
        ans
    }
}
```

## Racket

```racket
(define (swap-string s i j)
  (let* ((vec (list->vector (string->list s))))
    (let ((tmp (vector-ref vec i)))
      (vector-set! vec i (vector-ref vec j))
      (vector-set! vec j tmp))
    (list->string (vector->list vec))))

(define (reachable-set s)
  (let ((set (make-hash)))
    (hash-set! set s #t)
    (let ((len (string-length s)))
      (for ([i (in-range len)])
        (for ([j (in-range (+ i 1) len)])
          (hash-set! set (swap-string s i j) #t))))
    set))

(define/contract (count-pairs nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((strings (map number->string nums))
         (n (length strings))
         (reach (vector->list (list->vector (map reachable-set strings)))))
    (for/sum ([i (in-range n)])
      (for/sum ([j (in-range (+ i 1) n)]
                #:when (= (string-length (list-ref strings i))
                          (string-length (list-ref strings j))))
        (let ((seti (list-ref reach i))
              (setj (list-ref reach j)))
          (let loop ((keys (hash-keys setj)))
            (if (null? keys)
                0
                (if (hash-has-key? seti (car keys))
                    1
                    (loop (cdr keys))))))))))
```

## Erlang

```erlang
-spec count_pairs(Nums :: [integer()]) -> integer().
count_pairs(Nums) ->
    Sets = [gen(N) || N <- Nums],
    Len = length(Sets),
    loop(Sets, Len, 1, 0).

gen(N) ->
    Str = integer_to_list(N),
    L = length(Str),
    Swaps = [{I,J} || I <- lists:seq(1, L), J <- lists:seq(I+1, L)],
    Set0 = maps:put(N, true, #{}),
    lists:foldl(fun({I,J}, Acc) ->
        Swapped = swap(Str, I, J),
        Num = list_to_integer(Swapped),
        maps:put(Num, true, Acc)
    end, Set0, Swaps).

swap(Lst, I, J) ->
    Tup0 = list_to_tuple(Lst),
    Ei = element(I, Tup0),
    Ej = element(J, Tup0),
    Tup1 = setelement(I, Tup0, Ej),
    Tup2 = setelement(J, Tup1, Ei),
    tuple_to_list(Tup2).

has_common(SetA, SetB) ->
    lists:any(fun(K) -> maps:is_key(K, SetB) end, maps:keys(SetA)).

loop(_Sets, Len, I, Acc) when I > Len-1 ->
    Acc;
loop(Sets, Len, I, Acc) ->
    SetI = lists:nth(I, Sets),
    NewAcc = inner_loop(Sets, I+1, Len, SetI, Acc),
    loop(Sets, Len, I+1, NewAcc).

inner_loop(_Sets, J, Len, _SetI, Acc) when J > Len ->
    Acc;
inner_loop(Sets, J, Len, SetI, Acc) ->
    SetJ = lists:nth(J, Sets),
    Acc2 = case has_common(SetI, SetJ) of
        true -> Acc + 1;
        false -> Acc
    end,
    inner_loop(Sets, J+1, Len, SetI, Acc2).
```

## Elixir

```elixir
defmodule Solution do
  @spec count_pairs(nums :: [integer]) :: integer
  def count_pairs(nums) do
    reach = Enum.map(nums, &reachable/1)

    n = length(nums)

    Enum.reduce(0..(n - 2), 0, fn i, acc ->
      a = Enum.at(nums, i)
      ra = Enum.at(reach, i)

      Enum.reduce((i + 1)..(n - 1), acc, fn j, inner_acc ->
        b = Enum.at(nums, j)

        if a == b or MapSet.member?(ra, b) or MapSet.member?(Enum.at(reach, j), a) do
          inner_acc + 1
        else
          inner_acc
        end
      end)
    end)
  end

  defp reachable(num) do
    s = Integer.to_string(num)
    chars = String.graphemes(s)
    len = length(chars)

    Enum.reduce(0..(len - 2), MapSet.new(), fn i, set ->
      Enum.reduce((i + 1)..(len - 1), set, fn j, acc_set ->
        swapped =
          chars
          |> List.replace_at(i, Enum.at(chars, j))
          |> List.replace_at(j, Enum.at(chars, i))

        val = String.to_integer(Enum.join(swapped))
        MapSet.put(acc_set, val)
      end)
    end)
  end
end
```
