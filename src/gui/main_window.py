from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
)
from src.gui.portfolio_view import PortfolioView


class MainWindow(QMainWindow):
    def __init__(self, portfolio_model):
        super().__init__()
        self.portfolio_model = portfolio_model

        # Window setup
        self.setWindowTitle("Portfolio Analyzer")
        self.resize(1000, 600)

        # Central widget + layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Portfolio table view
        self.table = PortfolioView(self.portfolio_model)
        self.layout.addWidget(self.table)


def run_app(portfolio_model):
    app = QApplication([])
    window = MainWindow(portfolio_model)
    window.show()
    app.exec()
