from pathlib import Path
import pandas

class ExcelDataSource():
    def get_students(self):
        path: Path = Path(__file__).parent.parent / "data" / "demo.xlsx"
        print("!!!!!!!!!!!!!!!!!!", path)
        return pandas.read_excel(path, sheet_name="Sheet JS")