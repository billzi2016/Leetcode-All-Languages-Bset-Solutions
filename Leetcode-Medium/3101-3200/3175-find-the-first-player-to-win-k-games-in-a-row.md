# 3175. Find The First Player to win K Games in a Row

## Cpp

```cpp
class Solution {
public:
    int findWinningPlayer(vector<int>& skills, int k) {
        int n = skills.size();
        // If k is large enough, the strongest player will eventually win.
        if (k >= n - 1) {
            int maxIdx = 0;
            for (int i = 1; i < n; ++i) {
                if (skills[i] > skills[maxIdx]) maxIdx = i;
            }
            return maxIdx;
        }

        deque<pair<int,int>> dq;
        for (int i = 0; i < n; ++i) dq.emplace_back(skills[i], i);

        auto champion = dq.front(); dq.pop_front();
        int winCnt = 0;

        while (true) {
            if (winCnt == k) return champion.second;
            auto opponent = dq.front(); dq.pop_front();

            if (champion.first > opponent.first) {
                ++winCnt;
                dq.push_back(opponent); // loser goes to back
            } else {
                dq.push_back(champion); // previous champion loses
                champion = opponent;    // new champion
                winCnt = 1;             // just won this match
            }
        }
        return -1; // unreachable
    }
};
```

## Java

```java
class Solution {
    public int findWinningPlayer(int[] skills, int k) {
        int n = skills.length;
        // Find the index of the maximum skill
        int maxSkill = skills[0];
        int idxMax = 0;
        for (int i = 1; i < n; i++) {
            if (skills[i] > maxSkill) {
                maxSkill = skills[i];
                idxMax = i;
            }
        }
        // If k is large enough, the maximum skill player will inevitably win
        if (k >= n) {
            return idxMax;
        }

        int championIdx = 0;          // current winner's original index
        int championSkill = skills[championIdx];
        int streak = 0;               // consecutive wins of current champion

        for (int i = 1; ; i++) {
            int opponentIdx = i % n;
            int opponentSkill = skills[opponentIdx];

            if (championSkill > opponentSkill) {
                streak++;
            } else {
                championSkill = opponentSkill;
                championIdx = opponentIdx;
                streak = 1; // new champion just won this match
            }

            if (streak == k) {
                return championIdx;
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def findWinningPlayer(self, skills, k):
        """
        :type skills: List[int]
        :type k: int
        :rtype: int
        """
        n = len(skills)
        # If k is large enough, the strongest player will eventually win.
        if k >= n - 1:
            max_skill = max(skills)
            return skills.index(max_skill)

        cur_max = skills[0]
        cur_idx = 0
        streak = 0

        for i in range(1, n):
            if skills[i] > cur_max:
                cur_max = skills[i]
                cur_idx = i
                streak = 1  # new champion just won this match
            else:
                streak += 1  # current champion wins another game

            if streak == k:
                return cur_idx

        # Fallback (the strongest player will eventually win)
        return cur_idx
```

## Python3

```python
from typing import List

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        # If k is large enough, only the strongest player can achieve it
        if k >= n - 1:
            max_idx = 0
            for i in range(1, n):
                if skills[i] > skills[max_idx]:
                    max_idx = i
            return max_idx

        cur = 0          # current champion's index
        win = 0          # consecutive wins of current champion
        for i in range(1, n):
            if skills[cur] > skills[i]:
                win += 1
            else:
                cur = i
                win = 1
            if win == k:
                return cur

        # If not found during the loop, the strongest player will eventually win
        max_idx = 0
        for i in range(1, n):
            if skills[i] > skills[max_idx]:
                max_idx = i
        return max_idx
```

## C

```c
int findWinningPlayer(int* skills, int skillsSize, int k) {
    // Find index of maximum skill
    int maxIdx = 0;
    for (int i = 1; i < skillsSize; ++i) {
        if (skills[i] > skills[maxIdx]) maxIdx = i;
    }
    // If k is large enough, the strongest player will eventually win
    if (k >= skillsSize - 1) return maxIdx;

    typedef struct { int val; int idx; } Node;
    int cap = skillsSize;
    Node *q = (Node*)malloc(sizeof(Node) * cap);
    // Initialize queue with all players except the first one
    int head = 0, tail = -1, size = 0;
    for (int i = 1; i < skillsSize; ++i) {
        tail = (tail + 1) % cap;
        q[tail].val = skills[i];
        q[tail].idx = i;
        ++size;
    }

    // Current champion
    Node champ;
    champ.val = skills[0];
    champ.idx = 0;
    int winCnt = 0;

    while (winCnt < k) {
        // pop opponent from front
        Node opp = q[head];
        head = (head + 1) % cap;
        --size;

        if (champ.val > opp.val) {
            ++winCnt;
            // loser goes to back
            tail = (tail + 1) % cap;
            q[tail] = opp;
            ++size;
        } else {
            // opponent becomes new champion
            // previous champion goes to back
            tail = (tail + 1) % cap;
            q[tail] = champ;
            ++size;

            champ = opp;
            winCnt = 1; // opponent just won this match
        }
    }

    free(q);
    return champ.idx;
}
```

## Csharp

```csharp
public class Solution {
    public int FindWinningPlayer(int[] skills, int k) {
        int n = skills.Length;
        // Find the maximum skill and its original index
        int maxSkill = skills[0];
        int maxIdx = 0;
        for (int i = 1; i < n; i++) {
            if (skills[i] > maxSkill) {
                maxSkill = skills[i];
                maxIdx = i;
            }
        }

        // If k is large enough, the strongest player will inevitably win
        if (k >= n - 1) return maxIdx;

        int champion = skills[0];
        int champIdx = 0;
        int wins = 0;

        for (int i = 1; ; i++) {
            int oppIdx = i % n;
            int opponent = skills[oppIdx];

            if (champion > opponent) {
                wins++;
            } else {
                champion = opponent;
                champIdx = oppIdx;
                wins = 1;
            }

            if (wins == k) return champIdx;
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} skills
 * @param {number} k
 * @return {number}
 */
var findWinningPlayer = function(skills, k) {
    const n = skills.length;
    // Find index of the maximum skill player.
    let maxIdx = 0;
    for (let i = 1; i < n; ++i) {
        if (skills[i] > skills[maxIdx]) maxIdx = i;
    }
    // If k is large enough, the strongest player will inevitably win.
    if (k >= n - 1) return maxIdx;

    let curIdx = 0;
    let curSkill = skills[0];
    let streak = 0; // consecutive wins of current champion

    for (let i = 1; ; ++i) {
        const challengerIdx = i % n;
        const challengerSkill = skills[challengerIdx];

        if (curSkill > challengerSkill) {
            ++streak;
        } else {
            curSkill = challengerSkill;
            curIdx = challengerIdx;
            streak = 1; // just won this match
        }

        if (streak === k) return curIdx;
    }
};
```

## Typescript

```typescript
function findWinningPlayer(skills: number[], k: number): number {
    const n = skills.length;
    // Find index of maximum skill
    let maxIdx = 0;
    for (let i = 1; i < n; i++) {
        if (skills[i] > skills[maxIdx]) maxIdx = i;
    }
    // If k is large enough, the strongest player will inevitably win
    if (k >= n - 1) return maxIdx;

    let championIdx = 0;
    let wins = 0;

    for (let i = 1; i < n; i++) {
        if (skills[championIdx] > skills[i]) {
            wins++;
        } else {
            championIdx = i;
            wins = 1;
        }
        if (wins === k) return championIdx;
    }

    // If not decided within one pass, the strongest player will win
    return maxIdx;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $skills
     * @param Integer $k
     * @return Integer
     */
    function findWinningPlayer($skills, $k) {
        $n = count($skills);
        // If k is large enough, the strongest player will eventually win.
        if ($k >= $n - 1) {
            $maxSkill = max($skills);
            return array_search($maxSkill, $skills);
        }

        $queue = new SplQueue();
        for ($i = 0; $i < $n; $i++) {
            $queue->enqueue($i);
        }

        $champion = $queue->dequeue(); // current player at the front
        $streak = 0;

        while (true) {
            $opponent = $queue->dequeue();

            if ($skills[$champion] > $skills[$opponent]) {
                // champion wins this round
                $streak++;
                $queue->enqueue($opponent); // loser goes to the back
            } else {
                // opponent becomes new champion
                $queue->enqueue($champion);
                $champion = $opponent;
                $streak = 1; // opponent just won this game
            }

            if ($streak == $k) {
                return $champion;
            }
        }
    }
}
```

## Swift

```swift
class Solution {
    func findWinningPlayer(_ skills: [Int], _ k: Int) -> Int {
        let n = skills.count
        // If k is large enough, the strongest player will inevitably win.
        if k >= n - 1 {
            var maxIdx = 0
            var maxSkill = skills[0]
            for i in 1..<n {
                if skills[i] > maxSkill {
                    maxSkill = skills[i]
                    maxIdx = i
                }
            }
            return maxIdx
        }
        
        var curIdx = 0
        var curSkill = skills[0]
        var streak = 0
        
        for i in 1..<n {
            if curSkill > skills[i] {
                streak += 1
            } else {
                curSkill = skills[i]
                curIdx = i
                streak = 1   // new champion just won this match
            }
            if streak == k {
                return curIdx
            }
        }
        
        // Fallback (should not reach here because answer is guaranteed)
        var maxIdx = 0
        var maxSkill = skills[0]
        for i in 1..<n {
            if skills[i] > maxSkill {
                maxSkill = skills[i]
                maxIdx = i
            }
        }
        return maxIdx
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun findWinningPlayer(skills: IntArray, k: Int): Int {
        val n = skills.size
        if (k >= n - 1) {
            var maxIdx = 0
            for (i in 1 until n) {
                if (skills[i] > skills[maxIdx]) maxIdx = i
            }
            return maxIdx
        }
        var champion = 0
        var streak = 0
        var idx = 1
        while (true) {
            if (skills[champion] > skills[idx]) {
                streak++
            } else {
                champion = idx
                streak = 1
            }
            if (streak == k) return champion
            idx = (idx + 1) % n
        }
    }
}
```

## Dart

```dart
class Solution {
  int findWinningPlayer(List<int> skills, int k) {
    int n = skills.length;
    // Map each skill to its original index.
    final Map<int, int> indexMap = {};
    for (int i = 0; i < n; i++) {
      indexMap[skills[i]] = i;
    }

    // If k is large enough, the maximum skilled player will eventually win.
    if (k >= n - 1) {
      int maxSkill = skills[0];
      for (int s in skills) {
        if (s > maxSkill) maxSkill = s;
      }
      return indexMap[maxSkill]!;
    }

    int champion = skills[0];
    int winCount = 0;

    for (int i = 1; i < n; i++) {
      int opponent = skills[i];
      if (champion > opponent) {
        winCount++;
      } else {
        champion = opponent;
        winCount = 1;
      }
      if (winCount == k) {
        return indexMap[champion]!;
      }
    }

    // Fallback (should not be reached for valid inputs).
    int maxSkill = skills.reduce((a, b) => a > b ? a : b);
    return indexMap[maxSkill]!;
  }
}
```

## Golang

```go
func findWinningPlayer(skills []int, k int) int {
	n := len(skills)
	if k >= n-1 {
		maxIdx := 0
		for i := 1; i < n; i++ {
			if skills[i] > skills[maxIdx] {
				maxIdx = i
			}
		}
		return maxIdx
	}
	champ := 0
	streak := 0
	i := 1 % n
	for {
		if skills[champ] > skills[i] {
			streak++
		} else {
			champ = i
			streak = 1
		}
		if streak == k {
			return champ
		}
		i = (i + 1) % n
	}
}
```

## Ruby

```ruby
def find_winning_player(skills, k)
  n = skills.length
  # If k is large enough, the strongest player will eventually win.
  if k >= n - 1
    return skills.each_with_index.max_by { |val, _idx| val }[1]
  end

  cur_idx = 0          # current champion's index
  win_cnt = 0          # consecutive wins of current champion

  (1...n).each do |i|
    if skills[cur_idx] > skills[i]
      win_cnt += 1
    else
      cur_idx = i
      win_cnt = 1
    end
    return cur_idx if win_cnt == k
  end

  # Fallback (should not be reached for valid inputs)
  skills.each_with_index.max_by { |val, _idx| val }[1]
end
```

## Scala

```scala
object Solution {
    def findWinningPlayer(skills: Array[Int], k: Int): Int = {
        val n = skills.length
        if (k >= n - 1) {
            var maxIdx = 0
            for (i <- 1 until n) {
                if (skills(i) > skills(maxIdx)) maxIdx = i
            }
            return maxIdx
        }

        var curSkill = skills(0)
        var curIdx = 0
        var streak = 0
        var i = 1
        while (true) {
            val oppIdx = i % n
            val oppSkill = skills(oppIdx)

            if (curSkill > oppSkill) {
                streak += 1
            } else {
                curSkill = oppSkill
                curIdx = oppIdx
                streak = 1
            }

            if (streak == k) return curIdx
            i += 1
        }
        -1 // unreachable
    }
}
```

## Rust

```rust
impl Solution {
    pub fn find_winning_player(skills: Vec<i32>, k: i32) -> i32 {
        let n = skills.len();
        // If k is large enough, the strongest player will inevitably win.
        if (k as usize) >= n - 1 {
            let mut max_idx = 0usize;
            for (i, &s) in skills.iter().enumerate() {
                if s > skills[max_idx] {
                    max_idx = i;
                }
            }
            return max_idx as i32;
        }

        let mut champion = 0usize; // index of current winner
        let mut streak = 0i32;     // consecutive wins of champion

        for i in 1..n {
            if skills[champion] > skills[i] {
                streak += 1;
            } else {
                champion = i;
                streak = 1;
            }
            if streak == k {
                return champion as i32;
            }
        }

        // Fallback (the loop should have returned already)
        champion as i32
    }
}
```

## Racket

```racket
(define/contract (find-winning-player skills k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ((n (length skills))
         (skill-vec (list->vector skills))
         (idx-hash (make-hash)))
    ;; map skill value to its original index
    (for ([i (in-range n)])
      (hash-set! idx-hash (vector-ref skill-vec i) i))
    (if (>= k (- n 1))                     ; k large enough, max skill wins
        (let loop ((i 0) (max-s -1) (max-idx -1))
          (if (= i n)
              max-idx
              (let ((val (vector-ref skill-vec i)))
                (if (> val max-s)
                    (loop (+ i 1) val i)
                    (loop (+ i 1) max-s max-idx)))))
        ;; simulate for k < n
        (let loop ((champ-skill (vector-ref skill-vec 0))
                   (wins 0)
                   (i 1))
          (cond
            [(= wins k) (hash-ref idx-hash champ-skill)]
            [(>= i n)   (hash-ref idx-hash champ-skill)] ; champion is the max after full pass
            [else
             (let ((next-skill (vector-ref skill-vec i)))
               (if (> champ-skill next-skill)
                   (let ((new-wins (+ wins 1)))
                     (if (= new-wins k)
                         (hash-ref idx-hash champ-skill)
                         (loop champ-skill new-wins (+ i 1))))
                   ;; new champion appears
                   (loop next-skill 1 (+ i 1))))])))))
```

## Erlang

```erlang
-module(solution).
-export([find_winning_player/2]).

-spec find_winning_player(Skills :: [integer()], K :: integer()) -> integer().
find_winning_player(Skills, K) ->
    N = length(Skills),
    case K >= N - 1 of
        true ->
            {_, MaxIdx} = lists:max(lists:zip(Skills, lists:seq(0, N-1))),
            MaxIdx;
        false ->
            simulate(Skills, K)
    end.

simulate(Skills, K) ->
    Indexed = lists:zip(lists:seq(0, length(Skills)-1), Skills),
    [{CurIdx, CurSkill}|Rest] = Indexed,
    loop(Rest, CurIdx, CurSkill, 0, K).

loop([], CurIdx, _CurSkill, _Streak, _K) ->
    CurIdx;
loop([{Idx, Skill}|Tail], CurIdx, CurSkill, Streak, K) ->
    if
        CurSkill > Skill ->
            NewStreak = Streak + 1,
            case NewStreak >= K of
                true -> CurIdx;
                false -> loop(Tail, CurIdx, CurSkill, NewStreak, K)
            end;
        true ->
            NewStreak = 1,
            case NewStreak >= K of
                true -> Idx;
                false -> loop(Tail, Idx, Skill, NewStreak, K)
            end
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_winning_player(skills :: [integer], k :: integer) :: integer
  def find_winning_player(skills, k) do
    tuple = List.to_tuple(skills)
    n = tuple_size(tuple)

    if k >= n - 1 do
      # maximum skill will eventually win
      {_max_val, max_idx} =
        0..(n - 1)
        |> Enum.reduce({-1, -1}, fn i, {mv, mi} ->
          val = elem(tuple, i)

          if val > mv do
            {val, i}
          else
            {mv, mi}
          end
        end)

      max_idx
    else
      # simulate the competition
      champion_idx = 0
      champion_skill = elem(tuple, 0)
      win_streak = 0

      result =
        Enum.reduce_while(1..(n - 1), {champion_idx, champion_skill, win_streak}, fn i,
                                                                                 {c_idx,
                                                                                  c_skill,
                                                                                  streak} ->
          skill_i = elem(tuple, i)

          if c_skill > skill_i do
            new_streak = streak + 1

            if new_streak == k do
              {:halt, c_idx}
            else
              {:cont, {c_idx, c_skill, new_streak}}
            end
          else
            # new champion wins this round
            new_streak = 1

            if new_streak == k do
              {:halt, i}
            else
              {:cont, {i, skill_i, new_streak}}
            end
          end
        end)

      case result do
        idx when is_integer(idx) -> idx
        {c_idx, _c_skill, _streak} -> c_idx
      end
    end
  end
end
```
