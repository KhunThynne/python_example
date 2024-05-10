import datetime
import os


class ExportData():
    def __init__(self) -> None:     
        self.name = date_time = datetime.now().strftime("%Y%m%d%H%M%S")      
        self.createdirectory()
        
        pass
    def createdirectory(self,path_ex=False):
        path_ex = {path_ex if type(path_ex) !=bool else ""}
        coins_history_path = f"dataset/"
        indicators_path = f"indicators/{self.symbol}"
        try:
            os.makedirs(coins_history_path, exist_ok=True)
            os.makedirs(indicators_path, exist_ok=True)
        except:
            pass    
    def exportdata(self):
        pass
    