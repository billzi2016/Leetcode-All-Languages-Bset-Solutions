# 2512. Reward Top K Students

## Cpp

```cpp
class Solution {
public:
    vector<int> topStudents(vector<string>& positive_feedback, vector<string>& negative_feedback,
                            vector<string>& report, vector<int>& student_id, int k) {
        unordered_set<string> pos(positive_feedback.begin(), positive_feedback.end());
        unordered_set<string> neg(negative_feedback.begin(), negative_feedback.end());
        
        vector<pair<int,int>> students; // {points, id}
        for (int i = 0; i < (int)report.size(); ++i) {
            int pts = 0;
            istringstream iss(report[i]);
            string word;
            while (iss >> word) {
                if (pos.count(word)) pts += 3;
                else if (neg.count(word)) pts -= 1;
            }
            students.emplace_back(pts, student_id[i]);
        }
        
        sort(students.begin(), students.end(),
             [](const pair<int,int>& a, const pair<int,int>& b) {
                 if (a.first != b.first) return a.first > b.first; // higher points first
                 return a.second < b.second;                       // lower id first
             });
        
        vector<int> ans;
        for (int i = 0; i < k; ++i) ans.push_back(students[i].second);
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<Integer> topStudents(String[] positive_feedback, String[] negative_feedback,
                                     String[] report, int[] student_id, int k) {
        Set<String> posSet = new HashSet<>(Arrays.asList(positive_feedback));
        Set<String> negSet = new HashSet<>(Arrays.asList(negative_feedback));

        List<int[]> students = new ArrayList<>();
        for (int i = 0; i < report.length; i++) {
            int id = student_id[i];
            String[] words = report[i].split(" ");
            int points = 0;
            for (String w : words) {
                if (posSet.contains(w)) {
                    points += 3;
                } else if (negSet.contains(w)) {
                    points -= 1;
                }
            }
            students.add(new int[]{id, points});
        }

        students.sort((a, b) -> {
            if (b[1] != a[1]) return Integer.compare(b[1], a[1]); // descending points
            return Integer.compare(a[0], b[0]); // ascending id
        });

        List<Integer> result = new ArrayList<>(k);
        for (int i = 0; i < k; i++) {
            result.add(students.get(i)[0]);
        }
        return result;
    }
}
```

## Python

```python
class Solution(object):
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
        """
        :type positive_feedback: List[str]
        :type negative_feedback: List[str]
        :type report: List[str]
        :type student_id: List[int]
        :type k: int
        :rtype: List[int]
        """
        pos_set = set(positive_feedback)
        neg_set = set(negative_feedback)

        scores = {}
        for rep, sid in zip(report, student_id):
            pts = 0
            for word in rep.split():
                if word in pos_set:
                    pts += 3
                elif word in neg_set:
                    pts -= 1
            scores[sid] = pts

        # sort by descending points then ascending id
        sorted_students = sorted(scores.items(), key=lambda x: (-x[1], x[0]))
        return [sid for sid, _ in sorted_students[:k]]
```

## Python3

```python
from typing import List

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str],
                    report: List[str], student_id: List[int], k: int) -> List[int]:
        pos_set = set(positive_feedback)
        neg_set = set(negative_feedback)

        scores = {}
        for rep, sid in zip(report, student_id):
            total = 0
            for word in rep.split():
                if word in pos_set:
                    total += 3
                elif word in neg_set:
                    total -= 1
            scores[sid] = scores.get(sid, 0) + total

        sorted_students = sorted(scores.items(), key=lambda x: (-x[1], x[0]))
        return [sid for sid, _ in sorted_students[:k]]
```

## C

```c
#include <stdlib.h>
#include <string.h>

typedef struct {
    int id;
    int score;
} Student;

static int cmp_str(const void *a, const void *b) {
    const char *const *sa = a;
    const char *const *sb = b;
    return strcmp(*sa, *sb);
}

static int cmp_student(const void *a, const void *b) {
    const Student *s1 = (const Student *)a;
    const Student *s2 = (const Student *)b;
    if (s1->score != s2->score)
        return s2->score - s1->score;          // higher score first
    return s1->id - s2->id;                    // lower id first
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* topStudents(char** positive_feedback, int positive_feedbackSize,
                 char** negative_feedback, int negative_feedbackSize,
                 char** report, int reportSize,
                 int* student_id, int student_idSize,
                 int k, int* returnSize) {
    // Copy and sort positive feedback words
    char **posCopy = NULL;
    if (positive_feedbackSize > 0) {
        posCopy = malloc(sizeof(char*) * positive_feedbackSize);
        for (int i = 0; i < positive_feedbackSize; ++i)
            posCopy[i] = positive_feedback[i];
        qsort(posCopy, positive_feedbackSize, sizeof(char*), cmp_str);
    }

    // Copy and sort negative feedback words
    char **negCopy = NULL;
    if (negative_feedbackSize > 0) {
        negCopy = malloc(sizeof(char*) * negative_feedbackSize);
        for (int i = 0; i < negative_feedbackSize; ++i)
            negCopy[i] = negative_feedback[i];
        qsort(negCopy, negative_feedbackSize, sizeof(char*), cmp_str);
    }

    // Compute scores for each student
    Student *students = malloc(sizeof(Student) * reportSize);
    for (int i = 0; i < reportSize; ++i) {
        int score = 0;
        char *tmp = strdup(report[i]);
        char *token = strtok(tmp, " ");
        while (token) {
            // check positive
            if (positive_feedbackSize > 0 &&
                bsearch(&token, posCopy, positive_feedbackSize,
                        sizeof(char*), cmp_str)) {
                score += 3;
            } else if (negative_feedbackSize > 0 &&
                       bsearch(&token, negCopy, negative_feedbackSize,
                               sizeof(char*), cmp_str)) {
                score -= 1;
            }
            token = strtok(NULL, " ");
        }
        free(tmp);
        students[i].id = student_id[i];
        students[i].score = score;
    }

    // Sort students by score desc, id asc
    qsort(students, reportSize, sizeof(Student), cmp_student);

    // Prepare result
    int *res = malloc(sizeof(int) * k);
    for (int i = 0; i < k; ++i)
        res[i] = students[i].id;

    *returnSize = k;

    // Clean up
    free(posCopy);
    free(negCopy);
    free(students);

    return res;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public IList<int> TopStudents(string[] positive_feedback, string[] negative_feedback, string[] report, int[] student_id, int k) {
        var posSet = new HashSet<string>(positive_feedback);
        var negSet = new HashSet<string>(negative_feedback);
        var students = new List<(int id, int score)>();
        
        for (int i = 0; i < report.Length; i++) {
            int score = 0;
            foreach (var word in report[i].Split(' ')) {
                if (posSet.Contains(word)) {
                    score += 3;
                } else if (negSet.Contains(word)) {
                    score -= 1;
                }
            }
            students.Add((student_id[i], score));
        }
        
        students.Sort((a, b) => {
            int cmp = b.score.CompareTo(a.score); // descending points
            if (cmp != 0) return cmp;
            return a.id.CompareTo(b.id); // ascending id for tie
        });
        
        var result = new List<int>();
        for (int i = 0; i < k; i++) {
            result.Add(students[i].id);
        }
        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[]} positive_feedback
 * @param {string[]} negative_feedback
 * @param {string[]} report
 * @param {number[]} student_id
 * @param {number} k
 * @return {number[]}
 */
var topStudents = function(positive_feedback, negative_feedback, report, student_id, k) {
    const posSet = new Set(positive_feedback);
    const negSet = new Set(negative_feedback);
    const n = report.length;
    const students = new Array(n);
    
    for (let i = 0; i < n; ++i) {
        let score = 0;
        const words = report[i].split(' ');
        for (const w of words) {
            if (posSet.has(w)) {
                score += 3;
            } else if (negSet.has(w)) {
                score -= 1;
            }
        }
        students[i] = { id: student_id[i], score };
    }
    
    students.sort((a, b) => {
        if (b.score !== a.score) return b.score - a.score; // higher score first
        return a.id - b.id; // lower id first on tie
    });
    
    const result = new Array(k);
    for (let i = 0; i < k; ++i) {
        result[i] = students[i].id;
    }
    return result;
};
```

## Typescript

```typescript
function topStudents(positive_feedback: string[], negative_feedback: string[], report: string[], student_id: number[], k: number): number[] {
    const posSet = new Set<string>(positive_feedback);
    const negSet = new Set<string>(negative_feedback);
    const pointsMap = new Map<number, number>();

    for (let i = 0; i < report.length; ++i) {
        const words = report[i].split(' ');
        let score = 0;
        for (const w of words) {
            if (posSet.has(w)) {
                score += 3;
            } else if (negSet.has(w)) {
                score -= 1;
            }
        }
        pointsMap.set(student_id[i], score);
    }

    const arr: [number, number][] = [];
    for (const [id, sc] of pointsMap.entries()) {
        arr.push([id, sc]);
    }

    arr.sort((a, b) => {
        if (b[1] !== a[1]) return b[1] - a[1]; // higher score first
        return a[0] - b[0]; // lower id first on tie
    });

    const result: number[] = [];
    for (let i = 0; i < k; ++i) {
        result.push(arr[i][0]);
    }
    return result;
}
```

## Php

```php
class Solution {

    /**
     * @param String[] $positive_feedback
     * @param String[] $negative_feedback
     * @param String[] $report
     * @param Integer[] $student_id
     * @param Integer $k
     * @return Integer[]
     */
    function topStudents($positive_feedback, $negative_feedback, $report, $student_id, $k) {
        // Build hash sets for quick lookup
        $posSet = array_flip($positive_feedback);
        $negSet = array_flip($negative_feedback);

        $scores = [];

        $n = count($report);
        for ($i = 0; $i < $n; ++$i) {
            $id = $student_id[$i];
            $words = explode(' ', $report[$i]);
            $score = 0;
            foreach ($words as $w) {
                if (isset($posSet[$w])) {
                    $score += 3;
                } elseif (isset($negSet[$w])) {
                    $score -= 1;
                }
            }
            $scores[$id] = $score;
        }

        // Sort student IDs by descending score, then ascending id
        $ids = array_keys($scores);
        usort($ids, function($a, $b) use ($scores) {
            if ($scores[$a] == $scores[$b]) {
                return $a <=> $b; // lower ID first
            }
            // higher score comes first
            return $scores[$b] <=> $scores[$a];
        });

        return array_slice($ids, 0, $k);
    }
}
```

## Swift

```swift
class Solution {
    func topStudents(_ positive_feedback: [String], _ negative_feedback: [String], _ report: [String], _ student_id: [Int], _ k: Int) -> [Int] {
        let posSet = Set(positive_feedback)
        let negSet = Set(negative_feedback)
        var scores = [Int: Int]()
        
        for (idx, rep) in report.enumerated() {
            let id = student_id[idx]
            var score = 0
            for wordSub in rep.split(separator: " ") {
                let word = String(wordSub)
                if posSet.contains(word) {
                    score += 3
                } else if negSet.contains(word) {
                    score -= 1
                }
            }
            scores[id] = score
        }
        
        let sorted = scores.map { ($0.key, $0.value) }.sorted { a, b in
            if a.1 != b.1 {
                return a.1 > b.1
            } else {
                return a.0 < b.0
            }
        }
        
        var result = [Int]()
        for i in 0..<k {
            result.append(sorted[i].0)
        }
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun topStudents(
        positive_feedback: Array<String>,
        negative_feedback: Array<String>,
        report: Array<String>,
        student_id: IntArray,
        k: Int
    ): List<Int> {
        val posSet = positive_feedback.toHashSet()
        val negSet = negative_feedback.toHashSet()
        val scores = HashMap<Int, Int>()
        for (i in report.indices) {
            var score = 0
            for (word in report[i].split(' ')) {
                when {
                    posSet.contains(word) -> score += 3
                    negSet.contains(word) -> score -= 1
                }
            }
            scores[student_id[i]] = score
        }
        return scores.entries
            .sortedWith(compareByDescending<Map.Entry<Int, Int>> { it.value }.thenBy { it.key })
            .take(k)
            .map { it.key }
    }
}
```

## Dart

```dart
class Solution {
  List<int> topStudents(List<String> positive_feedback, List<String> negative_feedback,
      List<String> report, List<int> student_id, int k) {
    final Set<String> posSet = positive_feedback.toSet();
    final Set<String> negSet = negative_feedback.toSet();

    final Map<int, int> scores = {};

    for (int i = 0; i < report.length; ++i) {
      int sid = student_id[i];
      int cur = 0;
      for (String word in report[i].split(' ')) {
        if (posSet.contains(word)) {
          cur += 3;
        } else if (negSet.contains(word)) {
          cur -= 1;
        }
      }
      scores[sid] = (scores[sid] ?? 0) + cur;
    }

    List<MapEntry<int, int>> entries = scores.entries.toList();
    entries.sort((a, b) {
      if (b.value != a.value) return b.value - a.value; // higher points first
      return a.key - b.key; // lower id first on tie
    });

    List<int> result = [];
    for (int i = 0; i < k; ++i) {
      result.add(entries[i].key);
    }
    return result;
  }
}
```

## Golang

```go
import (
	"sort"
	"strings"
)

func topStudents(positive_feedback []string, negative_feedback []string, report []string, student_id []int, k int) []int {
	pos := make(map[string]struct{}, len(positive_feedback))
	for _, w := range positive_feedback {
		pos[w] = struct{}{}
	}
	neg := make(map[string]struct{}, len(negative_feedback))
	for _, w := range negative_feedback {
		neg[w] = struct{}{}
	}

	type pair struct {
		id    int
		score int
	}
	students := make([]pair, 0, len(report))

	for i, rep := range report {
		id := student_id[i]
		words := strings.Split(rep, " ")
		score := 0
		for _, w := range words {
			if _, ok := pos[w]; ok {
				score += 3
			} else if _, ok := neg[w]; ok {
				score -= 1
			}
		}
		students = append(students, pair{id: id, score: score})
	}

	sort.Slice(students, func(i, j int) bool {
		if students[i].score != students[j].score {
			return students[i].score > students[j].score
		}
		return students[i].id < students[j].id
	})

	res := make([]int, k)
	for i := 0; i < k; i++ {
		res[i] = students[i].id
	}
	return res
}
```

## Ruby

```ruby
def top_students(positive_feedback, negative_feedback, report, student_id, k)
  pos_set = {}
  positive_feedback.each { |w| pos_set[w] = true }
  neg_set = {}
  negative_feedback.each { |w| neg_set[w] = true }

  points = Hash.new(0)

  report.each_with_index do |rep, idx|
    sid = student_id[idx]
    score = 0
    rep.split(' ').each do |word|
      if pos_set.key?(word)
        score += 3
      elsif neg_set.key?(word)
        score -= 1
      end
    end
    points[sid] += score
  end

  sorted = points.sort_by { |sid, pts| [-pts, sid] }
  sorted.first(k).map { |sid, _| sid }
end
```

## Scala

```scala
object Solution {
    def topStudents(
        positive_feedback: Array[String],
        negative_feedback: Array[String],
        report: Array[String],
        student_id: Array[Int],
        k: Int
    ): List[Int] = {
        val posSet = positive_feedback.toSet
        val negSet = negative_feedback.toSet

        val scores = new scala.collection.mutable.ArrayBuffer[(Int, Int)]()
        for (i <- report.indices) {
            var score = 0
            val words = report(i).split(" ")
            var j = 0
            while (j < words.length) {
                val w = words(j)
                if (posSet.contains(w)) score += 3
                else if (negSet.contains(w)) score -= 1
                j += 1
            }
            scores.append((student_id(i), score))
        }

        val sorted = scores.sortWith { case ((id1, sc1), (id2, sc2)) =>
            if (sc1 != sc2) sc1 > sc2 else id1 < id2
        }

        sorted.take(k).map(_._1).toList
    }
}
```

## Rust

```rust
impl Solution {
    pub fn top_students(
        positive_feedback: Vec<String>,
        negative_feedback: Vec<String>,
        report: Vec<String>,
        student_id: Vec<i32>,
        k: i32,
    ) -> Vec<i32> {
        use std::collections::{HashMap, HashSet};

        let pos_set: HashSet<String> = positive_feedback.into_iter().collect();
        let neg_set: HashSet<String> = negative_feedback.into_iter().collect();

        let mut scores: HashMap<i32, i32> = HashMap::new();

        for (rep, &sid) in report.iter().zip(student_id.iter()) {
            let mut score = 0;
            for w in rep.split_whitespace() {
                if pos_set.contains(w) {
                    score += 3;
                } else if neg_set.contains(w) {
                    score -= 1;
                }
            }
            *scores.entry(sid).or_insert(0) += score;
        }

        let mut vec: Vec<(i32, i32)> = scores.into_iter().collect();
        vec.sort_unstable_by(|a, b| {
            if a.1 != b.1 {
                b.1.cmp(&a.1) // descending points
            } else {
                a.0.cmp(&b.0) // ascending id
            }
        });

        let k_usize = k as usize;
        vec.iter()
            .take(k_usize)
            .map(|&(id, _)| id)
            .collect()
    }
}
```

## Racket

```racket
(require racket/string)
(require racket/list)

(define/contract (top-students positive_feedback negative_feedback report student_id k)
  (-> (listof string?) (listof string?) (listof string?) (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ([pos-set
          (let ([h (make-hash)])
            (for-each (lambda (w) (hash-set! h w #t)) positive_feedback)
            h)]
         [neg-set
          (let ([h (make-hash)])
            (for-each (lambda (w) (hash-set! h w #t)) negative_feedback)
            h)]
         [pairs
          (for/list ([rep report] [sid student_id])
            (define words (string-split rep " "))
            (define pts
              (for/fold ([sum 0]) ([w words])
                (cond [(hash-has-key? pos-set w) (+ sum 3)]
                      [(hash-has-key? neg-set w) (- sum 1)]
                      [else sum])))
            (cons sid pts))])
    (define sorted
      (sort pairs
            (lambda (a b)
              (let ([pa (cdr a)] [pb (cdr b)])
                (or (> pa pb)
                    (and (= pa pb) (< (car a) (car b))))))))
    (for/list ([pair (in-list (take sorted k))]) (car pair))))
```

## Erlang

```erlang
-module(solution).
-export([top_students/5]).

-spec top_students(Positive_feedback :: [unicode:unicode_binary()],
                   Negative_feedback :: [unicode:unicode_binary()],
                   Report :: [unicode:unicode_binary()],
                   Student_id :: [integer()],
                   K :: integer()) -> [integer()].

top_students(Positive_feedback, Negative_feedback, Report, Student_id, K) ->
    PosMap = maps:from_list([{Word, true} || Word <- Positive_feedback]),
    NegMap = maps:from_list([{Word, true} || Word <- Negative_feedback]),

    %% Build map from student id to total points
    ScoresMap =
        lists:foldl(
          fun({Rpt, Id}, Acc) ->
                  Words = string:split(Rpt, <<" ">>, all),
                  Score = lists:foldl(
                            fun(W, S) ->
                                    case maps:is_key(W, PosMap) of
                                        true -> S + 3;
                                        false ->
                                            case maps:is_key(W, NegMap) of
                                                true -> S - 1;
                                                false -> S
                                            end
                                    end
                            end,
                            0,
                            Words),
                  maps:put(Id, Score, Acc)
          end,
          #{},
          lists:zip(Report, Student_id)),

    %% Convert to list and sort by points desc, id asc
    Sorted =
        lists:sort(
          fun({Id1, P1}, {Id2, P2}) ->
                  case P1 > P2 of
                      true -> true;
                      false ->
                          case P1 < P2 of
                              true -> false;
                              false -> Id1 =< Id2
                          end
                  end
          end,
          [{Id, Score} || {Id, Score} <- maps:to_list(ScoresMap)]),

    %% Take top K ids
    TopK = lists:sublist(Sorted, K),
    [Id || {Id, _} <- TopK].
```

## Elixir

```elixir
defmodule Solution do
  @spec top_students(
          positive_feedback :: [String.t()],
          negative_feedback :: [String.t()],
          report :: [String.t()],
          student_id :: [integer],
          k :: integer
        ) :: [integer]
  def top_students(positive_feedback, negative_feedback, report, student_id, k) do
    pos_set = MapSet.new(positive_feedback)
    neg_set = MapSet.new(negative_feedback)

    scores =
      Enum.zip([report, student_id])
      |> Enum.map(fn {rep, id} ->
        words = String.split(rep, " ", trim: true)

        {pos_cnt, neg_cnt} =
          Enum.reduce(words, {0, 0}, fn w, {p, n} ->
            cond do
              MapSet.member?(pos_set, w) -> {p + 1, n}
              MapSet.member?(neg_set, w) -> {p, n + 1}
              true -> {p, n}
            end
          end)

        points = pos_cnt * 3 - neg_cnt
        {id, points}
      end)

    scores
    |> Enum.sort_by(fn {id, pts} -> {-pts, id} end)
    |> Enum.take(k)
    |> Enum.map(fn {id, _} -> id end)
  end
end
```
