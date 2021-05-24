class TableEntry:
    def __init__(key: list[str], value: list[str], timestamp: str, deleted: bool):
        self.key = key
        self.value = value
        self.timestamp = timestamp
        self.deleted: deleted

class MemTable:
    def __init__() -> MemTable:
        self.entries = list()
        self.size = 0
    
