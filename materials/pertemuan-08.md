# MODUL STRUKTUR DATA: GRAPH & TRAVERSAL (BFS DAN DFS)

**Kode & Nama Mata Kuliah** : Struktur Data / Algoritma dan Pemrograman  
**Semester** : 2-3  
**Durasi** : 3 x 50 menit

## Capaian Pembelajaran

Setelah mempelajari modul ini, mahasiswa mampu:

1. Menjelaskan konsep graph dan perbedaannya dengan tree.
2. Merepresentasikan graph dalam memori (adjacency matrix & adjacency list).
3. Mengimplementasikan algoritma BFS (Breadth-First Search) dan DFS (Depth-First Search).
4. Menganalisis kompleksitas waktu dan ruang dari BFS dan DFS.
5. Memilih algoritma traversal yang tepat berdasarkan karakteristik masalah.

---

## A. Konsep Dasar Graph

**Graph** adalah struktur data non-linear yang terdiri dari:

- **Vertex** (simpul/node) : entitas dalam graph.
- **Edge** (sisi) : hubungan antar vertex.

### Perbedaan Graph dengan Tree

| Karakteristik  | Tree                  | Graph                           |
| -------------- | --------------------- | ------------------------------- |
| Jumlah edge    | n-1 edge untuk n node | bisa lebih banyak               |
| Siklus (cycle) | tidak boleh ada       | boleh ada                       |
| Konektivitas   | selalu terhubung      | bisa terhubung atau tidak       |
| Arah           | umumnya tidak berarah | bisa berarah atau tidak berarah |
| Root khusus    | ada root              | tidak ada root khusus           |

### Terminologi Penting

- **Adjacent** : dua vertex yang terhubung langsung oleh edge.
- **Degree** : jumlah edge yang terhubung ke suatu vertex (untuk graph berarah: indegree & outdegree).
- **Path** : rangkaian vertex yang dihubungkan oleh edge.
- **Cycle** : path yang kembali ke vertex awal tanpa mengulang edge.
- **Connected graph** : untuk setiap pasang vertex, ada path yang menghubungkan.
- **Weighted graph** : setiap edge memiliki nilai/bobot.

### Jenis-jenis Graph

- **Undirected Graph** : edge tidak memiliki arah (hubungan dua arah).
- **Directed Graph (Digraph)** : edge memiliki arah.
- **Weighted Graph** : edge memiliki bobot.
- **Unweighted Graph** : edge tanpa bobot.
- **Complete Graph** : setiap vertex terhubung ke semua vertex lainnya.

---

## B. Representasi Graph dalam Memori

### 1. Adjacency Matrix

Matriks `n x n` (n = jumlah vertex).  
`M[i][j] = 1` jika ada edge dari vertex `i` ke `j` (atau sebaliknya untuk undirected).

**Contoh undirected graph dengan 4 vertex:**

```
0 -- 1
|    |
3 -- 2

Adjacency Matrix:
    0 1 2 3
0   0 1 0 1
1   1 0 1 0
2   0 1 0 1
3   1 0 1 0
```

**Keuntungan**: Cek edge O(1).  
**Kerugian**: Memori O(V²) tidak efisien untuk graph jarang.

### 2. Adjacency List

Array/list yang berisi daftar tetangga untuk setiap vertex.

**Contoh di atas:**

```
0: [1, 3]
1: [0, 2]
2: [1, 3]
3: [0, 2]
```

**Keuntungan**: Memori efisien O(V + E).  
**Kerugian**: Cek edge O(degree) lebih lambat.

### Rekomendasi

- Gunakan **adjacency matrix** untuk graph padat (dense) atau jumlah vertex kecil.
- Gunakan **adjacency list** untuk graph jarang (sparse) – mayoritas kasus.

---

## C. Traversal Graph

Traversal = mengunjungi semua vertex secara sistematis. Dua algoritma utama:

### 1. Breadth-First Search (BFS)

**Prinsip**: Kunjungi vertex dalam urutan **level** (melebar). Gunakan antrian (queue).

**Algoritma BFS**:

```
BFS(graph, start):
    inisialisasi queue
    inisialisasi visited (set atau array boolean)

    masukkan start ke queue
    tandai start sebagai visited

    selama queue tidak kosong:
        vertex = dequeue
        proses vertex (misal: cetak)

        untuk setiap neighbor dari vertex:
            jika neighbor belum di-visited:
                tandai neighbor visited
                masukkan neighbor ke queue
```

**Ilustrasi BFS**:

```
Graph:    1 -- 3
         /     \
        0       5
         \     /
          2 -- 4

Mulai dari vertex 0:
Level 0: 0
Level 1: 1, 2
Level 2: 3, 4
Level 3: 5
Urutan: 0, 1, 2, 3, 4, 5
```

**Karakteristik BFS**:

- Menemukan **jalur terpendek** (dalam jumlah edge) dari start ke semua vertex.
- Menggunakan queue (FIFO).
- Kompleksitas waktu: O(V + E) untuk adjacency list.

### 2. Depth-First Search (DFS)

**Prinsip**: Kunjungi vertex **mendalam** dulu sebelum ke cabang lain. Gunakan stack (bisa rekursif atau eksplisit).

**Algoritma DFS (rekursif)**:

```
DFS(graph, vertex, visited):
    tandai vertex sebagai visited
    proses vertex (misal: cetak)

    untuk setiap neighbor dari vertex:
        jika neighbor belum di-visited:
            DFS(graph, neighbor, visited)
```

**Ilustrasi DFS**:

```
Graph sama:
Mulai dari vertex 0:
0 → 1 → 3 → 5
kembali ke 1 (tidak ada tetangga baru)
kembali ke 0 → 2 → 4
Urutan: 0, 1, 3, 5, 2, 4
```

**Karakteristik DFS**:

- Membutuhkan memori lebih kecil untuk graph yang dalam.
- Tidak memberikan jalur terpendek.
- Berguna untuk deteksi cycle, topological sort, dan masalah backtracking.
- Kompleksitas waktu: O(V + E) untuk adjacency list.

---

## D. Implementasi Python (Adjacency List)

```python
from collections import deque

class Graph:
    def __init__(self, directed=False):
        self.adj_list = {}          # dictionary: vertex -> list of neighbors
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, u, v):
        """Menambahkan edge dari u ke v"""
        if u not in self.adj_list:
            self.add_vertex(u)
        if v not in self.adj_list:
            self.add_vertex(v)

        self.adj_list[u].append(v)
        if not self.directed:
            self.adj_list[v].append(u)

    def bfs(self, start):
        """BFS traversal dari vertex start"""
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []

        while queue:
            vertex = queue.popleft()
            result.append(vertex)

            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    def dfs_recursive(self, start):
        """DFS traversal (rekursif) dari vertex start"""
        visited = set()
        result = []
        self._dfs_helper(start, visited, result)
        return result

    def _dfs_helper(self, vertex, visited, result):
        visited.add(vertex)
        result.append(vertex)

        for neighbor in self.adj_list[vertex]:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited, result)

    def dfs_iterative(self, start):
        """DFS traversal (iteratif dengan stack)"""
        visited = set()
        stack = [start]
        result = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)

                # Masukkan tetangga ke stack (urutan terbalik untuk mempertahankan urutan)
                for neighbor in reversed(self.adj_list[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return result

    def shortest_path_bfs(self, start, target):
        """Mencari jalur terpendek dari start ke target menggunakan BFS"""
        if start == target:
            return [start]

        visited = {start}
        queue = deque([(start, [start])])  # (vertex, path)

        while queue:
            vertex, path = queue.popleft()

            for neighbor in self.adj_list[vertex]:
                if neighbor == target:
                    return path + [neighbor]

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return None  # Tidak ada jalur

    def has_path_dfs(self, start, target):
        """Mengecek apakah ada path dari start ke target dengan DFS"""
        visited = set()
        return self._has_path_helper(start, target, visited)

    def _has_path_helper(self, current, target, visited):
        if current == target:
            return True

        visited.add(current)
        for neighbor in self.adj_list[current]:
            if neighbor not in visited:
                if self._has_path_helper(neighbor, target, visited):
                    return True
        return False

    def display(self):
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex}: {neighbors}")
```

### Contoh Penggunaan

```python
# Membuat graph tidak berarah
g = Graph(directed=False)

# Menambahkan edge
edges = [(0,1), (0,2), (1,3), (2,3), (3,4)]
for u, v in edges:
    g.add_edge(u, v)

g.display()
print("\nBFS dari 0:", g.bfs(0))           # [0, 1, 2, 3, 4]
print("DFS rekursif dari 0:", g.dfs_recursive(0))  # [0, 1, 3, 4, 2]
print("DFS iteratif dari 0:", g.dfs_iterative(0))  # bisa berbeda urutan
print("\nJalur terpendek 0->4:", g.shortest_path_bfs(0, 4))  # [0,1,3,4] atau [0,2,3,4]
print("Ada path 0->4?", g.has_path_dfs(0, 4))  # True
```

**Output:**

```
0: [1, 2]
1: [0, 3]
2: [0, 3]
3: [1, 2, 4]
4: [3]

BFS dari 0: [0, 1, 2, 3, 4]
DFS rekursif dari 0: [0, 1, 3, 4, 2]
DFS iteratif dari 0: [0, 2, 3, 4, 1]
Jalur terpendek 0->4: [0, 1, 3, 4]
Ada path 0->4? True
```

### Graph Berarah (Directed Graph)

```python
# Graph berarah untuk masalah dependensi
dg = Graph(directed=True)
dg.add_edge('A', 'B')
dg.add_edge('A', 'C')
dg.add_edge('B', 'D')
dg.add_edge('C', 'D')
dg.add_edge('D', 'E')

print("Graph berarah:")
dg.display()
print("BFS dari A:", dg.bfs('A'))  # ['A', 'B', 'C', 'D', 'E']
```

---

## E. Kompleksitas Waktu & Ruang

| Algoritma | Representasi     | Kompleksitas Waktu | Kompleksitas Ruang |
| --------- | ---------------- | ------------------ | ------------------ |
| BFS       | Adjacency List   | O(V + E)           | O(V)               |
| BFS       | Adjacency Matrix | O(V²)              | O(V)               |
| DFS       | Adjacency List   | O(V + E)           | O(V)               |
| DFS       | Adjacency Matrix | O(V²)              | O(V)               |

**Keterangan**:

- V = jumlah vertex
- E = jumlah edge
- Ruang tambahan untuk visited, queue (BFS), atau stack (DFS/ rekursi)

**Catatan DFS rekursif**: Potensi stack overflow jika graph terlalu dalam (V > 1000). Gunakan iteratif untuk kasus tersebut.

---

## F. Perbandingan BFS vs DFS

| Aspek            | BFS                             | DFS                               |
| ---------------- | ------------------------------- | --------------------------------- |
| Struktur data    | Queue (FIFO)                    | Stack (LIFO) atau rekursi         |
| Jalur terpendek  | ✅ Ya (unweighted graph)        | ❌ Tidak                          |
| Memori           | Besar (simpan semua node level) | Kecil (simpan satu jalur)         |
| Cocok untuk      | Graph luas, shallow             | Graph dalam, puzzle, backtracking |
| Hasil traversal  | Level-order                     | Preorder seperti tree             |
| Deteksi cycle    | Bisa (perlu tracking parent)    | Lebih mudah (dengan status node)  |
| Topological sort | Bisa (Kahn's algorithm)         | Bisa (postorder)                  |

### Kapan menggunakan BFS?

- Mencari jalur terpendek (dalam jumlah edge).
- Graph memiliki tingkat (level) yang lebar.
- Semua edge memiliki bobot sama.

### Kapan menggunakan DFS?

- Memeriksa apakah graph terhubung.
- Mendeteksi siklus (cycle) dalam graph.
- Menyelesaikan puzzle/maze (backtracking).
- Melakukan topological sort pada DAG.
- Membutuhkan memori terbatas.

---

## G. Studi Kasus & Latihan

### Latihan Pemahaman

1. **Representasi Graph**  
   Diberikan graph berikut:

   ```
   A --- B
   |     |
   C --- D --- E
   ```

   - Gambar graph tersebut.
   - Buat adjacency matrix.
   - Buat adjacency list.
   - Tentukan degree setiap vertex.

2. **Traversal Graph**  
   Gunakan graph di atas (start dari A):
   - Tentukan urutan BFS traversal.
   - Tentukan urutan DFS traversal (rekursif asumsi urutan neighbor alphabetical).

3. **Graph Berarah**  
   Diberikan digraph: 1→2, 1→3, 2→4, 3→4, 4→5.
   - Hitung indegree dan outdegree tiap vertex.
   - Apakah graph ini memiliki cycle? Jelaskan.
   - Lakukan BFS dan DFS dari vertex 1.

### Latihan Pemrograman

1. **Implementasi lengkap**  
   Tambahkan method `get_connected_components()` pada kelas Graph untuk mengembalikan semua komponen terhubung (connected components) dalam graph tidak berarah.

2. **Deteksi Cycle**  
   Buat method `has_cycle()` untuk graph tidak berarah dan graph berarah.

3. **Topological Sort**  
   Implementasikan topological sort pada DAG (Directed Acyclic Graph) menggunakan DFS.

4. **Maze Solver**  
   Representasikan maze 2D sebagai graph dan gunakan BFS/DFS untuk mencari jalur dari start ke finish.

5. **Social Network Analysis**  
   Buat graph pertemanan (undirected). Implementasikan fungsi:
   - `friend_recommendation(user)`: merekomendasikan teman berdasarkan teman dari teman (friend-of-friend).
   - `shortest_friend_chain(user1, user2)`: mencari jalur terpendek dalam degree of separation.

### Soal Analisis

1. Jelaskan mengapa BFS dapat menemukan jalur terpendek pada unweighted graph, sedangkan DFS tidak bisa.

2. Jika sebuah graph memiliki 10.000 vertex dan 15.000 edge, representasi mana yang lebih efisien (matrix atau list)? Mengapa?

3. Apa yang terjadi jika Anda menjalankan DFS pada graph yang sangat dalam (misal 10^6 node dalam satu jalur panjang)? Apakah pendekatan rekursif aman?

4. Sebuah graph sosial memiliki karakteristik "small world" (diameter kecil). Algoritma mana yang lebih cepat untuk menemukan apakah dua orang terhubung? Jelaskan.

5. Kapan sebaiknya Anda memilih DFS iteratif daripada rekursif?

---

## H. Aplikasi Dunia Nyata

| Aplikasi                            | Graph Type         | Algoritma Utama                       |
| ----------------------------------- | ------------------ | ------------------------------------- |
| GPS / Peta digital                  | Weighted, directed | BFS (unweighted), Dijkstra (weighted) |
| Social network (Facebook, LinkedIn) | Undirected         | BFS, DFS, Community detection         |
| Web crawling (Google)               | Directed           | DFS, BFS (depend on strategy)         |
| Recommender system                  | Bipartite graph    | BFS, Collaborative filtering          |
| Compiler (dependency resolution)    | DAG                | DFS (Topological sort)                |
| AI / Game (pathfinding)             | Grid graph         | BFS, A\*                              |
| Network routing (OSPF, BGP)         | Weighted, directed | DFS (spanning tree), Dijkstra         |

---

## I. Kesimpulan

- **Graph** adalah struktur data yang sangat fleksibel untuk merepresentasikan hubungan kompleks.
- Dua representasi utama: **adjacency matrix** (padat) dan **adjacency list** (jarang).
- **BFS** optimal untuk mencari jalur terpendek pada unweighted graph, menggunakan queue.
- **DFS** lebih hemat memori dan cocok untuk backtracking, menggunakan stack atau rekursi.
- Kedua algoritma memiliki kompleksitas O(V + E) untuk adjacency list, sangat efisien untuk graph besar.
- Pemilihan BFS vs DFS tergantung pada karakteristik masalah dan struktur graph.

---

## J. Referensi

1. Cormen, T.H., Leiserson, C.E., Rivest, R.L., & Stein, C. (2009). _Introduction to Algorithms_, 3rd ed. MIT Press.
2. Sedgewick, R., & Wayne, K. (2011). _Algorithms_, 4th ed. Addison-Wesley.
3. Goodrich, M.T., & Tamassia, R. (2013). _Data Structures and Algorithms in Python_. Wiley.
4. https://ds1-iiith.vlabs.ac.in/exp/tree-traversal/depth-first-traversal/dft.html

---

