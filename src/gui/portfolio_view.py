from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt

class PortfolioView(QTableWidget):

    def __init__(self, portfolio_model):
        super().__init__()
        self.portfolio_model = portfolio_model

        self.setColumnCount(6)
        self.setHorizontalHeaderLabels([
            "Brokerage", "Account", "Asset", "Quantity", "Asset Type", "Symbol"
        ])

        # Enable sorting + nicer layout
        self.setSortingEnabled(True)
        self.horizontalHeader().setStretchLastSection(True)

        self.populate_table()
        self.resizeColumnsToContents()

    def populate_table(self):
        positions = self.portfolio_model.positions
        self.setRowCount(len(positions))

        for i, position in enumerate(positions):
            self.setItem(i, 0, QTableWidgetItem(position.brokerage_name))
            self.setItem(i, 1, QTableWidgetItem(position.account_name))
            self.setItem(i, 2, QTableWidgetItem(position.asset_name))
            self.setItem(i, 3, QTableWidgetItem(str(position.quantity)))
            self.setItem(i, 4, QTableWidgetItem(position.asset_type))
            self.setItem(i, 5, QTableWidgetItem(position.symbol))
