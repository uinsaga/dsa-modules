# for i in range(0, 10, 3):
#     print(f"looping ke {i}")

# count = 0
# while count < 10:
#     count += 1
#     print(f"count adalah {count}")


# def getMalaysia():
#     print("harimau, harimau malaya")


# getMalaysia()


# def luasPersegiPanjang(p: int, l: int):
#     hasil = p * l
#     return hasil


# def kelilingPersegiPanjang(p: int, l: int):
#     hasil = 2 * (p + l)
#     return hasil


# p = 10
# l = 5

# luas = luasPersegiPanjang(p, l)
# print(f"luas dari panjang {p} dan lebar {l} adalah {luas}")

# print("------------------------")
# kll = kelilingPersegiPanjang(p, l)
# print(f"keliling dari panjang {p} dan lebar {l} adalah {kll}")


def evenOdd(val: int):
    if val % 2 == 0:
        print("genap")
    else:
        print("ganjil")


evenOdd(2)
