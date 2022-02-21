
import os
import json
from json import JSONEncoder



class ClassEncoder(JSONEncoder):
    def default(o):
        return o.__dict__



class PersistenceHanlder:
    relative_path_root = r'C:\Users\Utente 39\Documents\temp\github\projects\bank_managment_system_pro\Data'


    def __write_on_file__(self, value, path):
        f = open(path, 'a')
        f.write(value)
        f.close()

    def __read_file_bank__(self, value, path): 
        f = open(path, "r")
        f.read(value)
        f.close()

    def __remove_file__(self, path):
        os.remove(path)


    def bank_save_all(self, value):
        bankJSONData = json.dumps(value, indent = 4, cls = ClassEncoder)
        self.__write_on_file__(bankJSONData, self.relative_path_root + "/data_bank.json")

    def client_save_all(self, value):
        bankJSONData = json.dumps(value, indent = 4, cls = ClassEncoder)
        self.__write_on_file__(bankJSONData, self.relative_path_root + "/data_client.json")

    def count_save_all(self, value):
        bankJSONData = json.dumps(value, indent = 4, cls = ClassEncoder)
        self.__write_on_file__(bankJSONData, self.relative_path_root + "/data_count.json")

