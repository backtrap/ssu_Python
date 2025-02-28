class BankAccount:
    def __init__(self, name, account_num, balance = 0):
        self.name = name
        self.account_num = account_num
        self.balance = balance
        
    def get_name(self):
        return self.name
    
    def get_balance(self):
        return self.balance
    
    def get_account_num(self):
        return self.account_num
    
    def deposit(self, money):
        self.balance += money
        print("{}원이 입금되었습니다. 잔고는 {}원입니다.".format(money, self.balance))
        return self.balance
        
    def withdraw(self, money):
        if self.balance - money > 0:
            self.balance -= money
        else:
            print("계좌 잔고는 %d원으로 인출 요구 금액 %d원보다 작습니다." %(self.balance, money))
            
    def __str__(self):
        return "%s님의 계좌 %s의 잔고는 %d원입니다." %(self.name, self.account_num, self.balance)
    
        
account1 = BankAccount('홍길동', '1234-0001')
print(account1)
account1.deposit(2000)
print(account1)
account1.withdraw(500)
print(account1)
account1.withdraw(5000)
