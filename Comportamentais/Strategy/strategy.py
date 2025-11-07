from abc import ABC, abstractmethod
import pandas as pd

class IExport(ABC):
    @abstractmethod
    def export(self):
        pass


class CSVExport(IExport):
    def __init__(self):
        super.__init__(self)

    def export(self):
        return "TEST"
    
class ExcelExport(IExport):
    def __init__(self):
        super().__init__()

    def export(self):
        return "TEST"
    
class JSONExport(IExport):
    def __init__(self):
        super().__init__()

    def export(self):
        return "TEST"