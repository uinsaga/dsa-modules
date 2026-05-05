# MODUL ALGORITMA: BACKTRACKING

**Kode & Nama Mata Kuliah** : Desain dan Analisis Algoritma / Algoritma Lanjut  
**Semester** : 3-4  
**Durasi** : 4 x 50 menit

## Capaian Pembelajaran

Setelah mempelajari modul ini, mahasiswa mampu:

1. Menjelaskan konsep dan prinsip backtracking.
2. Membedakan backtracking dengan brute force dan dynamic programming.
3. Mengidentifikasi masalah yang cocok diselesaikan dengan backtracking.
4. Mengimplementasikan pola umum backtracking (rekursif dengan pruning).
5. Menyelesaikan masalah klasik seperti N-Queens, Sudoku, Subset Sum, dan Permutasi.

---

## A. Konsep Dasar Backtracking

**Backtracking** adalah algoritma untuk menyelesaikan masalah secara sistematis dengan mencoba semua kemungkinan solusi, tetapi **mundur (backtrack)** ketika mengetahui bahwa solusi saat ini tidak mungkin menghasilkan solusi yang valid.

### Analogi Sederhana

> Mencari jalan keluar dari labirin: Anda mencoba satu jalur. Jika menemui jalan buntu, Anda kembali ke persimpangan terakhir dan mencoba jalur lain.

### Prinsip Utama

| Prinsip                      | Penjelasan                                                                          |
| ---------------------------- | ----------------------------------------------------------------------------------- |
| **Incremental Construction** | Membangun solusi secara bertahap, satu langkah setiap kali.                         |
| **Feasibility Check**        | Setiap langkah, periksa apakah solusi parsial masih mungkin menjadi solusi lengkap. |
| **Backtrack**                | Jika tidak mungkin, batalkan langkah terakhir dan coba alternatif lain.             |
| **Pruning**                  | Memotong cabang yang tidak menjanjikan (tidak akan menghasilkan solusi).            |

### Karakteristik Masalah untuk Backtracking

| Cocok untuk Backtracking                      | Tidak Cocok                             |
| --------------------------------------------- | --------------------------------------- |
| Mencari **semua** solusi atau **satu** solusi | Masalah optimasi (lebih baik DP/Greedy) |
| Solusi dibangun secara bertahap               | Subproblem tidak tumpang tindih         |
| Banyak constraint/kendala                     | Input sangat besar (> 30-40)            |
| Biasanya masalah kombinatorial                | Ada solusi matematis langsung           |

---

## B. Backtracking vs Brute Force vs DP

| Aspek         | Brute Force                | Backtracking                       | Dynamic Programming           |
| ------------- | -------------------------- | ---------------------------------- | ----------------------------- |
| Metode        | Generate semua kemungkinan | Generate + pruning (potong cabang) | Simpan hasil subproblem       |
| Efisiensi     | Sangat lambat              | Lebih cepat dari brute force       | Sangat cepat jika overlapping |
| Memori        | Minimal                    | Minimal (stack rekursi)            | Bisa besar (tabel)            |
| Jenis masalah | Solusi eksplisit           | Masalah dengan constraint          | Masalah optimasi/penghitungan |
| Contoh        | Generate semua subset      | N-Queens, Sudoku                   | Knapsack, LCS                 |

### Ilustrasi Perbedaan

```
Masalah: Cari subset dari {1,2,3,4} yang jumlahnya 5.

Brute Force:  2^4 = 16 subset, cek semua.
Backtracking: Hanya 5 subset yang dievaluasi sebelum menemukan {1,4}.
DP:           Langsung hitung dengan tabel O(n × target).
```

---

## C. Pola Umum (Template) Backtracking

### Template Rekursif Backtracking

```python
def backtrack(candidate, state):
    """
    candidate: solusi parsial yang sedang dibangun
    state: informasi tambahan (posisi, sisa target, dll)
    """
    # 1. Cek apakah kandidat adalah solusi lengkap
    if is_solution(candidate, state):
        process_solution(candidate)
        return  # atau return True jika hanya butuh satu solusi

    # 2. Generate semua kemungkinan langkah berikutnya
    for choice in generate_choices(candidate, state):
        # 3. Periksa apakah pilihan valid (constraint)
        if is_valid(choice, candidate, state):
            # 4. Lakukan pilihan (make move)
            make_choice(candidate, choice)

            # 5. Rekursi ke level berikutnya
            backtrack(candidate, state)

            # 6. Batalkan pilihan (undo move) - BACKTRACK
            undo_choice(candidate, choice)
```

### Template dengan Pruning Lebih Lanjut

```python
def backtrack_with_pruning(candidate, state):
    # Pruning awal: apakah masih mungkin mencapai solusi?
    if not could_be_solution(candidate, state):
        return

    if is_solution(candidate, state):
        process_solution(candidate)
        return True  # atau collect

    for choice in generate_choices(candidate, state):
        if is_valid(choice, candidate, state):
            make_choice(candidate, choice)
            if backtrack_with_pruning(candidate, state):
                return True  # stop jika sudah ketemu
            undo_choice(candidate, choice)

    return False
```

---

## D. Contoh Klasik 1: N-Queens Problem

**Masalah**: Tempatkan N ratu di papan catur N×N sehingga tidak ada dua ratu yang saling menyerang (satu baris, satu kolom, atau satu diagonal).

### Solusi Backtracking

```python
def solve_n_queens(n):
    """
    Menyelesaikan N-Queens problem.
    Mengembalikan semua kemungkinan solusi.
    """
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]

    # Set untuk melacak kolom dan diagonal yang terpakai
    cols = set()           # kolom yang sudah ada ratu
    diag1 = set()          # diagonal '/' (r + c)
    diag2 = set()          # diagonal '\' (r - c)

    def backtrack(row):
        # Base case: semua baris terisi
        if row == n:
            # Simpan solusi dalam format string
            result.append([''.join(row_board) for row_board in board])
            return

        # Coba tempatkan ratu di setiap kolom pada baris ini
        for col in range(n):
            if col in cols or (row + col) in diag1 or (row - col) in diag2:
                continue  # tidak valid

            # Lakukan pilihan (place queen)
            board[row][col] = 'Q'
            cols.add(col)
            diag1.add(row + col)
            diag2.add(row - col)

            # Rekursi ke baris berikutnya
            backtrack(row + 1)

            # Backtrack: batalkan pilihan
            board[row][col] = '.'
            cols.remove(col)
            diag1.remove(row + col)
            diag2.remove(row - col)

    backtrack(0)
    return result

# Contoh penggunaan
solutions = solve_n_queens(4)
print(f"Total solusi untuk N=4: {len(solutions)}")  # 2
for sol in solutions:
    for row in sol:
        print(row)
    print()
```

**Output untuk N=4:**

```
.Q..
...Q
Q...
..Q.

..Q.
Q...
...Q
.Q..
```

### Optimasi: Hanya Simpan Posisi Kolom per Baris

```python
def solve_n_queens_optimized(n):
    """Versi hemat memori: hanya menyimpan posisi kolom per baris"""
    result = []
    cols = set()
    diag1 = set()
    diag2 = set()

    # board_state[row] = kolom tempat ratu di baris row
    board_state = [-1] * n

    def backtrack(row):
        if row == n:
            # Konversi ke format papan
            solution = []
            for r in range(n):
                row_str = ['.'] * n
                row_str[board_state[r]] = 'Q'
                solution.append(''.join(row_str))
            result.append(solution)
            return

        for col in range(n):
            if col in cols or (row + col) in diag1 or (row - col) in diag2:
                continue

            # Make move
            board_state[row] = col
            cols.add(col)
            diag1.add(row + col)
            diag2.add(row - col)

            backtrack(row + 1)

            # Undo move
            board_state[row] = -1
            cols.remove(col)
            diag1.remove(row + col)
            diag2.remove(row - col)

    backtrack(0)
    return result

print(f"Jumlah solusi N-Queens untuk N=8: {len(solve_n_queens_optimized(8))}")  # 92
```

**Kompleksitas**: O(N! × N) waktu, O(N²) ruang untuk output.

---

## E. Contoh Klasik 2: Sudoku Solver

**Masalah**: Isi papan Sudoku 9×9 sehingga setiap baris, kolom, dan kotak 3×3 berisi angka 1-9 tanpa pengulangan.

```python
def solve_sudoku(board):
    """
    Menyelesaikan Sudoku secara in-place.
    board: list of list of int (0 menandakan kosong)
    Mengembalikan True jika ada solusi.
    """
    def find_empty():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None

    def is_valid(num, pos):
        row, col = pos

        # Cek baris
        for j in range(9):
            if board[row][j] == num and j != col:
                return False

        # Cek kolom
        for i in range(9):
            if board[i][col] == num and i != row:
                return False

        # Cek kotak 3x3
        box_row, box_col = row // 3 * 3, col // 3 * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num and (i, j) != pos:
                    return False
        return True

    def backtrack():
        empty = find_empty()
        if not empty:
            return True  # Sudoku terisi semua

        row, col = empty

        for num in range(1, 10):
            if is_valid(num, (row, col)):
                board[row][col] = num

                if backtrack():
                    return True

                # Backtrack
                board[row][col] = 0

        return False

    backtrack()
    return board

# Contoh penggunaan
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solved = solve_sudoku(sudoku_board)
for row in solved:
    print(row)
```

**Kompleksitas**: O(9^(m)) dengan m jumlah sel kosong (worst-case), tetapi pruning sangat efektif.

---

## F. Contoh Klasik 3: Subset Sum

**Masalah**: Diberikan himpunan bilangan bulat, cari semua subset yang jumlahnya sama dengan target.

```python
def subset_sum(numbers, target):
    """
    Mencari semua subset yang jumlahnya sama dengan target.
    Mengembalikan list of list.
    """
    result = []

    def backtrack(start, current_sum, current_subset):
        # Jika jumlah mencapai target, simpan solusi
        if current_sum == target:
            result.append(current_subset[:])  # copy
            return

        # Jika melebihi target atau tidak ada angka lagi, berhenti
        if current_sum > target or start >= len(numbers):
            return

        # Pruning: jika sisa angka terkecil pun tidak bisa mencapai target
        # (opsional untuk sorted numbers)

        for i in range(start, len(numbers)):
            current_subset.append(numbers[i])
            backtrack(i + 1, current_sum + numbers[i], current_subset)
            current_subset.pop()  # backtrack

    # Sorting membantu pruning dan menghindari duplikasi
    numbers.sort()
    backtrack(0, 0, [])
    return result

# Contoh
nums = [1, 2, 3, 4, 5, 6]
target = 7
subsets = subset_sum(nums, target)
print(f"Subset dengan jumlah {target}:")
for sub in subsets:
    print(sub)

# Output:
# [1, 2, 4]
# [1, 6]
# [2, 5]
# [3, 4]
# [7] (jika 7 ada)
```

### Dengan Pruning Lebih Baik (Jika Numbers Sorted)

```python
def subset_sum_with_pruning(sorted_nums, target):
    """Dengan pruning awal: hentikan jika angka terkecil sudah melebihi sisa"""
    result = []

    def backtrack(start, remaining, current_subset):
        if remaining == 0:
            result.append(current_subset[:])
            return

        for i in range(start, len(sorted_nums)):
            num = sorted_nums[i]

            # Pruning: jika num > remaining, angka berikutnya lebih besar
            if num > remaining:
                break

            # Hindari duplikat (skip angka yang sama di posisi yang sama)
            if i > start and sorted_nums[i] == sorted_nums[i-1]:
                continue

            current_subset.append(num)
            backtrack(i + 1, remaining - num, current_subset)
            current_subset.pop()

    sorted_nums.sort()
    backtrack(0, target, [])
    return result
```

---

## G. Contoh Klasik 4: Permutasi dan Kombinasi

### Semua Permutasi (Dengan Angka Unik)

```python
def permute_unique(nums):
    """
    Menghasilkan semua permutasi dari array nums (tanpa duplikasi).
    """
    result = []
    n = len(nums)
    used = [False] * n

    def backtrack(current_perm):
        if len(current_perm) == n:
            result.append(current_perm[:])
            return

        for i in range(n):
            if not used[i]:
                # Pruning: jika nums[i] sama dengan sebelumnya dan sebelumnya tidak digunakan
                # (hindari duplikasi untuk angka yang sama)
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                current_perm.append(nums[i])
                backtrack(current_perm)
                current_perm.pop()
                used[i] = False

    nums.sort()  # Sorting penting untuk pruning duplikasi
    backtrack([])
    return result

# Contoh
print(permute_unique([1, 2, 3]))
# Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
```

### Kombinasi C(n, k)

```python
def combinations(n, k):
    """
    Menghasilkan semua kombinasi C(n, k) dari angka 1..n.
    """
    result = []

    def backtrack(start, current_comb):
        if len(current_comb) == k:
            result.append(current_comb[:])
            return

        # Pruning: sisa angka yang dibutuhkan
        need = k - len(current_comb)
        # start sampai n - need + 1
        for i in range(start, n - need + 2):
            current_comb.append(i)
            backtrack(i + 1, current_comb)
            current_comb.pop()

    backtrack(1, [])
    return result

print(combinations(5, 3))
# Output: [[1,2,3], [1,2,4], [1,2,5], [1,3,4], [1,3,5], [1,4,5], [2,3,4], [2,3,5], [2,4,5], [3,4,5]]
```

---

## H. Implementasi Lengkap: Kelas Backtracking Utility

```python
from typing import List, Any, Callable, Optional

class Backtracking:
    """Utility class untuk berbagai masalah backtracking"""

    @staticmethod
    def n_queens(n: int) -> List[List[str]]:
        """N-Queens problem"""
        result = []
        cols, diag1, diag2 = set(), set(), set()
        board = [-1] * n

        def backtrack(row: int):
            if row == n:
                solution = []
                for r in range(n):
                    row_str = ['.'] * n
                    row_str[board[r]] = 'Q'
                    solution.append(''.join(row_str))
                result.append(solution)
                return

            for col in range(n):
                if col in cols or (row + col) in diag1 or (row - col) in diag2:
                    continue
                board[row] = col
                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)
                backtrack(row + 1)
                board[row] = -1
                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)

        backtrack(0)
        return result

    @staticmethod
    def subsets(nums: List[int]) -> List[List[int]]:
        """Menghasilkan semua subset (power set)"""
        result = []

        def backtrack(start: int, current: List[int]):
            result.append(current[:])
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])
        return result

    @staticmethod
    def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
        """
        Combination Sum: cari semua kombinasi unik yang jumlahnya = target.
        Setiap angka dapat digunakan lebih dari sekali.
        """
        result = []
        candidates.sort()

        def backtrack(start: int, remaining: int, current: List[int]):
            if remaining == 0:
                result.append(current[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                current.append(candidates[i])
                backtrack(i, remaining - candidates[i], current)  # i, bukan i+1
                current.pop()

        backtrack(0, target, [])
        return result

    @staticmethod
    def letter_combinations(digits: str) -> List[str]:
        """
        Letter Combinations of a Phone Number.
        Misal: "23" -> ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        """
        if not digits:
            return []

        mapping = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        result = []

        def backtrack(index: int, current: List[str]):
            if index == len(digits):
                result.append(''.join(current))
                return

            for char in mapping[digits[index]]:
                current.append(char)
                backtrack(index + 1, current)
                current.pop()

        backtrack(0, [])
        return result

    @staticmethod
    def generate_parenthesis(n: int) -> List[str]:
        """Menghasilkan semua kombinasi parentheses valid untuk n pasang"""
        result = []

        def backtrack(open_count: int, close_count: int, current: List[str]):
            if open_count == close_count == n:
                result.append(''.join(current))
                return

            if open_count < n:
                current.append('(')
                backtrack(open_count + 1, close_count, current)
                current.pop()

            if close_count < open_count:
                current.append(')')
                backtrack(open_count, close_count + 1, current)
                current.pop()

        backtrack(0, 0, [])
        return result

# Contoh penggunaan
print("=== N-Queens (4) ===")
print(f"Jumlah solusi: {len(Backtracking.n_queens(4))}")

print("\n=== Subsets dari [1,2,3] ===")
print(Backtracking.subsets([1, 2, 3]))

print("\n=== Combination Sum ===")
print(Backtracking.combination_sum([2, 3, 6, 7], 7))

print("\n=== Letter Combinations '23' ===")
print(Backtracking.letter_combinations("23"))

print("\n=== Generate Parenthesis n=3 ===")
print(Backtracking.generate_parenthesis(3))
```

---

## I. Kompleksitas Backtracking

| Masalah              | Kompleksitas Waktu (Worst) | Kompleksitas Ruang |
| -------------------- | -------------------------- | ------------------ |
| N-Queens             | O(N!)                      | O(N²)              |
| Sudoku               | O(9^(m)) dengan pruning    | O(81)              |
| Subset Sum (brute)   | O(2ⁿ)                      | O(n)               |
| Permutasi (unique)   | O(n × n!)                  | O(n!)              |
| Kombinasi C(n,k)     | O(C(n,k) × k)              | O(k)               |
| Generate Parenthesis | O(4ⁿ / √n) (Catalan)       | O(n)               |
| Letter Combinations  | O(4ⁿ)                      | O(n)               |

### Optimasi Pruning yang Umum

| Teknik Pruning          | Contoh Penerapan                                    |
| ----------------------- | --------------------------------------------------- |
| **Constraint checking** | N-Queens: cek kolom/diagonal sebelum place          |
| **Bound checking**      | Subset Sum: hentikan jika angka > remaining         |
| **Symmetry breaking**   | N-Queens: batasi baris pertama                      |
| **Ordering heuristics** | Sudoku: coba sel dengan pilihan paling sedikit dulu |
| **Memoization**         | Gabungkan dengan DP (DP dengan state)               |

---

## J. Perbandingan Backtracking dengan Teknik Lain

| Aspek         | Brute Force           | Backtracking       | Branch & Bound       | DP                |
| ------------- | --------------------- | ------------------ | -------------------- | ----------------- |
| Pruning       | ❌ Tidak              | ✅ Ya              | ✅ Ya (dengan bound) | ❌ Tidak          |
| Optimal untuk | Solusi eksplisit      | Masalah constraint | Masalah optimasi     | Optimasi/Counting |
| Memori        | Minimal               | Stack rekursi      | Stack + bound info   | Tabel besar       |
| Contoh        | Generate semua subset | N-Queens           | Traveling Salesman   | Knapsack          |

---

## K. Studi Kasus & Latihan

### Latihan Pemahaman

1. **Analisis Pohon Rekursi**  
   Gambarkan pohon rekursi untuk N-Queens N=4. Berapa banyak node yang dipangkas (pruned)?

2. **Identifikasi Masalah**  
   Manakah yang lebih cocok diselesaikan dengan backtracking? Berikan alasan.
   - Mencari rute terpendek dari A ke B (graph berbobot)
   - Menyusun jadwal kuliah tanpa konflik ruang dan waktu
   - Menghitung jumlah cara menaiki tangga dengan langkah 1 atau 2
   - Menyelesaikan puzzle Kakuro (seperti Sudoku)
   - Memilah sampah berdasarkan jenis (klasifikasi)

3. **Constraint Propagation**  
   Mengapa Sudoku solver sering lebih cepat dari N-Queens meskipun ruang pencarian lebih besar?

### Latihan Pemrograman

1. **Rat in a Maze**  
   Diberikan maze N×N dengan dinding (1) dan jalan (0). Tikus ada di (0,0) dan ingin ke (N-1,N-1). Hanya bisa kanan dan bawah. Cari semua jalur yang mungkin.

2. **Palindrome Partitioning**  
   Diberikan string s, partisi s menjadi substring-substring yang semuanya palindrome. Kembalikan semua kemungkinan partisi.
   Contoh: `"aab"` → `[["a","a","b"], ["aa","b"]]`

3. **Word Search**  
   Diberikan grid karakter dan kata, cek apakah kata dapat ditemukan dalam grid (bisa ke kanan, kiri, atas, bawah, tanpa mengulang sel).

4. **Knight's Tour**  
   Tempatkan kuda catur di papan N×N sehingga mengunjungi setiap petak tepat satu kali (knight's tour). Cari satu solusi.

5. **M-Coloring Problem**  
   Diberikan graph tak berarah dan m warna, warnai semua vertex sehingga tidak ada dua vertex bertetangga yang memiliki warna sama. Cari semua kemungkinan pewarnaan.

### Soal Analisis

1. **Kompleksitas N-Queens**  
   Buktikan bahwa jumlah solusi N-Queens < N! / (N/2)! untuk N besar. Mengapa pruning efektif?

2. **Backtracking vs DP**  
   Kapan lebih baik menggunakan DP daripada backtracking? Berikan contoh masalah yang bisa diselesaikan keduanya, lalu bandingkan.

3. **Ordering Heuristics**  
   Pada Sudoku solver, mengapa memilih sel dengan kemungkinan paling sedikit (minimum remaining values) terlebih dahulu mempercepat pencarian?

4. **Optimasi Memori**  
   Sebutkan dan jelaskan teknik optimasi memori untuk backtracking yang dapat mengurangi penggunaan stack rekursi.

5. **Parallel Backtracking**  
   Bagaimana Anda dapat memparalelkan backtracking? Masalah apa yang muncul dalam implementasinya?

---

## L. Aplikasi Dunia Nyata

| Aplikasi                                   | Masalah Backtracking                           |
| ------------------------------------------ | ---------------------------------------------- |
| **Constraint Satisfaction Problems (CSP)** | Penjadwalan, kriptaritmetika                   |
| **Compiler**                               | Parsing (recursive descent parser)             |
| **AI / Game**                              | Puzzle solver (Sudoku, Crossword, Rubik)       |
| **Robotics**                               | Path planning dengan obstacle                  |
| **Bioinformatika**                         | Motif finding, sequence alignment (dengan gap) |
| **Network Security**                       | Graph coloring untuk frequency assignment      |
| **VLSI Design**                            | Routing, placement komponen                    |

---

## M. Kesimpulan

- **Backtracking** = DFS + pruning pada ruang solusi.
- Cocok untuk masalah **CSP (Constraint Satisfaction Problems)**.
- Implementasi dasar: rekursif dengan `make choice` → recurse → `undo choice`.
- **Kunci efisiensi** adalah pruning yang agresif dan ordering heuristics.
- Kompleksitas eksponensial di worst case, tetapi sangat praktis untuk banyak masalah.
- Berbeda dengan DP: DP untuk overlapping subproblems & optimasi, backtracking untuk constraint satisfaction & pencarian semua solusi.

---

## N. Referensi

1. Cormen, T.H., Leiserson, C.E., Rivest, R.L., & Stein, C. (2009). _Introduction to Algorithms_, 3rd ed. MIT Press. (Chapter 5 - Probabilistic Analysis, Backtracking di latihan)
2. Brassard, G., & Bratley, P. (1996). _Fundamentals of Algorithmics_. Prentice Hall.
3. Skiena, S.S. (2008). _The Algorithm Design Manual_, 2nd ed. Springer. (Chapter 7 - Backtracking)
4. Russell, S., & Norvig, P. (2020). _Artificial Intelligence: A Modern Approach_, 4th ed. Pearson. (CSP & Backtracking)
