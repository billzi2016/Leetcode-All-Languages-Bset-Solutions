# 2899. Last Visited Integers

## Cpp

```cpp
class Solution {
public:
    vector<int> lastVisitedIntegers(vector<int>& nums) {
        vector<int> seen;
        vector<int> ans;
        int idx = -1; // points to the current "last visited" position
        for (int x : nums) {
            if (x == -1) {
                if (idx >= 0) {
                    ans.push_back(seen[idx]);
                    --idx;
                } else {
                    ans.push_back(-1);
                }
            } else {
                seen.push_back(x);
                idx = (int)seen.size() - 1;
            }
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public List<Integer> lastVisitedIntegers(int[] nums) {
        Deque<Integer> stack = new ArrayDeque<>();
        List<Integer> ans = new ArrayList<>();
        for (int num : nums) {
            if (num == -1) {
                if (!stack.isEmpty()) {
                    ans.add(stack.pop());
                } else {
                    ans.add(-1);
                }
            } else {
                stack.push(num);
            }
        }
        return ans;
    }
}
```

## Python

```python
class Solution(object):
    def lastVisitedIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = []
        idx = -1  # points to the current "last visited" position in seen
        ans = []
        for x in nums:
            if x != -1:
                seen.append(x)
                idx = len(seen) - 1  # reset to the newest positive integer
            else:
                if idx >= 0:
                    ans.append(seen[idx])
                    idx -= 1
                else:
                    ans.append(-1)
        return ans
```

## Python3

```python
class Solution:
    def lastVisitedIntegers(self, nums):
        seen = []
        pos = -1
        ans = []
        for x in nums:
            if x != -1:
                seen.append(x)
                pos = len(seen) - 1
            else:
                if pos >= 0:
                    ans.append(seen[pos])
                    pos -= 1
                else:
                    ans.append(-1)
        return ans
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* lastVisitedIntegers(int* nums, int numsSize, int* returnSize) {
    // First count how many -1 entries there are to allocate answer array
    int cnt = 0;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == -1) cnt++;
    }
    *returnSize = cnt;
    int* ans = (int*)malloc(cnt * sizeof(int));
    
    // Simple stack to store seen positive integers
    int stack[101]; // nums length <= 100, values up to 100
    int top = -1;   // empty
    
    int idx = 0; // index in ans
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] != -1) {
            // push onto stack
            stack[++top] = nums[i];
        } else {
            if (top >= 0) {
                ans[idx++] = stack[top--]; // pop last visited integer
            } else {
                ans[idx++] = -1;
            }
        }
    }
    return ans;
}
```

## Csharp

```csharp
public class Solution {
    public IList<int> LastVisitedIntegers(int[] nums) {
        var seen = new List<int>();
        var ans = new List<int>();
        int idx = -1; // points to the current last visited integer
        
        foreach (int num in nums) {
            if (num != -1) {
                seen.Add(num);
                idx = seen.Count - 1; // newest positive becomes the top
            } else {
                if (idx >= 0) {
                    ans.Add(seen[idx]);
                    idx--;
                } else {
                    ans.Add(-1);
                }
            }
        }
        
        return ans;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var lastVisitedIntegers = function(nums) {
    const seen = [];
    const ans = [];
    for (const v of nums) {
        if (v !== -1) {
            seen.push(v);
        } else {
            if (seen.length > 0) {
                ans.push(seen.pop());
            } else {
                ans.push(-1);
            }
        }
    }
    return ans;
};
```

## Typescript

```typescript
function lastVisitedIntegers(nums: number[]): number[] {
    const stack: number[] = [];
    const ans: number[] = [];
    for (const x of nums) {
        if (x !== -1) {
            stack.push(x);
        } else {
            if (stack.length > 0) {
                ans.push(stack.pop()!);
            } else {
                ans.push(-1);
            }
        }
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function lastVisitedIntegers($nums) {
        $stack = [];
        $ans = [];
        foreach ($nums as $v) {
            if ($v == -1) {
                if (!empty($stack)) {
                    $ans[] = array_pop($stack);
                } else {
                    $ans[] = -1;
                }
            } else {
                $stack[] = $v;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func lastVisitedIntegers(_ nums: [Int]) -> [Int] {
        var seen = [Int]()
        var cur = -1
        var ans = [Int]()
        for num in nums {
            if num == -1 {
                if cur >= 0 {
                    ans.append(seen[cur])
                    cur -= 1
                } else {
                    ans.append(-1)
                }
            } else {
                seen.append(num)
                cur = seen.count - 1
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun lastVisitedIntegers(nums: IntArray): List<Int> {
        val seen = java.util.ArrayDeque<Int>()
        val ans = mutableListOf<Int>()
        for (x in nums) {
            if (x != -1) {
                seen.addLast(x)
            } else {
                if (seen.isNotEmpty()) {
                    ans.add(seen.removeLast())
                } else {
                    ans.add(-1)
                }
            }
        }
        return ans
    }
}
```

## Dart

```dart
class Solution {
  List<int> lastVisitedIntegers(List<int> nums) {
    List<int> seen = [];
    List<int> ans = [];
    int idx = -1;
    for (int v in nums) {
      if (v == -1) {
        if (idx >= 0) {
          ans.add(seen[idx]);
          idx--;
        } else {
          ans.add(-1);
        }
      } else {
        seen.add(v);
        idx = seen.length - 1;
      }
    }
    return ans;
  }
}
```

## Golang

```go
func lastVisitedIntegers(nums []int) []int {
	seen := make([]int, 0, len(nums))
	ans := make([]int, 0, len(nums))

	for _, v := range nums {
		if v != -1 {
			seen = append(seen, v)
		} else {
			if len(seen) > 0 {
				val := seen[len(seen)-1]
				seen = seen[:len(seen)-1]
				ans = append(ans, val)
			} else {
				ans = append(ans, -1)
			}
		}
	}
	return ans
}
```

## Ruby

```ruby
def last_visited_integers(nums)
  stack = []
  ans = []
  nums.each do |x|
    if x == -1
      ans << (stack.empty? ? -1 : stack.pop)
    else
      stack << x
    end
  end
  ans
end
```

## Scala

```scala
object Solution {
    def lastVisitedIntegers(nums: Array[Int]): List[Int] = {
        import scala.collection.mutable.ArrayBuffer
        val seen = new ArrayBuffer[Int]()
        var idx = -1
        val ans = new ArrayBuffer[Int]()
        for (v <- nums) {
            if (v == -1) {
                if (idx >= 0) {
                    ans += seen(idx)
                    idx -= 1
                } else {
                    ans += -1
                }
            } else {
                seen += v
                idx = seen.size - 1
            }
        }
        ans.toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn last_visited_integers(nums: Vec<i32>) -> Vec<i32> {
        let mut seen: Vec<i32> = Vec::new();
        let mut ans: Vec<i32> = Vec::new();
        let mut idx: i32 = -1; // index of the next available "last visited" integer

        for &v in nums.iter() {
            if v != -1 {
                seen.push(v);
                idx = (seen.len() as i32) - 1;
            } else {
                if idx >= 0 {
                    ans.push(seen[idx as usize]);
                    idx -= 1;
                } else {
                    ans.push(-1);
                }
            }
        }

        ans
    }
}
```

## Racket

```racket
(define/contract (last-visited-integers nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let loop ((rest nums) (seen '()) (idx -1) (ans '()))
    (if (null? rest)
        (reverse ans)
        (let ((x (car rest)))
          (cond
            [(> x 0)
             (define new-seen (append seen (list x)))
             (loop (cdr rest) new-seen (sub1 (length new-seen)) ans)]
            [else
             (if (>= idx 0)
                 (let ((val (list-ref seen idx)))
                   (loop (cdr rest) seen (sub1 idx) (cons val ans)))
                 (loop (cdr rest) seen idx (cons -1 ans)))])))))
```

## Erlang

```erlang
-spec last_visited_integers(Nums :: [integer()]) -> [integer()].
last_visited_integers(Nums) ->
    {_, _, RevAns} = lists:foldl(
        fun(Elem, {Seen, Pos, Acc}) ->
            case Elem of
                -1 ->
                    if Pos >= 0 ->
                            Value = lists:nth(Pos + 1, Seen),
                            {Seen, Pos - 1, [Value | Acc]};
                       true ->
                            {Seen, Pos, [-1 | Acc]}
                    end;
                X when X > 0 ->
                    NewSeen = Seen ++ [X],
                    NewPos = length(NewSeen) - 1,
                    {NewSeen, NewPos, Acc}
            end
        end,
        {[], -1, []},
        Nums),
    lists:reverse(RevAns).
```

## Elixir

```elixir
defmodule Solution do
  @spec last_visited_integers(nums :: [integer]) :: [integer]
  def last_visited_integers(nums) do
    {ans_rev, _stack} =
      Enum.reduce(nums, {[], []}, fn
        -1, {ans_acc, []} ->
          {[-1 | ans_acc], []}

        -1, {ans_acc, [top | rest]} ->
          {[top | ans_acc], rest}

        x, {ans_acc, stack} when x != -1 ->
          {ans_acc, [x | stack]}
      end)

    Enum.reverse(ans_rev)
  end
end
```
