# 1948. Delete Duplicate Folders in System

## Cpp

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    struct Node {
        unordered_map<string, Node*> child;
        string ser; // serialization of subtree rooted at this node
    };
    
    vector<vector<string>> deleteDuplicateFolder(vector<vector<string>>& paths) {
        Node* root = new Node();
        // Build trie
        for (const auto& p : paths) {
            Node* cur = root;
            for (const string& name : p) {
                if (!cur->child.count(name)) cur->child[name] = new Node();
                cur = cur->child[name];
            }
        }
        
        unordered_map<string, int> cnt;
        // Post-order serialization
        function<string(Node*)> dfs = [&](Node* node) -> string {
            vector<string> parts;
            for (auto& kv : node->child) {
                const string& name = kv.first;
                Node* chNode = kv.second;
                string childSer = dfs(chNode);
                parts.push_back(name + "(" + childSer + ")");
            }
            sort(parts.begin(), parts.end());
            string curSer;
            for (const string& s : parts) curSer += s;
            node->ser = curSer;
            ++cnt[curSer];
            return curSer;
        };
        dfs(root);
        
        vector<vector<string>> ans;
        vector<string> curPath;
        function<void(Node*)> collect = [&](Node* node) {
            for (auto& kv : node->child) {
                const string& name = kv.first;
                Node* chNode = kv.second;
                if (cnt[chNode->ser] > 1) continue; // duplicate subtree, skip entirely
                curPath.push_back(name);
                ans.push_back(curPath);
                collect(chNode);
                curPath.pop_back();
            }
        };
        collect(root);
        return ans;
    }
};
```

## Java

```java
import java.util.*;

class Solution {
    private static class Node {
        String name;
        Map<String, Node> children = new HashMap<>();
        String serial;
        Node(String name) { this.name = name; }
    }

    public List<List<String>> deleteDuplicateFolder(List<List<String>> paths) {
        Node root = new Node("");
        // Build trie
        for (List<String> path : paths) {
            Node cur = root;
            for (String folder : path) {
                cur = cur.children.computeIfAbsent(folder, k -> new Node(k));
            }
        }

        Map<String, Integer> freq = new HashMap<>();
        computeSerial(root, freq);

        List<List<String>> ans = new ArrayList<>();
        collect(root, new ArrayList<>(), freq, ans);
        return ans;
    }

    private String computeSerial(Node node, Map<String, Integer> freq) {
        if (node.children.isEmpty()) {
            node.serial = "";
            freq.put("", freq.getOrDefault("", 0) + 1);
            return "";
        }
        List<String> parts = new ArrayList<>();
        for (Map.Entry<String, Node> entry : node.children.entrySet()) {
            String childSerial = computeSerial(entry.getValue(), freq);
            parts.add(entry.getKey() + "(" + childSerial + ")");
        }
        Collections.sort(parts);
        StringBuilder sb = new StringBuilder();
        for (String p : parts) sb.append(p);
        node.serial = sb.toString();
        freq.put(node.serial, freq.getOrDefault(node.serial, 0) + 1);
        return node.serial;
    }

    private void collect(Node node, List<String> path,
                         Map<String, Integer> freq,
                         List<List<String>> ans) {
        for (Map.Entry<String, Node> entry : node.children.entrySet()) {
            Node child = entry.getValue();
            if (freq.getOrDefault(child.serial, 0) > 1) {
                // duplicate subtree, skip entirely
                continue;
            }
            List<String> newPath = new ArrayList<>(path);
            newPath.add(entry.getKey());
            ans.add(newPath);
            collect(child, newPath, freq, ans);
        }
    }
}
```

## Python

```python
import sys

sys.setrecursionlimit(1 << 25)


class Node:
    __slots__ = ("children", "serial")

    def __init__(self):
        self.children = {}
        self.serial = ""


class Solution(object):
    def deleteDuplicateFolder(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: List[List[str]]
        """
        root = Node()
        # Build trie
        for p in paths:
            cur = root
            for name in p:
                if name not in cur.children:
                    cur.children[name] = Node()
                cur = cur.children[name]

        serial_count = {}

        def serialize(node):
            parts = []
            for name, child in node.children.items():
                child_serial = serialize(child)
                parts.append(name + '(' + child_serial + ')')
            parts.sort()
            s = ''.join(parts)
            serial_count[s] = serial_count.get(s, 0) + 1
            node.serial = s
            return s

        serialize(root)

        ans = []

        def collect(node, path):
            for name, child in node.children.items():
                if serial_count[child.serial] > 1:
                    continue
                ans.append(path + [name])
                collect(child, path + [name])

        collect(root, [])
        return ans
```

## Python3

```python
from typing import List, Dict

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        class Node:
            __slots__ = ('name', 'children', 'ser')
            def __init__(self, name: str):
                self.name = name
                self.children: Dict[str, Node] = {}
                self.ser: str = ''
        
        root = Node("")
        # Build trie
        for p in paths:
            cur = root
            for folder in p:
                if folder not in cur.children:
                    cur.children[folder] = Node(folder)
                cur = cur.children[folder]
        
        from collections import defaultdict
        cnt = defaultdict(int)
        
        # Post-order serialization
        def dfs1(node: Node) -> str:
            parts = []
            for child in node.children.values():
                child_ser = dfs1(child)
                parts.append(child.name + '(' + child_ser + ')')
            parts.sort()
            node.ser = ''.join(parts)
            cnt[node.ser] += 1
            return node.ser
        
        dfs1(root)
        
        ans: List[List[str]] = []
        # Collect non-duplicate paths
        def dfs2(node: Node, path: List[str]) -> None:
            for child in node.children.values():
                if child.ser != '' and cnt[child.ser] > 1:
                    continue  # skip this subtree entirely
                ans.append(path + [child.name])
                dfs2(child, path + [child.name])
        
        dfs2(root, [])
        return ans
```

## C

```c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct Node {
    char *name;
    struct Node **children;
    int childCount;
    int childCap;
    char *serial;
} Node;

/* ---------- hash map for serialization counts ---------- */
#define HASH_SIZE 200003

typedef struct MapNode {
    char *key;
    int cnt;
    struct MapNode *next;
} MapNode;

static MapNode *hashTable[HASH_SIZE];

static unsigned long hashStr(const char *s) {
    unsigned long h = 5381;
    while (*s) {
        h = ((h << 5) + h) + (unsigned char)*s++;
    }
    return h;
}

static void mapInc(char *key) {
    unsigned long h = hashStr(key) % HASH_SIZE;
    MapNode *node = hashTable[h];
    while (node) {
        if (strcmp(node->key, key) == 0) {
            node->cnt++;
            return;
        }
        node = node->next;
    }
    MapNode *newnode = (MapNode *)malloc(sizeof(MapNode));
    newnode->key = key;
    newnode->cnt = 1;
    newnode->next = hashTable[h];
    hashTable[h] = newnode;
}

static int mapGet(const char *key) {
    unsigned long h = hashStr(key) % HASH_SIZE;
    MapNode *node = hashTable[h];
    while (node) {
        if (strcmp(node->key, key) == 0) return node->cnt;
        node = node->next;
    }
    return 0;
}

/* ---------- Trie utilities ---------- */
static Node *newNode(const char *name) {
    Node *n = (Node *)malloc(sizeof(Node));
    n->name = name ? strdup(name) : NULL;
    n->children = NULL;
    n->childCount = 0;
    n->childCap = 0;
    n->serial = NULL;
    return n;
}

static Node *getOrCreateChild(Node *parent, const char *name) {
    for (int i = 0; i < parent->childCount; ++i) {
        if (strcmp(parent->children[i]->name, name) == 0)
            return parent->children[i];
    }
    Node *child = newNode(name);
    if (parent->childCount == parent->childCap) {
        int nc = parent->childCap ? parent->childCap * 2 : 4;
        parent->children = (Node **)realloc(parent->children, nc * sizeof(Node *));
        parent->childCap = nc;
    }
    parent->children[parent->childCount++] = child;
    return child;
}

/* ---------- Serialization ---------- */
static int cmpStr(const void *a, const void *b) {
    const char *sa = *(const char **)a;
    const char *sb = *(const char **)b;
    return strcmp(sa, sb);
}

static char *serialize(Node *node) {
    for (int i = 0; i < node->childCount; ++i)
        serialize(node->children[i]);

    if (node->childCount == 0) {
        node->serial = strdup("");
        return node->serial;
    }

    char **reps = (char **)malloc(node->childCount * sizeof(char *));
    size_t totalLen = 0;
    for (int i = 0; i < node->childCount; ++i) {
        Node *ch = node->children[i];
        size_t len = strlen(ch->name) + 2 + strlen(ch->serial);
        char *s = (char *)malloc(len + 1);
        sprintf(s, "%s(%s)", ch->name, ch->serial);
        reps[i] = s;
        totalLen += len;
    }

    qsort(reps, node->childCount, sizeof(char *), cmpStr);

    char *res = (char *)malloc(totalLen + 1);
    char *p = res;
    for (int i = 0; i < node->childCount; ++i) {
        size_t l = strlen(reps[i]);
        memcpy(p, reps[i], l);
        p += l;
        free(reps[i]);
    }
    *p = '\0';
    free(reps);

    node->serial = res;
    mapInc(res);               // count only non‑leaf nodes
    return res;
}

/* ---------- Collect answer ---------- */
static void dfsCollect(Node *node, char **pathArr, int depth,
                       char ***ansPtr, int *sizePtr, int *capPtr,
                       int **colSizes) {
    if (node->name != NULL) {  // not root
        if (mapGet(node->serial) > 1)
            return;             // duplicate subtree, skip entirely

        if (*sizePtr >= *capPtr) {
            *capPtr *= 2;
            *ansPtr = (char ***)realloc(*ansPtr, (*capPtr) * sizeof(char **));
            *colSizes = (int *)realloc(*colSizes, (*capPtr) * sizeof(int));
        }
        char **curPath = (char **)malloc(depth * sizeof(char *));
        for (int i = 0; i < depth; ++i)
            curPath[i] = pathArr[i];
        (*ansPtr)[*sizePtr] = curPath;
        (*colSizes)[*sizePtr] = depth;
        (*sizePtr)++;
    }

    for (int i = 0; i < node->childCount; ++i) {
        Node *ch = node->children[i];
        pathArr[depth] = ch->name;
        dfsCollect(ch, pathArr, depth + 1, ansPtr, sizePtr, capPtr, colSizes);
    }
}

/* ---------- Main function ---------- */
char*** deleteDuplicateFolder(char*** paths, int pathsSize, int* pathsColSize,
                              int* returnSize, int** returnColumnSizes) {
    Node *root = newNode(NULL);

    /* Build trie */
    for (int i = 0; i < pathsSize; ++i) {
        Node *cur = root;
        for (int j = 0; j < pathsColSize[i]; ++j) {
            cur = getOrCreateChild(cur, paths[i][j]);
        }
    }

    /* Serialize and count */
    serialize(root);

    /* Prepare answer containers */
    int cap = 128;
    int sz = 0;
    char ***ans = (char ***)malloc(cap * sizeof(char **));
    int *colSizes = (int *)malloc(cap * sizeof(int));

    /* Collect non‑duplicate paths */
    int maxDepth = 505;   // per constraints
    char **curPath = (char **)malloc(maxDepth * sizeof(char *));
    dfsCollect(root, curPath, 0, &ans, &sz, &cap, &colSizes);
    free(curPath);

    *returnSize = sz;
    *returnColumnSizes = colSizes;
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    private class Node {
        public string Name;
        public Dictionary<string, Node> Children = new Dictionary<string, Node>();
        public string Serial;
        public Node(string name) { Name = name; }
    }

    public IList<IList<string>> DeleteDuplicateFolder(IList<IList<string>> paths) {
        // Build trie
        var root = new Node("");
        foreach (var p in paths) {
            var cur = root;
            foreach (var folder in p) {
                if (!cur.Children.ContainsKey(folder))
                    cur.Children[folder] = new Node(folder);
                cur = cur.Children[folder];
            }
        }

        // Serialize subtrees and count frequencies
        var freq = new Dictionary<string, int>();
        Serialize(root, freq);

        // Collect remaining paths
        var ans = new List<IList<string>>();
        var path = new List<string>();
        Collect(root, path, freq, ans);
        return ans;
    }

    private string Serialize(Node node, Dictionary<string, int> freq) {
        if (node.Children.Count == 0) {
            node.Serial = "";
            return "";
        }
        var parts = new List<string>();
        foreach (var kvp in node.Children) {
            var child = kvp.Value;
            string childSer = Serialize(child, freq);
            parts.Add(kvp.Key + "(" + childSer + ")");
        }
        parts.Sort(StringComparer.Ordinal);
        string ser = string.Concat(parts);
        node.Serial = ser;
        if (ser.Length > 0) {
            if (!freq.ContainsKey(ser)) freq[ser] = 0;
            freq[ser]++;
        }
        return ser;
    }

    private void Collect(Node node, List<string> curPath,
                         Dictionary<string, int> freq,
                         List<IList<string>> ans) {
        foreach (var child in node.Children.Values) {
            if (child.Serial.Length > 0 && freq[child.Serial] > 1) {
                // duplicate folder, skip this subtree
                continue;
            }
            curPath.Add(child.Name);
            ans.Add(new List<string>(curPath));
            Collect(child, curPath, freq, ans);
            curPath.RemoveAt(curPath.Count - 1);
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {string[][]} paths
 * @return {string[][]}
 */
var deleteDuplicateFolder = function(paths) {
    class Node {
        constructor(name) {
            this.name = name;
            this.children = new Map(); // name -> Node
            this.serial = '';
        }
    }

    const root = new Node('');

    // Build trie
    for (const p of paths) {
        let cur = root;
        for (const folder of p) {
            if (!cur.children.has(folder)) {
                cur.children.set(folder, new Node(folder));
            }
            cur = cur.children.get(folder);
        }
    }

    const freq = new Map(); // serialization -> count

    // Post-order serialization
    function dfs(node) {
        if (node.children.size === 0) {
            node.serial = '';
            return '';
        }
        const parts = [];
        for (const [name, child] of node.children) {
            const childSer = dfs(child);
            parts.push(name + '(' + childSer + ')');
        }
        parts.sort(); // order-independent
        const ser = parts.join('');
        node.serial = ser;
        freq.set(ser, (freq.get(ser) || 0) + 1);
        return ser;
    }

    dfs(root);

    const ans = [];

    // Collect non-duplicate paths
    function collect(node, path) {
        if (node !== root) {
            if (node.serial && freq.get(node.serial) > 1) {
                return; // skip this subtree
            }
            ans.push([...path]); // record current folder path
        }
        for (const [name, child] of node.children) {
            path.push(name);
            collect(child, path);
            path.pop();
        }
    }

    collect(root, []);
    return ans;
};
```

## Typescript

```typescript
function deleteDuplicateFolder(paths: string[][]): string[][] {
    class Node {
        name: string;
        children: Map<string, Node>;
        serial: string = '';
        constructor(name: string) {
            this.name = name;
            this.children = new Map();
        }
    }

    const root = new Node('');
    // Build trie
    for (const p of paths) {
        let cur = root;
        for (const folder of p) {
            if (!cur.children.has(folder)) {
                cur.children.set(folder, new Node(folder));
            }
            cur = cur.children.get(folder)!;
        }
    }

    const freq = new Map<string, number>();

    // Post-order serialization
    function serialize(node: Node): string {
        const parts: string[] = [];
        for (const [childName, childNode] of node.children) {
            const childSer = serialize(childNode);
            parts.push(childName + '(' + childSer + ')');
        }
        parts.sort();
        const ser = parts.join('');
        node.serial = ser;
        freq.set(ser, (freq.get(ser) ?? 0) + 1);
        return ser;
    }

    serialize(root);

    const result: string[][] = [];

    // Collect non-duplicate paths
    function collect(node: Node, path: string[]): void {
        for (const [childName, childNode] of node.children) {
            if ((freq.get(childNode.serial) ?? 0) > 1) continue; // duplicate subtree
            const newPath = [...path, childName];
            result.push(newPath);
            collect(childNode, newPath);
        }
    }

    collect(root, []);
    return result;
}
```

## Php

```php
class Solution {
    /**
     * @param String[][] $paths
     * @return String[][]
     */
    function deleteDuplicateFolder($paths) {
        // Build trie
        $root = new Node('');
        foreach ($paths as $p) {
            $cur = $root;
            foreach ($p as $folder) {
                if (!isset($cur->children[$folder])) {
                    $cur->children[$folder] = new Node($folder);
                }
                $cur = $cur->children[$folder];
            }
        }

        // First pass: compute serialization and frequency
        $freq = [];
        $this->dfsSerial($root, $freq);

        // Second pass: collect unique paths
        $ans = [];
        $this->dfsCollect($root, [], $freq, $ans);
        return $ans;
    }

    private function dfsSerial($node, &$freq) {
        if (empty($node->children)) {
            $node->serial = '';
            return '';
        }
        $parts = [];
        foreach ($node->children as $childName => $childNode) {
            $childSer = $this->dfsSerial($childNode, $freq);
            $parts[] = $childName . '(' . $childSer . ')';
        }
        sort($parts, SORT_STRING);
        $serial = implode('', $parts);
        $node->serial = $serial;
        // count only non‑leaf nodes
        $freq[$serial] = ($freq[$serial] ?? 0) + 1;
        return $serial;
    }

    private function dfsCollect($node, $path, &$freq, &$ans) {
        foreach ($node->children as $childName => $childNode) {
            // If this folder is duplicated (appears more than once), skip it entirely
            if (!empty($childNode->children) && ($freq[$childNode->serial] ?? 0) > 1) {
                continue;
            }
            $newPath = array_merge($path, [$childName]);
            $ans[] = $newPath;
            $this->dfsCollect($childNode, $newPath, $freq, $ans);
        }
    }
}

class Node {
    public string $name;
    /** @var Node[] */
    public array $children = [];
    public string $serial = '';

    public function __construct(string $name) {
        $this->name = $name;
    }
}
```

## Swift

```swift
import Foundation

class Node {
    let name: String
    var children: [String: Node] = [:]
    var serial: String = ""
    init(name: String) {
        self.name = name
    }
}

class Solution {
    private var serialCount = [String: Int]()
    
    func deleteDuplicateFolder(_ paths: [[String]]) -> [[String]] {
        let root = Node(name: "")
        // Build trie
        for path in paths {
            var cur = root
            for folder in path {
                if cur.children[folder] == nil {
                    cur.children[folder] = Node(name: folder)
                }
                cur = cur.children[folder]!
            }
        }
        // Serialize subtrees and count occurrences
        _ = serialize(root)
        
        var result = [[String]]()
        for child in root.children.values {
            dfsCollect(child, [child.name], &result)
        }
        return result
    }
    
    private func serialize(_ node: Node) -> String {
        var parts = [String]()
        for child in node.children.values {
            let childSer = serialize(child)
            child.serial = childSer
            let part = child.name + "(" + childSer + ")"
            parts.append(part)
        }
        parts.sort()
        let res = parts.joined()
        node.serial = res
        serialCount[res, default: 0] += 1
        return res
    }
    
    private func dfsCollect(_ node: Node, _ path: [String], _ ans: inout [[String]]) {
        if let cnt = serialCount[node.serial], cnt > 1 {
            // Duplicate folder, skip it and its entire subtree
            return
        }
        ans.append(path)
        for child in node.children.values {
            var newPath = path
            newPath.append(child.name)
            dfsCollect(child, newPath, &ans)
        }
    }
}
```

## Kotlin

```kotlin
import java.util.StringTokenizer

class Solution {
    private class Node(val name: String) {
        val children: MutableMap<String, Node> = mutableMapOf()
        var serial: String = ""
    }

    private val countMap = HashMap<String, Int>()

    fun deleteDuplicateFolder(paths: List<List<String>>): List<List<String>> {
        val root = Node("")
        // Build trie
        for (path in paths) {
            var cur = root
            for (folder in path) {
                cur = cur.children.computeIfAbsent(folder) { Node(folder) }
            }
        }

        // Serialize and count
        serialize(root)

        // Collect remaining paths
        val result = mutableListOf<List<String>>()
        val currentPath = mutableListOf<String>()
        collect(root, currentPath, result)
        return result
    }

    private fun serialize(node: Node): String {
        if (node.children.isEmpty()) {
            node.serial = ""
            countMap[node.serial] = countMap.getOrDefault(node.serial, 0) + 1
            return node.serial
        }
        val reps = mutableListOf<String>()
        for ((name, child) in node.children) {
            val childSer = serialize(child)
            reps.add(name + "(" + childSer + ")")
        }
        reps.sort()
        val sb = StringBuilder()
        for (s in reps) sb.append(s)
        node.serial = sb.toString()
        countMap[node.serial] = countMap.getOrDefault(node.serial, 0) + 1
        return node.serial
    }

    private fun collect(node: Node, path: MutableList<String>, res: MutableList<List<String>>) {
        for ((name, child) in node.children) {
            // If the folder is a duplicate (has children and appears more than once), skip it entirely
            if (child.children.isNotEmpty() && countMap.getOrDefault(child.serial, 0) > 1) continue
            path.add(name)
            res.add(ArrayList(path))
            collect(child, path, res)
            path.removeAt(path.size - 1)
        }
    }
}
```

## Dart

```dart
class Solution {
  List<List<String>> deleteDuplicateFolder(List<List<String>> paths) {
    // Trie node definition
    class Node {
      Map<String, Node> children = {};
      String serial = '';
      Node();
    }

    final root = Node();

    // Build the trie
    for (var path in paths) {
      var cur = root;
      for (var folder in path) {
        cur = cur.children.putIfAbsent(folder, () => Node());
      }
    }

    // Map to count serialization frequencies
    final Map<String, int> freq = {};

    // Post-order serialization
    String serialize(Node node) {
      if (node.children.isEmpty) {
        node.serial = '';
        freq[''] = (freq[''] ?? 0) + 1;
        return '';
      }
      List<String> parts = [];
      for (var entry in node.children.entries) {
        String childSer = serialize(entry.value);
        parts.add('${entry.key}($childSer)');
      }
      parts.sort();
      String ser = parts.join();
      node.serial = ser;
      freq[ser] = (freq[ser] ?? 0) + 1;
      return ser;
    }

    serialize(root);

    // Collect remaining paths
    List<List<String>> ans = [];

    void collect(Node node, List<String> curPath) {
      for (var entry in node.children.entries) {
        var child = entry.value;
        if ((freq[child.serial] ?? 0) > 1) continue; // duplicate subtree, skip
        var newPath = List<String>.from(curPath);
        newPath.add(entry.key);
        ans.add(newPath);
        collect(child, newPath);
      }
    }

    collect(root, []);

    return ans;
  }
}
```

## Golang

```go
package main

import (
	"sort"
	"strings"
)

type Node struct {
	name     string
	children map[string]*Node
	serial   string
}

func newNode(name string) *Node {
	return &Node{
		name:     name,
		children: make(map[string]*Node),
	}
}

// post-order serialization, filling cnt for non‑empty serializations
func dfsSerial(node *Node, cnt map[string]int) string {
	if len(node.children) == 0 {
		node.serial = ""
		return ""
	}
	parts := make([]string, 0, len(node.children))
	for _, child := range node.children {
		childSer := dfsSerial(child, cnt)
		part := child.name + "(" + childSer + ")"
		parts = append(parts, part)
	}
	sort.Strings(parts)
	var sb strings.Builder
	for _, p := range parts {
		sb.WriteString(p)
	}
	s := sb.String()
	node.serial = s
	if s != "" {
		cnt[s]++
	}
	return s
}

// collect unique paths, skipping subtrees whose serialization is duplicated
func collect(node *Node, path []string, cnt map[string]int, ans *[][]string) {
	for _, child := range node.children {
		newPath := append(path, child.name)
		if child.serial != "" && cnt[child.serial] > 1 {
			continue // skip this subtree entirely
		}
		cp := make([]string, len(newPath))
		copy(cp, newPath)
		*ans = append(*ans, cp)
		collect(child, newPath, cnt, ans)
	}
}

func deleteDuplicateFolder(paths [][]string) [][]string {
	root := newNode("")
	for _, p := range paths {
		cur := root
		for _, name := range p {
			if nxt, ok := cur.children[name]; ok {
				cur = nxt
			} else {
				nxt = newNode(name)
				cur.children[name] = nxt
				cur = nxt
			}
		}
	}
	cnt := make(map[string]int)
	dfsSerial(root, cnt)

	var ans [][]string
	collect(root, []string{}, cnt, &ans)
	return ans
}
```

## Ruby

```ruby
def delete_duplicate_folder(paths)
  class Node
    attr_accessor :name, :children, :serial
    def initialize(name)
      @name = name
      @children = {}
      @serial = nil
    end
  end

  root = Node.new("")
  paths.each do |p|
    cur = root
    p.each do |folder|
      cur.children[folder] ||= Node.new(folder)
      cur = cur.children[folder]
    end
  end

  counter = Hash.new(0)

  dfs_serial = nil
  dfs_serial = ->(node) {
    if node.children.empty?
      node.serial = ""
    else
      child_strs = []
      node.children.each_value do |child|
        dfs_serial.call(child)
        child_strs << "#{child.name}(#{child.serial})"
      end
      child_strs.sort!
      node.serial = child_strs.join
    end
    counter[node.serial] += 1
  }
  dfs_serial.call(root)

  ans = []
  dfs_collect = nil
  dfs_collect = ->(node, path) {
    node.children.each_value do |child|
      if counter[child.serial] > 1
        next
      else
        new_path = path + [child.name]
        ans << new_path
        dfs_collect.call(child, new_path)
      end
    end
  }
  dfs_collect.call(root, [])
  ans
end
```

## Scala

```scala
import scala.collection.mutable

object Solution {
  def deleteDuplicateFolder(paths: List[List[String]]): List[List[String]] = {
    class Node(val name: String) {
      val children: mutable.Map[String, Node] = mutable.Map()
      var serial: String = ""
    }

    // Build the trie
    val root = new Node("")
    for (p <- paths) {
      var cur = root
      for (folder <- p) {
        cur = cur.children.getOrElseUpdate(folder, new Node(folder))
      }
    }

    // Map from serialization to its frequency
    val freq = mutable.Map[String, Int]().withDefaultValue(0)

    // Post-order traversal to compute serialization
    def dfsSerial(node: Node): String = {
      val parts = mutable.ArrayBuffer[String]()
      for ((childName, childNode) <- node.children) {
        val childSer = dfsSerial(childNode)
        parts += s"$childName($childSer)"
      }
      val combined = if (parts.isEmpty) "" else parts.sorted.mkString
      node.serial = combined
      freq(combined) = freq(combined) + 1
      combined
    }

    dfsSerial(root)

    // Collect remaining paths, skipping duplicated subtrees
    val result = mutable.Buffer[List[String]]()

    def collect(node: Node, path: List[String]): Unit = {
      if (node != root && freq(node.serial) > 1) return
      if (node != root) {
        val newPath = path :+ node.name
        result += newPath
        for ((_, child) <- node.children) collect(child, newPath)
      } else {
        for ((_, child) <- node.children) collect(child, Nil)
      }
    }

    collect(root, Nil)

    result.toList
  }
}
```

## Rust

```rust
use std::collections::HashMap;

#[derive(Default)]
struct Node {
    children: HashMap<String, Box<Node>>,
    serial: String,
}

impl Node {
    fn new() -> Self {
        Node {
            children: HashMap::new(),
            serial: String::new(),
        }
    }
}

pub struct Solution;

impl Solution {
    pub fn delete_duplicate_folder(paths: Vec<Vec<String>>) -> Vec<Vec<String>> {
        // Build trie
        let mut root = Node::new();
        for path in paths.iter() {
            let mut cur = &mut root;
            for name in path {
                cur = cur
                    .children
                    .entry(name.clone())
                    .or_insert_with(|| Box::new(Node::new()));
            }
        }

        // First pass: compute serialization and frequency
        let mut freq: HashMap<String, i32> = HashMap::new();
        Self::dfs_serial(&mut root, &mut freq);

        // Second pass: collect remaining paths
        let mut ans: Vec<Vec<String>> = Vec::new();
        let mut cur_path: Vec<String> = Vec::new();
        Self::collect(&root, &mut cur_path, &mut ans, &freq);
        ans
    }

    fn dfs_serial(node: &mut Node, freq: &mut HashMap<String, i32>) -> String {
        let mut reps: Vec<String> = Vec::new();
        for (name, child) in node.children.iter_mut() {
            let child_ser = Self::dfs_serial(child, freq);
            let s = format!("{}({})", name, child_ser);
            reps.push(s);
        }
        reps.sort_unstable();
        let mut serial = String::new();
        for s in reps.iter() {
            serial.push_str(s);
        }
        node.serial = serial.clone();
        *freq.entry(serial.clone()).or_insert(0) += 1;
        serial
    }

    fn collect(
        node: &Node,
        path: &mut Vec<String>,
        ans: &mut Vec<Vec<String>>,
        freq: &HashMap<String, i32>,
    ) {
        for (name, child) in node.children.iter() {
            let cnt = *freq.get(&child.serial).unwrap_or(&0);
            if cnt > 1 && !child.children.is_empty() {
                // duplicate folder, skip entire subtree
                continue;
            }
            path.push(name.clone());
            ans.push(path.clone());
            Self::collect(child, path, ans, freq);
            path.pop();
        }
    }
}
```

## Racket

```racket
#lang racket
(require racket/list)

(struct node (name children ser) #:mutable)

(define (serialize n ser-count)
  (if (hash-empty? (node-children n))
      (begin
        (set-node-ser! n "")
        (hash-set! ser-count "" (+ 1 (hash-ref ser-count "" 0)))
        "")
      (let* ([child-reprs
               (for/list ([(name child) (in-hash (node-children n))])
                 (string-append name "(" (serialize child ser-count) ")"))]
             [sorted (sort child-reprs string<?)]
             [s (apply string-append sorted)])
        (hash-set! ser-count s (+ 1 (hash-ref ser-count s 0)))
        (set-node-ser! n s)
        s))))

(define (collect n prefix ser-count)
  (let ([s (node-ser n)])
    (if (> (hash-ref ser-count s) 1)
        '()
        (let* ([new-prefix (append prefix (list (node-name n)))]
               [subpaths
                (apply append
                       (map (lambda (child) (collect child new-prefix ser-count))
                            (hash-values (node-children n))))])
          (cons new-prefix subpaths)))))

(define/contract (delete-duplicate-folder paths)
  (-> (listof (listof string?)) (listof (listof string?)))
  (let* ([root (node "" (make-hash) #f)]
         [insert-path
          (lambda (p)
            (let loop ((cur root) (parts p))
              (unless (null? parts)
                (define name (car parts))
                (define children (node-children cur))
                (define child (hash-ref children name #f))
                (when (not child)
                  (set! child (node name (make-hash) #f))
                  (hash-set! children name child))
                (loop child (cdr parts)))) )])
    (for-each insert-path paths)
    (define ser-count (make-hash))
    (serialize root ser-count)
    (apply append
           (map (lambda (child) (collect child '() ser-count))
                (hash-values (node-children root)))))
```

## Erlang

```erlang
-spec delete_duplicate_folder(Paths :: [[unicode:unicode_binary()]]) -> [[unicode:unicode_binary()]].
delete_duplicate_folder(Paths) ->
    Root = #{name => <<>>, children => #{}},
    Root1 = lists:foldl(fun(Path, AccRoot) -> insert_path(AccRoot, Path) end, Root, Paths),
    {_RootSerial, RootWithSerial, FreqMap} = compute_serial(Root1, #{}),
    collect_from_root(RootWithSerial, FreqMap).

%% Insert a single path into the trie
-spec insert_path(Node :: map(), Path :: [unicode:unicode_binary()]) -> map().
insert_path(Node, []) ->
    Node;
insert_path(#{children := Children} = Node, [Name | Rest]) ->
    Child = maps:get(Name, Children, #{name => Name, children => #{}}),
    UpdatedChild = insert_path(Child, Rest),
    NewChildren = maps:put(Name, UpdatedChild, Children),
    Node#{children => NewChildren}.

%% Post-order traversal to compute serialization and frequency map
-spec compute_serial(Node :: map(), FreqMap :: map()) -> {binary(), map(), map()}.
compute_serial(#{children := Children} = Node, FreqMap) ->
    case maps:size(Children) of
        0 ->
            Serial = <<>>,
            Count = maps:get(Serial, FreqMap, 0) + 1,
            NewFreq = maps:put(Serial, Count, FreqMap),
            UpdatedNode = Node#{serial => Serial},
            {Serial, UpdatedNode, NewFreq};
        _ ->
            ChildList = maps:to_list(Children), % [{Name, ChildNode}]
            {Strs, UpdatedChildren, FreqAfter} = process_children(ChildList, [], #{}, FreqMap),
            SortedStrs = lists:sort(Strs),
            Serial = iolist_to_binary(SortedStrs),
            Count = maps:get(Serial, FreqAfter, 0) + 1,
            NewFreq = maps:put(Serial, Count, FreqAfter),
            UpdatedNode = Node#{serial => Serial, children => UpdatedChildren},
            {Serial, UpdatedNode, NewFreq}
    end.

%% Helper to process each child node
-spec process_children(
        ChildList :: [{unicode:unicode_binary(), map()}],
        AccStrs :: [binary()],
        AccMap :: map(),
        FreqMap :: map()
    ) -> {[binary()], map(), map()}.
process_children([], StrAcc, MapAcc, Freq) ->
    {StrAcc, MapAcc, Freq};
process_children([{Name, ChildNode} | Rest], StrAcc, MapAcc, Freq) ->
    {ChildSerial, UpdatedChild, NewFreq} = compute_serial(ChildNode, Freq),
    ChildStr = << Name/binary, "(", ChildSerial/binary, ")" >>,
    UpdatedMap = maps:put(Name, UpdatedChild, MapAcc),
    process_children(Rest, [ChildStr | StrAcc], UpdatedMap, NewFreq).

%% Collect remaining paths starting from root's children
-spec collect_from_root(Root :: map(), FreqMap :: map()) -> [[unicode:unicode_binary()]].
collect_from_root(#{children := Children}, FreqMap) ->
    lists:foldl(
        fun({_Name, ChildNode}, Acc) ->
            Acc ++ collect_paths(ChildNode, [], FreqMap)
        end,
        [],
        maps:to_list(Children)
    ).

%% Recursive collection of paths, skipping duplicates
-spec collect_paths(Node :: map(), Prefix :: [unicode:unicode_binary()], FreqMap :: map()) -> [[unicode:unicode_binary()]].
collect_paths(#{name := Name, children := Children, serial := Serial}, Prefix, FreqMap) ->
    case maps:get(Serial, FreqMap, 0) > 1 of
        true ->
            []; % skip this subtree
        false ->
            NewPath = Prefix ++ [Name],
            Current = [NewPath],
            SubPaths = lists:foldl(
                fun({_ChildName, ChildNode}, Acc) ->
                    Acc ++ collect_paths(ChildNode, NewPath, FreqMap)
                end,
                [],
                maps:to_list(Children)
            ),
            Current ++ SubPaths
    end.
```

## Elixir

```elixir
defmodule Solution do
  @spec delete_duplicate_folder(paths :: [[String.t]]) :: [[String.t]]
  def delete_duplicate_folder(paths) do
    root = Enum.reduce(paths, %{children: %{}, serial: nil}, fn p, acc ->
      insert_path(acc, p)
    end)

    {_root_serial, root_updated, freq_map} = dfs_serialize(root, %{})

    collect(root_updated, [], freq_map, [])
  end

  defp insert_path(node, []), do: node

  defp insert_path(%{children: children}=node, [folder | rest]) do
    child = Map.get(children, folder, %{children: %{}, serial: nil})
    updated_child = insert_path(child, rest)
    %{node | children: Map.put(children, folder, updated_child)}
  end

  defp dfs_serialize(node, freq) do
    {new_children, freq2} =
      Enum.reduce(node.children, {%{}, freq}, fn {name, child_node},
                                                {acc_children, acc_freq} ->
        {_, updated_child, new_acc_freq} = dfs_serialize(child_node, acc_freq)
        {Map.put(acc_children, name, updated_child), new_acc_freq}
      end)

    child_strings =
      Enum.map(new_children, fn {name, child_node} ->
        "#{name}(#{child_node.serial})"
      end)

    sorted = Enum.sort(child_strings)
    serial = Enum.join(sorted)

    freq_updated = Map.update(freq2, serial, 1, &(&1 + 1))

    updated_node = %{node | children: new_children, serial: serial}
    {serial, updated_node, freq_updated}
  end

  defp collect(node, path, freq, acc) do
    if node.serial != "" && Map.get(freq, node.serial, 0) > 1 do
      acc
    else
      new_acc =
        if path == [] do
          acc
        else
          [path | acc]
        end

      Enum.reduce(node.children, new_acc, fn {name, child}, a ->
        collect(child, path ++ [name], freq, a)
      end)
    end
  end
end
```
