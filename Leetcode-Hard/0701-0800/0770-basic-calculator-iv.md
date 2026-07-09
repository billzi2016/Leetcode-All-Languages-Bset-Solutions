# 0770. Basic Calculator IV

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    struct Poly {
        // map from sorted list of variables to coefficient
        map<vector<string>, long long> terms;
        
        static Poly fromNumber(long long val) {
            Poly p;
            if (val != 0) p.terms[{}] = val;
            return p;
        }
        static Poly fromVariable(const string& var) {
            Poly p;
            p.terms[{var}] = 1;
            return p;
        }
        
        Poly add(const Poly& other, int sign) const { // sign = +1 or -1
            Poly res = *this;
            for (auto &kv : other.terms) {
                long long coeff = kv.second * sign;
                auto it = res.terms.find(kv.first);
                if (it != res.terms.end()) {
                    it->second += coeff;
                    if (it->second == 0) res.terms.erase(it);
                } else {
                    if (coeff != 0) res.terms[kv.first] = coeff;
                }
            }
            return res;
        }
        
        Poly mul(const Poly& other) const {
            Poly res;
            for (auto &a : terms) {
                for (auto &b : other.terms) {
                    long long coeff = a.second * b.second;
                    vector<string> vars = a.first;
                    vars.insert(vars.end(), b.first.begin(), b.first.end());
                    sort(vars.begin(), vars.end());
                    auto it = res.terms.find(vars);
                    if (it != res.terms.end()) {
                        it->second += coeff;
                        if (it->second == 0) res.terms.erase(it);
                    } else {
                        if (coeff != 0) res.terms[vars] = coeff;
                    }
                }
            }
            return res;
        }
        
        Poly evaluate(const unordered_map<string,long long>& ev) const {
            Poly res;
            for (auto &kv : terms) {
                long long coeff = kv.second;
                vector<string> vars;
                for (const string& v : kv.first) {
                    auto it = ev.find(v);
                    if (it != ev.end()) {
                        coeff *= it->second;
                    } else {
                        vars.push_back(v);
                    }
                }
                sort(vars.begin(), vars.end());
                if (coeff == 0) continue;
                auto it = res.terms.find(vars);
                if (it != res.terms.end()) {
                    it->second += coeff;
                    if (it->second == 0) res.terms.erase(it);
                } else {
                    res.terms[vars] = coeff;
                }
            }
            return res;
        }
    };
    
    vector<string> basicCalculatorIV(string expression, vector<string>& evalvars, vector<int>& evalints) {
        // tokenize by space
        vector<string> tokens;
        string cur;
        for (char c : expression) {
            if (c == ' ') continue;
            if (c=='('||c==')'||c=='+'||c=='-'||c=='*') {
                if (!cur.empty()) { tokens.push_back(cur); cur.clear(); }
                tokens.emplace_back(1,c);
            } else {
                cur.push_back(c);
            }
        }
        if (!cur.empty()) tokens.push_back(cur);
        
        int pos = 0;
        function<Poly()> parseExpression, parseTerm, parseFactor;
        
        parseExpression = [&]() -> Poly {
            Poly left = parseTerm();
            while (pos < (int)tokens.size() && (tokens[pos] == "+" || tokens[pos] == "-")) {
                string op = tokens[pos++];
                Poly right = parseTerm();
                if (op == "+") left = left.add(right, 1);
                else left = left.add(right, -1);
            }
            return left;
        };
        
        parseTerm = [&]() -> Poly {
            Poly left = parseFactor();
            while (pos < (int)tokens.size() && tokens[pos] == "*") {
                ++pos;
                Poly right = parseFactor();
                left = left.mul(right);
            }
            return left;
        };
        
        parseFactor = [&]() -> Poly {
            if (tokens[pos] == "(") {
                ++pos; // '('
                Poly inside = parseExpression();
                ++pos; // ')'
                return inside;
            } else {
                string tok = tokens[pos++];
                if (isdigit(tok[0])) {
                    long long val = stoll(tok);
                    return Poly::fromNumber(val);
                } else {
                    return Poly::fromVariable(tok);
                }
            }
        };
        
        Poly poly = parseExpression();
        unordered_map<string,long long> ev;
        for (int i = 0; i < (int)evalvars.size(); ++i) ev[evalvars[i]] = evalints[i];
        poly = poly.evaluate(ev);
        
        vector<pair<vector<string>, long long>> terms(poly.terms.begin(), poly.terms.end());
        sort(terms.begin(), terms.end(),
            [](const auto& a, const auto& b){
                if (a.first.size() != b.first.size())
                    return a.first.size() > b.first.size();
                return a.first < b.first;
            });
        
        vector<string> ans;
        for (auto &kv : terms) {
            string s = to_string(kv.second);
            for (const string& v : kv.first) {
                s.push_back('*');
                s += v;
            }
            ans.push_back(s);
        }
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<String> basicCalculatorIV(String expression, String[] evalvars, int[] evalints) {
        Map<String, Integer> evalMap = new HashMap<>();
        for (int i = 0; i < evalvars.length; i++) {
            evalMap.put(evalvars[i], evalints[i]);
        }
        String[] tokens = expression.split(" ");
        Parser parser = new Parser(tokens, evalMap);
        Poly result = parser.parseExpression();
        List<Map.Entry<List<String>, Integer>> entries = new ArrayList<>(result.terms.entrySet());
        entries.removeIf(e -> e.getValue() == 0);
        Collections.sort(entries, (e1, e2) -> {
            int d1 = e1.getKey().size();
            int d2 = e2.getKey().size();
            if (d1 != d2) return Integer.compare(d2, d1); // descending degree
            List<String> k1 = e1.getKey();
            List<String> k2 = e2.getKey();
            for (int i = 0; i < k1.size(); i++) {
                int cmp = k1.get(i).compareTo(k2.get(i));
                if (cmp != 0) return cmp;
            }
            return 0;
        });
        List<String> ans = new ArrayList<>();
        for (Map.Entry<List<String>, Integer> e : entries) {
            int coeff = e.getValue();
            List<String> vars = e.getKey();
            StringBuilder sb = new StringBuilder();
            sb.append(coeff);
            if (!vars.isEmpty()) {
                sb.append('*');
                sb.append(String.join("*", vars));
            }
            ans.add(sb.toString());
        }
        return ans;
    }

    // Parser for the expression
    private static class Parser {
        String[] tokens;
        int pos = 0;
        Map<String, Integer> evalMap;

        Parser(String[] tokens, Map<String, Integer> evalMap) {
            this.tokens = tokens;
            this.evalMap = evalMap;
        }

        Poly parseExpression() {
            Poly left = parseTerm();
            while (pos < tokens.length && (tokens[pos].equals("+") || tokens[pos].equals("-"))) {
                String op = tokens[pos++];
                Poly right = parseTerm();
                if (op.equals("+")) {
                    left = add(left, right);
                } else {
                    left = sub(left, right);
                }
            }
            return left;
        }

        Poly parseTerm() {
            Poly left = parseFactor();
            while (pos < tokens.length && tokens[pos].equals("*")) {
                pos++; // skip '*'
                Poly right = parseFactor();
                left = mul(left, right);
            }
            return left;
        }

        Poly parseFactor() {
            String token = tokens[pos++];
            if (token.equals("(")) {
                Poly inside = parseExpression();
                // next token should be ')'
                pos++; // skip ')'
                return inside;
            } else if (Character.isDigit(token.charAt(0))) {
                int val = Integer.parseInt(token);
                return constantPoly(val);
            } else { // variable
                if (evalMap.containsKey(token)) {
                    int val = evalMap.get(token);
                    return constantPoly(val);
                } else {
                    return variablePoly(token);
                }
            }
        }

        private Poly constantPoly(int val) {
            Poly p = new Poly();
            if (val != 0) {
                p.terms.put(new ArrayList<>(), val);
            }
            return p;
        }

        private Poly variablePoly(String var) {
            Poly p = new Poly();
            List<String> list = new ArrayList<>();
            list.add(var);
            p.terms.put(list, 1);
            return p;
        }

        private Poly add(Poly a, Poly b) {
            Poly res = new Poly();
            for (Map.Entry<List<String>, Integer> e : a.terms.entrySet()) {
                res.terms.put(new ArrayList<>(e.getKey()), e.getValue());
            }
            for (Map.Entry<List<String>, Integer> e : b.terms.entrySet()) {
                List<String> key = new ArrayList<>(e.getKey());
                int coeff = e.getValue();
                res.terms.merge(key, coeff, Integer::sum);
                if (res.terms.get(key) == 0) {
                    res.terms.remove(key);
                }
            }
            return res;
        }

        private Poly sub(Poly a, Poly b) {
            Poly negB = new Poly();
            for (Map.Entry<List<String>, Integer> e : b.terms.entrySet()) {
                List<String> key = new ArrayList<>(e.getKey());
                negB.terms.put(key, -e.getValue());
            }
            return add(a, negB);
        }

        private Poly mul(Poly a, Poly b) {
            Poly res = new Poly();
            for (Map.Entry<List<String>, Integer> e1 : a.terms.entrySet()) {
                for (Map.Entry<List<String>, Integer> e2 : b.terms.entrySet()) {
                    int coeff = e1.getValue() * e2.getValue();
                    List<String> vars = new ArrayList<>();
                    vars.addAll(e1.getKey());
                    vars.addAll(e2.getKey());
                    Collections.sort(vars);
                    res.terms.merge(vars, coeff, Integer::sum);
                    if (res.terms.get(vars) == 0) {
                        res.terms.remove(vars);
                    }
                }
            }
            return res;
        }
    }

    // Polynomial representation
    private static class Poly {
        Map<List<String>, Integer> terms = new HashMap<>();
    }
}
```

## Python

```python
class Solution(object):
    def basicCalculatorIV(self, expression, evalvars, evalints):
        """
        :type expression: str
        :type evalvars: List[str]
        :type evalints: List[int]
        :rtype: List[str]
        """
        evalmap = dict(zip(evalvars, evalints))
        tokens = expression.split(' ')
        n = len(tokens)
        idx = 0

        def add(p1, p2, sign=1):
            res = p1.copy()
            for k, v in p2.items():
                nv = res.get(k, 0) + sign * v
                if nv:
                    res[k] = nv
                elif k in res:
                    del res[k]
            return res

        def mul(p1, p2):
            res = {}
            for k1, c1 in p1.items():
                for k2, c2 in p2.items():
                    coeff = c1 * c2
                    vars_tuple = tuple(sorted(k1 + k2))
                    nv = res.get(vars_tuple, 0) + coeff
                    if nv:
                        res[vars_tuple] = nv
                    elif vars_tuple in res:
                        del res[vars_tuple]
            return res

        def parseExpression():
            nonlocal idx
            left = parseTerm()
            while idx < n and tokens[idx] in ('+', '-'):
                op = tokens[idx]
                idx += 1
                right = parseTerm()
                if op == '+':
                    left = add(left, right, 1)
                else:
                    left = add(left, right, -1)
            return left

        def parseTerm():
            nonlocal idx
            left = parseFactor()
            while idx < n and tokens[idx] == '*':
                idx += 1
                right = parseFactor()
                left = mul(left, right)
            return left

        def parseFactor():
            nonlocal idx
            token = tokens[idx]
            idx += 1
            if token == '(':
                inner = parseExpression()
                # skip ')'
                idx += 1
                return inner
            elif token.isdigit():
                return {(): int(token)}
            else:  # variable
                if token in evalmap:
                    return {(): evalmap[token]}
                else:
                    return {(token,): 1}

        poly = parseExpression()

        terms = []
        for vars_tuple, coeff in poly.items():
            if coeff == 0:
                continue
            if not vars_tuple:
                term_str = str(coeff)
            else:
                term_str = str(coeff) + '*' + '*'.join(vars_tuple)
            terms.append((vars_tuple, term_str))

        terms.sort(key=lambda x: (-len(x[0]), x[0]))
        return [t[1] for t in terms]
```

## Python3

```python
class Solution:
    def basicCalculatorIV(self, expression: str, evalvars, evalints):
        from collections import defaultdict

        tokens = expression.split()
        n = len(tokens)
        i = 0
        evalmap = dict(zip(evalvars, evalints))

        def normalize(poly):
            # remove zero coeffs
            return {k: v for k, v in poly.items() if v != 0}

        def add(p1, p2):
            res = defaultdict(int, p1)
            for k, v in p2.items():
                res[k] += v
            return normalize(res)

        def sub(p1, p2):
            res = defaultdict(int, p1)
            for k, v in p2.items():
                res[k] -= v
            return normalize(res)

        def mul(p1, p2):
            res = defaultdict(int)
            for k1, c1 in p1.items():
                for k2, c2 in p2.items():
                    coeff = c1 * c2
                    vars_combined = tuple(sorted(k1 + k2))
                    res[vars_combined] += coeff
            return normalize(res)

        def make(token):
            # token is number or variable
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                val = int(token)
                return {(): val}
            else:
                if token in evalmap:
                    return {(): evalmap[token]}
                else:
                    return {(token,): 1}

        def parseFactor():
            nonlocal i
            tok = tokens[i]
            if tok == '(':
                i += 1
                poly = parseExpression()
                # expect ')'
                i += 1  # skip ')'
                return poly
            else:
                i += 1
                return make(tok)

        def parseTerm():
            nonlocal i
            left = parseFactor()
            while i < n and tokens[i] == '*':
                i += 1
                right = parseFactor()
                left = mul(left, right)
            return left

        def parseExpression():
            nonlocal i
            left = parseTerm()
            while i < n and (tokens[i] == '+' or tokens[i] == '-'):
                op = tokens[i]
                i += 1
                right = parseTerm()
                if op == '+':
                    left = add(left, right)
                else:
                    left = sub(left, right)
            return left

        poly = parseExpression()

        # sort terms
        def term_key(item):
            vars_tuple, coeff = item
            return (-len(vars_tuple), vars_tuple)

        sorted_items = sorted(poly.items(), key=term_key)
        result = []
        for vars_tuple, coeff in sorted_items:
            if not vars_tuple:
                result.append(str(coeff))
            else:
                term = str(coeff) + '*' + '*'.join(vars_tuple)
                result.append(term)
        return result
```

## C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define TABLE_SIZE 2003

typedef struct Node {
    char *key;          // monomial key, empty string for constant
    int coeff;
    struct Node *next;
} Node;

typedef struct Poly {
    Node **table;
} Poly;

/* hash function (djb2) */
static unsigned long hash_str(const char *s) {
    unsigned long h = 5381;
    while (*s)
        h = ((h << 5) + h) + (unsigned char)(*s++);
    return h;
}

/* create empty polynomial */
static Poly *poly_new() {
    Poly *p = (Poly *)malloc(sizeof(Poly));
    p->table = (Node **)calloc(TABLE_SIZE, sizeof(Node *));
    return p;
}

/* free polynomial */
static void poly_free(Poly *p) {
    if (!p) return;
    for (int i = 0; i < TABLE_SIZE; ++i) {
        Node *cur = p->table[i];
        while (cur) {
            Node *tmp = cur;
            cur = cur->next;
            free(tmp->key);
            free(tmp);
        }
    }
    free(p->table);
    free(p);
}

/* add term with delta coefficient */
static void poly_add_term(Poly *p, const char *key, int delta) {
    if (delta == 0) return;
    unsigned long h = hash_str(key);
    int idx = h % TABLE_SIZE;
    Node *cur = p->table[idx];
    while (cur) {
        if (strcmp(cur->key, key) == 0) {
            cur->coeff += delta;
            if (cur->coeff == 0) {
                /* remove node */
                Node **pp = &p->table[idx];
                while (*pp && *pp != cur) pp = &((*pp)->next);
                if (*pp) {
                    *pp = cur->next;
                    free(cur->key);
                    free(cur);
                }
            }
            return;
        }
        cur = cur->next;
    }
    /* not found, create */
    Node *n = (Node *)malloc(sizeof(Node));
    n->key = strdup(key);
    n->coeff = delta;
    n->next = p->table[idx];
    p->table[idx] = n;
}

/* add/subtract two polynomials: sign=+1 for addition, -1 for subtraction */
static Poly *poly_add(const Poly *a, const Poly *b, int sign) {
    Poly *res = poly_new();
    for (int i = 0; i < TABLE_SIZE; ++i) {
        Node *cur = a->table[i];
        while (cur) {
            poly_add_term(res, cur->key, cur->coeff);
            cur = cur->next;
        }
    }
    for (int i = 0; i < TABLE_SIZE; ++i) {
        Node *cur = b->table[i];
        while (cur) {
            poly_add_term(res, cur->key, sign * cur->coeff);
            cur = cur->next;
        }
    }
    return res;
}

/* split key into array of variable strings */
static char **split_key(const char *key, int *cnt) {
    if (!key || key[0] == '\0') {
        *cnt = 0;
        return NULL;
    }
    int c = 1;
    for (const char *p = key; *p; ++p)
        if (*p == '*') ++c;
    char **arr = (char **)malloc(c * sizeof(char *));
    char *dup = strdup(key);
    int idx = 0;
    char *tok = strtok(dup, "*");
    while (tok) {
        arr[idx++] = strdup(tok);
        tok = strtok(NULL, "*");
    }
    free(dup);
    *cnt = c;
    return arr;
}

/* merge two sorted variable arrays into a new key */
static char *merge_keys(const char *k1, const char *k2) {
    int cnt1, cnt2;
    char **a1 = split_key(k1, &cnt1);
    char **a2 = split_key(k2, &cnt2);
    int total = cnt1 + cnt2;
    if (total == 0) {
        free(a1);
        free(a2);
        return strdup("");
    }
    char **merged = (char **)malloc(total * sizeof(char *));
    int i = 0, j = 0, m = 0;
    while (i < cnt1 && j < cnt2) {
        if (strcmp(a1[i], a2[j]) <= 0)
            merged[m++] = a1[i++];
        else
            merged[m++] = a2[j++];
    }
    while (i < cnt1) merged[m++] = a1[i++];
    while (j < cnt2) merged[m++] = a2[j++];
    /* build string */
    int len = 0;
    for (int k = 0; k < total; ++k) len += strlen(merged[k]);
    len += total - 1; // '*'
    char *res = (char *)malloc(len + 1);
    char *p = res;
    for (int k = 0; k < total; ++k) {
        int l = strlen(merged[k]);
        memcpy(p, merged[k], l);
        p += l;
        if (k != total - 1) *p++ = '*';
    }
    *p = '\0';
    /* free */
    for (int k = 0; k < cnt1; ++k) free(a1[k]);
    for (int k = 0; k < cnt2; ++k) free(a2[k]);
    free(a1);
    free(a2);
    free(merged);
    return res;
}

/* multiplication */
static Poly *poly_mul(const Poly *a, const Poly *b) {
    Poly *res = poly_new();
    for (int i = 0; i < TABLE_SIZE; ++i) {
        Node *curA = a->table[i];
        while (curA) {
            for (int j = 0; j < TABLE_SIZE; ++j) {
                Node *curB = b->table[j];
                while (curB) {
                    long long coeff = (long long)curA->coeff * curB->coeff;
                    char *newKey = merge_keys(curA->key, curB->key);
                    poly_add_term(res, newKey, (int)coeff);
                    free(newKey);
                    curB = curB->next;
                }
            }
            curA = curA->next;
        }
    }
    return res;
}

/* token handling */
static char **gTokens;
static int gTokenCount;
static int gPos;

/* forward declarations */
static Poly *parseExpression(void);
static Poly *parseTerm(void);
static Poly *parseFactor(void);

/* parsing functions */
static Poly *parseExpression(void) {
    Poly *left = parseTerm();
    while (gPos < gTokenCount &&
           (strcmp(gTokens[gPos], "+") == 0 || strcmp(gTokens[gPos], "-") == 0)) {
        char op[2];
        strcpy(op, gTokens[gPos++]);
        Poly *right = parseTerm();
        Poly *tmp;
        if (op[0] == '+')
            tmp = poly_add(left, right, 1);
        else
            tmp = poly_add(left, right, -1);
        poly_free(left);
        poly_free(right);
        left = tmp;
    }
    return left;
}

static Poly *parseTerm(void) {
    Poly *left = parseFactor();
    while (gPos < gTokenCount && strcmp(gTokens[gPos], "*") == 0) {
        gPos++; // skip '*'
        Poly *right = parseFactor();
        Poly *tmp = poly_mul(left, right);
        poly_free(left);
        poly_free(right);
        left = tmp;
    }
    return left;
}

static int isNumber(const char *s) {
    if (!s || !*s) return 0;
    while (*s) {
        if (!isdigit(*s)) return 0;
        ++s;
    }
    return 1;
}

static Poly *parseFactor(void) {
    char *tok = gTokens[gPos++];
    if (strcmp(tok, "(") == 0) {
        Poly *inner = parseExpression();
        /* consume ')' */
        if (gPos < gTokenCount && strcmp(gTokens[gPos], ")") == 0)
            gPos++;
        return inner;
    } else if (isNumber(tok)) {
        int val = atoi(tok);
        Poly *p = poly_new();
        poly_add_term(p, "", val);
        return p;
    } else { /* variable */
        Poly *p = poly_new();
        poly_add_term(p, tok, 1);
        return p;
    }
}

/* evaluation map */
typedef struct EvalNode {
    char *var;
    int val;
    struct EvalNode *next;
} EvalNode;

static EvalNode *evalTable[TABLE_SIZE];

static void eval_insert(const char *var, int val) {
    unsigned long h = hash_str(var);
    int idx = h % TABLE_SIZE;
    EvalNode *n = (EvalNode *)malloc(sizeof(EvalNode));
    n->var = strdup(var);
    n->val = val;
    n->next = evalTable[idx];
    evalTable[idx] = n;
}

static int eval_lookup(const char *var, int *out) {
    unsigned long h = hash_str(var);
    int idx = h % TABLE_SIZE;
    EvalNode *cur = evalTable[idx];
    while (cur) {
        if (strcmp(cur->var, var) == 0) {
            *out = cur->val;
            return 1;
        }
        cur = cur->next;
    }
    return 0;
}

static void eval_free_all(void) {
    for (int i = 0; i < TABLE_SIZE; ++i) {
        EvalNode *cur = evalTable[i];
        while (cur) {
            EvalNode *tmp = cur;
            cur = cur->next;
            free(tmp->var);
            free(tmp);
        }
        evalTable[i] = NULL;
    }
}

/* evaluate polynomial with given variable values */
static Poly *poly_evaluate(const Poly *p) {
    Poly *res = poly_new();
    for (int i = 0; i < TABLE_SIZE; ++i) {
        Node *cur = p->table[i];
        while (cur) {
            int cnt;
            char **vars = split_key(cur->key, &cnt);
            long long coeff = cur->coeff;
            /* build remaining vars */
            char **remain = (char **)malloc(cnt * sizeof(char *));
            int rcnt = 0;
            for (int k = 0; k < cnt; ++k) {
                int val;
                if (eval_lookup(vars[k], &val)) {
                    coeff *= val;
                } else {
                    remain[rcnt++] = vars[k];
                }
            }
            /* construct new key */
            char *newKey;
            if (rcnt == 0) {
                newKey = strdup("");
            } else {
                int len = 0;
                for (int k = 0; k < rcnt; ++k) len += strlen(remain[k]);
                len += rcnt - 1;
                newKey = (char *)malloc(len + 1);
                char *pch = newKey;
                for (int k = 0; k < rcnt; ++k) {
                    int l = strlen(remain[k]);
                    memcpy(pch, remain[k], l);
                    pch += l;
                    if (k != rcnt - 1) *pch++ = '*';
                }
                *pch = '\0';
            }
            poly_add_term(res, newKey, (int)coeff);
            free(newKey);
            /* free split parts */
            for (int k = 0; k < cnt; ++k) free(vars[k]);
            free(vars);
            free(remain);
            cur = cur->next;
        }
    }
    return res;
}

/* term info for sorting */
typedef struct {
    char *key;
    int coeff;
    int degree;
} TermInfo;

/* comparator */
static int term_cmp(const void *a, const void *b) {
    const TermInfo *ta = (const TermInfo *)a;
    const TermInfo *tb = (const TermInfo *)b;
    if (ta->degree != tb->degree)
        return tb->degree - ta->degree; /* descending degree */
    return strcmp(ta->key, tb->key);
}

/* main function */
char** basicCalculatorIV(char* expression, char** evalvars, int evalvarsSize,
                         int* evalints, int evalintsSize, int* returnSize) {
    /* tokenization */
    char *exprCopy = strdup(expression);
    char **tmpTokens = (char **)malloc(500 * sizeof(char *));
    int cnt = 0;
    char *tok = strtok(exprCopy, " ");
    while (tok) {
        tmpTokens[cnt++] = strdup(tok);
        tok = strtok(NULL, " ");
    }
    free(exprCopy);
    gTokens = tmpTokens;
    gTokenCount = cnt;
    gPos = 0;

    /* parse expression */
    Poly *poly = parseExpression();

    /* build evaluation map */
    for (int i = 0; i < evalvarsSize; ++i) {
        eval_insert(evalvars[i], evalints[i]);
    }

    /* evaluate */
    Poly *evaled = poly_evaluate(poly);
    poly_free(poly);

    /* collect terms */
    int termCnt = 0;
    for (int i = 0; i < TABLE_SIZE; ++i) {
        Node *cur = evaled->table[i];
        while (cur) {
            ++termCnt;
            cur = cur->next;
        }
    }

    TermInfo *terms = (TermInfo *)malloc(termCnt * sizeof(TermInfo));
    int idx = 0;
    for (int i = 0; i < TABLE_SIZE; ++i) {
        Node *cur = evaled->table[i];
        while (cur) {
            terms[idx].coeff = cur->coeff;
            terms[idx].key = strdup(cur->key);
            if (cur->key[0] == '\0')
                terms[idx].degree = 0;
            else
                terms[idx].degree = 1 + (int)strchr(cur->key, '*') ? (int)(strlen(cur->key) - strlen(strrchr(cur->key, '*'))) : 0; /* placeholder */
            /* proper degree count */
            int deg = 0;
            if (cur->key[0] != '\0') {
                for (char *p = cur->key; *p; ++p)
                    if (*p == '*') ++deg;
                ++deg; // number of variables
            }
            terms[idx].degree = deg;
            ++idx;
            cur = cur->next;
        }
    }

    /* sort */
    qsort(terms, termCnt, sizeof(TermInfo), term_cmp);

    /* build result strings */
    char **result = (char **)malloc(termCnt * sizeof(char *));
    int outIdx = 0;
    for (int i = 0; i < termCnt; ++i) {
        if (terms[i].coeff == 0) {
            free(terms[i].key);
            continue;
        }
        char *s;
        if (terms[i].key[0] == '\0') {
            int len = snprintf(NULL, 0, "%d", terms[i].coeff);
            s = (char *)malloc(len + 1);
            sprintf(s, "%d", terms[i].coeff);
        } else {
            int len = snprintf(NULL, 0, "%d*%s", terms[i].coeff, terms[i].key);
            s = (char *)malloc(len + 1);
            sprintf(s, "%d*%s", terms[i].coeff, terms[i].key);
        }
        result[outIdx++] = s;
        free(terms[i].key);
    }

    /* cleanup */
    free(terms);
    poly_free(evaled);
    eval_free_all();
    for (int i = 0; i < gTokenCount; ++i) free(gTokens[i]);
    free(gTokens);

    *returnSize = outIdx;
    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<string> BasicCalculatorIV(string expression, string[] evalvars, int[] evalints) {
        var tokens = expression.Split(' ', StringSplitOptions.RemoveEmptyEntries).ToList();
        int pos = 0;
        Poly ParseExpression() {
            Poly left = ParseTerm();
            while (pos < tokens.Count && (tokens[pos] == "+" || tokens[pos] == "-")) {
                string op = tokens[pos++];
                Poly right = ParseTerm();
                if (op == "+") left = Add(left, right);
                else left = Sub(left, right);
            }
            return left;
        }
        Poly ParseTerm() {
            Poly left = ParseFactor();
            while (pos < tokens.Count && tokens[pos] == "*") {
                pos++;
                Poly right = ParseFactor();
                left = Mul(left, right);
            }
            return left;
        }
        Poly ParseFactor() {
            string tk = tokens[pos++];
            if (tk == "(") {
                Poly inside = ParseExpression();
                pos++; // skip ')'
                return inside;
            }
            if (char.IsDigit(tk[0])) {
                long val = long.Parse(tk);
                var p = new Poly();
                p.terms[""] = val;
                return p;
            } else { // variable
                var p = new Poly();
                p.terms[tk] = 1;
                return p;
            }
        }

        Poly Add(Poly a, Poly b) {
            var res = new Poly();
            foreach (var kv in a.terms) {
                res.terms[kv.Key] = kv.Value;
            }
            foreach (var kv in b.terms) {
                if (res.terms.ContainsKey(kv.Key))
                    res.terms[kv.Key] += kv.Value;
                else
                    res.terms[kv.Key] = kv.Value;
            }
            return res;
        }

        Poly Sub(Poly a, Poly b) {
            var res = new Poly();
            foreach (var kv in a.terms) {
                res.terms[kv.Key] = kv.Value;
            }
            foreach (var kv in b.terms) {
                if (res.terms.ContainsKey(kv.Key))
                    res.terms[kv.Key] -= kv.Value;
                else
                    res.terms[kv.Key] = -kv.Value;
            }
            return res;
        }

        Poly Mul(Poly a, Poly b) {
            var res = new Poly();
            foreach (var kv1 in a.terms) {
                foreach (var kv2 in b.terms) {
                    string key = CombineKeys(kv1.Key, kv2.Key);
                    long coeff = kv1.Value * kv2.Value;
                    if (res.terms.ContainsKey(key))
                        res.terms[key] += coeff;
                    else
                        res.terms[key] = coeff;
                }
            }
            return res;
        }

        string CombineKeys(string k1, string k2) {
            if (string.IsNullOrEmpty(k1)) return k2;
            if (string.IsNullOrEmpty(k2)) return k1;
            var list = new List<string>();
            list.AddRange(k1.Split('*'));
            list.AddRange(k2.Split('*'));
            list.Sort(StringComparer.Ordinal);
            return string.Join("*", list);
        }

        // Parse the expression
        Poly poly = ParseExpression();

        // Build evaluation map
        var evalMap = new Dictionary<string, long>();
        for (int i = 0; i < evalvars.Length; i++) {
            evalMap[evalvars[i]] = evalints[i];
        }

        // Evaluate known variables
        var evaluated = new Poly();
        foreach (var kv in poly.terms) {
            long coeff = kv.Value;
            List<string> vars = new List<string>();
            if (!string.IsNullOrEmpty(kv.Key))
                vars.AddRange(kv.Key.Split('*'));
            List<string> remaining = new List<string>();
            foreach (var v in vars) {
                if (evalMap.TryGetValue(v, out long val)) {
                    coeff *= val;
                } else {
                    remaining.Add(v);
                }
            }
            remaining.Sort(StringComparer.Ordinal);
            string newKey = remaining.Count == 0 ? "" : string.Join("*", remaining);
            if (evaluated.terms.ContainsKey(newKey))
                evaluated.terms[newKey] += coeff;
            else
                evaluated.terms[newKey] = coeff;
        }

        // Prepare output
        var items = new List<(string key, long coeff)>();
        foreach (var kv in evaluated.terms) {
            if (kv.Value != 0) {
                items.Add((kv.Key, kv.Value));
            }
        }
        var result = items
            .Select(p => (key: p.key,
                          coeff: p.coeff,
                          degree: string.IsNullOrEmpty(p.key) ? 0 : p.key.Split('*').Length))
            .OrderByDescending(p => p.degree)
            .ThenBy(p => p.key, StringComparer.Ordinal)
            .Select(p => {
                if (string.IsNullOrEmpty(p.key))
                    return p.coeff.ToString();
                else
                    return $"{p.coeff}*{p.key}";
            })
            .ToList();

        return result;
    }

    private class Poly {
        public Dictionary<string, long> terms = new Dictionary<string, long>();
    }
}
```

## Javascript

```javascript
/**
 * @param {string} expression
 * @param {string[]} evalvars
 * @param {number[]} evalints
 * @return {string[]}
 */
var basicCalculatorIV = function(expression, evalvars, evalints) {
    const evalMap = {};
    for (let i = 0; i < evalvars.length; ++i) {
        evalMap[evalvars[i]] = evalints[i];
    }

    const tokens = expression.split(' ');
    let idx = 0;

    function addPoly(p1, p2) {
        const res = new Map(p1);
        for (const [k, v] of p2) {
            const sum = (res.get(k) || 0) + v;
            if (sum === 0) res.delete(k);
            else res.set(k, sum);
        }
        return res;
    }

    function subPoly(p1, p2) {
        const neg = new Map();
        for (const [k, v] of p2) {
            neg.set(k, -v);
        }
        return addPoly(p1, neg);
    }

    function mulPoly(p1, p2) {
        const res = new Map();
        for (const [k1, c1] of p1) {
            const vars1 = k1 ? k1.split('*') : [];
            for (const [k2, c2] of p2) {
                const vars2 = k2 ? k2.split('*') : [];
                const coeff = c1 * c2;
                const combined = [...vars1, ...vars2];
                combined.sort();
                const key = combined.join('*');
                const sum = (res.get(key) || 0) + coeff;
                if (sum === 0) res.delete(key);
                else res.set(key, sum);
            }
        }
        return res;
    }

    function parseFactor() {
        const token = tokens[idx++];
        if (token === '(') {
            const inside = parseExpression();
            idx++; // skip ')'
            return inside;
        } else if (/[0-9]/.test(token[0])) { // number
            const map = new Map();
            map.set('', Number(token));
            return map;
        } else { // variable
            if (evalMap.hasOwnProperty(token)) {
                const map = new Map();
                map.set('', evalMap[token]);
                return map;
            } else {
                const map = new Map();
                map.set(token, 1);
                return map;
            }
        }
    }

    function parseTerm() {
        let left = parseFactor();
        while (idx < tokens.length && tokens[idx] === '*') {
            idx++; // skip '*'
            const right = parseFactor();
            left = mulPoly(left, right);
        }
        return left;
    }

    function parseExpression() {
        let left = parseTerm();
        while (idx < tokens.length && (tokens[idx] === '+' || tokens[idx] === '-')) {
            const op = tokens[idx++];
            const right = parseTerm();
            if (op === '+') left = addPoly(left, right);
            else left = subPoly(left, right);
        }
        return left;
    }

    const poly = parseExpression();

    // Convert to sorted list
    const entries = [];
    for (const [k, v] of poly) {
        if (v !== 0) entries.push([k, v]);
    }

    entries.sort((a, b) => {
        const degA = a[0] ? a[0].split('*').length : 0;
        const degB = b[0] ? b[0].split('*').length : 0;
        if (degA !== degB) return degB - degA; // higher degree first
        if (a[0] < b[0]) return -1;
        if (a[0] > b[0]) return 1;
        return 0;
    });

    const result = [];
    for (const [k, v] of entries) {
        if (k === '') result.push(String(v));
        else result.push(`${v}*${k}`);
    }
    if (result.length === 0) result.push('0');
    return result;
};
```

## Typescript

```typescript
function basicCalculatorIV(expression: string, evalvars: string[], evalints: number[]): string[] {
    const evalMap: Record<string, number> = {};
    for (let i = 0; i < evalvars.length; ++i) {
        evalMap[evalvars[i]] = evalints[i];
    }

    type Poly = Map<string, number>;

    function add(p1: Poly, p2: Poly, sign: number = 1): Poly {
        const res = new Map<string, number>(p1);
        for (const [k, v] of p2.entries()) {
            const coeff = sign * v;
            const cur = res.get(k) ?? 0;
            const sum = cur + coeff;
            if (sum === 0) {
                res.delete(k);
            } else {
                res.set(k, sum);
            }
        }
        return res;
    }

    function mul(p1: Poly, p2: Poly): Poly {
        const res = new Map<string, number>();
        for (const [k1, v1] of p1.entries()) {
            const vars1 = k1 ? k1.split('*') : [];
            for (const [k2, v2] of p2.entries()) {
                const vars2 = k2 ? k2.split('*') : [];
                const combined = [...vars1, ...vars2].sort();
                const key = combined.join('*');
                const coeff = v1 * v2;
                const cur = res.get(key) ?? 0;
                const sum = cur + coeff;
                if (sum === 0) {
                    res.delete(key);
                } else {
                    res.set(key, sum);
                }
            }
        }
        return res;
    }

    function make(token: string): Poly {
        const poly = new Map<string, number>();
        if (/^\d+$/.test(token)) {
            poly.set('', parseInt(token));
        } else if (evalMap.hasOwnProperty(token)) {
            poly.set('', evalMap[token]);
        } else {
            poly.set(token, 1);
        }
        return poly;
    }

    const tokens = expression.split(' ');
    let pos = 0;

    function peek(): string {
        return tokens[pos];
    }

    function next(): string {
        return tokens[pos++];
    }

    function parseFactor(): Poly {
        if (peek() === '(') {
            next(); // '('
            const expr = parseExpression();
            next(); // ')'
            return expr;
        } else {
            const tok = next();
            return make(tok);
        }
    }

    function parseTerm(): Poly {
        let left = parseFactor();
        while (pos < tokens.length && peek() === '*') {
            next(); // '*'
            const right = parseFactor();
            left = mul(left, right);
        }
        return left;
    }

    function parseExpression(): Poly {
        let left = parseTerm();
        while (pos < tokens.length && (peek() === '+' || peek() === '-')) {
            const op = next();
            const right = parseTerm();
            if (op === '+') {
                left = add(left, right, 1);
            } else {
                left = add(left, right, -1);
            }
        }
        return left;
    }

    const poly = parseExpression();

    // Convert to sorted list
    interface Term {
        vars: string[];
        coeff: number;
    }
    const terms: Term[] = [];
    for (const [k, v] of poly.entries()) {
        if (v === 0) continue;
        const vars = k ? k.split('*') : [];
        terms.push({ vars, coeff: v });
    }

    terms.sort((a, b) => {
        if (a.vars.length !== b.vars.length) {
            return b.vars.length - a.vars.length; // higher degree first
        }
        for (let i = 0; i < a.vars.length; ++i) {
            if (a.vars[i] !== b.vars[i]) {
                return a.vars[i] < b.vars[i] ? -1 : 1;
            }
        }
        return 0;
    });

    const result: string[] = [];
    for (const t of terms) {
        if (t.vars.length === 0) {
            result.push(t.coeff.toString());
        } else {
            result.push(`${t.coeff}*${t.vars.join('*')}`);
        }
    }

    return result;
}
```

## Php

```php
<?php
function polyAdd(array $p1, array $p2): array {
    foreach ($p2 as $k => $v) {
        if (isset($p1[$k])) {
            $p1[$k] += $v;
        } else {
            $p1[$k] = $v;
        }
    }
    return $p1;
}
function polySub(array $p1, array $p2): array {
    foreach ($p2 as $k => $v) {
        if (isset($p1[$k])) {
            $p1[$k] -= $v;
        } else {
            $p1[$k] = -$v;
        }
    }
    return $p1;
}
function polyMul(array $p1, array $p2): array {
    $res = [];
    foreach ($p1 as $k1 => $c1) {
        $vars1 = $k1 === '' ? [] : explode('*', $k1);
        foreach ($p2 as $k2 => $c2) {
            $vars2 = $k2 === '' ? [] : explode('*', $k2);
            $merged = array_merge($vars1, $vars2);
            sort($merged, SORT_STRING);
            $newKey = implode('*', $merged);
            $coeff = $c1 * $c2;
            if (isset($res[$newKey])) {
                $res[$newKey] += $coeff;
            } else {
                $res[$newKey] = $coeff;
            }
        }
    }
    return $res;
}
class Parser {
    public array $tokens;
    public int $pos = 0;
    public array $evalMap;
    public function __construct(array $tokens, array $evalMap) {
        $this->tokens = $tokens;
        $this->evalMap = $evalMap;
    }
    public function parseExpression(): array {
        $left = $this->parseTerm();
        while ($this->pos < count($this->tokens) && ($this->tokens[$this->pos] === '+' || $this->tokens[$this->pos] === '-')) {
            $op = $this->tokens[$this->pos++];
            $right = $this->parseTerm();
            if ($op === '+') {
                $left = polyAdd($left, $right);
            } else {
                $left = polySub($left, $right);
            }
        }
        return $left;
    }
    public function parseTerm(): array {
        $left = $this->parseFactor();
        while ($this->pos < count($this->tokens) && $this->tokens[$this->pos] === '*') {
            $this->pos++;
            $right = $this->parseFactor();
            $left = polyMul($left, $right);
        }
        return $left;
    }
    public function parseFactor(): array {
        return $this->parsePrimary();
    }
    public function parsePrimary(): array {
        $token = $this->tokens[$this->pos++];
        if ($token === '(') {
            $expr = $this->parseExpression();
            // skip ')'
            $this->pos++;
            return $expr;
        } elseif (ctype_digit($token)) {
            return ['' => intval($token)];
        } else { // variable
            if (isset($this->evalMap[$token])) {
                return ['' => $this->evalMap[$token]];
            } else {
                return [$token => 1];
            }
        }
    }
}
class Solution {
    /**
     * @param String $expression
     * @param String[] $evalvars
     * @param Integer[] $evalints
     * @return String[]
     */
    function basicCalculatorIV($expression, $evalvars, $evalints) {
        $evalMap = [];
        for ($i = 0; $i < count($evalvars); $i++) {
            $evalMap[$evalvars[$i]] = $evalints[$i];
        }
        $tokens = explode(' ', $expression);
        $parser = new Parser($tokens, $evalMap);
        $poly = $parser->parseExpression();
        $terms = [];
        foreach ($poly as $key => $coeff) {
            if ($coeff == 0) continue;
            $degree = $key === '' ? 0 : substr_count($key, '*') + 1;
            $terms[] = ['key' => $key, 'coeff' => $coeff, 'deg' => $degree];
        }
        usort($terms, function ($a, $b) {
            if ($a['deg'] !== $b['deg']) return $b['deg'] - $a['deg'];
            return strcmp($a['key'], $b['key']);
        });
        $result = [];
        foreach ($terms as $t) {
            if ($t['key'] === '') {
                $result[] = strval($t['coeff']);
            } else {
                $result[] = $t['coeff'] . '*' . $t['key'];
            }
        }
        return $result;
    }
}
?>
```

## Swift

```swift
import Foundation

typealias Poly = [String: Int]

func makePoly(_ token: String) -> Poly {
    if let val = Int(token) {
        return ["": val]
    } else {
        return [token: 1]
    }
}

func addPoly(_ a: Poly, _ b: Poly, sign: Int = 1) -> Poly {
    var res = a
    for (k, v) in b {
        res[k, default: 0] += sign * v
    }
    return res
}

func mulPoly(_ a: Poly, _ b: Poly) -> Poly {
    var res: Poly = [:]
    for (k1, v1) in a {
        let vars1 = k1.isEmpty ? [] : k1.split(separator: "*").map(String.init)
        for (k2, v2) in b {
            let vars2 = k2.isEmpty ? [] : k2.split(separator: "*").map(String.init)
            var combined = vars1 + vars2
            combined.sort()
            let key = combined.joined(separator: "*")
            res[key, default: 0] += v1 * v2
        }
    }
    return res
}

func evaluatePoly(_ poly: Poly, _ evalMap: [String: Int]) -> Poly {
    var res: Poly = [:]
    for (key, coeff) in poly where coeff != 0 {
        let vars = key.isEmpty ? [] : key.split(separator: "*").map(String.init)
        var newCoeff = coeff
        var remaining: [String] = []
        for v in vars {
            if let val = evalMap[v] {
                newCoeff *= val
            } else {
                remaining.append(v)
            }
        }
        let newKey = remaining.sorted().joined(separator: "*")
        res[newKey, default: 0] += newCoeff
    }
    return res
}

struct Parser {
    var tokens: [String]
    var idx: Int = 0

    mutating func parseExpression() -> Poly {
        var left = parseTerm()
        while idx < tokens.count && (tokens[idx] == "+" || tokens[idx] == "-") {
            let op = tokens[idx]
            idx += 1
            let right = parseTerm()
            if op == "+" {
                left = addPoly(left, right)
            } else {
                left = addPoly(left, right, sign: -1)
            }
        }
        return left
    }

    mutating func parseTerm() -> Poly {
        var left = parseFactor()
        while idx < tokens.count && tokens[idx] == "*" {
            idx += 1
            let right = parseFactor()
            left = mulPoly(left, right)
        }
        return left
    }

    mutating func parseFactor() -> Poly {
        let token = tokens[idx]
        idx += 1
        if token == "(" {
            let expr = parseExpression()
            // skip ')'
            _ = tokens[idx] // should be ")"
            idx += 1
            return expr
        } else {
            return makePoly(token)
        }
    }
}

class Solution {
    func basicCalculatorIV(_ expression: String, _ evalvars: [String], _ evalints: [Int]) -> [String] {
        let tokens = expression.split(separator: " ").map { String($0) }
        var parser = Parser(tokens: tokens)
        var poly = parser.parseExpression()
        var evalMap: [String: Int] = [:]
        for (i, v) in evalvars.enumerated() {
            evalMap[v] = evalints[i]
        }
        poly = evaluatePoly(poly, evalMap)

        var terms: [(key: String, coeff: Int)] = []
        for (k, v) in poly where v != 0 {
            terms.append((k, v))
        }

        if terms.isEmpty {
            return ["0"]
        }

        terms.sort { a, b in
            let degA = a.key.isEmpty ? 0 : a.key.split(separator: "*").count
            let degB = b.key.isEmpty ? 0 : b.key.split(separator: "*").count
            if degA != degB {
                return degA > degB
            }
            return a.key < b.key
        }

        var result: [String] = []
        for term in terms {
            if term.key.isEmpty {
                result.append("\(term.coeff)")
            } else {
                result.append("\(term.coeff)*\(term.key)")
            }
        }
        return result
    }
}
```

## Kotlin

```kotlin
import java.util.Stack

class Solution {
    fun basicCalculatorIV(expression: String, evalvars: Array<String>, evalints: IntArray): List<String> {
        val evalMap = mutableMapOf<String, Int>()
        for (i in evalvars.indices) {
            evalMap[evalvars[i]] = evalints[i]
        }

        // Polynomial representation
        class Polynomial(val terms: MutableMap<List<String>, Int>) {
            companion object {
                fun fromNumber(value: Int): Polynomial {
                    val m = mutableMapOf<List<String>, Int>()
                    if (value != 0) m[emptyList()] = value
                    return Polynomial(m)
                }

                fun fromVariable(name: String, eval: Map<String, Int>): Polynomial {
                    val v = eval[name]
                    return if (v != null) {
                        fromNumber(v)
                    } else {
                        val m = mutableMapOf<List<String>, Int>()
                        m[listOf(name)] = 1
                        Polynomial(m)
                    }
                }
            }

            fun add(other: Polynomial): Polynomial {
                val res = mutableMapOf<List<String>, Int>()
                for ((k, v) in this.terms) {
                    res[k] = (res[k] ?: 0) + v
                }
                for ((k, v) in other.terms) {
                    res[k] = (res[k] ?: 0) + v
                }
                val it = res.entries.iterator()
                while (it.hasNext()) {
                    if (it.next().value == 0) it.remove()
                }
                return Polynomial(res)
            }

            fun sub(other: Polynomial): Polynomial {
                val res = mutableMapOf<List<String>, Int>()
                for ((k, v) in this.terms) {
                    res[k] = (res[k] ?: 0) + v
                }
                for ((k, v) in other.terms) {
                    res[k] = (res[k] ?: 0) - v
                }
                val it = res.entries.iterator()
                while (it.hasNext()) {
                    if (it.next().value == 0) it.remove()
                }
                return Polynomial(res)
            }

            fun mul(other: Polynomial): Polynomial {
                val res = mutableMapOf<List<String>, Int>()
                for ((k1, v1) in this.terms) {
                    for ((k2, v2) in other.terms) {
                        val coeff = v1 * v2
                        val merged = (k1 + k2).sorted()
                        res[merged] = (res[merged] ?: 0) + coeff
                    }
                }
                val it = res.entries.iterator()
                while (it.hasNext()) {
                    if (it.next().value == 0) it.remove()
                }
                return Polynomial(res)
            }
        }

        fun precedence(op: Char): Int = when (op) {
            '+', '-' -> 1
            '*' -> 2
            else -> 0
        }

        val values = Stack<Polynomial>()
        val ops = Stack<Char>()

        fun applyOp() {
            val op = ops.pop()
            val right = values.pop()
            val left = values.pop()
            val result = when (op) {
                '+' -> left.add(right)
                '-' -> left.sub(right)
                '*' -> left.mul(right)
                else -> Polynomial(mutableMapOf())
            }
            values.push(result)
        }

        val tokens = expression.split(" ")
        for (token in tokens) {
            if (token.isEmpty()) continue
            when {
                token == "(" -> ops.push('(')
                token == ")" -> {
                    while (ops.peek() != '(') applyOp()
                    ops.pop()
                }
                token == "+" || token == "-" || token == "*" -> {
                    val cur = token[0]
                    while (!ops.empty() && ops.peek() != '(' && precedence(ops.peek()) >= precedence(cur)) {
                        applyOp()
                    }
                    ops.push(cur)
                }
                else -> {
                    val poly = if (token[0].isDigit()) {
                        Polynomial.fromNumber(token.toInt())
                    } else {
                        Polynomial.fromVariable(token, evalMap)
                    }
                    values.push(poly)
                }
            }
        }

        while (!ops.empty()) applyOp()

        val finalPoly = if (values.isEmpty()) Polynomial(mutableMapOf()) else values.pop()
        val termList = finalPoly.terms.entries.filter { it.value != 0 }.toMutableList()
        termList.sortWith(Comparator { e1, e2 ->
            val k1 = e1.key
            val k2 = e2.key
            if (k1.size != k2.size) return@Comparator k2.size - k1.size // descending degree
            for (i in k1.indices) {
                val cmp = k1[i].compareTo(k2[i])
                if (cmp != 0) return@Comparator cmp
            }
            0
        })

        val result = mutableListOf<String>()
        for ((k, coeff) in termList) {
            if (k.isEmpty()) {
                result.add(coeff.toString())
            } else {
                result.add("${coeff}*${k.joinToString("*")}")
            }
        }
        return result
    }
}
```

## Dart

```dart
class Solution {
  List<String> basicCalculatorIV(String expression, List<String> evalvars, List<int> evalints) {
    // Build evaluation map
    final Map<String, int> evalMap = {};
    for (int i = 0; i < evalvars.length; ++i) {
      evalMap[evalvars[i]] = evalints[i];
    }

    // Tokenize by space
    final List<String> tokens = expression.split(' ');
    int pos = 0;

    // Polynomial represented as map from variable key to coefficient
    // key: "" for constant, otherwise variables sorted and joined by '*'
    Map<String, int> constPoly(int v) {
      if (v == 0) return {};
      return { "": v };
    }

    Map<String, int> varPoly(String name) {
      return { name: 1 };
    }

    bool isNumber(String s) => RegExp(r'^\d+$').hasMatch(s);

    String mergeVars(String a, String b) {
      if (a.isEmpty) return b;
      if (b.isEmpty) return a;
      final List<String> la = a.split('*');
      final List<String> lb = b.split('*');
      int i = 0, j = 0;
      final List<String> res = [];
      while (i < la.length && j < lb.length) {
        if (la[i].compareTo(lb[j]) <= 0) {
          res.add(la[i]);
          i++;
        } else {
          res.add(lb[j]);
          j++;
        }
      }
      while (i < la.length) { res.add(la[i]); i++; }
      while (j < lb.length) { res.add(lb[j]); j++; }
      return res.join('*');
    }

    Map<String, int> addPoly(Map<String, int> a, Map<String, int> b, [int sign = 1]) {
      final Map<String, int> res = Map.from(a);
      b.forEach((k, v) {
        final int newVal = (res[k] ?? 0) + sign * v;
        if (newVal == 0) {
          res.remove(k);
        } else {
          res[k] = newVal;
        }
      });
      return res;
    }

    Map<String, int> mulPoly(Map<String, int> a, Map<String, int> b) {
      final Map<String, int> res = {};
      a.forEach((ka, va) {
        b.forEach((kb, vb) {
          final String key = mergeVars(ka, kb);
          final int coeff = va * vb;
          final int newVal = (res[key] ?? 0) + coeff;
          if (newVal == 0) {
            res.remove(key);
          } else {
            res[key] = newVal;
          }
        });
      });
      return res;
    }

    Map<String, int> parseExpression() {
      Map<String, int> left = parseTerm();
      while (pos < tokens.length && (tokens[pos] == '+' || tokens[pos] == '-')) {
        final String op = tokens[pos++];
        final Map<String, int> right = parseTerm();
        if (op == '+') {
          left = addPoly(left, right);
        } else {
          left = addPoly(left, right, -1);
        }
      }
      return left;
    }

    Map<String, int> parseTerm() {
      Map<String, int> left = parseFactor();
      while (pos < tokens.length && tokens[pos] == '*') {
        pos++; // skip '*'
        final Map<String, int> right = parseFactor();
        left = mulPoly(left, right);
      }
      return left;
    }

    Map<String, int> parseFactor() {
      final String token = tokens[pos++];
      if (token == '(') {
        final Map<String, int> inside = parseExpression();
        pos++; // skip ')'
        return inside;
      } else if (isNumber(token)) {
        return constPoly(int.parse(token));
      } else { // variable
        if (evalMap.containsKey(token)) {
          return constPoly(evalMap[token]!);
        } else {
          return varPoly(token);
        }
      }
    }

    final Map<String, int> resultPoly = parseExpression();

    // Convert to sorted list of strings
    final List<MapEntry<String, int>> entries = [];
    resultPoly.forEach((k, v) {
      if (v != 0) entries.add(MapEntry(k, v));
    });

    entries.sort((e1, e2) {
      int deg1 = e1.key.isEmpty ? 0 : e1.key.split('*').length;
      int deg2 = e2.key.isEmpty ? 0 : e2.key.split('*').length;
      if (deg1 != deg2) return deg2 - deg1; // descending degree
      return e1.key.compareTo(e2.key);
    });

    final List<String> ans = [];
    for (var entry in entries) {
      String term = '${entry.value}';
      if (entry.key.isNotEmpty) term += '*${entry.key}';
      ans.add(term);
    }
    return ans;
  }
}
```

## Golang

```go
package main

import (
	"strconv"
	"strings"
)

type Poly map[string]int

func addPoly(a, b Poly) Poly {
	res := make(Poly)
	for k, v := range a {
		if v != 0 {
			res[k] = v
		}
	}
	for k, v := range b {
		if v == 0 {
			continue
		}
		res[k] += v
		if res[k] == 0 {
			delete(res, k)
		}
	}
	return res
}

func subPoly(a, b Poly) Poly {
	res := make(Poly)
	for k, v := range a {
		if v != 0 {
			res[k] = v
		}
	}
	for k, v := range b {
		if v == 0 {
			continue
		}
		res[k] -= v
		if res[k] == 0 {
			delete(res, k)
		}
	}
	return res
}

func mergeVars(v1, v2 []string) []string {
	i, j := 0, 0
	merged := make([]string, 0, len(v1)+len(v2))
	for i < len(v1) && j < len(v2) {
		if v1[i] <= v2[j] {
			merged = append(merged, v1[i])
			i++
		} else {
			merged = append(merged, v2[j])
			j++
		}
	}
	for i < len(v1) {
		merged = append(merged, v1[i])
		i++
	}
	for j < len(v2) {
		merged = append(merged, v2[j])
		j++
	}
	return merged
}

func mulPoly(a, b Poly) Poly {
	res := make(Poly)
	for k1, c1 := range a {
		var vars1 []string
		if k1 != "" {
			vars1 = strings.Split(k1, "*")
		}
		for k2, c2 := range b {
			coeff := c1 * c2
			var newKey string
			switch {
			case k1 == "" && k2 == "":
				newKey = ""
			case k1 == "":
				newKey = k2
			case k2 == "":
				newKey = k1
			default:
				vars2 := strings.Split(k2, "*")
				merged := mergeVars(vars1, vars2)
				newKey = strings.Join(merged, "*")
			}
			res[newKey] += coeff
			if res[newKey] == 0 {
				delete(res, newKey)
			}
		}
	}
	return res
}

func precedence(op string) int {
	if op == "*" {
		return 2
	}
	if op == "+" || op == "-" {
		return 1
	}
	return 0
}

func basicCalculatorIV(expression string, evalvars []string, evalints []int) []string {
	evalMap := make(map[string]int)
	for i, v := range evalvars {
		evalMap[v] = evalints[i]
	}

	makePoly := func(token string) Poly {
		p := make(Poly)
		if token[0] >= '0' && token[0] <= '9' {
			val, _ := strconv.Atoi(token)
			if val != 0 {
				p[""] = val
			}
		} else { // variable
			if v, ok := evalMap[token]; ok {
				if v != 0 {
					p[""] = v
				}
			} else {
				p[token] = 1
			}
		}
		return p
	}

	tokens := strings.Split(expression, " ")
	valStack := []Poly{}
	opStack := []string{}

	applyOp := func() {
		if len(opStack) == 0 || len(valStack) < 2 {
			return
		}
		op := opStack[len(opStack)-1]
		opStack = opStack[:len(opStack)-1]

		right := valStack[len(valStack)-1]
		left := valStack[len(valStack)-2]
		valStack = valStack[:len(valStack)-2]

		var res Poly
		if op == "+" {
			res = addPoly(left, right)
		} else if op == "-" {
			res = subPoly(left, right)
		} else { // "*"
			res = mulPoly(left, right)
		}
		valStack = append(valStack, res)
	}

	for _, tok := range tokens {
		if tok == "" {
			continue
		}
		switch tok {
		case "(":
			opStack = append(opStack, tok)
		case ")":
			for len(opStack) > 0 && opStack[len(opStack)-1] != "(" {
				applyOp()
			}
			if len(opStack) > 0 && opStack[len(opStack)-1] == "(" {
				opStack = opStack[:len(opStack)-1]
			}
		case "+", "-", "*":
			for len(opStack) > 0 && opStack[len(opStack)-1] != "(" &&
				precedence(opStack[len(opStack)-1]) >= precedence(tok) {
				applyOp()
			}
			opStack = append(opStack, tok)
		default: // operand
			valStack = append(valStack, makePoly(tok))
		}
	}

	for len(opStack) > 0 {
		applyOp()
	}

	result := valStack[0]

	keys := make([]string, 0, len(result))
	for k := range result {
		if result[k] != 0 {
			keys = append(keys, k)
		}
	}
	if len(keys) == 0 {
		return []string{"0"}
	}
	// custom sort
	sort.Slice(keys, func(i, j int) bool {
		ki, kj := keys[i], keys[j]
		vari := 0
		if ki != "" {
			vari = strings.Count(ki, "*") + 1
		}
		varj := 0
		if kj != "" {
			varj = strings.Count(kj, "*") + 1
		}
		if vari != varj {
			return vari > varj // higher degree first
		}
		return ki < kj
	})

	ans := []string{}
	for _, k := range keys {
		coeff := result[k]
		if coeff == 0 {
			continue
		}
		if k == "" {
			ans = append(ans, strconv.Itoa(coeff))
		} else {
			ans = append(ans, strconv.Itoa(coeff)+"*"+k)
		}
	}
	return ans
}

// needed import for sort
import "sort"
```

## Ruby

```ruby
def basic_calculator_iv(expression, evalvars, evalints)
  eval_map = {}
  evalvars.each_with_index { |v, i| eval_map[v] = evalints[i] }

  class Parser
    def initialize(tokens, eval_map)
      @tokens = tokens
      @i = 0
      @eval_map = eval_map
    end

    def make_token(tok)
      if tok =~ /^\d+$/
        { [] => tok.to_i }
      else
        if @eval_map.key?(tok)
          { [] => @eval_map[tok] }
        else
          { [tok] => 1 }
        end
      end
    end

    def add(p1, p2, sign = 1)
      res = Hash.new(0)
      p1.each { |k, v| res[k] += v }
      p2.each { |k, v| res[k] += sign * v }
      res.delete_if { |_k, v| v == 0 }
      res
    end

    def mul(p1, p2)
      res = Hash.new(0)
      p1.each do |k1, c1|
        p2.each do |k2, c2|
          new_key = (k1 + k2).sort
          res[new_key] += c1 * c2
        end
      end
      res.delete_if { |_k, v| v == 0 }
      res
    end

    def parse_expression
      left = parse_term
      while @i < @tokens.size && (op = @tokens[@i]) && (op == '+' || op == '-')
        @i += 1
        right = parse_term
        if op == '+'
          left = add(left, right, 1)
        else
          left = add(left, right, -1)
        end
      end
      left
    end

    def parse_term
      left = parse_factor
      while @i < @tokens.size && @tokens[@i] == '*'
        @i += 1
        right = parse_factor
        left = mul(left, right)
      end
      left
    end

    def parse_factor
      token = @tokens[@i]
      if token == '('
        @i += 1
        poly = parse_expression
        @i += 1 # skip ')'
        poly
      else
        @i += 1
        make_token(token)
      end
    end
  end

  tokens = expression.split(' ')
  parser = Parser.new(tokens, eval_map)
  poly = parser.parse_expression

  terms = poly.map { |vars, coeff| [coeff, vars] }
  sorted = terms.sort_by { |_, vars| [-vars.size, vars.join('*')] }

  sorted.map do |coeff, vars|
    if vars.empty?
      coeff.to_s
    else
      "#{coeff}*" + vars.join('*')
    end
  end
end
```

## Scala

```scala
import scala.collection.mutable
object Solution {
  type Poly = Map[Seq[String], Long]

  def basicCalculatorIV(expression: String, evalvars: Array[String], evalints: Array[Int]): List[String] = {
    val tokens: Array[String] = expression.split(" ").filter(_.nonEmpty)
    var pos = 0

    val evalMap: Map[String, Int] = evalvars.zip(evalints).toMap

    def constPoly(v: Long): Poly = if (v == 0) Map.empty else Map(Seq.empty -> v)

    def varPoly(name: String): Poly = Map(Seq(name) -> 1L)

    def add(a: Poly, b: Poly): Poly = {
      val res = mutable.Map[Seq[String], Long]()
      for ((k, v) <- a) res(k) = res.getOrElse(k, 0L) + v
      for ((k, v) <- b) res(k) = res.getOrElse(k, 0L) + v
      res.filter(_._2 != 0).toMap
    }

    def sub(a: Poly, b: Poly): Poly = {
      val res = mutable.Map[Seq[String], Long]()
      for ((k, v) <- a) res(k) = res.getOrElse(k, 0L) + v
      for ((k, v) <- b) res(k) = res.getOrElse(k, 0L) - v
      res.filter(_._2 != 0).toMap
    }

    def mergeVars(a: Seq[String], b: Seq[String]): Seq[String] = {
      val sb = mutable.ArrayBuffer[String]()
      var i = 0
      var j = 0
      while (i < a.length && j < b.length) {
        if (a(i) <= b(j)) { sb += a(i); i += 1 }
        else { sb += b(j); j += 1 }
      }
      while (i < a.length) { sb += a(i); i += 1 }
      while (j < b.length) { sb += b(j); j += 1 }
      sb.toSeq
    }

    def mul(a: Poly, b: Poly): Poly = {
      val res = mutable.Map[Seq[String], Long]()
      for ((ka, va) <- a; (kb, vb) <- b) {
        val coeff = va * vb
        val merged = mergeVars(ka, kb)
        res(merged) = res.getOrElse(merged, 0L) + coeff
      }
      res.filter(_._2 != 0).toMap
    }

    def parseExpression(): Poly = {
      var left = parseTerm()
      while (pos < tokens.length && (tokens(pos) == "+" || tokens(pos) == "-")) {
        val op = tokens(pos)
        pos += 1
        val right = parseTerm()
        left = if (op == "+") add(left, right) else sub(left, right)
      }
      left
    }

    def parseTerm(): Poly = {
      var left = parseFactor()
      while (pos < tokens.length && tokens(pos) == "*") {
        pos += 1
        val right = parseFactor()
        left = mul(left, right)
      }
      left
    }

    def parseFactor(): Poly = {
      val token = tokens(pos)
      pos += 1
      token match {
        case "(" =>
          val inner = parseExpression()
          // skip ')'
          if (pos < tokens.length && tokens(pos) == ")") pos += 1
          inner
        case _ =>
          if (token.head.isDigit || (token.head == '-' && token.length > 1 && token.tail.head.isDigit)) {
            constPoly(token.toLong)
          } else {
            evalMap.get(token) match {
              case Some(v) => constPoly(v.toLong)
              case None    => varPoly(token)
            }
          }
      }
    }

    val poly = parseExpression()

    val sortedTerms = poly.toSeq.sortWith { (p1, p2) =>
      val d1 = p1._1.length
      val d2 = p2._1.length
      if (d1 != d2) d1 > d2
      else {
        var i = 0
        while (i < d1 && i < d2 && p1._1(i) == p2._1(i)) i += 1
        if (i < d1 && i < d2) p1._1(i) < p2._1(i)
        else false
      }
    }

    sortedTerms.map { case (vars, coeff) =>
      if (vars.isEmpty) coeff.toString
      else coeff.toString + "*" + vars.mkString("*")
    }.toList
  }
}
```

## Rust

```rust
use std::collections::HashMap;

type Poly = HashMap<Vec<String>, i64>;

fn add_poly(a: &Poly, b: &Poly) -> Poly {
    let mut res = a.clone();
    for (k, v) in b.iter() {
        *res.entry(k.clone()).or_insert(0) += v;
    }
    res.retain(|_, c| *c != 0);
    res
}

fn sub_poly(a: &Poly, b: &Poly) -> Poly {
    let mut res = a.clone();
    for (k, v) in b.iter() {
        *res.entry(k.clone()).or_insert(0) -= v;
    }
    res.retain(|_, c| *c != 0);
    res
}

fn merge_vars(a: &Vec<String>, b: &Vec<String>) -> Vec<String> {
    let mut res = Vec::with_capacity(a.len() + b.len());
    let (mut i, mut j) = (0usize, 0usize);
    while i < a.len() && j < b.len() {
        if a[i] <= b[j] {
            res.push(a[i].clone());
            i += 1;
        } else {
            res.push(b[j].clone());
            j += 1;
        }
    }
    while i < a.len() {
        res.push(a[i].clone());
        i += 1;
    }
    while j < b.len() {
        res.push(b[j].clone());
        j += 1;
    }
    res
}

fn mul_poly(a: &Poly, b: &Poly) -> Poly {
    let mut res: Poly = HashMap::new();
    for (ka, va) in a.iter() {
        for (kb, vb) in b.iter() {
            let merged = merge_vars(ka, kb);
            *res.entry(merged).or_insert(0) += va * vb;
        }
    }
    res.retain(|_, c| *c != 0);
    res
}

struct Parser<'a> {
    tokens: Vec<String>,
    pos: usize,
    eval: &'a HashMap<String, i64>,
}

impl<'a> Parser<'a> {
    fn new(tokens: Vec<String>, eval: &'a HashMap<String, i64>) -> Self {
        Self { tokens, pos: 0, eval }
    }

    fn peek(&self) -> Option<&String> {
        self.tokens.get(self.pos)
    }

    fn next(&mut self) -> Option<String> {
        if self.pos < self.tokens.len() {
            let s = self.tokens[self.pos].clone();
            self.pos += 1;
            Some(s)
        } else {
            None
        }
    }

    fn parse_expression(&mut self) -> Poly {
        let mut left = self.parse_term();
        while let Some(op) = self.peek() {
            if op == "+" || op == "-" {
                let oper = op.clone();
                self.pos += 1;
                let right = self.parse_term();
                if oper == "+" {
                    left = add_poly(&left, &right);
                } else {
                    left = sub_poly(&left, &right);
                }
            } else {
                break;
            }
        }
        left
    }

    fn parse_term(&mut self) -> Poly {
        let mut left = self.parse_factor();
        while let Some(op) = self.peek() {
            if op == "*" {
                self.pos += 1;
                let right = self.parse_factor();
                left = mul_poly(&left, &right);
            } else {
                break;
            }
        }
        left
    }

    fn parse_factor(&mut self) -> Poly {
        let token = self.next().unwrap();
        if token == "(" {
            let inner = self.parse_expression();
            // consume ')'
            self.pos += 1; // assuming valid input
            inner
        } else if let Ok(num) = token.parse::<i64>() {
            let mut map = HashMap::new();
            map.insert(Vec::new(), num);
            map
        } else {
            if let Some(&val) = self.eval.get(&token) {
                let mut map = HashMap::new();
                map.insert(Vec::new(), val);
                map
            } else {
                let mut map = HashMap::new();
                map.insert(vec![token], 1);
                map
            }
        }
    }
}

impl Solution {
    pub fn basic_calculator_iv(expression: String, evalvars: Vec<String>, evalints: Vec<i32>) -> Vec<String> {
        let mut eval: HashMap<String, i64> = HashMap::new();
        for (v, i) in evalvars.iter().zip(evalints.iter()) {
            eval.insert(v.clone(), *i as i64);
        }
        let tokens: Vec<String> = expression.split_whitespace().map(|s| s.to_string()).collect();
        let mut parser = Parser::new(tokens, &eval);
        let poly = parser.parse_expression();

        let mut terms: Vec<(Vec<String>, i64)> = poly.into_iter().filter(|(_, c)| *c != 0).collect();
        terms.sort_by(|a, b| {
            let deg_a = a.0.len() as i32;
            let deg_b = b.0.len() as i32;
            if deg_a != deg_b {
                return deg_b.cmp(&deg_a); // descending degree
            }
            let sa = a.0.join("*");
            let sb = b.0.join("*");
            sa.cmp(&sb)
        });

        let mut result = Vec::new();
        for (vars, coeff) in terms {
            if vars.is_empty() {
                result.push(coeff.to_string());
            } else {
                result.push(format!("{}*{}", coeff, vars.join("*")));
            }
        }
        result
    }
}
```

## Racket

```racket
#lang racket
(require racket/hash)

;; Helper constructors for polynomials
(define (poly-from-number n)
  (let ((h (make-hash)))
    (unless (= n 0) (hash-set! h '() n))
    h))

(define (poly-from-var v)
  (let ((h (make-hash)))
    (hash-set! h (list v) 1)
    h))

;; Polynomial addition: p2 added with sign (+1 or -1)
(define (poly-add p1 p2 sign)
  (let ((res (hash-copy p1)))
    (for-each
     (lambda (kv)
       (define vars (car kv))
       (define coeff (cdr kv))
       (hash-update! res vars (lambda (old) (+ old (* sign coeff))) 0))
     (hash->list p2))
    (for ([k (hash-keys res)])
      (when (= (hash-ref res k) 0)
        (hash-remove! res k)))
    res))

;; Polynomial multiplication
(define (poly-mul p1 p2)
  (let ((res (make-hash)))
    (for* ([kv1 (in-hash p1)] [kv2 (in-hash p2)])
      (define vars1 (car kv1))
      (define coeff1 (cdr kv1))
      (define vars2 (car kv2))
      (define coeff2 (cdr kv2))
      (define newcoeff (* coeff1 coeff2))
      (define newvars (sort (append vars1 vars2) string<?))
      (hash-update! res newvars (lambda (old) (+ old newcoeff)) 0))
    (for ([k (hash-keys res)])
      (when (= (hash-ref res k) 0)
        (hash-remove! res k)))
    res))

;; Evaluate polynomial with given variable assignments
(define (evaluate-poly poly evalmap)
  (let ((res (make-hash)))
    (for ([kv (in-hash poly)])
      (define vars (car kv))
      (define coeff (cdr kv))
      (define factor coeff)
      (define remaining '())
      (for ([v vars])
        (if (hash-has-key? evalmap v)
            (set! factor (* factor (hash-ref evalmap v)))
            (set! remaining (cons v remaining))))
      (set! remaining (reverse remaining))
      (when (not (= factor 0))
        (hash-update! res remaining (lambda (old) (+ old factor)) 0)))
    (for ([k (hash-keys res)])
      (when (= (hash-ref res k) 0)
        (hash-remove! res k)))
    res))

;; Main function
(define/contract (basic-calculator-iv expression evalvars evalints)
  (-> string? (listof string?) (listof exact-integer?) (listof string?))
  (let* ((tokens (regexp-split #px"\\s+" expression))
         (len (length tokens)))
    ;; Recursive descent parser
    (define (parse-factor i)
      (let ((tok (list-ref tokens i)))
        (cond [(equal? tok "(")
               (let-values ([(poly j) (parse-expression (+ i 1))])
                 (values poly (+ j 1)))]
              [(regexp-match? #px"^[0-9]+$" tok)
               (values (poly-from-number (string->number tok)) (+ i 1))]
              [else
               (values (poly-from-var tok) (+ i 1))])))
    (define (parse-term i)
      (let-values ([(poly j) (parse-factor i)])
        (let loop ((p poly) (idx j))
          (if (and (< idx len) (equal? (list-ref tokens idx) "*"))
              (let-values ([(right k) (parse-factor (+ idx 1))])
                (loop (poly-mul p right) k))
              (values p idx)))))
    (define (parse-expression i)
      (let-values ([(poly j) (parse-term i)])
        (let loop ((p poly) (idx j))
          (if (< idx len)
              (let ((op (list-ref tokens idx)))
                (cond [(or (equal? op "+") (equal? op "-"))
                       (let-values ([(right k) (parse-term (+ idx 1))])
                         (loop (poly-add p right (if (equal? op "+") 1 -1)) k))]
                      [else (values p idx)]))
              (values p idx)))))
    ;; Parse whole expression
    (let-values ([(poly _) (parse-expression 0)])
      ;; Build evaluation map
      (define evalmap (make-hash))
      (for ([v evalvars] [n evalints])
        (hash-set! evalmap v n))
      (define evaluated (evaluate-poly poly evalmap))
      ;; Convert to required list format
      (let* ((terms (hash->list evaluated))
             (sorted (sort terms
                           (lambda (a b)
                             (let ((deg-a (length (car a)))
                                   (deg-b (length (car b))))
                               (cond [(> deg-a deg-b) #t]
                                     [(< deg-a deg-b) #f]
                                     [else (string<? (string-join (car a) "*")
                                                     (string-join (car b) "*"))]))))
             (result
              (map (lambda (kv)
                     (let ((vars (car kv)) (coeff (cdr kv)))
                       (if (null? vars)
                           (number->string coeff)
                           (string-append (number->string coeff) "*" (string-join vars "*")))))
                   sorted))
        result))))
```

## Erlang

```erlang
-module(solution).
-export([basic_calculator_iv/3]).

-spec basic_calculator_iv(Expression :: unicode:unicode_binary(),
                         Evalvars :: [unicode:unicode_binary()],
                         Evalints :: [integer()]) -> [unicode:unicode_binary()].
basic_calculator_iv(Expression, Evalvars, Evalints) ->
    Tokens = string:tokens(Expression, <<" ">>),
    {Poly0, []} = parse_expr(Tokens),
    EvalMap = build_eval_map(Evalvars, Evalints, #{}),
    Poly1 = evaluate_poly(Poly0, EvalMap),
    Terms = [{Vars, Coef} || {Vars, Coef} <- maps:to_list(Poly1), Coef =/= 0],
    Sorted = lists:sort(fun term_cmp/2, Terms),
    [list_to_binary(format_term(Vars, Coef)) || {Vars, Coef} <- Sorted].

%% Parsing
parse_expr(Toks) ->
    {Left, Rest1} = parse_term(Toks),
    parse_expr_rest(Left, Rest1).

parse_expr_rest(Acc, [<<"+">> | Rest]) ->
    {Right, Rest2} = parse_term(Rest),
    NewAcc = add_poly(Acc, Right),
    parse_expr_rest(NewAcc, Rest2);
parse_expr_rest(Acc, [<<"-">> | Rest]) ->
    {Right, Rest2} = parse_term(Rest),
    NewAcc = sub_poly(Acc, Right),
    parse_expr_rest(NewAcc, Rest2);
parse_expr_rest(Acc, Rest) -> {Acc, Rest}.

parse_term(Toks) ->
    {Left, Rest1} = parse_factor(Toks),
    parse_term_rest(Left, Rest1).

parse_term_rest(Acc, [<<"*">> | Rest]) ->
    {Right, Rest2} = parse_factor(Rest),
    NewAcc = mul_poly(Acc, Right),
    parse_term_rest(NewAcc, Rest2);
parse_term_rest(Acc, Rest) -> {Acc, Rest}.

parse_factor([Token | Rest]) ->
    case Token of
        <<"(">> ->
            {Poly, AfterParen} = parse_expr(Rest),
            case AfterParen of
                [<<")">> | Rest2] -> {Poly, Rest2};
                _ -> erlang:error(badmatch)
            end;
        _ ->
            Str = binary_to_list(Token),
            case string:to_integer(Str) of
                {Int, []} ->
                    {% number token
                     #{[] => Int}, Rest};
                error ->
                    {% variable token
                     #{[Token] => 1}, Rest}
            end
    end.

%% Polynomial operations
add_poly(P1, P2) ->
    maps:fold(fun(K,V,Acc) ->
        NewCoeff = V + maps:get(K, Acc, 0),
        if NewCoeff == 0 -> maps:remove(K, Acc);
           true -> maps:put(K, NewCoeff, Acc)
        end
    end, P1, P2).

sub_poly(P1, P2) ->
    add_poly(P1, negate_poly(P2)).

negate_poly(P) ->
    maps:map(fun(_K,V) -> -V end, P).

mul_poly(P1, P2) ->
    maps:fold(fun(Vars1,Coeff1,Acc) ->
        maps:fold(fun(Vars2,Coeff2,AccInner) ->
            NewCoeff = Coeff1 * Coeff2,
            MergedVars = merge_vars(Vars1, Vars2),
            Old = maps:get(MergedVars, AccInner, 0),
            Updated = Old + NewCoeff,
            if Updated == 0 -> maps:remove(MergedVars, AccInner);
               true -> maps:put(MergedVars, Updated, AccInner)
            end
        end, Acc, P2)
    end, #{}, P1).

merge_vars([], V) -> V;
merge_vars(V, []) -> V;
merge_vars([H1|T1]=L1, [H2|T2]=L2) ->
    case H1 =< H2 of
        true -> [H1 | merge_vars(T1, L2)];
        false -> [H2 | merge_vars(L1, T2)]
    end.

%% Evaluation with given variable values
evaluate_poly(Poly, EvalMap) ->
    maps:fold(fun(Vars,Coeff,Acc) ->
        {NewCoeff, NewVars} = substitute_vars(Vars, Coeff, EvalMap),
        if NewCoeff == 0 -> Acc;
           true ->
               Old = maps:get(NewVars, Acc, 0),
               Updated = Old + NewCoeff,
               maps:put(NewVars, Updated, Acc)
        end
    end, #{}, Poly).

substitute_vars(Vars, Coef, EvalMap) ->
    lists:foldl(fun(Var,{AccC,AccV}) ->
        case maps:get(Var, EvalMap, undefined) of
            undefined -> {AccC, AccV ++ [Var]};
            Value -> {AccC * Value, AccV}
        end
    end, {Coef, []}, Vars).

%% Build evaluation map
build_eval_map([], [], Map) -> Map;
build_eval_map([Var|Vs], [Int|Is], Map) ->
    build_eval_map(Vs, Is, maps:put(Var, Int, Map)).

%% Sorting comparator
term_cmp({V1,_},{V2,_}) ->
    Len1 = length(V1),
    Len2 = length(V2),
    if Len1 > Len2 -> true;
       Len1 < Len2 -> false;
       true -> V1 < V2
    end.

%% Formatting output term
format_term([], Coef) ->
    integer_to_list(Coef);
format_term(Vars, Coef) ->
    CoefStr = integer_to_list(Coef),
    VarStr = string:join([binary_to_list(V) || V <- Vars], "*"),
    CoefStr ++ "*" ++ VarStr.
```

## Elixir

```elixir
defmodule Solution do
  @spec basic_calculator_iv(String.t(), [String.t()], [integer]) :: [String.t()]
  def basic_calculator_iv(expression, evalvars, evalints) do
    tokens = String.split(expression, " ", trim: true)
    {poly, []} = parse_expr(tokens)

    eval_map = Enum.zip(evalvars, evalints) |> Map.new()
    poly = evaluate(poly, eval_map)
    format(poly)
  end

  # Parsing functions ---------------------------------------------------------

  defp parse_expr(tokens) do
    {left, rest} = parse_term(tokens)
    parse_expr_rest(left, rest)
  end

  defp parse_expr_rest(acc, ["+" | rest]) do
    {right, rest2} = parse_term(rest)
    parse_expr_rest(add(acc, right), rest2)
  end

  defp parse_expr_rest(acc, ["-" | rest]) do
    {right, rest2} = parse_term(rest)
    parse_expr_rest(sub(acc, right), rest2)
  end

  defp parse_expr_rest(acc, tokens), do: {acc, tokens}

  defp parse_term(tokens) do
    {left, rest} = parse_factor(tokens)
    parse_term_rest(left, rest)
  end

  defp parse_term_rest(acc, ["*" | rest]) do
    {right, rest2} = parse_factor(rest)
    parse_term_rest(mul(acc, right), rest2)
  end

  defp parse_term_rest(acc, tokens), do: {acc, tokens}

  defp parse_factor(["(" | rest]) do
    {poly, [")" | rest2]} = parse_expr(rest)
    {poly, rest2}
  end

  defp parse_factor([token | rest]), do: {make_poly(token), rest}

  # Polynomial operations -----------------------------------------------------

  defp make_poly(token) do
    case Integer.parse(token) do
      {num, ""} -> %{[] => num}
      :error -> %{[token] => 1}
    end
  end

  defp add(p1, p2), do: Map.merge(p1, p2, fn _k v1 v2 -> v1 + v2 end)

  defp sub(p1, p2), do: Map.merge(p1, p2, fn _k v1 v2 -> v1 - v2 end)

  defp mul(p1, p2) do
    Enum.reduce(p1, %{}, fn {vars1, coeff1}, acc ->
      Enum.reduce(p2, acc, fn {vars2, coeff2}, acc2 ->
        new_vars = (vars1 ++ vars2) |> Enum.sort()
        Map.update(acc2, new_vars, coeff1 * coeff2, &(&1 + coeff1 * coeff2))
      end)
    end)
  end

  # Evaluation with given variable values -------------------------------------

  defp evaluate(poly, eval_map) do
    Enum.reduce(poly, %{}, fn {vars, coeff}, acc ->
      {new_coeff, remaining} =
        Enum.reduce(vars, {coeff, []}, fn var, {c, rem} ->
          case Map.fetch(eval_map, var) do
            {:ok, val} -> {c * val, rem}
            :error -> {c, [var | rem]}
          end
        end)

      if new_coeff == 0 do
        acc
      else
        sorted_rem = Enum.sort(remaining)
        Map.update(acc, sorted_rem, new_coeff, &(&1 + new_coeff))
      end
    end)
  end

  # Formatting output ---------------------------------------------------------

  defp format(poly) do
    poly
    |> Enum.filter(fn {_vars, coeff} -> coeff != 0 end)
    |> Enum.map(fn {vars, coeff} ->
      term =
        if vars == [] do
          Integer.to_string(coeff)
        else
          var_part = Enum.join(vars, "*")
          "#{coeff}*#{var_part}"
        end

      {length(vars), vars, term}
    end)
    |> Enum.sort_by(fn {deg, vars, _term} -> {-deg, vars} end)
    |> Enum.map(fn {_d, _v, term} -> term end)
  end
end
```
