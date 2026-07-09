# 2043. Simple Bank System

## Cpp

```cpp
class Bank {
public:
    Bank(std::vector<long long>& balance) : bal(balance) {}
    
    bool transfer(int account1, int account2, long long money) {
        if (!valid(account1) || !valid(account2)) return false;
        if (bal[account1 - 1] < money) return false;
        bal[account1 - 1] -= money;
        bal[account2 - 1] += money;
        return true;
    }
    
    bool deposit(int account, long long money) {
        if (!valid(account)) return false;
        bal[account - 1] += money;
        return true;
    }
    
    bool withdraw(int account, long long money) {
        if (!valid(account)) return false;
        if (bal[account - 1] < money) return false;
        bal[account - 1] -= money;
        return true;
    }
private:
    std::vector<long long> bal;
    bool valid(int account) const {
        return account >= 1 && account <= static_cast<int>(bal.size());
    }
};

/**
 * Your Bank object will be instantiated and called as such:
 * Bank* obj = new Bank(balance);
 * bool param_1 = obj->transfer(account1,account2,money);
 * bool param_2 = obj->deposit(account,money);
 * bool param_3 = obj->withdraw(account,money);
 */
```

## Java

```java
class Bank {
    private final long[] balances;

    public Bank(long[] balance) {
        this.balances = balance.clone();
    }

    private boolean isValid(int account) {
        return account >= 1 && account <= balances.length;
    }

    public boolean transfer(int account1, int account2, long money) {
        if (!isValid(account1) || !isValid(account2)) {
            return false;
        }
        int idx1 = account1 - 1;
        int idx2 = account2 - 1;
        if (balances[idx1] < money) {
            return false;
        }
        balances[idx1] -= money;
        balances[idx2] += money;
        return true;
    }

    public boolean deposit(int account, long money) {
        if (!isValid(account)) {
            return false;
        }
        balances[account - 1] += money;
        return true;
    }

    public boolean withdraw(int account, long money) {
        if (!isValid(account)) {
            return false;
        }
        int idx = account - 1;
        if (balances[idx] < money) {
            return false;
        }
        balances[idx] -= money;
        return true;
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * Bank obj = new Bank(balance);
 * boolean param_1 = obj.transfer(account1,account2,money);
 * boolean param_2 = obj.deposit(account,money);
 * boolean param_3 = obj.withdraw(account,money);
 */
```

## Python

```python
class Bank(object):
    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.bal = balance

    def _valid(self, account):
        return 1 <= account <= len(self.bal)

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if not (self._valid(account1) and self._valid(account2)):
            return False
        idx1 = account1 - 1
        idx2 = account2 - 1
        if self.bal[idx1] < money:
            return False
        self.bal[idx1] -= money
        self.bal[idx2] += money
        return True

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if not self._valid(account):
            return False
        self.bal[account - 1] += money
        return True

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if not self._valid(account):
            return False
        idx = account - 1
        if self.bal[idx] < money:
            return False
        self.bal[idx] -= money
        return True
```

## Python3

```python
from typing import List

class Bank:
    def __init__(self, balance: List[int]):
        self.bal = balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 1 <= account1 <= self.n and 1 <= account2 <= self.n:
            idx1 = account1 - 1
            idx2 = account2 - 1
            if self.bal[idx1] >= money:
                self.bal[idx1] -= money
                self.bal[idx2] += money
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if 1 <= account <= self.n:
            self.bal[account - 1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if 1 <= account <= self.n:
            idx = account - 1
            if self.bal[idx] >= money:
                self.bal[idx] -= money
                return True
        return False
```

## C

```c
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    long long *bal;
    int size;
} Bank;

Bank* bankCreate(long long* balance, int balanceSize) {
    Bank *obj = (Bank*)malloc(sizeof(Bank));
    obj->size = balanceSize;
    obj->bal = (long long*)malloc(sizeof(long long) * balanceSize);
    for (int i = 0; i < balanceSize; ++i) {
        obj->bal[i] = balance[i];
    }
    return obj;
}

bool bankTransfer(Bank* obj, int account1, int account2, long long money) {
    if (!obj) return false;
    if (account1 < 1 || account1 > obj->size) return false;
    if (account2 < 1 || account2 > obj->size) return false;
    if (obj->bal[account1 - 1] < money) return false;
    obj->bal[account1 - 1] -= money;
    obj->bal[account2 - 1] += money;
    return true;
}

bool bankDeposit(Bank* obj, int account, long long money) {
    if (!obj) return false;
    if (account < 1 || account > obj->size) return false;
    obj->bal[account - 1] += money;
    return true;
}

bool bankWithdraw(Bank* obj, int account, long long money) {
    if (!obj) return false;
    if (account < 1 || account > obj->size) return false;
    if (obj->bal[account - 1] < money) return false;
    obj->bal[account - 1] -= money;
    return true;
}

void bankFree(Bank* obj) {
    if (!obj) return;
    free(obj->bal);
    free(obj);
}
```

## Csharp

```csharp
public class Bank
{
    private readonly long[] _balances;

    public Bank(long[] balance)
    {
        _balances = new long[balance.Length];
        System.Array.Copy(balance, _balances, balance.Length);
    }

    public bool Transfer(int account1, int account2, long money)
    {
        if (!IsValid(account1) || !IsValid(account2))
            return false;
        int idx1 = account1 - 1;
        int idx2 = account2 - 1;
        if (_balances[idx1] < money)
            return false;
        _balances[idx1] -= money;
        _balances[idx2] += money;
        return true;
    }

    public bool Deposit(int account, long money)
    {
        if (!IsValid(account))
            return false;
        int idx = account - 1;
        _balances[idx] += money;
        return true;
    }

    public bool Withdraw(int account, long money)
    {
        if (!IsValid(account))
            return false;
        int idx = account - 1;
        if (_balances[idx] < money)
            return false;
        _balances[idx] -= money;
        return true;
    }

    private bool IsValid(int account)
    {
        return account >= 1 && account <= _balances.Length;
    }
}
```

## Javascript

```javascript
/**
 * @param {number[]} balance
 */
var Bank = function(balance) {
    this.balances = balance; // 0-indexed array, accounts are 1-indexed
};

/** 
 * @param {number} account1 
 * @param {number} account2 
 * @param {number} money
 * @return {boolean}
 */
Bank.prototype.transfer = function(account1, account2, money) {
    const n = this.balances.length;
    if (account1 < 1 || account1 > n || account2 < 1 || account2 > n) return false;
    const idx1 = account1 - 1;
    const idx2 = account2 - 1;
    if (this.balances[idx1] < money) return false;
    this.balances[idx1] -= money;
    this.balances[idx2] += money;
    return true;
};

/** 
 * @param {number} account 
 * @param {number} money
 * @return {boolean}
 */
Bank.prototype.deposit = function(account, money) {
    const n = this.balances.length;
    if (account < 1 || account > n) return false;
    const idx = account - 1;
    this.balances[idx] += money;
    return true;
};

/** 
 * @param {number} account 
 * @param {number} money
 * @return {boolean}
 */
Bank.prototype.withdraw = function(account, money) {
    const n = this.balances.length;
    if (account < 1 || account > n) return false;
    const idx = account - 1;
    if (this.balances[idx] < money) return false;
    this.balances[idx] -= money;
    return true;
};

/** 
 * Your Bank object will be instantiated and called as such:
 * var obj = new Bank(balance)
 * var param_1 = obj.transfer(account1,account2,money)
 * var param_2 = obj.deposit(account,money)
 * var param_3 = obj.withdraw(account,money)
 */
```

## Typescript

```typescript
class Bank {
    private balances: number[];

    constructor(balance: number[]) {
        this.balances = balance.slice();
    }

    private isValid(account: number): boolean {
        return account >= 1 && account <= this.balances.length;
    }

    transfer(account1: number, account2: number, money: number): boolean {
        if (!this.isValid(account1) || !this.isValid(account2)) return false;
        const idx1 = account1 - 1;
        if (this.balances[idx1] < money) return false;
        this.balances[idx1] -= money;
        this.balances[account2 - 1] += money;
        return true;
    }

    deposit(account: number, money: number): boolean {
        if (!this.isValid(account)) return false;
        this.balances[account - 1] += money;
        return true;
    }

    withdraw(account: number, money: number): boolean {
        if (!this.isValid(account)) return false;
        const idx = account - 1;
        if (this.balances[idx] < money) return false;
        this.balances[idx] -= money;
        return true;
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * var obj = new Bank(balance)
 * var param_1 = obj.transfer(account1,account2,money)
 * var param_2 = obj.deposit(account,money)
 * var param_3 = obj.withdraw(account,money)
 */
```

## Php

```php
class Bank {
    /**
     * @var int[]
     */
    private $balance;
    /**
     * @var int
     */
    private $n;

    /**
     * @param Integer[] $balance
     */
    function __construct($balance) {
        $this->balance = $balance; // 0-indexed internal storage
        $this->n = count($balance);
    }

    /**
     * @param Integer $account1
     * @param Integer $account2
     * @param Integer $money
     * @return Boolean
     */
    function transfer($account1, $account2, $money) {
        if ($account1 < 1 || $account1 > $this->n ||
            $account2 < 1 || $account2 > $this->n) {
            return false;
        }
        $i = $account1 - 1;
        $j = $account2 - 1;
        if ($this->balance[$i] < $money) {
            return false;
        }
        $this->balance[$i] -= $money;
        $this->balance[$j] += $money;
        return true;
    }

    /**
     * @param Integer $account
     * @param Integer $money
     * @return Boolean
     */
    function deposit($account, $money) {
        if ($account < 1 || $account > $this->n) {
            return false;
        }
        $i = $account - 1;
        $this->balance[$i] += $money;
        return true;
    }

    /**
     * @param Integer $account
     * @param Integer $money
     * @return Boolean
     */
    function withdraw($account, $money) {
        if ($account < 1 || $account > $this->n) {
            return false;
        }
        $i = $account - 1;
        if ($this->balance[$i] < $money) {
            return false;
        }
        $this->balance[$i] -= $money;
        return true;
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * $obj = new Bank($balance);
 * $ret_1 = $obj->transfer($account1, $account2, $money);
 * $ret_2 = $obj->deposit($account, $money);
 * $ret_3 = $obj->withdraw($account, $money);
 */
```

## Swift

```swift
class Bank {
    private var balances: [Int]

    init(_ balance: [Int]) {
        self.balances = balance
    }

    private func isValidAccount(_ account: Int) -> Bool {
        return account >= 1 && account <= balances.count
    }

    func transfer(_ account1: Int, _ account2: Int, _ money: Int) -> Bool {
        guard isValidAccount(account1), isValidAccount(account2) else { return false }
        let idx1 = account1 - 1
        let idx2 = account2 - 1
        if balances[idx1] < money { return false }
        balances[idx1] -= money
        balances[idx2] += money
        return true
    }

    func deposit(_ account: Int, _ money: Int) -> Bool {
        guard isValidAccount(account) else { return false }
        let idx = account - 1
        balances[idx] += money
        return true
    }

    func withdraw(_ account: Int, _ money: Int) -> Bool {
        guard isValidAccount(account) else { return false }
        let idx = account - 1
        if balances[idx] < money { return false }
        balances[idx] -= money
        return true
    }
}
```

## Kotlin

```kotlin
class Bank(private val balance: LongArray) {

    private fun isValid(account: Int): Boolean {
        return account in 1..balance.size
    }

    fun transfer(account1: Int, account2: Int, money: Long): Boolean {
        if (!isValid(account1) || !isValid(account2)) return false
        val idx1 = account1 - 1
        val idx2 = account2 - 1
        if (balance[idx1] < money) return false
        balance[idx1] -= money
        balance[idx2] += money
        return true
    }

    fun deposit(account: Int, money: Long): Boolean {
        if (!isValid(account)) return false
        val idx = account - 1
        balance[idx] += money
        return true
    }

    fun withdraw(account: Int, money: Long): Boolean {
        if (!isValid(account)) return false
        val idx = account - 1
        if (balance[idx] < money) return false
        balance[idx] -= money
        return true
    }
}
```

## Dart

```dart
class Bank {
  late List<int> _balance;

  Bank(List<int> balance) {
    // Store a mutable copy of balances (1-indexed accounts)
    _balance = List.from(balance);
  }

  bool transfer(int account1, int account2, int money) {
    if (!_isValidAccount(account1) || !_isValidAccount(account2)) return false;
    int idx1 = account1 - 1;
    int idx2 = account2 - 1;
    if (_balance[idx1] < money) return false;
    _balance[idx1] -= money;
    _balance[idx2] += money;
    return true;
  }

  bool deposit(int account, int money) {
    if (!_isValidAccount(account)) return false;
    _balance[account - 1] += money;
    return true;
  }

  bool withdraw(int account, int money) {
    if (!_isValidAccount(account)) return false;
    int idx = account - 1;
    if (_balance[idx] < money) return false;
    _balance[idx] -= money;
    return true;
  }

  bool _isValidAccount(int account) {
    return account >= 1 && account <= _balance.length;
  }
}

/**
 * Your Bank object will be instantiated and called as such:
 * Bank obj = Bank(balance);
 * bool param1 = obj.transfer(account1,account2,money);
 * bool param2 = obj.deposit(account,money);
 * bool param3 = obj.withdraw(account,money);
 */
```

## Golang

```go
type Bank struct {
	balances []int64
}

func Constructor(balance []int64) Bank {
	// make a copy to avoid external modifications
	b := make([]int64, len(balance))
	copy(b, balance)
	return Bank{balances: b}
}

// Transfer transfers money from account1 to account2 if possible.
func (this *Bank) Transfer(account1 int, account2 int, money int64) bool {
	n := len(this.balances)
	if account1 < 1 || account1 > n || account2 < 1 || account2 > n {
		return false
	}
	idx1, idx2 := account1-1, account2-1
	if this.balances[idx1] < money {
		return false
	}
	this.balances[idx1] -= money
	this.balances[idx2] += money
	return true
}

// Deposit adds money to the specified account if it exists.
func (this *Bank) Deposit(account int, money int64) bool {
	n := len(this.balances)
	if account < 1 || account > n {
		return false
	}
	idx := account - 1
	this.balances[idx] += money
	return true
}

// Withdraw subtracts money from the specified account if possible.
func (this *Bank) Withdraw(account int, money int64) bool {
	n := len(this.balances)
	if account < 1 || account > n {
		return false
	}
	idx := account - 1
	if this.balances[idx] < money {
		return false
	}
	this.balances[idx] -= money
	return true
}

/**
 * Your Bank object will be instantiated and called as such:
 * obj := Constructor(balance);
 * param_1 := obj.Transfer(account1,account2,money);
 * param_2 := obj.Deposit(account,money);
 * param_3 := obj.Withdraw(account,money);
 */
```

## Ruby

```ruby
class Bank
  def initialize(balance)
    @balance = balance
    @n = balance.length
  end

  def transfer(account1, account2, money)
    return false unless valid?(account1) && valid?(account2)
    i1 = account1 - 1
    i2 = account2 - 1
    return false if @balance[i1] < money
    @balance[i1] -= money
    @balance[i2] += money
    true
  end

  def deposit(account, money)
    return false unless valid?(account)
    @balance[account - 1] += money
    true
  end

  def withdraw(account, money)
    return false unless valid?(account)
    i = account - 1
    return false if @balance[i] < money
    @balance[i] -= money
    true
  end

  private

  def valid?(account)
    account >= 1 && account <= @n
  end
end
```

## Scala

```scala
class Bank(_balance: Array[Long]) {
  private val balance = _balance

  def transfer(account1: Int, account2: Int, money: Long): Boolean = {
    if (account1 < 1 || account1 > balance.length ||
        account2 < 1 || account2 > balance.length) return false
    if (balance(account1 - 1) < money) return false
    balance(account1 - 1) -= money
    balance(account2 - 1) += money
    true
  }

  def deposit(account: Int, money: Long): Boolean = {
    if (account < 1 || account > balance.length) return false
    balance(account - 1) += money
    true
  }

  def withdraw(account: Int, money: Long): Boolean = {
    if (account < 1 || account > balance.length) return false
    if (balance(account - 1) < money) return false
    balance(account - 1) -= money
    true
  }
}

/**
 * Your Bank object will be instantiated and called as such:
 * val obj = new Bank(balance)
 * val param_1 = obj.transfer(account1,account2,money)
 * val param_2 = obj.deposit(account,money)
 * val param_3 = obj.withdraw(account,money)
 */
```

## Rust

```rust
use std::cell::RefCell;

struct Bank {
    balances: RefCell<Vec<i64>>,
}

impl Bank {
    fn new(balance: Vec<i64>) -> Self {
        Bank {
            balances: RefCell::new(balance),
        }
    }

    fn transfer(&self, account1: i32, account2: i32, money: i64) -> bool {
        let idx1 = (account1 - 1) as usize;
        let idx2 = (account2 - 1) as usize;
        let mut bal = self.balances.borrow_mut();
        if idx1 >= bal.len() || idx2 >= bal.len() {
            return false;
        }
        if bal[idx1] < money {
            return false;
        }
        bal[idx1] -= money;
        bal[idx2] += money;
        true
    }

    fn deposit(&self, account: i32, money: i64) -> bool {
        let idx = (account - 1) as usize;
        let mut bal = self.balances.borrow_mut();
        if idx >= bal.len() {
            return false;
        }
        bal[idx] += money;
        true
    }

    fn withdraw(&self, account: i32, money: i64) -> bool {
        let idx = (account - 1) as usize;
        let mut bal = self.balances.borrow_mut();
        if idx >= bal.len() || bal[idx] < money {
            return false;
        }
        bal[idx] -= money;
        true
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * let obj = Bank::new(balance);
 * let ret_1: bool = obj.transfer(account1, account2, money);
 * let ret_2: bool = obj.deposit(account, money);
 * let ret_3: bool = obj.withdraw(account, money);
 */
```

## Racket

```racket
(define bank%
  (class object%
    (super-new)
    (init-field balance)
    (define bal-vec (list->vector balance))
    (define (valid? acc)
      (and (>= acc 1) (<= acc (vector-length bal-vec))))
    (define/public (transfer account1 account2 money)
      (if (and (valid? account1) (valid? account2)
               (>= (vector-ref bal-vec (- account1 1)) money))
          (begin
            (vector-set! bal-vec (- account1 1)
                         (- (vector-ref bal-vec (- account1 1)) money))
            (vector-set! bal-vec (- account2 1)
                         (+ (vector-ref bal-vec (- account2 1)) money))
            #t)
          #f))
    (define/public (deposit account money)
      (if (valid? account)
          (begin
            (vector-set! bal-vec (- account 1)
                         (+ (vector-ref bal-vec (- account 1)) money))
            #t)
          #f))
    (define/public (withdraw account money)
      (if (and (valid? account)
               (>= (vector-ref bal-vec (- account 1)) money))
          (begin
            (vector-set! bal-vec (- account 1)
                         (- (vector-ref bal-vec (- account 1)) money))
            #t)
          #f))))
```

## Erlang

```erlang
-module(bank).

-export([bank_init_/1,
         bank_transfer/3,
         bank_deposit/2,
         bank_withdraw/2]).

-define(TABLE, bank_table).

%% Initialize balances
-spec bank_init_(Balance :: [integer()]) -> any().
bank_init_(Balance) ->
    case ets:info(?TABLE) of
        undefined -> ok;
        _Info -> ets:delete(?TABLE)
    end,
    ets:new(?TABLE, [named_table, public, set]),
    init_accounts(Balance, 1),
    ok.

init_accounts([], _) -> ok;
init_accounts([B|Rest], Id) ->
    ets:insert(?TABLE, {Id, B}),
    init_accounts(Rest, Id + 1).

%% Transfer money from Account1 to Account2
-spec bank_transfer(Account1 :: integer(), Account2 :: integer(), Money :: integer()) -> boolean().
bank_transfer(Account1, Account2, Money) when Money >= 0 ->
    case ets:lookup(?TABLE, Account1) of
        [{Account1, Bal1}] when Bal1 >= Money ->
            case ets:lookup(?TABLE, Account2) of
                [{Account2, _Bal2}] ->
                    ok = ets:update_counter(?TABLE, Account1, {2, -Money}),
                    ok = ets:update_counter(?TABLE, Account2, {2, Money}),
                    true;
                [] -> false
            end;
        _ -> false
    end.

%% Deposit money into an account
-spec bank_deposit(Account :: integer(), Money :: integer()) -> boolean().
bank_deposit(Account, Money) when Money >= 0 ->
    case ets:lookup(?TABLE, Account) of
        [{Account, _}] ->
            ok = ets:update_counter(?TABLE, Account, {2, Money}),
            true;
        [] -> false
    end.

%% Withdraw money from an account
-spec bank_withdraw(Account :: integer(), Money :: integer()) -> boolean().
bank_withdraw(Account, Money) when Money >= 0 ->
    case ets:lookup(?TABLE, Account) of
        [{Account, Bal}] when Bal >= Money ->
            ok = ets:update_counter(?TABLE, Account, {2, -Money}),
            true;
        _ -> false
    end.
```

## Elixir

```elixir
defmodule Bank do
  @spec init_(balance :: [integer]) :: any
  def init_(balance) do
    balances =
      balance
      |> Enum.with_index(1)
      |> Enum.into(%{}, fn {bal, idx} -> {idx, bal} end)

    case Process.whereis(__MODULE__) do
      nil ->
        {:ok, _pid} = Agent.start_link(fn -> balances end, name: __MODULE__)

      pid ->
        Agent.update(pid, fn _ -> balances end)
    end

    :ok
  end

  @spec transfer(account1 :: integer, account2 :: integer, money :: integer) :: boolean
  def transfer(account1, account2, money) do
    Agent.get_and_update(__MODULE__, fn state ->
      cond do
        not Map.has_key?(state, account1) or not Map.has_key?(state, account2) ->
          {false, state}

        state[account1] < money ->
          {false, state}

        true ->
          new_state =
            state
            |> Map.update!(account1, &(&1 - money))
            |> Map.update!(account2, &(&1 + money))

          {true, new_state}
      end
    end)
  end

  @spec deposit(account :: integer, money :: integer) :: boolean
  def deposit(account, money) do
    Agent.get_and_update(__MODULE__, fn state ->
      if Map.has_key?(state, account) do
        {true, Map.update!(state, account, &(&1 + money))}
      else
        {false, state}
      end
    end)
  end

  @spec withdraw(account :: integer, money :: integer) :: boolean
  def withdraw(account, money) do
    Agent.get_and_update(__MODULE__, fn state ->
      cond do
        not Map.has_key?(state, account) ->
          {false, state}

        state[account] < money ->
          {false, state}

        true ->
          {true, Map.update!(state, account, &(&1 - money))}
      end
    end)
  end
end
```
