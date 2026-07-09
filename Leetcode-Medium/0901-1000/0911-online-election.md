# 0911. Online Election

## Cpp

```cpp
class TopVotedCandidate {
public:
    TopVotedCandidate(std::vector<int>& persons, std::vector<int>& times) {
        int n = persons.size();
        leaders.reserve(n);
        voteCount.resize(*std::max_element(persons.begin(), persons.end()) + 1, 0);
        int curLeader = -1;
        int maxVotes = 0;
        for (int i = 0; i < n; ++i) {
            int p = persons[i];
            if (p >= (int)voteCount.size())
                voteCount.resize(p + 1, 0);
            ++voteCount[p];
            if (voteCount[p] >= maxVotes) {
                // tie goes to most recent vote
                curLeader = p;
                maxVotes = voteCount[p];
            }
            leaders.push_back(curLeader);
        }
        this->times = times;
    }
    
    int q(int t) {
        int idx = std::upper_bound(times.begin(), times.end(), t) - times.begin() - 1;
        if (idx < 0) return -1;
        return leaders[idx];
    }
private:
    std::vector<int> times;
    std::vector<int> leaders;
    std::vector<int> voteCount;
};
```

## Java

```java
import java.util.*;

class TopVotedCandidate {

    private final int[] times;
    private final int[] leaders;

    public TopVotedCandidate(int[] persons, int[] times) {
        this.times = times.clone();
        int n = persons.length;
        leaders = new int[n];
        Map<Integer, Integer> cnt = new HashMap<>();
        int curLeader = -1;
        int maxVotes = 0;
        for (int i = 0; i < n; i++) {
            int p = persons[i];
            int votes = cnt.getOrDefault(p, 0) + 1;
            cnt.put(p, votes);
            if (votes >= maxVotes) { // tie goes to most recent vote
                curLeader = p;
                maxVotes = votes;
            }
            leaders[i] = curLeader;
        }
    }

    public int q(int t) {
        int idx = Arrays.binarySearch(times, t);
        if (idx < 0) {
            idx = -idx - 2; // largest index with times[idx] < t
        }
        return leaders[idx];
    }
}

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * TopVotedCandidate obj = new TopVotedCandidate(persons, times);
 * int param_1 = obj.q(t);
 */
```

## Python

```python
class TopVotedCandidate(object):
    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        from collections import defaultdict
        self.times = times
        self.leaders = []
        vote_count = defaultdict(int)
        leader = None
        max_votes = 0
        for p in persons:
            vote_count[p] += 1
            if vote_count[p] >= max_votes:
                # tie or new max, recent vote wins
                leader = p
                max_votes = vote_count[p]
            self.leaders.append(leader)

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        import bisect
        idx = bisect.bisect_right(self.times, t) - 1
        return self.leaders[idx]
```

## Python3

```python
class TopVotedCandidate:
    def __init__(self, persons, times):
        from collections import defaultdict
        self.times = times
        vote_counts = defaultdict(int)
        leaders = []
        current_leader = None
        max_votes = 0
        for p in persons:
            vote_counts[p] += 1
            if vote_counts[p] >= max_votes:
                # tie or new max, recent vote wins
                current_leader = p
                max_votes = vote_counts[p]
            leaders.append(current_leader)
        self.leaders = leaders

    def q(self, t):
        import bisect
        idx = bisect.bisect_right(self.times, t) - 1
        return self.leaders[idx]
```

## C

```c
#include <stdlib.h>

typedef struct {
    int *times;
    int timesSize;
    int *leaders;
} TopVotedCandidate;

TopVotedCandidate* topVotedCandidateCreate(int* persons, int personsSize, int* times, int timesSize) {
    TopVotedCandidate *obj = (TopVotedCandidate*)malloc(sizeof(TopVotedCandidate));
    obj->timesSize = timesSize;
    obj->times = (int*)malloc(timesSize * sizeof(int));
    for (int i = 0; i < timesSize; ++i) {
        obj->times[i] = times[i];
    }
    obj->leaders = (int*)malloc(timesSize * sizeof(int));

    int *cnt = (int*)calloc(personsSize, sizeof(int));
    int leader = -1;
    int maxVotes = 0;

    for (int i = 0; i < timesSize; ++i) {
        int p = persons[i];
        cnt[p]++;
        if (cnt[p] >= maxVotes) { // tie goes to most recent vote
            maxVotes = cnt[p];
            leader = p;
        }
        obj->leaders[i] = leader;
    }

    free(cnt);
    return obj;
}

int topVotedCandidateQ(TopVotedCandidate* obj, int t) {
    int low = 0, high = obj->timesSize - 1, ans = 0;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (obj->times[mid] <= t) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return obj->leaders[ans];
}

void topVotedCandidateFree(TopVotedCandidate* obj) {
    if (!obj) return;
    free(obj->times);
    free(obj->leaders);
    free(obj);
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class TopVotedCandidate {
    private readonly int[] _times;
    private readonly int[] _leaders;

    public TopVotedCandidate(int[] persons, int[] times) {
        int n = persons.Length;
        _times = new int[n];
        _leaders = new int[n];

        var voteCount = new Dictionary<int, int>();
        int currentLeader = -1;
        int maxVotes = 0;

        for (int i = 0; i < n; i++) {
            int p = persons[i];
            _times[i] = times[i];

            if (!voteCount.ContainsKey(p))
                voteCount[p] = 0;
            voteCount[p]++;

            int cnt = voteCount[p];
            if (cnt >= maxVotes) {
                // tie goes to most recent vote, so use >=
                currentLeader = p;
                maxVotes = cnt;
            }
            _leaders[i] = currentLeader;
        }
    }

    public int Q(int t) {
        int idx = Array.BinarySearch(_times, t);
        if (idx < 0) {
            idx = ~idx - 1; // index of greatest element less than t
        }
        return _leaders[idx];
    }
}

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * TopVotedCandidate obj = new TopVotedCandidate(persons, times);
 * int param_1 = obj.Q(t);
 */
```

## Javascript

```javascript
/**
 * @param {number[]} persons
 * @param {number[]} times
 */
var TopVotedCandidate = function(persons, times) {
    this.times = times;
    const voteCount = new Map();
    let currentLeader = -1;
    let maxVotes = 0;
    this.leaders = [];
    
    for (let i = 0; i < persons.length; i++) {
        const p = persons[i];
        const cnt = (voteCount.get(p) || 0) + 1;
        voteCount.set(p, cnt);
        if (cnt >= maxVotes) { // tie goes to most recent
            currentLeader = p;
            maxVotes = cnt;
        }
        this.leaders.push(currentLeader);
    }
};

/** 
 * @param {number} t
 * @return {number}
 */
TopVotedCandidate.prototype.q = function(t) {
    const times = this.times;
    let lo = 0, hi = times.length - 1;
    while (lo <= hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (times[mid] <= t) {
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    // hi is the last index with times[hi] <= t
    return this.leaders[hi];
};
```

## Typescript

```typescript
class TopVotedCandidate {
    private times: number[];
    private leaders: number[];

    constructor(persons: number[], times: number[]) {
        this.times = times;
        const voteCount = new Map<number, number>();
        this.leaders = [];
        let currentLeader = -1;

        for (let i = 0; i < persons.length; ++i) {
            const p = persons[i];
            const cnt = (voteCount.get(p) ?? 0) + 1;
            voteCount.set(p, cnt);

            if (currentLeader === -1 || cnt >= (voteCount.get(currentLeader) ?? 0)) {
                currentLeader = p;
            }
            this.leaders.push(currentLeader);
        }
    }

    q(t: number): number {
        let lo = 0, hi = this.times.length - 1;
        let idx = -1;
        while (lo <= hi) {
            const mid = Math.floor((lo + hi) / 2);
            if (this.times[mid] <= t) {
                idx = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return this.leaders[idx];
    }
}

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * var obj = new TopVotedCandidate(persons, times)
 * var param_1 = obj.q(t)
 */
```

## Php

```php
class TopVotedCandidate {
    private $times;
    private $leaders;

    /**
     * @param Integer[] $persons
     * @param Integer[] $times
     */
    function __construct($persons, $times) {
        $this->times = $times;
        $counts = [];
        $currentLeader = -1;
        $currentCount = 0;
        $this->leaders = [];

        $n = count($persons);
        for ($i = 0; $i < $n; $i++) {
            $p = $persons[$i];
            if (!isset($counts[$p])) {
                $counts[$p] = 0;
            }
            $counts[$p]++;

            if ($counts[$p] >= $currentCount) { // tie goes to most recent
                $currentLeader = $p;
                $currentCount = $counts[$p];
            }
            $this->leaders[] = $currentLeader;
        }
    }

    /**
     * @param Integer $t
     * @return Integer
     */
    function q($t) {
        $l = 0;
        $r = count($this->times) - 1;
        $ans = 0;

        while ($l <= $r) {
            $mid = intdiv($l + $r, 2);
            if ($this->times[$mid] <= $t) {
                $ans = $mid;
                $l = $mid + 1;
            } else {
                $r = $mid - 1;
            }
        }

        return $this->leaders[$ans];
    }
}
```

## Swift

```swift
class TopVotedCandidate {
    private let times: [Int]
    private let leaders: [Int]

    init(_ persons: [Int], _ times: [Int]) {
        self.times = times
        var voteCount = [Int: Int]()
        var currentLeader = -1
        var maxVotes = 0
        var leaderList = [Int]()

        for person in persons {
            let newCount = (voteCount[person] ?? 0) + 1
            voteCount[person] = newCount

            if newCount >= maxVotes {
                currentLeader = person
                maxVotes = newCount
            }
            leaderList.append(currentLeader)
        }

        self.leaders = leaderList
    }

    func q(_ t: Int) -> Int {
        var low = 0
        var high = times.count - 1

        while low < high {
            let mid = (low + high + 1) / 2
            if times[mid] <= t {
                low = mid
            } else {
                high = mid - 1
            }
        }

        return leaders[low]
    }
}
```

## Kotlin

```kotlin
class TopVotedCandidate(persons: IntArray, times: IntArray) {
    private val timesArr = times
    private val leaders: IntArray

    init {
        val n = persons.size
        leaders = IntArray(n)
        val voteCount = HashMap<Int, Int>()
        var currentLeader = -1
        var maxVotes = 0
        for (i in 0 until n) {
            val p = persons[i]
            val cnt = (voteCount[p] ?: 0) + 1
            voteCount[p] = cnt
            if (cnt >= maxVotes) { // tie goes to most recent
                currentLeader = p
                maxVotes = cnt
            }
            leaders[i] = currentLeader
        }
    }

    fun q(t: Int): Int {
        var lo = 0
        var hi = timesArr.size - 1
        while (lo < hi) {
            val mid = (lo + hi + 1) ushr 1
            if (timesArr[mid] <= t) {
                lo = mid
            } else {
                hi = mid - 1
            }
        }
        return leaders[lo]
    }
}

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * var obj = TopVotedCandidate(persons, times)
 * var param_1 = obj.q(t)
 */
```

## Dart

```dart
class TopVotedCandidate {
  final List<int> _times;
  final List<int> _leaders;

  TopVotedCandidate(List<int> persons, List<int> times)
      : _times = List.from(times),
        _leaders = [] {
    final Map<int, int> count = {};
    int curLeader = -1;
    int maxVotes = 0;
    for (int i = 0; i < persons.length; i++) {
      final int p = persons[i];
      count[p] = (count[p] ?? 0) + 1;
      final int votes = count[p]!;
      if (votes >= maxVotes) {
        curLeader = p;
        maxVotes = votes;
      }
      _leaders.add(curLeader);
    }
  }

  int q(int t) {
    int left = 0, right = _times.length - 1;
    int ans = 0;
    while (left <= right) {
      final int mid = (left + right) >> 1;
      if (_times[mid] <= t) {
        ans = mid;
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
    return _leaders[ans];
  }
}

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * TopVotedCandidate obj = TopVotedCandidate(persons, times);
 * int param1 = obj.q(t);
 */
```

## Golang

```go
import "sort"

type TopVotedCandidate struct {
	times   []int
	leaders []int
}

func Constructor(persons []int, times []int) TopVotedCandidate {
	count := make(map[int]int)
	leaders := make([]int, len(persons))
	curLeader := -1
	maxCnt := 0

	for i, p := range persons {
		count[p]++
		if count[p] >= maxCnt {
			curLeader = p
			maxCnt = count[p]
		}
		leaders[i] = curLeader
	}

	return TopVotedCandidate{
		times:   append([]int(nil), times...),
		leaders: leaders,
	}
}

func (this *TopVotedCandidate) Q(t int) int {
	idx := sort.Search(len(this.times), func(i int) bool { return this.times[i] > t }) - 1
	return this.leaders[idx]
}
```

## Ruby

```ruby
class TopVotedCandidate
  def initialize(persons, times)
    @times = times
    @leaders = []
    count = Hash.new(0)
    leader = -1
    persons.each_with_index do |p, i|
      count[p] += 1
      if leader == -1 || count[p] >= count[leader]
        leader = p
      end
      @leaders << leader
    end
  end

  def q(t)
    l = 0
    r = @times.length - 1
    while l <= r
      mid = (l + r) / 2
      if @times[mid] <= t
        l = mid + 1
      else
        r = mid - 1
      end
    end
    @leaders[r]
  end
end
```

## Scala

```scala
class TopVotedCandidate(_persons: Array[Int], _times: Array[Int]) {
  private val times: Array[Int] = _times
  private val leaders: Array[Int] = new Array[Int](_times.length)

  {
    import scala.collection.mutable
    val cnt = mutable.Map[Int, Int]().withDefaultValue(0)
    var curLeader = -1
    var maxCnt = 0
    for (i <- _persons.indices) {
      val p = _persons(i)
      val c = cnt(p) + 1
      cnt(p) = c
      if (c >= maxCnt) {
        curLeader = p
        maxCnt = c
      }
      leaders(i) = curLeader
    }
  }

  def q(t: Int): Int = {
    var lo = 0
    var hi = times.length - 1
    while (lo <= hi) {
      val mid = (lo + hi) >>> 1
      if (times(mid) <= t) lo = mid + 1 else hi = mid - 1
    }
    leaders(hi)
  }
}
```

## Rust

```rust
struct TopVotedCandidate {
    times: Vec<i32>,
    leaders: Vec<i32>,
}

impl TopVotedCandidate {
    fn new(persons: Vec<i32>, times: Vec<i32>) -> Self {
        use std::collections::HashMap;
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        let mut leader = -1;
        let mut max_votes = 0;
        let mut leaders = Vec::with_capacity(persons.len());

        for (&p, &t) in persons.iter().zip(times.iter()) {
            let e = cnt.entry(p).or_insert(0);
            *e += 1;
            if *e >= max_votes {
                // tie or new maximum: current person becomes leader (most recent wins ties)
                max_votes = *e;
                leader = p;
            }
            leaders.push(leader);
        }

        TopVotedCandidate { times, leaders }
    }

    fn q(&self, t: i32) -> i32 {
        // Find the last index with time <= t
        let idx = match self.times.binary_search(&t) {
            Ok(i) => i,
            Err(i) => {
                if i == 0 { return -1; } // should not happen per constraints
                i - 1
            }
        };
        self.leaders[idx]
    }
}
```

## Racket

```racket
(define top-voted-candidate%
  (class object%
    (init-field persons times)
    (super-new)

    ;; number of votes
    (define n (length persons))
    ;; vector for fast random access to times
    (define times-vec (list->vector times))
    ;; leaders[i] = person leading after i‑th vote (inclusive)
    (define leaders (make-vector n))

    ;; pre‑compute the leader after each vote
    (let* ([cnt (make-hash)]          ; person -> vote count
           [current-leader -1]
           [max-count 0])
      (for ([i (in-range n)])
        (define p (list-ref persons i))
        (hash-set! cnt p (+ (hash-ref cnt p 0) 1))
        (define c (hash-ref cnt p))
        ;; if this person ties or exceeds the max, they become leader
        (when (>= c max-count)
          (set! current-leader p)
          (set! max-count c))
        (vector-set! leaders i current-leader)))

    ;; binary search for greatest index with times[idx] <= t
    (define/public (q t)
      (let loop ([lo 0] [hi (- n 1)] [ans -1])
        (if (> lo hi)
            (if (= ans -1)
                -1
                (vector-ref leaders ans))
            (let* ([mid (quotient (+ lo hi) 2)]
                   [mid-time (vector-ref times-vec mid)])
              (if (<= mid-time t)
                  (loop (+ mid 1) hi mid)
                  (loop lo (- mid 1) ans)))))))
```

## Erlang

```erlang
-module(solution).
-export([top_voted_candidate_init_/2, top_voted_candidate_q/1]).

-spec top_voted_candidate_init_(Persons :: [integer()], Times :: [integer()]) -> any().
top_voted_candidate_init_(Persons, Times) ->
    % Compute leader after each vote
    {LeadersRev, _Acc} = lists:foldl(
        fun({P,_T}, {LeadersAcc, Acc}) ->
            CountMap = maps:get(counts, Acc),
            CurLeader = maps:get(leader, Acc),
            CurCnt = maps:get(leader_cnt, Acc),

            NewCnt = maps:get(P, CountMap, 0) + 1,
            CountMap2 = maps:put(P, NewCnt, CountMap),

            {NewLeader, NewLeaderCnt} =
                if
                    NewCnt > CurCnt -> {P, NewCnt};
                    NewCnt == CurCnt -> {P, NewCnt}; % recent vote wins on tie
                    true -> {CurLeader, CurCnt}
                end,
            {[NewLeader | LeadersAcc],
             #{counts => CountMap2, leader => NewLeader, leader_cnt => NewLeaderCnt}}
        end,
        {[], #{counts => #{}, leader => undefined, leader_cnt => 0}},
        lists:zip(Persons, Times)
    ),
    LeadersTuple = list_to_tuple(lists:reverse(LeadersRev)),
    TimesTuple = list_to_tuple(Times),
    put(state, #{times => TimesTuple, leaders => LeadersTuple}),
    ok.

-spec top_voted_candidate_q(T :: integer()) -> integer().
top_voted_candidate_q(T) ->
    State = get(state),
    Times = maps:get(times, State),
    Leaders = maps:get(leaders, State),
    Index = binary_search(Times, T, 0, tuple_size(Times) - 1),
    element(Index + 1, Leaders).

binary_search(_Times, _Target, Low, High) when Low > High ->
    High;
binary_search(Times, Target, Low, High) ->
    Mid = (Low + High) div 2,
    TimeMid = element(Mid + 1, Times),
    if
        TimeMid =< Target -> binary_search(Times, Target, Mid + 1, High);
        true -> binary_search(Times, Target, Low, Mid - 1)
    end.
```

## Elixir

```elixir
defmodule TopVotedCandidate do
  @spec init_(persons :: [integer], times :: [integer]) :: any
  def init_(persons, times) do
    {counts, _max_votes, leaders_rev} =
      Enum.reduce(persons, {%{}, 0, []}, fn person, {cnts, max_v, acc} ->
        new_cnt = Map.get(cnts, person, 0) + 1
        cnts = Map.put(cnts, person, new_cnt)

        if new_cnt >= max_v do
          {cnts, new_cnt, [person | acc]}
        else
          {cnts, max_v, [hd(acc) | tl(acc)]}
        end
      end)

    leaders = List.to_tuple(Enum.reverse(leaders_rev))
    times_t = List.to_tuple(times)
    Process.put(:top_voted_data, {times_t, leaders})
  end

  @spec q(t :: integer) :: integer
  def q(t) do
    {times_t, leaders_t} = Process.get(:top_voted_data)
    idx = find_idx(times_t, t)
    elem(leaders_t, idx)
  end

  defp find_idx(times_t, target) do
    len = tuple_size(times_t)
    binary_search(times_t, target, 0, len - 1)
  end

  defp binary_search(_times_t, _target, low, high) when low > high do
    high
  end

  defp binary_search(times_t, target, low, high) do
    mid = div(low + high, 2)

    if elem(times_t, mid) <= target do
      binary_search(times_t, target, mid + 1, high)
    else
      binary_search(times_t, target, low, mid - 1)
    end
  end
end
```
