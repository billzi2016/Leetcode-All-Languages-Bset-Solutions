# 0726. Number of Atoms

## Cpp

```cpp
class Solution {
public:
    string countOfAtoms(string formula) {
        int n = formula.size();
        vector<unordered_map<string, long long>> stk;
        stk.emplace_back(); // base map
        
        int i = 0;
        while (i < n) {
            char c = formula[i];
            if (c == '(') {
                stk.emplace_back();
                ++i;
            } else if (c == ')') {
                ++i;
                int start = i;
                while (i < n && isdigit(formula[i])) ++i;
                long long mult = (start < i) ? stoll(formula.substr(start, i - start)) : 1LL;
                
                auto topMap = move(stk.back());
                stk.pop_back();
                for (auto &p : topMap) {
                    stk.back()[p.first] += p.second * mult;
                }
            } else { // atom
                int start = i; // uppercase letter
                ++i;
                while (i < n && islower(formula[i])) ++i;
                string atom = formula.substr(start, i - start);
                
                int numStart = i;
                while (i < n && isdigit(formula[i])) ++i;
                long long cnt = (numStart < i) ? stoll(formula.substr(numStart, i - numStart)) : 1LL;
                
                stk.back()[atom] += cnt;
            }
        }
        
        auto &finalMap = stk.back();
        vector<string> atoms;
        atoms.reserve(finalMap.size());
        for (auto &p : finalMap) atoms.push_back(p.first);
        sort(atoms.begin(), atoms.end());
        
        string res;
        for (const string &a : atoms) {
            res += a;
            long long cnt = finalMap[a];
            if (cnt > 1) res += to_string(cnt);
        }
        return res;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public String countOfAtoms(String formula) {
        Deque<Map<String, Integer>> stack = new ArrayDeque<>();
        stack.push(new HashMap<>());
        int n = formula.length();
        int i = 0;
        while (i < n) {
            char ch = formula.charAt(i);
            if (ch == '(') {
                stack.push(new HashMap<>());
                i++;
            } else if (ch == ')') {
                Map<String, Integer> top = stack.pop();
                i++; // skip ')'
                int start = i;
                while (i < n && Character.isDigit(formula.charAt(i))) i++;
                int mult = start < i ? Integer.parseInt(formula.substring(start, i)) : 1;
                Map<String, Integer> cur = stack.peek();
                for (Map.Entry<String, Integer> e : top.entrySet()) {
                    cur.put(e.getKey(), cur.getOrDefault(e.getKey(), 0) + e.getValue() * mult);
                }
            } else { // atom
                int start = i;
                i++; // first uppercase
                while (i < n && Character.isLowerCase(formula.charAt(i))) i++;
                String atom = formula.substring(start, i);
                int numStart = i;
                while (i < n && Character.isDigit(formula.charAt(i))) i++;
                int count = numStart < i ? Integer.parseInt(formula.substring(numStart, i)) : 1;
                Map<String, Integer> cur = stack.peek();
                cur.put(atom, cur.getOrDefault(atom, 0) + count);
            }
        }
        Map<String, Integer> result = stack.pop();
        List<String> atoms = new ArrayList<>(result.keySet());
        Collections.sort(atoms);
        StringBuilder sb = new StringBuilder();
        for (String atom : atoms) {
            sb.append(atom);
            int cnt = result.get(atom);
            if (cnt > 1) sb.append(cnt);
        }
        return sb.toString();
    }
}
```

## Python

```python
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        n = len(formula)
        stack = [dict()]  # each element holds counts for current scope
        i = 0
        while i < n:
            ch = formula[i]
            if ch == '(':
                stack.append(dict())
                i += 1
            elif ch == ')':
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                mult = int(formula[start:i]) if start != i else 1
                cur = stack.pop()
                for atom, cnt in cur.items():
                    stack[-1][atom] = stack[-1].get(atom, 0) + cnt * mult
            elif ch.isupper():
                j = i + 1
                while j < n and formula[j].islower():
                    j += 1
                atom = formula[i:j]
                k = j
                while k < n and formula[k].isdigit():
                    k += 1
                cnt = int(formula[j:k]) if j != k else 1
                stack[-1][atom] = stack[-1].get(atom, 0) + cnt
                i = k
            else:
                # digits are processed together with preceding atom or ')'
                i += 1

        final_counts = stack.pop()
        result_parts = []
        for atom in sorted(final_counts):
            count = final_counts[atom]
            if count == 1:
                result_parts.append(atom)
            else:
                result_parts.append(f"{atom}{count}")
        return "".join(result_parts)
```

## Python3

```python
import collections

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        i = 0
        stack = [collections.Counter()]
        while i < n:
            ch = formula[i]
            if ch == '(':
                stack.append(collections.Counter())
                i += 1
            elif ch == ')':
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                mult = int(formula[start:i] or 1)
                top = stack.pop()
                for atom, cnt in top.items():
                    stack[-1][atom] += cnt * mult
            else:  # atom
                start = i
                i += 1  # first uppercase letter
                while i < n and formula[i].islower():
                    i += 1
                name = formula[start:i]
                start_num = i
                while i < n and formula[i].isdigit():
                    i += 1
                cnt = int(formula[start_num:i] or 1)
                stack[-1][name] += cnt

        result_parts = []
        for atom in sorted(stack[0]):
            count = stack[0][atom]
            if count > 1:
                result_parts.append(f"{atom}{count}")
            else:
                result_parts.append(atom)
        return "".join(result_parts)
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct {
    char **atoms;
    int *counts;
    int size;
    int capacity;
} Map;

static Map* createMap() {
    Map *m = (Map*)malloc(sizeof(Map));
    m->capacity = 16;
    m->size = 0;
    m->atoms = (char**)malloc(m->capacity * sizeof(char*));
    m->counts = (int*)malloc(m->capacity * sizeof(int));
    return m;
}

static char* strDup(const char *s) {
    size_t len = strlen(s);
    char *r = (char*)malloc(len + 1);
    memcpy(r, s, len + 1);
    return r;
}

static void ensureCapacity(Map *m) {
    if (m->size >= m->capacity) {
        m->capacity <<= 1;
        m->atoms = (char**)realloc(m->atoms, m->capacity * sizeof(char*));
        m->counts = (int*)realloc(m->counts, m->capacity * sizeof(int));
    }
}

static void add(Map *m, const char *atom, int cnt) {
    for (int i = 0; i < m->size; ++i) {
        if (strcmp(m->atoms[i], atom) == 0) {
            m->counts[i] += cnt;
            return;
        }
    }
    ensureCapacity(m);
    m->atoms[m->size] = strDup(atom);
    m->counts[m->size] = cnt;
    ++m->size;
}

static void merge(Map *dest, Map *src, int mult) {
    for (int i = 0; i < src->size; ++i) {
        add(dest, src->atoms[i], src->counts[i] * mult);
    }
}

/* Recursive parser */
static Map* parse(const char *s, int *pos) {
    int n = strlen(s);
    Map *cur = createMap();
    while (*pos < n && s[*pos] != ')') {
        if (s[*pos] == '(') {
            (*pos)++;                     // skip '('
            Map *inner = parse(s, pos);   // parse inside parentheses
            (*pos)++;                     // skip ')'
            int mult = 0;
            while (*pos < n && isdigit(s[*pos])) {
                mult = mult * 10 + (s[*pos] - '0');
                (*pos)++;
            }
            if (mult == 0) mult = 1;
            merge(cur, inner, mult);
            /* free inner map structures (atoms strings are duplicated in add) */
            for (int i = 0; i < inner->size; ++i) free(inner->atoms[i]);
            free(inner->atoms);
            free(inner->counts);
            free(inner);
        } else { // atom
            int start = *pos;
            (*pos)++; // uppercase letter
            while (*pos < n && islower(s[*pos])) (*pos)++;
            int lenAtom = *pos - start;
            char *atom = (char*)malloc(lenAtom + 1);
            memcpy(atom, s + start, lenAtom);
            atom[lenAtom] = '\0';
            int cnt = 0;
            while (*pos < n && isdigit(s[*pos])) {
                cnt = cnt * 10 + (s[*pos] - '0');
                (*pos)++;
            }
            if (cnt == 0) cnt = 1;
            add(cur, atom, cnt);
            free(atom);
        }
    }
    return cur;
}

/* Comparator for qsort */
typedef struct {
    char *atom;
    int count;
} Pair;

static int cmpPair(const void *a, const void *b) {
    const Pair *pa = (const Pair *)a;
    const Pair *pb = (const Pair *)b;
    return strcmp(pa->atom, pb->atom);
}

char* countOfAtoms(char* formula) {
    int pos = 0;
    Map *m = parse(formula, &pos);

    int sz = m->size;
    Pair *pairs = (Pair*)malloc(sz * sizeof(Pair));
    for (int i = 0; i < sz; ++i) {
        pairs[i].atom = m->atoms[i];
        pairs[i].count = m->counts[i];
    }

    qsort(pairs, sz, sizeof(Pair), cmpPair);

    int totalLen = 0;
    for (int i = 0; i < sz; ++i) {
        totalLen += strlen(pairs[i].atom);
        if (pairs[i].count > 1) {
            char buf[20];
            int len = sprintf(buf, "%d", pairs[i].count);
            totalLen += len;
        }
    }

    char *result = (char*)malloc(totalLen + 1);
    char *p = result;
    for (int i = 0; i < sz; ++i) {
        int l = strlen(pairs[i].atom);
        memcpy(p, pairs[i].atom, l);
        p += l;
        if (pairs[i].count > 1) {
            p += sprintf(p, "%d", pairs[i].count);
        }
    }
    *p = '\0';

    /* free map structures */
    for (int i = 0; i < sz; ++i) free(pairs[i].atom);
    free(pairs);
    free(m->atoms);
    free(m->counts);
    free(m);

    return result;
}
```

## Csharp

```csharp
public class Solution
{
    public string CountOfAtoms(string formula)
    {
        int n = formula.Length;
        int i = 0;

        // Stack of dictionaries to hold counts at each nesting level
        var stack = new System.Collections.Generic.Stack<System.Collections.Generic.Dictionary<string, int>>();
        stack.Push(new System.Collections.Generic.Dictionary<string, int>());

        // Helper to parse a number starting at current index; returns 1 if no number present
        int ParseNumber()
        {
            if (i >= n || !char.IsDigit(formula[i]))
                return 1;
            int val = 0;
            while (i < n && char.IsDigit(formula[i]))
            {
                val = val * 10 + (formula[i] - '0');
                i++;
            }
            return val;
        }

        while (i < n)
        {
            char ch = formula[i];
            if (ch == '(')
            {
                // Start a new scope
                stack.Push(new System.Collections.Generic.Dictionary<string, int>());
                i++;
            }
            else if (ch == ')')
            {
                i++; // move past ')'
                int mult = ParseNumber(); // multiplier after the parenthesis

                var topMap = stack.Pop(); // map for this inner group
                var prevMap = stack.Peek();

                foreach (var kvp in topMap)
                {
                    long multiplied = (long)kvp.Value * mult; // use long to avoid intermediate overflow
                    int addVal = (int)multiplied;
                    if (prevMap.ContainsKey(kvp.Key))
                        prevMap[kvp.Key] += addVal;
                    else
                        prevMap[kvp.Key] = addVal;
                }
            }
            else // must be an atom starting with uppercase letter
            {
                var sb = new System.Text.StringBuilder();
                sb.Append(ch);
                i++;
                while (i < n && char.IsLower(formula[i]))
                {
                    sb.Append(formula[i]);
                    i++;
                }
                string name = sb.ToString();

                int count = ParseNumber();

                var curMap = stack.Peek();
                if (curMap.ContainsKey(name))
                    curMap[name] += count;
                else
                    curMap[name] = count;
            }
        }

        var finalMap = stack.Pop();
        var keys = new System.Collections.Generic.List<string>(finalMap.Keys);
        keys.Sort(System.StringComparer.Ordinal);

        var result = new System.Text.StringBuilder();
        foreach (var key in keys)
        {
            result.Append(key);
            int cnt = finalMap[key];
            if (cnt > 1)
                result.Append(cnt);
        }

        return result.ToString();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} formula
 * @return {string}
 */
var countOfAtoms = function(formula) {
    const n = formula.length;
    const stack = [new Map()];
    
    const isDigit = (c) => c >= '0' && c <= '9';
    const isLower = (c) => c >= 'a' && c <= 'z';
    
    let i = 0;
    while (i < n) {
        const ch = formula[i];
        if (ch === '(') {
            stack.push(new Map());
            i++;
        } else if (ch === ')') {
            i++;
            // parse multiplier after ')'
            let start = i;
            while (i < n && isDigit(formula[i])) i++;
            const mult = start === i ? 1 : parseInt(formula.slice(start, i), 10);
            
            const topMap = stack.pop();
            const curMap = stack[stack.length - 1];
            for (const [atom, cnt] of topMap.entries()) {
                curMap.set(atom, (curMap.get(atom) || 0) + cnt * mult);
            }
        } else { // atom
            // parse atom name
            let start = i;
            i++; // consume uppercase
            while (i < n && isLower(formula[i])) i++;
            const atom = formula.slice(start, i);
            
            // parse count
            let numStart = i;
            while (i < n && isDigit(formula[i])) i++;
            const cnt = numStart === i ? 1 : parseInt(formula.slice(numStart, i), 10);
            
            const curMap = stack[stack.length - 1];
            curMap.set(atom, (curMap.get(atom) || 0) + cnt);
        }
    }
    
    const finalMap = stack.pop();
    const atoms = Array.from(finalMap.keys()).sort();
    let result = '';
    for (const atom of atoms) {
        const count = finalMap.get(atom);
        result += atom + (count > 1 ? count : '');
    }
    return result;
};
```

## Typescript

```typescript
function countOfAtoms(formula: string): string {
    const n = formula.length;
    const stack: Map<string, number>[] = [new Map()];
    let i = 0;

    const isDigit = (c: number) => c >= 48 && c <= 57; // '0' - '9'
    const isLower = (c: number) => c >= 97 && c <= 122; // 'a' - 'z'

    while (i < n) {
        const ch = formula.charCodeAt(i);
        if (ch === 40) { // '('
            stack.push(new Map());
            i++;
        } else if (ch === 41) { // ')'
            i++;
            let start = i;
            while (i < n && isDigit(formula.charCodeAt(i))) i++;
            const multStr = formula.slice(start, i);
            const mult = multStr.length ? parseInt(multStr) : 1;

            const topMap = stack.pop()!;
            const prevMap = stack[stack.length - 1];
            for (const [atom, cnt] of topMap.entries()) {
                const newCnt = cnt * mult;
                prevMap.set(atom, (prevMap.get(atom) ?? 0) + newCnt);
            }
        } else { // atom
            let startName = i; // uppercase letter
            i++; // move past uppercase
            while (i < n && isLower(formula.charCodeAt(i))) i++;
            const name = formula.slice(startName, i);

            let startCnt = i;
            while (i < n && isDigit(formula.charCodeAt(i))) i++;
            const cntStr = formula.slice(startCnt, i);
            const cnt = cntStr.length ? parseInt(cntStr) : 1;

            const curMap = stack[stack.length - 1];
            curMap.set(name, (curMap.get(name) ?? 0) + cnt);
        }
    }

    const finalMap = stack.pop()!;
    const atoms = Array.from(finalMap.keys()).sort();
    let result = '';
    for (const atom of atoms) {
        const count = finalMap.get(atom)!;
        result += atom;
        if (count > 1) result += count.toString();
    }
    return result;
}
```

## Php

```php
class Solution {
    /**
     * @param String $formula
     * @return String
     */
    function countOfAtoms($formula) {
        $n = strlen($formula);
        $stack = [];
        // push a base map
        $stack[] = [];

        $i = 0;
        while ($i < $n) {
            $ch = $formula[$i];
            if ($ch === '(') {
                // start new scope
                $stack[] = [];
                $i++;
            } elseif ($ch === ')') {
                $i++;
                // parse multiplier after ')'
                $mult = 0;
                while ($i < $n && ctype_digit($formula[$i])) {
                    $mult = $mult * 10 + intval($formula[$i]);
                    $i++;
                }
                if ($mult === 0) $mult = 1;

                // pop current map and merge
                $currMap = array_pop($stack);
                $topIdx = count($stack) - 1;
                foreach ($currMap as $atom => $cnt) {
                    $add = $cnt * $mult;
                    if (isset($stack[$topIdx][$atom])) {
                        $stack[$topIdx][$atom] += $add;
                    } else {
                        $stack[$topIdx][$atom] = $add;
                    }
                }
            } else { // must be an atom starting with uppercase
                // parse atom name
                $atom = $ch;
                $i++;
                while ($i < $n && ctype_lower($formula[$i])) {
                    $atom .= $formula[$i];
                    $i++;
                }
                // parse count
                $cnt = 0;
                while ($i < $n && ctype_digit($formula[$i])) {
                    $cnt = $cnt * 10 + intval($formula[$i]);
                    $i++;
                }
                if ($cnt === 0) $cnt = 1;

                // add to current map
                $topIdx = count($stack) - 1;
                if (isset($stack[$topIdx][$atom])) {
                    $stack[$topIdx][$atom] += $cnt;
                } else {
                    $stack[$topIdx][$atom] = $cnt;
                }
            }
        }

        $result = $stack[0];
        ksort($result);
        $ans = '';
        foreach ($result as $atom => $cnt) {
            $ans .= $atom;
            if ($cnt > 1) {
                $ans .= $cnt;
            }
        }
        return $ans;
    }
}
```

## Swift

```swift
class Solution {
    func countOfAtoms(_ formula: String) -> String {
        let chars = Array(formula)
        var i = 0
        let n = chars.count
        var stack: [Dictionary<String, Int>] = [[:]]
        
        func parseNumber() -> Int {
            var num = 0
            while i < n && chars[i].isNumber {
                if let digit = Int(String(chars[i])) {
                    num = num * 10 + digit
                }
                i += 1
            }
            return num == 0 ? 1 : num
        }
        
        func parseAtom() -> String {
            var atom = ""
            atom.append(chars[i]) // uppercase guaranteed
            i += 1
            while i < n && chars[i].isLowercase {
                atom.append(chars[i])
                i += 1
            }
            return atom
        }
        
        while i < n {
            let ch = chars[i]
            if ch == "(" {
                stack.append([:])
                i += 1
            } else if ch == ")" {
                i += 1
                let mult = parseNumber()
                var top = stack.removeLast()
                for (atom, cnt) in top {
                    stack[stack.count - 1][atom, default: 0] += cnt * mult
                }
            } else { // atom
                let atom = parseAtom()
                let count = parseNumber()
                stack[stack.count - 1][atom, default: 0] += count
            }
        }
        
        let result = stack.last!
        let sortedKeys = result.keys.sorted()
        var ans = ""
        for key in sortedKeys {
            ans.append(key)
            if let cnt = result[key], cnt > 1 {
                ans.append(String(cnt))
            }
        }
        return ans
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun countOfAtoms(formula: String): String {
        val n = formula.length
        val stack = ArrayDeque<MutableMap<String, Long>>()
        stack.push(mutableMapOf())
        var i = 0
        while (i < n) {
            when (val ch = formula[i]) {
                '(' -> {
                    stack.push(mutableMapOf())
                    i++
                }
                ')' -> {
                    i++
                    var start = i
                    while (i < n && formula[i].isDigit()) i++
                    val mult = if (start == i) 1 else formula.substring(start, i).toInt()
                    val top = stack.pop()
                    val curMap = stack.peek()
                    for ((atom, cnt) in top) {
                        curMap[atom] = curMap.getOrDefault(atom, 0L) + cnt * mult
                    }
                }
                else -> {
                    if (ch.isUpperCase()) {
                        var start = i
                        i++ // consume uppercase
                        while (i < n && formula[i].isLowerCase()) i++
                        val atom = formula.substring(start, i)
                        val numStart = i
                        while (i < n && formula[i].isDigit()) i++
                        val cnt = if (numStart == i) 1 else formula.substring(numStart, i).toInt()
                        val curMap = stack.peek()
                        curMap[atom] = curMap.getOrDefault(atom, 0L) + cnt
                    } else {
                        // Should not happen for valid input
                        i++
                    }
                }
            }
        }
        val resultMap = stack.pop()
        val keys = resultMap.keys.sorted()
        val sb = StringBuilder()
        for (k in keys) {
            sb.append(k)
            val v = resultMap[k]!!
            if (v > 1) sb.append(v)
        }
        return sb.toString()
    }
}
```

## Dart

```dart
class Solution {
  String countOfAtoms(String formula) {
    int n = formula.length;
    List<Map<String, int>> stack = [{}];
    int i = 0;

    bool isDigit(String ch) =>
        ch.codeUnitAt(0) >= 48 && ch.codeUnitAt(0) <= 57;
    bool isLower(String ch) =>
        ch.codeUnitAt(0) >= 97 && ch.codeUnitAt(0) <= 122;

    while (i < n) {
      String ch = formula[i];
      if (ch == '(') {
        stack.add({});
        i++;
      } else if (ch == ')') {
        i++;
        int start = i;
        while (i < n && isDigit(formula[i])) i++;
        int mult = start < i ? int.parse(formula.substring(start, i)) : 1;

        Map<String, int> top = stack.removeLast();
        Map<String, int> prev = stack.last;
        top.forEach((atom, cnt) {
          prev[atom] = (prev[atom] ?? 0) + cnt * mult;
        });
      } else {
        // parse atom name
        int start = i;
        i++; // first uppercase letter
        while (i < n && isLower(formula[i])) i++;
        String atom = formula.substring(start, i);

        // parse count
        int numStart = i;
        while (i < n && isDigit(formula[i])) i++;
        int cnt = numStart < i ? int.parse(formula.substring(numStart, i)) : 1;

        Map<String, int> cur = stack.last;
        cur[atom] = (cur[atom] ?? 0) + cnt;
      }
    }

    Map<String, int> finalMap = stack.single;
    List<String> atoms = finalMap.keys.toList()..sort();

    StringBuffer sb = StringBuffer();
    for (String atom in atoms) {
      sb.write(atom);
      int count = finalMap[atom]!;
      if (count > 1) sb.write(count);
    }
    return sb.toString();
  }
}
```

## Golang

```go
package main

import (
	"sort"
	"strconv"
	"strings"
)

func countOfAtoms(formula string) string {
	n := len(formula)
	stack := []map[string]int{make(map[string]int)}
	i := 0
	for i < n {
		ch := formula[i]
		if ch == '(' {
			stack = append(stack, make(map[string]int))
			i++
		} else if ch == ')' {
			i++
			start := i
			for i < n && formula[i] >= '0' && formula[i] <= '9' {
				i++
			}
			mult := 1
			if start < i {
				val, _ := strconv.Atoi(formula[start:i])
				mult = val
			}
			topMap := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			for atom, cnt := range topMap {
				stack[len(stack)-1][atom] += cnt * mult
			}
		} else { // atom
			start := i
			i++ // consume uppercase
			for i < n && formula[i] >= 'a' && formula[i] <= 'z' {
				i++
			}
			atom := formula[start:i]
			numStart := i
			for i < n && formula[i] >= '0' && formula[i] <= '9' {
				i++
			}
			cnt := 1
			if numStart < i {
				val, _ := strconv.Atoi(formula[numStart:i])
				cnt = val
			}
			stack[len(stack)-1][atom] += cnt
		}
	}
	m := stack[0]
	keys := make([]string, 0, len(m))
	for k := range m {
		keys = append(keys, k)
	}
	sort.Strings(keys)
	var sb strings.Builder
	for _, atom := range keys {
		sb.WriteString(atom)
		if m[atom] > 1 {
			sb.WriteString(strconv.Itoa(m[atom]))
		}
	}
	return sb.String()
}
```

## Ruby

```ruby
def count_of_atoms(formula)
  bytes = formula.bytes
  n = bytes.length
  i = 0
  stack = [Hash.new(0)]

  while i < n
    b = bytes[i]
    if b == 40 # '('
      stack << Hash.new(0)
      i += 1
    elsif b == 41 # ')'
      i += 1
      start = i
      while i < n && bytes[i] >= 48 && bytes[i] <= 57
        i += 1
      end
      mult = (start < i) ? formula[start...i].to_i : 1
      popped = stack.pop
      popped.each do |atom, cnt|
        stack[-1][atom] += cnt * mult
      end
    else # atom start with uppercase letter
      start_atom = i
      i += 1
      while i < n && bytes[i] >= 97 && bytes[i] <= 122
        i += 1
      end
      atom = formula[start_atom...i]
      start_num = i
      while i < n && bytes[i] >= 48 && bytes[i] <= 57
        i += 1
      end
      cnt = (start_num < i) ? formula[start_num...i].to_i : 1
      stack[-1][atom] += cnt
    end
  end

  result = stack.pop
  keys = result.keys.sort
  ans = ""
  keys.each do |k|
    ans << k
    v = result[k]
    ans << v.to_s if v > 1
  end
  ans
end
```

## Scala

```scala
object Solution {
    import scala.collection.mutable

    def countOfAtoms(formula: String): String = {
        val n = formula.length
        var i = 0
        val stack = new mutable.Stack[mutable.Map[String, Long]]()
        stack.push(mutable.Map.empty[String, Long])

        while (i < n) {
            val ch = formula.charAt(i)
            if (ch == '(') {
                stack.push(mutable.Map.empty[String, Long])
                i += 1
            } else if (ch == ')') {
                i += 1
                var start = i
                while (i < n && formula.charAt(i).isDigit) i += 1
                val multStr = formula.substring(start, i)
                val mult = if (multStr.isEmpty) 1L else multStr.toLong

                val topMap = stack.pop()
                val curMap = stack.top
                for ((atom, cnt) <- topMap) {
                    curMap(atom) = curMap.getOrElse(atom, 0L) + cnt * mult
                }
            } else { // atom starts with uppercase
                var start = i
                i += 1 // consume uppercase
                while (i < n && formula.charAt(i).isLower) i += 1
                val atom = formula.substring(start, i)

                var numStart = i
                while (i < n && formula.charAt(i).isDigit) i += 1
                val numStr = formula.substring(numStart, i)
                val cnt = if (numStr.isEmpty) 1L else numStr.toLong

                val curMap = stack.top
                curMap(atom) = curMap.getOrElse(atom, 0L) + cnt
            }
        }

        val finalMap = stack.pop()
        val keys = finalMap.keys.toArray.sorted
        val sb = new StringBuilder
        for (k <- keys) {
            sb.append(k)
            val v = finalMap(k)
            if (v > 1) sb.append(v)
        }
        sb.toString()
    }
}
```

## Rust

```rust
impl Solution {
    pub fn count_of_atoms(formula: String) -> String {
        use std::collections::HashMap;

        fn parse_number(bytes: &[u8], mut i: usize) -> (i64, usize) {
            let n = bytes.len();
            if i >= n || !bytes[i].is_ascii_digit() {
                return (0, i);
            }
            let mut num = 0i64;
            while i < n && bytes[i].is_ascii_digit() {
                num = num * 10 + (bytes[i] - b'0') as i64;
                i += 1;
            }
            (num, i)
        }

        let bytes = formula.as_bytes();
        let n = bytes.len();
        let mut stack: Vec<HashMap<String, i64>> = vec![HashMap::new()];
        let mut i = 0usize;

        while i < n {
            match bytes[i] as char {
                '(' => {
                    stack.push(HashMap::new());
                    i += 1;
                }
                ')' => {
                    i += 1;
                    let (mult, new_i) = parse_number(bytes, i);
                    i = new_i;
                    let mult = if mult == 0 { 1 } else { mult };
                    let mut top = stack.pop().unwrap();
                    for (atom, cnt) in top.drain() {
                        let entry = stack.last_mut().unwrap().entry(atom).or_insert(0);
                        *entry += cnt * mult;
                    }
                }
                c if c.is_ascii_uppercase() => {
                    // parse atom name
                    let mut name = String::new();
                    name.push(c);
                    i += 1;
                    while i < n && (bytes[i] as char).is_ascii_lowercase() {
                        name.push(bytes[i] as char);
                        i += 1;
                    }
                    // parse count
                    let (cnt, new_i) = parse_number(bytes, i);
                    i = new_i;
                    let cnt = if cnt == 0 { 1 } else { cnt };
                    let entry = stack.last_mut().unwrap().entry(name).or_insert(0);
                    *entry += cnt;
                }
                _ => {
                    // should not occur with valid input
                    i += 1;
                }
            }
        }

        let mut result = String::new();
        if let Some(final_map) = stack.pop() {
            let mut keys: Vec<String> = final_map.keys().cloned().collect();
            keys.sort();
            for k in keys {
                result.push_str(&k);
                let v = final_map.get(&k).unwrap();
                if *v > 1 {
                    result.push_str(&v.to_string());
                }
            }
        }
        result
    }
}
```

## Racket

```racket
(define/contract (count-of-atoms formula)
  (-> string? string?)
  (let* ((n (string-length formula))
         (upper?
          (lambda (c) (and (char>=? c #\A) (char<=? c #\Z))))
         (lower?
          (lambda (c) (and (char>=? c #\a) (char<=? c #\z))))
         (digit?
          (lambda (c) (and (char>=? c #\0) (char<=? c #\9))))
         ;; parse a number starting at idx; return (values number next-index)
         (parse-number
          (lambda (idx)
            (let loop ((j idx) (num 0) (found? #f))
              (if (and (< j n) (digit? (string-ref formula j)))
                  (loop (+ j 1)
                        (+ (* num 10)
                           (- (char->integer (string-ref formula j))
                              (char->integer #\0)))
                        #t)
                  (values (if found? num 1) j)))))
         ;; parse an atom name and its count starting at idx
         (parse-atom
          (lambda (idx)
            (let ((start idx))
              (let loop-name ((j (+ idx 1)))
                (if (and (< j n) (lower? (string-ref formula j)))
                    (loop-name (+ j 1))
                    (let ((name (substring formula start j)))
                      (call-with-values
                       (lambda () (parse-number j))
                       (lambda (cnt nexti)
                         (values name cnt nexti))))))))
         ;; add count to hashmap
         (add-to-map!
          (lambda (hm atom cnt)
            (hash-set! hm atom (+ (hash-ref hm atom 0) cnt)))))
    ;; main processing loop
    (let loop ((i 0) (stack (list (make-hash))))
      (if (= i n)
          (let* ((result (first stack))
                 (keys (sort (hash-keys result) string<?)))
            (for/fold ([s ""]) ([k keys])
              (let ((cnt (hash-ref result k)))
                (string-append s k (if (= cnt 1) "" (number->string cnt))))))
          (let ((c (string-ref formula i)))
            (cond
              [(char=? c #\()
               (loop (+ i 1) (cons (make-hash) stack))]
              [(char=? c #\))
               (call-with-values
                (lambda () (parse-number (+ i 1)))
                (lambda (mult nexti)
                  (let* ((cur (first stack))
                         (rest (rest stack)))
                    (for ([k (hash-keys cur)])
                      (add-to-map! (first rest) k (* (hash-ref cur k) mult)))
                    (loop nexti rest))))]
              [(upper? c)
               (call-with-values
                (lambda () (parse-atom i))
                (lambda (name cnt nexti)
                  (add-to-map! (first stack) name cnt)
                  (loop nexti stack)))]
              [else
               (loop (+ i 1) stack)]))))))
```

## Erlang

```erlang
-module(solution).
-export([count_of_atoms/1]).
-spec count_of_atoms(Formula :: unicode:unicode_binary()) -> unicode:unicode_binary().
count_of_atoms(Formula) ->
    Chars = unicode:characters_to_list(Formula),
    {Map, _} = parse_seq(#{}, Chars),
    Sorted = lists:keysort(1, maps:to_list(Map)),
    build_result(Sorted).

%% Parse a sequence until end or ')'
parse_seq(Map, []) -> {Map, []};
parse_seq(Map, [$)|Rest]) -> {Map, Rest};
parse_seq(Map, [$$(|Rest]) ->
    {InnerMap, AfterParen} = parse_seq(#{}, Rest),
    {Multiplier, Remaining} = parse_number(AfterParen),
    UpdatedInner = multiply_map(InnerMap, Multiplier),
    NewMap = merge_maps(Map, UpdatedInner),
    parse_seq(NewMap, Remaining);
parse_seq(Map, Chars) ->
    {Atom, AfterAtom} = parse_atom(Chars),
    {Count, Remaining} = parse_number(AfterAtom),
    NewMap = maps:update_with(
                Atom,
                fun(Old) -> Old + Count end,
                Count,
                Map),
    parse_seq(NewMap, Remaining).

%% Parse an atom name: Uppercase followed by zero or more lowercase
parse_atom([U|Rest]) when U >= $A, U =< $Z ->
    {LowerList, Rest2} = collect_lower(Rest, []),
    AtomChars = [U | LowerList],
    {list_to_binary(AtomChars), Rest2}.

collect_lower([C|Rest], Acc) when C >= $a, C =< $z ->
    collect_lower(Rest, [C|Acc]);
collect_lower(Rest, Acc) ->
    {lists:reverse(Acc), Rest}.

%% Parse a number; if absent return 1
parse_number([D|Rest]) when D >= $0, D =< $9 ->
    {DigitsRev, Rest2} = collect_digits(Rest, [D]),
    Number = list_to_integer(lists:reverse(DigitsRev)),
    {Number, Rest2};
parse_number(Chars) -> {1, Chars}.

collect_digits([C|Rest], Acc) when C >= $0, C =< $9 ->
    collect_digits(Rest, [C|Acc]);
collect_digits(Rest, Acc) ->
    {lists:reverse(Acc), Rest}.

%% Multiply all values in a map by Mult
multiply_map(Map, Mult) ->
    maps:map(fun(_K, V) -> V * Mult end, Map).

%% Merge two maps adding counts
merge_maps(M1, M2) ->
    maps:fold(
        fun(Key, Val, Acc) ->
            maps:update_with(
                Key,
                fun(Old) -> Old + Val end,
                Val,
                Acc)
        end,
        M1,
        M2).

%% Build the final binary result from sorted list
build_result([]) -> <<>>;
build_result([{Atom, Count} | Rest]) ->
    CountBin = case Count of
                   1 -> <<>>;
                   _ -> integer_to_binary(Count)
               end,
    <<Atom/binary, CountBin/binary, (build_result(Rest))/binary>>.
```

## Elixir

```elixir
defmodule Solution do
  @spec count_of_atoms(formula :: String.t) :: String.t
  def count_of_atoms(formula) do
    {atom_counts, _} = parse(formula, %{})
    keys = Map.keys(atom_counts) |> Enum.sort()
    Enum.map_join(keys, fn atom ->
      cnt = atom_counts[atom]
      if cnt == 1, do: atom, else: atom <> Integer.to_string(cnt)
    end)
  end

  # Recursive parsing
  defp parse(<<>>, acc), do: {acc, <<>>}

  defp parse(<<"(", rest::binary>>, acc) do
    {inner_map, rest_after_inner} = parse(rest, %{})
    {multiplier, rest_after_multiplier} = read_number(rest_after_inner)
    merged = merge_maps(acc, multiply_map(inner_map, multiplier))
    parse(rest_after_multiplier, merged)
  end

  defp parse(<<")", rest::binary>>, acc) do
    {acc, rest}
  end

  defp parse(<<c::utf8, _rest::binary>> = bin, acc) when c >= ?A and c <= ?Z do
    <<first, rest::binary>> = bin
    {atom_name, rest1} = read_atom_name(first, rest)
    {cnt, rest2} = read_number(rest1)
    merged = Map.update(acc, atom_name, cnt, &(&1 + cnt))
    parse(rest2, merged)
  end

  # Read an atom name: first uppercase already consumed
  defp read_atom_name(first, bin) do
    {lower, rest} = take_while_lower(bin, [])
    {<<first>> <> lower, rest}
  end

  defp take_while_lower(<<c::utf8, rest::binary>>, acc) when c >= ?a and c <= ?z do
    take_while_lower(rest, [<<c>> | acc])
  end

  defp take_while_lower(bin, acc) do
    {Enum.reverse(acc) |> IO.iodata_to_binary(), bin}
  end

  # Read a number; default is 1
  defp read_number(<<c::utf8, _rest::binary>> = bin) when c >= ?0 and c <= ?9 do
    <<first, rest::binary>> = bin
    {num_str, rest2} = collect_digits(rest, [<<first>>])
    {String.to_integer(num_str), rest2}
  end

  defp read_number(bin), do: {1, bin}

  defp collect_digits(<<c::utf8, rest::binary>>, acc) when c >= ?0 and c <= ?9 do
    collect_digits(rest, [<<c>> | acc])
  end

  defp collect_digits(bin, acc) do
    {Enum.reverse(acc) |> IO.iodata_to_binary(), bin}
  end

  # Multiply all counts in a map by a factor
  defp multiply_map(map, 1), do: map

  defp multiply_map(map, mult) do
    Enum.into(map, %{}, fn {k, v} -> {k, v * mult} end)
  end

  # Merge two maps adding counts for duplicate atoms
  defp merge_maps(m1, m2) do
    Map.merge(m1, m2, fn _k, v1, v2 -> v1 + v2 end)
  end
end
```
