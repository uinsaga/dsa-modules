class CustomHashTable:
    def __init__(self):
        self.list = [[],[],[],[],[],[],[],[],[],[],]

    def hash_function(self, value: str):
        sum_of_chars = 0
        for char in value:
            sum_of_chars += ord(char)

        index: int = sum_of_chars % 10
        return index

    def add(self, value):
        index: int = self.hash_function(value)
        self.list[index].append(value)

    def contain(self, value):
        index: int = self.hash_function(value)
        isExist = self.list[index] == value
        return isExist

    def displayData(self):
        return self.list


ht = CustomHashTable()
ht.add("ba")
ht.add("bi")
ht.add("bu")
ht.add("be")
ht.add("bo")
ht.add("bo")


print(ht.displayData())
