# MODUL ALGORITMA: DYNAMIC PROGRAMMING (DP)

**Kode & Nama Mata Kuliah** : Desain dan Analisis Algoritma / Algoritma Lanjut  
**Semester** : 3-4  
**Durasi** : 4 x 50 menit

## Capaian Pembelajaran

Setelah mempelajari modul ini, mahasiswa mampu:

1. Menjelaskan konsep dan prinsip Dynamic Programming.
2. Mengidentifikasi masalah yang dapat diselesaikan dengan DP (optimal substructure & overlapping subproblems).
3. Membedakan pendekatan top-down (memoization) dan bottom-up (tabulation).
4. Mengimplementasikan solusi DP untuk masalah klasik (Fibonacci, Knapsack, LCS, Coin Change).
5. Menganalisis kompleksitas waktu dan ruang solusi DP.

---

## A. Konsep Dasar Dynamic Programming

**Dynamic Programming (DP)** adalah metode pemecahan masalah dengan cara memecah masalah besar menjadi **submasalah yang lebih kecil**, menyimpan hasil submasalah yang sudah dihitung, dan menggunakan kembali hasil tersebut untuk menghindari perhitungan berulang.

### Prinsip Utama DP

| Prinsip                     | Penjelasan                                                               |
| --------------------------- | ------------------------------------------------------------------------ |
| **Optimal Substructure**    | Solusi optimal masalah dapat dibangun dari solusi optimal submasalahnya. |
| **Overlapping Subproblems** | Submasalah yang sama muncul berkali-kali saat rekursi.                   |

> **Perbedaan dengan Divide and Conquer (seperti Merge Sort)**:  
> D&C membagi masalah menjadi submasalah yang _independen_ (tidak tumpang tindih).  
> DP menangani submasalah yang _tumpang tindih_ (overlapping).

### Kapan Menggunakan DP?

- Masalah dapat didekomposisi menjadi submasalah yang lebih kecil.
- Submasalah yang sama muncul berulang kali.
- Masalah memiliki struktur optimal (optimal substructure).
- Biasanya masalah **optimasi** (maksimum/minimum) atau **penghitungan** (jumlah cara).

---

## B. Dua Pendekatan DP

### 1. Top-Down (Memoization)

- Mulai dari masalah besar, pecahkan secara rekursif.
- Simpan hasil setiap submasalah yang sudah dihitung dalam memo (biasanya array/dictionary).
- Cek memo sebelum menghitung ulang.

**Pseudo-code:**

```python
def solve(problem):
    if problem in memo:
        return memo[problem]
    if base_case:
        return base_value
    memo[problem] = combine(solve(sub1), solve(sub2), ...)
    return memo[problem]
```

### 2. Bottom-Up (Tabulation)

- Mulai dari submasalah terkecil (base case).
- Hitung secara iteratif dari bawah ke atas.
- Gunakan tabel (array) untuk menyimpan hasil.

**Pseudo-code:**

```python
def solve(problem):
    dp = array dengan ukuran sesuai masalah
    inisialisasi base case di dp

    for i from smallest to largest:
        dp[i] = combine(dp[sub1], dp[sub2], ...)

    return dp[largest]
```

### Perbandingan Top-Down vs Bottom-Up

| Aspek               | Top-Down (Memoization)                  | Bottom-Up (Tabulation)               |
| ------------------- | --------------------------------------- | ------------------------------------ |
| Pendekatan          | Rekursif                                | Iteratif                             |
| Kemudahan           | Lebih intuitif, mirip rekursi biasa     | Perlu menentukan urutan perhitungan  |
| Memori              | Memori untuk stack rekursi + memo       | Hanya tabel (bisa dioptimasi)        |
| Evaluasi subproblem | Hanya yang diperlukan                   | Semua subproblem dari kecil ke besar |
| Risiko              | Stack overflow untuk input besar        | -                                    |
| Kecepatan           | Sedikit lebih lambat (overhead rekursi) | Lebih cepat (iteratif)               |

---

## C. Contoh Klasik 1: Deret Fibonacci

**Masalah**: Hitung bilangan Fibonacci ke-n, dengan F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2).

### Pendekatan Naif (Rekursif) - JANGAN GUNAKAN

```python
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)
```

**Kompleksitas**: O(2ⁿ) - sangat lambat untuk n besar.

### Solusi DP Top-Down (Memoization)

```python
def fib_top_down(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_top_down(n-1, memo) + fib_top_down(n-2, memo)
    return memo[n]

# Penggunaan
print(fib_top_down(50))  # 12586269025, cepat!
```

### Solusi DP Bottom-Up (Tabulation)

```python
def fib_bottom_up(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

print(fib_bottom_up(50))  # 12586269025
```

### Optimasi Ruang Bottom-Up (Hanya perlu 2 variabel)

```python
def fib_optimized(n):
    if n <= 1:
        return n

    prev2, prev1 = 0, 1
    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr

    return prev1
```

**Kompleksitas**: O(n) waktu, O(1) ruang.

---

## D. Contoh Klasik 2: 0/1 Knapsack

**Masalah**:  
Terdapat N barang, masing-masing dengan berat `weight[i]` dan nilai `value[i]`.  
Tersedia tas dengan kapasitas maksimum `capacity`.  
Setiap barang hanya bisa diambil **0 atau 1 kali**.  
Tentukan nilai maksimum yang dapat diperoleh.

### Rekursi Naif (Tanpa DP)

```
knapsack(i, remaining_capacity) =
    if i == 0 or remaining_capacity == 0: return 0
    if weight[i] > remaining_capacity: return knapsack(i-1, remaining_capacity)
    else: return max(
        knapsack(i-1, remaining_capacity),  # tidak ambil barang i
        value[i] + knapsack(i-1, remaining_capacity - weight[i])  # ambil
    )
```

### Solusi DP Bottom-Up (Tabulation)

```python
def knapsack(weights, values, capacity):
    n = len(weights)

    # dp[i][w] = nilai maksimum dengan i barang pertama dan kapasitas w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] > w:
                # Barang i-1 terlalu berat, tidak bisa diambil
                dp[i][w] = dp[i-1][w]
            else:
                # Pilih maksimum antara tidak ambil atau ambil barang i-1
                dp[i][w] = max(
                    dp[i-1][w],  # tidak ambil
                    values[i-1] + dp[i-1][w - weights[i-1]]  # ambil
                )

    return dp[n][capacity]

# Contoh
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print(knapsack(weights, values, capacity))  # Output: 7 (ambil barang 0 dan 1: 3+4)
```

### Optimasi Ruang (1D Array)

```python
def knapsack_optimized(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        # Iterasi mundur agar tidak menggunakan barang yang sama dua kali
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[capacity]
```

**Kompleksitas**: O(n × capacity) waktu, O(capacity) ruang.

---

## E. Contoh Klasik 3: Longest Common Subsequence (LCS)

**Masalah**:  
Diberikan dua string `text1` dan `text2`, cari panjang **subsequence terpanjang** yang sama.  
Subsequence adalah urutan karakter yang dapat diperoleh dengan menghapus beberapa karakter (tanpa mengubah urutan).

**Contoh**:  
text1 = "ABCBDAB", text2 = "BDCABB" → LCS = "BCAB" atau "BDAB" (panjang 4)

### Rekursi

```
LCS(i, j) = panjang LCS dari text1[0..i-1] dan text2[0..j-1]
Base case: if i == 0 or j == 0: return 0
if text1[i-1] == text2[j-1]: return 1 + LCS(i-1, j-1)
else: return max(LCS(i-1, j), LCS(i, j-1))
```

### Solusi DP Bottom-Up

```python
def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)

    # dp[i][j] = LCS dari text1[:i] dan text2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

# Contoh
print(longest_common_subsequence("ABCBDAB", "BDCABB"))  # Output: 4
```

### Rekonstruksi LCS (Mendapatkan string LCS)

```python
def reconstruct_lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Isi tabel DP
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Rekonstruksi
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i-1] == text2[j-1]:
            lcs.append(text1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))

print(reconstruct_lcs("ABCBDAB", "BDCABB"))  # Output: "BCAB" atau "BDAB"
```

**Kompleksitas**: O(m × n) waktu, O(m × n) ruang (bisa dioptimasi ke O(min(m,n))).

---

## F. Contoh Klasik 4: Coin Change

**Masalah**:  
Diberikan koin dengan denominasi tertentu (array `coins`), dan target jumlah `amount`.  
Tentukan **jumlah cara minimum** koin yang diperlukan untuk mencapai `amount` (setiap koin dapat digunakan tak terbatas).

**Contoh**: coins = [1,2,5], amount = 11 → output: 3 (5+5+1)

### Solusi DP Bottom-Up

```python
def coin_change_min(coins, amount):
    # dp[i] = jumlah koin minimum untuk membentuk jumlah i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 koin untuk jumlah 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Contoh
print(coin_change_min([1, 2, 5], 11))  # Output: 3
print(coin_change_min([2], 3))         # Output: -1 (tidak bisa)
```

### Jumlah Cara (Berapa cara membentuk amount)

```python
def coin_change_ways(coins, amount):
    # dp[i] = jumlah cara membentuk jumlah i
    dp = [0] * (amount + 1)
    dp[0] = 1  # 1 cara: tidak ambil koin apapun

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]

print(coin_change_ways([1, 2, 5], 5))  # Output: 4 (1+1+1+1+1, 1+1+1+2, 1+2+2, 5)
```

**Kompleksitas**: O(n × amount) waktu, O(amount) ruang.

---

## G. Implementasi Lengkap: Kelas DP Utility

```python
from functools import lru_cache
from typing import List, Tuple

class DynamicProgramming:

    @staticmethod
    @lru_cache(maxsize=None)
    def fib(n: int) -> int:
        """Fibonacci dengan lru_cache decorator (top-down)"""
        if n <= 1:
            return n
        return DynamicProgramming.fib(n-1) + DynamicProgramming.fib(n-2)

    @staticmethod
    def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
        """0/1 Knapsack problem"""
        n = len(weights)
        dp = [0] * (capacity + 1)

        for i in range(n):
            for w in range(capacity, weights[i] - 1, -1):
                dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

        return dp[capacity]

    @staticmethod
    def lcs(text1: str, text2: str) -> int:
        """Longest Common Subsequence"""
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(2)]  # hanya 2 baris

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i % 2][j] = 1 + dp[(i-1) % 2][j-1]
                else:
                    dp[i % 2][j] = max(dp[(i-1) % 2][j], dp[i % 2][j-1])

        return dp[m % 2][n]

    @staticmethod
    def coin_change(coins: List[int], amount: int) -> int:
        """Minimum coins to form amount"""
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

    @staticmethod
    def max_subarray_sum(nums: List[int]) -> int:
        """Kadane's Algorithm - Maximum subarray sum"""
        max_ending_here = max_so_far = nums[0]

        for num in nums[1:]:
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far

# Contoh penggunaan
print("Fibonacci(50):", DynamicProgramming.fib(50))
print("Knapsack:", DynamicProgramming.knapsack_01([2,3,4,5], [3,4,5,6], 5))
print("LCS:", DynamicProgramming.lcs("ABCBDAB", "BDCABB"))
print("Coin Change min:", DynamicProgramming.coin_change([1,2,5], 11))
print("Max Subarray:", DynamicProgramming.max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))
```

---

## H. Pola Umum Solusi DP

### Langkah Menyelesaikan Masalah DP

| Langkah | Deskripsi                                                                                              |
| ------- | ------------------------------------------------------------------------------------------------------ |
| **1**   | Identifikasi bahwa masalah memiliki **optimal substructure** dan **overlapping subproblems**.          |
| **2**   | Definisikan **state** (parameter yang membedakan submasalah). Contoh: `dp[i]`, `dp[i][j]`, `dp[i][w]`. |
| **3**   | Tentukan **base case** (kondisi terkecil yang nilainya diketahui).                                     |
| **4**   | Tentukan **recurrence relation** (hubungan antara state dengan state yang lebih kecil).                |
| **5**   | Pilih pendekatan (top-down atau bottom-up).                                                            |
| **6**   | Implementasi dan optimasi ruang jika memungkinkan.                                                     |

### State Umum dalam DP

| Jenis Masalah | State yang Umum Digunakan                                   |
| ------------- | ----------------------------------------------------------- |
| 1D DP         | `dp[i]` = solusi untuk input ukuran i                       |
| 2 String      | `dp[i][j]` = solusi untuk prefix pertama string i dan j     |
| Knapsack      | `dp[i][w]` = solusi dengan i barang pertama dan kapasitas w |
| Grid/Matrix   | `dp[i][j]` = solusi untuk posisi (i,j)                      |
| Interval      | `dp[i][j]` = solusi untuk interval [i,j]                    |
| Bitmask       | `dp[mask]` = solusi untuk subset mask                       |

---

## I. Kompleksitas DP

| Algoritma                   | Kompleksitas Waktu | Kompleksitas Ruang (naif) | Optimasi Ruang |
| --------------------------- | ------------------ | ------------------------- | -------------- |
| Fibonacci                   | O(n)               | O(n)                      | O(1)           |
| 0/1 Knapsack                | O(n × capacity)    | O(n × capacity)           | O(capacity)    |
| LCS                         | O(m × n)           | O(m × n)                  | O(min(m,n))    |
| Coin Change                 | O(n × amount)      | O(amount)                 | O(amount)      |
| Kadane                      | O(n)               | O(1)                      | O(1)           |
| Matrix Chain Multiplication | O(n³)              | O(n²)                     | O(n²)          |
| Edit Distance               | O(m × n)           | O(m × n)                  | O(min(m,n))    |

---

## J. Studi Kasus & Latihan

### Latihan Pemahaman

1. **Identifikasi Masalah DP**  
   Manakah dari masalah berikut yang dapat diselesaikan dengan DP? Jelaskan alasannya.
   - Mencari elemen terbesar dalam array
   - Menghitung bilangan faktorial
   - Mencari jalur terpendek dalam grid (hanya kanan dan bawah)
   - Mencari semua subset dari suatu himpunan
   - Menentukan apakah string merupakan palindrome

2. **Fibonacci**  
   Hitung F(10) menggunakan pendekatan bottom-up. Tunjukkan isi array dp di setiap iterasi.

3. **Knapsack**  
   Barang: (berat=2, nilai=3), (3,4), (4,5), (5,6) dengan kapasitas 7.  
   Tentukan nilai maksimum dan barang apa saja yang diambil.

4. **LCS**  
   text1 = "ABCDGH", text2 = "AEDFHR". Berapa panjang LCS? Sebutkan salah satu LCS-nya.

### Latihan Pemrograman

1. **Climbing Stairs**  
   Anda menaiki tangga dengan n anak tangga. Setiap kali, Anda dapat menaiki 1 atau 2 anak tangga. Berapa banyak cara berbeda untuk sampai ke puncak?  
   _Hint: dp[n] = dp[n-1] + dp[n-2]_

2. **House Robber**  
   Anda adalah perampok. Rumah-rumah di suatu jalan memiliki uang yang tersimpan. Jika Anda merampok dua rumah berdekatan, alarm akan menyala. Berapa uang maksimum yang bisa Anda curi?  
   _Hint: dp[i] = max(dp[i-1], dp[i-2] + nums[i])_

3. **Unique Paths**  
   Robot berada di pojok kiri atas grid m x n. Hanya bisa bergerak kanan atau bawah. Berapa banyak jalur unik untuk mencapai pojok kanan bawah?  
   _Hint: dp[i][j] = dp[i-1][j] + dp[i][j-1]_

4. **Word Break**  
   Diberikan string s dan dictionary wordDict. Return True jika s dapat dipisah menjadi kata-kata yang ada dalam dictionary.  
   Contoh: s = "leetcode", wordDict = ["leet","code"] → True

5. **Longest Palindromic Substring**  
   Diberikan string s, cari panjang substring palindrom terpanjang.  
   _Hint: dp[i][j] = (s[i]==s[j] and dp[i+1][j-1])_

### Soal Analisis

1. Mengapa rekursi naif Fibonacci memiliki kompleksitas O(2ⁿ) tetapi DP-nya O(n)? Jelaskan perbedaannya.

2. Pada 0/1 Knapsack dengan kapasitas besar (misal 10⁹) tetapi jumlah barang kecil (n ≤ 100), apakah pendekatan DP O(n×capacity) masih layak? Alternatif apa?

3. Jelaskan mengapa pada knapsack dengan optimasi 1D array, kita harus iterasi kapasitas dari besar ke kecil (mundur), bukan dari kecil ke besar.

4. Bandingkan penggunaan memoization (@lru_cache) vs tabulation manual. Kapan lebih baik menggunakan masing-masing?

5. Berikan contoh masalah yang memiliki optimal substructure tetapi TIDAK memiliki overlapping subproblems. Apakah DP tetap berguna?

---

## K. Aplikasi Dunia Nyata

| Aplikasi                        | Masalah DP                                                |
| ------------------------------- | --------------------------------------------------------- |
| **Bioinformatika**              | Sequence alignment (LCS, Edit Distance) untuk DNA/protein |
| **Text diff (git diff)**        | Longest Common Subsequence                                |
| **Autocomplete/spell check**    | Edit Distance (Levenshtein)                               |
| **Sistem rekomendasi**          | Knapsack-like (batasan anggaran, nilai maksimum)          |
| **Rute penerbangan murah**      | DP dengan weighted graph (mirip knapsack + graph)         |
| **Image compression**           | DP untuk optimal segmentation                             |
| **Scheduling job**              | Weighted interval scheduling (DP)                         |
| **Natural Language Processing** | Word break, segmentasi kalimat                            |

---

## L. Kesimpulan

- **Dynamic Programming** adalah teknik optimasi untuk masalah dengan **overlapping subproblems** dan **optimal substructure**.
- Dua pendekatan: **Top-Down (memoization)** - rekursif dengan cache, dan **Bottom-Up (tabulation)** - iteratif dari base case.
- DP mengubah eksponensial menjadi polinomial, menghemat waktu secara drastis.
- Identifikasi state, recurrence relation, dan base case adalah kunci solusi DP.
- Optimasi ruang sering memungkinkan untuk mengurangi kompleksitas memori.

---

## M. Referensi

1. Cormen, T.H., Leiserson, C.E., Rivest, R.L., & Stein, C. (2009). _Introduction to Algorithms_, 3rd ed. MIT Press. (Chapter 15 - Dynamic Programming)
2. Kleinberg, J., & Tardos, É. (2005). _Algorithm Design_. Addison-Wesley.
3. Skiena, S.S. (2008). _The Algorithm Design Manual_, 2nd ed. Springer.
4. Neapolitan, R.E. (2015). _Foundations of Algorithms_, 5th ed. Jones & Bartlett.
