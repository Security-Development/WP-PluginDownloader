from json import load as json_load

class JsonTool:
    def __init__(self):
        pass
    
    def dump(self, file):
        with open(file, 'r', encoding='utf-8') as handle:
            return json_load(handle)
        
