class Atm():
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
    
    def cashWithdrawl(self):
        print("Cash has been withdrawn")

    def balanceInquiry(self):
        print("balance Inquired")

HDFC=Atm("5689433213213","₹3000")
print(HDFC.cardNumber)
print(HDFC.pinNumber)
