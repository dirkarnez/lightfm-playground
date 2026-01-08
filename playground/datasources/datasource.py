from abc import ABC, abstractmethod
from pandas import DataFrame, read_excel

class DataSource(ABC): # Inherit from ABC
    @abstractmethod
    def get_students(self) -> DataFrame:
        pass
  