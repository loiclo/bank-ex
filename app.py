# Crééer une classe Bank qui contient une liste d'utilisateurs. (la banque doit avoir un nom et une ville en plus d'une liste de clients)
class Bank:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.userlist = []
        self.accounts = []  # Liste des comptes de la banque

    # Méthode pour ajouter des clients à la banque   
    def add_customer(self, customer):
        self.userlist.append(customer)

    # Méthode pour ajouter des comptes à la banque
    def add_account(self, account):
        self.accounts.append(account)


# Crééer une classe Account qui contient le solde, la date d'ouverture et l'intérêt.
# Il y aura deux types de comptes : un compte courant et un compte épargne (le compte épargne aura un taux d'intérêt).
class Account:
    def __init__(self, solde, opening_date, interest, type_account):
        self.solde = solde
        self.opening_date = opening_date
        self.interest = interest
        self.type_account = type_account


# Crééer une classe Customer qui contient le nom, l'âge et la banque.
class Customer:
    def __init__(self, name, age, bank):
        self.name = name
        self.age = age
        self.bank = bank
        self.accounts = []  # Liste des comptes du client
        self.bank.add_customer(self)

    # Méthode pour créer un compte courant
    def create_current_account(self, solde, opening_date):
        current_account = Account(solde, opening_date, 0, "courant")  # Ajout de "courant" comme type de compte
        self.accounts.append(current_account)
        self.bank.add_account(current_account)
        return current_account

    # Méthode pour créer un compte épargne
    def create_saving_account(self, solde, opening_date, interest):
        saving_account = Account(solde, opening_date, interest, "épargne")  # Ajout de "épargne" comme type de compte
        self.accounts.append(saving_account)
        self.bank.add_account(saving_account)
        return saving_account


# Déclaration de la banque
bank1 = Bank("ING", "city")

# Création d'un client
customer1 = Customer("Loic", 34, bank1)

# Création des comptes pour le client
customer1.create_current_account(1000, "13 mars")
customer1.create_saving_account(2000, "13 mars", 0.05)

# Affichage des comptes du client
# print(customer1.accounts)

for compte in customer1.accounts:
    print(f"  - Type : {compte.type_account}")
    print(f"    Solde : {compte.solde}")
    print(f"    Date d'ouverture : {compte.opening_date}")
    print(f"    Taux d'intérêt : {compte.interest}")