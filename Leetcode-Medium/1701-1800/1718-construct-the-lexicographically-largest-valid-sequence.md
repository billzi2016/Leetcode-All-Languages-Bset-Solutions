# 1718. Construct the Lexicographically Largest Valid Sequence

## Cpp

```cpp
class Solution {
public:
    vector<int> constructDistancedSequence(int n) {
        int m = 2 * n - 1;
        vector<int> seq(m, 0);
        vector<char> used(n + 1, false);
        
        function<bool(int)> dfs = [&](int idx) -> bool {
            if (idx == m) return true; // filled all positions
            if (seq[idx] != 0) return dfs(idx + 1);
            
            for (int num = n; num >= 1; --num) {
                if (used[num]) continue;
                if (num == 1) {
                    seq[idx] = 1;
                    used[1] = true;
                    if (dfs(idx + 1)) return true;
                    used[1] = false;
                    seq[idx] = 0;
                } else {
                    int j = idx + num;
                    if (j >= m || seq[j] != 0) continue;
                    seq[idx] = seq[j] = num;
                    used[num] = true;
                    if (dfs(idx + 1)) return true;
                    used[num] = false;
                    seq[idx] = seq[j] = 0;
                }
            }
            return false;
        };
        
        dfs(0);
        return seq;
    }
};
```

## Java

```java
class Solution {
    public int[] constructDistancedSequence(int n) {
        int len = 2 * n - 1;
        int[] ans = new int[len];
        boolean[] used = new boolean[n + 1];
        backtrack(0, ans, used, n);
        return ans;
    }

    private boolean backtrack(int pos, int[] ans, boolean[] used, int n) {
        if (pos == ans.length) {
            return true;
        }
        if (ans[pos] != 0) {
            return backtrack(pos + 1, ans, used, n);
        }
        for (int num = n; num >= 1; --num) {
            if (used[num]) continue;
            if (num == 1) {
                ans[pos] = 1;
                used[1] = true;
                if (backtrack(pos + 1, ans, used, n)) return true;
                ans[pos] = 0;
                used[1] = false;
            } else {
                int j = pos + num;
                if (j < ans.length && ans[j] == 0) {
                    ans[pos] = num;
                    ans[j] = num;
                    used[num] = true;
                    if (backtrack(pos + 1, ans, used, n)) return true;
                    ans[pos] = 0;
                    ans[j] = 0;
                    used[num] = false;
                }
            }
        }
        return false;
    }
}
```

## Python

```python
class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        length = 2 * n - 1
        ans = [0] * length
        used = [False] * (n + 1)

        def dfs(pos):
            if pos == length:
                return True
            if ans[pos] != 0:
                return dfs(pos + 1)
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                if num == 1:
                    ans[pos] = 1
                    used[1] = True
                    if dfs(pos + 1):
                        return True
                    ans[pos] = 0
                    used[1] = False
                else:
                    nxt = pos + num
                    if nxt < length and ans[nxt] == 0:
                        ans[pos] = ans[nxt] = num
                        used[num] = True
                        if dfs(pos + 1):
                            return True
                        ans[pos] = ans[nxt] = 0
                        used[num] = False
            return False

        dfs(0)
        return ans
```

## Python3

```python
class Solution:
    def constructDistancedSequence(self, n):
        size = 2 * n - 1
        seq = [0] * size
        used = [False] * (n + 1)

        def dfs(pos):
            while pos < size and seq[pos] != 0:
                pos += 1
            if pos == size:
                return True

            for num in range(n, 0, -1):
                if used[num]:
                    continue
                if num == 1:
                    # place single occurrence
                    seq[pos] = 1
                    used[1] = True
                    if dfs(pos + 1):
                        return True
                    seq[pos] = 0
                    used[1] = False
                else:
                    nxt = pos + num
                    if nxt < size and seq[nxt] == 0:
                        seq[pos] = seq[nxt] = num
                        used[num] = True
                        if dfs(pos + 1):
                            return True
                        seq[pos] = seq[nxt] = 0
                        used[num] = False
            return False

        dfs(0)
        return seq
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

static int N;
static int LEN;
static int seq[40];
static bool used[21];

static bool dfs(int pos) {
    if (pos == LEN) return true;
    if (seq[pos] != 0) return dfs(pos + 1);
    for (int num = N; num >= 1; --num) {
        if (used[num]) continue;
        if (num == 1) {
            seq[pos] = 1;
            used[1] = true;
            if (dfs(pos + 1)) return true;
            seq[pos] = 0;
            used[1] = false;
        } else {
            int nxt = pos + num;
            if (nxt < LEN && seq[nxt] == 0) {
                seq[pos] = seq[nxt] = num;
                used[num] = true;
                if (dfs(pos + 1)) return true;
                seq[pos] = seq[nxt] = 0;
                used[num] = false;
            }
        }
    }
    return false;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* constructDistancedSequence(int n, int* returnSize) {
    N = n;
    LEN = 2 * n - 1;
    for (int i = 0; i < LEN; ++i) seq[i] = 0;
    for (int i = 0; i <= n; ++i) used[i] = false;

    dfs(0);

    int* res = (int*)malloc(LEN * sizeof(int));
    for (int i = 0; i < LEN; ++i) res[i] = seq[i];
    *returnSize = LEN;
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public int[] ConstructDistancedSequence(int n)
    {
        int len = 2 * n - 1;
        int[] seq = new int[len];
        bool[] used = new bool[n + 1];

        bool Dfs(int idx)
        {
            while (idx < len && seq[idx] != 0) idx++;
            if (idx == len) return true;

            for (int num = n; num >= 1; --num)
            {
                if (used[num]) continue;

                if (num == 1)
                {
                    seq[idx] = 1;
                    used[1] = true;
                    if (Dfs(idx + 1)) return true;
                    seq[idx] = 0;
                    used[1] = false;
                }
                else
                {
                    int j = idx + num;
                    if (j < len && seq[j] == 0)
                    {
                        seq[idx] = num;
                        seq[j] = num;
                        used[num] = true;
                        if (Dfs(idx + 1)) return true;
                        seq[idx] = 0;
                        seq[j] = 0;
                        used[num] = false;
                    }
                }
            }

            return false;
        }

        Dfs(0);
        return seq;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @return {number[]}
 */
var constructDistancedSequence = function(n) {
    const len = 2 * n - 1;
    const seq = new Array(len).fill(0);
    const used = new Array(n + 1).fill(false);

    function dfs(idx) {
        if (idx === len) return true;
        if (seq[idx] !== 0) return dfs(idx + 1);

        for (let num = n; num >= 1; --num) {
            if (used[num]) continue;

            if (num === 1) {
                seq[idx] = 1;
                used[1] = true;
                if (dfs(idx + 1)) return true;
                used[1] = false;
                seq[idx] = 0;
            } else {
                const j = idx + num;
                if (j >= len || seq[j] !== 0) continue;

                seq[idx] = num;
                seq[j] = num;
                used[num] = true;
                if (dfs(idx + 1)) return true;
                used[num] = false;
                seq[idx] = 0;
                seq[j] = 0;
            }
        }
        return false;
    }

    dfs(0);
    return seq;
};
```

## Typescript

```typescript
function constructDistancedSequence(n: number): number[] {
    const len = 2 * n - 1;
    const seq = new Array<number>(len).fill(0);
    const used = new Array<boolean>(n + 1).fill(false);

    function dfs(pos: number): boolean {
        if (pos === len) return true;
        if (seq[pos] !== 0) return dfs(pos + 1);
        for (let num = n; num >= 1; --num) {
            if (used[num]) continue;
            if (num === 1) {
                seq[pos] = 1;
                used[1] = true;
                if (dfs(pos + 1)) return true;
                seq[pos] = 0;
                used[1] = false;
            } else {
                const nxt = pos + num;
                if (nxt >= len || seq[nxt] !== 0) continue;
                seq[pos] = num;
                seq[nxt] = num;
                used[num] = true;
                if (dfs(pos + 1)) return true;
                seq[pos] = 0;
                seq[nxt] = 0;
                used[num] = false;
            }
        }
        return false;
    }

    dfs(0);
    return seq;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer[]
     */
    function constructDistancedSequence($n) {
        $size = 2 * $n - 1;
        $res = array_fill(0, $size, 0);
        $used = array_fill(0, $n + 1, false);

        $dfs = function ($idx) use (&$dfs, &$res, &$used, $n, $size) {
            if ($idx == $size) {
                return true;
            }
            if ($res[$idx] != 0) {
                return $dfs($idx + 1);
            }

            for ($num = $n; $num >= 1; $num--) {
                if ($used[$num]) {
                    continue;
                }
                $used[$num] = true;
                $res[$idx] = $num;

                if ($num == 1) {
                    if ($dfs($idx + 1)) {
                        return true;
                    }
                } else {
                    $nextIdx = $idx + $num;
                    if ($nextIdx < $size && $res[$nextIdx] == 0) {
                        $res[$nextIdx] = $num;
                        if ($dfs($idx + 1)) {
                            return true;
                        }
                        $res[$nextIdx] = 0;
                    }
                }

                // backtrack
                $res[$idx] = 0;
                $used[$num] = false;
            }
            return false;
        };

        $dfs(0);
        return $res;
    }
}
```

## Swift

```swift
class Solution {
    func constructDistancedSequence(_ n: Int) -> [Int] {
        var sequence = Array(repeating: 0, count: 2 * n - 1)
        var used = Array(repeating: false, count: n + 1)

        func dfs(_ index: Int) -> Bool {
            if index == sequence.count { return true }
            if sequence[index] != 0 { return dfs(index + 1) }

            for num in stride(from: n, through: 1, by: -1) {
                if used[num] { continue }
                if num == 1 {
                    sequence[index] = 1
                    used[1] = true
                    if dfs(index + 1) { return true }
                    sequence[index] = 0
                    used[1] = false
                } else {
                    let partner = index + num
                    if partner < sequence.count && sequence[partner] == 0 {
                        sequence[index] = num
                        sequence[partner] = num
                        used[num] = true
                        if dfs(index + 1) { return true }
                        sequence[index] = 0
                        sequence[partner] = 0
                        used[num] = false
                    }
                }
            }
            return false
        }

        _ = dfs(0)
        return sequence
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun constructDistancedSequence(n: Int): IntArray {
        val len = 2 * n - 1
        val seq = IntArray(len)
        val used = BooleanArray(n + 1)

        fun dfs(pos: Int): Boolean {
            if (pos == len) return true
            if (seq[pos] != 0) return dfs(pos + 1)

            for (num in n downTo 1) {
                if (used[num]) continue
                if (num == 1) {
                    used[1] = true
                    seq[pos] = 1
                    if (dfs(pos + 1)) return true
                    seq[pos] = 0
                    used[1] = false
                } else {
                    val j = pos + num
                    if (j < len && seq[j] == 0) {
                        used[num] = true
                        seq[pos] = num
                        seq[j] = num
                        if (dfs(pos + 1)) return true
                        seq[pos] = 0
                        seq[j] = 0
                        used[num] = false
                    }
                }
            }
            return false
        }

        dfs(0)
        return seq
    }
}
```

## Dart

```dart
class Solution {
  List<int> constructDistancedSequence(int n) {
    int size = 2 * n - 1;
    List<int> seq = List.filled(size, 0);
    List<bool> used = List.filled(n + 1, false);

    bool dfs(int idx) {
      if (idx == size) return true;
      if (seq[idx] != 0) return dfs(idx + 1);

      for (int num = n; num >= 1; --num) {
        if (used[num]) continue;

        if (num == 1) {
          seq[idx] = 1;
          used[1] = true;
          if (dfs(idx + 1)) return true;
          seq[idx] = 0;
          used[1] = false;
        } else {
          int j = idx + num;
          if (j < size && seq[j] == 0) {
            seq[idx] = num;
            seq[j] = num;
            used[num] = true;
            if (dfs(idx + 1)) return true;
            seq[idx] = 0;
            seq[j] = 0;
            used[num] = false;
          }
        }
      }
      return false;
    }

    dfs(0);
    return seq;
  }
}
```

## Golang

```go
func constructDistancedSequence(n int) []int {
	length := 2*n - 1
	res := make([]int, length)
	used := make([]bool, n+1)

	var dfs func(int) bool
	dfs = func(pos int) bool {
		if pos == length {
			return true
		}
		if res[pos] != 0 {
			return dfs(pos + 1)
		}
		for num := n; num >= 1; num-- {
			if used[num] {
				continue
			}
			if num == 1 {
				res[pos] = 1
				used[1] = true
				if dfs(pos+1) {
					return true
				}
				res[pos] = 0
				used[1] = false
			} else {
				nxt := pos + num
				if nxt < length && res[nxt] == 0 {
					res[pos] = num
					res[nxt] = num
					used[num] = true
					if dfs(pos+1) {
						return true
					}
					res[pos] = 0
					res[nxt] = 0
					used[num] = false
				}
			}
		}
		return false
	}

	dfs(0)
	return res
}
```

## Ruby

```ruby
def construct_distanced_sequence(n)
  len = 2 * n - 1
  res = Array.new(len, 0)
  used = Array.new(n + 1, false)

  dfs = nil
  dfs = lambda do |pos|
    while pos < len && res[pos] != 0
      pos += 1
    end
    return true if pos == len

    n.downto(1) do |num|
      next if used[num]

      if num == 1
        res[pos] = 1
        used[1] = true
        if dfs.call(pos + 1)
          return true
        end
        used[1] = false
        res[pos] = 0
      else
        nxt = pos + num
        next if nxt >= len || res[nxt] != 0

        res[pos] = num
        res[nxt] = num
        used[num] = true
        if dfs.call(pos + 1)
          return true
        end
        used[num] = false
        res[pos] = 0
        res[nxt] = 0
      end
    end

    false
  end

  dfs.call(0)
  res
end
```

## Scala

```scala
object Solution {
    def constructDistancedSequence(n: Int): Array[Int] = {
        val size = 2 * n - 1
        val res = new Array[Int](size)
        java.util.Arrays.fill(res, 0)
        val used = new Array[Boolean](n + 1)

        def backtrack(pos: Int): Boolean = {
            if (pos == size) return true
            if (res(pos) != 0) return backtrack(pos + 1)

            for (num <- n to 1 by -1) {
                if (!used(num)) {
                    if (num == 1) {
                        res(pos) = 1
                        used(1) = true
                        if (backtrack(pos + 1)) return true
                        res(pos) = 0
                        used(1) = false
                    } else {
                        val j = pos + num
                        if (j < size && res(j) == 0) {
                            res(pos) = num
                            res(j) = num
                            used(num) = true
                            if (backtrack(pos + 1)) return true
                            res(pos) = 0
                            res(j) = 0
                            used(num) = false
                        }
                    }
                }
            }
            false
        }

        backtrack(0)
        res
    }
}
```

## Rust

```rust
impl Solution {
    pub fn construct_distanced_sequence(n: i32) -> Vec<i32> {
        let n_usize = n as usize;
        if n_usize == 0 {
            return vec![];
        }
        let len = 2 * n_usize - 1;
        let mut seq = vec![0i32; len];
        let mut used = vec![false; n_usize + 1];

        fn dfs(pos: usize, n: usize, seq: &mut Vec<i32>, used: &mut Vec<bool>) -> bool {
            if pos == seq.len() {
                return true;
            }
            if seq[pos] != 0 {
                return dfs(pos + 1, n, seq, used);
            }

            for num in (1..=n).rev() {
                if used[num] {
                    continue;
                }
                if num == 1 {
                    // place single occurrence
                    seq[pos] = 1;
                    used[1] = true;
                    if dfs(pos + 1, n, seq, used) {
                        return true;
                    }
                    seq[pos] = 0;
                    used[1] = false;
                } else {
                    let next = pos + num;
                    if next < seq.len() && seq[next] == 0 {
                        // place both occurrences
                        seq[pos] = num as i32;
                        seq[next] = num as i32;
                        used[num] = true;
                        if dfs(pos + 1, n, seq, used) {
                            return true;
                        }
                        seq[pos] = 0;
                        seq[next] = 0;
                        used[num] = false;
                    }
                }
            }
            false
        }

        dfs(0, n_usize, &mut seq, &mut used);
        seq
    }
}
```

## Racket

```racket
(define/contract (construct-distanced-sequence n)
  (-> exact-integer? (listof exact-integer?))
  (let* ((len (- (* 2 n) 1))
         (seq (make-vector len 0))
         (used (make-vector (+ n 1) #f)))
    (define (dfs idx)
      (if (= idx len)
          #t
          (let ((val (vector-ref seq idx)))
            (if (not (= val 0))
                (dfs (+ idx 1))
                (try-number idx n)))))
    (define (try-number idx num)
      (cond [(< num 1) #f]
            [(vector-ref used num) (try-number idx (- num 1))]
            [(= num 1)
             (vector-set! seq idx 1)
             (vector-set! used 1 #t)
             (if (dfs (+ idx 1))
                 #t
                 (begin
                   (vector-set! seq idx 0)
                   (vector-set! used 1 #f)
                   (try-number idx (- num 1))))]
            [else
             (let ((j (+ idx num)))
               (if (and (< j len) (= (vector-ref seq j) 0))
                   (begin
                     (vector-set! seq idx num)
                     (vector-set! seq j num)
                     (vector-set! used num #t)
                     (if (dfs (+ idx 1))
                         #t
                         (begin
                           (vector-set! seq idx 0)
                           (vector-set! seq j 0)
                           (vector-set! used num #f)
                           (try-number idx (- num 1)))))
                   (try-number idx (- num 1))))]))
    (dfs 0)
    (vector->list seq)))
```

## Erlang

```erlang
-module(solution).
-export([construct_distanced_sequence/1]).

-spec construct_distanced_sequence(N :: integer()) -> [integer()].
construct_distanced_sequence(N) ->
    Len = 2 * N - 1,
    Seq0 = erlang:make_tuple(Len, 0),
    Used0 = erlang:make_tuple(N + 1, false),
    {ok, Res} = dfs(N, Len, 0, Seq0, Used0),
    Res.

dfs(_N, Len, Index, _Seq, _Used) when Index == Len ->
    {ok, tuple_to_list(_Seq)}; % unreachable placeholder
dfs(N, Len, Index, Seq, Used) when Index == Len ->
    {ok, tuple_to_list(Seq)};
dfs(N, Len, Index, Seq, Used) ->
    case get_elem(Seq, Index) of
        0 -> try_number(N, N, Index, Len, Seq, Used);
        _ -> dfs(N, Len, Index + 1, Seq, Used)
    end.

try_number(_N, 0, _Index, _Len, _Seq, _Used) ->
    false;
try_number(N, Number, Index, Len, Seq, Used) when Number >= 1 ->
    case get_elem(Used, Number) of
        true -> try_number(N, Number - 1, Index, Len, Seq, Used);
        false ->
            NewSeq = set_elem(Seq, Index, Number),
            NewUsed = set_elem(Used, Number, true),
            if Number == 1 ->
                    case dfs(N, Len, Index + 1, NewSeq, NewUsed) of
                        {ok, _}=Res -> Res;
                        false -> try_number(N, Number - 1, Index, Len, Seq, Used)
                    end;
               true ->
                    SecondPos = Index + Number,
                    if SecondPos < Len andalso get_elem(Seq, SecondPos) == 0 ->
                            NewSeq2 = set_elem(NewSeq, SecondPos, Number),
                            case dfs(N, Len, Index + 1, NewSeq2, NewUsed) of
                                {ok, _}=Res -> Res;
                                false -> try_number(N, Number - 1, Index, Len, Seq, Used)
                            end;
                       true ->
                            try_number(N, Number - 1, Index, Len, Seq, Used)
                    end
            end
    end.

get_elem(Tuple, Pos) ->
    element(Pos + 1, Tuple).

set_elem(Tuple, Pos, Value) ->
    erlang:setelement(Pos + 1, Tuple, Value).
```

## Elixir

```elixir
defmodule Solution do
  @spec construct_distanced_sequence(n :: integer) :: [integer]
  def construct_distanced_sequence(n) do
    len = 2 * n - 1
    seq = :erlang.make_tuple(len, 0)
    used = :erlang.make_tuple(n + 1, false)

    {:ok, result} = dfs(0, len, seq, used, n)
    result
  end

  defp dfs(idx, len, seq, used, n) do
    if idx == len do
      {:ok, Tuple.to_list(seq)}
    else
      cur = :erlang.element(idx + 1, seq)

      if cur != 0 do
        dfs(idx + 1, len, seq, used, n)
      else
        try_place(idx, len, seq, used, n)
      end
    end
  end

  defp try_place(idx, len, seq, used, n) do
    Enum.reduce_while(n..1, :error, fn k, _acc ->
      if :erlang.element(k + 1, used) do
        {:cont, :error}
      else
        if k == 1 do
          seq2 = :erlang.setelement(idx + 1, seq, 1)
          used2 = :erlang.setelement(k + 1, used, true)

          case dfs(idx + 1, len, seq2, used2, n) do
            {:ok, _} = res -> {:halt, res}
            _ -> {:cont, :error}
          end
        else
          j = idx + k

          if j < len and :erlang.element(j + 1, seq) == 0 do
            seq2 =
              seq
              |> :erlang.setelement(idx + 1, k)
              |> :erlang.setelement(j + 1, k)

            used2 = :erlang.setelement(k + 1, used, true)

            case dfs(idx + 1, len, seq2, used2, n) do
              {:ok, _} = res -> {:halt, res}
              _ -> {:cont, :error}
            end
          else
            {:cont, :error}
          end
        end
      end
    end)
  end
end
```
