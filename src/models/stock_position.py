#Class to store stock / crypto position

class StockPosition:
    def __init__(self,brokerage_name,account_name,asset_name, quantity,asset_type,symbol):
        self.brokerage_name = brokerage_name #Name
        self.account_name = account_name #Account Name
        self.asset_name = asset_name #Asset
        self.quantity = quantity #Shares
        self.asset_type = asset_type #Type
        self.symbol = symbol #Symbol
    
    def toString(self):
        print( f"{self.brokerage_name} {self.account_name} {self.asset_name} {self.quantity} {self.asset_type} {self.symbol}")