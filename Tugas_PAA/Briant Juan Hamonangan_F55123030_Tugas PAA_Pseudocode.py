# 1.Bubble sort
BubbleSort(array)
    n = length(array)                  # Mendapatkan panjang array
                                       # Kompleksitas O(1) untuk operasi ini

    for i from 0 to n-1                # Loop pertama (eksternal) berjalan n kali
                                       # Kompleksitas O(n)

        for j from 0 to n-i-2          # Loop kedua (internal) berjalan untuk elemen yang belum terurut
                                       # Iterasi berkurang sebanyak i pada setiap langkah
                                       # Secara total, kompleksitas untuk kedua loop adalah O(n^2)

            if array[j] > array[j+1]   # Membandingkan dua elemen yang berdekatan
                                       # Operasi perbandingan berjalan O(1) pada setiap iterasi

                swap(array[j], array[j+1]) # Menukar elemen jika elemen kiri lebih besar dari elemen kanan
                                           # Operasi swap juga berjalan O(1) per iterasi

    return array                       # Mengembalikan array yang sudah terurut
                                       # Kompleksitas akhir tetap O(n^2)

# 2.Merge sort

Merge(left, right, array)
    i = j = k = 0                       # Menginisialisasi indeks untuk array kiri (i), kanan (j), dan utama (k)
                                        # Operasi ini berjalan O(1)

    while i < length(left) and j < length(right)  # Loop untuk membandingkan elemen kiri dan kanan
                                                  # Operasi ini berjalan O(n) untuk seluruh elemen di array

        if left[i] < right[j]           # Jika elemen kiri lebih kecil dari elemen kanan
            array[k] = left[i]          # Masukkan elemen kiri ke array utama
            i = i + 1                   # Geser indeks kiri
        else
            array[k] = right[j]         # Masukkan elemen kanan ke array utama
            j = j + 1                   # Geser indeks kanan
        k = k + 1                       # Geser indeks array utama

    while i < length(left)              # Menyalin elemen yang tersisa di array kiri
        array[k] = left[i]
        i = i + 1
        k = k + 1

    while j < length(right)             # Menyalin elemen yang tersisa di array kanan
        array[k] = right[j]
        j = j + 1
        k = k + 1
                                        # Operasi penggabungan secara total tetap O(n)

#1.Analisa Bubble Sort
#Bubble Sort adalah algoritma berbasis perbandingan yang melakukan iterasi berulang untuk mengurutkan elemen. 
#Dalam kasus terburuk, ketika array terurut terbalik, setiap elemen dibandingkan dengan semua elemen lainnya,
#menghasilkan kompleksitas O(n2)O(n^2). Pada kasus rata-rata, algoritma ini tetap membutuhkan jumlah iterasi 
#yang serupa karena data acak masih memerlukan banyak perbandingan dan pertukaran, sehingga kompleksitasnya adalah 
#Θ(n2)\Theta(n^2). Namun, dalam kasus terbaik, jika array sudah terurut, algoritma dapat dioptimalkan menggunakan 
#flag untuk mendeteksi bahwa tidak ada elemen yang perlu ditukar. Hal ini mengurangi waktu eksekusi menjadi linear,
#yaitu Θ(n)\Theta(n).

#2.Analisa Merge Sort
#Merge Sort, di sisi lain, menggunakan pendekatan divide-and-conquer dengan membagi array menjadi bagian kecil,
#mengurutkannya secara rekursif, lalu menggabungkannya kembali. Pada setiap level rekursi, proses penggabungan 
#membutuhkan waktu O(n)O(n), dan terdapat log⁡2(n)\log_2(n) level rekursi, menghasilkan kompleksitas total O(nlog⁡n)O(n \log n)
#dalam kasus terburuk. Karena jumlah operasi tidak tergantung pada urutan awal data, kompleksitas rata-rata juga Θ(nlog⁡n)\Theta(n \log n), 
#begitu pula pada kasus terbaik. Hal ini membuat Merge Sort lebih efisien dan konsisten dibandingkan Bubble Sort, terutama untuk data berukuran besar.