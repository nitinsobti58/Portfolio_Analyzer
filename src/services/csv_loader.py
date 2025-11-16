import pandas as pd
from pathlib import Path
from src.models.portfolio_model import PortfolioModel
from src.models.stock_position import StockPosition
#from src.models.portfolio_model import PortfolioModel


class CSVLoader:
    
    def load_csv():
        model=PortfolioModel()
        p=Path('data/crypto/')
        for x in p.glob('**/*.csv'):
            df=pd.read_csv(x)
            df = df.rename(columns=lambda x: x.replace(" ", "_"))
            for value in df.itertuples(index=False):
                position=StockPosition(value.Name,value.Account_Name ,value.Asset,value.Shares,"Crypto",value.Symbol)
                model.add_position(position)



        p=Path('data/stocks/')
        for x in p.glob('**/*.csv'):
            df=pd.read_csv(x)
            df = df.rename(columns=lambda x: x.replace(" ", "_"))
            for value in df.itertuples(index=False):
                position=StockPosition(value.Name,value.Account_Name ,value.Asset,value.Shares,"Stock",value.Symbol)
                model.add_position(position)
        return model

if __name__ == "__main__":
    model=CSVLoader.load_csv()
    for x in model.positions:
        x.toString()