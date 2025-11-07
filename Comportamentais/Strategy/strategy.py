from abc import ABC, abstractmethod
import pandas as pd
import json
import os

class IExport(ABC):
    @abstractmethod
    def export(self, df, output_path):
        pass


class CSVExport(IExport):
    def __init__(self):
        super.__init__(self)

    def export(self, df, output_path):
        try:
            return "TEST"
        
        except Exception as e:
            return "ERROR"
    
class ExcelExport(IExport):
    def __init__(self):
        super().__init__()

    def export(self, df, output_path):
        try:
            return "TEST"
        
        except Exception as e:
            return "ERROR"
    
class JSONExport(IExport):
    def __init__(self):
        super().__init__()

    def export(self, df, output_path):
        try:
            return "TEST"
        
        except Exception as e:
            return "ERROR"