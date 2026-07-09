# 0690. Employee Importance

## Cpp

```cpp
/*
// Definition for Employee.
class Employee {
public:
    int id;
    int importance;
    vector<int> subordinates;
};
*/

class Solution {
public:
    int getImportance(vector<Employee*> employees, int id) {
        unordered_map<int, Employee*> mp;
        for (auto e : employees) mp[e->id] = e;
        
        function<int(int)> dfs = [&](int curId) -> int {
            Employee* emp = mp[curId];
            int total = emp->importance;
            for (int subId : emp->subordinates) {
                total += dfs(subId);
            }
            return total;
        };
        
        return dfs(id);
    }
};
```

## Java

```java
/*
// Definition for Employee.
class Employee {
    public int id;
    public int importance;
    public List<Integer> subordinates;
};
*/

class Solution {
    public int getImportance(List<Employee> employees, int id) {
        Map<Integer, Employee> map = new HashMap<>();
        for (Employee e : employees) {
            map.put(e.id, e);
        }
        return dfs(id, map);
    }

    private int dfs(int id, Map<Integer, Employee> map) {
        Employee emp = map.get(id);
        int total = emp.importance;
        for (int subId : emp.subordinates) {
            total += dfs(subId, map);
        }
        return total;
    }
}
```

## Python

```python
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
        """
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        """
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        emp_map = {e.id: e for e in employees}
        
        def dfs(eid):
            emp = emp_map[eid]
            total = emp.importance
            for sub_id in emp.subordinates:
                total += dfs(sub_id)
            return total
        
        return dfs(id)
```

## Python3

```python
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: list[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

from typing import List

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_map = {e.id: e for e in employees}
        
        def dfs(eid: int) -> int:
            emp = emp_map[eid]
            total = emp.importance
            for sub_id in emp.subordinates:
                total += dfs(sub_id)
            return total
        
        return dfs(id)
```

## Csharp

```csharp
/*
// Definition for Employee.
class Employee {
    public int id;
    public int importance;
    public IList<int> subordinates;
}
*/

class Solution {
    public int GetImportance(IList<Employee> employees, int id) {
        var map = new Dictionary<int, Employee>();
        foreach (var e in employees) {
            map[e.id] = e;
        }

        int Dfs(int eid) {
            var emp = map[eid];
            int total = emp.importance;
            foreach (int subId in emp.subordinates) {
                total += Dfs(subId);
            }
            return total;
        }

        return Dfs(id);
    }
}
```

## Javascript

```javascript
/**
 * Definition for Employee.
 * function Employee(id, importance, subordinates) {
 *     this.id = id;
 *     this.importance = importance;
 *     this.subordinates = subordinates;
 * }
 */

/**
 * @param {Employee[]} employees
 * @param {number} id
 * @return {number}
 */
var GetImportance = function(employees, id) {
    const empMap = new Map();
    for (const e of employees) {
        empMap.set(e.id, e);
    }
    let total = 0;
    const stack = [id];
    while (stack.length) {
        const curId = stack.pop();
        const emp = empMap.get(curId);
        if (!emp) continue;
        total += emp.importance;
        for (const subId of emp.subordinates) {
            stack.push(subId);
        }
    }
    return total;
};
```

## Typescript

```typescript
/**
 * Definition for Employee.
 * class Employee {
 *     id: number
 *     importance: number
 *     subordinates: number[]
 *     constructor(id: number, importance: number, subordinates: number[]) {
 *         this.id = (id === undefined) ? 0 : id;
 *         this.importance = (importance === undefined) ? 0 : importance;
 *         this.subordinates = (subordinates === undefined) ? [] : subordinates;
 *     }
 * }
 */

function getImportance(employees: Employee[], id: number): number {
    const empMap = new Map<number, Employee>();
    for (const e of employees) {
        empMap.set(e.id, e);
    }

    let total = 0;
    const stack: number[] = [id];

    while (stack.length > 0) {
        const curId = stack.pop()!;
        const emp = empMap.get(curId);
        if (!emp) continue;
        total += emp.importance;
        for (const subId of emp.subordinates) {
            stack.push(subId);
        }
    }

    return total;
}
```

## Php

```php
/**
 * Definition for Employee.
 * class Employee {
 *     public $id = null;
 *     public $importance = null;
 *     public $subordinates = array();
 *     function __construct($id, $importance, $subordinates) {
 *         $this->id = $id;
 *         $this->importance = $importance;
 *         $this->subordinates = $subordinates;
 *     }
 * }
 */
class Solution {
    /**
     * @param Employee[] $employees
     * @param Integer $id
     * @return Integer
     */
    function getImportance($employees, $id) {
        $emap = [];
        foreach ($employees as $e) {
            $emap[$e->id] = $e;
        }
        $total = 0;
        $stack = [$id];
        while (!empty($stack)) {
            $curId = array_pop($stack);
            $emp = $emap[$curId];
            $total += $emp->importance;
            foreach ($emp->subordinates as $sub) {
                $stack[] = $sub;
            }
        }
        return $total;
    }
}
```

## Swift

```swift
/**
 * Definition for Employee.
 * public class Employee {
 *     public var id: Int
 *     public var importance: Int
 *     public var subordinates: [Int]
 *     public init(_ id: Int, _ importance: Int, _ subordinates: [Int]) {
 *         self.id = id
 *         self.importance = importance
 *         self.subordinates = subordinates
 *     }
 * }
 */

class Solution {
    func getImportance(_ employees: [Employee], _ id: Int) -> Int {
        var empMap = [Int: Employee]()
        for e in employees {
            empMap[e.id] = e
        }
        
        func dfs(_ curId: Int) -> Int {
            guard let emp = empMap[curId] else { return 0 }
            var total = emp.importance
            for subId in emp.subordinates {
                total += dfs(subId)
            }
            return total
        }
        
        return dfs(id)
    }
}
```

## Kotlin

```kotlin
/*
 * // Definition for Employee.
 * class Employee {
 *     var id: Int = 0
 *     var importance: Int = 0
 *     var subordinates: List<Int> = listOf()
 * }
 */

class Solution {
    fun getImportance(employees: List<Employee?>, id: Int): Int {
        val empMap = HashMap<Int, Employee>()
        for (e in employees) {
            if (e != null) {
                empMap[e.id] = e
            }
        }

        fun dfs(curId: Int): Int {
            val emp = empMap[curId] ?: return 0
            var total = emp.importance
            for (subId in emp.subordinates) {
                total += dfs(subId)
            }
            return total
        }

        return dfs(id)
    }
}
```

## Golang

```go
/**
 * Definition for Employee.
 * type Employee struct {
 *     Id int
 *     Importance int
 *     Subordinates []int
 * }
 */

func getImportance(employees []*Employee, id int) int {
    empMap := make(map[int]*Employee, len(employees))
    for _, e := range employees {
        empMap[e.Id] = e
    }

    var dfs func(int) int
    dfs = func(eid int) int {
        e := empMap[eid]
        total := e.Importance
        for _, subID := range e.Subordinates {
            total += dfs(subID)
        }
        return total
    }

    return dfs(id)
}
```

## Ruby

```ruby
=begin
# Definition for Employee.
class Employee
    attr_accessor :id, :importance, :subordinates
    def initialize( id, importance, subordinates)
        @id = id
        @importance = importance
        @subordinates = subordinates
    end
end
=end

# @param {Employee[]} employees
# @param {Integer} id
# @return {Integer}
def get_importance(employees, id)
  emp_map = {}
  employees.each { |e| emp_map[e.id] = e }

  dfs = lambda do |eid|
    emp = emp_map[eid]
    total = emp.importance
    emp.subordinates.each { |sub_id| total += dfs.call(sub_id) }
    total
  end

  dfs.call(id)
end
```

## Scala

```scala
// Definition for Employee.
class Employee() {
    var id: Int = 0
    var importance: Int = 0
    var subordinates: List[Int] = List()
};

object Solution {
    def getImportance(employees: List[Employee], id: Int): Int = {
        val empMap: Map[Int, Employee] = employees.map(e => e.id -> e).toMap
        def dfs(curId: Int): Int = {
            val emp = empMap(curId)
            emp.importance + emp.subordinates.map(dfs).sum
        }
        dfs(id)
    }
}
```
