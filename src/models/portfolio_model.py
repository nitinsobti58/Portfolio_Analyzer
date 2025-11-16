from typing import List
from src.models.stock_position import StockPosition

class PortfolioModel:
    def __init__(self):
        self.positions: List[StockPosition] = []
    
    def add_position(self, position: StockPosition):
        self.positions.append(position)
