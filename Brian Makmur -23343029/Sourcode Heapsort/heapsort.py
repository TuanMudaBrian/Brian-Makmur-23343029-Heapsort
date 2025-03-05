def susun_heap(A, n, i):
    terbesar = i
    kiri = 2 * i + 1
    kanan = 2 * i + 2

    if kiri < n and A[kiri] > A[terbesar]:
        terbesar = kiri
    if kanan < n and A[kanan] > A[terbesar]:
        terbesar = kanan
    if terbesar != i:
        A[i], A[terbesar] = A[terbesar], A[i]
        susun_heap(A, n, terbesar)


def pengurutan_heap(A):
    n = len(A)
    # Tahap 1: Konstruksi Heap
    for i in range(n // 2 - 1, -1, -1):
        susun_heap(A, n, i)
    # Tahap 2: Penghapusan Maksimum Berulang
    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        susun_heap(A, i, 0)


A = [12, 11, 13, 5, 6, 7]
pengurutan_heap(A)
print(A)
