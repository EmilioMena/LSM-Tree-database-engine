import bisect # binary search
import sys

class Entry:
    def __init__(key: str, value: str, deleted: bool):
        self.key = key
        self.value = value
        self.deleted = deleted # tombstone

    # required for bisect comparison
    def __lt__(self, other):
      return self.key < other.key

class Memtable:
    def __init__() -> Memtable:
        self.entries = list()
        self.keys = []
        self.size = 0

    def insert(self, key: str, value: str):
      """
      Insert a new entry into the Memtable.
      If entry is already present, update the value.
      """
      entry = Entry(key, value, False)
      result, idx = _get_index(key)
      if result:
        size_diff = sys.getsizeof(value) - sys.getsizeof(self.entries[idx].value)
        self.size += size_diff # Add or remove difference in value size to total size
        self.entries[idx] = entry
      else:
        self.size += sys.getsizeof(key) + sys.getsizeof(value) + 1 # Add key, value and tombstone size to total size
        self.entries.insert(idx, entry)

    def delete(self, key: str):
      """
      Delete the entry from the Memtable.
      If entry is not present, create new entry with deleted True tombstone as the entry may be present in other SSTable segments
      """
      entry = Entry(key, None, True)
      result, idx = _get_index(key)
      if result:
        self.size -= sys.getsizeof(self.entries[idx].value) # Add or remove difference to total size
        self.entries[idx] = entry
      else:
        self.size += sys.getsizeof(key) + 1 # Add key and tombstone size to total size
        self.entries.insert(idx, entry)

    def find(self, key: str):
      """
      Search for entry with key and return value if found.
      If not found raise KeyError 
      """
      result, idx = _get_index(key)
      if result:
        return self.entries[idx].value
      else:
        raise KeyError

    def _get_index(self, key:str) -> (bool, int):
      """
      Search for the index of entry with binary search.
      If found return True and the index.
      If not found return False and the insertion index to maintain sorted order.
      """
      idx = bisect.bisect(self.entries, key)
      if idx != len(self.entries) and self.entries[idx].key == x:
        return True, idx
      else:
        return False, idx

