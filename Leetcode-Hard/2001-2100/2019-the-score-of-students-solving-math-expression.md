# 2019. The Score of Students Solving Math Expression

## Cpp

```cpp
class Solution {
public:
    int scoreOfStudents(string s, vector<int>& answers) {
        const int MAXV = 1000;
        // Parse numbers and operators
        vector<int> nums;
        vector<char> ops;
        for (int i = 0; i < (int)s.size(); ++i) {
            if (isdigit(s[i])) {
                nums.push_back(s[i] - '0');
            } else {
                ops.push_back(s[i]);
            }
        }
        int n = nums.size();
        // Compute correct answer with normal precedence (* before +)
        long long total = 0;
        long long curProd = nums[0];
        for (int i = 0; i < (int)ops.size(); ++i) {
            if (ops[i] == '*') {
                curProd *= nums[i + 1];
            } else { // '+'
                total += curProd;
                curProd = nums[i + 1];
            }
        }
        total += curProd;
        int correct = (int)total; // guaranteed within [0,1000]
        // DP to compute all possible results with any parenthesization
        vector<vector<unordered_set<int>>> memo(n, vector<unordered_set<int>>(n));
        vector<vector<char>> done(n, vector<char>(n, 0));
        function<const unordered_set<int>&(int,int)> dfs = [&](int l, int r) -> const unordered_set<int>& {
            if (done[l][r]) return memo[l][r];
            unordered_set<int> cur;
            if (l == r) {
                cur.insert(nums[l]);
            } else {
                for (int k = l; k < r; ++k) {
                    char op = ops[k];
                    const auto& left = dfs(l, k);
                    const auto& right = dfs(k + 1, r);
                    for (int a : left) {
                        for (int b : right) {
                            int val = (op == '+') ? a + b : a * b;
                            if (val <= MAXV) cur.insert(val);
                        }
                    }
                }
            }
            memo[l][r] = std::move(cur);
            done[l][r] = 1;
            return memo[l][r];
        };
        const auto& possible = dfs(0, n - 1);
        // Score answers
        int sum = 0;
        for (int ans : answers) {
            if (ans == correct) sum += 5;
            else if (possible.find(ans) != possible.end()) sum += 2;
        }
        return sum;
    }
};
```

## Java

```java
class Solution {
    public int scoreOfStudents(String s, int[] answers) {
        // Parse numbers and operators
        java.util.List<Integer> nums = new java.util.ArrayList<>();
        java.util.List<Character> ops = new java.util.ArrayList<>();
        for (int i = 0; i < s.length(); ++i) {
            char c = s.charAt(i);
            if (c == '+' || c == '*') {
                ops.add(c);
            } else { // digit
                nums.add(c - '0');
            }
        }
        int n = nums.size();
        // DP memoization for all possible results with any parenthesization
        @SuppressWarnings("unchecked")
        java.util.HashSet<Integer>[][] dp = new java.util.HashSet[n][n];
        java.util.function.BiFunction<Integer, Integer, java.util.HashSet<Integer>> compute =
            new java.util.function.BiFunction<Integer, Integer, java.util.HashSet<Integer>>() {
                public java.util.HashSet<Integer> apply(Integer l, Integer r) {
                    if (dp[l][r] != null) return dp[l][r];
                    java.util.HashSet<Integer> set = new java.util.HashSet<>();
                    if (l == r) {
                        set.add(nums.get(l));
                    } else {
                        for (int k = l; k < r; ++k) {
                            char op = ops.get(k);
                            java.util.HashSet<Integer> left = this.apply(l, k);
                            java.util.HashSet<Integer> right = this.apply(k + 1, r);
                            for (int a : left) {
                                for (int b : right) {
                                    if (op == '+') set.add(a + b);
                                    else set.add(a * b); // '*'
                                }
                            }
                        }
                    }
                    dp[l][r] = set;
                    return set;
                }
            };
        java.util.HashSet<Integer> allPossible = compute.apply(0, n - 1);

        // Compute correct answer with standard precedence (* before +)
        int total = 0;
        int curProd = nums.get(0);
        for (int i = 0; i < ops.size(); ++i) {
            char op = ops.get(i);
            int nextNum = nums.get(i + 1);
            if (op == '*') {
                curProd *= nextNum;
            } else { // '+'
                total += curProd;
                curProd = nextNum;
            }
        }
        total += curProd; // add last term
        int correct = total;

        // Score the answers
        int score = 0;
        for (int ans : answers) {
            if (ans == correct) {
                score += 5;
            } else if (allPossible.contains(ans)) {
                score += 2;
            }
        }
        return score;
    }
}
```

## Python

```python
class Solution(object):
    def scoreOfStudents(self, s, answers):
        """
        :type s: str
        :type answers: List[int]
        :rtype: int
        """
        # parse numbers and operators
        nums = []
        ops = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                nums.append(int(s[i]))
                i += 1
            else:
                ops.append(s[i])
                i += 1

        # correct answer with normal precedence (* before +)
        correct = 0
        for term in s.split('+'):
            prod = 1
            for part in term.split('*'):
                prod *= int(part)
            correct += prod

        from functools import lru_cache

        @lru_cache(None)
        def dfs(l, r):
            """return set of possible results from nums[l..r]"""
            if l == r:
                return {nums[l]}
            res = set()
            for k in range(l, r):
                left_set = dfs(l, k)
                right_set = dfs(k + 1, r)
                op = ops[k]
                if op == '+':
                    for a in left_set:
                        for b in right_set:
                            val = a + b
                            if val <= 1000:   # answers are bounded, prune larger values
                                res.add(val)
                else:  # '*'
                    for a in left_set:
                        for b in right_set:
                            val = a * b
                            if val <= 1000:
                                res.add(val)
            return res

        possible = dfs(0, len(nums) - 1)

        total = 0
        for ans in answers:
            if ans == correct:
                total += 5
            elif ans in possible:
                total += 2
        return total
```

## Python3

```python
class Solution:
    def scoreOfStudents(self, s: str, answers):
        # parse numbers and operators
        nums = []
        ops = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                nums.append(int(s[i]))
                i += 1
            else:
                ops.append(s[i])
                i += 1

        n = len(nums)

        # evaluate correct answer with normal precedence (* before +)
        def eval_correct():
            total = 0
            cur_prod = nums[0]
            for idx, op in enumerate(ops):
                if op == '*':
                    cur_prod *= nums[idx + 1]
                else:  # '+'
                    total += cur_prod
                    cur_prod = nums[idx + 1]
            total += cur_prod
            return total

        correct_val = eval_correct()

        from functools import lru_cache

        @lru_cache(None)
        def dfs(l, r):
            if l == r:
                return {nums[l]}
            res = set()
            for k in range(l, r):
                left_set = dfs(l, k)
                right_set = dfs(k + 1, r)
                op = ops[k]
                if op == '+':
                    for a in left_set:
                        for b in right_set:
                            val = a + b
                            if val <= 1000:   # answers are bounded, prune larger values
                                res.add(val)
                else:  # '*'
                    for a in left_set:
                        for b in right_set:
                            val = a * b
                            if val <= 1000:
                                res.add(val)
            return res

        possible_vals = dfs(0, n - 1)

        total_score = 0
        for ans in answers:
            if ans == correct_val:
                total_score += 5
            elif ans in possible_vals:
                total_score += 2
        return total_score
```

## C

```c
#include <string.h>
#include <stdlib.h>

#define MAXV 1000
#define MAXN 16   // max numbers (operators <=15)

typedef struct {
    int cnt;
    char present[MAXV + 1];
    int vals[MAXV + 1];
} Set;

int scoreOfStudents(char* s, int* answers, int answersSize) {
    int nums[MAXN];
    char ops[MAXN];
    int n = 0;          // number of operands
    int opCnt = 0;
    
    // parse expression (single digit numbers)
    for (int i = 0; s[i]; ++i) {
        if (s[i] >= '0' && s[i] <= '9') {
            nums[n++] = s[i] - '0';
        } else { // '+' or '*'
            ops[opCnt++] = s[i];
        }
    }

    // DP sets for intervals
    static Set dp[MAXN][MAXN];
    for (int i = 0; i < n; ++i) {
        memset(dp[i][i].present, 0, sizeof(dp[i][i].present));
        dp[i][i].cnt = 1;
        int v = nums[i];
        dp[i][i].present[v] = 1;
        dp[i][i].vals[0] = v;
    }

    for (int len = 2; len <= n; ++len) {
        for (int l = 0; l + len - 1 < n; ++l) {
            int r = l + len - 1;
            memset(dp[l][r].present, 0, sizeof(dp[l][r].present));
            dp[l][r].cnt = 0;
            for (int k = l; k < r; ++k) {
                Set *L = &dp[l][k];
                Set *R = &dp[k + 1][r];
                char op = ops[k];
                for (int i = 0; i < L->cnt; ++i) {
                    int a = L->vals[i];
                    for (int j = 0; j < R->cnt; ++j) {
                        int b = R->vals[j];
                        int val = (op == '+') ? a + b : a * b;
                        if (val <= MAXV && !dp[l][r].present[val]) {
                            dp[l][r].present[val] = 1;
                            dp[l][r].vals[dp[l][r].cnt++] = val;
                        }
                    }
                }
            }
        }
    }

    // compute correct answer with normal precedence (* before +)
    int correct = 0;
    int cur = nums[0];
    for (int i = 0; i < opCnt; ++i) {
        if (ops[i] == '*') {
            cur *= nums[i + 1];
        } else { // '+'
            correct += cur;
            cur = nums[i + 1];
        }
    }
    correct += cur;

    // set of all possible results
    Set *allSet = &dp[0][n - 1];

    int totalPoints = 0;
    for (int i = 0; i < answersSize; ++i) {
        int ans = answers[i];
        if (ans == correct) {
            totalPoints += 5;
        } else if (ans <= MAXV && allSet->present[ans]) {
            totalPoints += 2;
        }
    }
    return totalPoints;
}
```

## Csharp

```csharp
using System.Collections.Generic;

public class Solution {
    public int ScoreOfStudents(string s, int[] answers) {
        List<int> nums = new List<int>();
        List<char> ops = new List<char>();
        foreach (char c in s) {
            if (c >= '0' && c <= '9')
                nums.Add(c - '0');
            else
                ops.Add(c);
        }

        int n = nums.Count;

        // correct answer with normal precedence (* before +)
        long total = 0;
        long curMul = nums[0];
        for (int i = 0; i < ops.Count; i++) {
            if (ops[i] == '*')
                curMul *= nums[i + 1];
            else { // '+'
                total += curMul;
                curMul = nums[i + 1];
            }
        }
        total += curMul;
        int correct = (int)total;

        // DP to compute all possible results from any parenthesization
        HashSet<int>[,] memo = new HashSet<int>[n, n];
        bool[,] visited = new bool[n, n];

        HashSet<int> Compute(int l, int r) {
            if (visited[l, r]) return memo[l, r];
            var set = new HashSet<int>();
            if (l == r) {
                set.Add(nums[l]);
            } else {
                for (int k = l; k < r; k++) {
                    char op = ops[k];
                    var left = Compute(l, k);
                    var right = Compute(k + 1, r);
                    foreach (int a in left) {
                        foreach (int b in right) {
                            long val = op == '+' ? (long)a + b : (long)a * b;
                            if (val <= 1000) set.Add((int)val);
                        }
                    }
                }
            }
            memo[l, r] = set;
            visited[l, r] = true;
            return set;
        }

        var possible = Compute(0, n - 1);

        int score = 0;
        foreach (int ans in answers) {
            if (ans == correct) score += 5;
            else if (possible.Contains(ans)) score += 2;
        }
        return score;
    }
}
```

## Javascript

```javascript
/**
 * @param {string} s
 * @param {number[]} answers
 * @return {number}
 */
var scoreOfStudents = function(s, answers) {
    // parse numbers and operators
    const nums = [];
    const ops = [];
    for (let i = 0; i < s.length; ++i) {
        const ch = s[i];
        if (ch === '+' || ch === '*') {
            ops.push(ch);
        } else {
            nums.push(ch.charCodeAt(0) - 48); // digit
        }
    }

    // evaluate with normal precedence to get the correct answer
    const evalCorrect = () => {
        const stack = [];
        let cur = nums[0];
        for (let i = 0; i < ops.length; ++i) {
            const op = ops[i];
            const nxt = nums[i + 1];
            if (op === '*') {
                cur = cur * nxt;
            } else { // '+'
                stack.push(cur);
                cur = nxt;
            }
        }
        stack.push(cur);
        return stack.reduce((a, b) => a + b, 0);
    };
    const correctAns = evalCorrect();

    // memoized DP to compute all possible results from any parenthesization
    const memo = new Map();
    const LIMIT = 1000; // answers are bounded by this

    function dfs(l, r) {
        const key = l + ',' + r;
        if (memo.has(key)) return memo.get(key);
        const res = new Set();
        if (l === r) {
            const val = nums[l];
            if (val <= LIMIT) res.add(val);
            memo.set(key, res);
            return res;
        }
        for (let k = l; k < r; ++k) { // split between k and k+1
            const leftSet = dfs(l, k);
            const rightSet = dfs(k + 1, r);
            const op = ops[k];
            for (const a of leftSet) {
                for (const b of rightSet) {
                    let v;
                    if (op === '+') v = a + b;
                    else v = a * b;
                    if (v <= LIMIT) res.add(v);
                }
            }
        }
        memo.set(key, res);
        return res;
    }

    const possible = dfs(0, nums.length - 1);

    // compute total score
    let total = 0;
    for (const ans of answers) {
        if (ans === correctAns) {
            total += 5;
        } else if (possible.has(ans)) {
            total += 2;
        }
    }
    return total;
};
```

## Typescript

```typescript
function scoreOfStudents(s: string, answers: number[]): number {
    const nums: number[] = [];
    const ops: string[] = [];
    for (let i = 0; i < s.length; i++) {
        const ch = s[i];
        if (ch === '+' || ch === '*') {
            ops.push(ch);
        } else {
            nums.push(Number(ch));
        }
    }
    const n = nums.length;
    // correct answer with normal precedence
    const stack: number[] = [nums[0]];
    for (let i = 0; i < ops.length; i++) {
        const op = ops[i];
        const num = nums[i + 1];
        if (op === '*') {
            const prev = stack.pop()!;
            stack.push(prev * num);
        } else {
            stack.push(num);
        }
    }
    const correct = stack.reduce((a, b) => a + b, 0);
    // DP for all possible results with any parenthesization
    const dp: Array<Array<Set<number>>> = Array.from({ length: n }, () => Array(n));
    for (let i = 0; i < n; i++) {
        dp[i][i] = new Set([nums[i]]);
    }
    for (let len = 2; len <= n; len++) {
        for (let i = 0; i + len - 1 < n; i++) {
            const j = i + len - 1;
            const cur = new Set<number>();
            for (let k = i; k < j; k++) {
                const op = ops[k];
                const left = dp[i][k];
                const right = dp[k + 1][j];
                for (const a of left) {
                    for (const b of right) {
                        cur.add(op === '+' ? a + b : a * b);
                    }
                }
            }
            dp[i][j] = cur;
        }
    }
    const possible = dp[0][n - 1];
    let total = 0;
    for (const ans of answers) {
        if (ans === correct) total += 5;
        else if (possible.has(ans)) total += 2;
    }
    return total;
}
```

## Php

```php
class Solution {
    /**
     * @param String $s
     * @param Integer[] $answers
     * @return Integer
     */
    function scoreOfStudents($s, $answers) {
        // parse numbers and operators
        $nums = [];
        $ops = [];
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $ch = $s[$i];
            if ($ch >= '0' && $ch <= '9') {
                $nums[] = intval($ch);
            } else {
                $ops[] = $ch;
            }
        }

        // correct answer with normal precedence (* before +)
        $total = 0;
        $cur = $nums[0];
        $opCount = count($ops);
        for ($i = 0; $i < $opCount; $i++) {
            if ($ops[$i] === '*') {
                $cur *= $nums[$i + 1];
            } else { // '+'
                $total += $cur;
                $cur = $nums[$i + 1];
            }
        }
        $total += $cur; // add last term

        // all possible results from any parenthesization (values capped at 1000)
        $possible = $this->allResults($nums, $ops);

        $score = 0;
        foreach ($answers as $ans) {
            if ($ans == $total) {
                $score += 5;
            } elseif (isset($possible[$ans])) {
                $score += 2;
            }
        }
        return $score;
    }

    private function allResults($nums, $ops) {
        $n = count($nums);
        $memo = [];
        return $this->dfs(0, $n - 1, $nums, $ops, $memo);
    }

    private function dfs($l, $r, &$nums, &$ops, &$memo) {
        $key = $l . ',' . $r;
        if (isset($memo[$key])) {
            return $memo[$key];
        }
        if ($l == $r) {
            $set = [$nums[$l] => true];
            $memo[$key] = $set;
            return $set;
        }

        $set = [];
        for ($k = $l; $k < $r; $k++) {
            $left = $this->dfs($l, $k, $nums, $ops, $memo);
            $right = $this->dfs($k + 1, $r, $nums, $ops, $memo);
            $op = $ops[$k];
            foreach ($left as $a => $_) {
                foreach ($right as $b => $_) {
                    $val = ($op === '+') ? $a + $b : $a * $b;
                    if ($val <= 1000) {
                        $set[$val] = true;
                    }
                }
            }
        }

        $memo[$key] = $set;
        return $set;
    }
}
```

## Swift

```swift
class Solution {
    func scoreOfStudents(_ s: String, _ answers: [Int]) -> Int {
        // Parse numbers and operators
        var nums = [Int]()
        var ops = [Character]()
        for ch in s {
            if ch == "+" || ch == "*" {
                ops.append(ch)
            } else {
                nums.append(Int(String(ch))!)
            }
        }
        
        // Compute correct answer with normal precedence (* before +)
        var stack = [Int]()
        var num = 0
        var lastOp: Character = "+"
        for ch in s {
            if ch >= "0" && ch <= "9" {
                num = Int(String(ch))!
            }
            if ch == "+" || ch == "*" {
                if lastOp == "+" {
                    stack.append(num)
                } else { // '*'
                    let prev = stack.removeLast()
                    stack.append(prev * num)
                }
                lastOp = ch
                num = 0
            }
        }
        // Process the final number
        if lastOp == "+" {
            stack.append(num)
        } else {
            let prev = stack.removeLast()
            stack.append(prev * num)
        }
        let correct = stack.reduce(0, +)
        
        // DP to compute all possible results from any parenthesization
        let n = nums.count
        var memo = Array(repeating: Array<Set<Int>?>(repeating: nil, count: n), count: n)
        func dfs(_ l: Int, _ r: Int) -> Set<Int> {
            if let cached = memo[l][r] { return cached }
            var res = Set<Int>()
            if l == r {
                res.insert(nums[l])
            } else {
                for k in l..<r {
                    let leftSet = dfs(l, k)
                    let rightSet = dfs(k + 1, r)
                    let op = ops[k]
                    for a in leftSet {
                        for b in rightSet {
                            if op == "+" {
                                res.insert(a + b)
                            } else { // '*'
                                res.insert(a * b)
                            }
                        }
                    }
                }
            }
            memo[l][r] = res
            return res
        }
        let possible = dfs(0, n - 1)
        
        // Score the answers
        var totalScore = 0
        for ans in answers {
            if ans == correct {
                totalScore += 5
            } else if possible.contains(ans) {
                totalScore += 2
            }
        }
        return totalScore
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun scoreOfStudents(s: String, answers: IntArray): Int {
        val nums = mutableListOf<Int>()
        val ops = mutableListOf<Char>()
        var i = 0
        while (i < s.length) {
            val c = s[i]
            if (c.isDigit()) {
                nums.add(c - '0')
                i++
            } else {
                ops.add(c)
                i++
            }
        }
        val n = nums.size

        // correct answer with normal precedence (* before +)
        var cur = nums[0]
        val stack = mutableListOf<Int>()
        for (idx in ops.indices) {
            val op = ops[idx]
            val nxt = nums[idx + 1]
            if (op == '*') {
                cur *= nxt
            } else { // '+'
                stack.add(cur)
                cur = nxt
            }
        }
        stack.add(cur)
        var correct = 0
        for (v in stack) correct += v

        val limit = 1000   // answers are within [0,1000]
        val memo = Array(n) { arrayOfNulls<MutableSet<Int>>(n) }

        fun dfs(l: Int, r: Int): MutableSet<Int> {
            memo[l][r]?.let { return it }
            val res = mutableSetOf<Int>()
            if (l == r) {
                val v = nums[l]
                if (v <= limit) res.add(v)
            } else {
                for (k in l until r) {
                    val left = dfs(l, k)
                    val right = dfs(k + 1, r)
                    val op = ops[k]
                    for (a in left) {
                        for (b in right) {
                            val value = if (op == '+') a + b else a * b
                            if (value <= limit) res.add(value)
                        }
                    }
                }
            }
            memo[l][r] = res
            return res
        }

        val possible = dfs(0, n - 1)

        var total = 0
        for (ans in answers) {
            if (ans == correct) total += 5
            else if (possible.contains(ans)) total += 2
        }
        return total
    }
}
```

## Dart

```dart
class Solution {
  int scoreOfStudents(String s, List<int> answers) {
    // Parse numbers and operators
    List<int> nums = [];
    List<String> ops = [];
    for (int i = 0; i < s.length; ++i) {
      String ch = s[i];
      if (ch == '+' || ch == '*') {
        ops.add(ch);
      } else {
        nums.add(int.parse(ch));
      }
    }

    // Compute correct answer with normal precedence (* before +)
    int cur = nums[0];
    List<int> terms = [];
    for (int i = 0; i < ops.length; ++i) {
      if (ops[i] == '*') {
        cur *= nums[i + 1];
      } else { // '+'
        terms.add(cur);
        cur = nums[i + 1];
      }
    }
    terms.add(cur);
    int correct = 0;
    for (int v in terms) correct += v;

    // DP to compute all possible results from any parenthesization
    Map<String, Set<int>> memo = {};

    Set<int> dfs(int l, int r) {
      String key = '$l,$r';
      if (memo.containsKey(key)) return memo[key]!;
      Set<int> res = {};
      if (l == r) {
        res.add(nums[l]);
      } else {
        for (int k = l; k < r; ++k) {
          Set<int> left = dfs(l, k);
          Set<int> right = dfs(k + 1, r);
          String op = ops[k];
          for (int a in left) {
            for (int b in right) {
              int val = op == '+' ? a + b : a * b;
              res.add(val);
            }
          }
        }
      }
      memo[key] = res;
      return res;
    }

    Set<int> possible = dfs(0, nums.length - 1);

    // Score the answers
    int total = 0;
    for (int ans in answers) {
      if (ans == correct) {
        total += 5;
      } else if (possible.contains(ans)) {
        total += 2;
      }
    }
    return total;
  }
}
```

## Golang

```go
func scoreOfStudents(s string, answers []int) int {
    // Parse numbers and operators
    var nums []int
    var ops []byte
    for i := 0; i < len(s); i++ {
        c := s[i]
        if c >= '0' && c <= '9' {
            nums = append(nums, int(c-'0'))
        } else { // '+' or '*'
            ops = append(ops, c)
        }
    }

    n := len(nums)

    // Compute correct answer with normal precedence (* before +)
    total := 0
    curProd := nums[0]
    for i := 0; i < len(ops); i++ {
        if ops[i] == '*' {
            curProd *= nums[i+1]
        } else { // '+'
            total += curProd
            curProd = nums[i+1]
        }
    }
    total += curProd

    // DP to compute all possible results from any parenthesization
    dp := make([][]map[int]struct{}, n)
    vis := make([][]bool, n)
    for i := 0; i < n; i++ {
        dp[i] = make([]map[int]struct{}, n)
        vis[i] = make([]bool, n)
    }

    var dfs func(l, r int) map[int]struct{}
    dfs = func(l, r int) map[int]struct{} {
        if vis[l][r] {
            return dp[l][r]
        }
        res := make(map[int]struct{})
        if l == r {
            res[nums[l]] = struct{}{}
        } else {
            for k := l; k < r; k++ { // operator index k between operand k and k+1
                leftSet := dfs(l, k)
                rightSet := dfs(k+1, r)
                op := ops[k]
                if op == '+' {
                    for a := range leftSet {
                        for b := range rightSet {
                            res[a+b] = struct{}{}
                        }
                    }
                } else { // '*'
                    for a := range leftSet {
                        for b := range rightSet {
                            res[a*b] = struct{}{}
                        }
                    }
                }
            }
        }
        dp[l][r] = res
        vis[l][r] = true
        return res
    }

    allResults := dfs(0, n-1)

    // Score the answers
    score := 0
    for _, ans := range answers {
        if ans == total {
            score += 5
        } else if _, ok := allResults[ans]; ok {
            score += 2
        }
    }
    return score
}
```

## Ruby

```ruby
require 'set'

def score_of_students(s, answers)
  numbers = []
  ops = []
  s.each_char do |ch|
    if ch >= '0' && ch <= '9'
      numbers << ch.to_i
    else
      ops << ch
    end
  end

  n = numbers.size
  memo = {}

  dfs = lambda do |l, r|
    key = [l, r]
    return memo[key] if memo.key?(key)
    if l == r
      res = Set[numbers[l]]
    else
      res = Set.new
      (l...r).each do |k|
        left_set = dfs.call(l, k)
        right_set = dfs.call(k + 1, r)
        op = ops[k]
        left_set.each do |a|
          right_set.each do |b|
            val = op == '+' ? a + b : a * b
            res.add(val)
          end
        end
      end
    end
    memo[key] = res
  end

  all_possible = dfs.call(0, n - 1)

  # compute correct value with normal precedence (* before +)
  terms = []
  cur = numbers[0]
  (0...ops.size).each do |i|
    if ops[i] == '*'
      cur *= numbers[i + 1]
    else
      terms << cur
      cur = numbers[i + 1]
    end
  end
  terms << cur
  correct = terms.sum

  total_score = 0
  answers.each do |ans|
    if ans == correct
      total_score += 5
    elsif all_possible.include?(ans)
      total_score += 2
    end
  end
  total_score
end
```

## Scala

```scala
object Solution {
    def scoreOfStudents(s: String, answers: Array[Int]): Int = {
        val nums = scala.collection.mutable.ArrayBuffer[Int]()
        val ops = scala.collection.mutable.ArrayBuffer[Char]()
        for (c <- s) {
            if (c == '+' || c == '*') ops += c
            else nums += (c - '0')
        }
        val m = nums.length

        // DP to compute all possible results with any parenthesization
        val dp = Array.ofDim[scala.collection.mutable.Set[Long]](m, m)
        for (i <- 0 until m) {
            dp(i)(i) = scala.collection.mutable.HashSet(nums(i).toLong)
        }
        for (len <- 2 to m) {
            for (i <- 0 to m - len) {
                val j = i + len - 1
                val curSet = scala.collection.mutable.HashSet[Long]()
                for (k <- i until j) {
                    val op = ops(k)
                    for (left <- dp(i)(k); right <- dp(k + 1)(j)) {
                        val res = if (op == '+') left + right else left * right
                        curSet += res
                    }
                }
                dp(i)(j) = curSet
            }
        }
        val allPossible = dp(0)(m - 1)

        // Compute correct answer with standard precedence (* before +)
        var total = 0L
        var curProd = nums(0).toLong
        for (idx <- ops.indices) {
            val op = ops(idx)
            val nextNum = nums(idx + 1).toLong
            if (op == '*') {
                curProd *= nextNum
            } else { // '+'
                total += curProd
                curProd = nextNum
            }
        }
        total += curProd
        val correct = total

        var score = 0
        for (ans <- answers) {
            val a = ans.toLong
            if (a == correct) score += 5
            else if (allPossible.contains(a)) score += 2
        }
        score
    }
}
```

## Rust

```rust
use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn score_of_students(s: String, answers: Vec<i32>) -> i32 {
        // Parse numbers and operators
        let mut nums = Vec::new();
        let mut ops = Vec::new();
        for ch in s.chars() {
            if ch == '+' || ch == '*' {
                ops.push(ch);
            } else {
                nums.push((ch as u8 - b'0') as i32);
            }
        }
        let n = nums.len();

        // Compute correct answer with normal precedence (* before +)
        let correct = {
            let mut sum = 0i32;
            for term in s.split('+') {
                let mut prod = 1i32;
                for factor in term.split('*') {
                    let v: i32 = factor.parse().unwrap();
                    prod *= v;
                }
                sum += prod;
            }
            sum
        };

        // DP to compute all possible results from any parenthesization
        fn dfs(
            l: usize,
            r: usize,
            nums: &Vec<i32>,
            ops: &Vec<char>,
            memo: &mut Vec<Vec<Option<HashSet<i32>>>>,
        ) -> HashSet<i32> {
            if let Some(ref cached) = memo[l][r] {
                return cached.clone();
            }
            let mut res = HashSet::new();
            if l == r {
                res.insert(nums[l]);
            } else {
                for k in l..r {
                    let left_set = dfs(l, k, nums, ops, memo);
                    let right_set = dfs(k + 1, r, nums, ops, memo);
                    let op = ops[k];
                    for &a in &left_set {
                        for &b in &right_set {
                            let val = match op {
                                '+' => a + b,
                                '*' => a * b,
                                _ => unreachable!(),
                            };
                            res.insert(val);
                        }
                    }
                }
            }
            memo[l][r] = Some(res.clone());
            res
        }

        let mut memo: Vec<Vec<Option<HashSet<i32>>>> = vec![vec![None; n]; n];
        let possible = dfs(0, n - 1, &nums, &ops, &mut memo);

        // Score answers
        let mut total_score = 0i32;
        for ans in answers {
            if ans == correct {
                total_score += 5;
            } else if possible.contains(&ans) {
                total_score += 2;
            }
        }
        total_score
    }
}
```

## Racket

```racket
(define/contract (score-of-students s answers)
  (-> string? (listof exact-integer?) exact-integer?)
  (let* ((nums '())
         (ops '()))
    ;; parse the expression
    (for ([i (in-range (string-length s))])
      (let ((ch (string-ref s i)))
        (cond [(and (char>=? ch #\0) (char<=? ch #\9))
               (set! nums (append nums (list (- (char->integer ch)
                                                (char->integer #\0)))))]
              [(or (char=? ch #\+) (char=? ch #\*))
               (set! ops (append ops (list ch)))])))
    (let* ((nvec (list->vector nums))
           (ovec (list->vector ops))
           (n (vector-length nvec))
           ;; correct evaluation respecting precedence (* before +)
           (correct
            (let loop ((idx 0) (cur (vector-ref nvec 0)) (sum 0))
              (if (= idx (vector-length ovec))
                  (+ sum cur)
                  (let ((op (vector-ref ovec idx))
                        (next (vector-ref nvec (+ idx 1))))
                    (if (char=? op #\*)
                        (loop (+ idx 1) (* cur next) sum)
                        (loop (+ idx 1) next (+ sum cur)))))))
           ;; memoization for all possible results with any parenthesization
           (memo (make-hash))
           (compute
            (letrec ((proc (lambda (i j)
                             (define key (cons i j))
                             (if (hash-has-key? memo key)
                                 (hash-ref memo key)
                                 (let ((res (make-hash)))
                                   (if (= i j)
                                       (hash-set! res (vector-ref nvec i) #t)
                                       (for ([k (in-range i j)])
                                         (define left  (proc i k))
                                         (define right (proc (+ k 1) j))
                                         (define op    (vector-ref ovec k))
                                         (for ([a (in-hash-keys left)])
                                           (for ([b (in-hash-keys right)])
                                             (define val (if (char=? op #\+)
                                                             (+ a b)
                                                             (* a b)))
                                             (when (<= val 1000) ; answers are bounded
                                               (hash-set! res val #t))))))
                                   (hash-set! memo key res)
                                   res)))))
              proc))
           (all-set (compute 0 (- n 1))))
      ;; compute total points
      (let loop ((lst answers) (total 0))
        (if (null? lst)
            total
            (let* ((a (car lst))
                   (pts (cond [(= a correct) 5]
                              [(hash-has-key? all-set a) 2]
                              [else 0])))
              (loop (cdr lst) (+ total pts))))))))
```

## Erlang

```erlang
-export([score_of_students/2]).
-spec score_of_students(S :: unicode:unicode_binary(), Answers :: [integer()]) -> integer().
score_of_students(S, Answers) ->
    {Nums, Ops} = parse(S),
    Correct = eval_correct(Nums, Ops),
    {AllSet,_} = compute(0, length(Nums)-1, Nums, Ops, #{}),
    lists:foldl(fun(Ac, Sum) ->
        if
            Ac == Correct -> Sum + 5;
            sets:is_element(Ac, AllSet) -> Sum + 2;
            true -> Sum
        end
    end, 0, Answers).

%% parsing the expression into numbers and operators
parse(Bin) ->
    Chars = binary_to_list(Bin),
    parse_chars(Chars, [], []).

parse_chars([], NumsRev, OpsRev) ->
    {lists:reverse(NumsRev), lists:reverse(OpsRev)};
parse_chars([C|Rest], NumsRev, OpsRev) when C >= $0, C =< $9 ->
    Digit = C - $0,
    parse_chars(Rest, [Digit|NumsRev], OpsRev);
parse_chars([C|Rest], NumsRev, OpsRev) ->
    parse_chars(Rest, NumsRev, [C|OpsRev]).

%% evaluate with normal precedence (* before +)
eval_correct([First|RestNums], Ops) ->
    eval_mul_add(RestNums, Ops, First, []).

eval_mul_add([], [], Prod, Acc) ->
    lists:sum([Prod | Acc]);
eval_mul_add([Num|NumsTail], [Op|OpsTail], Prod, Acc) ->
    case Op of
        $* -> NewProd = Prod * Num,
              eval_mul_add(NumsTail, OpsTail, NewProd, Acc);
        $+ -> eval_mul_add(NumsTail, OpsTail, Num, [Prod | Acc])
    end.

%% compute all possible results from any parenthesization
compute(L, R, Nums, Ops, Memo) ->
    case maps:is_key({L,R}, Memo) of
        true ->
            {maps:get({L,R}, Memo), Memo};
        false ->
            ResultSet =
                if L == R ->
                        sets:from_list([lists:nth(L+1, Nums)]);
                   true ->
                        compute_all_splits(L, R, Nums, Ops, sets:new(), Memo)
                end,
            NewMemo = maps:put({L,R}, ResultSet, Memo),
            {ResultSet, NewMemo}
    end.

compute_all_splits(L, R, Nums, Ops, AccSet, Memo0) ->
    lists:foldl(fun(K, {Acc, Memo}) ->
        Op = lists:nth(K+1, Ops),
        {LeftSet, Memo1} = compute(L, K, Nums, Ops, Memo),
        {RightSet, Memo2} = compute(K+1, R, Nums, Ops, Memo1),
        Combined = combine_sets(LeftSet, RightSet, Op, Acc),
        {Combined, Memo2}
    end, {AccSet, Memo0}, lists:seq(L, R-1)).

combine_sets(Left, Right, Op, Acc) ->
    sets:fold(fun(A, Acc1) ->
        sets:fold(fun(B, Acc2) ->
            Val = case Op of
                $+ -> A + B;
                $* -> A * B
            end,
            sets:add_element(Val, Acc2)
        end, Acc1, Right)
    end, Acc, Left).
```

## Elixir

```elixir
defmodule Solution do
  @spec score_of_students(s :: String.t(), answers :: [integer]) :: integer
  def score_of_students(s, answers) do
    # Parse numbers and operators
    {nums_rev, ops_rev} =
      Enum.reduce(String.graphemes(s), {[], []}, fn
        c, {ns, os} when c in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] ->
          {[String.to_integer(c) | ns], os}

        c, {ns, os} ->
          {ns, [c | os]}
      end)

    nums = Enum.reverse(nums_rev)
    ops = Enum.reverse(ops_rev)

    # Correct answer with normal precedence (* before +)
    correct =
      case nums do
        [] -> 0
        [_] -> hd(nums)
        _ ->
          {result, cur} =
            Enum.reduce(0..(length(ops) - 1), {0, hd(nums)}, fn i, {res, cur_val} ->
              op = Enum.at(ops, i)
              nxt = Enum.at(nums, i + 1)

              if op == "+" do
                {res + cur_val, nxt}
              else
                {res, cur_val * nxt}
              end
            end)

          result + cur
      end

    n = length(nums)

    # DP to compute all possible results from any parenthesization
    dp =
      Enum.reduce(0..(n - 1), %{}, fn i, acc ->
        Map.put(acc, {i, i}, MapSet.new([Enum.at(nums, i)]))
      end)

    dp =
      Enum.reduce(2..n, dp, fn len, dp_acc ->
        Enum.reduce(0..(n - len), dp_acc, fn i, inner_dp ->
          j = i + len - 1

          set =
            Enum.reduce(i..(j - 1), MapSet.new(), fn k, acc_set ->
              left = inner_dp[{i, k}]
              right = inner_dp[{k + 1, j}]
              op = Enum.at(ops, k)

              combined =
                for a <- left,
                    b <- right,
                    reduce: MapSet.new() do
                  s -> MapSet.put(s, if op == "+", do: a + b, else: a * b)
                end

              MapSet.union(acc_set, combined)
            end)

          Map.put(inner_dp, {i, j}, set)
        end)
      end)

    all_possible = dp[{0, n - 1}]

    # Score answers
    Enum.reduce(answers, 0, fn ans, sum ->
      cond do
        ans == correct -> sum + 5
        MapSet.member?(all_possible, ans) -> sum + 2
        true -> sum
      end
    end)
  end
end
```
