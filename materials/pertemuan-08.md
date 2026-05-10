# STRUKTUR DATA

# GRAPH & TRAVERSAL (BFS DAN DFS)

**Mata Kuliah** : Struktur Data / Algoritma dan Pemrograman

---

# 1. Tujuan Pembelajaran

Setelah mempelajari materi ini, mahasiswa mampu:

✅ Memahami konsep graph dalam dunia nyata.

✅ Membedakan graph dan tree.

✅ Membuat representasi graph menggunakan adjacency matrix dan adjacency list.

✅ Mengimplementasikan BFS dan DFS.

✅ Memilih algoritma traversal yang tepat sesuai kasus.

✅ Menyelesaikan masalah nyata menggunakan graph.

---

# 2. Kenapa Graph Penting?

Sebelum belajar teori, coba lihat contoh berikut:

| Kasus Dunia Nyata      | Bentuk Graph                    |
| ---------------------- | ------------------------------- |
| Google Maps            | Kota = node, jalan = edge       |
| Instagram/Facebook     | User = node, pertemanan = edge  |
| Jaringan komputer      | Device = node, koneksi = edge   |
| Sistem rekomendasi     | Produk/user saling terhubung    |
| Jalur listrik/internet | Titik jaringan saling terhubung |

Intinya:

> Graph digunakan untuk merepresentasikan hubungan antar objek.

---

# 3. Konsep Dasar Graph

Graph terdiri dari:

* **Vertex (Node/Simpul)** → objek
* **Edge (Sisi)** → hubungan antar objek

Contoh:

```text
A ----- B
|       |
|       |
C ----- D
```

Node:

* A, B, C, D

Edge:

* A-B
* A-C
* B-D
* C-D

---

# 4. Perbedaan Tree dan Graph

| Tree              | Graph             |
| ----------------- | ----------------- |
| Tidak boleh cycle | Boleh cycle       |
| Selalu punya root | Tidak harus       |
| Jalur tunggal     | Bisa banyak jalur |
| Struktur hirarki  | Struktur bebas    |

## Analogi Mudah

### Tree

Struktur organisasi kampus:

```text
Rektor
 ├── Dekan
 │    └── Kaprodi
```

### Graph

Pertemanan mahasiswa:

```text
Andi berteman dengan Budi dan Citra
Budi berteman dengan Deni
Citra juga berteman dengan Deni
```

Hubungannya bebas dan saling terhubung.

---

# 5. Terminologi Penting

## Adjacent

Dua node yang terhubung langsung.

Contoh:

```text
A --- B
```

A adjacent dengan B.

---

## Degree

Jumlah edge yang terhubung ke node.

```text
A --- B --- C
```

Degree B = 2

---

## Path

Jalur dari satu node ke node lain.

```text
A → B → C
```

---

## Cycle

Jalur yang kembali ke titik awal.

```text
A → B → C → A
```

---

# 6. Jenis Graph

## a. Undirected Graph

Hubungan dua arah.

```text
A --- B
```

Artinya:

* A ke B bisa
* B ke A bisa

Contoh:

* Pertemanan Facebook

---

## b. Directed Graph

Memiliki arah.

```text
A → B
```

Artinya:

* A menuju B
* B belum tentu menuju A

Contoh:

* Instagram follow
* Dependency project

---

## c. Weighted Graph

Setiap edge punya nilai/bobot.

```text
Jakarta --(450km)-- Bandung
```

Contoh:

* GPS
* Ongkir
* Biaya perjalanan

---

# 7. Representasi Graph dalam Program

# A. Adjacency Matrix

Graph:

```text
0 --- 1
|     |
3 --- 2
```

Matrix:

|   | 0 | 1 | 2 | 3 |
| - | - | - | - | - |
| 0 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 1 | 0 |
| 2 | 0 | 1 | 0 | 1 |
| 3 | 1 | 0 | 1 | 0 |

## Cara Membaca

Baris 0 kolom 1 = 1
Artinya:

* node 0 terhubung ke node 1

---

## Kelebihan

✅ Cek koneksi sangat cepat
✅ Mudah dipahami

## Kekurangan

❌ Boros memori
❌ Tidak efisien untuk graph besar

---

# B. Adjacency List

Graph yang sama:

```text
0: [1, 3]
1: [0, 2]
2: [1, 3]
3: [0, 2]
```

## Artinya

Node 0 terhubung ke:

* 1
* 3

---

## Kelebihan

✅ Hemat memori
✅ Cocok untuk graph besar

## Kekurangan

❌ Cek koneksi lebih lambat

---

# 8. Traversal Graph

Traversal = proses mengunjungi node satu per satu.

Dua algoritma utama:

| Algoritma | Cara Kerja               |
| --------- | ------------------------ |
| BFS       | Melebar per level        |
| DFS       | Menyelam sedalam mungkin |

---

# 9. BFS (Breadth First Search)

## Konsep BFS

BFS bekerja seperti:

> “Kunjungi semua tetangga terdekat dulu.”

Menggunakan:

* Queue (FIFO)

---

# Visualisasi BFS

Graph:

```text
      A
     / \
    B   C
   /     \
  D ----- E
```

Mulai dari A.

---

## Langkah BFS

### Step 1

Kunjungi:

```text
A
```

Queue:

```text
[B, C]
```

---

### Step 2

Kunjungi:

```text
B
```

Queue:

```text
[C, D]
```

---

### Step 3

Kunjungi:

```text
C
```

Queue:

```text
[D, E]
```

---

### Hasil BFS

```text
A → B → C → D → E
```

---

# Analogi BFS

Bayangkan banjir air.

Air menyebar:

* ke tetangga terdekat dulu
* lalu melebar

Itulah BFS.

---

# Kapan BFS Digunakan?

✅ Mencari jalur terpendek
✅ Pencarian level
✅ Social network
✅ GPS sederhana
✅ Maze shortest path

---

# Contoh Dunia Nyata BFS

## Kasus: Cari Teman Terdekat

LinkedIn ingin mencari:

> “Siapa koneksi paling dekat dari Andi ke Budi?”

BFS akan:

* cek teman langsung
* lalu teman dari teman
* lalu level berikutnya

Karena BFS mencari per level, maka:
✅ jalur pertama yang ditemukan adalah jalur terpendek.

---

# Contoh Penyelesaian BFS

Graph pertemanan:

```text
Andi -- Budi -- Citra
  |
Deni
```

Cari jalur dari Andi ke Citra.

## BFS:

Level 1:

* Budi
* Deni

Level 2:

* Citra

Hasil:

```text
Andi → Budi → Citra
```

---

# 10. DFS (Depth First Search)

## Konsep DFS

DFS bekerja seperti:

> “Masuk sedalam mungkin dulu.”

Menggunakan:

* Stack
* atau rekursi

---

# Visualisasi DFS

Graph:

```text
      A
     / \
    B   C
   /     \
  D ----- E
```

Mulai dari A.

---

## Langkah DFS

### Masuk terus:

```text
A → B → D → E → C
```

DFS akan terus menyelam sampai mentok.

---

# Analogi DFS

Bayangkan masuk labirin.

Kita:

* pilih satu jalan
* terus masuk
* kalau mentok baru mundur

Itulah DFS.

---

# Kapan DFS Digunakan?

✅ Maze solving
✅ Backtracking
✅ Deteksi cycle
✅ Topological sort
✅ Sudoku solver

---

# Contoh Dunia Nyata DFS

## Kasus: Web Crawling

Google crawler membuka halaman web:

* buka halaman A
* masuk ke link pertama
* masuk lagi
* terus mendalam

Ini mirip DFS.

---

# Contoh Penyelesaian DFS

Maze:

```text
S → A → B → C → Finish
```

DFS akan mencoba satu jalur penuh dulu.

Jika mentok:

* mundur
* coba cabang lain

---

# 11. Perbandingan BFS dan DFS

| BFS                | DFS               |
| ------------------ | ----------------- |
| Melebar            | Mendalam          |
| Queue              | Stack             |
| Shortest path      | Tidak selalu      |
| Butuh memori besar | Lebih hemat       |
| Cocok graph lebar  | Cocok graph dalam |

---

# 12. Implementasi Python BFS dan DFS

## Membuat Graph

```python
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}
```

---

# BFS Python

```python
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=' ')
            visited.add(node)

            for neighbor in graph[node]:
                queue.append(neighbor)

bfs(graph, 'A')
```

Output:

```text
A B C D E
```

---

# Penjelasan Mudah

## Queue

FIFO:

> Yang masuk dulu keluar dulu

```python
queue.append()
queue.popleft()
```

---

# DFS Python

```python
def dfs(graph, node, visited=set()):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

dfs(graph, 'A')
```

Output:

```text
A B D C E
```

---

# 13. Studi Kasus Nyata

# Studi Kasus 1 — GPS Sederhana

## Masalah

Ada kota:

```text
A -- B -- D
 \       /
   C ----
```

Cari jalur tercepat dari A ke D.

---

## Solusi

Gunakan BFS.

Kenapa?

Karena:

* semua jalan dianggap setara
* BFS menemukan jalur paling pendek

---

## Proses BFS

Dari A:

* cek B
* cek C

Lalu:

* D ditemukan

Hasil:

```text
A → B → D
```

atau

```text
A → C → D
```

---

# Studi Kasus 2 — Friend Recommendation

## Masalah

```text
Andi -- Budi -- Citra
  |
Deni
```

Andi belum kenal Citra.

---

## Solusi

Gunakan BFS level 2:

* teman dari teman

Hasil rekomendasi:

```text
Citra
```

---

# Studi Kasus 3 — Deteksi Jalan Buntu Maze

Gunakan DFS.

Kenapa?

Karena DFS cocok:

* eksplorasi mendalam
* backtracking

---

# 14. Kompleksitas

## Rumus Penting

| Simbol | Arti          |
| ------ | ------------- |
| V      | jumlah vertex |
| E      | jumlah edge   |

---

# Kompleksitas BFS dan DFS

| Algoritma | Waktu    |
| --------- | -------- |
| BFS       | O(V + E) |
| DFS       | O(V + E) |

Artinya:

* semua node dikunjungi sekali
* semua edge dicek sekali

---

# 15. Kesalahan Umum Mahasiswa

## 1. Lupa visited

Akibat:
❌ infinite loop

Contoh cycle:

```text
A → B → C → A
```

---

## 2. Salah memilih BFS/DFS

### Harusnya BFS

Jika:

* cari shortest path

### Harusnya DFS

Jika:

* eksplorasi mendalam

---

## 3. Salah memahami Queue vs Stack

| Struktur | Sifat |
| -------- | ----- |
| Queue    | FIFO  |
| Stack    | LIFO  |

---

# 16. Tips Mengingat BFS dan DFS

## BFS

Huruf:

> B = Broad = melebar

---

## DFS

Huruf:

> D = Deep = mendalam

---

# 17. Latihan Pemahaman

## Soal 1

Graph:

```text
A --- B
|     |
C --- D
```

### Pertanyaan

1. Buat adjacency list.
2. Tentukan BFS dari A.
3. Tentukan DFS dari A.

---

## Jawaban

### Adjacency List

```python
A: [B, C]
B: [A, D]
C: [A, D]
D: [B, C]
```

---

### BFS

```text
A → B → C → D
```

---

### DFS

```text
A → B → D → C
```

---

# 18. Latihan Analisis

## Pertanyaan

Kenapa BFS bisa menemukan shortest path?

---

## Jawaban

Karena BFS mengunjungi node:

* berdasarkan level
* dari jarak terdekat dulu

Sehingga:

* node pertama yang ditemukan
* pasti jalur paling pendek (untuk unweighted graph)

---

# 19. Ringkasan Super Singkat

## Graph

Struktur hubungan antar objek.

---

## BFS

* Melebar
* Queue
* Shortest path

---

## DFS

* Mendalam
* Stack/Rekursi
* Backtracking

---

# 20. Kesimpulan

* Graph adalah struktur data penting dalam dunia nyata.
* BFS dan DFS adalah algoritma traversal dasar yang wajib dipahami.
* BFS cocok untuk shortest path.
* DFS cocok untuk eksplorasi mendalam.
* Pemilihan algoritma bergantung pada masalah yang diselesaikan.

---

# 21. Mini Cheat Sheet

| Kebutuhan             | Gunakan |
| --------------------- | ------- |
| Shortest path         | BFS     |
| Maze solving          | DFS     |
| Friend recommendation | BFS     |
| Backtracking          | DFS     |
| Topological sort      | DFS     |
| Social network        | BFS     |
| Web crawling          | DFS/BFS |

---

# 22. Referensi

1. Cormen — Introduction to Algorithms
2. Sedgewick — Algorithms
3. Goodrich — Data Structures and Algorithms in Python
4. Visualgo Graph Traversal
