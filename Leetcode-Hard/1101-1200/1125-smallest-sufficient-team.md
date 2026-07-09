# 1125. Smallest Sufficient Team

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> smallestSufficientTeam(vector<string>& req_skills, vector<vector<string>>& people) {
        int m = req_skills.size();
        unordered_map<string,int> skillId;
        for (int i = 0; i < m; ++i) skillId[req_skills[i]] = i;

        int n = people.size();
        vector<int> personMask(n, 0);
        for (int i = 0; i < n; ++i) {
            for (const string& s : people[i]) {
                auto it = skillId.find(s);
                if (it != skillId.end())
                    personMask[i] |= (1 << it->second);
            }
        }

        int fullMask = (1 << m) - 1;
        vector<vector<int>> dp(1 << m);
        vector<char> seen(1 << m, false);
        dp[0] = {};
        seen[0] = true;

        for (int i = 0; i < n; ++i) {
            int pMask = personMask[i];
            if (pMask == 0) continue;
            // iterate over a snapshot of masks to avoid using updated states in same iteration
            vector<int> curMasks;
            for (int mask = 0; mask <= fullMask; ++mask)
                if (seen[mask]) curMasks.push_back(mask);

            for (int mask : curMasks) {
                int newMask = mask | pMask;
                if (newMask == mask) continue;
                if (!seen[newMask] || dp[mask].size() + 1 < dp[newMask].size()) {
                    dp[newMask] = dp[mask];
                    dp[newMask].push_back(i);
                    seen[newMask] = true;
                }
            }
        }

        return dp[fullMask];
    }
};
```

## Java

```java
class Solution {
    public int[] smallestSufficientTeam(String[] req_skills, java.util.List<java.util.List<String>> people) {
        int m = req_skills.length;
        java.util.Map<String, Integer> skillIndex = new java.util.HashMap<>();
        for (int i = 0; i < m; i++) {
            skillIndex.put(req_skills[i], i);
        }
        int n = people.size();
        int[] personMask = new int[n];
        for (int i = 0; i < n; i++) {
            int mask = 0;
            for (String skill : people.get(i)) {
                Integer idx = skillIndex.get(skill);
                if (idx != null) {
                    mask |= 1 << idx;
                }
            }
            personMask[i] = mask;
        }

        int fullMask = (1 << m) - 1;
        java.util.List<Integer>[] dp = new java.util.ArrayList[fullMask + 1];
        dp[0] = new java.util.ArrayList<>();

        for (int i = 0; i < n; i++) {
            int curMask = personMask[i];
            if (curMask == 0) continue;
            java.util.List<Integer>[] prev = dp.clone();
            for (int mask = 0; mask <= fullMask; mask++) {
                if (prev[mask] == null) continue;
                int newMask = mask | curMask;
                if (dp[newMask] == null || prev[mask].size() + 1 < dp[newMask].size()) {
                    java.util.ArrayList<Integer> list = new java.util.ArrayList<>(prev[mask]);
                    list.add(i);
                    dp[newMask] = list;
                }
            }
        }

        java.util.List<Integer> resultList = dp[fullMask];
        int[] res = new int[resultList.size()];
        for (int i = 0; i < resultList.size(); i++) {
            res[i] = resultList.get(i);
        }
        return res;
    }
}
```

## Python

```python
class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        # Map each skill to a bit position
        skill_id = {skill: i for i, skill in enumerate(req_skills)}
        m = len(req_skills)

        # Convert each person's skills to a bitmask
        person_masks = []
        for p in people:
            mask = 0
            for s in p:
                if s in skill_id:  # guaranteed but safe
                    mask |= 1 << skill_id[s]
            person_masks.append(mask)

        full_mask = (1 << m) - 1

        # dp[mask] = list of people indices achieving this skill set with minimal size
        dp = {0: []}

        for i, p_mask in enumerate(person_masks):
            if p_mask == 0:
                continue
            # iterate over a snapshot to avoid using updated entries in same iteration
            current_items = list(dp.items())
            for mask, team in current_items:
                new_mask = mask | p_mask
                if new_mask not in dp or len(team) + 1 < len(dp[new_mask]):
                    dp[new_mask] = team + [i]

        return dp[full_mask]
```

## Python3

```python
class Solution:
    def smallestSufficientTeam(self, req_skills, people):
        from collections import defaultdict

        m = len(req_skills)
        skill_id = {skill: i for i, skill in enumerate(req_skills)}

        # Convert each person's skills to a bitmask
        person_masks = []
        for p in people:
            mask = 0
            for s in p:
                mask |= 1 << skill_id[s]
            person_masks.append(mask)

        dp = {0: []}  # skillset -> list of selected people indices

        for i, pmask in enumerate(person_masks):
            if pmask == 0:
                continue
            # snapshot to avoid using updates from this iteration
            current_items = list(dp.items())
            for skill_set, team in current_items:
                new_set = skill_set | pmask
                if new_set not in dp or len(team) + 1 < len(dp[new_set]):
                    dp[new_set] = team + [i]

        full_mask = (1 << m) - 1
        return dp[full_mask]
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <limits.h>

static int skill_index(const char *skill, char **req_skills, int req_skillsSize) {
    for (int i = 0; i < req_skillsSize; ++i) {
        if (strcmp(skill, req_skills[i]) == 0) return i;
    }
    return -1;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* smallestSufficientTeam(char** req_skills, int req_skillsSize,
                            char*** people, int peopleSize,
                            int* peopleColSize, int* returnSize) {
    int fullMask = (1 << req_skillsSize) - 1;
    unsigned long long *personMask = (unsigned long long *)malloc(sizeof(unsigned long long) * peopleSize);
    for (int i = 0; i < peopleSize; ++i) {
        unsigned long long mask = 0ULL;
        for (int j = 0; j < peopleColSize[i]; ++j) {
            int idx = skill_index(people[i][j], req_skills, req_skillsSize);
            if (idx >= 0) mask |= 1ULL << idx;
        }
        personMask[i] = mask;
    }

    unsigned long long INF = ULLONG_MAX;
    unsigned long long *dp = (unsigned long long *)malloc(sizeof(unsigned long long) * (fullMask + 1));
    for (int m = 0; m <= fullMask; ++m) dp[m] = INF;
    dp[0] = 0ULL;

    for (int mask = 0; mask <= fullMask; ++mask) {
        if (dp[mask] == INF) continue;
        for (int i = 0; i < peopleSize; ++i) {
            unsigned long long newMask = mask | personMask[i];
            if ((unsigned int)newMask == (unsigned int)mask) continue; // no new skill
            unsigned long long candidate = dp[mask] | (1ULL << i);
            if (dp[newMask] == INF ||
                __builtin_popcountll(candidate) < __builtin_popcountll(dp[newMask])) {
                dp[newMask] = candidate;
            }
        }
    }

    unsigned long long resultMask = dp[fullMask];
    int cnt = __builtin_popcountll(resultMask);
    int *ans = (int *)malloc(sizeof(int) * cnt);
    int idx = 0;
    for (int i = 0; i < peopleSize; ++i) {
        if (resultMask & (1ULL << i)) {
            ans[idx++] = i;
        }
    }
    *returnSize = cnt;

    free(personMask);
    free(dp);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] SmallestSufficientTeam(string[] req_skills, IList<IList<string>> people) {
        int m = req_skills.Length;
        var skillIndex = new Dictionary<string, int>();
        for (int i = 0; i < m; i++) {
            skillIndex[req_skills[i]] = i;
        }

        int n = people.Count;
        int[] personMask = new int[n];
        for (int i = 0; i < n; i++) {
            int mask = 0;
            foreach (var skill in people[i]) {
                if (skillIndex.TryGetValue(skill, out int idx)) {
                    mask |= 1 << idx;
                }
            }
            personMask[i] = mask;
        }

        int fullMask = (1 << m) - 1;
        List<int>[] dp = new List<int>[fullMask + 1];
        dp[0] = new List<int>();

        for (int mask = 0; mask <= fullMask; mask++) {
            if (dp[mask] == null) continue;
            for (int i = 0; i < n; i++) {
                int newMask = mask | personMask[i];
                if (newMask == mask) continue; // no contribution
                var candidate = dp[mask].Count + 1;
                if (dp[newMask] == null || candidate < dp[newMask].Count) {
                    var list = new List<int>(dp[mask]);
                    list.Add(i);
                    dp[newMask] = list;
                }
            }
        }

        return dp[fullMask].ToArray();
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} req_skills
 * @param {string[][]} people
 * @return {number[]}
 */
var smallestSufficientTeam = function(req_skills, people) {
    const m = req_skills.length;
    const skillIndex = new Map();
    for (let i = 0; i < m; ++i) skillIndex.set(req_skills[i], i);
    
    const n = people.length;
    const personMask = new Array(n).fill(0);
    for (let i = 0; i < n; ++i) {
        let mask = 0;
        for (const s of people[i]) {
            const idx = skillIndex.get(s);
            if (idx !== undefined) mask |= (1 << idx);
        }
        personMask[i] = mask;
    }
    
    const fullMask = (1 << m) - 1;
    const dp = new Array(1 << m).fill(null);
    dp[0] = [];
    
    for (let mask = 0; mask <= fullMask; ++mask) {
        if (dp[mask] === null) continue;
        for (let i = 0; i < n; ++i) {
            const newMask = mask | personMask[i];
            if (newMask === mask) continue; // no contribution
            if (dp[newMask] === null || dp[mask].length + 1 < dp[newMask].length) {
                dp[newMask] = dp[mask].concat(i);
            }
        }
    }
    
    return dp[fullMask];
};
```

## Typescript

```typescript
function smallestSufficientTeam(req_skills: string[], people: string[][]): number[] {
    const m = req_skills.length;
    const skillId = new Map<string, number>();
    for (let i = 0; i < m; ++i) skillId.set(req_skills[i], i);

    const personMasks: number[] = people.map(p => {
        let mask = 0;
        for (const s of p) {
            const id = skillId.get(s);
            if (id !== undefined) mask |= 1 << id;
        }
        return mask;
    });

    const dp = new Map<number, number[]>();
    dp.set(0, []);

    for (let i = 0; i < people.length; ++i) {
        const pMask = personMasks[i];
        if (pMask === 0) continue; // contributes nothing
        const currentEntries = Array.from(dp.entries());
        for (const [mask, team] of currentEntries) {
            const newMask = mask | pMask;
            const existing = dp.get(newMask);
            if (!existing || existing.length > team.length + 1) {
                dp.set(newMask, [...team, i]);
            }
        }
    }

    const fullMask = (1 << m) - 1;
    return dp.get(fullMask)!;
}
```

## Php

```php
class Solution {
    /**
     * @param String[] $req_skills
     * @param String[][] $people
     * @return Integer[]
     */
    function smallestSufficientTeam($req_skills, $people) {
        $m = count($req_skills);
        $skillIndex = [];
        foreach ($req_skills as $idx => $skill) {
            $skillIndex[$skill] = $idx;
        }

        $n = count($people);
        $personMasks = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $mask = 0;
            foreach ($people[$i] as $skill) {
                if (isset($skillIndex[$skill])) {
                    $mask |= (1 << $skillIndex[$skill]);
                }
            }
            $personMasks[$i] = $mask;
        }

        $size = 1 << $m;
        $dp = array_fill(0, $size, null);
        $dp[0] = 0;

        for ($i = 0; $i < $n; $i++) {
            $pMask = $personMasks[$i];
            if ($pMask == 0) continue;
            for ($mask = 0; $mask < $size; $mask++) {
                if ($dp[$mask] === null) continue;
                $newMask = $mask | $pMask;
                $candidate = $dp[$mask] | (1 << $i);
                if ($dp[$newMask] === null || $this->popcount($candidate) < $this->popcount($dp[$newMask])) {
                    $dp[$newMask] = $candidate;
                }
            }
        }

        $fullMask = $size - 1;
        $teamMask = $dp[$fullMask];
        $result = [];
        for ($i = 0; $i < $n; $i++) {
            if (($teamMask >> $i) & 1) {
                $result[] = $i;
            }
        }
        return $result;
    }

    private function popcount($x) {
        $cnt = 0;
        while ($x) {
            $cnt++;
            $x &= ($x - 1);
        }
        return $cnt;
    }
}
```

## Swift

```swift
class Solution {
    func smallestSufficientTeam(_ req_skills: [String], _ people: [[String]]) -> [Int] {
        let m = req_skills.count
        var skillIndex = [String:Int]()
        for (i, skill) in req_skills.enumerated() {
            skillIndex[skill] = i
        }
        
        let n = people.count
        var personMask = [Int](repeating: 0, count: n)
        for i in 0..<n {
            var mask = 0
            for skill in people[i] {
                if let idx = skillIndex[skill] {
                    mask |= (1 << idx)
                }
            }
            personMask[i] = mask
        }
        
        let fullMask = (1 << m) - 1
        var dp = Array<[Int]?>(repeating: nil, count: 1 << m)
        dp[0] = []
        
        for i in 0..<n {
            let pMask = personMask[i]
            if pMask == 0 { continue }
            for mask in 0...fullMask {
                guard let curTeam = dp[mask] else { continue }
                let combined = mask | pMask
                if dp[combined] == nil || curTeam.count + 1 < dp[combined]!.count {
                    var newTeam = curTeam
                    newTeam.append(i)
                    dp[combined] = newTeam
                }
            }
        }
        
        return dp[fullMask] ?? []
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun smallestSufficientTeam(req_skills: Array<String>, people: List<List<String>>): IntArray {
        val m = req_skills.size
        val skillIndex = HashMap<String, Int>()
        for (i in 0 until m) {
            skillIndex[req_skills[i]] = i
        }

        val n = people.size
        val personMask = IntArray(n)
        for (i in 0 until n) {
            var mask = 0
            for (skill in people[i]) {
                val idx = skillIndex[skill] ?: continue
                mask = mask or (1 shl idx)
            }
            personMask[i] = mask
        }

        val totalMasks = 1 shl m
        val dp = arrayOfNulls<List<Int>>(totalMasks)
        dp[0] = emptyList()

        for (i in 0 until n) {
            val pMask = personMask[i]
            if (pMask == 0) continue
            val cur = dp.clone() as Array<List<Int>?>
            for (mask in 0 until totalMasks) {
                val curTeam = cur[mask] ?: continue
                val newMask = mask or pMask
                if (dp[newMask] == null || curTeam.size + 1 < dp[newMask]!!.size) {
                    val newTeam = ArrayList<Int>(curTeam.size + 1)
                    newTeam.addAll(curTeam)
                    newTeam.add(i)
                    dp[newMask] = newTeam
                }
            }
        }

        return dp[totalMasks - 1]!!.toIntArray()
    }
}
```

## Dart

```dart
class Solution {
  List<int> smallestSufficientTeam(List<String> req_skills, List<List<String>> people) {
    int m = req_skills.length;
    Map<String, int> skillId = {};
    for (int i = 0; i < m; i++) {
      skillId[req_skills[i]] = i;
    }

    int n = people.length;
    List<int> personMask = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      int mask = 0;
      for (String s in people[i]) {
        int? id = skillId[s];
        if (id != null) {
          mask |= (1 << id);
        }
      }
      personMask[i] = mask;
    }

    int fullMask = (1 << m) - 1;
    List<List<int>?> dp = List.filled(fullMask + 1, null);
    dp[0] = [];

    for (int mask = 0; mask <= fullMask; mask++) {
      if (dp[mask] == null) continue;
      for (int i = 0; i < n; i++) {
        int newMask = mask | personMask[i];
        if (newMask == mask) continue; // no new skill contributed
        List<int>? cur = dp[newMask];
        List<int> candidate = List.from(dp[mask]!);
        candidate.add(i);
        if (cur == null || candidate.length < cur.length) {
          dp[newMask] = candidate;
        }
      }
    }

    return dp[fullMask] ?? [];
  }
}
```

## Golang

```go
func smallestSufficientTeam(req_skills []string, people [][]string) []int {
    // Map each skill to a unique bit position
    skillIdx := make(map[string]int)
    for i, s := range req_skills {
        skillIdx[s] = i
    }
    m := len(req_skills)
    fullMask := 1<<m - 1

    // Convert each person's skills into a bitmask
    personMask := make([]int, len(people))
    for i, p := range people {
        mask := 0
        for _, skill := range p {
            if idx, ok := skillIdx[skill]; ok {
                mask |= 1 << idx
            }
        }
        personMask[i] = mask
    }

    // dp[mask] holds the smallest team (as slice of indices) achieving this skill set
    dp := make([][]int, 1<<m)
    dp[0] = []int{}

    for i, pMask := range personMask {
        if pMask == 0 {
            continue // this person adds no new skills
        }
        // Iterate over a snapshot of current dp to avoid using updates from this iteration
        for mask := 0; mask <= fullMask; mask++ {
            if dp[mask] == nil {
                continue
            }
            newMask := mask | pMask
            if dp[newMask] != nil && len(dp[newMask]) <= len(dp[mask])+1 {
                continue // existing team is not larger
            }
            // Build candidate team
            cand := make([]int, len(dp[mask])+1)
            copy(cand, dp[mask])
            cand[len(dp[mask])] = i
            dp[newMask] = cand
        }
    }

    return dp[fullMask]
}
```

## Ruby

```ruby
def smallest_sufficient_team(req_skills, people)
  m = req_skills.length
  skill_index = {}
  req_skills.each_with_index { |skill, i| skill_index[skill] = i }

  person_masks = people.map do |skills|
    mask = 0
    skills.each { |s| mask |= (1 << skill_index[s]) if skill_index.key?(s) }
    mask
  end

  dp = Array.new(1 << m)
  dp[0] = []

  person_masks.each_with_index do |p_mask, i|
    next if p_mask == 0
    new_dp = dp.clone
    (0...(1 << m)).each do |mask|
      next unless dp[mask]
      combined = mask | p_mask
      if new_dp[combined].nil? || dp[mask].length + 1 < new_dp[combined].length
        new_dp[combined] = dp[mask] + [i]
      end
    end
    dp = new_dp
  end

  full_mask = (1 << m) - 1
  dp[full_mask] || []
end
```

## Scala

```scala
object Solution {
    def smallestSufficientTeam(req_skills: Array[String], people: List[List[String]]): Array[Int] = {
        val m = req_skills.length
        val skillId = scala.collection.mutable.Map[String, Int]()
        for (i <- 0 until m) skillId(req_skills(i)) = i

        val n = people.length
        val personMask = new Array[Int](n)
        var idx = 0
        for (p <- people) {
            var mask = 0
            for (skill <- p) {
                skillId.get(skill).foreach { id => mask |= (1 << id) }
            }
            personMask(idx) = mask
            idx += 1
        }

        val size = 1 << m
        val dp = Array.fill[Long](size)(-1L)
        dp(0) = 0L

        for (mask <- 0 until size) {
            if (dp(mask) != -1L) {
                val curTeamMask = dp(mask)
                for (i <- 0 until n) {
                    val newMask = mask | personMask(i)
                    if (newMask != mask) {
                        val newTeamMask = curTeamMask | (1L << i)
                        if (dp(newMask) == -1L || java.lang.Long.bitCount(newTeamMask) < java.lang.Long.bitCount(dp(newMask))) {
                            dp(newMask) = newTeamMask
                        }
                    }
                }
            }
        }

        val finalMask = dp(size - 1)
        val result = scala.collection.mutable.ArrayBuffer[Int]()
        for (i <- 0 until n) {
            if ((finalMask & (1L << i)) != 0) result += i
        }
        result.toArray
    }
}
```

## Rust

```rust
use std::collections::HashMap;

impl Solution {
    pub fn smallest_sufficient_team(req_skills: Vec<String>, people: Vec<Vec<String>>) -> Vec<i32> {
        let m = req_skills.len();
        // map skill to its index
        let mut skill_id: HashMap<&String, usize> = HashMap::new();
        for (i, s) in req_skills.iter().enumerate() {
            skill_id.insert(s, i);
        }

        // compute each person's skill mask
        let n = people.len();
        let mut person_masks: Vec<u32> = vec![0; n];
        for (i, skills) in people.iter().enumerate() {
            let mut mask: u32 = 0;
            for sk in skills {
                if let Some(&idx) = skill_id.get(sk) {
                    mask |= 1 << idx;
                }
            }
            person_masks[i] = mask;
        }

        let total_states = 1usize << m;
        // dp[mask] = minimal team (list of indices) achieving this skill set
        let mut dp: Vec<Option<Vec<usize>>> = vec![None; total_states];
        dp[0] = Some(Vec::new());

        for (i, &p_mask) in person_masks.iter().enumerate() {
            if p_mask == 0 {
                continue;
            }
            let cur_dp = dp.clone(); // snapshot of current states
            for mask in 0..total_states {
                if let Some(team) = &cur_dp[mask] {
                    let new_mask = mask | (p_mask as usize);
                    if new_mask == mask {
                        continue; // no new skill contributed
                    }
                    let better = match &dp[new_mask] {
                        None => true,
                        Some(existing) => existing.len() > team.len() + 1,
                    };
                    if better {
                        let mut new_team = team.clone();
                        new_team.push(i);
                        dp[new_mask] = Some(new_team);
                    }
                }
            }
        }

        let final_team = dp[total_states - 1].as_ref().unwrap();
        final_team.iter().map(|&idx| idx as i32).collect()
    }
}
```

## Racket

```racket
#lang racket

(define/contract (smallest-sufficient-team req_skills people)
  (-> (listof string?) (listof (listof string?)) (listof exact-integer?))
  (let* ([m (length req_skills)]
         [n (length people)]
         [skill->idx (make-hash)])
    ;; map each required skill to an index
    (for ([i (in-range m)]
          [sk (in-list req_skills)])
      (hash-set! skill->idx sk i))
    ;; compute bitmask of skills for each person
    (define person-masks (make-vector n 0))
    (for ([i (in-range n)])
      (let* ([skills (list-ref people i)]
             [mask (foldl (λ (sk acc)
                            (bitwise-ior acc (arithmetic-shift 1 (hash-ref skill->idx sk))))
                          0
                          skills)])
        (vector-set! person-masks i mask)))
    ;; DP over skill subsets
    (define dp-size (expt 2 m))
    (define dp (make-vector dp-size #f))
    (vector-set! dp 0 0) ; empty team for no skills
    (for ([mask (in-range 1 dp-size)])
      (define best #f)
      (for ([i (in-range n)])
        (define p-mask (vector-ref person-masks i))
        (define smaller (bitwise-and mask (bitwise-not p-mask))) ; remove skills covered by person i
        (when (and (not (= smaller mask)) (vector-ref dp smaller))
          (define candidate (bitwise-ior (vector-ref dp smaller) (arithmetic-shift 1 i)))
          (cond [(not best)
                 (set! best candidate)]
                [else
                 (when (< (bitwise-bit-count candidate) (bitwise-bit-count best))
                   (set! best candidate))])))
      (vector-set! dp mask best))
    ;; retrieve answer mask for all skills
    (define full-mask (- dp-size 1))
    (define ans-mask (vector-ref dp full-mask))
    ;; extract indices of selected people
    (for/list ([i (in-range n)]
               #:when (not (= (bitwise-and ans-mask (arithmetic-shift 1 i)) 0)))
      i)))
```

## Erlang

```erlang
-module(solution).
-export([smallest_sufficient_team/2]).

-spec smallest_sufficient_team(Req_skills :: [unicode:unicode_binary()], People :: [[unicode:unicode_binary()]]) -> [integer()].
smallest_sufficient_team(Req_skills, People) ->
    SkillMap = skill_idx_map(Req_skills, 0, #{}),
    PersonMasks = [mask_skills(P, SkillMap) || P <- People],
    DP = dp_loop(PersonMasks, 0, #{0 => []}),
    FullMask = (1 bsl length(Req_skills)) - 1,
    maps:get(FullMask, DP).

skill_idx_map([], _Id, Map) -> Map;
skill_idx_map([S|Rest], Id, Map) ->
    skill_idx_map(Rest, Id + 1, maps:put(S, Id, Map)).

mask_skills(Skills, SkillMap) ->
    lists:foldl(fun(Skill, Acc) ->
        case maps:get(Skill, SkillMap, undefined) of
            undefined -> Acc;
            Id -> Acc bor (1 bsl Id)
        end
    end, 0, Skills).

dp_loop([], _Idx, DP) -> DP;
dp_loop([Mask|Rest], Idx, DP) ->
    Entries = maps:to_list(DP),
    NewDP = lists:foldl(fun({SkillMask, Team}, AccDP) ->
        NewMask = SkillMask bor Mask,
        ExistingTeam = maps:get(NewMask, AccDP, undefined),
        NewTeam = Team ++ [Idx],
        case ExistingTeam of
            undefined -> maps:put(NewMask, NewTeam, AccDP);
            _ when length(NewTeam) < length(ExistingTeam) ->
                maps:put(NewMask, NewTeam, AccDP);
            _ -> AccDP
        end
    end, DP, Entries),
    dp_loop(Rest, Idx + 1, NewDP).
```

## Elixir

```elixir
defmodule Solution do
  @spec smallest_sufficient_team(req_skills :: [String.t()], people :: [[String.t()]]) :: [integer()]
  def smallest_sufficient_team(req_skills, people) do
    import Bitwise

    skill_to_idx =
      req_skills
      |> Enum.with_index()
      |> Enum.into(%{}, fn {skill, idx} -> {skill, idx} end)

    person_masks =
      Enum.map(people, fn skills ->
        Enum.reduce(skills, 0, fn s, acc ->
          case Map.fetch(skill_to_idx, s) do
            {:ok, idx} -> acc ||| (1 <<< idx)
            :error -> acc
          end
        end)
      end)

    full_mask = (1 <<< length(req_skills)) - 1

    dp_initial = %{0 => []}

    final_dp =
      Enum.with_index(person_masks)
      |> Enum.reduce(dp_initial, fn {p_mask, i}, dp ->
        snapshot = Map.to_list(dp)

        Enum.reduce(snapshot, dp, fn {mask, team}, acc ->
          new_mask = mask ||| p_mask

          cond do
            not Map.has_key?(acc, new_mask) ->
              Map.put(acc, new_mask, team ++ [i])

            length(team) + 1 < length(Map.get(acc, new_mask)) ->
              Map.put(acc, new_mask, team ++ [i])

            true ->
              acc
          end
        end)
      end)

    Map.get(final_dp, full_mask, [])
  end
end
```
