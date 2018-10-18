

class Customer:
    __slots__ = ("__id", "__name")
    __pid = 0
    
    def __init__(self, name):
        self.__name = name.title()
        self.__id = Customer.__pid
        Customer.__pid += 1
        
    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, name):
        self.__name = name.title()
        
    @property
    def id(self):
        return self.__id
        
    def __str__(self):
        return "{} ({})".format(self.__name, self.__id)
        
        
class Account:
    __slots__ = ( "__number", "__owner", "__balance", "__transactions")
    __accnumber = 1000000
    
    def __init__(self, owner):
        self.__owner = owner
        self.__balance = 0
        self.__transactions = []
        self.__number = Account.__accnumber
        Account.__accnumber += 1
        
        
    @property
    def number(self):
        return self.__number
        
    @property
    def owner(self):
        return self.__owner
        
    @property
    def balance(self):
        return self.__balance
        
    def doTransaction(self, transaction):
        self.__transactions.append(transaction)
        if transaction.source == self.number:
            self.__balance -= transaction.amount
        else:
            self.__balance += transaction.amount
            
    def listTransactions(self):
        for transaction in self.__transactions:
            print(transaction)
            
    def __str__(self):
        return "number: {}, owner id: {}, balance: {}".format(self.number, self.owner, self.balance)
        
        
        
class Transaction:
    __slots__ = ("__source", "__target", "__amount")
    
    def __init__(self, source, target, amount):
        self.__source = source
        self.__target = target
        self.__amount = amount
        
    @property
    def source(self):
        return self.__source
        
    @property
    def target(self):
        return self.__target
        
    @property
    def amount(self):
        return self.__amount
        
    def __str__(self):
        return "{} from {} to {}".format(self.__amount, self.__source, self.__target)
        
        
        
        
        
class Bank:
    __slots__ = ("__accounts", "__customers")

    def __init__(self):
        self.__accounts = []
        self.__customers = []
        
    def accountExists(self, accountNumber):
        for account in self.__accounts:
            if account.number == accountNumber:
                return (True, account)
        else:
            return (False, None)
        
    def addCustomer(self, customer):
        self.__customers.append(customer)
        
    def addAccount(self, customerID):
        self.__accounts.append(Account(customerID))
    
    def listCustomers(self):
        for customer in self.__customers:
            print(customer)
            
    def listAccounts(self):
        for account in self.__accounts:
            print(account)
            
    def listTransactions(self, accountNumber):
        (Exists, foundAc) = self.accountExists(accountNumber)
        if Exists == False:
            print("No such account found!")
        else:
            foundAc.listTransactions()
            
    def doTransaction(self, source, target, amount):
        (Exists, targetAc) = self.accountExists(target)
        if Exists == False:
            print("Illegal account number(s)!")
            return
        
        (Exists, sourceAc) = self.accountExists(source)
        if Exists == True:
            if sourceAc.balance < amount:
                print("Insufficient funds for payment!")
                return
            tsaction = Transaction(source, target, amount)
            sourceAc.doTransaction(tsaction)
            targetAc.doTransaction(tsaction)
        else:
            tsaction = Transaction(source, target, amount)
            targetAc.doTransaction(tsaction)
  