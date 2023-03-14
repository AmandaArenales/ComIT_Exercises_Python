"""Create a Person class, with attributes name, surname and phone. Check that the phone 
only accepts 9 digits. Create an Account class, with accountNumber, balance and owner attributes. 
The owner is a Person. Create a constructor with parameters and another without parameters, access 
methods and toString for these classes. Check that the balance of the account must not be less than 0. 
Create a method called transaction that enters as parameters quantity and transactionType; Transaction 
type is "withdrawal" or "deposit". If it is a withdrawal, the amount is subtracted from the balance, 
and if it is deposit the amount is increased to the balance. The transaction method must print the 
transaction type and the new balance. Create in a class called Main, two accounts belonging to two 
different people and make a deposit and a withdrawal in each account. Print the values of people and transactions."""

class Person:
    name = ""
    surname = ""
    phone = ""

    def __init__(self, *args):
        if (len(args) == 3):
            self.name = args[0]
            self.surname = args[1]
            self.phone = args[2]
    
    def __str__(self):
        return ("\nName: " + self.name + 
                "\nSurname: "+ self.surname + 
                "\nphone: " + str(self.phone))
    
    def get_name(self):
        return self.name
    
class Account:
    account_number = 0
    balance = 0
    owner = None

    def __init__(self, *args):
        if (len(args) == 3):
            self.account_number = args[0]
            self.balance = args[1]
            self.owner = args[2]

    def __str__(self):
        return ("\nAccount Number: " + str(self.account_number) +
                "\nBalance: "+ str(self.balance) + 
                "\nOwner: " + self.owner.get_name())
    
    def get_account_number (self):
        return self.account_number

    def get_owner (self):
        return self.owner.get_name()

    def transaction (self, quantity, transaction_type):
        if transaction_type == "withdrawal": 
            new_balance = self.balance - quantity
            if new_balance < 0:
                print(f"\nHello, {self.owner.get_name()}.")
                print("You don't have enough balance.")
            else:
                self.balance = new_balance
                print(f"\nHello, {self.owner.get_name()}.")
                print(f"Your withdrawal is concluded and you new balance is: {self.balance}")
        if transaction_type == "deposit":
            self.balance += quantity
            print(f"\nHello, {self.owner.get_name()}.")
            print(f"Your deposit is concluded and you new balance is: {self.balance}")

class Main:
    list_accounts = []

    def add_account(self, name, surname, phone, account, balance):
        person = Person(name, surname, phone)
        account = Account(account, balance, person)
        self.list_accounts.append(account)

    def search_account(self, account_number):
        for account in self.list_accounts:
            if account_number == account.get_account_number():
                return account

    def insert_new_data(self):
        print("\nCreating New Account")

        phone = ""
        name = input("\nPlease, insert the name: ")
        surname = input("Please, insert the surname: ")
        
        while len(phone) != 9:
            phone = input("Please, insert the phone: ")
            if len(phone) == 9:
                break
            else:
                print("The phone number doesn't have 9 digits. Please insert it again")
        
        account_number = int(input("Please, insert the account number: "))
        balance = int(input("Please, insert the balance: "))
        self.add_account(name, surname, phone, account_number, balance)

main = Main()

main.insert_new_data()

print ("\nTo do some transactions:")
account_number = int(input("\nPlease, insert the account number: "))
acc1 = main.search_account(account_number)
acc1.transaction(200, "deposit")
acc1.transaction(50, "withdrawal")

main.insert_new_data()
print ("\nTo do some transactions:")
account_number = int(input("Please, insert the account number: "))
acc2 = main.search_account(account_number)
acc2.transaction(100, "deposit")
acc2.transaction(25, "withdrawal")

print(acc1)
print(acc2)
