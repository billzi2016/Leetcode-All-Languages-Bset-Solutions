# 0721. Accounts Merge

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class DSU {
public:
    vector<int> parent, rankv;
    DSU() {}
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    void unite(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra == rb) return;
        if (rankv[ra] < rankv[rb]) swap(ra, rb);
        parent[rb] = ra;
        if (rankv[ra] == rankv[rb]) ++rankv[ra];
    }
};

class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        unordered_map<string,int> emailToId;
        unordered_map<string,string> emailToName;
        DSU dsu;
        int idx = 0;

        for (const auto& acc : accounts) {
            const string& name = acc[0];
            if (acc.size() < 2) continue; // safety
            // ensure first email exists in map
            const string& firstEmail = acc[1];
            if (!emailToId.count(firstEmail)) {
                emailToId[firstEmail] = idx++;
                dsu.parent.push_back(emailToId[firstEmail]);
                dsu.rankv.push_back(0);
                emailToName[firstEmail] = name;
            } else {
                // name should be same for this email across accounts
                emailToName[firstEmail] = name;
            }
            int firstId = emailToId[firstEmail];
            // process remaining emails
            for (size_t i = 2; i < acc.size(); ++i) {
                const string& em = acc[i];
                if (!emailToId.count(em)) {
                    emailToId[em] = idx++;
                    dsu.parent.push_back(emailToId[em]);
                    dsu.rankv.push_back(0);
                    emailToName[em] = name;
                }
                int curId = emailToId[em];
                dsu.unite(firstId, curId);
            }
        }

        unordered_map<int, vector<string>> groups;
        for (const auto& p : emailToId) {
            int root = dsu.find(p.second);
            groups[root].push_back(p.first);
        }

        vector<vector<string>> result;
        for (auto& kv : groups) {
            auto& emails = kv.second;
            sort(emails.begin(), emails.end());
            string name = emailToName[emails[0]];
            vector<string> merged;
            merged.reserve(emails.size() + 1);
            merged.push_back(name);
            merged.insert(merged.end(), emails.begin(), emails.end());
            result.push_back(move(merged));
        }
        return result;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        int n = accounts.size();
        UnionFind uf = new UnionFind(n);
        Map<String, Integer> emailToAccount = new HashMap<>();

        for (int i = 0; i < n; i++) {
            List<String> acc = accounts.get(i);
            for (int j = 1; j < acc.size(); j++) {
                String email = acc.get(j);
                if (!emailToAccount.containsKey(email)) {
                    emailToAccount.put(email, i);
                } else {
                    uf.union(i, emailToAccount.get(email));
                }
            }
        }

        Map<Integer, List<String>> groups = new HashMap<>();
        for (Map.Entry<String, Integer> e : emailToAccount.entrySet()) {
            int root = uf.find(e.getValue());
            groups.computeIfAbsent(root, k -> new ArrayList<>()).add(e.getKey());
        }

        List<List<String>> result = new ArrayList<>();
        for (Map.Entry<Integer, List<String>> entry : groups.entrySet()) {
            List<String> emails = entry.getValue();
            Collections.sort(emails);
            List<String> merged = new ArrayList<>();
            merged.add(accounts.get(entry.getKey()).get(0));
            merged.addAll(emails);
            result.add(merged);
        }

        return result;
    }

    private static class UnionFind {
        int[] parent;
        int[] rank;

        UnionFind(int size) {
            parent = new int[size];
            rank = new int[size];
            for (int i = 0; i < size; i++) {
                parent[i] = i;
                rank[i] = 1;
            }
        }

        int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }

        void union(int a, int b) {
            int rootA = find(a);
            int rootB = find(b);
            if (rootA == rootB) return;
            if (rank[rootA] < rank[rootB]) {
                parent[rootA] = rootB;
            } else if (rank[rootA] > rank[rootB]) {
                parent[rootB] = rootA;
            } else {
                parent[rootB] = rootA;
                rank[rootA]++;
            }
        }
    }
}
```

## Python

```python
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        email_to_id = {}
        email_to_name = {}
        parent = []
        rank = []

        def add_email(email):
            if email not in email_to_id:
                idx = len(parent)
                email_to_id[email] = idx
                parent.append(idx)
                rank.append(0)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1

        for acc in accounts:
            name = acc[0]
            first_email = acc[1]
            add_email(first_email)
            email_to_name[first_email] = name
            first_id = email_to_id[first_email]
            for e in acc[2:]:
                add_email(e)
                email_to_name[e] = name
                union(first_id, email_to_id[e])

        from collections import defaultdict
        groups = defaultdict(list)
        for email, idx in email_to_id.items():
            root = find(idx)
            groups[root].append(email)

        result = []
        for emails in groups.values():
            emails.sort()
            result.append([email_to_name[emails[0]]] + emails)

        return result
```

## Python3

```python
from typing import List
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = list(range(n))
        rank = [0] * n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1

        email_to_id = {}
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email not in email_to_id:
                    email_to_id[email] = i
                else:
                    union(i, email_to_id[email])

        from collections import defaultdict
        groups = defaultdict(list)
        for email, idx in email_to_id.items():
            root = find(idx)
            groups[root].append(email)

        merged = []
        for root, emails in groups.items():
            name = accounts[root][0]
            merged.append([name] + sorted(emails))
        return merged
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include "uthash.h"

/* Union-Find (Disjoint Set Union) */
static int *parent;
static int *rankArr;

static int find_set(int x) {
    if (parent[x] != x)
        parent[x] = find_set(parent[x]);
    return parent[x];
}

static void union_set(int a, int b) {
    int ra = find_set(a);
    int rb = find_set(b);
    if (ra == rb) return;
    if (rankArr[ra] < rankArr[rb]) {
        parent[ra] = rb;
    } else if (rankArr[ra] > rankArr[rb]) {
        parent[rb] = ra;
    } else {
        parent[rb] = ra;
        rankArr[ra]++;
    }
}

/* Hash map for email -> id and name */
typedef struct {
    char *email;          /* key */
    int   id;             /* value: unique integer id */
    char *name;           /* owner's name (first string of the account) */
    UT_hash_handle hh;
} EmailInfo;

/* Dynamic list to collect emails belonging to same component */
typedef struct {
    char **emails;
    int    size;
    int    cap;
    char  *name;          /* owner name for this component */
} EmailList;

static int cmp_str(const void *a, const void *b) {
    const char *sa = *(const char **)a;
    const char *sb = *(const char **)b;
    return strcmp(sa, sb);
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced,
 * assume caller calls free().
 */
char*** accountsMerge(char*** accounts, int accountsSize, int* accountsColSize,
                     int* returnSize, int** returnColumnSizes) {
    EmailInfo *emailMap = NULL;   /* hash table */
    int maxEmails = accountsSize * 10 + 5;
    parent = (int *)malloc(maxEmails * sizeof(int));
    rankArr = (int *)calloc(maxEmails, sizeof(int));

    int emailCnt = 0;

    /* First pass: assign ids and union emails within each account */
    for (int i = 0; i < accountsSize; ++i) {
        char *ownerName = accounts[i][0];
        int col = accountsColSize[i];
        if (col <= 1) continue;   // no email

        /* process first email to get its id */
        EmailInfo *firstInfo;
        HASH_FIND_STR(emailMap, accounts[i][1], firstInfo);
        if (!firstInfo) {
            firstInfo = (EmailInfo *)malloc(sizeof(EmailInfo));
            firstInfo->email = accounts[i][1];
            firstInfo->id = emailCnt++;
            firstInfo->name = ownerName;
            HASH_ADD_KEYPTR(hh, emailMap, firstInfo->email,
                            strlen(firstInfo->email), firstInfo);
        }
        int firstId = firstInfo->id;

        for (int j = 2; j < col; ++j) {
            EmailInfo *info;
            HASH_FIND_STR(emailMap, accounts[i][j], info);
            if (!info) {
                info = (EmailInfo *)malloc(sizeof(EmailInfo));
                info->email = accounts[i][j];
                info->id = emailCnt++;
                info->name = ownerName;
                HASH_ADD_KEYPTR(hh, emailMap, info->email,
                                strlen(info->email), info);
            }
            union_set(firstId, info->id);
        }
    }

    /* Initialize DSU parent array */
    for (int i = 0; i < emailCnt; ++i) parent[i] = i;

    /* Second pass: union again now that parent array is ready */
    EmailInfo *e, *tmp;
    HASH_ITER(hh, emailMap, e, tmp) {
        // ensure each node points to its root after all unions
        find_set(e->id);
    }

    /* Prepare lists for each component */
    EmailList *lists = (EmailList *)calloc(emailCnt, sizeof(EmailList));

    HASH_ITER(hh, emailMap, e, tmp) {
        int root = find_set(e->id);
        EmailList *lst = &lists[root];
        if (lst->size == lst->cap) {
            lst->cap = lst->cap ? lst->cap * 2 : 4;
            lst->emails = (char **)realloc(lst->emails,
                                           lst->cap * sizeof(char *));
        }
        lst->emails[lst->size++] = e->email;
        if (!lst->name) lst->name = e->name;
    }

    /* Count components */
    int compCount = 0;
    for (int i = 0; i < emailCnt; ++i)
        if (lists[i].size > 0) compCount++;

    char ***result = (char ***)malloc(compCount * sizeof(char **));
    int *colSizes = (int *)malloc(compCount * sizeof(int));

    int idx = 0;
    for (int i = 0; i < emailCnt; ++i) {
        if (lists[i].size == 0) continue;

        qsort(lists[i].emails, lists[i].size,
              sizeof(char *), cmp_str);

        int totalCols = lists[i].size + 1;
        char **row = (char **)malloc(totalCols * sizeof(char *));
        row[0] = strdup(lists[i].name);
        for (int j = 0; j < lists[i].size; ++j)
            row[j + 1] = strdup(lists[i].emails[j]);

        result[idx] = row;
        colSizes[idx] = totalCols;
        idx++;
    }

    *returnSize = compCount;
    *returnColumnSizes = colSizes;

    /* Cleanup hash table and auxiliary structures */
    HASH_ITER(hh, emailMap, e, tmp) {
        HASH_DEL(emailMap, e);
        free(e);
    }
    for (int i = 0; i < emailCnt; ++i) {
        free(lists[i].emails);
    }
    free(lists);
    free(parent);
    free(rankArr);

    return result;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution
{
    private List<int> parent = new List<int>();
    private List<int> rank = new List<int>();

    private int Find(int x)
    {
        if (parent[x] != x)
            parent[x] = Find(parent[x]);
        return parent[x];
    }

    private void Union(int x, int y)
    {
        int rootX = Find(x);
        int rootY = Find(y);
        if (rootX == rootY) return;

        if (rank[rootX] < rank[rootY])
            parent[rootX] = rootY;
        else if (rank[rootX] > rank[rootY])
            parent[rootY] = rootX;
        else
        {
            parent[rootY] = rootX;
            rank[rootX]++;
        }
    }

    public IList<IList<string>> AccountsMerge(IList<IList<string>> accounts)
    {
        var emailToId = new Dictionary<string, int>();
        var emailToName = new Dictionary<string, string>();
        int idCounter = 0;

        // Build DSU connections
        foreach (var account in accounts)
        {
            if (account.Count < 2) continue;
            string name = account[0];
            for (int i = 1; i < account.Count; i++)
            {
                string email = account[i];
                if (!emailToId.ContainsKey(email))
                {
                    emailToId[email] = idCounter++;
                    parent.Add(emailToId[email]);
                    rank.Add(0);
                    emailToName[email] = name;
                }
                // Union first email of this account with current
                if (i == 1) continue; // skip union for the first email itself
                int firstId = emailToId[account[1]];
                int curId = emailToId[email];
                Union(firstId, curId);
            }
        }

        // Group emails by root parent
        var groups = new Dictionary<int, List<string>>();
        foreach (var kvp in emailToId)
        {
            string email = kvp.Key;
            int root = Find(kvp.Value);
            if (!groups.ContainsKey(root))
                groups[root] = new List<string>();
            groups[root].Add(email);
        }

        var result = new List<IList<string>>();
        foreach (var group in groups.Values)
        {
            group.Sort(StringComparer.Ordinal);
            string name = emailToName[group[0]];
            var merged = new List<string> { name };
            merged.AddRange(group);
            result.Add(merged);
        }

        return result;
    }
}
```

## Javascript

```javascript
/**
 * @param {string[][]} accounts
 * @return {string[][]}
 */
var accountsMerge = function(accounts) {
    const n = accounts.length;
    const parent = new Array(n);
    const size = new Array(n).fill(1);
    for (let i = 0; i < n; ++i) parent[i] = i;

    const find = (x) => {
        if (parent[x] !== x) parent[x] = find(parent[x]);
        return parent[x];
    };
    const union = (a, b) => {
        let ra = find(a), rb = find(b);
        if (ra === rb) return;
        // union by size
        if (size[ra] < size[rb]) {
            parent[ra] = rb;
            size[rb] += size[ra];
        } else {
            parent[rb] = ra;
            size[ra] += size[rb];
        }
    };

    const emailToIdx = new Map(); // email -> account index

    for (let i = 0; i < n; ++i) {
        const emails = accounts[i];
        for (let j = 1; j < emails.length; ++j) {
            const email = emails[j];
            if (!emailToIdx.has(email)) {
                emailToIdx.set(email, i);
            } else {
                union(i, emailToIdx.get(email));
            }
        }
    }

    // group emails by root parent
    const groups = new Map(); // root -> array of emails
    for (const [email, idx] of emailToIdx.entries()) {
        const root = find(idx);
        if (!groups.has(root)) groups.set(root, []);
        groups.get(root).push(email);
    }

    const result = [];
    for (const [root, emails] of groups.entries()) {
        emails.sort(); // lexicographic
        const merged = [accounts[root][0], ...emails];
        result.push(merged);
    }
    return result;
};
```

## Typescript

```typescript
function accountsMerge(accounts: string[][]): string[][] {
    const n = accounts.length;
    const parent = new Array<number>(n);
    for (let i = 0; i < n; i++) parent[i] = i;

    const find = (x: number): number => {
        if (parent[x] !== x) parent[x] = find(parent[x]);
        return parent[x];
    };

    const union = (a: number, b: number): void => {
        const ra = find(a);
        const rb = find(b);
        if (ra !== rb) parent[rb] = ra;
    };

    const emailToIdx = new Map<string, number>();

    for (let i = 0; i < n; i++) {
        const emails = accounts[i];
        for (let j = 1; j < emails.length; j++) {
            const email = emails[j];
            if (!emailToIdx.has(email)) {
                emailToIdx.set(email, i);
            } else {
                union(i, emailToIdx.get(email)!);
            }
        }
    }

    const groups = new Map<number, string[]>();
    for (const [email, idx] of emailToIdx.entries()) {
        const root = find(idx);
        if (!groups.has(root)) groups.set(root, []);
        groups.get(root)!.push(email);
    }

    const result: string[][] = [];
    for (const [root, emails] of groups.entries()) {
        emails.sort();
        const name = accounts[root][0];
        result.push([name, ...emails]);
    }
    return result;
}
```

## Php

```php
class Solution {
    /**
     * @param String[][] $accounts
     * @return String[][]
     */
    function accountsMerge($accounts) {
        $emailToId = [];
        $emailToName = [];
        $parent = [];
        $size = [];

        // Find with path compression
        $find = null;
        $find = function ($x) use (&$parent, &$find) {
            if ($parent[$x] !== $x) {
                $parent[$x] = $find($parent[$x]);
            }
            return $parent[$x];
        };

        // Union by size
        $union = function ($a, $b) use (&$parent, &$size, $find) {
            $rootA = $find($a);
            $rootB = $find($b);
            if ($rootA === $rootB) return;
            if ($size[$rootA] < $size[$rootB]) {
                $parent[$rootA] = $rootB;
                $size[$rootB] += $size[$rootA];
            } else {
                $parent[$rootB] = $rootA;
                $size[$rootA] += $size[$rootB];
            }
        };

        // Assign IDs and union emails within each account
        foreach ($accounts as $account) {
            $name = $account[0];
            if (count($account) < 2) continue; // no email

            $firstEmail = $account[1];
            if (!isset($emailToId[$firstEmail])) {
                $id = count($parent);
                $emailToId[$firstEmail] = $id;
                $parent[$id] = $id;
                $size[$id] = 1;
                $emailToName[$firstEmail] = $name;
            } else {
                // ensure name is stored (same person)
                $emailToName[$firstEmail] = $name;
            }
            $firstId = $emailToId[$firstEmail];

            $len = count($account);
            for ($i = 2; $i < $len; $i++) {
                $email = $account[$i];
                if (!isset($emailToId[$email])) {
                    $id = count($parent);
                    $emailToId[$email] = $id;
                    $parent[$id] = $id;
                    $size[$id] = 1;
                    $emailToName[$email] = $name;
                }
                $currId = $emailToId[$email];
                $union($firstId, $currId);
            }
        }

        // Group emails by their root parent
        $components = [];
        foreach ($emailToId as $email => $id) {
            $root = $find($id);
            if (!isset($components[$root])) {
                $components[$root] = [];
            }
            $components[$root][] = $email;
        }

        // Build the final merged accounts list
        $result = [];
        foreach ($components as $emails) {
            sort($emails, SORT_STRING);
            $name = $emailToName[$emails[0]];
            array_unshift($emails, $name);
            $result[] = $emails;
        }

        return $result;
    }
}
```

## Swift

```swift
class Solution {
    func accountsMerge(_ accounts: [[String]]) -> [[String]] {
        var emailToId = [String: Int]()
        var emailToName = [String: String]()
        var parent = [Int]()
        var rank = [Int]()
        
        func find(_ x: Int) -> Int {
            if parent[x] != x {
                parent[x] = find(parent[x])
            }
            return parent[x]
        }
        
        func union(_ x: Int, _ y: Int) {
            let rootX = find(x)
            let rootY = find(y)
            if rootX == rootY { return }
            if rank[rootX] < rank[rootY] {
                parent[rootX] = rootY
            } else if rank[rootX] > rank[rootY] {
                parent[rootY] = rootX
            } else {
                parent[rootY] = rootX
                rank[rootX] += 1
            }
        }
        
        for account in accounts {
            let name = account[0]
            guard account.count > 1 else { continue }
            var firstId: Int? = nil
            for i in 1..<account.count {
                let email = account[i]
                if emailToId[email] == nil {
                    let id = parent.count
                    emailToId[email] = id
                    parent.append(id)
                    rank.append(0)
                    emailToName[email] = name
                }
                let curId = emailToId[email]!
                if firstId == nil {
                    firstId = curId
                } else {
                    union(firstId!, curId)
                }
            }
        }
        
        var groups = [Int: [String]]()
        for (email, id) in emailToId {
            let root = find(id)
            groups[root, default: []].append(email)
        }
        
        var result = [[String]]()
        for (_, emails) in groups {
            let sortedEmails = emails.sorted()
            if let name = emailToName[sortedEmails.first ?? ""] {
                var entry = [name]
                entry.append(contentsOf: sortedEmails)
                result.append(entry)
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
class Solution {
    fun accountsMerge(accounts: List<List<String>>): List<List<String>> {
        val emailToId = HashMap<String, Int>()
        val emailToName = HashMap<String, String>()
        val parent = mutableListOf<Int>()
        val rank = mutableListOf<Int>()

        fun find(x: Int): Int {
            var p = parent[x]
            if (p != x) {
                parent[x] = find(p)
                p = parent[x]
            }
            return p
        }

        fun union(a: Int, b: Int) {
            var ra = find(a)
            var rb = find(b)
            if (ra == rb) return
            if (rank[ra] < rank[rb]) {
                parent[ra] = rb
            } else if (rank[ra] > rank[rb]) {
                parent[rb] = ra
            } else {
                parent[rb] = ra
                rank[ra] = rank[ra] + 1
            }
        }

        for (account in accounts) {
            val name = account[0]
            if (account.size < 2) continue
            // ensure all emails have ids
            for (i in 1 until account.size) {
                val email = account[i]
                if (!emailToId.containsKey(email)) {
                    val id = parent.size
                    emailToId[email] = id
                    parent.add(id)
                    rank.add(0)
                }
                emailToName[email] = name
            }
            // union emails in the same account
            val firstId = emailToId[account[1]]!!
            for (i in 2 until account.size) {
                val curId = emailToId[account[i]]!!
                union(firstId, curId)
            }
        }

        val groups = HashMap<Int, MutableList<String>>()
        for ((email, id) in emailToId) {
            val root = find(id)
            groups.getOrPut(root) { mutableListOf() }.add(email)
        }

        val result = mutableListOf<List<String>>()
        for (emails in groups.values) {
            emails.sort()
            val name = emailToName[emails[0]]!!
            val merged = mutableListOf<String>()
            merged.add(name)
            merged.addAll(emails)
            result.add(merged)
        }
        return result
    }
}
```

## Dart

```dart
class UnionFind {
  List<int> parent = [];
  List<int> rank = [];

  int add() {
    int id = parent.length;
    parent.add(id);
    rank.add(0);
    return id;
  }

  int find(int x) {
    while (parent[x] != x) {
      parent[x] = parent[parent[x]];
      x = parent[x];
    }
    return x;
  }

  void union(int x, int y) {
    int rx = find(x);
    int ry = find(y);
    if (rx == ry) return;
    if (rank[rx] < rank[ry]) {
      parent[rx] = ry;
    } else if (rank[rx] > rank[ry]) {
      parent[ry] = rx;
    } else {
      parent[ry] = rx;
      rank[rx]++;
    }
  }
}

class Solution {
  List<List<String>> accountsMerge(List<List<String>> accounts) {
    UnionFind uf = UnionFind();
    Map<String, int> emailToId = {};
    Map<String, String> emailToName = {};

    for (var account in accounts) {
      if (account.length < 2) continue;
      String name = account[0];
      String firstEmail = account[1];

      int firstId;
      if (!emailToId.containsKey(firstEmail)) {
        firstId = uf.add();
        emailToId[firstEmail] = firstId;
        emailToName[firstEmail] = name;
      } else {
        firstId = emailToId[firstEmail]!;
      }

      for (int i = 2; i < account.length; i++) {
        String email = account[i];
        int id;
        if (!emailToId.containsKey(email)) {
          id = uf.add();
          emailToId[email] = id;
          emailToName[email] = name;
        } else {
          id = emailToId[email]!;
        }
        uf.union(firstId, id);
      }
    }

    Map<int, List<String>> groups = {};
    for (var entry in emailToId.entries) {
      String email = entry.key;
      int root = uf.find(entry.value);
      groups.putIfAbsent(root, () => []).add(email);
    }

    List<List<String>> result = [];
    for (var emails in groups.values) {
      emails.sort();
      String name = emailToName[emails[0]]!;
      List<String> merged = [name];
      merged.addAll(emails);
      result.add(merged);
    }
    return result;
  }
}
```

## Golang

```go
import "sort"

func accountsMerge(accounts [][]string) [][]string {
    emailToName := make(map[string]string)
    adj := make(map[string][]string)

    for _, acc := range accounts {
        name := acc[0]
        if len(acc) < 2 {
            continue
        }
        firstEmail := acc[1]
        // map each email to its owner name
        for i := 1; i < len(acc); i++ {
            emailToName[acc[i]] = name
        }
        // connect emails in a star shape
        for i := 2; i < len(acc); i++ {
            e := acc[i]
            adj[firstEmail] = append(adj[firstEmail], e)
            adj[e] = append(adj[e], firstEmail)
        }
    }

    visited := make(map[string]bool)
    var result [][]string

    for email := range emailToName {
        if visited[email] {
            continue
        }
        // DFS to collect all connected emails
        stack := []string{email}
        visited[email] = true
        component := []string{}
        for len(stack) > 0 {
            cur := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            component = append(component, cur)
            for _, nb := range adj[cur] {
                if !visited[nb] {
                    visited[nb] = true
                    stack = append(stack, nb)
                }
            }
        }
        sort.Strings(component)
        merged := make([]string, 0, len(component)+1)
        merged = append(merged, emailToName[email])
        merged = append(merged, component...)
        result = append(result, merged)
    }

    return result
}
```

## Ruby

```ruby
def accounts_merge(accounts)
  require 'set'
  email_to_name = {}
  graph = Hash.new { |h, k| h[k] = [] }

  accounts.each do |account|
    name = account[0]
    first_email = account[1]
    (1...account.size).each do |i|
      email = account[i]
      email_to_name[email] = name
      graph[first_email] << email
      graph[email] << first_email
    end
  end

  visited = Set.new
  result = []

  accounts.each do |account|
    (1...account.size).each do |i|
      email = account[i]
      next if visited.include?(email)

      stack = [email]
      component = []
      while !stack.empty?
        cur = stack.pop
        next if visited.include?(cur)
        visited.add(cur)
        component << cur
        graph[cur].each { |nbr| stack << nbr unless visited.include?(nbr) }
      end

      component.sort!
      component.unshift(email_to_name[email])
      result << component
    end
  end

  result
end
```

## Scala

```scala
object Solution {
  import scala.collection.mutable

  def accountsMerge(accounts: List[List[String]]): List[List[String]] = {
    val parent = mutable.Map[String, String]()
    val emailToName = mutable.Map[String, String]()

    def find(x: String): String = {
      var p = parent.getOrElseUpdate(x, x)
      if (p != x) {
        val root = find(p)
        parent.update(x, root)
        root
      } else x
    }

    def union(a: String, b: String): Unit = {
      val ra = find(a)
      val rb = find(b)
      if (ra != rb) parent.update(ra, rb)
    }

    for (account <- accounts) {
      val name = account.head
      val emails = account.tail
      if (emails.nonEmpty) {
        for (email <- emails) {
          emailToName(email) = name
          if (!parent.contains(email)) parent(email) = email
        }
        val first = emails.head
        for (email <- emails.tail) union(first, email)
      }
    }

    val groups = mutable.Map[String, mutable.ArrayBuffer[String]]()
    for (email <- parent.keys) {
      val root = find(email)
      groups.getOrElseUpdate(root, mutable.ArrayBuffer()) += email
    }

    val result = mutable.ArrayBuffer[List[String]]()
    for ((root, buf) <- groups) {
      val sortedEmails = buf.sorted
      val name = emailToName(root)
      result += (name +: sortedEmails).toList
    }
    result.toList
  }
}
```

## Rust

```rust
use std::collections::HashMap;

struct DSU {
    parent: Vec<usize>,
    rank: Vec<usize>,
}

impl DSU {
    fn new(n: usize) -> Self {
        let mut parent = Vec::with_capacity(n);
        for i in 0..n {
            parent.push(i);
        }
        let rank = vec![0; n];
        DSU { parent, rank }
    }

    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] != x {
            let root = self.find(self.parent[x]);
            self.parent[x] = root;
        }
        self.parent[x]
    }

    fn union(&mut self, x: usize, y: usize) {
        let mut xr = self.find(x);
        let mut yr = self.find(y);
        if xr == yr {
            return;
        }
        if self.rank[xr] < self.rank[yr] {
            std::mem::swap(&mut xr, &mut yr);
        }
        self.parent[yr] = xr;
        if self.rank[xr] == self.rank[yr] {
            self.rank[xr] += 1;
        }
    }
}

impl Solution {
    pub fn accounts_merge(accounts: Vec<Vec<String>>) -> Vec<Vec<String>> {
        let n = accounts.len();
        let mut dsu = DSU::new(n);
        let mut email_to_idx: HashMap<String, usize> = HashMap::new();

        for (i, account) in accounts.iter().enumerate() {
            for email in account.iter().skip(1) {
                if let Some(&j) = email_to_idx.get(email) {
                    dsu.union(i, j);
                } else {
                    email_to_idx.insert(email.clone(), i);
                }
            }
        }

        let mut groups: HashMap<usize, Vec<String>> = HashMap::new();
        for (email, &idx) in email_to_idx.iter() {
            let root = dsu.find(idx);
            groups.entry(root).or_default().push(email.clone());
        }

        let mut result: Vec<Vec<String>> = Vec::new();
        for (root, mut emails) in groups {
            emails.sort();
            let mut merged = Vec::with_capacity(emails.len() + 1);
            merged.push(accounts[root][0].clone());
            merged.extend(emails);
            result.push(merged);
        }

        result
    }
}
```

## Racket

```racket
(require racket/set)

(define/contract (accounts-merge accounts)
  (-> (listof (listof string?)) (listof (listof string?)))
  (let* ((adj (make-hash))          ; email -> set of neighbor emails
         (email-name (make-hash))) ; email -> owner name
    ;; Build graph and map each email to its owner's name
    (for ([account accounts])
      (match account
        [(list name . emails)
         (when (null? emails) (void))
         (for ([e emails])
           (unless (hash-has-key? email-name e)
             (hash-set! email-name e name)))
         (let ([first (car emails)])
           (for ([e (cdr emails)])
             ;; add undirected edge between first and e
             (define set1 (hash-ref adj first (set)))
             (hash-set! adj first (set-add set1 e))
             (define set2 (hash-ref adj e (set)))
             (hash-set! adj e (set-add set2 first))))]))
    ;; Depth‑first search to collect connected components
    (let ((visited (make-hash))) ; email -> #t
      (define (dfs start)
        (let loop ((stack (list start)) (comp '()))
          (if (null? stack)
              comp
              (let* ((node (car stack))
                     (rest-stack (cdr stack)))
                (if (hash-has-key? visited node)
                    (loop rest-stack comp)
                    (begin
                      (hash-set! visited node #t)
                      (define neighbors (hash-ref adj node (set))) ; may be empty
                      (loop (append (set->list neighbors) rest-stack)
                            (cons node comp))))))))
      (let ((result '()))
        (for ([email (hash-keys email-name)])
          (unless (hash-has-key? visited email)
            (define component (dfs email))
            (define sorted-emails
              (sort (map ~a component) string<?)) ; ensure strings and sort
            (define name (hash-ref email-name email))
            (set! result (cons (cons name sorted-emails) result))))
        (reverse result))))
```

## Erlang

```erlang
-spec accounts_merge(Accounts :: [[unicode:unicode_binary()]]) -> [[unicode:unicode_binary()]].
accounts_merge(Accounts) ->
    {EmailToId, EmailToName, Parent, Size, _NextId} =
        lists:foldl(fun process_account/2,
                    {#{}, #{}, #{}, #{}, 0},
                    Accounts),
    Ids = maps:keys(Parent),
    FinalParent = lists:foldl(fun(Id, PAcc) ->
                                    {_, NewP} = find(Id, PAcc),
                                    NewP
                               end,
                               Parent,
                               Ids),
    Groups = maps:fold(fun(Email, Id, GAcc) ->
                           Root = maps:get(Id, FinalParent),
                           Emails = maps:get(Root, GAcc, []),
                           maps:put(Root, [Email | Emails], GAcc)
                       end,
                       #{},
                       EmailToId),
    lists:map(fun({_Root, Unsorted}) ->
                  Sorted = lists:sort(Unsorted),
                  Name = maps:get(hd(Sorted), EmailToName),
                  [Name | Sorted]
              end,
              maps:to_list(Groups)).

process_account([Name | Emails], {EmailToId, EmailToName, Parent, Size, NextId}) ->
    case Emails of
        [] -> {EmailToId, EmailToName, Parent, Size, NextId};
        [First|Rest] ->
            {E2I1, P1, S1, N1} = ensure_email(First, EmailToId, Parent, Size, NextId),
            EmailToName1 = maps:put(First, Name, EmailToName),
            {E2IFinal, PFinal, SFinal, NFinal, EmailToNameFinal} =
                lists:foldl(fun(E, {E2IAcc, PAcc, SAcc, NAcc, ENAcc}) ->
                                {E2I2, P2, S2, N2} = ensure_email(E, E2IAcc, PAcc, SAcc, NAcc),
                                EmailToName2 = maps:put(E, Name, ENAcc),
                                Id1 = maps:get(First, E2I2),
                                Id2 = maps:get(E, E2I2),
                                {P3, S3} = union(Id1, Id2, P2, S2),
                                {E2I2, P3, S3, N2, EmailToName2}
                            end,
                            {E2I1, P1, S1, N1, EmailToName1},
                            Rest),
            {E2IFinal, EmailToNameFinal, PFinal, SFinal, NFinal}
    end.

ensure_email(Email, EmailToId, Parent, Size, NextId) ->
    case maps:is_key(Email, EmailToId) of
        true -> {EmailToId, Parent, Size, NextId};
        false ->
            Id = NextId,
            NewEmailToId = maps:put(Email, Id, EmailToId),
            NewParent = maps:put(Id, Id, Parent),
            NewSize = maps:put(Id, 1, Size),
            {NewEmailToId, NewParent, NewSize, NextId + 1}
    end.

union(A, B, Parent, Size) ->
    {RootA, P1} = find(A, Parent),
    {RootB, P2} = find(B, P1),
    if RootA == RootB -> {P2, Size};
       true ->
           SizeA = maps:get(RootA, Size),
           SizeB = maps:get(RootB, Size),
           if SizeA < SizeB ->
                  NewParent = maps:put(RootA, RootB, P2),
                  NewSize = maps:put(RootB, SizeA + SizeB, Size);
              true ->
                  NewParent = maps:put(RootB, RootA, P2),
                  NewSize = maps:put(RootA, SizeA + SizeB, Size)
           end,
           {NewParent, NewSize}
    end.

find(Id, Parent) ->
    ParentId = maps:get(Id, Parent),
    if ParentId == Id -> {Id, Parent};
       true ->
            {Root, UpdatedParent} = find(ParentId, Parent),
            NewParent = maps:put(Id, Root, UpdatedParent),
            {Root, NewParent}
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec accounts_merge(accounts :: [[String.t]]) :: [[String.t]]
  def accounts_merge(accounts) do
    {adjacency, email_to_name} = build_graph(accounts)
    merged = dfs_all(adjacency, email_to_name, MapSet.new(), [])
    Enum.reverse(merged)
  end

  # Build adjacency list and map each email to its owner's name
  defp build_graph(accounts) do
    Enum.reduce(accounts, {%{}, %{}}, fn account, {adj, name_map} ->
      [name | emails] = account

      # associate every email with the name (first occurrence wins)
      name_map =
        Enum.reduce(emails, name_map, fn email, acc ->
          Map.put_new(acc, email, name)
        end)

      case emails do
        [] -> {adj, name_map}
        [first | rest] ->
          adj =
            Enum.reduce(rest, adj, fn e, a ->
              a
              |> Map.update(first, MapSet.new([e]), &MapSet.put(&1, e))
              |> Map.update(e, MapSet.new([first]), &MapSet.put(&1, first))
            end)

          {adj, name_map}
      end
    end)
  end

  # Perform DFS for all emails and collect merged accounts
  defp dfs_all(adjacency, email_to_name, visited, result) do
    Enum.reduce(Map.keys(email_to_name), {visited, result}, fn email, {vis, res} ->
      if MapSet.member?(vis, email) do
        {vis, res}
      else
        {component_emails, new_vis} = dfs_collect(email, adjacency, vis)
        sorted = Enum.sort(component_emails)
        name = Map.fetch!(email_to_name, hd(sorted))
        merged = [name | sorted]
        {new_vis, [merged | res]}
      end
    end)
    |> elem(1)
  end

  # Iterative DFS returning the list of emails in this component and updated visited set
  defp dfs_collect(start, adjacency, visited) do
    do_dfs([start], adjacency, visited, [])
  end

  defp do_dfs([], _adjacency, visited, comp), do: {comp, visited}

  defp do_dfs([node | stack], adjacency, visited, comp) do
    if MapSet.member?(visited, node) do
      do_dfs(stack, adjacency, visited, comp)
    else
      visited = MapSet.put(visited, node)

      neighbors = Map.get(adjacency, node, MapSet.new())

      new_stack =
        Enum.reduce(neighbors, stack, fn nb, acc ->
          if MapSet.member?(visited, nb), do: acc, else: [nb | acc]
        end)

      do_dfs(new_stack, adjacency, visited, [node | comp])
    end
  end
end
```
