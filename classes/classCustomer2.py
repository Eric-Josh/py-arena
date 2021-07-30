class Customer:
    
    # constructor
    def __init__(self, customerID, customerName, yearsInvolved, discount):
        self.customerID = customerID
        self.customerName = customerName
        self.yearsInvolved = yearsInvolved
        self.discount = discount
        
    # getters
    def get_customerID(self):
        return self.customerID
    def get_customerName(self):
        return self.customerName
    def get_yearsInvolved(self):
        return self.yearsInvolved
    def get_discount(self):
        if self.yearsInvolved < 2 :
            self.discount = '20%'
        elif 2 < self.yearsInvolved < 5 :
            self.discount = '22%'
        elif 5 < self.yearsInvolved < 10 :
            self.discount = '28%'
        elif self.yearsInvolved > 10 :
            self.discount = '30%'
            
        return self.discount
    
    
    # setters
    def set_customerID(self, customerID):
        self.customerID = customerID
    def set_customerName(self, customerName):
        self.customerName = customerName
    def set_yearsInvolved(self, yearsInvolved):
        self.yearsInvolved = yearsInvolved
    def set_discount(self, discount):
        self.discount = discount
        
    
def displayInformation():
    customerID = input('Enter Customer ID: ')
    customerName = input('Enter Customer Name: ')
    yearsInvolved = int(input('Enter Number of years involved: '))
    discount = '0%'
    
    cutomerInfo = Customer(customerID, customerName, yearsInvolved, discount)
    
    print('=' * 40)
    print('CustomerID: '+ cutomerInfo.get_customerID())
    print('CustomerName: '+cutomerInfo.get_customerName())
    print('Years Involved: ',cutomerInfo.get_yearsInvolved())
    print('Discount: ',cutomerInfo.get_discount())


displayInformation()