# MODUL PENGANTAR STRUKTUR DATA: TREE & BINARY SEARCH TREE (BST)

**Kode & Nama Mata Kuliah** : Struktur Data
**Semester** : 2
**Durasi** : 3 x 50 menit

## Capaian Pembelajaran

Setelah mempelajari modul ini, mahasiswa mampu:

1. Menjelaskan konsep tree dan hierarki data.
2. Membedakan berbagai jenis tree (binary tree, BST, dll).
3. Memahami konsep dan karakteristik Binary Search Tree (BST).
4. Mengimplementasikan operasi dasar BST (insert, search, delete).
5. Menganalisis kompleksitas operasi pada BST.

---

# A. Konsep Dasar Tree

## Pengertian Tree

Tree adalah struktur data non-linear yang digunakan untuk merepresentasikan hubungan hierarkis antar data.

Tree terdiri dari kumpulan node (simpul) yang saling terhubung melalui edge (sisi).

Berbeda dengan struktur data linear seperti array atau linked list, tree memungkinkan data disusun dalam bentuk bertingkat.

Contoh penggunaan tree:

- Struktur folder komputer
- Struktur organisasi
- DOM HTML
- Struktur menu aplikasi
- Sistem file

---

## Terminologi dalam Tree

| Istilah | Penjelasan                   |
| ------- | ---------------------------- |
| Root    | Node paling atas             |
| Parent  | Node induk                   |
| Child   | Node anak                    |
| Sibling | Node dengan parent yang sama |
| Leaf    | Node tanpa child             |
| Subtree | Bagian tree                  |
| Height  | Tinggi tree                  |
| Depth   | Kedalaman node               |
| Edge    | Penghubung antar node        |

---

## Contoh Struktur Tree

```text
            A
          / | \
         B  C  D
        / \
       E   F
```

Keterangan:

- A adalah root
- B, C, D adalah child dari A
- E dan F adalah leaf

---

# B. Jenis-Jenis Tree

## 1. Binary Tree

Binary Tree adalah tree dimana setiap node maksimal memiliki dua child:

- Left Child
- Right Child

Contoh:

```text
       10
      /  \
     5    15
```

---

## 2. Full Binary Tree

Setiap node memiliki:

- 0 child
  atau
- 2 child

Contoh:

```text
        1
      /   \
     2     3
    / \   / \
   4  5  6   7
```

---

## 3. Complete Binary Tree

Semua level terisi penuh kecuali level terakhir, dan pengisian dilakukan dari kiri ke kanan.

Contoh:

```text
        1
      /   \
     2     3
    / \   /
   4  5  6
```

---

## 4. Binary Search Tree (BST)

BST adalah binary tree yang memiliki aturan pengurutan tertentu.

Aturan BST:

- Nilai subtree kiri lebih kecil dari root.
- Nilai subtree kanan lebih besar dari root.
- Kedua subtree juga merupakan BST.

---

# C. Binary Search Tree (BST)

## Definisi BST

Binary Search Tree (BST) adalah struktur data tree yang digunakan untuk menyimpan data secara terurut sehingga proses pencarian menjadi lebih cepat.

Contoh BST:

```text
          50
        /    \
      30      70
     /  \    /  \
   20   40  60  80
```

Penjelasan:

- Semua node kiri lebih kecil dari parent.
- Semua node kanan lebih besar dari parent.

---

## Karakteristik BST

| Karakteristik      | Penjelasan |
| ------------------ | ---------- |
| Data terurut       | Ya         |
| Maksimal child     | 2          |
| Search lebih cepat | Ya         |
| Bersifat rekursif  | Ya         |

---

## Keunggulan BST

- Pencarian data lebih cepat.
- Penambahan data lebih efisien.
- Data tersusun secara otomatis.
- Banyak digunakan pada sistem database dan indexing.

---

## Kekurangan BST

- Dapat menjadi tidak seimbang.
- Worst case dapat berubah seperti linked list.
- Kompleksitas dapat turun menjadi O(n).

Contoh skew tree:

```text
10
 \
 20
   \
    30
      \
       40
```

---

# D. Operasi Dasar BST

## 1. Search (Pencarian)

Langkah pencarian:

1. Bandingkan data dengan root.
2. Jika sama → data ditemukan.
3. Jika lebih kecil → ke subtree kiri.
4. Jika lebih besar → ke subtree kanan.

Contoh:

Cari angka 40.

```text
          50
        /    \
      30      70
     /  \    /  \
   20   40  60  80
```

Proses:

```text
40 < 50 → kiri
40 > 30 → kanan
40 ditemukan
```

---

## 2. Insert (Penambahan)

Langkah insert:

1. Jika tree kosong → menjadi root.
2. Jika data lebih kecil → ke kiri.
3. Jika data lebih besar → ke kanan.
4. Ulangi hingga menemukan posisi kosong.

Contoh insert:

Data:

```text
50, 30, 70, 20, 40
```

Hasil:

```text
        50
       /  \
     30    70
    /  \
   20  40
```

---

## 3. Delete (Penghapusan)

Penghapusan node memiliki 3 kondisi:

### a. Node tanpa child

Node dapat langsung dihapus.

### b. Node memiliki 1 child

Node digantikan child-nya.

### c. Node memiliki 2 child

Gunakan:

- inorder successor
  atau
- inorder predecessor

Contoh:

```text
        50
       /  \
     30    70
    /  \
   20  40
```

Hapus node 30.

Node 30 dapat diganti dengan 40.

Hasil:

```text
        50
       /  \
     40    70
    /
   20
```

---

# E. Implementasi BST dalam Python

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)

        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node

        if value < node.value:
            return self._search_recursive(node.left, value)

        return self._search_recursive(node.right, value)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)

        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)

        else:
            if node.left is None:
                return node.right

            elif node.right is None:
                return node.left

            min_larger_node = self._find_min(node.right)
            node.value = min_larger_node.value
            node.right = self._delete_recursive(node.right, min_larger_node.value)

        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node
```

---

## Contoh Penggunaan

```python
bst = BST()

for val in [50,30,70,20,40,60,80]:
    bst.insert(val)

print("Cari 40:", bst.search(40) is not None)

bst.delete(30)

print("Node 30 berhasil dihapus")
```

---

# F. Kompleksitas Waktu BST

| Operasi | Average Case | Worst Case |
| ------- | ------------ | ---------- |
| Search  | O(log n)     | O(n)       |
| Insert  | O(log n)     | O(n)       |
| Delete  | O(log n)     | O(n)       |

Worst case terjadi ketika BST tidak seimbang.

---

# G. Studi Kasus

## Kasus

Sebuah perpustakaan menyimpan ID buku menggunakan BST.

Tujuan:

- Mempercepat pencarian buku
- Mempermudah penambahan data
- Menjaga data tetap terurut

Contoh data:

```text
100, 50, 150, 25, 75
```

BST membuat proses pencarian lebih efisien dibanding pencarian linear.

---

# H. Latihan

## Latihan Pemahaman

1. Jelaskan perbedaan Binary Tree dan Binary Search Tree.
2. Gambarkan BST dari data berikut:

```text
40, 20, 60, 10, 30, 50, 70
```

3. Jelaskan aturan utama pada BST.
4. Mengapa BST dapat menjadi lambat?

---

## Latihan Pemrograman

1. Lengkapi fungsi `delete()` pada BST.
2. Buat fungsi untuk menghitung jumlah node dalam BST.
3. Buat program penyimpanan data mahasiswa menggunakan BST.
4. Buat fungsi untuk mencari nilai terbesar dan terkecil pada BST.

---

# I. Kesimpulan

- Tree adalah struktur data hierarkis.
- Binary Tree merupakan tree dengan maksimal dua child.
- Binary Search Tree (BST) memiliki aturan pengurutan tertentu.
- BST memungkinkan proses search, insert, dan delete lebih cepat dibanding pencarian linear.
- Performa BST sangat dipengaruhi keseimbangan tree.

---

# Referensi

1. https://www.tutorialspoint.com/data_structures_algorithms/tree_data_structure.htm
2. https://visualgo.net/en/bst
3. Cormen, T.H. — Introduction to Algorithms
4. Mark Allen Weiss — Data Structures and Algorithm Analysis
5. Goodrich & Tamassia — Data Structures and Algorithms in Python
6. GeeksForGeeks — Binary Search Tree
