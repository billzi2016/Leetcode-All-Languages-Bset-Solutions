# 3321. Find X-Sum of All K-Long Subarrays II

## Cpp

```cpp
class Solution {
public:
    vector<long long> findXSum(vector<int>& nums, int k, int x) {
        using Node = pair<int,int>; // {value, count}
        struct Cmp {
            bool operator()(const Node& a, const Node& b) const {
                if (a.second != b.second) return a.second < b.second; // count asc
                return a.first < b.first; // value asc
            }
        };
        using Set = set<Node, Cmp>;
        
        unordered_map<int, pair<bool, typename Set::iterator>> where; // bool: true if in top
        unordered_map<int,int> cnt;
        Set top, rest;
        long long sumTop = 0;
        
        auto insertNode = [&](int val, int c)->void{
            Node nd = {val,c};
            // initially put into top
            auto it = top.insert(nd).first;
            sumTop += 1LL*val*c;
            where[val] = {true,it};
            if ((int)top.size() > x) {
                auto itMove = top.begin(); // worst in top
                Node mv = *itMove;
                top.erase(itMove);
                sumTop -= 1LL*mv.first*mv.second;
                auto itR = rest.insert(mv).first;
                where[mv.first] = {false,itR};
            }
        };
        
        auto eraseNode = [&](int val, int c)->void{
            // remove node with count c from whichever set it's in
            auto infoIt = where.find(val);
            if (infoIt == where.end()) return;
            bool inTop = infoIt->second.first;
            auto it = infoIt->second.second;
            if (inTop) {
                top.erase(it);
                sumTop -= 1LL*val*c;
            } else {
                rest.erase(it);
            }
            where.erase(infoIt);
        };
        
        auto add = [&](int val)->void{
            int old = cnt[val];
            int nw = old + 1;
            cnt[val] = nw;
            if (old > 0) eraseNode(val, old);
            insertNode(val, nw);
        };
        
        auto remove = [&](int val)->void{
            int old = cnt[val];
            int nw = old - 1;
            eraseNode(val, old);
            if (nw == 0) {
                cnt.erase(val);
            } else {
                cnt[val] = nw;
                insertNode(val, nw);
            }
            // rebalance if top has less than x elements
            while ((int)top.size() < x && !rest.empty()) {
                auto itBest = prev(rest.end()); // best in rest
                Node mv = *itBest;
                rest.erase(itBest);
                auto itT = top.insert(mv).first;
                sumTop += 1LL*mv.first*mv.second;
                where[mv.first] = {true,itT};
            }
        };
        
        int n = nums.size();
        vector<long long> ans;
        for (int i = 0; i < k; ++i) add(nums[i]);
        ans.push_back(sumTop);
        for (int i = k; i < n; ++i) {
            remove(nums[i - k]);
            add(nums[i]);
            ans.push_back(sumTop);
        }
        return ans;
    }
};
```

## Java

```java
class Solution {
    private int limit;
    private TreeSet<Pair> top;
    private TreeSet<Pair> rest;
    private long sumTop;
    private HashMap<Integer, Integer> cnt;

    private static class Pair {
        int val;
        int cnt;
        Pair(int cnt, int val) { this.cnt = cnt; this.val = val; }
        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Pair)) return false;
            Pair p = (Pair) o;
            return val == p.val && cnt == p.cnt;
        }
        @Override
        public int hashCode() {
            return 31 * val + cnt;
        }
    }

    private final Comparator<Pair> comp = (a, b) -> {
        if (a.cnt != b.cnt) return Integer.compare(a.cnt, b.cnt);
        return Integer.compare(a.val, b.val);
    };

    public long[] findXSum(int[] nums, int k, int x) {
        limit = x;
        top = new TreeSet<>(comp);
        rest = new TreeSet<>(comp);
        sumTop = 0L;
        cnt = new HashMap<>();
        int n = nums.length;
        int m = n - k + 1;
        long[] ans = new long[m];
        for (int i = 0; i < k; i++) add(nums[i]);
        ans[0] = sumTop;
        for (int i = k; i < n; i++) {
            remove(nums[i - k]);
            add(nums[i]);
            ans[i - k + 1] = sumTop;
        }
        return ans;
    }

    private void add(int val) {
        int prev = cnt.getOrDefault(val, 0);
        if (prev > 0) {
            Pair old = new Pair(prev, val);
            if (top.remove(old)) {
                sumTop -= (long) old.cnt * old.val;
            } else {
                rest.remove(old);
            }
        }
        int cur = prev + 1;
        cnt.put(val, cur);
        Pair np = new Pair(cur, val);
        top.add(np);
        sumTop += (long) np.cnt * np.val;
        rebalance();
    }

    private void remove(int val) {
        Integer prevObj = cnt.get(val);
        if (prevObj == null) return;
        int prev = prevObj;
        Pair old = new Pair(prev, val);
        if (top.remove(old)) {
            sumTop -= (long) old.cnt * old.val;
        } else {
            rest.remove(old);
        }
        if (prev == 1) {
            cnt.remove(val);
        } else {
            int cur = prev - 1;
            cnt.put(val, cur);
            Pair np = new Pair(cur, val);
            top.add(np);
            sumTop += (long) np.cnt * np.val;
        }
        rebalance();
    }

    private void rebalance() {
        while (top.size() > limit) {
            Pair low = top.first();
            top.remove(low);
            sumTop -= (long) low.cnt * low.val;
            rest.add(low);
        }
        while (top.size() < limit && !rest.isEmpty()) {
            Pair high = rest.last();
            rest.remove(high);
            top.add(high);
            sumTop += (long) high.cnt * high.val;
        }
        while (!top.isEmpty() && !rest.isEmpty()) {
            Pair lowTop = top.first();
            Pair highRest = rest.last();
            if (highRest.cnt > lowTop.cnt ||
                (highRest.cnt == lowTop.cnt && highRest.val > lowTop.val)) {
                top.remove(lowTop);
                sumTop -= (long) lowTop.cnt * lowTop.val;
                rest.remove(highRest);
                top.add(highRest);
                sumTop += (long) highRest.cnt * highRest.val;
                rest.add(lowTop);
            } else break;
        }
    }
}
```

## Python

```python
import heapq
class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(nums)
        cnt = {}
        in_top = {}
        top_min = []      # (freq, val) for elements currently in top set
        rest_max = []     # (-freq, -val) for elements not in top set
        cur_sum = [0]     # sum of values * frequencies for top set
        top_cnt = 0

        # initial window counts
        for i in range(k):
            v = nums[i]
            cnt[v] = cnt.get(v, 0) + 1

        # decide initial top set (most frequent x distinct numbers)
        items = [(f, v) for v, f in cnt.items()]
        items.sort(key=lambda t: (-t[0], -t[1]))
        need = min(x, len(items))
        for i, (f, v) in enumerate(items):
            if i < need:
                in_top[v] = True
                top_cnt += 1
                cur_sum[0] += v * f
                heapq.heappush(top_min, (f, v))
            else:
                in_top[v] = False
                heapq.heappush(rest_max, (-f, -v))

        def clean_top():
            while top_min:
                f, v = top_min[0]
                if cnt.get(v, 0) != f or not in_top.get(v, False):
                    heapq.heappop(top_min)
                else:
                    break

        def clean_rest():
            while rest_max:
                nf, nv = rest_max[0]
                f, v = -nf, -nv
                if cnt.get(v, 0) != f or in_top.get(v, True):
                    heapq.heappop(rest_max)
                else:
                    break

        def get_top_worst():
            clean_top()
            f, v = top_min[0]
            return f, v

        def get_rest_best():
            clean_rest()
            nf, nv = rest_max[0]
            return -nf, -nv

        def change(val, delta):
            nonlocal top_cnt
            old = cnt.get(val, 0)
            new = old + delta

            if old > 0 and in_top.get(val, False):
                cur_sum[0] += val * (new - old)

            if new == 0:
                # removal
                cnt.pop(val, None)
                if in_top.get(val, False):
                    in_top[val] = False
                    top_cnt -= 1
                # no heap entry needed
            else:
                cnt[val] = new
                if in_top.get(val, False):
                    heapq.heappush(top_min, (new, val))
                else:
                    heapq.heappush(rest_max, (-new, -val))

        def rebalance():
            nonlocal top_cnt
            needed = min(x, len(cnt))

            # ensure correct size
            while top_cnt < needed and rest_max:
                f, v = get_rest_best()
                in_top[v] = True
                top_cnt += 1
                cur_sum[0] += v * f
                heapq.heappush(top_min, (f, v))

            while top_cnt > needed and top_min:
                f, v = get_top_worst()
                in_top[v] = False
                top_cnt -= 1
                cur_sum[0] -= v * f
                heapq.heappush(rest_max, (-f, -v))

            # maintain ordering property
            while top_min and rest_max:
                f_w, v_w = get_top_worst()
                f_b, v_b = get_rest_best()
                if f_b > f_w or (f_b == f_w and v_b > v_w):
                    # swap
                    in_top[v_w] = False
                    top_cnt -= 1
                    cur_sum[0] -= v_w * f_w
                    heapq.heappush(rest_max, (-f_w, -v_w))

                    in_top[v_b] = True
                    top_cnt += 1
                    cur_sum[0] += v_b * f_b
                    heapq.heappush(top_min, (f_b, v_b))
                else:
                    break

        ans = []
        for i in range(n - k + 1):
            ans.append(cur_sum[0])
            if i == n - k:
                break
            out_val = nums[i]
            in_val = nums[i + k]

            change(out_val, -1)
            change(in_val, 1)
            rebalance()

        return ans
```

## Python3

```python
import heapq
from collections import defaultdict
from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        cnt = defaultdict(int)

        # initial window counts
        for i in range(k):
            cnt[nums[i]] += 1

        # build initial top set (x most frequent)
        items = list(cnt.items())
        items.sort(key=lambda p: (-p[1], -p[0]))  # freq desc, value desc
        top_set = set()
        top_heap = []   # min-heap of (freq, val) for elements in top_set
        rest_heap = []  # max-heap of (-freq, -val) for others
        sum_top = 0

        for i, (val, freq) in enumerate(items):
            if i < x:
                top_set.add(val)
                sum_top += freq * val
                heapq.heappush(top_heap, (freq, val))
            else:
                heapq.heappush(rest_heap, (-freq, -val))

        ans = [sum_top]

        # helper cleaning functions
        def clean_top():
            while top_heap:
                f, v = top_heap[0]
                if cnt.get(v, 0) != f or v not in top_set:
                    heapq.heappop(top_heap)
                else:
                    break

        def clean_rest():
            while rest_heap:
                nf, nv = rest_heap[0]
                f, v = -nf, -nv
                if cnt.get(v, 0) != f or v in top_set:
                    heapq.heappop(rest_heap)
                else:
                    break

        # slide the window
        for start in range(1, n - k + 1):
            out_val = nums[start - 1]
            in_val = nums[start + k - 1]

            # remove outgoing element
            old_freq = cnt[out_val]
            new_freq = old_freq - 1
            if new_freq == 0:
                del cnt[out_val]
            else:
                cnt[out_val] = new_freq

            if out_val in top_set:
                sum_top += (new_freq - old_freq) * out_val
                if new_freq > 0:
                    heapq.heappush(top_heap, (new_freq, out_val))
                else:
                    top_set.remove(out_val)
            else:
                if new_freq > 0:
                    heapq.heappush(rest_heap, (-new_freq, -out_val))

            # add incoming element
            old_freq = cnt.get(in_val, 0)
            new_freq = old_freq + 1
            cnt[in_val] = new_freq

            if in_val in top_set:
                sum_top += (new_freq - old_freq) * in_val
                heapq.heappush(top_heap, (new_freq, in_val))
            else:
                heapq.heappush(rest_heap, (-new_freq, -in_val))

            # rebalance to keep exactly min(x, distinct) elements in top_set
            while len(top_set) > x:
                clean_top()
                if not top_heap:
                    break
                f, v = heapq.heappop(top_heap)
                if cnt.get(v, 0) != f or v not in top_set:
                    continue
                top_set.remove(v)
                sum_top -= f * v
                heapq.heappush(rest_heap, (-f, -v))

            while len(top_set) < x:
                clean_rest()
                if not rest_heap:
                    break
                nf, nv = heapq.heappop(rest_heap)
                f, v = -nf, -nv
                if cnt.get(v, 0) != f or v in top_set:
                    continue
                top_set.add(v)
                sum_top += f * v
                heapq.heappush(top_heap, (f, v))

            # swap if a better candidate exists in rest
            while True:
                clean_top()
                clean_rest()
                if not top_heap or not rest_heap:
                    break
                wf, wv = top_heap[0]                     # smallest freq in top_set
                bf, bv = -rest_heap[0][0], -rest_heap[0][1]  # largest freq in rest
                if bf > wf or (bf == wf and bv > wv):
                    heapq.heappop(top_heap)
                    heapq.heappop(rest_heap)

                    top_set.remove(wv)
                    sum_top -= wf * wv
                    top_set.add(bv)
                    sum_top += bf * bv

                    heapq.heappush(top_heap, (bf, bv))
                    heapq.heappush(rest_heap, (-wf, -wv))
                else:
                    break

            ans.append(sum_top)

        return ans
```

## C

```c
/****
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>
#include <string.h>

typedef struct {
    long long key;
    int cnt;
    char inA;   // 1 if element is currently in set A
    char used;  // slot occupied
} Entry;

static size_t hm_cap;
static Entry *hm_tab;

/* simple hash */
static inline size_t hm_hash(long long k) {
    return (size_t)(k ^ (k >> 33));
}

/* find existing or create new entry */
static Entry* hm_find_or_insert(long long key) {
    size_t idx = hm_hash(key) & (hm_cap - 1);
    while (1) {
        if (!hm_tab[idx].used) {
            hm_tab[idx].used = 1;
            hm_tab[idx].key = key;
            hm_tab[idx].cnt = 0;
            hm_tab[idx].inA = 0;
            return &hm_tab[idx];
        }
        if (hm_tab[idx].key == key)
            return &hm_tab[idx];
        idx = (idx + 1) & (hm_cap - 1);
    }
}

/* get entry, NULL if absent */
static Entry* hm_get(long long key) {
    size_t idx = hm_hash(key) & (hm_cap - 1);
    while (1) {
        if (!hm_tab[idx].used)
            return NULL;
        if (hm_tab[idx].key == key)
            return &hm_tab[idx];
        idx = (idx + 1) & (hm_cap - 1);
    }
}

/* heap structures */
typedef struct {
    int freq;
    long long val;
} Node;

typedef struct {
    Node *data;
    int size;
    int cap;
    char type;   // 0 -> A (worst first), 1 -> B (best first)
} Heap;

/* comparator for set A: worse element has smaller freq, tie smaller value */
static inline int cmpA(const Node *a, const Node *b) {
    if (a->freq != b->freq) return a->freq < b->freq;
    return a->val < b->val;
}

/* comparator for set B: better element has larger freq, tie larger value */
static inline int cmpB(const Node *a, const Node *b) {
    if (a->freq != b->freq) return a->freq > b->freq;
    return a->val > b->val;
}

static void heap_push(Heap *h, Node nd) {
    if (h->size == h->cap) {
        h->cap = h->cap ? h->cap * 2 : 4;
        h->data = realloc(h->data, sizeof(Node) * h->cap);
    }
    int i = h->size++;
    h->data[i] = nd;
    while (i > 0) {
        int p = (i - 1) >> 1;
        int better = (h->type == 0) ? cmpA(&h->data[i], &h->data[p])
                                    : cmpB(&h->data[i], &h->data[p]);
        if (better) {
            Node tmp = h->data[i];
            h->data[i] = h->data[p];
            h->data[p] = tmp;
            i = p;
        } else break;
    }
}

/* remove top element */
static void heap_pop(Heap *h) {
    if (!h->size) return;
    h->data[0] = h->data[--h->size];
    int i = 0;
    while (1) {
        int l = i * 2 + 1, r = l + 1, best = i;
        if (l < h->size) {
            int better = (h->type == 0) ? cmpA(&h->data[l], &h->data[best])
                                        : cmpB(&h->data[l], &h->data[best]);
            if (better) best = l;
        }
        if (r < h->size) {
            int better = (h->type == 0) ? cmpA(&h->data[r], &h->data[best])
                                        : cmpB(&h->data[r], &h->data[best]);
            if (better) best = r;
        }
        if (best != i) {
            Node tmp = h->data[i];
            h->data[i] = h->data[best];
            h->data[best] = tmp;
            i = best;
        } else break;
    }
}

/* clean stale top */
static void heap_clean_top(Heap *h) {
    while (h->size) {
        Node nd = h->data[0];
        Entry *e = hm_get(nd.val);
        if (!e || e->cnt != nd.freq ||
            ((h->type == 0 && !e->inA) || (h->type == 1 && e->inA))) {
            heap_pop(h);
        } else break;
    }
}

/* peek valid top */
static Node heap_peek_valid(Heap *h) {
    heap_clean_top(h);
    return h->size ? h->data[0] : (Node){0, 0};
}

/* pop and return valid top */
static Node heap_pop_valid(Heap *h) {
    heap_clean_top(h);
    if (!h->size) return (Node){0, 0};
    Node nd = h->data[0];
    heap_pop(h);
    return nd;
}

/* rebalance sets A and B */
static void rebalance(Heap *A, Heap *B, int x,
                      long long *sumA, int *cntInA) {
    while (*cntInA > x) {
        Node nd = heap_pop_valid(A);
        Entry *e = hm_get(nd.val);
        if (!e) continue;
        e->inA = 0;
        *sumA -= (long long)nd.val * e->cnt;
        (*cntInA)--;
        heap_push(B, (Node){e->cnt, nd.val});
    }
    while (*cntInA < x) {
        if (!B->size) break;
        Node nd = heap_pop_valid(B);
        Entry *e = hm_get(nd.val);
        if (!e) continue;
        e->inA = 1;
        *sumA += (long long)nd.val * e->cnt;
        (*cntInA)++;
        heap_push(A, (Node){e->cnt, nd.val});
    }
    while (1) {
        if (!A->size || !B->size) break;
        Node topA = heap_peek_valid(A);
        Node topB = heap_peek_valid(B);
        int better = 0;
        if (topB.freq > topA.freq) better = 1;
        else if (topB.freq == topA.freq && topB.val > topA.val) better = 1;
        if (!better) break;

        /* swap */
        heap_pop_valid(A);
        heap_pop_valid(B);
        Entry *eA = hm_get(topA.val);
        Entry *eB = hm_get(topB.val);
        if (eA) {
            eA->inA = 0;
            *sumA -= (long long)topA.val * eA->cnt;
            (*cntInA)--;
            heap_push(B, (Node){eA->cnt, topA.val});
        }
        if (eB) {
            eB->inA = 1;
            *sumA += (long long)topB.val * eB->cnt;
            (*cntInA)++;
            heap_push(A, (Node){eB->cnt, topB.val});
        }
    }
}

/* main function */
long long* findXSum(int* nums, int numsSize, int k, int x, int* returnSize) {
    /* initialise hashmap */
    hm_cap = 1;
    while (hm_cap < (size_t)numsSize * 4) hm_cap <<= 1;
    hm_tab = calloc(hm_cap, sizeof(Entry));

    Heap A = {NULL, 0, 0, 0};   // worst first
    Heap B = {NULL, 0, 0, 1};   // best first

    /* build initial window */
    for (int i = 0; i < k; ++i) {
        Entry *e = hm_find_or_insert(nums[i]);
        e->cnt++;
    }

    /* insert all distinct into B initially */
    for (size_t i = 0; i < hm_cap; ++i) {
        if (hm_tab[i].used && hm_tab[i].cnt > 0) {
            heap_push(&B, (Node){hm_tab[i].cnt, hm_tab[i].key});
        }
    }

    long long sumA = 0;
    int cntInA = 0;
    rebalance(&A, &B, x, &sumA, &cntInA);

    int outLen = numsSize - k + 1;
    long long *ans = malloc(sizeof(long long) * outLen);
    ans[0] = sumA;

    for (int i = k; i < numsSize; ++i) {
        int outVal = nums[i - k];
        int inVal = nums[i];

        /* remove outgoing */
        Entry *eOut = hm_get(outVal);
        if (eOut && eOut->cnt > 0) {
            if (eOut->inA) sumA -= outVal;
            eOut->cnt--;
            if (eOut->cnt == 0) {
                if (eOut->inA) { eOut->inA = 0; cntInA--; }
                /* keep entry for stale heap cleanup */
            } else {
                if (eOut->inA)
                    heap_push(&A, (Node){eOut->cnt, outVal});
                else
                    heap_push(&B, (Node){eOut->cnt, outVal});
            }
        }

        /* add incoming */
        Entry *eIn = hm_find_or_insert(inVal);
        if (eIn->inA) sumA += inVal;
        eIn->cnt++;
        if (eIn->inA)
            heap_push(&A, (Node){eIn->cnt, inVal});
        else
            heap_push(&B, (Node){eIn->cnt, inVal});

        rebalance(&A, &B, x, &sumA, &cntInA);
        ans[i - k + 1] = sumA;
    }

    *returnSize = outLen;
    free(hm_tab);
    free(A.data);
    free(B.data);
    return ans;
}
```

## Csharp

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public long[] FindXSum(int[] nums, int k, int x) {
        int n = nums.Length;
        long[] ans = new long[n - k + 1];
        var freq = new Dictionary<int, int>();
        var comparer = new NodeComparer();
        var top = new SortedSet<Node>(comparer);
        var rest = new SortedSet<Node>(comparer);
        long sumTop = 0;

        void RemoveNode(int val, int f) {
            var node = new Node(val, f);
            if (top.Remove(node)) {
                sumTop -= (long)val * f;
            } else {
                rest.Remove(node);
            }
        }

        void Rebalance() {
            while (top.Count > x) {
                var minTop = top.Min;
                top.Remove(minTop);
                sumTop -= (long)minTop.val * minTop.freq;
                rest.Add(minTop);
            }
            while (top.Count < x && rest.Count > 0) {
                var maxRest = rest.Max;
                rest.Remove(maxRest);
                top.Add(maxRest);
                sumTop += (long)maxRest.val * maxRest.freq;
            }
            while (top.Count > 0 && rest.Count > 0) {
                var minTop = top.Min;
                var maxRest = rest.Max;
                if (comparer.Compare(minTop, maxRest) < 0) {
                    top.Remove(minTop);
                    sumTop -= (long)minTop.val * minTop.freq;
                    rest.Remove(maxRest);
                    top.Add(maxRest);
                    sumTop += (long)maxRest.val * maxRest.freq;
                    rest.Add(minTop);
                } else break;
            }
        }

        void InsertNode(int val, int f) {
            var node = new Node(val, f);
            if (top.Count < x) {
                top.Add(node);
                sumTop += (long)val * f;
            } else {
                var minTop = top.Min; // guaranteed to exist because top.Count == x
                int cmp = comparer.Compare(node, minTop);
                if (cmp > 0) {
                    top.Remove(minTop);
                    sumTop -= (long)minTop.val * minTop.freq;
                    rest.Add(minTop);
                    top.Add(node);
                    sumTop += (long)val * f;
                } else {
                    rest.Add(node);
                }
            }
            Rebalance();
        }

        void AddOrUpdate(int val, int delta) {
            int oldFreq = 0;
            freq.TryGetValue(val, out oldFreq);
            int newFreq = oldFreq + delta;

            if (oldFreq > 0) {
                RemoveNode(val, oldFreq);
            }
            if (newFreq > 0) {
                InsertNode(val, newFreq);
                freq[val] = newFreq;
            } else {
                freq.Remove(val);
            }
        }

        // initialize first window
        for (int i = 0; i < k; ++i) {
            AddOrUpdate(nums[i], +1);
        }
        ans[0] = sumTop;

        // slide the window
        for (int i = k; i < n; ++i) {
            AddOrUpdate(nums[i - k], -1); // remove outgoing
            AddOrUpdate(nums[i], +1);     // add incoming
            ans[i - k + 1] = sumTop;
        }

        return ans;
    }

    private class Node {
        public int val;
        public int freq;
        public Node(int v, int f) { val = v; freq = f; }
    }

    private class NodeComparer : IComparer<Node> {
        public int Compare(Node a, Node b) {
            if (a.freq != b.freq) return a.freq.CompareTo(b.freq);
            return a.val.CompareTo(b.val);
        }
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} x
 * @return {number[]}
 */
var findXSum = function(nums, k, x) {
    class Heap {
        constructor(comp) {
            this.data = [];
            this.comp = comp;
        }
        size() { return this.data.length; }
        peek() { return this.data[0]; }
        push(item) {
            const a = this.data;
            a.push(item);
            let i = a.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (this.comp(a[i], a[p]) < 0) {
                    [a[i], a[p]] = [a[p], a[i]];
                    i = p;
                } else break;
            }
        }
        pop() {
            const a = this.data;
            if (a.length === 0) return undefined;
            const top = a[0];
            const last = a.pop();
            if (a.length > 0) {
                a[0] = last;
                let i = 0;
                while (true) {
                    let l = i * 2 + 1, r = l + 1, best = i;
                    if (l < a.length && this.comp(a[l], a[best]) < 0) best = l;
                    if (r < a.length && this.comp(a[r], a[best]) < 0) best = r;
                    if (best !== i) {
                        [a[i], a[best]] = [a[best], a[i]];
                        i = best;
                    } else break;
                }
            }
            return top;
        }
    }

    // min-heap for A (least desirable in top set)
    const minHeapA = new Heap((a, b) => {
        if (a.freq !== b.freq) return a.freq - b.freq;
        return a.val - b.val;
    });
    // max-heap for B (most desirable outside top set)
    const maxHeapB = new Heap((a, b) => {
        if (a.freq !== b.freq) return b.freq - a.freq;
        return b.val - a.val;
    });

    const freq = new Map();          // val -> count in current window
    const inA = new Set();           // values currently in top-x set
    let totalSum = 0;                // sum of all occurrences of numbers in A

    function cleanMin() {
        while (minHeapA.size()) {
            const t = minHeapA.peek();
            if (!inA.has(t.val) || freq.get(t.val) !== t.freq) {
                minHeapA.pop();
            } else break;
        }
    }

    function cleanMax() {
        while (maxHeapB.size()) {
            const t = maxHeapB.peek();
            if (inA.has(t.val) || !freq.has(t.val) || freq.get(t.val) !== t.freq) {
                maxHeapB.pop();
            } else break;
        }
    }

    function rebalance() {
        // ensure size of A does not exceed x
        while (inA.size > Math.min(x, freq.size)) {
            cleanMin();
            const out = minHeapA.pop(); // least desirable in A
            if (!out) break;
            inA.delete(out.val);
            totalSum -= out.val * freq.get(out.val);
            maxHeapB.push({freq: freq.get(out.val), val: out.val});
        }
        // ensure size of A reaches x (or all distinct if fewer)
        while (inA.size < Math.min(x, freq.size)) {
            cleanMax();
            const inItem = maxHeapB.pop(); // most desirable candidate
            if (!inItem) break;
            inA.add(inItem.val);
            totalSum += inItem.val * freq.get(inItem.val);
            minHeapA.push({freq: freq.get(inItem.val), val: inItem.val});
        }
        // swap if ordering violated
        while (true) {
            cleanMin(); cleanMax();
            if (!minHeapA.size() || !maxHeapB.size()) break;
            const aTop = minHeapA.peek(); // least in A
            const bTop = maxHeapB.peek(); // best in B
            if (bTop.freq > aTop.freq ||
                (bTop.freq === aTop.freq && bTop.val > aTop.val)) {
                // swap them
                minHeapA.pop();
                maxHeapB.pop();

                // move aTop out of A
                inA.delete(aTop.val);
                totalSum -= aTop.val * freq.get(aTop.val);
                maxHeapB.push({freq: freq.get(aTop.val), val: aTop.val});

                // move bTop into A
                inA.add(bTop.val);
                totalSum += bTop.val * freq.get(bTop.val);
                minHeapA.push({freq: freq.get(bTop.val), val: bTop.val});
            } else break;
        }
    }

    function add(val) {
        const old = freq.get(val) || 0;
        const nw = old + 1;
        freq.set(val, nw);
        if (inA.has(val)) {
            totalSum += val; // one more occurrence contributes
        }
        // push updated entry into appropriate heap
        if (inA.has(val)) {
            minHeapA.push({freq: nw, val});
        } else {
            maxHeapB.push({freq: nw, val});
        }
    }

    function remove(val) {
        const old = freq.get(val);
        if (!old) return;
        const nw = old - 1;
        if (inA.has(val)) {
            totalSum -= val; // one occurrence removed from sum
        }
        if (nw === 0) {
            freq.delete(val);
            if (inA.has(val)) inA.delete(val);
        } else {
            freq.set(val, nw);
            if (inA.has(val)) {
                minHeapA.push({freq: nw, val});
            } else {
                maxHeapB.push({freq: nw, val});
            }
        }
    }

    // build initial window
    for (let i = 0; i < k; ++i) add(nums[i]);
    // initially move best x distinct into A
    while (inA.size < Math.min(x, freq.size)) {
        cleanMax();
        const cand = maxHeapB.pop();
        if (!cand) break;
        inA.add(cand.val);
        totalSum += cand.val * freq.get(cand.val);
        minHeapA.push({freq: freq.get(cand.val), val: cand.val});
    }

    const ans = [];
    ans.push(totalSum);

    // slide window
    for (let i = k; i < nums.length; ++i) {
        remove(nums[i - k]);
        add(nums[i]);
        rebalance();
        ans.push(totalSum);
    }
    return ans;
};
```

## Typescript

```typescript
class Heap<T> {
    private data: T[] = [];
    private comp: (a: T, b: T) => number;
    constructor(comp: (a: T, b: T) => number) {
        this.comp = comp;
    }
    size(): number { return this.data.length; }
    peek(): T { return this.data[0]; }
    push(item: T): void {
        const a = this.data;
        a.push(item);
        let i = a.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (this.comp(a[i], a[p]) < 0) {
                [a[i], a[p]] = [a[p], a[i]];
                i = p;
            } else break;
        }
    }
    pop(): T | undefined {
        const a = this.data;
        if (a.length === 0) return undefined;
        const top = a[0];
        const last = a.pop()!;
        if (a.length > 0) {
            a[0] = last;
            let i = 0;
            while (true) {
                let l = i * 2 + 1, r = l + 1, smallest = i;
                if (l < a.length && this.comp(a[l], a[smallest]) < 0) smallest = l;
                if (r < a.length && this.comp(a[r], a[smallest]) < 0) smallest = r;
                if (smallest !== i) {
                    [a[i], a[smallest]] = [a[smallest], a[i]];
                    i = smallest;
                } else break;
            }
        }
        return top;
    }
}

function findXSum(nums: number[], k: number, x: number): number[] {
    const n = nums.length;
    const ans: number[] = [];

    const cntMap = new Map<number, number>();
    const topSet = new Set<number>();
    let sumTop = 0;

    const topMinHeap = new Heap<{ val: number; cnt: number }>((a, b) => a.cnt - b.cnt || a.val - b.val);
    const otherMaxHeap = new Heap<{ val: number; cnt: number }>((a, b) => b.cnt - a.cnt || b.val - a.val);

    function cleanTopPeek(): { val: number; cnt: number } | null {
        while (topMinHeap.size() > 0) {
            const e = topMinHeap.peek();
            if (!cntMap.has(e.val) || cntMap.get(e.val)! !== e.cnt || !topSet.has(e.val)) {
                topMinHeap.pop();
                continue;
            }
            return e;
        }
        return null;
    }

    function cleanTopPop(): { val: number; cnt: number } | null {
        while (topMinHeap.size() > 0) {
            const e = topMinHeap.pop()!;
            if (!cntMap.has(e.val) || cntMap.get(e.val)! !== e.cnt || !topSet.has(e.val)) continue;
            return e;
        }
        return null;
    }

    function cleanOtherPeek(): { val: number; cnt: number } | null {
        while (otherMaxHeap.size() > 0) {
            const e = otherMaxHeap.peek();
            if (!cntMap.has(e.val) || cntMap.get(e.val)! !== e.cnt || topSet.has(e.val)) {
                otherMaxHeap.pop();
                continue;
            }
            return e;
        }
        return null;
    }

    function cleanOtherPop(): { val: number; cnt: number } | null {
        while (otherMaxHeap.size() > 0) {
            const e = otherMaxHeap.pop()!;
            if (!cntMap.has(e.val) || cntMap.get(e.val)! !== e.cnt || topSet.has(e.val)) continue;
            return e;
        }
        return null;
    }

    function rebalance(): void {
        while (topSet.size > x) {
            const worst = cleanTopPop();
            if (!worst) break;
            topSet.delete(worst.val);
            sumTop -= worst.val * worst.cnt;
            otherMaxHeap.push(worst);
        }
        const targetSize = Math.min(x, cntMap.size);
        while (topSet.size < targetSize) {
            const best = cleanOtherPop();
            if (!best) break;
            topSet.add(best.val);
            sumTop += best.val * best.cnt;
            topMinHeap.push(best);
        }
        while (true) {
            const worst = cleanTopPeek();
            const best = cleanOtherPeek();
            if (!worst || !best) break;
            if (worst.cnt < best.cnt || (worst.cnt === best.cnt && worst.val < best.val)) {
                // swap
                cleanTopPop();
                cleanOtherPop();
                topSet.delete(worst.val);
                sumTop -= worst.val * worst.cnt;
                otherMaxHeap.push(worst);

                topSet.add(best.val);
                sumTop += best.val * best.cnt;
                topMinHeap.push(best);
            } else break;
        }
    }

    function add(val: number): void {
        const old = cntMap.get(val) || 0;
        const newc = old + 1;
        cntMap.set(val, newc);
        otherMaxHeap.push({ val, cnt: newc });
        if (topSet.has(val)) {
            sumTop -= val * old;
            sumTop += val * newc;
            topMinHeap.push({ val, cnt: newc });
        }
    }

    function remove(val: number): void {
        const old = cntMap.get(val)!;
        const newc = old - 1;
        if (newc === 0) {
            cntMap.delete(val);
        } else {
            cntMap.set(val, newc);
            otherMaxHeap.push({ val, cnt: newc });
        }
        if (topSet.has(val)) {
            sumTop -= val * old;
            if (newc > 0) {
                sumTop += val * newc;
                topMinHeap.push({ val, cnt: newc });
            } else {
                topSet.delete(val);
            }
        }
    }

    for (let i = 0; i < n; ++i) {
        add(nums[i]);
        if (i >= k) remove(nums[i - k]);
        rebalance();
        if (i >= k - 1) ans.push(sumTop);
    }
    return ans;
}
```

## Php

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer $x
     * @return Integer[]
     */
    function findXSum($nums, $k, $x) {
        $n = count($nums);
        $freq = [];               // value => frequency in current window
        $inTop = [];              // value => bool whether in top set
        $topSize = 0;
        $topSum = 0;              // sum of value*frequency for elements in top

        $maxHeap = new SplPriorityQueue(); // max by (freq, val)
        $maxHeap->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $minHeap = new SplPriorityQueue(); // min by (freq, val) using negative priority
        $minHeap->setExtractFlags(SplPriorityQueue::EXTR_DATA);

        // build initial window frequencies
        for ($i = 0; $i < $k; ++$i) {
            $v = $nums[$i];
            if (!isset($freq[$v])) $freq[$v] = 0;
            $freq[$v]++;
        }

        // push all distinct values into both heaps
        foreach ($freq as $val => $f) {
            $maxHeap->insert(['val' => $val, 'freq' => $f], [$f, $val]);
            $minHeap->insert(['val' => $val, 'freq' => $f], [-$f, -$val]);
        }

        // helper to add best candidates until top size reaches x
        $addBest = function() use (&$maxHeap, &$freq, &$inTop, &$topSize, &$topSum, $x) {
            while ($topSize < $x) {
                // get valid best not in top
                $best = null;
                while (!$maxHeap->isEmpty()) {
                    $item = $maxHeap->top();
                    $v = $item['val'];
                    $f = $item['freq'];
                    if (!isset($freq[$v]) || $freq[$v] != $f) { $maxHeap->extract(); continue; }
                    if (isset($inTop[$v]) && $inTop[$v]) { $maxHeap->extract(); continue; }
                    $best = $item;
                    break;
                }
                if ($best === null) break;
                $maxHeap->extract(); // remove it
                $val = $best['val'];
                $inTop[$val] = true;
                $topSize++;
                $topSum += $val * $freq[$val];
            }
        };

        // initial fill of top set
        $addBest();

        $ans = [];
        $ans[] = $topSum;

        // slide the window
        for ($i = 1; $i <= $n - $k; ++$i) {
            $outVal = $nums[$i - 1];
            $inVal  = $nums[$i + $k - 1];

            // remove outgoing element
            $oldFreq = $freq[$outVal];
            if (isset($inTop[$outVal]) && $inTop[$outVal]) {
                $topSum -= $outVal * $oldFreq;
            }
            $newFreq = $oldFreq - 1;
            if ($newFreq == 0) {
                unset($freq[$outVal]);
                if (isset($inTop[$outVal]) && $inTop[$outVal]) {
                    $inTop[$outVal] = false;
                    $topSize--;
                }
            } else {
                $freq[$outVal] = $newFreq;
                $maxHeap->insert(['val' => $outVal, 'freq' => $newFreq], [$newFreq, $outVal]);
                $minHeap->insert(['val' => $outVal, 'freq' => $newFreq], [-$newFreq, -$outVal]);
                if (isset($inTop[$outVal]) && $inTop[$outVal]) {
                    $topSum += $outVal * $newFreq;
                }
            }

            // add incoming element
            $oldFreq = $freq[$inVal] ?? 0;
            if (isset($inTop[$inVal]) && $inTop[$inVal]) {
                $topSum -= $inVal * $oldFreq;
            }
            $newFreq = $oldFreq + 1;
            $freq[$inVal] = $newFreq;
            $maxHeap->insert(['val' => $inVal, 'freq' => $newFreq], [$newFreq, $inVal]);
            $minHeap->insert(['val' => $inVal, 'freq' => $newFreq], [-$newFreq, -$inVal]);
            if (isset($inTop[$inVal]) && $inTop[$inVal]) {
                $topSum += $inVal * $newFreq;
            }

            // ensure top size does not exceed x
            while ($topSize > $x) {
                // remove worst element from top set
                $worst = null;
                while (!$minHeap->isEmpty()) {
                    $item = $minHeap->top();
                    $v = $item['val'];
                    $f = $item['freq'];
                    if (!isset($freq[$v]) || $freq[$v] != $f) { $minHeap->extract(); continue; }
                    if (!isset($inTop[$v]) || !$inTop[$v]) { $minHeap->extract(); continue; }
                    $worst = $item;
                    break;
                }
                if ($worst === null) break;
                $minHeap->extract();
                $val = $worst['val'];
                $inTop[$val] = false;
                $topSize--;
                $topSum -= $val * $freq[$val];
            }

            // add best candidates to fill up to x
            $addBest();

            // swap if there exists a better candidate than the worst in top
            while (true) {
                // get current worst in top
                $worst = null;
                while (!$minHeap->isEmpty()) {
                    $item = $minHeap->top();
                    $v = $item['val'];
                    $f = $item['freq'];
                    if (!isset($freq[$v]) || $freq[$v] != $f) { $minHeap->extract(); continue; }
                    if (!isset($inTop[$v]) || !$inTop[$v]) { $minHeap->extract(); continue; }
                    $worst = $item;
                    break;
                }

                // get current best not in top
                $best = null;
                while (!$maxHeap->isEmpty()) {
                    $item = $maxHeap->top();
                    $v = $item['val'];
                    $f = $item['freq'];
                    if (!isset($freq[$v]) || $freq[$v] != $f) { $maxHeap->extract(); continue; }
                    if (isset($inTop[$v]) && $inTop[$v]) { $maxHeap->extract(); continue; }
                    $best = $item;
                    break;
                }

                if ($worst === null || $best === null) break;

                $better = false;
                if ($best['freq'] > $worst['freq']) {
                    $better = true;
                } elseif ($best['freq'] == $worst['freq'] && $best['val'] > $worst['val']) {
                    $better = true;
                }

                if (!$better) break;

                // perform swap
                $maxHeap->extract(); // remove best
                $minHeap->extract(); // remove worst

                $valW = $worst['val'];
                $valB = $best['val'];

                $inTop[$valW] = false;
                $topSum -= $valW * $freq[$valW];

                $inTop[$valB] = true;
                $topSum += $valB * $freq[$valB];
                // topSize unchanged
            }

            $ans[] = $topSum;
        }

        return $ans;
    }
}
```

## Swift

```swift
import Foundation

struct Entry {
    let val: Int
    let freq: Int
}

struct Heap<T> {
    var elements: [T] = []
    let priorityFunction: (T, T) -> Bool
    
    init(sort: @escaping (T, T) -> Bool) {
        self.priorityFunction = sort
    }
    
    mutating func push(_ value: T) {
        elements.append(value)
        siftUp(elements.count - 1)
    }
    
    mutating func pop() -> T? {
        guard !elements.isEmpty else { return nil }
        if elements.count == 1 {
            return elements.removeLast()
        }
        let value = elements[0]
        elements[0] = elements.removeLast()
        siftDown(0)
        return value
    }
    
    func peek() -> T? {
        elements.first
    }
    
    var isEmpty: Bool { elements.isEmpty }
    
    private mutating func siftUp(_ index: Int) {
        var child = index
        var parent = (child - 1) / 2
        while child > 0 && priorityFunction(elements[child], elements[parent]) {
            elements.swapAt(child, parent)
            child = parent
            parent = (child - 1) / 2
        }
    }
    
    private mutating func siftDown(_ index: Int) {
        var parent = index
        while true {
            let left = parent * 2 + 1
            let right = left + 1
            var candidate = parent
            if left < elements.count && priorityFunction(elements[left], elements[candidate]) {
                candidate = left
            }
            if right < elements.count && priorityFunction(elements[right], elements[candidate]) {
                candidate = right
            }
            if candidate == parent { return }
            elements.swapAt(parent, candidate)
            parent = candidate
        }
    }
}

class Solution {
    func findXSum(_ nums: [Int], _ k: Int, _ x: Int) -> [Int] {
        let n = nums.count
        if k == 0 || n < k { return [] }
        
        var freq = [Int:Int]()
        var topSet = Set<Int>()
        var sumTop: Int64 = 0
        
        var topHeap = Heap<Entry>(sort: { a, b in
            if a.freq != b.freq { return a.freq < b.freq }
            return a.val < b.val
        })
        var otherHeap = Heap<Entry>(sort: { a, b in
            if a.freq != b.freq { return a.freq > b.freq }
            return a.val > b.val
        })
        
        // initial window frequencies
        for i in 0..<k {
            let v = nums[i]
            freq[v, default: 0] += 1
        }
        for (val, f) in freq {
            otherHeap.push(Entry(val: val, freq: f))
        }
        
        func getValidTopWorst() -> Entry? {
            while let e = topHeap.peek() {
                if let curF = freq[e.val], curF == e.freq, topSet.contains(e.val) {
                    return e
                } else {
                    _ = topHeap.pop()
                }
            }
            return nil
        }
        
        func getValidOtherTop() -> Entry? {
            while let e = otherHeap.peek() {
                if let curF = freq[e.val], curF == e.freq, !topSet.contains(e.val) {
                    return e
                } else {
                    _ = otherHeap.pop()
                }
            }
            return nil
        }
        
        func rebalance() {
            // Fill up to min(x, distinct)
            while topSet.count < min(x, freq.count) {
                guard let best = getValidOtherTop() else { break }
                _ = otherHeap.pop()
                topSet.insert(best.val)
                sumTop += Int64(best.freq) * Int64(best.val)
                topHeap.push(best)
            }
            
            // Ensure ordering
            while true {
                guard let worst = getValidTopWorst(),
                      let best = getValidOtherTop() else { break }
                if (best.freq > worst.freq) || (best.freq == worst.freq && best.val > worst.val) {
                    _ = topHeap.pop()
                    _ = otherHeap.pop()
                    
                    // move worst out
                    topSet.remove(worst.val)
                    sumTop -= Int64(worst.freq) * Int64(worst.val)
                    otherHeap.push(worst)
                    
                    // move best in
                    topSet.insert(best.val)
                    sumTop += Int64(best.freq) * Int64(best.val)
                    topHeap.push(best)
                } else {
                    break
                }
            }
            
            // If too many (after deletions)
            while topSet.count > x {
                guard let worst = getValidTopWorst() else { break }
                _ = topHeap.pop()
                topSet.remove(worst.val)
                sumTop -= Int64(worst.freq) * Int64(worst.val)
                otherHeap.push(worst)
            }
        }
        
        rebalance()
        var result = [Int]()
        result.append(Int(sumTop))
        
        if n > k {
            for i in k..<n {
                let outVal = nums[i - k]
                let inVal = nums[i]
                
                // Remove outgoing
                if let oldFreq = freq[outVal] {
                    let newFreq = oldFreq - 1
                    if newFreq == 0 {
                        freq.removeValue(forKey: outVal)
                    } else {
                        freq[outVal] = newFreq
                    }
                    if newFreq > 0 {
                        otherHeap.push(Entry(val: outVal, freq: newFreq))
                    }
                    if topSet.contains(outVal) {
                        sumTop += Int64(newFreq - oldFreq) * Int64(outVal)
                        if newFreq == 0 {
                            topSet.remove(outVal)
                        }
                    }
                }
                
                // Add incoming
                let oldInFreq = freq[inVal] ?? 0
                let newInFreq = oldInFreq + 1
                freq[inVal] = newInFreq
                otherHeap.push(Entry(val: inVal, freq: newInFreq))
                if topSet.contains(inVal) {
                    sumTop += Int64(newInFreq - oldInFreq) * Int64(inVal)
                }
                
                rebalance()
                result.append(Int(sumTop))
            }
        }
        
        return result
    }
}
```

## Kotlin

```kotlin
import java.util.TreeSet

data class Elem(val freq: Int, val value: Int)

class Solution {
    fun findXSum(nums: IntArray, k: Int, x: Int): LongArray {
        val n = nums.size
        val res = LongArray(n - k + 1)
        val freqMap = HashMap<Int, Int>()
        val comp = compareBy<Elem>({ it.freq }, { it.value })
        val topSet = TreeSet(comp)          // holds up to x elements with highest (freq, value)
        val bottomSet = TreeSet(comp)       // the rest
        var sumTop = 0L

        fun rebalance() {
            while (topSet.size > x) {
                val smallest = topSet.pollFirst()
                sumTop -= smallest.value.toLong() * smallest.freq
                bottomSet.add(smallest)
            }
            while (topSet.size < x && bottomSet.isNotEmpty()) {
                val largest = bottomSet.pollLast()
                topSet.add(largest)
                sumTop += largest.value.toLong() * largest.freq
            }
            while (topSet.isNotEmpty() && bottomSet.isNotEmpty()) {
                val lowTop = topSet.first()
                val highBottom = bottomSet.last()
                if (highBottom.freq > lowTop.freq ||
                    (highBottom.freq == lowTop.freq && highBottom.value > lowTop.value)
                ) {
                    topSet.pollFirst()
                    bottomSet.pollLast()
                    sumTop -= lowTop.value.toLong() * lowTop.freq
                    sumTop += highBottom.value.toLong() * highBottom.freq
                    topSet.add(highBottom)
                    bottomSet.add(lowTop)
                } else break
            }
        }

        fun add(v: Int) {
            val oldFreq = freqMap.getOrDefault(v, 0)
            val newFreq = oldFreq + 1
            freqMap[v] = newFreq
            if (oldFreq > 0) {
                val oldElem = Elem(oldFreq, v)
                if (!topSet.remove(oldElem)) {
                    bottomSet.remove(oldElem)
                } else {
                    sumTop -= v.toLong() * oldFreq
                }
            }
            bottomSet.add(Elem(newFreq, v))
            rebalance()
        }

        fun remove(v: Int) {
            val oldFreq = freqMap[v]!!
            val newFreq = oldFreq - 1
            val oldElem = Elem(oldFreq, v)
            if (!topSet.remove(oldElem)) {
                bottomSet.remove(oldElem)
            } else {
                sumTop -= v.toLong() * oldFreq
            }
            if (newFreq == 0) {
                freqMap.remove(v)
            } else {
                freqMap[v] = newFreq
                bottomSet.add(Elem(newFreq, v))
            }
            rebalance()
        }

        // Initialize first window
        for (i in 0 until k) add(nums[i])
        res[0] = sumTop

        // Slide the window
        for (i in k until n) {
            add(nums[i])
            remove(nums[i - k])
            res[i - k + 1] = sumTop
        }

        return res
    }
}
```

## Dart

```dart
import 'dart:collection';

class _Node {
  int val;
  int freq;
  _Node(this.val, this.freq);
}

class Solution {
  List<int> findXSum(List<int> nums, int k, int x) {
    // Comparator for descending frequency, then descending value
    int compare(_Node a, _Node b) {
      if (a.freq != b.freq) return b.freq - a.freq;
      return b.val - a.val;
    }

    final SplayTreeSet<_Node> selected = SplayTreeSet<_Node>(compare);
    final SplayTreeSet<_Node> rest = SplayTreeSet<_Node>(compare);
    final Map<int, int> freqMap = {};
    final Map<int, _Node> nodeMap = {};

    int totalSum = 0;
    List<int> ans = [];

    void rebalance() {
      int target = x < freqMap.length ? x : freqMap.length;

      // Adjust size to target
      while (selected.length > target) {
        final _Node worst = selected.last; // lowest priority in selected
        selected.remove(worst);
        totalSum -= worst.freq * worst.val;
        rest.add(worst);
      }
      while (selected.length < target && rest.isNotEmpty) {
        final _Node best = rest.first; // highest priority in rest
        rest.remove(best);
        selected.add(best);
        totalSum += best.freq * best.val;
      }

      // Ensure ordering property between sets
      while (selected.isNotEmpty && rest.isNotEmpty) {
        final _Node worstSel = selected.last;
        final _Node bestRest = rest.first;
        if (compare(bestRest, worstSel) > 0) {
          // swap them
          selected.remove(worstSel);
          totalSum -= worstSel.freq * worstSel.val;
          rest.remove(bestRest);

          selected.add(bestRest);
          totalSum += bestRest.freq * bestRest.val;

          rest.add(worstSel);
        } else {
          break;
        }
      }
    }

    void update(int val, int delta) {
      if (delta == 1) {
        // increment
        if (!freqMap.containsKey(val)) {
          final _Node node = _Node(val, 1);
          freqMap[val] = 1;
          nodeMap[val] = node;
          rest.add(node);
        } else {
          final _Node node = nodeMap[val]!;
          // remove from current set
          if (selected.contains(node)) {
            selected.remove(node);
          } else {
            rest.remove(node);
          }
          int newFreq = freqMap[val]! + 1;
          freqMap[val] = newFreq;
          node.freq = newFreq;
          // temporarily insert into rest; rebalance will place it correctly
          rest.add(node);
        }
      } else {
        // decrement
        final _Node? node = nodeMap[val];
        if (node == null) return; // should not happen
        // remove from current set
        if (selected.contains(node)) {
          selected.remove(node);
          totalSum -= node.freq * node.val;
        } else {
          rest.remove(node);
        }
        int newFreq = freqMap[val]! - 1;
        if (newFreq == 0) {
          freqMap.remove(val);
          nodeMap.remove(val);
          // node discarded
        } else {
          freqMap[val] = newFreq;
          node.freq = newFreq;
          rest.add(node);
        }
      }
      rebalance();
    }

    for (int i = 0; i < nums.length; ++i) {
      update(nums[i], 1);
      if (i >= k) {
        update(nums[i - k], -1);
      }
      if (i >= k - 1) {
        ans.add(totalSum);
      }
    }

    return ans;
  }
}
```

## Golang

```go
package main

import (
	"container/heap"
)

type Item struct {
	val  int
	freq int
}

// MaxHeap keeps the highest (freq, val) on top.
type MaxHeap []Item

func (h MaxHeap) Len() int { return len(h) }
func (h MaxHeap) Less(i, j int) bool {
	if h[i].freq != h[j].freq {
		return h[i].freq > h[j].freq
	}
	return h[i].val > h[j].val
}
func (h MaxHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *MaxHeap) Push(x interface{}) {
	*h = append(*h, x.(Item))
}
func (h *MaxHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

// MinHeap keeps the lowest (freq, val) on top.
type MinHeap []Item

func (h MinHeap) Len() int { return len(h) }
func (h MinHeap) Less(i, j int) bool {
	if h[i].freq != h[j].freq {
		return h[i].freq < h[j].freq
	}
	return h[i].val < h[j].val
}
func (h MinHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(Item))
}
func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	it := old[n-1]
	*h = old[:n-1]
	return it
}

// better returns true if a has higher priority than b.
func better(a, b Item) bool {
	if a.freq != b.freq {
		return a.freq > b.freq
	}
	return a.val > b.val
}

func findXSum(nums []int, k int, x int) []int64 {
	n := len(nums)
	ans := make([]int64, n-k+1)

	freqMap := make(map[int]int) // current frequencies
	inTop := make(map[int]bool)  // whether a value is currently in the top set

	var maxRest MaxHeap
	var minTop MinHeap
	heap.Init(&maxRest)
	heap.Init(&minTop)

	topSize := 0
	var sumTop int64 = 0

	// initialize first window
	for i := 0; i < k; i++ {
		v := nums[i]
		oldFreq := freqMap[v]
		newFreq := oldFreq + 1
		freqMap[v] = newFreq
		if inTop[v] {
			sumTop -= int64(v) * int64(oldFreq)
			sumTop += int64(v) * int64(newFreq)
			heap.Push(&minTop, Item{v, newFreq})
		} else {
			heap.Push(&maxRest, Item{v, newFreq})
		}
	}

	desired := x
	if len(freqMap) < desired {
		desired = len(freqMap)
	}
	for topSize < desired {
		// pop valid from maxRest
		for maxRest.Len() > 0 {
			it := maxRest[0]
			curFreq, ok := freqMap[it.val]
			if !ok || curFreq != it.freq || inTop[it.val] {
				heap.Pop(&maxRest)
				continue
			}
			heap.Pop(&maxRest)
			inTop[it.val] = true
			topSize++
			sumTop += int64(it.val) * int64(it.freq)
			heap.Push(&minTop, Item{it.val, it.freq})
			break
		}
	}

	ans[0] = sumTop

	// slide the window
	for i := 1; i <= n-k; i++ {
		outVal := nums[i-1]

		// decrement outVal
		oldFreq := freqMap[outVal]
		newFreq := oldFreq - 1
		if inTop[outVal] {
			sumTop -= int64(outVal) * int64(oldFreq)
			if newFreq > 0 {
				sumTop += int64(outVal) * int64(newFreq)
				heap.Push(&minTop, Item{outVal, newFreq})
			}
		} else {
			if newFreq > 0 {
				heap.Push(&maxRest, Item{outVal, newFreq})
			}
		}
		if newFreq == 0 {
			delete(freqMap, outVal)
			if inTop[outVal] {
				inTop[outVal] = false
				topSize--
			}
		} else {
			freqMap[outVal] = newFreq
		}

		// add incoming value
		inVal := nums[i+k-1]
		oldFreq = freqMap[inVal]
		newFreq = oldFreq + 1
		freqMap[inVal] = newFreq
		if inTop[inVal] {
			sumTop -= int64(inVal) * int64(oldFreq)
			sumTop += int64(inVal) * int64(newFreq)
			heap.Push(&minTop, Item{inVal, newFreq})
		} else {
			heap.Push(&maxRest, Item{inVal, newFreq})
		}

		// rebalance size to desired
		desired = x
		if len(freqMap) < desired {
			desired = len(freqMap)
		}
		for topSize > desired {
			// move worst from top to rest
			for minTop.Len() > 0 {
				it := minTop[0]
				curFreq, ok := freqMap[it.val]
				if !ok || curFreq != it.freq || !inTop[it.val] {
					heap.Pop(&minTop)
					continue
				}
				heap.Pop(&minTop)
				inTop[it.val] = false
				topSize--
				sumTop -= int64(it.val) * int64(it.freq)
				heap.Push(&maxRest, Item{it.val, it.freq})
				break
			}
		}
		for topSize < desired {
			// move best from rest to top
			for maxRest.Len() > 0 {
				it := maxRest[0]
				curFreq, ok := freqMap[it.val]
				if !ok || curFreq != it.freq || inTop[it.val] {
					heap.Pop(&maxRest)
					continue
				}
				heap.Pop(&maxRest)
				inTop[it.val] = true
				topSize++
				sumTop += int64(it.val) * int64(it.freq)
				heap.Push(&minTop, Item{it.val, it.freq})
				break
			}
		}

		// swap if a rest element outranks a top element
		for {
			var bestRest Item
			hasBest := false
			for maxRest.Len() > 0 {
				it := maxRest[0]
				curFreq, ok := freqMap[it.val]
				if !ok || curFreq != it.freq || inTop[it.val] {
					heap.Pop(&maxRest)
					continue
				}
				bestRest = it
				hasBest = true
				break
			}
			var worstTop Item
			hasWorst := false
			for minTop.Len() > 0 {
				it := minTop[0]
				curFreq, ok := freqMap[it.val]
				if !ok || curFreq != it.freq || !inTop[it.val] {
					heap.Pop(&minTop)
					continue
				}
				worstTop = it
				hasWorst = true
				break
			}
			if !hasBest || !hasWorst {
				break
			}
			if better(bestRest, worstTop) {
				// swap them
				heap.Pop(&maxRest)
				heap.Pop(&minTop)

				inTop[bestRest.val] = true
				inTop[worstTop.val] = false

				sumTop -= int64(worstTop.val) * int64(worstTop.freq)
				sumTop += int64(bestRest.val) * int64(bestRest.freq)

				heap.Push(&minTop, Item{bestRest.val, bestRest.freq})
				heap.Push(&maxRest, Item{worstTop.val, worstTop.freq})
			} else {
				break
			}
		}

		ans[i] = sumTop
	}

	return ans
}
```

## Ruby

```ruby
def find_x_sum(nums, k, x)
  # Heap implementation with custom comparator
  class Heap
    attr_reader :size
    def initialize(&comp)
      @data = []
      @comp = comp
    end

    def push(item)
      @data << item
      sift_up(@data.size - 1)
    end

    def pop
      return nil if @data.empty?
      top = @data[0]
      last = @data.pop
      unless @data.empty?
        @data[0] = last
        sift_down(0)
      end
      top
    end

    def peek
      @data[0]
    end

    def empty?
      @data.empty?
    end

    private

    def sift_up(idx)
      while idx > 0
        parent = (idx - 1) / 2
        break unless @comp.call(@data[idx], @data[parent])
        @data[idx], @data[parent] = @data[parent], @data[idx]
        idx = parent
      end
    end

    def sift_down(idx)
      n = @data.size
      loop do
        left = idx * 2 + 1
        right = left + 1
        best = idx
        if left < n && @comp.call(@data[left], @data[best])
          best = left
        end
        if right < n && @comp.call(@data[right], @data[best])
          best = right
        end
        break if best == idx
        @data[idx], @data[best] = @data[best], @data[idx]
        idx = best
      end
    end
  end

  # Comparator for max-heap (higher freq, then higher value)
  comp_max = ->(a, b) { a[0] > b[0] || (a[0] == b[0] && a[1] > b[1]) }
  # Comparator for min-heap (lower freq, then lower value)
  comp_min = ->(a, b) { a[0] < b[0] || (a[0] == b[0] && a[1] < b[1]) }

  max_heap = Heap.new(&comp_max)   # candidates
  sel_heap = Heap.new(&comp_min)   # selected top x

  freq = Hash.new(0)

  n = nums.length

  # build initial window frequencies
  (0...k).each do |i|
    v = nums[i]
    freq[v] += 1
  end

  # push distinct elements into max_heap
  freq.each do |v, f|
    max_heap.push([f, v])
  end

  # helper to clean stale top entries
  clean_top = lambda do |heap|
    while !heap.empty?
      f, v = heap.peek
      cur = freq[v]
      break if cur && cur == f
      heap.pop
    end
  end

  selected_sum = 0

  # fill selected heap with up to x best elements
  while sel_heap.size < x && !max_heap.empty?
    clean_top.call(max_heap)
    break if max_heap.empty?
    f, v = max_heap.pop
    sel_heap.push([f, v])
    selected_sum += f * v
  end

  ans = []
  ans << selected_sum

  (1..(n - k)).each do |i|
    out_val = nums[i - 1]
    in_val = nums[i + k - 1]

    # remove outgoing element
    old_f = freq[out_val]
    new_f = old_f - 1
    if new_f == 0
      freq.delete(out_val)
    else
      freq[out_val] = new_f
      max_heap.push([new_f, out_val])
    end

    # add incoming element
    old_f = freq[in_val] || 0
    new_f = old_f + 1
    freq[in_val] = new_f
    max_heap.push([new_f, in_val])

    # clean stale entries from selected heap top
    clean_top.call(sel_heap)

    # ensure selected size does not exceed x (possible after deletions)
    while sel_heap.size > x
      f, v = sel_heap.pop
      selected_sum -= f * v
      max_heap.push([f, v])
    end

    # fill up to x if possible
    while sel_heap.size < x && !max_heap.empty?
      clean_top.call(max_heap)
      break if max_heap.empty?
      f, v = max_heap.pop
      sel_heap.push([f, v])
      selected_sum += f * v
    end

    # swap if there is a better candidate outside
    loop do
      clean_top.call(sel_heap)
      clean_top.call(max_heap)
      break if sel_heap.empty? || max_heap.empty?
      sel_f, sel_v = sel_heap.peek
      cand_f, cand_v = max_heap.peek
      better = (cand_f > sel_f) || (cand_f == sel_f && cand_v > sel_v)
      break unless better
      # swap
      sel_heap.pop
      selected_sum -= sel_f * sel_v
      max_heap.pop
      sel_heap.push([cand_f, cand_v])
      selected_sum += cand_f * cand_v
      max_heap.push([sel_f, sel_v])
    end

    ans << selected_sum
  end

  ans
end
```

## Scala

```scala
import java.util.{TreeSet, Comparator}
import scala.collection.mutable

object Solution {
  case class Node(value: Int, freq: Int)

  def findXSum(nums: Array[Int], k: Int, x: Int): Array[Long] = {
    val cmp = new Comparator[Node] {
      override def compare(a: Node, b: Node): Int = {
        if (a.freq != b.freq) Integer.compare(a.freq, b.freq)
        else Integer.compare(a.value, b.value)
      }
    }

    val top = new TreeSet[Node](cmp)   // holds up to x elements with highest frequencies
    val rest = new TreeSet[Node](cmp)  // all other distinct elements

    val freq = mutable.HashMap[Int, Int]()          // value -> frequency in current window
    val inTop = mutable.HashMap[Int, Boolean]()     // value -> is it currently in top set
    var sumTop: Long = 0L

    def insertNode(node: Node): Unit = {
      if (top.size < x) {
        top.add(node)
        inTop(node.value) = true
        sumTop += node.value.toLong * node.freq
      } else {
        val minTop = top.first()
        if (cmp.compare(node, minTop) > 0) {
          // move minTop to rest, insert new node into top
          top.remove(minTop)
          sumTop -= minTop.value.toLong * minTop.freq
          inTop(minTop.value) = false
          rest.add(minTop)

          top.add(node)
          inTop(node.value) = true
          sumTop += node.value.toLong * node.freq
        } else {
          rest.add(node)
          inTop(node.value) = false
        }
      }
    }

    def rebalance(): Unit = {
      // fill top up to x elements if possible
      while (top.size < x && !rest.isEmpty) {
        val maxRest = rest.last()
        rest.remove(maxRest)
        top.add(maxRest)
        inTop(maxRest.value) = true
        sumTop += maxRest.value.toLong * maxRest.freq
      }
      // ensure ordering property: every element in top has freq >= any in rest
      var continue = true
      while (continue && !top.isEmpty && !rest.isEmpty) {
        val lowTop = top.first()
        val highRest = rest.last()
        if (cmp.compare(lowTop, highRest) < 0) {
          // swap them
          top.remove(lowTop)
          sumTop -= lowTop.value.toLong * lowTop.freq
          inTop(lowTop.value) = false
          rest.add(lowTop)

          rest.remove(highRest)
          top.add(highRest)
          inTop(highRest.value) = true
          sumTop += highRest.value.toLong * highRest.freq
        } else {
          continue = false
        }
      }
    }

    def addValue(v: Int): Unit = {
      val oldFreq = freq.getOrElse(v, 0)
      val newFreq = oldFreq + 1
      freq(v) = newFreq

      if (oldFreq > 0) {
        val oldNode = Node(v, oldFreq)
        if (inTop.getOrElse(v, false)) {
          top.remove(oldNode)
          sumTop -= v.toLong * oldFreq
        } else {
          rest.remove(oldNode)
        }
      }

      insertNode(Node(v, newFreq))
    }

    def removeValue(v: Int): Unit = {
      val oldFreq = freq(v) // must exist
      val newFreq = oldFreq - 1

      if (inTop.getOrElse(v, false)) {
        top.remove(Node(v, oldFreq))
        sumTop -= v.toLong * oldFreq
      } else {
        rest.remove(Node(v, oldFreq))
      }

      if (newFreq == 0) {
        freq.remove(v)
        inTop.remove(v)
      } else {
        freq(v) = newFreq
        insertNode(Node(v, newFreq))
      }
    }

    val n = nums.length
    val res = new Array[Long](n - k + 1)

    // initialize first window
    var i = 0
    while (i < k) {
      addValue(nums(i))
      i += 1
    }
    rebalance()
    res(0) = sumTop

    var left = 0
    var right = k
    while (right < n) {
      removeValue(nums(left))
      addValue(nums(right))
      rebalance()
      left += 1
      right += 1
      res(left) = sumTop
    }

    res
  }
}
```

## Rust

```rust
use std::collections::{HashMap, BTreeSet};

#[derive(Clone, Copy, Debug, Eq)]
struct Node {
    freq: i32,
    val: i32,
}

impl PartialEq for Node {
    fn eq(&self, other: &Self) -> bool {
        self.freq == other.freq && self.val == other.val
    }
}

// higher frequency first, if tie larger value first
impl Ord for Node {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        match self.freq.cmp(&other.freq).reverse() {
            std::cmp::Ordering::Equal => self.val.cmp(&other.val).reverse(),
            ord => ord,
        }
    }
}
impl PartialOrd for Node {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

impl Solution {
    pub fn find_x_sum(nums: Vec<i32>, k: i32, x: i32) -> Vec<i64> {
        let n = nums.len();
        let k_usize = k as usize;
        let x_usize = x as usize;

        let mut cnt: HashMap<i32, i32> = HashMap::new();
        let mut top: BTreeSet<Node> = BTreeSet::new();   // best up to x elements
        let mut rest: BTreeSet<Node> = BTreeSet::new();  // the others
        let mut sum_top: i64 = 0;
        let mut ans: Vec<i64> = Vec::with_capacity(n - k_usize + 1);

        // helper to rebalance sets after any change
        let mut balance = |top: &mut BTreeSet<Node>,
                           rest: &mut BTreeSet<Node>,
                           cnt_len: usize,
                           sum_top: &mut i64| {
            let desired = std::cmp::min(x_usize, cnt_len);

            // fill top up to desired
            while top.len() < desired {
                if let Some(&node) = rest.iter().next() {
                    rest.remove(&node);
                    top.insert(node);
                    *sum_top += (node.val as i64) * (node.freq as i64);
                } else {
                    break;
                }
            }

            // shrink top if too many
            while top.len() > desired {
                if let Some(&node) = top.iter().next_back() {
                    top.remove(&node);
                    *sum_top -= (node.val as i64) * (node.freq as i64);
                    rest.insert(node);
                } else {
                    break;
                }
            }

            // ensure ordering property
            loop {
                let worst_top_opt = top.iter().next_back().cloned();
                let best_rest_opt = rest.iter().next().cloned();
                match (worst_top_opt, best_rest_opt) {
                    (Some(wt), Some(br)) => {
                        // if br is better than wt according to ordering
                        if br < wt {
                            top.remove(&wt);
                            *sum_top -= (wt.val as i64) * (wt.freq as i64);
                            rest.insert(wt);

                            rest.remove(&br);
                            top.insert(br);
                            *sum_top += (br.val as i64) * (br.freq as i64);
                        } else {
                            break;
                        }
                    }
                    _ => break,
                }
            }
        };

        // functions to add/remove a number
        let mut add = |num: i32,
                       cnt: &mut HashMap<i32, i32>,
                       top: &mut BTreeSet<Node>,
                       rest: &mut BTreeSet<Node>,
                       sum_top: &mut i64| {
            let old = *cnt.get(&num).unwrap_or(&0);
            if old > 0 {
                let node_old = Node { freq: old, val: num };
                if top.remove(&node_old) {
                    *sum_top -= (num as i64) * (old as i64);
                } else {
                    rest.remove(&node_old);
                }
            }
            let new_cnt = old + 1;
            cnt.insert(num, new_cnt);
            let node_new = Node { freq: new_cnt, val: num };
            // insert into rest first; balance will move it if needed
            rest.insert(node_new);
        };

        let mut remove = |num: i32,
                          cnt: &mut HashMap<i32, i32>,
                          top: &mut BTreeSet<Node>,
                          rest: &mut BTreeSet<Node>,
                          sum_top: &mut i64| {
            if let Some(&old) = cnt.get(&num) {
                let node_old = Node { freq: old, val: num };
                if top.remove(&node_old) {
                    *sum_top -= (num as i64) * (old as i64);
                } else {
                    rest.remove(&node_old);
                }
                if old == 1 {
                    cnt.remove(&num);
                } else {
                    let new_cnt = old - 1;
                    cnt.insert(num, new_cnt);
                    let node_new = Node { freq: new_cnt, val: num };
                    rest.insert(node_new);
                }
            }
        };

        // build initial window
        for i in 0..k_usize {
            add(nums[i], &mut cnt, &mut top, &mut rest, &mut sum_top);
        }
        balance(&mut top, &mut rest, cnt.len(), &mut sum_top);
        ans.push(sum_top);

        // slide the window
        for i in k_usize..n {
            let out = nums[i - k_usize];
            let inn = nums[i];
            remove(out, &mut cnt, &mut top, &mut rest, &mut sum_top);
            add(inn, &mut cnt, &mut top, &mut rest, &mut sum_top);
            balance(&mut top, &mut rest, cnt.len(), &mut sum_top);
            ans.push(sum_top);
        }

        ans
    }
}
```

## Racket

```racket
(require data/heap)

(define (find-x-sum nums k x)
  (let* ([n (length nums)]
         [freq-hash (make-hash)]          ; val -> count
         [inTop-hash (make-hash)]        ; val -> boolean
         [top-heap (make-heap
                    (lambda (a b)
                      (or (< (first a) (first b))
                          (and (= (first a) (first b)) (< (second a) (second b))))))]
         [rest-heap (make-heap
                     (lambda (a b)
                       (or (> (first a) (first b))
                           (and (= (first a) (first b)) (> (second a) (second b))))))]
         [sumTop 0]
         [sizeTop 0])

    ;; helper to get valid entry from top-heap (worst in top)
    (define (pop-worst-top!)
      (let loop ()
        (if (heap-empty? top-heap)
            #f
            (let* ([e (heap-peek top-heap)]
                   [cnt (first e)] [val (second e)])
              (if (and (hash-has-key? freq-hash val)
                       (= (hash-ref freq-hash val) cnt)
                       (hash-ref inTop-hash val #f))
                  (begin (heap-delete-min! top-heap) e)
                  (begin (heap-delete-min! top-heap) (loop)))))))

    ;; helper to get valid entry from rest-heap (best outside top)
    (define (pop-best-rest!)
      (let loop ()
        (if (heap-empty? rest-heap)
            #f
            (let* ([e (heap-peek rest-heap)]
                   [cnt (first e)] [val (second e)])
              (if (and (hash-has-key? freq-hash val)
                       (= (hash-ref freq-hash val) cnt)
                       (not (hash-ref inTop-hash val #f)))
                  (begin (heap-delete-min! rest-heap) e)
                  (begin (heap-delete-min! rest-heap) (loop)))))))

    ;; rebalance after any frequency change
    (define (rebalance!)
      (let loop ()
        (cond
          [(> sizeTop x)
           (let ([e (pop-worst-top!)])
             (when e
               (let* ([cnt (first e)] [val (second e)])
                 (hash-set! inTop-hash val #f)
                 (set! sumTop (- sumTop (* cnt val)))
                 (set! sizeTop (- sizeTop 1))
                 (heap-insert! rest-heap (list cnt val)))))
           (loop)]
          [(< sizeTop x)
           (let ([e (pop-best-rest!)])
             (when e
               (let* ([cnt (first e)] [val (second e)])
                 (hash-set! inTop-hash val #t)
                 (set! sumTop (+ sumTop (* cnt val)))
                 (set! sizeTop (+ sizeTop 1))
                 (heap-insert! top-heap (list cnt val)))))
           (loop)]
          [else
           ;; ensure ordering property between the two heaps
           (let ([worst (pop-worst-top!)]
                 [best  (pop-best-rest!)])
             (cond
               [(and worst best)
                (let* ([cntW (first worst)] [valW (second worst)]
                       [cntB (first best)]  [valB (second best)])
                  (if (or (< cntW cntB) (and (= cntW cntB) (< valW valB)))
                      ;; swap
                      (begin
                        (hash-set! inTop-hash valW #f)
                        (hash-set! inTop-hash valB #t)
                        (set! sumTop (- sumTop (* cntW valW)))
                        (set! sumTop (+ sumTop (* cntB valB)))
                        (heap-insert! rest-heap (list cntW valW))
                        (heap-insert! top-heap  (list cntB valB))
                        (rebalance!)) ; re‑check after swap
                      ;; keep as is, push back
                      (begin
                        (heap-insert! top-heap worst)
                        (heap-insert! rest-heap best)))))]
               [worst (heap-insert! top-heap worst)]
               [best  (heap-insert! rest-heap best)]))])))

    ;; increase count of a value
    (define (inc val)
      (let* ([old (hash-ref freq-hash val 0)]
             [new (+ old 1)])
        (hash-set! freq-hash val new)
        (if (= old 0)
            (begin
              (hash-set! inTop-hash val #f)
              (heap-insert! rest-heap (list new val)))
            (let ([in-top (hash-ref inTop-hash val)])
              (if in-top
                  (heap-insert! top-heap (list new val))
                  (heap-insert! rest-heap (list new val))))))
      (rebalance!))

    ;; decrease count of a value
    (define (dec val)
      (let* ([old (hash-ref freq-hash val)]
             [new (- old 1)])
        (if (= new 0)
            (begin
              (hash-remove! freq-hash val)
              (hash-set! inTop-hash val #f))
            (begin
              (hash-set! freq-hash val new)
              (let ([in-top (hash-ref inTop-hash val)])
                (if in-top
                    (heap-insert! top-heap (list new val))
                    (heap-insert! rest-heap (list new val))))))
        (rebalance!)))

    ;; build first window
    (for ([i (in-range k)])
      (inc (list-ref nums i)))
    (define result (list sumTop))

    ;; slide the window
    (let loop ((start 1))
      (when (<= (+ start k -1) (- n 1))
        (dec (list-ref nums (- start 1)))          ; outgoing
        (inc (list-ref nums (+ start k -1)))       ; incoming
        (set! result (append result (list sumTop)))
        (loop (+ start 1))))
    result))
```

## Erlang

```erlang
-spec find_x_sum(Nums :: [integer()], K :: integer(), X :: integer()) -> [integer()].
find_x_sum(Nums, K, X) ->
    NumsTuple = list_to_tuple(Nums),
    Len = tuple_size(NumsTuple),
    %% Initial empty state
    EmptyState = {#{}, #{}, gb_trees:empty(), gb_trees:empty(), 0, 0},
    %% Build first window
    State1 = build_initial_window(1, K, NumsTuple, X, EmptyState),
    Answer0 = [calc_answer(State1, X)],
    NumWindows = Len - K + 1,
    AnswersRev = slide_windows(2, NumWindows, NumsTuple, K, X, State1, Answer0),
    lists:reverse(AnswersRev).

%% Build the first window by adding elements indices From..To (inclusive)
build_initial_window(From, To, Tuple, X, State) when From =< To ->
    Val = element(From, Tuple),
    NewState = add_val(Val, X, State),
    build_initial_window(From + 1, To, Tuple, X, NewState);
build_initial_window(_, _, _, _, State) -> State.

%% Slide windows from StartIdx (window start index) to EndIdx
slide_windows(StartIdx, EndIdx, _Tuple, _K, _X, State, Acc) when StartIdx > EndIdx ->
    Acc;
slide_windows(StartIdx, EndIdx, Tuple, K, X, State, Acc) ->
    OutIdx = StartIdx - 1,
    InIdx = StartIdx + K - 1,
    OutVal = element(OutIdx, Tuple),
    InVal = element(InIdx, Tuple),
    State1 = remove_val(OutVal, X, State),
    State2 = add_val(InVal, X, State1),
    NewAns = calc_answer(State2, X),
    slide_windows(StartIdx + 1, EndIdx, Tuple, K, X, State2, [NewAns | Acc]).

%% Add a value to the current window
add_val(Val, X, {FreqMap, SetMap, TopTree, RestTree, SumTop, TotalSum}) ->
    OldFreq = maps:get(Val, FreqMap, 0),
    NewFreq = OldFreq + 1,
    FreqMap1 = maps:put(Val, NewFreq, FreqMap),
    case OldFreq of
        0 ->
            %% new distinct element goes to RestTree initially
            Key = {NewFreq, Val},
            RestTree1 = gb_trees:insert(Key, Val, RestTree),
            SetMap1 = maps:put(Val, rest, SetMap),
            SumTop1 = SumTop;
        _ ->
            CurrSet = maps:get(Val, SetMap),
            KeyOld = {OldFreq, Val},
            case CurrSet of
                top ->
                    TopTreeTmp = gb_trees:delete(KeyOld, TopTree),
                    SumTopTmp = SumTop - Val,
                    KeyNew = {NewFreq, Val},
                    TopTree1 = gb_trees:insert(KeyNew, Val, TopTreeTmp),
                    SetMap1 = SetMap,
                    SumTop1 = SumTopTmp + Val;
                rest ->
                    RestTreeTmp = gb_trees:delete(KeyOld, RestTree),
                    KeyNew = {NewFreq, Val},
                    RestTree1 = gb_trees:insert(KeyNew, Val, RestTreeTmp),
                    SetMap1 = SetMap,
                    TopTree1 = TopTree,
                    SumTop1 = SumTop
            end,
            %% unify variables for later rebalance
            case CurrSet of
                top -> {FreqMap1, SetMap1, TopTree1, RestTree, SumTop1};
                rest -> {FreqMap1, SetMap1, TopTree, RestTree1, SumTop1}
            end
    end,
    %% unify after handling both cases
    case OldFreq of
        0 ->
            StateTmp = {FreqMap1, SetMap1, TopTree, RestTree, SumTop1, TotalSum + Val};
        _ ->
            case maps:get(Val, SetMap) of
                top -> StateTmp = {FreqMap1, SetMap1, TopTree1, RestTree, SumTop1, TotalSum + Val};
                rest -> StateTmp = {FreqMap1, SetMap1, TopTree, RestTree1, SumTop1, TotalSum + Val}
            end
    end,
    rebalance(X, StateTmp).

%% Remove a value leaving the window
remove_val(Val, X, {FreqMap, SetMap, TopTree, RestTree, SumTop, TotalSum}) ->
    OldFreq = maps:get(Val, FreqMap),
    NewFreq = OldFreq - 1,
    CurrSet = maps:get(Val, SetMap),
    KeyOld = {OldFreq, Val},
    case CurrSet of
        top ->
            TopTreeTmp = gb_trees:delete(KeyOld, TopTree),
            SumTopTmp = SumTop - Val;
        rest ->
            RestTreeTmp = gb_trees:delete(KeyOld, RestTree),
            SumTopTmp = SumTop
    end,
    case NewFreq of
        0 ->
            FreqMap1 = maps:remove(Val, FreqMap),
            SetMap1 = maps:remove(Val, SetMap),
            case CurrSet of
                top -> StateTmp = {FreqMap1, SetMap1, TopTreeTmp, RestTree, SumTopTmp, TotalSum - Val};
                rest -> StateTmp = {FreqMap1, SetMap1, TopTree, RestTreeTmp, SumTopTmp, TotalSum - Val}
            end;
        _ ->
            FreqMap1 = maps:put(Val, NewFreq, FreqMap),
            KeyNew = {NewFreq, Val},
            case CurrSet of
                top ->
                    TopTree1 = gb_trees:insert(KeyNew, Val, TopTreeTmp),
                    SumTop1 = SumTopTmp + Val,
                    SetMap1 = SetMap,
                    StateTmp = {FreqMap1, SetMap1, TopTree1, RestTree, SumTop1, TotalSum - Val};
                rest ->
                    RestTree1 = gb_trees:insert(KeyNew, Val, RestTreeTmp),
                    SumTop1 = SumTopTmp,
                    SetMap1 = SetMap,
                    StateTmp = {FreqMap1, SetMap1, TopTree, RestTree1, SumTop1, TotalSum - Val}
            end
    end,
    rebalance(X, StateTmp).

%% Rebalance the two trees to satisfy size and ordering constraints
rebalance(X, State) ->
    rebalance_step(X, State).

rebalance_step(X, {FreqMap, SetMap, TopTree, RestTree, SumTop, TotalSum}=State) ->
    SizeTop = gb_trees:size(TopTree),
    Cond1 = SizeTop > X,
    Cond2 = (SizeTop < X) andalso not gb_trees:is_empty(RestTree),
    case {Cond1, Cond2} of
        {true, _} ->
            {TopT1, RestT1, SetM1, SumT1} = move_worst_to_rest(TopTree, RestTree, SetMap, SumTop),
            rebalance_step(X, {FreqMap, SetM1, TopT1, RestT1, SumT1, TotalSum});
        {false, true} ->
            {TopT1, RestT1, SetM1, SumT1} = move_best_to_top(TopTree, RestTree, SetMap, SumTop),
            rebalance_step(X, {FreqMap, SetM1, TopT1, RestT1, SumT1, TotalSum});
        _ ->
            case {gb_trees:is_empty(TopTree), gb_trees:is_empty(RestTree)} of
                {false, false} ->
                    {WorstKey, WorstVal} = gb_trees:smallest(TopTree),
                    {BestKey, BestVal} = gb_trees:largest(RestTree),
                    if erlang:'<'(WorstKey, BestKey) ->
                        TopT1 = gb_trees:delete(WorstKey, TopTree),
                        RestT1 = gb_trees:delete(BestKey, RestTree),
                        TopT2 = gb_trees:insert(BestKey, BestVal, TopT1),
                        RestT2 = gb_trees:insert(WorstKey, WorstVal, RestT1),
                        SetM1 = maps:put(WorstVal, rest,
                                 maps:put(BestVal, top, SetMap)),
                        SumTop1 = SumTop - WorstVal + BestVal,
                        rebalance_step(X, {FreqMap, SetM1, TopT2, RestT2, SumTop1, TotalSum});
                       true ->
                        {FreqMap, SetMap, TopTree, RestTree, SumTop, TotalSum}
                    end;
                _ -> {FreqMap, SetMap, TopTree, RestTree, SumTop, TotalSum}
            end
    end.

move_worst_to_rest(TopTree, RestTree, SetMap, SumTop) ->
    {WorstKey, WorstVal} = gb_trees:smallest(TopTree),
    TopT1 = gb_trees:delete(WorstKey, TopTree),
    RestT1 = gb_trees:insert(WorstKey, WorstVal, RestTree),
    SetM1 = maps:put(WorstVal, rest, SetMap),
    SumTop1 = SumTop - WorstVal,
    {TopT1, RestT1, SetM1, SumTop1}.

move_best_to_top(TopTree, RestTree, SetMap, SumTop) ->
    {BestKey, BestVal} = gb_trees:largest(RestTree),
    RestT1 = gb_trees:delete(BestKey, RestTree),
    TopT1 = gb_trees:insert(BestKey, BestVal, TopTree),
    SetM1 = maps:put(BestVal, top, SetMap),
    SumTop1 = SumTop + BestVal,
    {TopT1, RestT1, SetM1, SumTop1}.

%% Compute answer for current window
calc_answer({_, _, TopTree, RestTree, SumTop, TotalSum}, X) ->
    Distinct = gb_trees:size(TopTree) + gb_trees:size(RestTree),
    if Distinct < X -> TotalSum; true -> SumTop end.
```

## Elixir

```elixir
defmodule Solution do
  @spec find_x_sum(nums :: [integer], k :: integer, x :: integer) :: [integer]
  def find_x_sum(nums, k, x) do
    n = length(nums)
    arr = List.to_tuple(nums)

    # initial empty structures
    freq_map = %{}
    loc_map = %{}
    s_tree = :gb_trees.empty()
    r_tree = :gb_trees.empty()
    sum_s = 0

    # add first k elements
    {freq_map, loc_map, s_tree, r_tree, sum_s} =
      Enum.reduce(0..(k - 1), {freq_map, loc_map, s_tree, r_tree, sum_s}, fn i,
                                                                            {fm, lm, st, rt, ss} ->
        val = elem(arr, i)
        add(val, fm, lm, st, rt, ss, x)
      end)

    # rebalance after initial window
    {s_tree, r_tree, sum_s, loc_map} = rebalance(s_tree, r_tree, sum_s, loc_map, x)
    ans_rev = [sum_s]

    # slide the window
    {_, _, s_tree, r_tree, sum_s, loc_map, ans_rev} =
      Enum.reduce(k..(n - 1), {freq_map, loc_map, s_tree, r_tree, sum_s, loc_map, ans_rev},
        fn i,
           {fm, lm, st, rt, ss, lmap, a_rev} ->
          out_val = elem(arr, i - k)
          in_val = elem(arr, i)

          {fm1, lm1, st1, rt1, ss1} =
            remove(out_val, fm, lm, st, rt, ss, x)

          {fm2, lm2, st2, rt2, ss2} =
            add(in_val, fm1, lm1, st1, rt1, ss1, x)

          {st3, rt3, ss3, lm3} = rebalance(st2, rt2, ss2, lm2, x)
          {[ss3 | a_rev], {fm2, lm3, st3, rt3, ss3, lm3, [ss3 | a_rev]}}
        end)

    Enum.reverse(ans_rev)
  end

  # ---------- helpers ----------
  defp key(val, freq), do: {-freq, -val}

  defp add(val, freq_map, loc_map, s_tree, r_tree, sum_s, _x) do
    old_freq = Map.get(freq_map, val, 0)
    new_freq = old_freq + 1
    freq_map = Map.put(freq_map, val, new_freq)

    {s_tree, r_tree, sum_s, loc_map} =
      case Map.get(loc_map, val) do
        :s ->
          # remove from S
          s_tree = delete_from_tree(s_tree, val, old_freq)
          sum_s = sum_s - val * old_freq
          {s_tree, r_tree, sum_s, Map.put(loc_map, val, nil)}
        :r ->
          r_tree = delete_from_tree(r_tree, val, old_freq)
          {s_tree, r_tree, sum_s, Map.put(loc_map, val, nil)}
        _ ->
          {s_tree, r_tree, sum_s, loc_map}
      end

    # insert into R with new frequency
    r_tree = insert_into_tree(r_tree, val, new_freq)
    loc_map = Map.put(loc_map, val, :r)

    {freq_map, loc_map, s_tree, r_tree, sum_s}
  end

  defp remove(val, freq_map, loc_map, s_tree, r_tree, sum_s, _x) do
    old_freq = Map.get(freq_map, val)
    new_freq = old_freq - 1

    {s_tree, r_tree, sum_s, loc_map} =
      case Map.get(loc_map, val) do
        :s ->
          s_tree = delete_from_tree(s_tree, val, old_freq)
          sum_s = sum_s - val * old_freq
          {s_tree, r_tree, sum_s, Map.put(loc_map, val, nil)}
        :r ->
          r_tree = delete_from_tree(r_tree, val, old_freq)
          {s_tree, r_tree, sum_s, Map.put(loc_map, val, nil)}
        _ ->
          {s_tree, r_tree, sum_s, loc_map}
      end

    if new_freq == 0 do
      freq_map = Map.delete(freq_map, val)
      loc_map = Map.delete(loc_map, val)
      {freq_map, loc_map, s_tree, r_tree, sum_s}
    else
      freq_map = Map.put(freq_map, val, new_freq)
      r_tree = insert_into_tree(r_tree, val, new_freq)
      loc_map = Map.put(loc_map, val, :r)
      {freq_map, loc_map, s_tree, r_tree, sum_s}
    end
  end

  defp delete_from_tree(tree, val, freq) do
    :gb_trees.delete(key(val, freq), tree)
  end

  defp insert_into_tree(tree, val, freq) do
    :gb_trees.enter(key(val, freq), {val, freq}, tree)
  end

  # rebalance to keep S size = min(x, total distinct) and ordering invariant
  defp rebalance(s_tree, r_tree, sum_s, loc_map, x) do
    total = :gb_trees.size(s_tree) + :gb_trees.size(r_tree)
    target = min(x, total)

    {s_tree, r_tree, sum_s, loc_map} =
      ensure_size_up(s_tree, r_tree, sum_s, loc_map, target)

    {s_tree, r_tree, sum_s, loc_map} =
      ensure_size_down(s_tree, r_tree, sum_s, loc_map, target)

    order_swap(s_tree, r_tree, sum_s, loc_map)
  end

  defp ensure_size_up(s_tree, r_tree, sum_s, loc_map, target) do
    if :gb_trees.size(s_tree) < target do
      {{negf, negv}, {val, freq}} = :gb_trees.smallest(r_tree)
      r_tree = :gb_trees.delete({negf, negv}, r_tree)
      s_tree = :gb_trees.enter({negf, negv}, {val, freq}, s_tree)
      sum_s = sum_s + val * freq
      loc_map = Map.put(loc_map, val, :s)
      ensure_size_up(s_tree, r_tree, sum_s, loc_map, target)
    else
      {s_tree, r_tree, sum_s, loc_map}
    end
  end

  defp ensure_size_down(s_tree, r_tree, sum_s, loc_map, target) do
    if :gb_trees.size(s_tree) > target do
      {{negf, negv}, {val, freq}} = :gb_trees.largest(s_tree)
      s_tree = :gb_trees.delete({negf, negv}, s_tree)
      r_tree = :gb_trees.enter({negf, negv}, {val, freq}, r_tree)
      sum_s = sum_s - val * freq
      loc_map = Map.put(loc_map, val, :r)
      ensure_size_down(s_tree, r_tree, sum_s, loc_map, target)
    else
      {s_tree, r_tree, sum_s, loc_map}
    end
  end

  defp order_swap(s_tree, r_tree, sum_s, loc_map) do
    if not :gb_trees.is_empty(s_tree) and not :gb_trees.is_empty(r_tree) do
      {{negf_s, negv_s}, {val_s, freq_s}} = :gb_trees.largest(s_tree)
      {{negf_r, negv_r}, {val_r, freq_r}} = :gb_trees.smallest(r_tree)

      if {negf_s, negv_s} > {negf_r, negv_r} do
        s_tree = :gb_trees.delete({negf_s, negv_s}, s_tree)
        r_tree = :gb_trees.delete({negf_r, negv_r}, r_tree)

        s_tree = :gb_trees.enter({negf_r, negv_r}, {val_r, freq_r}, s_tree)
        r_tree = :gb_trees.enter({negf_s, negv_s}, {val_s, freq_s}, r_tree)

        sum_s = sum_s - val_s * freq_s + val_r * freq_r
        loc_map =
          loc_map
          |> Map.put(val_s, :r)
          |> Map.put(val_r, :s)

        order_swap(s_tree, r_tree, sum_s, loc_map)
      else
        {s_tree, r_tree, sum_s, loc_map}
      end
    else
      {s_tree, r_tree, sum_s, loc_map}
    end
  end
end
```
