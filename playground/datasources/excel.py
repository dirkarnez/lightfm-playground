from pathlib import Path
from pandas import DataFrame, read_excel
from playground.datasources.datasource import DataSource

class ExcelDataSource(DataSource):
    def __init__(self) -> None:
        self.path: Path = Path(__file__).parent.parent / "data" / "demo.xlsx"

    def get_students(self) -> DataFrame:
        return read_excel(self.path, sheet_name="users")
