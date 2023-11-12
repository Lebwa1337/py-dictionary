import math
from typing import Any, Hashable, Final


class Dictionary:
    def __init__(self) -> None:
        self._initialize_hash_table(8)
        self.data = []
        self.capacity = 0

    def __setitem__(self, key: Hashable, value: Any) -> None:
        self.data.append([key, value])
        self.create_hash_table(key, value)
        self.capacity += 1
        const: Final[float] = 2 / 3
        if self.capacity >= math.floor(len(self.hash_table) * const):
            self._resize()

    def __getitem__(self, item: Hashable) -> Any:
        for key, value in self.data:
            if key == item:
                return value
        raise KeyError(f"Key '{item}' not found in the dictionary")

    def __len__(self) -> int:
        return len(self.data)

    def _initialize_hash_table(self, hash_table_len: int) -> None:
        self.hash_table = [[key, None] for key in range(hash_table_len)]

    def create_hash_table(self, key: Hashable, value: Any) -> None:
        cell_index = hash(key) % len(self.hash_table)
        while True:
            if self.hash_table[cell_index][1]:
                if self.hash_table[cell_index][1][0] == key:
                    for data in self.data:
                        if data[0] == key:
                            self.data.remove(data)
                            break
                    self.hash_table[cell_index][1] = [key, hash(key), value]
                    self.capacity -= 1
                    break
                cell_index = (cell_index + 1) % len(self.hash_table)
            if self.hash_table[cell_index][1] is None:
                self.hash_table[cell_index][1] = [key, hash(key), value]
                break

    def _resize(self) -> None:
        copy_hash_table = self.hash_table.copy()
        two_times_len = len(self.hash_table) * 2
        self._initialize_hash_table(two_times_len)
        for stored_node in copy_hash_table:
            if stored_node[1] is not None:
                key = stored_node[1][0]
                value = stored_node[1][2]
                self.create_hash_table(key, value)


my_dict = Dictionary()

my_dict[30] = 100
my_dict[50] = 200
my_dict[60] = 300
my_dict[25] = 400
my_dict[40] = 500
my_dict[30] = 900
