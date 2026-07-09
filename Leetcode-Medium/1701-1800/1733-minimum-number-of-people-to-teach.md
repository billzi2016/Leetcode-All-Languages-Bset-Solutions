# 1733. Minimum Number of People to Teach

## Cpp

```cpp
class Solution {
public:
    int minimumTeachings(int n, vector<vector<int>>& languages, vector<vector<int>>& friendships) {
        int m = languages.size();
        vector<unordered_set<int>> know(m);
        for (int i = 0; i < m; ++i) {
            for (int lang : languages[i]) know[i].insert(lang);
        }
        
        unordered_set<int> badUsers;
        for (auto &fr : friendships) {
            int u = fr[0] - 1, v = fr[1] - 1;
            bool ok = false;
            // iterate over smaller set
            if (know[u].size() > know[v].size()) swap(u, v);
            for (int lang : know[u]) {
                if (know[v].count(lang)) { ok = true; break; }
            }
            if (!ok) {
                badUsers.insert(fr[0] - 1);
                badUsers.insert(fr[1] - 1);
            }
        }
        
        if (badUsers.empty()) return 0;
        
        int ans = INT_MAX;
        for (int lang = 1; lang <= n; ++lang) {
            int teach = 0;
            for (int user : badUsers) {
                if (!know[user].count(lang)) ++teach;
            }
            ans = min(ans, teach);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    public int minimumTeachings(int n, int[][] languages, int[][] friendships) {
        int m = languages.length;
        // Build language sets for each user
        java.util.List<java.util.Set<Integer>> userLangs = new java.util.ArrayList<>(m);
        for (int i = 0; i < m; i++) {
            java.util.HashSet<Integer> set = new java.util.HashSet<>();
            for (int lang : languages[i]) {
                set.add(lang);
            }
            userLangs.add(set);
        }

        java.util.Set<Integer> usersInBad = new java.util.HashSet<>();

        // Identify friendships without a common language
        for (int[] f : friendships) {
            int u = f[0] - 1;
            int v = f[1] - 1;
            java.util.Set<Integer> setU = userLangs.get(u);
            java.util.Set<Integer> setV = userLangs.get(v);

            boolean canCommunicate = false;
            // iterate over smaller set for efficiency
            if (setU.size() > setV.size()) {
                java.util.Set<Integer> tmp = setU;
                setU = setV;
                setV = tmp;
            }
            for (int lang : setU) {
                if (setV.contains(lang)) {
                    canCommunicate = true;
                    break;
                }
            }
            if (!canCommunicate) {
                usersInBad.add(u);
                usersInBad.add(v);
            }
        }

        // If all friendships already work
        if (usersInBad.isEmpty()) return 0;

        int maxAlreadyKnow = 0;
        // For each language, count how many of the problematic users already know it
        for (int lang = 1; lang <= n; ++lang) {
            int cnt = 0;
            for (int user : usersInBad) {
                if (userLangs.get(user).contains(lang)) {
                    cnt++;
                }
            }
            maxAlreadyKnow = Math.max(maxAlreadyKnow, cnt);
        }

        return usersInBad.size() - maxAlreadyKnow;
    }
}
```

## Python

```python
class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        m = len(languages)
        user_langs = [set(lang_list) for lang_list in languages]

        bad_users = set()
        # Identify friendships where users share no common language
        for u, v in friendships:
            u -= 1
            v -= 1
            if not (user_langs[u] & user_langs[v]):
                bad_users.add(u)
                bad_users.add(v)

        if not bad_users:
            return 0

        # For each possible language, count how many of the bad users don't know it
        min_teach = float('inf')
        for lang in range(1, n + 1):
            cnt = sum(1 for user in bad_users if lang not in user_langs[user])
            if cnt < min_teach:
                min_teach = cnt

        return min_teach
```

## Python3

```python
from typing import List
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        user_langs = [set(l) for l in languages]
        bad_users = set()
        for u, v in friendships:
            u -= 1
            v -= 1
            if not (user_langs[u] & user_langs[v]):
                bad_users.add(u)
                bad_users.add(v)
        if not bad_users:
            return 0
        lang_count = {}
        for u in bad_users:
            for lang in user_langs[u]:
                lang_count[lang] = lang_count.get(lang, 0) + 1
        total_bad = len(bad_users)
        ans = total_bad  # worst case: teach everyone involved a new language
        for cnt in lang_count.values():
            ans = min(ans, total_bad - cnt)
        return ans
```

## C

```c
#include <stdlib.h>
#include <limits.h>

int minimumTeachings(int n, int** languages, int languagesSize, int* languagesColSize,
                     int** friendships, int friendshipsSize, int* friendshipsColSize) {
    int m = languagesSize;  // number of users

    // know[i][lang] == 1 if user i knows language lang
    char **know = (char **)malloc(m * sizeof(char *));
    for (int i = 0; i < m; ++i) {
        know[i] = (char *)calloc(n + 1, sizeof(char));
        for (int j = 0; j < languagesColSize[i]; ++j) {
            int lang = languages[i][j];
            know[i][lang] = 1;
        }
    }

    // bad[i] == 1 if user i participates in a friendship without common language
    char *bad = (char *)calloc(m, sizeof(char));

    for (int k = 0; k < friendshipsSize; ++k) {
        int u = friendships[k][0] - 1;
        int v = friendships[k][1] - 1;

        int ok = 0;
        // check intersection using the smaller language list
        if (languagesColSize[u] <= languagesColSize[v]) {
            for (int idx = 0; idx < languagesColSize[u]; ++idx) {
                int lang = languages[u][idx];
                if (know[v][lang]) { ok = 1; break; }
            }
        } else {
            for (int idx = 0; idx < languagesColSize[v]; ++idx) {
                int lang = languages[v][idx];
                if (know[u][lang]) { ok = 1; break; }
            }
        }

        if (!ok) {
            bad[u] = 1;
            bad[v] = 1;
        }
    }

    int answer = INT_MAX;
    for (int L = 1; L <= n; ++L) {
        int cnt = 0;
        for (int i = 0; i < m; ++i) {
            if (bad[i] && !know[i][L]) cnt++;
        }
        if (cnt < answer) answer = cnt;
    }

    // clean up
    for (int i = 0; i < m; ++i) free(know[i]);
    free(know);
    free(bad);

    return answer == INT_MAX ? 0 : answer;
}
```

## Csharp

```csharp
public class Solution {
    public int MinimumTeachings(int n, int[][] languages, int[][] friendships) {
        int m = languages.Length;
        var userLangs = new HashSet<int>[m];
        for (int i = 0; i < m; i++) {
            userLangs[i] = new HashSet<int>(languages[i]);
        }

        var badUsers = new HashSet<int>();
        foreach (var f in friendships) {
            int u = f[0] - 1;
            int v = f[1] - 1;
            bool canCommunicate = false;
            // iterate over smaller set for efficiency
            if (userLangs[u].Count < userLangs[v].Count) {
                foreach (int lang in userLangs[u]) {
                    if (userLangs[v].Contains(lang)) { canCommunicate = true; break; }
                }
            } else {
                foreach (int lang in userLangs[v]) {
                    if (userLangs[u].Contains(lang)) { canCommunicate = true; break; }
                }
            }
            if (!canCommunicate) {
                badUsers.Add(u);
                badUsers.Add(v);
            }
        }

        if (badUsers.Count == 0) return 0;

        int answer = int.MaxValue;
        for (int lang = 1; lang <= n; lang++) {
            int teach = 0;
            foreach (int user in badUsers) {
                if (!userLangs[user].Contains(lang)) teach++;
            }
            if (teach < answer) answer = teach;
        }

        return answer;
    }
}
```

## Javascript

```javascript
/**
 * @param {number} n
 * @param {number[][]} languages
 * @param {number[][]} friendships
 * @return {number}
 */
var minimumTeachings = function(n, languages, friendships) {
    const m = languages.length;
    const userLang = languages.map(arr => new Set(arr));
    
    // Find friendships that cannot currently communicate
    const badPairs = [];
    for (const [u, v] of friendships) {
        const a = u - 1, b = v - 1;
        let canCommunicate = false;
        for (const lang of userLang[a]) {
            if (userLang[b].has(lang)) {
                canCommunicate = true;
                break;
            }
        }
        if (!canCommunicate) badPairs.push([a, b]);
    }
    
    if (badPairs.length === 0) return 0;
    
    let answer = Number.MAX_SAFE_INTEGER;
    
    // Try teaching each language
    for (let lang = 1; lang <= n; ++lang) {
        const taught = new Set();
        for (const [a, b] of badPairs) {
            if (!userLang[a].has(lang)) taught.add(a);
            if (!userLang[b].has(lang)) taught.add(b);
        }
        answer = Math.min(answer, taught.size);
    }
    
    return answer;
};
```

## Typescript

```typescript
function minimumTeachings(n: number, languages: number[][], friendships: number[][]): number {
    const m = languages.length;
    const langSets: Set<number>[] = new Array(m);
    for (let i = 0; i < m; i++) {
        langSets[i] = new Set(languages[i]);
    }
    const bad = new Array(m).fill(false);
    for (const [uRaw, vRaw] of friendships) {
        let u = uRaw - 1;
        let v = vRaw - 1;
        let canCommunicate = false;
        if (langSets[u].size < langSets[v].size) {
            for (const l of langSets[u]) {
                if (langSets[v].has(l)) {
                    canCommunicate = true;
                    break;
                }
            }
        } else {
            for (const l of langSets[v]) {
                if (langSets[u].has(l)) {
                    canCommunicate = true;
                    break;
                }
            }
        }
        if (!canCommunicate) {
            bad[u] = true;
            bad[v] = true;
        }
    }
    const badUsers: number[] = [];
    for (let i = 0; i < m; i++) {
        if (bad[i]) badUsers.push(i);
    }
    const totalBad = badUsers.length;
    if (totalBad === 0) return 0;
    let answer = Number.MAX_SAFE_INTEGER;
    for (let lang = 1; lang <= n; ++lang) {
        let known = 0;
        for (const user of badUsers) {
            if (langSets[user].has(lang)) known++;
        }
        const teach = totalBad - known;
        if (teach < answer) answer = teach;
    }
    return answer;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $languages
     * @param Integer[][] $friendships
     * @return Integer
     */
    function minimumTeachings($n, $languages, $friendships) {
        $m = count($languages);
        // Build language set for each user (1-indexed)
        $userLangs = [];
        for ($i = 0; $i < $m; $i++) {
            $set = [];
            foreach ($languages[$i] as $lang) {
                $set[$lang] = true;
            }
            $userLangs[$i + 1] = $set;
        }

        $badUsers = []; // users involved in at least one bad friendship
        foreach ($friendships as $pair) {
            [$u, $v] = $pair;
            $hasCommon = false;
            foreach ($userLangs[$u] as $lang => $_) {
                if (isset($userLangs[$v][$lang])) {
                    $hasCommon = true;
                    break;
                }
            }
            if (!$hasCommon) {
                $badUsers[$u] = true;
                $badUsers[$v] = true;
            }
        }

        if (empty($badUsers)) {
            return 0;
        }

        $maxKnown = 0;
        for ($lang = 1; $lang <= $n; $lang++) {
            $cnt = 0;
            foreach ($badUsers as $user => $_) {
                if (isset($userLangs[$user][$lang])) {
                    $cnt++;
                }
            }
            if ($cnt > $maxKnown) {
                $maxKnown = $cnt;
            }
        }

        $totalBadUsers = count($badUsers);
        return $totalBadUsers - $maxKnown;
    }
}
```

## Swift

```swift
class Solution {
    func minimumTeachings(_ n: Int, _ languages: [[Int]], _ friendships: [[Int]]) -> Int {
        let m = languages.count
        var userLangSets = Array(repeating: Set<Int>(), count: m + 1) // 1-indexed users
        for i in 1...m {
            userLangSets[i] = Set(languages[i - 1])
        }
        
        var badPairs = [(Int, Int)]()
        for pair in friendships {
            let u = pair[0]
            let v = pair[1]
            var hasCommon = false
            // check if they share any language
            for lang in userLangSets[u] {
                if userLangSets[v].contains(lang) {
                    hasCommon = true
                    break
                }
            }
            if !hasCommon {
                badPairs.append((u, v))
            }
        }
        
        if badPairs.isEmpty { return 0 }
        
        var answer = Int.max
        for lang in 1...n {
            var needTeach = Set<Int>()
            for (u, v) in badPairs {
                if !userLangSets[u].contains(lang) {
                    needTeach.insert(u)
                }
                if !userLangSets[v].contains(lang) {
                    needTeach.insert(v)
                }
            }
            answer = min(answer, needTeach.count)
        }
        return answer
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun minimumTeachings(n: Int, languages: Array<IntArray>, friendships: Array<IntArray>): Int {
        val m = languages.size
        // knows[user][lang] = true if user (0-index) knows language lang (1-indexed)
        val knows = Array(m) { BooleanArray(n + 1) }
        for (i in 0 until m) {
            for (lang in languages[i]) {
                knows[i][lang] = true
            }
        }

        // collect friendships that currently cannot communicate
        val badPairs = mutableListOf<Pair<Int, Int>>()
        for (pair in friendships) {
            val u = pair[0] - 1
            val v = pair[1] - 1
            var common = false
            for (lang in languages[u]) {
                if (knows[v][lang]) {
                    common = true
                    break
                }
            }
            if (!common) {
                badPairs.add(Pair(u, v))
            }
        }

        if (badPairs.isEmpty()) return 0

        var answer = Int.MAX_VALUE
        for (lang in 1..n) {
            val needTeach = BooleanArray(m)
            var cnt = 0
            for ((u, v) in badPairs) {
                if (!knows[u][lang] && !needTeach[u]) {
                    needTeach[u] = true
                    cnt++
                }
                if (!knows[v][lang] && !needTeach[v]) {
                    needTeach[v] = true
                    cnt++
                }
            }
            answer = kotlin.math.min(answer, cnt)
        }
        return answer
    }
}
```

## Dart

```dart
class Solution {
  int minimumTeachings(int n, List<List<int>> languages, List<List<int>> friendships) {
    int m = languages.length;
    // userLang[1..m] stores the set of languages each user knows
    List<Set<int>> userLang = List.generate(m + 1, (_) => <int>{});
    for (int i = 0; i < m; i++) {
      for (int lang in languages[i]) {
        userLang[i + 1].add(lang);
      }
    }

    // Find friendships where users cannot currently communicate
    List<List<int>> badPairs = [];
    for (List<int> f in friendships) {
      int u = f[0];
      int v = f[1];
      bool canTalk = false;
      // iterate over the smaller set for efficiency
      if (userLang[u].length > userLang[v].length) {
        for (int lang in userLang[v]) {
          if (userLang[u].contains(lang)) {
            canTalk = true;
            break;
          }
        }
      } else {
        for (int lang in userLang[u]) {
          if (userLang[v].contains(lang)) {
            canTalk = true;
            break;
          }
        }
      }
      if (!canTalk) badPairs.add([u, v]);
    }

    if (badPairs.isEmpty) return 0;

    int answer = m; // maximum possible teachers
    for (int lang = 1; lang <= n; lang++) {
      Set<int> needTeach = <int>{};
      for (List<int> pair in badPairs) {
        int u = pair[0];
        int v = pair[1];
        if (!userLang[u].contains(lang)) needTeach.add(u);
        if (!userLang[v].contains(lang)) needTeach.add(v);
      }
      if (needTeach.length < answer) answer = needTeach.length;
    }

    return answer;
  }
}
```

## Golang

```go
func minimumTeachings(n int, languages [][]int, friendships [][]int) int {
	m := len(languages)
	// know[user][lang] = true if user knows lang
	know := make([][]bool, m+1)
	for i := 1; i <= m; i++ {
		know[i] = make([]bool, n+1)
		for _, l := range languages[i-1] {
			know[i][l] = true
		}
	}

	bad := make(map[int]struct{})
	for _, f := range friendships {
		u, v := f[0], f[1]
		shared := false
		for _, l := range languages[u-1] {
			if know[v][l] {
				shared = true
				break
			}
		}
		if !shared {
			bad[u] = struct{}{}
			bad[v] = struct{}{}
		}
	}

	if len(bad) == 0 {
		return 0
	}

	minTeach := len(bad)
	for lang := 1; lang <= n; lang++ {
		cnt := 0
		for user := range bad {
			if know[user][lang] {
				cnt++
			}
		}
		if need := len(bad) - cnt; need < minTeach {
			minTeach = need
		}
	}
	return minTeach
}
```

## Ruby

```ruby
require 'set'

def minimum_teachings(n, languages, friendships)
  m = languages.size
  known = Array.new(m) { Set.new }
  languages.each_with_index do |langs, i|
    langs.each { |l| known[i].add(l) }
  end

  bad = []
  friendships.each do |u, v|
    u -= 1
    v -= 1
    bad << [u, v] if (known[u] & known[v]).empty?
  end

  return 0 if bad.empty?

  min_teach = Float::INFINITY
  (1..n).each do |lang|
    taught = Set.new
    bad.each do |u, v|
      taught.add(u) unless known[u].include?(lang)
      taught.add(v) unless known[v].include?(lang)
    end
    min_teach = [min_teach, taught.size].min
  end

  min_teach
end
```

## Scala

```scala
object Solution {
    def minimumTeachings(n: Int, languages: Array[Array[Int]], friendships: Array[Array[Int]]): Int = {
        val m = languages.length
        val known = Array.ofDim[Set[Int]](m)
        for (i <- 0 until m) {
            known(i) = languages(i).toSet
        }
        val badUsers = scala.collection.mutable.Set[Int]()
        for (pair <- friendships) {
            val u = pair(0) - 1
            val v = pair(1) - 1
            if (known(u).intersect(known(v)).isEmpty) {
                badUsers += u
                badUsers += v
            }
        }
        if (badUsers.isEmpty) return 0
        var answer = Int.MaxValue
        for (lang <- 1 to n) {
            var cnt = 0
            val it = badUsers.iterator
            while (it.hasNext) {
                val user = it.next()
                if (!known(user).contains(lang)) cnt += 1
            }
            if (cnt < answer) answer = cnt
        }
        answer
    }
}
```

## Rust

```rust
impl Solution {
    pub fn minimum_teachings(n: i32, languages: Vec<Vec<i32>>, friendships: Vec<Vec<i32>>) -> i32 {
        use std::collections::HashSet;
        let m = languages.len();
        let mut user_langs: Vec<HashSet<i32>> = vec![HashSet::new(); m];
        for (i, langs) in languages.iter().enumerate() {
            for &lang in langs {
                user_langs[i].insert(lang);
            }
        }

        let mut bad_pairs: Vec<(usize, usize)> = Vec::new();
        for pair in friendships.iter() {
            let u = (pair[0] - 1) as usize;
            let v = (pair[1] - 1) as usize;
            let mut can_communicate = false;
            if user_langs[u].len() < user_langs[v].len() {
                for &lang in user_langs[u].iter() {
                    if user_langs[v].contains(&lang) {
                        can_communicate = true;
                        break;
                    }
                }
            } else {
                for &lang in user_langs[v].iter() {
                    if user_langs[u].contains(&lang) {
                        can_communicate = true;
                        break;
                    }
                }
            }
            if !can_communicate {
                bad_pairs.push((u, v));
            }
        }

        if bad_pairs.is_empty() {
            return 0;
        }

        let mut answer = i32::MAX;
        for lang in 1..=n {
            let mut need_teach = vec![false; m];
            for &(u, v) in &bad_pairs {
                if !user_langs[u].contains(&lang) {
                    need_teach[u] = true;
                }
                if !user_langs[v].contains(&lang) {
                    need_teach[v] = true;
                }
            }
            let cnt = need_teach.iter().filter(|&&b| b).count() as i32;
            if cnt < answer {
                answer = cnt;
            }
        }

        answer
    }
}
```

## Racket

```racket
(define/contract (minimum-teachings n languages friendships)
  (-> exact-integer?
      (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      exact-integer?)
  (let* ((m (length languages))
         (lang-sets (make-vector (+ m 1) #f)))
    ;; build a hash set of known languages for each user (1‑based index)
    (for ([i (in-range 1 (add1 m))])
      (let ((h (make-hash)))
        (for ([lg (list-ref languages (- i 1))])
          (hash-set! h lg #t))
        (vector-set! lang-sets i h)))
    ;; collect users that belong to a friendship without common language
    (define bad (make-hash))
    (for ([pair friendships])
      (let* ((u (list-ref pair 0))
             (v (list-ref pair 1))
             (set-u (vector-ref lang-sets u))
             (langs-v (list-ref languages (- v 1))))
        (define has-common? #f)
        (for ([lg langs-v])
          (when (hash-has-key? set-u lg)
            (set! has-common? #t)))
        (unless has-common?
          (hash-set! bad u #t)
          (hash-set! bad v #t))))
    (let ((bad-users (hash-keys bad)))
      (if (null? bad-users)
          0
          (let loop ((L 1) (best n))
            (if (> L n)
                best
                (let ((cnt (for/sum ([u bad-users])
                             (if (hash-has-key? (vector-ref lang-sets u) L) 0 1))))
                  (loop (+ L 1) (min best cnt)))))))))
```

## Erlang

```erlang
-spec minimum_teachings(N :: integer(), Languages :: [[integer()]], Friendships :: [[integer()]]) -> integer().
minimum_teachings(N, Languages, Friendships) ->
    ProblemSet = lists:foldl(
        fun([U, V], Acc) ->
            case have_common_language(U, V, Languages) of
                true -> Acc;
                false -> sets:add_element(U, sets:add_element(V, Acc))
            end
        end,
        sets:new(),
        Friendships),
    ProblemUsers = sets:to_list(ProblemSet),
    case ProblemUsers of
        [] -> 0;
        _ ->
            lists:min(
                [missing_count(Lang, ProblemUsers, Languages) || Lang <- lists:seq(1, N)]
            )
    end.

have_common_language(U, V, Languages) ->
    ULangs = lists:nth(U, Languages),
    VLangs = lists:nth(V, Languages),
    have_intersection(ULangs, VLangs).

have_intersection([], _) -> false;
have_intersection([H|T], VLangs) ->
    case lists:member(H, VLangs) of
        true -> true;
        false -> have_intersection(T, VLangs)
    end.

missing_count(Lang, Users, Languages) ->
    length(
        [U || U <- Users,
              not lists:member(Lang, lists:nth(U, Languages))]
    ).
```

## Elixir

```elixir
defmodule Solution do
  @spec minimum_teachings(integer, [[integer]], [[integer]]) :: integer
  def minimum_teachings(n, languages, friendships) do
    known = Enum.map(languages, &MapSet.new/1)

    bad_edges =
      Enum.reduce(friendships, [], fn [u, v], acc ->
        u_idx = u - 1
        v_idx = v - 1

        if MapSet.size(MapSet.intersection(Enum.at(known, u_idx), Enum.at(known, v_idx))) == 0 do
          [{u_idx, v_idx} | acc]
        else
          acc
        end
      end)

    if bad_edges == [] do
      0
    else
      1..n
      |> Enum.map(fn lang ->
        users_to_teach =
          Enum.reduce(bad_edges, MapSet.new(), fn {u_idx, v_idx}, set ->
            set =
              if MapSet.member?(Enum.at(known, u_idx), lang) do
                set
              else
                MapSet.put(set, u_idx)
              end

            if MapSet.member?(Enum.at(known, v_idx), lang) do
              set
            else
              MapSet.put(set, v_idx)
            end
          end)

        MapSet.size(users_to_teach)
      end)
      |> Enum.min()
    end
  end
end
```
