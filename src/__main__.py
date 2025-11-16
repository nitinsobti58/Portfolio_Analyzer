from src.services.csv_loader import CSVLoader
from src.gui.main_window import run_app


def main():
    portfolio_model = CSVLoader.load_csv()
    run_app(portfolio_model)


if __name__ == "__main__":
    main()
