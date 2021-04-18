class BankAccount(object):
    """Creates new backaccount object"""
    interestRate = .0125
    nextAccountNum = 123456

    def __init__(self, name, bal):
        """builds a Bankaccount Object"""
        self.name = name
        self.bal = bal
        self.accountNumber = BankAccount.nextAccountNum
        BankAccount.nextAccountNum += 1

    def __str__(self):
        """Defines how to print a BankAccount Object"""
        output = "Name: " + str(self.name) + "\n"
        output += "AccNum: " + str(self.accountNumber) + "\n"
        output += "Balance: " + str(self.bal) + "\n"
        return output
    
    def deposit(self, amount):
        self.bal += amount

    def withdraw(self, amount):
        if self.bal >= amount:
            self.bal -= amount
        else: 
            print("Account " + str(self.accountNumber))
            print("Does not have enough to withdraw", amount)
    
    def transferFunds(self, otherAccount, amount):
        if self.bal >= amount:
            self.bal -= amount
            otherAccount.bal += amount
        else: 
            print("Account " + str(self.accountNumber))
            print("Does not have enough to transfer to accNum", otherAccount.accountNumber)
            print()
    
    def depositInterest(self): 
        self.deposit(self.bal * BankAccount.interestRate)


if __name__ == '__main__':
    account1 = BankAccount("Brandon", 1250.00)
    print(account1)
    account1.depositInterest()
    print(account1)