class ItemNotFoundError(Exception):
    
    def __init__(self, key):
        self.key = key

class ItemCannotBeUsedError(Exception):
    
    def __init__(self, key):
        self.key = key

class ItemPresetNotFoundError(Exception):
    def __init__(self, key):
        self.key = key