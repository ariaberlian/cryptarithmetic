from time import time

def permutasi(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]
    l = []
    for i in range(len(arr)):
        N = arr[i]
        sisa = arr[:i] + arr[i+1:]
        for p in permutasi(sisa):
            l.append([N] + p)
    return l

def nilai(kata, dict):
    total = 0
    s = 1
    balikin = kata[::-1]
    for i in range(len(balikin)):
        total += dict[balikin[i]] * s
        s *= 10
    return total

def print_solusi(solusi):
    n = len(solusi)
    for i in range(n-2):
        print(solusi[i])
    print("{} +".format(solusi[n-2]))
    print("---------")
    print(solusi[n-1])

soal = input("Masukkan nama file lengkap dengan direktorinya: ")

f = open(soal, "r")
isi = f.read()
data = isi.split("\n")
idxMax = len(data) - 1
data.pop(idxMax - 1)


for i in range(idxMax):
    data[i] = data[i].replace("+", " ").strip() #Bersihin data
    data[i] = list(data[i])
    
f.close()

start = time()  # Mulai hitung waktu

angka = list(range(10))   #Kemungkinan angka: 0-9

# Semua huruf yang ada dalam string
char_list = []
for i in range(idxMax):
    n = len(data[i])
    for j in range(n):
        char_list.append(data[i][j])
char_list = list(set(char_list))

coba = 0  # Menghitung jumlah percobaan

for tes in permutasi(angka):
    char_dict = dict(zip(char_list, tes[::-1]))  # {char:angka}

    nol = 0
    for i in range(len(data)):
        if(char_dict[data[i][0]] == 0) :
            nol += 1
    if nol != 0:
        continue

    else:
        hasil = 0
        jawaban = []

        for i in range(len(data)-1):
            hasil += nilai(data[i],char_dict)
            jawaban.append(nilai(data[i],char_dict))

        if (hasil == nilai(data[-1], char_dict)):
            jawaban.append(nilai(data[-1], char_dict))
            end = time()
            print(isi)
            print()
            print_solusi(jawaban)
            print()
            print("Jumlah percobaan :", coba)
            print("Waktu yang dibutuhkan :", end-start,"detik")
            break
    coba += 1




