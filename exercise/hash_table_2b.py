class HashTable2B:
    def __init__(self):
        self.list_data = [[],[],[],[],[],[],[],[],[],[],]

    # the key to generate unique index from data
    def hashFunction(self, data):
        index_nums = 0

        for v in data:
            index_nums += ord(v)

        return index_nums % 10

    def insertData(self, data):
        index = self.hashFunction(data)
        self.list_data[index].append(data)

    def showListData(self):
        print(self.list_data)

    def isExist(self, data):
        index = self.hashFunction(data)
        return self.list_data[index] == data


ht = HashTable2B()

ht.insertData("ba")
ht.insertData("bu")
ht.insertData("boba")

ht.showListData()

# print(ht.isExist("bob"))
# print(ht.isExist("cow"))

# name = "GIBRAN"
# totalNilai  = 0

# for n in name:
#     nilai = ord(n)
#     print(f"n adalah {n}, menghasilkan nilai: {nilai}")
#     totalNilai += nilai

# print(f"total nilai {name} adalah {totalNilai}")
# lastIndex = totalNilai % 10
# print(f"index akhir adalah {lastIndex}")
