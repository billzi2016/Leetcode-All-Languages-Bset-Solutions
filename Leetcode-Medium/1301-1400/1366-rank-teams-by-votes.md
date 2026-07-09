# 1366. Rank Teams by Votes

## Cpp

```cpp
class Solution {
public:
    string rankTeams(vector<string>& votes) {
        int m = votes.size();
        int n = votes[0].size(); // number of teams
        int cnt[26][26] = {}; // cnt[team][position]
        for (const string& v : votes) {
            for (int i = 0; i < n; ++i) {
                cnt[v[i] - 'A'][i]++;
            }
        }
        vector<char> teams(votes[0].begin(), votes[0].end());
        sort(teams.begin(), teams.end(), [&](char a, char b) {
            int ia = a - 'A', ib = b - 'A';
            for (int i = 0; i < n; ++i) {
                if (cnt[ia][i] != cnt[ib][i])
                    return cnt[ia][i] > cnt[ib][i];
            }
            return a < b;
        });
        string res;
        for (char c : teams) res += c;
        return res;
    }
};
```

## Java

```java
class Solution {
    public String rankTeams(String[] votes) {
        int n = votes[0].length();
        int[][] cnt = new int[26][n];
        for (String vote : votes) {
            for (int i = 0; i < n; i++) {
                char c = vote.charAt(i);
                cnt[c - 'A'][i]++;
            }
        }
        Character[] teams = new Character[n];
        for (int i = 0; i < n; i++) {
            teams[i] = votes[0].charAt(i);
        }
        java.util.Arrays.sort(teams, (a, b) -> {
            int[] ca = cnt[a - 'A'];
            int[] cb = cnt[b - 'A'];
            for (int i = 0; i < n; i++) {
                if (ca[i] != cb[i]) return cb[i] - ca[i];
            }
            return a - b;
        });
        StringBuilder sb = new StringBuilder();
        for (char c : teams) sb.append(c);
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        from functools import cmp_to_key

        if not votes:
            return ""

        m = len(votes[0])
        # initialize count dict for each team
        counts = {c: [0] * m for c in votes[0]}
        for vote in votes:
            for i, ch in enumerate(vote):
                counts[ch][i] += 1

        teams = list(counts.keys())

        def compare(a, b):
            for i in range(m):
                if counts[a][i] != counts[b][i]:
                    # higher count should come first
                    return -1 if counts[a][i] > counts[b][i] else 1
            # all position counts equal, alphabetical order
            return -1 if a < b else 1

        teams.sort(key=cmp_to_key(compare))
        return "".join(teams)
```

## Python3

```python
from typing import List

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if not votes:
            return ""
        m = len(votes[0])
        cnt = {ch: [0] * m for ch in votes[0]}
        for vote in votes:
            for i, ch in enumerate(vote):
                cnt[ch][i] += 1
        teams = list(cnt.keys())
        teams.sort(key=lambda c: (tuple(-x for x in cnt[c]), c))
        return "".join(teams)
```

## C

```c
#include <stdlib.h>
#include <string.h>

static int teamCount;
static int cnt[26][26];
static char nameArr[26];

static int cmpIdx(const void *a, const void *b) {
    int i = *(const int *)a;
    int j = *(const int *)b;
    for (int pos = 0; pos < teamCount; ++pos) {
        if (cnt[i][pos] != cnt[j][pos])
            return cnt[j][pos] - cnt[i][pos]; // higher count first
    }
    return nameArr[i] - nameArr[j]; // alphabetical
}

char* rankTeams(char** votes, int votesSize) {
    if (votesSize == 0) return NULL;
    int n = strlen(votes[0]);          // number of teams
    teamCount = n;

    int map[26];
    for (int i = 0; i < 26; ++i) map[i] = -1;

    // assign indices based on first vote string
    for (int i = 0; i < n; ++i) {
        char c = votes[0][i];
        int idx = i;
        map[c - 'A'] = idx;
        nameArr[idx] = c;
    }

    // count rankings
    memset(cnt, 0, sizeof(cnt));
    for (int v = 0; v < votesSize; ++v) {
        char *s = votes[v];
        for (int pos = 0; pos < n; ++pos) {
            int idx = map[s[pos] - 'A'];
            cnt[idx][pos]++;
        }
    }

    // sort indices
    int *order = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) order[i] = i;
    qsort(order, n, sizeof(int), cmpIdx);

    // build result string
    char *res = (char *)malloc((n + 1) * sizeof(char));
    for (int i = 0; i < n; ++i) {
        res[i] = nameArr[order[i]];
    }
    res[n] = '\0';

    free(order);
    return res;
}
```

## Csharp

```csharp
public class Solution
{
    public string RankTeams(string[] votes)
    {
        int teamCount = votes[0].Length;
        int[,] cnt = new int[26, 26]; // [team][position]

        foreach (var vote in votes)
        {
            for (int pos = 0; pos < vote.Length; pos++)
            {
                int idx = vote[pos] - 'A';
                cnt[idx, pos]++;
            }
        }

        List<char> teams = new List<char>();
        foreach (char c in votes[0])
            teams.Add(c);

        teams.Sort((a, b) =>
        {
            int ai = a - 'A', bi = b - 'A';
            for (int i = 0; i < teamCount; i++)
            {
                if (cnt[ai, i] != cnt[bi, i])
                    return cnt[bi, i].CompareTo(cnt[ai, i]); // descending
            }
            return a.CompareTo(b); // alphabetical tie‑breaker
        });

        return new string(teams.ToArray());
    }
}
```

## Javascript

```javascript
var rankTeams = function(votes) {
    if (!votes || votes.length === 0) return "";
    const m = votes[0].length;
    const cnt = {};
    for (const vote of votes) {
        for (let i = 0; i < vote.length; ++i) {
            const ch = vote[i];
            if (!cnt[ch]) cnt[ch] = new Array(m).fill(0);
            cnt[ch][i]++;
        }
    }
    const teams = Object.keys(cnt);
    teams.sort((a, b) => {
        const ca = cnt[a], cb = cnt[b];
        for (let i = 0; i < m; ++i) {
            if (ca[i] !== cb[i]) return cb[i] - ca[i];
        }
        return a.localeCompare(b);
    });
    return teams.join('');
};
```

## Typescript

```typescript
function rankTeams(votes: string[]): string {
    const m = votes[0].length;
    const cnt: Record<string, number[]> = {};

    for (const vote of votes) {
        for (let i = 0; i < m; ++i) {
            const ch = vote[i];
            if (!cnt[ch]) cnt[ch] = new Array(m).fill(0);
            cnt[ch][i]++;
        }
    }

    const teams = Object.keys(cnt);
    teams.sort((a, b) => {
        for (let i = 0; i < m; ++i) {
            const diff = (cnt[b][i] ?? 0) - (cnt[a][i] ?? 0);
            if (diff !== 0) return diff;
        }
        return a < b ? -1 : a > b ? 1 : 0;
    });

    return teams.join('');
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $votes
     * @return String
     */
    function rankTeams($votes) {
        $n = strlen($votes[0]);
        $teams = str_split($votes[0]);

        // Initialize count matrix
        $cnt = [];
        foreach ($teams as $t) {
            $cnt[$t] = array_fill(0, $n, 0);
        }

        // Count votes per position for each team
        foreach ($votes as $vote) {
            $chars = str_split($vote);
            foreach ($chars as $pos => $team) {
                $cnt[$team][$pos]++;
            }
        }

        // Custom sort according to the ranking rules
        usort($teams, function($a, $b) use ($cnt, $n) {
            for ($i = 0; $i < $n; $i++) {
                if ($cnt[$a][$i] != $cnt[$b][$i]) {
                    // Higher count should come first
                    return $cnt[$b][$i] <=> $cnt[$a][$i];
                }
            }
            // If all counts are equal, sort alphabetically
            return $a <=> $b;
        });

        return implode('', $teams);
    }
}
```

## Swift

```swift
class Solution {
    func rankTeams(_ votes: [String]) -> String {
        guard let firstVote = votes.first else { return "" }
        let teamCount = firstVote.count
        var rank = [Character: [Int]]()
        
        // Initialize count arrays for each team
        for ch in firstVote {
            rank[ch] = Array(repeating: 0, count: teamCount)
        }
        
        // Count votes per position
        for vote in votes {
            let chars = Array(vote)
            for (pos, ch) in chars.enumerated() {
                rank[ch]![pos] += 1
            }
        }
        
        // Sort teams according to the ranking rules
        let sortedTeams = rank.keys.sorted { a, b in
            let ra = rank[a]!
            let rb = rank[b]!
            for i in 0..<teamCount {
                if ra[i] != rb[i] {
                    return ra[i] > rb[i]
                }
            }
            // If all counts are equal, sort alphabetically
            return a < b
        }
        
        return String(sortedTeams)
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun rankTeams(votes: Array<String>): String {
        val n = votes[0].length
        val counts = mutableMapOf<Char, IntArray>()
        for (c in votes[0]) {
            counts[c] = IntArray(n)
        }
        for (vote in votes) {
            for (i in vote.indices) {
                val c = vote[i]
                counts[c]!![i]++
            }
        }
        val teams = counts.keys.toMutableList()
        teams.sortWith { a, b ->
            val ca = counts[a]!!
            val cb = counts[b]!!
            for (i in 0 until n) {
                if (ca[i] != cb[i]) return@sortWith cb[i] - ca[i]
            }
            a.compareTo(b)
        }
        val sb = StringBuilder()
        for (c in teams) sb.append(c)
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String rankTeams(List<String> votes) {
    if (votes.isEmpty) return "";
    int n = votes[0].length;
    // Initialize count map for each team
    Map<String, List<int>> cnt = {};
    for (int i = 0; i < n; i++) {
      String ch = votes[0][i];
      cnt[ch] = List.filled(n, 0);
    }
    // Count positions
    for (var vote in votes) {
      for (int pos = 0; pos < vote.length; pos++) {
        String ch = vote[pos];
        cnt[ch]![pos]++;
      }
    }
    // List of teams to sort
    List<String> teams = votes[0].split('');
    teams.sort((a, b) {
      List<int> ca = cnt[a]!;
      List<int> cb = cnt[b]!;
      for (int i = 0; i < n; i++) {
        if (ca[i] != cb[i]) return cb[i] - ca[i]; // descending
      }
      return a.compareTo(b); // alphabetical
    });
    return teams.join();
  }
}
```

## Golang

```go
import "sort"

func rankTeams(votes []string) string {
	if len(votes) == 0 {
		return ""
	}
	n := len(votes[0])

	// count[team][position] = number of votes where team appears at that position
	count := make(map[byte][]int)
	for i := 0; i < n; i++ {
		ch := votes[0][i]
		count[ch] = make([]int, n)
	}
	for _, v := range votes {
		for pos := 0; pos < n; pos++ {
			ch := v[pos]
			count[ch][pos]++
		}
	}

	teams := []byte(votes[0])
	sort.Slice(teams, func(i, j int) bool {
		a, b := teams[i], teams[j]
		for k := 0; k < n; k++ {
			if count[a][k] != count[b][k] {
				return count[a][k] > count[b][k]
			}
		}
		return a < b
	})

	return string(teams)
}
```

## Ruby

```ruby
def rank_teams(votes)
  return "" if votes.empty?
  m = votes[0].length
  counts = Hash.new { |h, k| h[k] = Array.new(m, 0) }

  votes.each do |vote|
    vote.chars.each_with_index do |team, idx|
      counts[team][idx] += 1
    end
  end

  teams = counts.keys
  sorted = teams.sort_by { |team| counts[team].map { |c| -c } + [team] }
  sorted.join
end
```

## Scala

```scala
object Solution {
  def rankTeams(votes: Array[String]): String = {
    val n = votes(0).length
    val counts = scala.collection.mutable.Map[Char, Array[Int]]()
    for (c <- votes(0)) {
      counts(c) = Array.fill(n)(0)
    }
    for (vote <- votes) {
      var i = 0
      while (i < n) {
        val c = vote(i)
        counts(c)(i) += 1
        i += 1
      }
    }
    val teams = votes(0).toList
    val sorted = teams.sortWith { (a, b) =>
      val ca = counts(a)
      val cb = counts(b)
      var i = 0
      while (i < n && ca(i) == cb(i)) i += 1
      if (i == n) a < b else ca(i) > cb(i)
    }
    sorted.mkString
  }
}
```

## Rust

```rust
impl Solution {
    pub fn rank_teams(votes: Vec<String>) -> String {
        if votes.is_empty() {
            return String::new();
        }
        let m = votes[0].len();
        use std::collections::HashMap;
        let mut cnt: HashMap<char, Vec<usize>> = HashMap::new();

        for vote in &votes {
            for (pos, ch) in vote.chars().enumerate() {
                cnt.entry(ch).or_insert(vec![0; m])[pos] += 1;
            }
        }

        let mut teams: Vec<char> = cnt.keys().cloned().collect();
        teams.sort_by(|&a, &b| {
            let ca = &cnt[&a];
            let cb = &cnt[&b];
            for i in 0..m {
                if ca[i] != cb[i] {
                    return cb[i].cmp(&ca[i]); // higher count first
                }
            }
            a.cmp(&b) // alphabetical tie‑breaker
        });

        teams.iter().collect()
    }
}
```

## Racket

```racket
(define/contract (rank-teams votes)
  (-> (listof string?) string?)
  (let* ((first-vote (car votes))
         (team-count (string-length first-vote))
         (counts (make-hash)))
    ;; initialize count vectors for each team
    (for ([i (in-range team-count)])
      (define ch (substring first-vote i (+ i 1)))
      (hash-set! counts ch (make-vector team-count 0)))
    ;; tally votes
    (for ([vote votes])
      (for ([i (in-range team-count)])
        (define ch (substring vote i (+ i 1)))
        (define vec (hash-ref counts ch))
        (vector-set! vec i (add1 (vector-ref vec i)))))
    ;; comparator: higher rank comes first; ties broken alphabetically
    (define (team-less? a b)
      (let loop ((i 0))
        (cond [(= i team-count) (string<? a b)]
              [else (define ca (vector-ref (hash-ref counts a) i))
                    (define cb (vector-ref (hash-ref counts b) i))
                    (if (= ca cb)
                        (loop (+ i 1))
                        (> ca cb))])))
    ;; sort and concatenate
    (let ((sorted (sort (hash-keys counts) team-less?)))
      (apply string-append sorted))))
```

## Erlang

```erlang
-module(solution).
-export([rank_teams/1]).

-spec rank_teams(Votes :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
rank_teams(Votes) ->
    case Votes of
        [] -> <<>>;
        [First|RestVotes] ->
            Teams = binary_to_list(First),
            N = length(Teams),
            InitMap = maps:from_list([{T, lists:duplicate(N,0)} || T <- Teams]),
            MapAfter = lists:foldl(fun(Vote, Acc) ->
                CharList = binary_to_list(Vote),
                update_counts(Acc, CharList, 0)
            end, InitMap, Votes),
            TeamCounts = [{Team, maps:get(Team, MapAfter)} || Team <- Teams],
            Sorted = lists:sort(
                fun({Ta, Ca}, {Tb, Cb}) ->
                    case compare_counts(Ca, Cb) of
                        greater -> true;
                        less -> false;
                        equal -> Ta < Tb
                    end
                end,
                TeamCounts),
            OrderedChars = [Team || {Team,_} <- Sorted],
            list_to_binary(OrderedChars)
    end.

update_counts(Map, [], _Pos) ->
    Map;
update_counts(Map, [Team|Rest], Pos) ->
    Cnts = maps:get(Team, Map),
    NewCnts = inc_at(Pos, Cnts),
    NewMap = maps:put(Team, NewCnts, Map),
    update_counts(NewMap, Rest, Pos + 1).

inc_at(Pos, List) ->
    {Left, [Val|Right]} = lists:split(Pos, List),
    Left ++ [Val + 1] ++ Right.

compare_counts([], []) -> equal;
compare_counts([A|RestA], [B|RestB]) ->
    if
        A > B -> greater;
        A < B -> less;
        true -> compare_counts(RestA, RestB)
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec rank_teams(votes :: [String.t]) :: String.t
  def rank_teams(votes) do
    n = votes |> hd() |> String.length()
    teams = votes |> hd() |> String.graphemes()

    init_map =
      for t <- teams, into: %{} do
        {t, List.duplicate(0, n)}
      end

    counts_map =
      Enum.reduce(votes, init_map, fn vote, acc ->
        vote
        |> String.graphemes()
        |> Enum.with_index()
        |> Enum.reduce(acc, fn {team, idx}, a2 ->
          Map.update!(a2, team, fn list -> List.update_at(list, idx, &(&1 + 1)) end)
        end)
      end)

    sorted =
      Enum.sort(teams, fn a, b ->
        better?(counts_map[a], counts_map[b], a, b)
      end)

    Enum.join(sorted)
  end

  defp better?(cnt_a, cnt_b, name_a, name_b) do
    case first_diff(cnt_a, cnt_b) do
      nil -> name_a < name_b
      {ca, cb} -> ca > cb
    end
  end

  defp first_diff([], []), do: nil
  defp first_diff([ha | ta], [hb | tb]) do
    if ha != hb do
      {ha, hb}
    else
      first_diff(ta, tb)
    end
  end
end
```
