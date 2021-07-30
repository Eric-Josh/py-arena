# If account balance is less than 100 print message”very less”
# If acc balance is greater than 100 and less than 1000 print “some savings in there”
# If account balance is greater than 1000 and less than 5000 Print message “weldone
# If balance is greater than 5000 print good savings

class Customer:
    
    # constructor
    def __init__(self, cust_name, cust_code, acct_type, acct_balance):
        self.cust_name = cust_name
        self.cust_code = cust_code
        self.acct_type = acct_type
        self.acct_balance = acct_balance
        
    # getters
    def get_custName(self):
        return self.cust_name
    def get_custCode(self):
        return self.cust_code
    def get_acctType(self):
        return self.acct_type
    def get_acctBalance(self):
        return self.acct_balance
    
    # setters
    def set_custName(self, cust_name):
        self.cust_name = cust_name
    def set_custCode(self, cust_code):
        self.cust_code = cust_code
    def set_acctType(self, acct_type):
        self.acct_type = acct_type
    def set_acctBalance(self, acct_balance):
        self.acct_balance = cust_balance
        
    # method to update cust account
    def account(self):
        if self.acct_balance < 100 :
            print('Very Less')
        elif 100 > self.acct_balance < 1000 :
            print('Some savings in there')
        elif 1000 > self.acct_balance < 5000 :
            print('Weldone')
        elif self.acct_balance > 5000 :
            print('Good savings')
            
# request input from customer
custName = input('Account Name: ')
custCode = input('Account Code: ')
accType = input('Account Type: ')
accBal = float(input('Account Balance: '))

custInput = Customer(custName, custCode, accType, accBal)

print('*' * 35)
print(custInput.get_custName())
print(custInput.get_custCode())
print(custInput.get_acctType())
print(custInput.get_acctBalance())
custInput.account()