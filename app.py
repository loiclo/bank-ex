class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = []
        self.accounts = []
    def add_client(self, client):
        self.clients.append(client)
    def add_account(self, account):
        self.accounts.append(account)

class User:
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.bank.add_client(self)
        self.comptes = []
    def add_new_account(somme = 0):
        #ligne qui va creer un nouveau compte
        #ligne qui va ajouter ce compte a mon user
        #ligne qui va ajouter ce compte a la banque
        return account

class Account:
    def __init__(self):
        print("coucou")

banque1 = Bank("BNP")
print("coucou")
client1 = User("Lucie", banque1)

print("coucou")
compte_de_lucie = client1.add_new_account(45)