class Bank:
    def __init__(self,name, street, number, zip_code, city ):
        self.name = name
        self.street = street
        self.number = number
        self.zip_code = zip_code
        self.city = city
        self.userlist = []
        
    def add_customer(self, customer):
        self.userlist.append(customer)
        

        
class Account:
    
            
        
bank1 = Bank("ING", "street", "number", "zip_code", "city")


class Customer:
    def __init__(self,name, age, birth, street, number, zip_code, city, bank ):
        self.name = name
        self.age = age
        self.birth = birth
        self.street = street
        self.number = number
        self.zip_code = zip_code
        self.city = city
        self.bank = bank
        self.userlist = []
        bank.add_customer(self)
        
        
        
    def create_current_account(self, solde, opening_date, interest ):
    # customer et bank -> self.customer & self.bank ? ? ? 
    
    # self.add_customer ?  ? ? 

    
    
    

def create_saving_account(self, customer, bank, solde, opening_date, interest ):        
    
    
    self.sole = solde
    self.opening_date = opening_date
    self.interest = interest
        
        
        
        
customer1 = Customer("Loic", "34", "13 mars", "jhjhjh", "number", "zip_code", "city", bank1 )

# class Account



#cr