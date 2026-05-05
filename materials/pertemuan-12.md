# IDE MINI PROJECT

## STRUKTUR DATA & ALGORITMA

---

## PROJECT 1: SISTEM MANAJEMEN NILAI MAHASISWA (BST)

**Tingkat:** Mudah  
**Topik:** Binary Search Tree (BST)  
**Durasi:** 1-2 hari

### Deskripsi

Buat sistem untuk menyimpan dan mengelola data nilai mahasiswa menggunakan BST yang diurutkan berdasarkan NIM. Sistem ini dapat digunakan dosen untuk mengelola nilai mahasiswa secara efisien.

### Fitur Minimal

1. **Tambah mahasiswa** (NIM, Nama, Nilai)
2. **Cari mahasiswa** berdasarkan NIM
3. **Tampilkan semua mahasiswa** (diurutkan ascending berdasarkan NIM)
4. **Tampilkan mahasiswa dengan nilai tertinggi/terendah**
5. **Hitung rata-rata nilai** semua mahasiswa
6. **Hapus mahasiswa** berdasarkan NIM

### Contoh Input/Output

```
=== SISTEM MANAJEMEN NILAI MAHASISWA ===
1. Tambah Mahasiswa
2. Cari Mahasiswa
3. Tampilkan Semua (inorder)
4. Nilai Tertinggi & Terendah
5. Hitung Rata-rata
6. Hapus Mahasiswa
7. Keluar

Pilih: 1
NIM: 2023001
Nama: Andi
Nilai: 85
✅ Mahasiswa berhasil ditambahkan!

Pilih: 3
========================================
NIM         | Nama        | Nilai
2023001     | Andi        | 85
2023002     | Budi        | 72
2023003     | Cici        | 90
========================================

Pilih: 5
Rata-rata nilai: 82.33
```

### Ekstensi (Bonus)

- Export data ke file CSV
- Import data dari file CSV
- Tampilkan mahasiswa dengan nilai di atas KKM (misal > 75)
- Visualisasi tree (print tree secara horizontal)

---

## PROJECT 2: SISTEM REKOMENDASI TEMAN (GRAPH BFS/DFS)

**Tingkat:** Sedang  
**Topik:** Graph (BFS, DFS, Shortest Path)  
**Durasi:** 2-3 hari

### Deskripsi

Buat sistem rekomendasi teman berbasis social network graph. Setiap user adalah node, dan pertemanan adalah edge. Sistem dapat merekomendasikan "teman yang mungkin dikenal" (friend-of-friend) dan mencari derajat keterpisahan (degree of separation).

### Fitur Minimal

1. **Tambah user** (nama/ID)
2. **Tambah pertemanan** (hubungkan dua user)
3. **Tampilkan semua teman** dari suatu user (BFS/DFS)
4. **Rekomendasi teman** (teman dari teman yang belum berteman langsung)
5. **Cari derajat keterpisahan** (shortest path) antara dua user
6. **Deteksi komponen terhubung** (connected components)

### Contoh Input/Output

```
=== SISTEM REKOMENDASI TEMAN ===
1. Tambah User
2. Tambah Pertemanan
3. Lihat Teman
4. Rekomendasi Teman
5. Derajat Keterpisahan
6. Lihat Komunitas
7. Keluar

Pilih: 1
Nama user: Andi
✅ User Andi ditambahkan!

Pilih: 2
User 1: Andi
User 2: Budi
✅ Pertemanan terbentuk!

Pilih: 4
User: Andi
Rekomendasi teman untuk Andi:
- Cici (teman dari Budi)
- Dodi (teman dari Budi)

Pilih: 5
User 1: Andi
User 2: Cici
Derajat keterpisahan: 2
Jalur: Andi → Budi → Cici
```

### Ekstensi (Bonus)

- Visualisasi graph (gunakan networkx + matplotlib)
- Jumlah mutual friends
- Top N user dengan teman terbanyak
- Fitur "saran grup" berdasarkan komunitas

---

## PROJECT 3: SISTEM INVENTORY DENGAN KNAPSACK OPTIMIZER (DP)

**Tingkat:** Sedang  
**Topik:** Dynamic Programming (0/1 Knapsack, Coin Change)  
**Durasi:** 2-3 hari

### Deskripsi

Buat sistem inventory untuk toko yang membantu pemilik toko memilih barang yang akan dibawa dalam perjalanan bisnis dengan batasan berat tas. Sistem akan merekomendasikan kombinasi barang dengan nilai total tertinggi.

### Fitur Minimal

1. **Tambah barang** (nama, berat, nilai/harga)
2. **Lihat semua barang**
3. **Optimasi knapsack** (input kapasitas tas, output barang yang harus dibawa)
4. **Tampilkan total nilai dan total berat**
5. **Coin Change** - fitur untuk menghitung minimum koin kembalian

### Contoh Input/Output

```
=== SISTEM INVENTORY OPTIMIZER ===
1. Tambah Barang
2. Lihat Barang
3. Optimasi Knapsack
4. Kalkulator Kembalian (Coin Change)
5. Keluar

Pilih: 1
Nama barang: Laptop
Berat (kg): 2
Nilai (juta): 15
✅ Barang ditambahkan!

Barang saat ini:
1. Laptop (2kg, 15jt)
2. Buku (1kg, 5jt)
3. Powerbank (1kg, 3jt)
4. Kamera (3kg, 12jt)

Pilih: 3
Kapasitas tas (kg): 4

Hasil optimasi:
Ambil barang:
- Laptop (2kg, 15jt)
- Buku (1kg, 5jt)
- Powerbank (1kg, 3jt)

Total nilai: 23 juta
Total berat: 4 kg
```

### Ekstensi (Bonus)

- Edit/hapus barang
- Simpan dan load data inventory
- Tambah fitur "unbounded knapsack" (barang bisa diambil lebih dari sekali)
- Visualisasi tabel DP

---

## PROJECT 4: SUDOKU SOLVER & GENERATOR (BACKTRACKING)

**Tingkat:** Sulit  
**Topik:** Backtracking (dengan pruning)  
**Durasi:** 3-4 hari

### Deskripsi

Buat aplikasi yang dapat menyelesaikan puzzle Sudoku (9x9) secara otomatis menggunakan algoritma backtracking, serta dapat menghasilkan puzzle Sudoku baru dengan tingkat kesulitan yang bisa dipilih.

### Fitur Minimal

1. **Input puzzle Sudoku** (manual atau dari file)
2. **Selesaikan Sudoku** (gunakan backtracking dengan MRV heuristic)
3. **Validasi puzzle** (apakah puzzle valid)
4. **Tampilkan langkah penyelesaian** (opsional)
5. **Generate puzzle acak** (dengan tingkat kesulitan: mudah, sedang, sulit)

### Contoh Input/Output

```
=== SUDOKU SOLVER & GENERATOR ===
1. Input Puzzle Manual
2. Load dari File
3. Selesaikan Sudoku
4. Validasi Puzzle
5. Generate Puzzle Acak
6. Keluar

Pilih: 1
Masukkan papan Sudoku (0 untuk kosong):
Baris 1: 5 3 0 0 7 0 0 0 0
Baris 2: 6 0 0 1 9 5 0 0 0
...

Puzzle input:
5 3 0 | 0 7 0 | 0 0 0
6 0 0 | 1 9 5 | 0 0 0
0 9 8 | 0 0 0 | 0 6 0
------+-------+------
8 0 0 | 0 6 0 | 0 0 3
4 0 0 | 8 0 3 | 0 0 1
7 0 0 | 0 2 0 | 0 0 6
------+-------+------
0 6 0 | 0 0 0 | 2 8 0
0 0 0 | 4 1 9 | 0 0 5
0 0 0 | 0 8 0 | 0 7 9

Pilih: 3
Menyelesaikan...

Solusi:
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
------+-------+------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
------+-------+------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9

✅ Sudoku berhasil diselesaikan!
```

### Ekstensi (Bonus)

- GUI (Tkinter/PyQt) untuk input dan display
- Timer (catat waktu penyelesaian)
- Hint system (saran satu langkah)
- Multi-level difficulty dengan jumlah sel kosong berbeda
- Export solusi ke file

---

## PROJECT 5: APLIKASI RUTE PETA (DIJKSTRA + BFS/DFS + DP)

**Tingkat:** Sulit  
**Topik:** Graph (BFS/DFS), Dynamic Programming (Shortest Path)  
**Durasi:** 3-4 hari

### Deskripsi

Buat aplikasi peta sederhana untuk mencari rute terpendek antar lokasi. Graph bisa berupa grid (2D map) atau graph berbobot. Aplikasi dapat mencari rute dengan BFS (unweighted), Dijkstra (weighted), dan membandingkan dengan DP.

### Fitur Minimal

1. **Buat peta** (grid N x M dengan rintangan/tembok)
2. **Tentukan titik start dan finish**
3. **Cari rute dengan BFS** (jumlah langkah minimal)
4. **Cari rute dengan Dijkstra** (jika ada bobot berbeda)
5. **Tampilkan jalur** di peta
6. **Hitung jarak minimal**

### Contoh Input/Output

```
=== APLIKASI RUTE PETA ===
Peta 5x5 (0=jalan, 1=rintangan):
   0 1 2 3 4
0: 0 0 0 1 0
1: 0 1 0 1 0
2: 0 0 0 0 0
3: 1 1 0 1 0
4: 0 0 0 0 0

Start (baris,kolom): 0 0
Finish (baris,kolom): 4 4

Mencari rute dengan BFS...

Rute terpendek (8 langkah):
(0,0) → (0,1) → (0,2) → (1,2) → (2,2) → (2,3) → (2,4) → (3,4) → (4,4)

Visualisasi peta dengan jalur:
S . . # .
. # . # .
. . . . .
# # . # .
. . . . F
(. = jalur, # = rintangan, S=start, F=finish)
```

### Ekstensi (Bonus)

- Tambah bobot pada sel (misal jalan, tanjakan, turunan)
- Fitur "bandingkan algoritma" (BFS vs Dijkstra vs DP)
- Animasi pencarian jalur
- Load/save peta dari file
- Antarmuka grafis dengan pygame

---

## PROJECT 6: SCHEDULING TUGAS DEADLINE (DP + BACKTRACKING)

**Tingkat:** Sedang  
**Topik:** Dynamic Programming + Backtracking  
**Durasi:** 2 hari

### Deskripsi

Buat aplikasi untuk menjadwalkan pengerjaan tugas yang memiliki deadline dan nilai. Mahasiswa dapat memilih tugas mana yang akan dikerjakan agar total nilai maksimal, dengan batasan waktu yang tersedia.

### Fitur Minimal

1. **Tambah tugas** (nama, deadline, nilai, durasi)
2. **Lihat daftar tugas**
3. **Optimasi jadwal** (pilih tugas dengan nilai maksimal dalam batas waktu)
4. **Tampilkan jadwal pengerjaan** (urutan tugas)
5. **Backtracking untuk cari semua kemungkinan**

### Contoh Input/Output

```
=== SCHEDULING TUGAS ===
Daftar tugas:
1. Matematika (hari ke-2, nilai 10, durasi 1)
2. Fisika (hari ke-1, nilai 8, durasi 1)
3. Bahasa (hari ke-3, nilai 12, durasi 2)
4. Kimia (hari ke-2, nilai 6, durasi 1)
5. Biologi (hari ke-3, nilai 9, durasi 1)

Total waktu tersedia: 3 hari

Optimasi jadwal:
Tugas yang dipilih:
- Fisika (day1, nilai 8)
- Matematika (day2, nilai 10)
- Biologi (day3, nilai 9)

Total nilai: 27
Total durasi: 3 hari

Alternatif lain (backtracking):
- Bahasa + Matematika = 22
- Fisika + Matematika + Biologi = 27 (optimal)
```

### Ekstensi (Bonus)

- Sorting tugas berdasarkan deadline (EDD/Earliest Due Date)
- Visualisasi timeline (Gantt chart sederhana)
- Fitur "what-if" jika ada tugas tambahan

---

## PROJECT 7: MIND MAP GENERATOR (TREE + GRAPH)

**Tingkat:** Sedang  
**Topik:** Tree + Graph + Traversal  
**Durasi:** 2-3 hari

### Deskripsi

Buat aplikasi untuk membuat dan memvisualisasikan mind map (peta pikiran). Mind map adalah tree/graf hierarkis yang dimulai dari satu ide utama dan bercabang ke ide-ide turunan.

### Fitur Minimal

1. **Buat mind map baru** dengan root node
2. **Tambah child node** ke node tertentu
3. **Hapus node** (beserta semua child-nya)
4. **Edit node**
5. **Tampilkan mind map** (text-based atau tree view)
6. **Export ke text** (indentasi / bullet points)
7. **BFS/DFS traversal** untuk menampilkan semua node

### Contoh Input/Output

```
=== MIND MAP GENERATOR ===
Current mind map:
[ROOT] Algoritma
  ├─ [CHILD] Sorting
  │    ├─ Quick Sort
  │    └─ Merge Sort
  ├─ [CHILD] Searching
  │    ├─ Binary Search
  │    └─ Linear Search
  └─ [CHILD] Graph
       ├─ BFS
       └─ DFS

Menu:
1. Tambah node
2. Hapus node
3. Edit node
4. Tampilkan BFS
5. Tampilkan DFS
6. Export
7. Keluar

Pilih 1:
Node parent: Sorting
Nama node baru: Bubble Sort
✅ Node ditambahkan!

Export hasil (format text):
Algoritma
  - Sorting
    - Quick Sort
    - Merge Sort
    - Bubble Sort
  - Searching
    - Binary Search
    - Linear Search
  - Graph
    - BFS
    - DFS
```

### Ekstensi (Bonus)

- Load/save mind map ke file JSON
- Fitur "collapse/expand" node
- Visualisasi dengan library `graphviz`
- Fitur pencarian node

---

## PROJECT 8: WORD PUZZLE SOLVER (BACKTRACKING + BFS)

**Tingkat:** Sulit  
**Topik:** Backtracking + Graph BFS  
**Durasi:** 3-4 hari

### Deskripsi

Buat aplikasi untuk menyelesaikan word puzzle (seperti word search atau crosswords) di grid huruf. Carilah semua kata yang tersembunyi dalam grid dengan arah horizontal, vertikal, dan diagonal.

### Fitur Minimal

1. **Input grid huruf** (N x M)
2. **Input daftar kata** yang akan dicari
3. **Cari kata** dengan backtracking di grid
4. **Tampilkan posisi kata** ditemukan (baris, kolom, arah)
5. **Highlight posisi kata** di grid
6. **BFS untuk kata dengan wildcard** (misal H\*T)

### Contoh Input/Output

```
=== WORD PUZZLE SOLVER ===
Grid 4x4:
A B C D
E F G H
I J K L
M N O P

Kata yang dicari:
- ABC
- FG
- KOP
- MILIK (tidak ditemukan)

Hasil pencarian:
✅ "ABC" ditemukan di (0,0) ke kanan
✅ "FG" ditemukan di (1,1) ke kanan
✅ "KOP" ditemukan di (2,2) ke bawah
❌ "MILIK" tidak ditemukan

Grid dengan highlight:
[A] [B] [C] D
E  [F] [G] H
I  J  [K] [O]
M  N  [P]  L
```

### Ekstensi (Bonus)

- Pencarian 8 arah (termasuk diagonal)
- Fitur "timer" dan "score"
- Mode permainan (player mencari kata sendiri)
- Load dictionary dari file

---

## PROJECT 9: KASIR KANTIN DENGAN CASHBACK (DP COIN CHANGE)

**Tingkat:** Mudah-Sedang  
**Topik:** Dynamic Programming (Coin Change, 0/1 Knapsack)  
**Durasi:** 1-2 hari

### Deskripsi

Buat aplikasi kasir untuk kantin sederhana. Sistem dapat menghitung total belanja, menerima pembayaran, dan memberikan kembalian dengan jumlah koin/bilyet minimal.

### Fitur Minimal

1. **Daftar menu makanan/minuman** (nama, harga)
2. **Pesan menu** (bisa lebih dari satu)
3. **Hitung total belanja**
4. **Input pembayaran**
5. **Hitung kembalian** dengan jumlah lembar/bijih minimal (coin change)
6. **Cetak struk**

### Contoh Input/Output

```
=== KASIR KANTIN KELAS ===
Menu:
1. Nasi Goreng   - Rp 15.000
2. Mie Ayam      - Rp 12.000
3. Es Teh        - Rp 5.000
4. Es Jeruk      - Rp 7.000
5. Selesai pesan

Pilih menu: 1
Jumlah: 2
-> Nasi Goreng x 2 = Rp 30.000

Pilih menu: 3
Jumlah: 1
-> Es Teh x 1 = Rp 5.000

Pilih menu: 5

Total belanja: Rp 35.000
Pembayaran: Rp 50.000
Kembalian: Rp 15.000

Kembalian minimal (pecahan: 1000,2000,5000,10000,20000):
- 1 x 10000
- 1 x 5000

Terima kasih!
```

### Ekstensi (Bonus)

- Diskon member
- Pajak (PPN)
- Riwayat transaksi
- Export laporan penjualan

---

## PROJECT 10: REKOMENDASI JADWAL MATA KULIAH (GRAPH + BACKTRACKING)

**Tingkat:** Sulit  
**Topik:** Graph (Conflict Graph) + Backtracking (Graph Coloring)  
**Durasi:** 3-4 hari

### Deskripsi

Buat sistem untuk merekomendasikan jadwal kuliah semester depan. Sistem akan membaca mata kuliah yang diambil, jam kuliah yang tersedia, dosen pengampu, dan menghindari jadwal bentrok (konflik). Menggunakan graph coloring untuk penjadwalan.

### Fitur Minimal

1. **Daftar mata kuliah** (kode, nama, SKS, dosen)
2. **Daftar slot waktu** (Senin 07:00, Senin 09:00, dst)
3. **Input preference mahasiswa** (mata kuliah yang diambil)
4. **Deteksi konflik** (mata kuliah dengan dosen sama, atau mahasiswa bentrok)
5. **Buat jadwal otomatis** (graph coloring/backtracking)
6. **Tampilkan jadwal**

### Contoh Input/Output

```
=== PENJADWALAN MATA KULIAH ===
Mata kuliah tersedia (12 MK):
1. ASD (3 SKS, Dosen: Andi)
2. Basis Data (3 SKS, Dosen: Budi)
3. Jaringan (3 SKS, Dosen: Andi)  <- konflik dengan ASD (dosen sama)
...

Mata kuliah yang diambil mahasiswa:
- ASD
- Basis Data
- Jaringan
- Statistik

Slot waktu tersedia:
Senin (07:00-09:00, 09:00-11:00, 11:00-13:00)
Selasa (07:00-09:00, 09:00-11:00)
...

Hasil penjadwalan:
Senin 07:00-09:00 : ASD
Senin 09:00-11:00 : Basis Data
Selasa 07:00-09:00 : Jaringan
Selasa 09:00-11:00 : Statistik

✅ Tidak ada jadwal bentrok!
```

### Ekstensi (Bonus)

- Simpan jadwal ke file (ICS/Google Calendar)
- Auto-reschedule jika ada bentrok
- Drag-and-drop manual scheduling (GUI)

---

# RINGKASAN IDE MINI PROJECT

| No  | Nama Project             | Topik Utama          | Tingkat      | Durasi   |
| --- | ------------------------ | -------------------- | ------------ | -------- |
| 1   | Sistem Manajemen Nilai   | BST                  | Mudah        | 1-2 hari |
| 2   | Sistem Rekomendasi Teman | Graph BFS/DFS        | Sedang       | 2-3 hari |
| 3   | Inventory Knapsack       | DP                   | Sedang       | 2-3 hari |
| 4   | Sudoku Solver            | Backtracking         | Sulit        | 3-4 hari |
| 5   | Aplikasi Rute Peta       | Graph + DP           | Sulit        | 3-4 hari |
| 6   | Scheduling Tugas         | DP + Backtracking    | Sedang       | 2 hari   |
| 7   | Mind Map Generator       | Tree + Graph         | Sedang       | 2-3 hari |
| 8   | Word Puzzle Solver       | Backtracking + BFS   | Sulit        | 3-4 hari |
| 9   | Kasir Kantin             | DP Coin Change       | Mudah-Sedang | 1-2 hari |
| 10  | Penjadwalan Kuliah       | Graph + Backtracking | Sulit        | 3-4 hari |

---

# FORMAT PENGUMPULAN MINI PROJECT

Setiap project sebaiknya dikumpulkan dengan struktur:

```
Nama_NIM_ProjectName/
├── README.md               # Deskripsi project, fitur, cara run
├── src/
│   ├── main.py            # File utama
│   ├── bst.py              # Modul BST (jika ada)
│   ├── graph.py            # Modul Graph
│   └── ...
├── data/
│   └── sample_input.txt   # Contoh data input
├── docs/
│   └── laporan.pdf        # Laporan (jika diminta)
└── requirements.txt        # Dependencies (jika ada)
```

---

# RUBRIK PENILAIAN (Skala 100)

| Kriteria                 | Bobot | Deskripsi                                        |
| ------------------------ | ----- | ------------------------------------------------ |
| **Kebenaran Fungsional** | 40%   | Semua fitur minimal berfungsi sesuai spesifikasi |
| **Kualitas Kode**        | 20%   | Clean code, komentar, struktur modul yang baik   |
| **Efisiensi Algoritma**  | 15%   | Penggunaan algoritma yang tepat & efisien        |
| **Error Handling**       | 10%   | Menangani input error, edge cases                |
| **User Interface**       | 10%   | CLI/GUI yang jelas dan mudah digunakan           |
| **Dokumentasi**          | 5%    | README yang jelas, komentar di kode              |

---

