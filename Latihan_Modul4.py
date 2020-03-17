#Latihan
#LINEAR SEARCH

##if target in arrayTempatYangDicari:
##    print("targetnya terdapat di array itu.")
##else:
##    print("targetnya tidak terdapat di array itu.")

#Pencarian Lurus di Linked List
##def cariLurus(wadah, target):
##    n = len(wadah)
##    for i in range(n):
##        if wadah[i] == target:
##            return True
##    return False
##
##A = [10,51,2,18,4,31,13,5,23,64,29]
##print(cariLurus(A, 31))
##print(cariLurus(A, 8))

#Pencarian lurus di objek buatan sendiri
class MhsTIF(object):
    def __init__(self, nama, NIM,kota,us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    
c0 = MhsTIF('Ika', 10, 'Sukoharjo', 240000)
c1 = MhsTIF('Budi', 51, 'Sragen', 230000)
c2 = MhsTIF('Ahmad', 2, 'Sukoharjo', 250000)
c3 = MhsTIF('Chandra', 18, 'Sukoharjo', 235000)
c4 = MhsTIF('Eka', 4, 'Boyolali', 240000)
c5 = MhsTIF('Fandi', 31, 'Salatiga', 230000)
c6 = MhsTIF('Deni', 13, 'Klaten', 245000)
c7 = MhsTIF('Galuh', 5, 'Wonogiri', 245000)
c8 = MhsTIF('Janto', 23, 'Klaten', 245000)
c9 = MhsTIF('Hasan', 64, 'Karanganyar', 270000)
c10 = MhsTIF('Khalid', 29, 'Purwodadi', 265000)
Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

#mencetak nama MhsTIF yang beralamat Klaten
target = 'Klaten'
for i in Daftar:
    if i.kotaTinggal == target:
        print(i.nama + ' tinggal di '+ target)

#Mencari data yang memiliki uang sakunya terkecil
def minim(Daftar):
    nama = []
    terkecil = Daftar[0].uangSaku
    for i in Daftar:
        if i.uangSaku < terkecil:
            terkecil = i.uangSaku
            nama.append(i.nama)
    return nama, terkecil
print("Uang terkecil dimiliki oleh", minim(Daftar))

#Mencari data yang memiliki uang sakunya terbesar
def max(Daftar):
    nama = []
    terbesar = Daftar[10].uangSaku
    for i in Daftar:
        if i.uangSaku > terbesar:
            terkecil = i.uangSaku
            nama.append(i.nama)
    return nama, terbesar
print("Uang terbesar dimiliki oleh", max(Daftar)) 

#Mencari MhsTIF yang uang sakunya kurang dari 250ribu
def kurang(Daftar):
    a=[]
    for i in Daftar:
        if i.uangSaku < 250000:
            a.append(i.nama)
    return a
print("Mahasiswa yang memiliki uang kurang dari 250000 adalah", kurang(Daftar))

#Mencari MhsTIF yang uang sakunya lebih dari 250ribu
def lebih(Daftar):
    a=[]
    for i in Daftar:
        if i.uangSaku > 250000:
            a.append(i.nama)
    return a
print("Mahasiswa yang memiliki uang lebih dari 250000 adalah", lebih(Daftar))










#BINARY SEARCH

def binSe(kumpulan, target):
    #mulai dari seluruh runtutan elemen
    low = 0
    high = len(kumpulan) - 1

    #secara berulang belah runtutan itu menjadi separuhnya
    #   sampai targetnya ditemukan
    while low <= high:
        #temukan pertengahan runtut itu
        mid = (high+low) // 2
        #Apakah pertengahanya semua target?
        if kumpulan[mid] == target:
            return True
        #ataukah targetnya di sebelah kirinya?
        elif target < kumpulan[mid]:
            high = mid - 1
        #jika runtutnya tidak bisa dibelah lagi, berarti targetnya tidak ada
        else:
            low = mid + 1
    return False

kumpulan = [2,2,3,5,5,6,9,10,11,12,13,13,14,15,15]
target = 5
print(binSe(kumpulan,target))
kumpulan = [2,2,3,5,5,6,9,10,11,12,13,13,14,15,15]
target = 7
print(binSe(kumpulan,target))

