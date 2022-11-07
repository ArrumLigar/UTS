print("Nim : 20220801389")
print("Nama : Arrum Ligar")
print("Pilihan:")
print("1. Cappucino")
print("2. Teh")
print("3. Exit")

pilihan_array = ['CAPPUCINO', 'TEH']
ppn = 0.1
pilihan = int(input("masukan pilihan :"))
if pilihan < 3  :
  print("memilih " + pilihan_array[pilihan-1])
  harga = int(input("masukan harga :"))
  harga = harga + (harga*ppn)
  print(harga)
else :
  print("exit program")
    
    
    