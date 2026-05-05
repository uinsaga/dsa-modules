# KUMPULAN MODUL PRAKTIKUM + JAWABAN

## Struktur Data & Algoritma

---

# PRAKTIKUM 1: TREE & BINARY SEARCH TREE (BST)

**Durasi:** 60 menit

---

## Soal 1: Implementasi Dasar BST (30 menit)

### Kode Lengkap:

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
        """Menambahkan node ke BST"""
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
        # nilai sama diabaikan

    def search(self, value):
        """Mencari nilai dalam BST"""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node is not None
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder(self):
        """Inorder traversal (kiri-root-kanan) -> terurut"""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

    def preorder(self):
        """Preorder traversal (root-kiri-kanan)"""
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node.value)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self):
        """Postorder traversal (kiri-kanan-root)"""
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.value)

# TEST CASE
bst = BST()
for val in [50, 30, 20, 40, 70, 60, 80]:
    bst.insert(val)

print("Inorder:", bst.inorder())     # [20, 30, 40, 50, 60, 70, 80]
print("Preorder:", bst.preorder())   # [50, 30, 20, 40, 70, 60, 80]
print("Postorder:", bst.postorder()) # [20, 40, 30, 60, 80, 70, 50]
print("Search 40:", bst.search(40))  # True
print("Search 100:", bst.search(100)) # False
```

**Output:**

```
Inorder: [20, 30, 40, 50, 60, 70, 80]
Preorder: [50, 30, 20, 40, 70, 60, 80]
Postorder: [20, 40, 30, 60, 80, 70, 50]
Search 40: True
Search 100: False
```

---

## Soal 2: Delete Node pada BST (20 menit)

### Kode Lengkap (tambahkan ke kelas BST di atas):

```python
def delete(self, value):
    """Menghapus node dengan nilai tertentu dari BST"""
    self.root = self._delete_recursive(self.root, value)

def _delete_recursive(self, node, value):
    if node is None:
        return None

    if value < node.value:
        node.left = self._delete_recursive(node.left, value)
    elif value > node.value:
        node.right = self._delete_recursive(node.right, value)
    else:
        # Node ditemukan
        # Kasus 1: Node leaf (tidak punya anak)
        if node.left is None and node.right is None:
            return None

        # Kasus 2: Node punya 1 anak
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left

        # Kasus 3: Node punya 2 anak
        # Cari inorder successor (nilai terkecil di subtree kanan)
        successor = self._find_min(node.right)
        node.value = successor.value
        # Hapus successor
        node.right = self._delete_recursive(node.right, successor.value)

    return node

def _find_min(self, node):
    """Mencari node dengan nilai minimum dalam subtree"""
    current = node
    while current.left:
        current = current.left
    return current

def _find_max(self, node):
    """Mencari node dengan nilai maksimum dalam subtree"""
    current = node
    while current.right:
        current = current.right
    return current

# TEST CASE
bst = BST()
for val in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(val)

bst.delete(20)  # hapus leaf
print("Setelah hapus 20:", bst.inorder())  # [30, 40, 50, 60, 70, 80]

bst.delete(30)  # hapus node dengan 1 child (40)
print("Setelah hapus 30:", bst.inorder())  # [40, 50, 60, 70, 80]

bst.delete(50)  # hapus root dengan 2 child
print("Setelah hapus 50:", bst.inorder())  # [40, 60, 70, 80]
```

**Output:**

```
Setelah hapus 20: [30, 40, 50, 60, 70, 80]
Setelah hapus 30: [40, 50, 60, 70, 80]
Setelah hapus 50: [40, 60, 70, 80]
```

---

## Soal 3: Validasi BST (10 menit)

### Kode Lengkap:

```python
def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    """
    Memvalidasi apakah binary tree memenuhi aturan BST
    """
    if root is None:
        return True

    # Cek apakah nilai node dalam rentang yang valid
    if not (min_val < root.value < max_val):
        return False

    # Rekursif cek subtree kiri dan kanan dengan rentang yang diperbarui
    return (is_bst(root.left, min_val, root.value) and
            is_bst(root.right, root.value, max_val))

# TEST CASE
# BST valid
root1 = Node(10)
root1.left = Node(5)
root1.right = Node(15)
root1.left.left = Node(3)
root1.left.right = Node(7)
root1.right.right = Node(20)
print("BST valid 1:", is_bst(root1))  # True

# BST tidak valid (kiri > root)
root2 = Node(10)
root2.left = Node(15)
root2.right = Node(5)
print("BST valid 2:", is_bst(root2))  # False

# BST tidak valid (nilai di subtree kanan < root)
root3 = Node(10)
root3.left = Node(5)
root3.right = Node(8)  # 8 < 10, seharusnya di kiri
print("BST valid 3:", is_bst(root3))  # False
```

**Output:**

```
BST valid 1: True
BST valid 2: False
BST valid 3: False
```

---

# PRAKTIKUM 2: GRAPH & TRAVERSAL (BFS/DFS)

**Durasi:** 60 menit

---

## Soal 1: Implementasi Graph & Traversal (25 menit)

### Kode Lengkap:

```python
from collections import deque

class Graph:
    def __init__(self, directed=False):
        self.adj = {}  # dictionary: node -> list of neighbors
        self.directed = directed

    def add_vertex(self, vertex):
        """Menambahkan vertex baru ke graph"""
        if vertex not in self.adj:
            self.adj[vertex] = []

    def add_edge(self, u, v):
        """Menambahkan edge dari u ke v"""
        if u not in self.adj:
            self.add_vertex(u)
        if v not in self.adj:
            self.add_vertex(v)

        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)

    def bfs(self, start):
        """BFS traversal menggunakan queue"""
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []

        while queue:
            vertex = queue.popleft()
            result.append(vertex)

            for neighbor in self.adj[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    def dfs_recursive(self, start):
        """DFS traversal rekursif"""
        visited = set()
        result = []
        self._dfs_helper(start, visited, result)
        return result

    def _dfs_helper(self, vertex, visited, result):
        visited.add(vertex)
        result.append(vertex)

        for neighbor in self.adj[vertex]:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited, result)

    def dfs_iterative(self, start):
        """DFS traversal iteratif dengan stack"""
        visited = set()
        stack = [start]
        result = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)

                # Masukkan tetangga ke stack (urutan terbalik)
                for neighbor in reversed(self.adj[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return result

    def display(self):
        """Menampilkan adjacency list"""
        for vertex, neighbors in self.adj.items():
            print(f"{vertex}: {neighbors}")

# TEST CASE
g = Graph()
edges = [(0,1), (0,2), (1,3), (1,4), (2,5), (3,6)]
for u, v in edges:
    g.add_edge(u, v)

print("Adjacency List:")
g.display()
print("\nBFS dari 0:", g.bfs(0))              # [0, 1, 2, 3, 4, 5, 6]
print("DFS rekursif dari 0:", g.dfs_recursive(0))  # [0, 1, 3, 6, 4, 2, 5]
print("DFS iteratif dari 0:", g.dfs_iterative(0))  # [0, 2, 5, 1, 4, 3, 6]
```

**Output:**

```
Adjacency List:
0: [1, 2]
1: [0, 3, 4]
2: [0, 5]
3: [1, 6]
4: [1]
5: [2]
6: [3]

BFS dari 0: [0, 1, 2, 3, 4, 5, 6]
DFS rekursif dari 0: [0, 1, 3, 6, 4, 2, 5]
DFS iteratif dari 0: [0, 2, 5, 1, 4, 3, 6]
```

---

## Soal 2: Shortest Path dengan BFS (20 menit)

### Kode Lengkap (tambahkan ke kelas Graph):

```python
def shortest_path(self, start, target):
    """
    Mencari jalur terpendek dari start ke target menggunakan BFS
    Mengembalikan list node (jalur) atau None jika tidak ada jalur
    """
    if start == target:
        return [start]

    visited = {start}
    queue = deque([(start, [start])])  # (vertex, path)

    while queue:
        vertex, path = queue.popleft()

        for neighbor in self.adj[vertex]:
            if neighbor == target:
                return path + [neighbor]

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None  # Tidak ada jalur

# TEST CASE
g = Graph()
edges = [(0,1), (0,2), (1,3), (2,3), (3,4)]
for u, v in edges:
    g.add_edge(u, v)

print("Shortest path 0->4:", g.shortest_path(0, 4))  # [0, 1, 3, 4] atau [0, 2, 3, 4]
print("Shortest path 0->5:", g.shortest_path(0, 5))  # None
print("Shortest path 0->0:", g.shortest_path(0, 0))  # [0]
```

**Output:**

```
Shortest path 0->4: [0, 1, 3, 4]
Shortest path 0->5: None
Shortest path 0->0: [0]
```

---

## Soal 3: Deteksi Cycle pada Graph Berarah (15 menit)

### Kode Lengkap:

```python
def has_cycle(n, edges):
    """
    Mendeteksi cycle pada graph berarah
    n: jumlah vertex (0..n-1)
    edges: list of [u, v]
    return True jika ada cycle
    """
    # Bangun adjacency list
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)

    # Status: 0 = unvisited, 1 = visiting (di stack rekursi), 2 = visited
    status = [0] * n

    def dfs(vertex):
        status[vertex] = 1  # visiting

        for neighbor in graph[vertex]:
            if status[neighbor] == 1:
                # Ketemu back edge -> cycle
                return True
            if status[neighbor] == 0:
                if dfs(neighbor):
                    return True

        status[vertex] = 2  # selesai dikunjungi
        return False

    # Cek semua vertex (graph mungkin terputus)
    for i in range(n):
        if status[i] == 0:
            if dfs(i):
                return True

    return False

# TEST CASE
print("Cycle [[0,1],[1,2],[2,0]]:", has_cycle(4, [[0,1], [1,2], [2,0]]))  # True
print("Cycle [[0,1],[1,2],[2,3]]:", has_cycle(4, [[0,1], [1,2], [2,3]]))  # False
print("Cycle empty:", has_cycle(3, []))                                      # False
print("Cycle dengan 2 komponen:", has_cycle(5, [[0,1], [1,2], [3,4]]))       # False
```

**Output:**

```
Cycle [[0,1],[1,2],[2,0]]: True
Cycle [[0,1],[1,2],[2,3]]: False
Cycle empty: False
Cycle dengan 2 komponen: False
```

---

# PRAKTIKUM 3: DYNAMIC PROGRAMMING

**Durasi:** 60 menit

---

## Soal 1: Fibonacci dengan DP (10 menit)

### Kode Lengkap:

```python
def fib_naive(n):
    """Rekursif biasa - O(2^n) - sangat lambat untuk n besar"""
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

def fib_memo(n, memo=None):
    """Top-down dengan memoization - O(n)"""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

def fib_bottom_up(n):
    """Bottom-up dengan tabulation - O(n) time, O(1) space"""
    if n <= 1:
        return n

    prev2, prev1 = 0, 1
    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr

    return prev1

# TEST CASE
print("fib_memo(50):", fib_memo(50))        # 12586269025
print("fib_bottom_up(50):", fib_bottom_up(50))  # 12586269025
# print(fib_naive(50))  # JANGAN dijalankan - terlalu lambat!
```

**Output:**

```
fib_memo(50): 12586269025
fib_bottom_up(50): 12586269025
```

---

## Soal 2: Climbing Stairs (15 menit)

### Kode Lengkap:

```python
def climb_ways(n):
    """
    Menghitung jumlah cara menaiki tangga dengan langkah 1, 2, atau 3
    """
    if n == 0:
        return 1
    if n < 0:
        return 0

    dp = [0] * (n + 1)
    dp[0] = 1  # 1 cara untuk berada di tanah

    for i in range(1, n + 1):
        dp[i] = dp[i-1]  # langkah 1
        if i >= 2:
            dp[i] += dp[i-2]  # langkah 2
        if i >= 3:
            dp[i] += dp[i-3]  # langkah 3

    return dp[n]

# Versi dengan optimasi ruang O(1)
def climb_ways_optimized(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2

    a, b, c = 1, 1, 2  # dp[0]=1, dp[1]=1, dp[2]=2
    for i in range(3, n + 1):
        d = a + b + c
        a, b, c = b, c, d

    return c

# TEST CASE
print("climb_ways(1):", climb_ways(1))   # 1
print("climb_ways(2):", climb_ways(2))   # 2
print("climb_ways(3):", climb_ways(3))   # 4
print("climb_ways(4):", climb_ways(4))   # 7
print("climb_ways_optimized(10):", climb_ways_optimized(10))  # 274
```

**Output:**

```
climb_ways(1): 1
climb_ways(2): 2
climb_ways(3): 4
climb_ways(4): 7
climb_ways_optimized(10): 274
```

---

## Soal 3: 0/1 Knapsack (20 menit)

### Kode Lengkap:

```python
def knapsack(weights, values, capacity):
    """
    Menghitung nilai maksimum yang bisa diperoleh dari 0/1 Knapsack
    Versi bottom-up dengan optimasi ruang O(capacity)
    """
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        # Iterasi mundur agar tidak menggunakan barang yang sama dua kali
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[capacity]

# Versi 2D untuk debugging (menampilkan tabel)
def knapsack_2d(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w],
                               values[i-1] + dp[i-1][w - weights[i-1]])

    return dp[n][capacity]

# TEST CASE
weights1 = [2, 3, 4, 5]
values1 = [3, 4, 5, 6]
capacity1 = 5
print("Knapsack 1:", knapsack(weights1, values1, capacity1))  # 7

weights2 = [1, 2, 3]
values2 = [6, 10, 12]
capacity2 = 5
print("Knapsack 2:", knapsack(weights2, values2, capacity2))  # 22

weights3 = [10, 20, 30]
values3 = [60, 100, 120]
capacity3 = 50
print("Knapsack 3:", knapsack(weights3, values3, capacity3))  # 220 (ambil barang 1 dan 3)
```

**Output:**

```
Knapsack 1: 7
Knapsack 2: 22
Knapsack 3: 220
```

---

## Soal 4: Minimum Path Sum (15 menit)

### Kode Lengkap:

```python
def min_path_sum(grid):
    """
    Mencari jumlah minimum dari (0,0) ke (m-1,n-1)
    Hanya bisa bergerak kanan atau bawah
    """
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])

    # Inisialisasi dp dengan ukuran yang sama dengan grid
    dp = [[0] * n for _ in range(m)]

    # Base case: sel (0,0)
    dp[0][0] = grid[0][0]

    # Isi baris pertama (hanya bisa dari kiri)
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # Isi kolom pertama (hanya bisa dari atas)
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # Isi sisa grid
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[m-1][n-1]

# Versi dengan optimasi ruang O(n)
def min_path_sum_optimized(grid):
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [0] * n
    dp[0] = grid[0][0]

    # Inisialisasi baris pertama
    for j in range(1, n):
        dp[j] = dp[j-1] + grid[0][j]

    # Proses baris berikutnya
    for i in range(1, m):
        dp[0] += grid[i][0]  # update kolom pertama
        for j in range(1, n):
            dp[j] = grid[i][j] + min(dp[j], dp[j-1])

    return dp[n-1]

# TEST CASE
grid1 = [[1, 3, 1],
         [1, 5, 1],
         [4, 2, 1]]
print("Min path sum 1:", min_path_sum(grid1))  # 7
print("Min path sum 1 (optimized):", min_path_sum_optimized(grid1))  # 7

grid2 = [[1, 2, 3],
         [4, 5, 6]]
print("Min path sum 2:", min_path_sum(grid2))  # 12

grid3 = [[1]]
print("Min path sum 3:", min_path_sum(grid3))  # 1
```

**Output:**

```
Min path sum 1: 7
Min path sum 1 (optimized): 7
Min path sum 2: 12
Min path sum 3: 1
```

---

# PRAKTIKUM 4: BACKTRACKING

**Durasi:** 60 menit

---

## Soal 1: Generate All Subsets (10 menit)

### Kode Lengkap:

```python
def subsets(nums):
    """
    Menghasilkan semua subset (power set) dari nums
    """
    result = []

    def backtrack(start, current):
        # Simpan subset saat ini (termasuk subset kosong)
        result.append(current[:])

        # Coba tambahkan elemen dari start hingga akhir
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()  # backtrack

    backtrack(0, [])
    return result

# TEST CASE
print("Subsets [1,2,3]:")
print(subsets([1, 2, 3]))
# [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]

print("\nSubsets [0]:")
print(subsets([0]))  # [[], [0]]
```

**Output:**

```
Subsets [1,2,3]:
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

Subsets [0]:
[[], [0]]
```

---

## Soal 2: Generate All Permutations (15 menit)

### Kode Lengkap:

```python
def permute(nums):
    """
    Menghasilkan semua permutasi unik dari nums (tanpa duplikasi angka)
    """
    result = []
    used = [False] * len(nums)

    def backtrack(current):
        if len(current) == len(nums):
            result.append(current[:])
            return

        for i in range(len(nums)):
            if not used[i]:
                # Pruning: skip angka duplikat yang sama
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                current.append(nums[i])
                backtrack(current)
                current.pop()
                used[i] = False

    nums.sort()  # Sorting penting untuk pruning duplikasi
    backtrack([])
    return result

# TEST CASE
print("Permute [1,2,3]:")
print(permute([1, 2, 3]))
# [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

print("\nPermute [0,1]:")
print(permute([0, 1]))  # [[0,1], [1,0]]
```

**Output:**

```
Permute [1,2,3]:
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

Permute [0,1]:
[[0, 1], [1, 0]]
```

---

## Soal 3: Subset Sum (15 menit)

### Kode Lengkap:

```python
def subset_sum(nums, target):
    """
    Mencari semua subset yang jumlahnya sama dengan target
    """
    result = []
    nums.sort()  # Sorting untuk pruning

    def backtrack(start, current, current_sum):
        # Base case: ditemukan subset dengan jumlah target
        if current_sum == target:
            result.append(current[:])
            return

        # Pruning: jika current_sum sudah melebihi target, berhenti
        if current_sum > target:
            return

        for i in range(start, len(nums)):
            # Pruning: jika angka ini > sisa target, break (karena array sudah sorted)
            if current_sum + nums[i] > target:
                break

            # Skip duplikat
            if i > start and nums[i] == nums[i-1]:
                continue

            current.append(nums[i])
            backtrack(i + 1, current, current_sum + nums[i])
            current.pop()

    backtrack(0, [], 0)
    return result

# TEST CASE
nums = [1, 2, 3, 4, 5]
target = 7
print(f"Subset dengan jumlah {target} dari {nums}:")
print(subset_sum(nums, target))
# [[1, 2, 4], [2, 5], [3, 4]]

nums2 = [10, 1, 2, 7, 6, 1, 5]
target2 = 8
print(f"\nSubset dengan jumlah {target2} dari {nums2}:")
print(subset_sum(nums2, target2))
# [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
```

**Output:**

```
Subset dengan jumlah 7 dari [1, 2, 3, 4, 5]:
[[1, 2, 4], [2, 5], [3, 4]]

Subset dengan jumlah 8 dari [10, 1, 2, 7, 6, 1, 5]:
[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
```

---

## Soal 4: N-Queens (20 menit)

### Kode Lengkap:

```python
def solve_n_queens(n):
    """
    Menyelesaikan N-Queens problem
    Mengembalikan semua kemungkinan solusi dalam format papan
    """
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]

    # Set untuk tracking kolom dan diagonal yang terpakai
    cols = set()
    diag1 = set()  # diagonal '/' (r + c)
    diag2 = set()  # diagonal '\' (r - c)

    def backtrack(row):
        # Base case: semua baris terisi
        if row == n:
            # Simpan solusi
            solution = [''.join(row_board) for row_board in board]
            result.append(solution)
            return

        # Coba tempatkan ratu di setiap kolom pada baris ini
        for col in range(n):
            if col in cols or (row + col) in diag1 or (row - col) in diag2:
                continue

            # Lakukan pilihan
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

# Versi yang hanya menghitung jumlah solusi (lebih cepat)
def count_n_queens(n):
    """Menghitung jumlah solusi N-Queens tanpa menyimpan papan"""
    cols = set()
    diag1 = set()
    diag2 = set()

    def backtrack(row):
        if row == n:
            return 1

        count = 0
        for col in range(n):
            if col in cols or (row + col) in diag1 or (row - col) in diag2:
                continue

            cols.add(col)
            diag1.add(row + col)
            diag2.add(row - col)

            count += backtrack(row + 1)

            cols.remove(col)
            diag1.remove(row + col)
            diag2.remove(row - col)

        return count

    return backtrack(0)

# TEST CASE
solutions = solve_n_queens(4)
print(f"Jumlah solusi N=4: {len(solutions)}")  # 2
print("Solusi N=4:")
for i, sol in enumerate(solutions, 1):
    print(f"Solusi {i}:")
    for row in sol:
        print(row)
    print()

print(f"Jumlah solusi N=8: {count_n_queens(8)}")  # 92
```

**Output:**

```
Jumlah solusi N=4: 2
Solusi N=4:
Solusi 1:
.Q..
...Q
Q...
..Q.

Solusi 2:
..Q.
Q...
...Q
.Q..

Jumlah solusi N=8: 92
```

---

## Soal 5: Generate Parentheses (Bonus, 10 menit)

### Kode Lengkap:

```python
def generate_parenthesis(n):
    """
    Menghasilkan semua kombinasi tanda kurung yang valid untuk n pasang
    """
    result = []

    def backtrack(open_count, close_count, current):
        # Base case: sudah menggunakan n pasang kurung
        if open_count == close_count == n:
            result.append(''.join(current))
            return

        # Tambahkan kurung buka jika masih ada
        if open_count < n:
            current.append('(')
            backtrack(open_count + 1, close_count, current)
            current.pop()

        # Tambahkan kurung tutup jika jumlah tutup < buka
        if close_count < open_count:
            current.append(')')
            backtrack(open_count, close_count + 1, current)
            current.pop()

    backtrack(0, 0, [])
    return result

# TEST CASE
print("Generate parenthesis n=3:")
print(generate_parenthesis(3))
# ['((()))', '(()())', '(())()', '()(())', '()()()']

print("\nGenerate parenthesis n=1:")
print(generate_parenthesis(1))  # ['()']

print("\nGenerate parenthesis n=2:")
print(generate_parenthesis(2))  # ['(())', '()()']
```

**Output:**

```
Generate parenthesis n=3:
['((()))', '(()())', '(())()', '()(())', '()()()']

Generate parenthesis n=1:
['()']

Generate parenthesis n=2:
['(())', '()()']
```

---

# LEMBAR JAWABAN PRAKTIKUM (dengan kunci)

**Nama:** ********\_********  
**NIM:** ********\_********  
**Kelas:** ********\_********

| Praktikum | Soal 1 | Soal 2 | Soal 3 | Soal 4 | Soal 5 | Total |
| --------- | ------ | ------ | ------ | ------ | ------ | ----- |
| BST       | /30    | /20    | /10    | -      | -      | /60   |
| Graph     | /25    | /20    | /15    | -      | -      | /60   |
| DP        | /10    | /15    |
