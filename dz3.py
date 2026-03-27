class BankAccount:
    def __init__(self, owner, acount_number, balance):
        self.owner = owner
        self.account_number = acount_number
        self.balance = balance
class Bank:
    def __init__(self):
        self.al_accounts = []
    def add_new_account(self, account):
        self.al_accounts.append(account)
        print("Рахунок додано :", account.owner)
    def deposit(self, number, money):
        for acc in self.al_accounts:
            if acc.account_number == number:
                acc.balance = acc.balance + money
                print("Баланс оновлен тепер там:", acc.balance)
    def withdraw(self, number, money):
        for acc in self.al_accounts:
            if acc.account_number == number:
                if acc.balance >= money:
                    acc.balance = acc.balance - money #😢
                    print("Ви зняли гроші зхалишилось:", acc.balance)
                else:
                    print("У вас мало грошей на рахунку")
    def transfer(self, from_num, to_num, money):
        seder = None
        receiver = None
        for acc in self.al_accounts:
            if acc.account_number == from_num:
                seder = acc
            if acc.account_number == to_num:
                receiver = acc
        if seder != None and receiver != None:
            if seder.balance >= money:
                seder.balance = seder.balance - money
                receiver.balance = receiver.balance + money
                print("переказ пройшов успішно")
            else:
                print("пемає грошей для переказу")
        else:
            print("Якийсь із рахунків не знайдено")
my_bank = Bank()
user1 = BankAccount("Іван", "111", 500)
user2 = BankAccount("Олена", "222", 1000)
my_bank.add_new_account(user1)
my_bank.add_new_account(user2)
my_bank.deposit("111", 200)
my_bank.withdraw("222", 100)
my_bank.transfer("222", "111", 300)
print(user1.owner, "має", user1.balance)
print(user2.owner, "має", user2.balance)