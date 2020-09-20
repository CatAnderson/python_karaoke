class Guest:
    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet

    
    def alter_guests_wallet_amount(self, entrance_fee):
        if self.wallet < entrance_fee:
            return "Not enough money!"
        else:
            self.wallet -= entrance_fee
